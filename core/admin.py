from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display
from .models import Service, Testimonial, HotelStat


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ("title", "badge_display", "preview_icon", "action_type", "link_text", "order", "display_active")
    list_editable = ("order",)
    list_filter = ("action_type", "is_active")
    search_fields = ("title", "description", "badge")
    ordering = ("order", "id")

    fieldsets = (
        ("Asosiy ma'lumotlar", {
            "fields": ("title", "badge", "icon", "description", "features")
        }),
        ("Harakat va Tugma", {
            "fields": ("action_type", "link_url", "link_text"),
            "description": "Foydalanuvchi xizmat kartasidagi tugmani bosganda nima sodir bo'lishini belgilang."
        }),
        ("Boshqaruv", {
            "fields": ("order", "is_active")
        }),
    )

    @display(description="Ikonka")
    def preview_icon(self, obj):
        return format_html('<i class="{}" style="font-size: 18px; color: #c19b76;"></i> <span style="font-size: 12px; color: #888;">({})</span>', obj.icon, obj.icon)

    @display(description="Belgi (Badge)")
    def badge_display(self, obj):
        if obj.badge:
            return format_html('<span style="background: #f7f1eb; color: #c19b76; font-weight: 600; padding: 3px 8px; border-radius: 4px; font-size: 11px;">{}</span>', obj.badge)
        return "-"

    @display(description="Faolligi", label={True: "success", False: "danger"})
    def display_active(self, obj):
        return obj.is_active, "Faol" if obj.is_active else "Nofaol"


@admin.register(Testimonial)
class TestimonialAdmin(ModelAdmin):
    list_display = ("preview_image", "name", "role", "rating_display", "order", "display_active", "created_at")
    list_editable = ("order",)
    list_filter = ("is_active", "rating", "created_at")
    search_fields = ("name", "role", "content")
    ordering = ("order", "-created_at")

    @display(description="Rasm")
    def preview_image(self, obj):
        img_url = obj.get_display_image()
        return format_html(
            '<img src="{}" style="width: 38px; height: 38px; border-radius: 50%; object-fit: cover;" />',
            img_url
        )

    @display(description="Reyting")
    def rating_display(self, obj):
        stars = "★" * obj.rating + "☆" * (5 - obj.rating)
        return format_html('<span style="color: #ffb703; font-size: 16px;">{}</span>', stars)

    @display(description="Faolligi", label={True: "success", False: "danger"})
    def display_active(self, obj):
        return obj.is_active, "Faol" if obj.is_active else "Nofaol"


@admin.register(HotelStat)
class HotelStatAdmin(ModelAdmin):
    list_display = ("title", "value", "order", "display_active")
    list_editable = ("value", "order")
    list_filter = ("is_active",)
    search_fields = ("title",)
    ordering = ("order", "id")

    @display(description="Faolligi", label={True: "success", False: "danger"})
    def display_active(self, obj):
        return obj.is_active, "Faol" if obj.is_active else "Nofaol"
