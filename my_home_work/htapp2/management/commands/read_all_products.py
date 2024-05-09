from django.core.management.base import BaseCommand
from htapp2.models import Product


class Command(BaseCommand):
    help = "Get all clients."

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        self.stdout.write(f'{products}')
