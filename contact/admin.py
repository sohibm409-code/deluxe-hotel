from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ("full_name", "phone", "email", "subject", "created_at")
    list_filter = ("created_at",)
    search_fields = ("full_name", "phone", "email", "subject", "description")
    list_filter_submit = True
    readonly_fields = ("full_name", "phone", "email", "subject", "description", "created_at")

    fieldsets = (
        ("Yuboruvchi", {
            "fields": ("full_name", "phone", "email")
        }),
        ("Xabar mazmuni", {
            "fields": ("subject", "description", "created_at")
        }),
    )
