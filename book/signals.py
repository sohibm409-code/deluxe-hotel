from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking
from core.telegram import send_booking_notification

@receiver(post_save, sender=Booking)
def on_booking_created(sender, instance, created, **kwargs):
    if created:
        send_booking_notification(instance, async_mode=True)
