from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=150, verbose_name="Xona nomi")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi (kuniga)")
    image = models.ImageField(upload_to="room_images/", blank=True, null=True, verbose_name="Rasm")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Tashqi rasm URL manzili")
    max_persons = models.PositiveIntegerField(default=2, verbose_name="Maksimal odam soni")
    size = models.PositiveIntegerField(default=45, verbose_name="Maydoni (m²)")
    view = models.CharField(max_length=100, default="Sea View", verbose_name="Ko'rinish (View)")
    bed = models.PositiveIntegerField(default=1, verbose_name="Krovatlar soni")
    stars = models.PositiveSmallIntegerField(default=5, verbose_name="Yulduzlar reytingi")
    is_featured = models.BooleanField(default=True, verbose_name="Bosh sahifada ko'rsatish")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    class Meta:
        verbose_name = "Xona"
        verbose_name_plural = "Xonalar"
        ordering = ["price"]

    def __str__(self):
        return f"{self.title} - ${self.price}"

    def get_display_image(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=900&q=80"
