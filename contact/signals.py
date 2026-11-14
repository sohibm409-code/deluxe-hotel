from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact
from core.telegram import send_contact_notification

@receiver(post_save, sender=Contact)
def on_contact_created(sender, instance, created, **kwargs):
    if created:
        send_contact_notification(instance, async_mode=True)
