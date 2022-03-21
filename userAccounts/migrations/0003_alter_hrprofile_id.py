# Generated by Django 4.0.2 on 2022-02-16 14:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userAccounts', '0002_alter_hrprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrprofile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
