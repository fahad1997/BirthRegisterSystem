# Generated by Django 2.2.6 on 2019-12-12 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BirthRegisterSystem', '0003_hospital_upadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AddDistrict', models.CharField(max_length=50)),
            ],
        ),
    ]
