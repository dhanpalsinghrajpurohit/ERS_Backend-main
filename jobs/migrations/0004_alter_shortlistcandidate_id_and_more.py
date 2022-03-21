# Generated by Django 4.0.2 on 2022-02-21 09:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0003_shortlistcandidate_is_shortlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlistcandidate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterUniqueTogether(
            name='shortlistcandidate',
            unique_together={('user', 'job')},
        ),
    ]
