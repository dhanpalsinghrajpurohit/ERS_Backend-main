from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

STATUS = (
    ('1',"Pending"),
    ('2',"Reject"),
    ('3',"Selected")
)
class Jobs(models.Model):
    id = models.AutoField(primary_key=True)
    postBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=225)
    description = models.TextField()
    skills = models.TextField()
    salary = models.IntegerField()
    vacancy = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class Applicant(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE, null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_shortlist = models.CharField(choices=STATUS, max_length=3, default='1')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

class ShortlistCandidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE, null=True,blank=True)
    is_deleted = models.BooleanField(default=False)
    is_shortlist = models.CharField(choices=STATUS,max_length=3,default='1')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("user", "job"),)
    def __str__(self):
        return str(self.user)


class SelectedCandidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user","job"))

    def __str__(self):
        return str(self.user)


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    schedule = models.DateField(default=None)

    def __str__(self):
        return str(self.user)
