# Generated by Django 2.2.6 on 2019-12-04 20:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newchildinfo',
            name='Birth_Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='newchildinfo',
            name='Validation',
            field=models.BooleanField(default=False),
        ),
    ]
