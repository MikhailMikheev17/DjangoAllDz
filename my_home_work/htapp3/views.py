from datetime import  timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from htapp2.models import Client, Order, Product


def main(request):
    return render(request, "htapp3/main.html")


def about(request):
    return render(request, "htapp3/about.html")


def get_orders_by_client(request):
    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        period = request.POST.get('period')
        unique = request.POST.get('unique')
        kwargs = {'client_id': client_id}
        if period:
            kwargs['period'] = period
        if unique:
            kwargs['unique'] = unique
        return HttpResponseRedirect(reverse('all_client_orders', kwargs=kwargs))
    return render(request, 'htapp3/get_orders_by_client.html')


def all_client_orders(request, **kwargs):
    client_id = kwargs.get('client_id')
    period = kwargs.get('period')
    unique = kwargs.get('unique')
    client = get_object_or_404(Client, pk=client_id)
    if period:
        end_date = timezone.now()
        start_date = end_date - timedelta(days=int(period))
        orders = Order.objects.filter(customer=client, date_ordered__gte=start_date, date_ordered__lte=end_date)
    else:
        orders = Order.objects.filter(customer=client)
    if unique:
        products = Product.objects.filter(order__in=orders).distinct()
    else:
        products = Product.objects.filter(order__in=orders)
    return render(request, 'htapp3/all_client_orders.html',
                  {'unique': unique, 'period': period, 'client': client, 'orders': orders, 'products': products})

# Create your views here.
