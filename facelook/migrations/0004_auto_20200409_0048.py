# Generated by Django 3.0.4 on 2020-04-08 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facelook', '0003_live_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='live_attendance',
            name='Department',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='live_attendance',
            name='Time',
            field=models.CharField(default='00:48:15', max_length=40),
        ),
    ]
