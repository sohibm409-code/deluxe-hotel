from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from unfold.decorators import display
from .models import Room, RoomImage


class RoomImageInline(TabularInline):
    model = RoomImage
    extra = 3
    fields = ("preview_img", "caption", "image", "image_url", "order")
    readonly_fields = ("preview_img",)

    def preview_img(self, obj):
        if obj and obj.id:
            u = obj.get_image_url()
            if u:
                return format_html(
                    '<img src="{}" style="width: 52px; height: 36px; object-fit: cover; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.15);" />',
                    u
                )
        return "-"
    preview_img.short_description = "Ko'rinish"


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
        "images_count",
        "is_featured",
        "created_at",
    )
    list_filter = ("view", "max_persons", "stars", "is_featured")
    search_fields = ("title", "description", "view")
    list_editable = ("is_featured",)
    list_filter_submit = True
    inlines = [RoomImageInline]

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": ("title", "price", "is_featured", "stars")
        }),
        ("Xona xususiyatlari", {
            "fields": ("max_persons", "size", "view", "bed")
        }),
        ("Asosiy Rasm va Tavsif", {
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

    @display(description="Rasmlar soni")
    def images_count(self, obj):
        total = 1 + obj.images.count()
        return f"📸 {total} ta rasm"


@admin.register(RoomImage)
class RoomImageAdmin(ModelAdmin):
    list_display = ("preview_image", "room", "caption", "order", "created_at")
    list_filter = ("room",)
    search_fields = ("caption", "room__title")
    list_editable = ("order",)

    @display(description="Rasm")
    def preview_image(self, obj):
        u = obj.get_image_url()
        if u:
            return format_html(
                '<img src="{}" style="width: 54px; height: 38px; object-fit: cover; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" />',
                u
            )
        return "-"
