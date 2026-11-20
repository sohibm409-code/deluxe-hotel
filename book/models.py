from decimal import Decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from rooms.models import Room


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Kutilmoqda')),
        ('confirmed', _('Tasdiqlangan')),
        ('cancelled', _('Bekor qilingan')),
    ]

    PAYMENT_METHOD_CHOICES = [
        ('cash', _("Naqd to'lov (Mehmonxonada to'lash)")),
        ('uzcard', _("UzCard (Bank kartasi)")),
        ('humo', _("Humo (Bank kartasi)")),
        ('visa_mastercard', _("Visa / MasterCard (Xalqaro karta)")),
        ('payme', _("Payme ilovasi")),
        ('click', _("Click ilovasi")),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('pay_on_arrival', _("Kelganda to'lanadi")),
        ('pending', _("To'lov kutilmoqda")),
        ('paid', _("To'langan")),
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
    
    # To'lov ma'lumotlari
    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_METHOD_CHOICES,
        default='cash',
        verbose_name="To'lov turi"
    )
    payment_status = models.CharField(
        max_length=30,
        choices=PAYMENT_STATUS_CHOICES,
        default='pay_on_arrival',
        verbose_name="To'lov holati"
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        verbose_name="Jami summa ($)"
    )

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

    @property
    def nights_count(self):
        if self.check_in and self.check_out:
            diff = (self.check_out - self.check_in).days
            return max(1, diff)
        return 1

    def calculate_total_price(self):
        if self.room and self.room.price:
            return Decimal(str(self.room.price)) * Decimal(str(self.nights_count))
        return Decimal("0.00")

    def save(self, *args, **kwargs):
        if not self.total_price or self.total_price == Decimal("0.00"):
            calc = self.calculate_total_price()
            if calc > 0:
                self.total_price = calc
        super().save(*args, **kwargs)

    def get_payment_method_icon(self):
        icons = {
            'cash': 'fa-solid fa-money-bill-wave',
            'uzcard': 'fa-solid fa-credit-card',
            'humo': 'fa-solid fa-credit-card',
            'visa_mastercard': 'fa-brands fa-cc-visa',
            'payme': 'fa-solid fa-mobile-screen-button',
            'click': 'fa-solid fa-mobile-screen-button',
        }
        return icons.get(self.payment_method, 'fa-solid fa-wallet')
