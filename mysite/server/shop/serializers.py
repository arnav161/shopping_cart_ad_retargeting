from django.contrib.auth.models import User, Group
from shop.models import Product
from cart.models import UserCart
from orders.models import Order, OrderItem
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('url', 'name', 'id', 'image')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('email', 'id')


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = OrderItem
        fields = ('order_id', 'product_id')


class UserCartSerializer(serializers.HyperlinkedIdentityField):
    class Meta:
        model = UserCart
        fields = ('id', 'email')
