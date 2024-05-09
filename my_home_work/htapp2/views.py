import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Client, Product, Order


# Create your views here.
def products(request):
    products_all = Product.objects.all()
    products_list = [
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': str(product.price),
        }
        for product in products_all
    ]
    products_json = json.dumps(products_list)
    return HttpResponse(products_json, content_type='application/json')


def clients(request):
    clients_all = Client.objects.all()
    clients_list = [
        {
            'id': client.id,
            'name': client.name,
            'phone': client.phone,
            'address': client.address
        }
        for client in clients_all
    ]
    clients_json = json.dumps(clients_list)

    return HttpResponse(clients_json, content_type='application/json')


def orders(request):
    orders = Order.objects.all()
    return HttpResponse(orders)
