# Generated by Django 4.0.2 on 2022-02-24 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_selectedcandidate'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortlistcandidate',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
