from django.shortcuts import render
from shop.models import Product
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
import requests
import sqlite3


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})


def img_choose(self, request):
    response = requests.get('http://192.168.88.81:8080/apriori/')
    data = response.json()
    val_list = {}
    for i in range(len(data)):
        val_list[data[i]] = requests.get('http://192.168.88.81:8080/apriori/' + data[i]).json()
    print(val_list)
    # some_value = int(data[0])

    conn = sqlite3.connect('C:\\Users\\Arnav\\PycharmProjects\\ad-retarget\\mysite\\server\\db.sqlite3')
    # conn.row_factory = sqlite3.Row
    c = conn.cursor()
    d = conn.cursor()

    # c.execute("SELECT order_id FROM orders_orderitem where product_id=" + str(some_value) + ";")
    c.execute("SELECT order_id FROM orders_orderitem where product_id= 61;")
    the_id = list(c.fetchone())

    d.execute("SELECT email FROM orders_order where id=" + (str(the_id[0]))+ ";")
    the_email = list(d.fetchone())

    print(the_email)
    print()
    #print(data)
    print(the_id)
    return render(request, 'orders/order/newf.html', {'name': the_id[0], 'email': the_email[0]})
