from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TableReservation
from core.telegram import send_table_reservation_notification


@receiver(post_save, sender=TableReservation)
def on_table_reservation_created(sender, instance, created, **kwargs):
    if created:
        send_table_reservation_notification(instance, async_mode=True)
