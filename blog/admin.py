from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display
from .models import Blog


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ("preview_image", "full_name", "created_at")
    list_filter = ("created_at",)
    search_fields = ("full_name", "description")
    ordering = ("-created_at",)
    list_filter_submit = True

    fieldsets = (
        ("Maqola", {
            "fields": ("full_name", "description")
        }),
        ("Rasm", {
            "fields": ("image", "image_url")
        }),
    )

    @display(description="Rasm")
    def preview_image(self, obj):
        img_url = obj.get_display_image()
        return format_html(
            '<img src="{}" style="width: 50px; height: 35px; border-radius: 6px; object-fit: cover; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" />',
            img_url
        )
