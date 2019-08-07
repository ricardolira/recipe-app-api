import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('WAITING FOR DATABASE...')
        db_comm = None
        while not db_comm:
            try:
                db_comm = connections['default']
            except OperationalError:
                self.stdout.write('DATABASE UNAVAILABLE, WAITING 1 SECOND...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('DATABASE AVAILABLE!'))
