from django.core.management.base import BaseCommand
from htapp2.models import Client


class Command(BaseCommand):
    help = "Update client phone by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('address', type=str, help='new  address')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        address = kwargs.get('address')
        client = Client.objects.filter(pk=pk).first()
        client.address = address
        client.save()
        self.stdout.write(f'{client}')
