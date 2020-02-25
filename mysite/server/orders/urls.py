from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^newf/$', views.img_choose, name='img_choose'),
]