# Generated by Django 2.2 on 2019-06-04 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190518_1314'),
        ('cart', '0027_usercart_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercart',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='usercart',
            name='id',
        ),
        migrations.AddField(
            model_name='usercart',
            name='id',
            field=models.ManyToManyField(to='shop.Product'),
        ),
    ]
