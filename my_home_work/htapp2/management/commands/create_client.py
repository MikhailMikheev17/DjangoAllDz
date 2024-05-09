from django.core.management.base import BaseCommand

from htapp2.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='Test', email='test@test.com', phone='+7 912 765-56-56', address='2344 ,lane 23 , Moscow')
        client.save()
        self.stdout.write(f'{client}')
