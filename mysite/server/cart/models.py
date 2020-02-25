from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.CharField(Product, max_length=100, null=True, blank=True)
    # id = models.IntegerField(primary_key=True, null=False, auto_created=True)
    quantity = models.IntegerField(Product, default=1)
    email = models.CharField(User, max_length=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
