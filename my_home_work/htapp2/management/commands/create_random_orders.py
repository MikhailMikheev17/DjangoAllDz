import random
from django.core.management.base import BaseCommand
from htapp2.models import Order, Product, Client
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = "Generate random orders, users, and products."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of orders to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        clients = list(Client.objects.all())
        products = list(Product.objects.all())

        start_date = datetime(2023, 4, 1)
        end_date = datetime(2024, 3, 31)

        for _ in range(count):
            client = random.choice(clients)
            products_for_order = random.sample(products, random.randint(1, len(products)))
            total_amount = sum(product.price for product in products_for_order)

            random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))
            random_date = start_date + timedelta(seconds=random_seconds)


            order = Order.objects.create(customer=client, total_amount=total_amount, date_ordered=random_date)
            order.products.add(*products_for_order)
            self.stdout.write(f'Order created: {order.id}')
