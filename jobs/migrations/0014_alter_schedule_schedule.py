# Generated by Django 4.0.2 on 2022-03-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_alter_schedule_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='schedule',
            field=models.DateField(default=None),
        ),
    ]
