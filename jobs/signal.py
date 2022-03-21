from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail  import send_mail
from django.conf import settings
from .models import ShortlistCandidate,SelectedCandidate


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        profile = ShortlistCandidate.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )
        subject = 'Welcome to Devsearch'
        message = 'We are glad you are here.'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )
