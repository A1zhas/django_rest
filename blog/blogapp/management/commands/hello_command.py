from django.core.management.base import BaseCommand
from django.conf import settings
import os

# from blogapp.models import Poll

class Command(BaseCommand):
    def handle(self, *args, **options):
        # path = os.path.join(settings.Base_DIR, 'blogapp', 'management', 'my.json')
        # with open(path, 'w') as  f:
        #     pass
        print('Привет')