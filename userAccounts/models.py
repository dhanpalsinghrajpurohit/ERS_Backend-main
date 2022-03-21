from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class HRProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    company = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user)

EXPERIENCE_YEAR = (
    ('0','FRESHER'),
    ('1', '1'),
    ('2','2'),
    ('3','3+'),
    ('4','5+'),
)

DEGREE_CHOICE = (
    ('0','B.Tech'),
    ('1', 'M.Tech'),
    ('2','MCA'),
    ('3','BCA'),
    ('4','B.Sc'),
    ('5','M.Sc'),
)


class userProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=255,default="no user")
    email = models.EmailField(max_length=255,default="abc@gmail.com")
    contactNumber = models.CharField(max_length=10)
    degree = models.CharField(max_length=6, choices=DEGREE_CHOICE, default='0')
    college = models.CharField(max_length=255)
    experience = models.CharField(max_length=6, choices=EXPERIENCE_YEAR, default='0')
    skills = models.CharField(max_length=255)
    ResumeLink = models.CharField(max_length=255,blank=True)

    def __str__(self):
        return str(self.fullname)
#
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models
# from django.utils import timezone
#

# class UserManager(BaseUserManager):
#
#     def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
#         if not email:
#             raise ValueError('Users must have an email address')
#         now = timezone.now()
#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             is_staff=is_staff,
#             is_active=True,
#             is_superuser=is_superuser,
#             last_login=now,
#             date_joined=now,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_user(self, email=None, password=None, **extra_fields):
#         return self._create_user(email, password, False, False, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         user = self._create_user(email, password, True, True, **extra_fields)
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length=254, unique=True)
#     name = models.CharField(max_length=254, null=True, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     last_login = models.DateTimeField(null=True, blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#
#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = UserManager()
#
#     def get_absolute_url(self):
#         return "/users/%i/" % (self.pk)
#     def get_email(self):
#         return self.email

# -----I will explain this part later. So let's keep it commented for now-------

# class user_type(models.Model):
#     is_teach = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         if self.is_student == True:
#             return User.get_email(self.user) + " - is_student"
#         else:
#             return User.get_email(self.user) + " - is_teacher"

