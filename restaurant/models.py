from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "Taom kategoriyasi"
        verbose_name_plural = "Taom kategoriyalari"
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Kategoriya"
    )
    title = models.CharField(max_length=150, verbose_name="Taom nomi")
    description = models.TextField(blank=True, verbose_name="Tavsif / Masalliqlar")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Narxi ($)")
    image = models.ImageField(upload_to="menu_images/", blank=True, null=True, verbose_name="Yuklangan rasm")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Tashqi rasm URL")
    is_featured = models.BooleanField(default=False, verbose_name="Tavsiya etilgan (Featured)")
    is_available = models.BooleanField(default=True, verbose_name="Mavjud")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqt")

    class Meta:
        verbose_name = "Menyu taomi"
        verbose_name_plural = "Menyu taomlari"
        ordering = ["order", "-created_at"]

    def __str__(self):
        return f"{self.title} - ${self.price}"

    def get_display_image(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80"


class TableReservation(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Kutilmoqda')),
        ('confirmed', _('Tasdiqlangan')),
        ('cancelled', _('Bekor qilingan')),
    ]

    customer_name = models.CharField(max_length=150, verbose_name="Mijoz ismi")
    customer_phone = models.CharField(max_length=50, verbose_name="Telefon raqami")
    customer_email = models.EmailField(blank=True, verbose_name="Email")
    reservation_date = models.DateField(verbose_name="Tashrif sanasi")
    reservation_time = models.CharField(max_length=30, verbose_name="Tashrif vaqti (masalan, 19:00)")
    guests = models.CharField(max_length=50, default="2 kishi", verbose_name="Mehmonlar soni")
    special_requests = models.TextField(blank=True, verbose_name="Qo'shimcha istaklar / Izoh")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Holati")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Band qilingan vaqt")

    class Meta:
        verbose_name = "Stol band qilish (Reservation)"
        verbose_name_plural = "Stol band qilishlar"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.customer_name} - {self.reservation_date} {self.reservation_time} ({self.guests})"
