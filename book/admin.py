from django.contrib import admin
from .models import Booking
from core.sms import send_booking_sms_confirmation

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "customer_phone", "room", "room_name", "check_in", "check_out", "guests", "status", "created_at")
    list_filter = ("status", "check_in", "check_out", "created_at")
    search_fields = ("customer_name", "customer_phone", "customer_email", "room_name")
    list_editable = ("status",)

    def save_model(self, request, obj, form, change):
        if change and 'status' in form.changed_data and obj.status == 'confirmed':
            send_booking_sms_confirmation(obj)
        super().save_model(request, obj, form, change)
