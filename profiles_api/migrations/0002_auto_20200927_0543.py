# Generated by Django 3.1.1 on 2020-09-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]