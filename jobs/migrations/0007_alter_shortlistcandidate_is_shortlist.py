# Generated by Django 4.0.2 on 2022-02-25 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_shortlistcandidate_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlistcandidate',
            name='is_shortlist',
            field=models.CharField(default=1, max_length=3, verbose_name=((1, 'Pending'), (2, 'Reject'), (3, 'Selected'))),
        ),
    ]
