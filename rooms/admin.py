from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display
from .models import Room


@admin.register(Room)
class RoomAdmin(ModelAdmin):
    list_display = (
        "preview_image",
        "title",
        "price_display",
        "max_persons",
        "size_display",
        "view",
        "bed",
        "is_featured",
        "created_at",
    )
    list_filter = ("view", "max_persons", "stars", "is_featured")
    search_fields = ("title", "description", "view")
    list_editable = ("is_featured",)
    list_filter_submit = True

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": ("title", "price", "is_featured", "stars")
        }),
        ("Xona xususiyatlari", {
            "fields": ("max_persons", "size", "view", "bed")
        }),
        ("Tavsif va Media", {
            "fields": ("description", "image", "image_url")
        }),
    )

    @display(description="Rasm")
    def preview_image(self, obj):
        img_url = obj.get_display_image()
        return format_html(
            '<img src="{}" style="width: 54px; height: 38px; object-fit: cover; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" />',
            img_url
        )

    @display(description="Narxi (kuniga)")
    def price_display(self, obj):
        return f"${obj.price}"

    @display(description="Maydoni")
    def size_display(self, obj):
        return f"{obj.size} m²"
