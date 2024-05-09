from django.core.management.base import BaseCommand
from htapp2.models import Product


class Command(BaseCommand):
    help = "Update product price by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('price', type=float, help='new  price')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        price = kwargs.get('price')
        product = Product.objects.filter(pk=pk).first()
        product.price = price
        product.save()

        self.stdout.write(f'{product}')
