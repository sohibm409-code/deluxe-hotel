from django.db import models


class Room(models.Model):
    title = models.CharField(max_length=150, verbose_name="Xona nomi")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi (kuniga)")
    image = models.ImageField(upload_to="room_images/", blank=True, null=True, verbose_name="Asosiy rasm")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Asosiy rasm URL manzili")
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

    def get_all_images(self):
        """Asosiy rasm va barcha galereya rasmlarini ro'yxat sifatida qaytaradi."""
        img_list = []
        main_img = self.get_display_image()
        if main_img:
            img_list.append({"url": main_img, "caption": f"{self.title} - Asosiy ko'rinish"})

        for gi in self.images.all().order_by("order", "id"):
            u = gi.get_image_url()
            if u and u not in [x["url"] for x in img_list]:
                img_list.append({"url": u, "caption": gi.caption or f"{self.title}"})

        return img_list


class RoomImage(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Xona"
    )
    image = models.ImageField(upload_to="room_gallery/", blank=True, null=True, verbose_name="Yuklangan rasm")
    image_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Tashqi rasm URL manzili")
    caption = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Rasm tavsifi (masalan: Master yotoqxona, Jakuzzi vanna, Balkon manzarasi)"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")

    class Meta:
        verbose_name = "Xona rasmi"
        verbose_name_plural = "Xona galereyasi rasmlari"
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.room.title} - {self.caption or 'Rasm'}"

    def get_image_url(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return ""
