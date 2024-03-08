# yourapp/management/commands/autocollectstatic.py
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Automatically run collectstatic on image upload"

    def handle(self, *args, **options):
        call_command('collectstatic', interactive=False)
