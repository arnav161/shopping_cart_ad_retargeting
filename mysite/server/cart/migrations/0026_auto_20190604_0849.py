# Generated by Django 2.2 on 2019-06-04 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0025_auto_20190604_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]