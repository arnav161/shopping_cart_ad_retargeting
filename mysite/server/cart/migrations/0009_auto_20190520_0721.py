# Generated by Django 2.2 on 2019-05-20 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_auto_20190520_0650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercart',
            old_name='products',
            new_name='product',
        ),
    ]