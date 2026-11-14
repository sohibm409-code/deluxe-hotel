from django.db import models
from rooms.models import Room

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Kutilmoqda'),
        ('confirmed', 'Tasdiqlangan'),
        ('cancelled', 'Bekor qilingan'),
    ]

    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name="bookings", verbose_name="Xona")
    room_name = models.CharField(max_length=150, blank=True, verbose_name="Xona turi / nomi")
    check_in = models.DateField(verbose_name="Kelish sanasi (Check-in)")
    check_out = models.DateField(verbose_name="Ketish sanasi (Check-out)")
    guests = models.CharField(max_length=50, default="1 Adult", verbose_name="Mehmonlar soni")
    customer_name = models.CharField(max_length=150, blank=True, verbose_name="Mijoz ismi")
    customer_phone = models.CharField(max_length=50, blank=True, verbose_name="Telefon raqami")
    customer_email = models.EmailField(blank=True, verbose_name="Email")
    notes = models.TextField(blank=True, verbose_name="Qo'shimcha izoh")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Band qilingan vaqt")

    class Meta:
        verbose_name = "Band qilish (Bron)"
        verbose_name_plural = "Band qilinganlar (Bronlar)"
        ordering = ["-created_at"]

    def __str__(self):
        name = self.customer_name or "Mehmon"
        room = self.room.title if self.room else self.room_name or "Noma'lum xona"
        return f"{name} - {room} ({self.check_in} -> {self.check_out})"
