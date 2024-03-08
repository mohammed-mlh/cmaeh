# yourapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Product
from config.models import Config
from django.core.management import call_command

@receiver(post_save, sender=Product)
@receiver(post_save, sender=Config)
def run_collectstatic(sender, instance, created, **kwargs):
  if created:  # Only run on creation of new instance
      call_command('collectstatic', interactive=False)
