from django.core.management.base import BaseCommand
from htapp2.models import Product


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        product = Product(name='Tv', description='television', price=54.55, quantity=2)
        product.save()
        self.stdout.write(f'{product}')
