# Generated by Django 2.2 on 2019-06-04 02:39

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0022_auto_20190520_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercart',
            name='total',
        ),
        migrations.AddField(
            model_name='usercart',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]
