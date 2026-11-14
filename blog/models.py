from django.db import models

class Blog(models.Model):
    full_name = models.CharField(max_length=200, verbose_name="Sarlavha")
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
