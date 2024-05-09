from django.core.management.base import BaseCommand
from htapp2.models import Client


class Command(BaseCommand):
    help = "Update client phone by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('phone', type=str, help='new  phone number')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        phone = kwargs.get('phone')
        client = Client.objects.filter(pk=pk).first()
        client.phone = phone
        client.save()
        self.stdout.write(f'{client}')
