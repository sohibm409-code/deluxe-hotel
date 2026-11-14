from django.contrib import admin
from .models import Service, Testimonial, HotelStat

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("order", "id")

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "rating", "order", "is_active", "created_at")
    list_editable = ("order", "is_active", "rating")
    list_filter = ("is_active", "rating", "created_at")
    search_fields = ("name", "role", "content")
    ordering = ("order", "-created_at")

@admin.register(HotelStat)
class HotelStatAdmin(admin.ModelAdmin):
    list_display = ("title", "value", "order", "is_active")
    list_editable = ("value", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)
    ordering = ("order", "id")
