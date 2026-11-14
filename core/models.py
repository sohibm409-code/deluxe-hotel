from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name="Xizmat nomi")
    description = models.TextField(verbose_name="Tavsif")
    icon = models.CharField(
        max_length=100,
        default="fa-regular fa-clock",
        verbose_name="Ikonka (FontAwesome)",
        help_text="Masalan: fa-regular fa-clock, fa-solid fa-champagne-glasses, fa-solid fa-car-side, fa-solid fa-water-ladder"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "Xizmat"
        verbose_name_plural = "Xizmatlar"
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=150, verbose_name="Mehmon / Mijoz ismi")
    role = models.CharField(max_length=100, default="Guests", verbose_name="Maqomi (masalan: Guests)")
    content = models.TextField(verbose_name="Fikr / Sharh")
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True, verbose_name="Yuklangan rasm")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Tashqi rasm URL")
    rating = models.PositiveSmallIntegerField(default=5, verbose_name="Reyting (yulduz)")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")

    class Meta:
        verbose_name = "Mijoz fikri (Testimonial)"
        verbose_name_plural = "Mijozlar fikrlari"
        ordering = ["order", "-created_at"]

    def __str__(self):
        return f"{self.name} ({self.role})"

    def get_display_image(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return "https://randomuser.me/api/portraits/men/32.jpg"


class HotelStat(models.Model):
    title = models.CharField(max_length=100, verbose_name="Ko'rsatkich nomi")
    value = models.CharField(max_length=50, verbose_name="Qiymat (masalan: 25K+, 60, 45)")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    is_active = models.BooleanField(default=True, verbose_name="Faol")

    class Meta:
        verbose_name = "Statistika ko'rsatkichi"
        verbose_name_plural = "Statistika ko'rsatkichlari"
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.title}: {self.value}"
