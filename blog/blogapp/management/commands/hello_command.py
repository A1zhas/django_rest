from django.core.management.base import BaseCommand

# from blogapp.models import Poll

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Привет')