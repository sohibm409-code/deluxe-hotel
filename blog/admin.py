from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("full_name", "created_at")
    list_filter = ("created_at",)
    search_fields = ("full_name", "description")
    ordering = ("-created_at",)
