from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "max_persons", "size", "view", "bed", "is_featured", "created_at")
    list_filter = ("view", "max_persons", "stars", "is_featured")
    search_fields = ("title", "description", "view")
    list_editable = ("price", "is_featured")
