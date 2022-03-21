# Generated by Django 4.0.2 on 2022-02-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_alter_shortlistcandidate_is_shortlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlistcandidate',
            name='is_shortlist',
            field=models.CharField(choices=[(1, 'Pending'), (2, 'Reject'), (3, 'Selected')], default='1', max_length=3),
        ),
    ]
