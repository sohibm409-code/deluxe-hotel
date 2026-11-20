from django.db import models
from django.utils.translation import gettext_lazy as _

class Blog(models.Model):
    CATEGORY_CHOICES = [
        ('hotels', _("Mehmonxona yangiliklari")),
        ('restaurant', _("Restoran & Taomlar")),
        ('events', _("Tadbirlar & To'ylar")),
        ('tourism', _("Toshkent Bo'ylab Sayohat")),
        ('tips', _("Mehmonlar uchun Maslahatlar")),
    ]

    full_name = models.CharField(max_length=200, verbose_name="Sarlavha")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='hotels', verbose_name="Rukn (Kategoriya)")
    description = models.TextField(verbose_name="Maqola matni")
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True, verbose_name="Yuklangan rasm")
    image_url = models.URLField(max_length=500, null=True, blank=True, verbose_name="Tashqi rasm URL")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name

    def get_display_image(self):
        if self.image:
            return self.image.url
        if self.image_url:
            return self.image_url
        return "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1200&q=80"


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments', verbose_name="Maqola")
    name = models.CharField(max_length=120, verbose_name="Ism")
    email = models.EmailField(verbose_name="Email")
    comment = models.TextField(verbose_name="Izoh matni")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")
    is_approved = models.BooleanField(default=True, verbose_name="Tasdiqlangan")

    class Meta:
        verbose_name = "Blog Izohi"
        verbose_name_plural = "Blog Izohlari"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.blog.full_name}"

