from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.decorators import display, action
from .models import Booking
from core.sms import send_booking_sms_confirmation


@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = (
        "id",
        "customer_name",
        "customer_phone",
        "room_display",
        "check_in",
        "check_out",
        "guests",
        "display_status",
        "created_at",
    )
    list_filter = ("status", "check_in", "check_out", "created_at")
    search_fields = ("customer_name", "customer_phone", "customer_email", "room_name", "room__title")
    list_filter_submit = True
    actions = ["make_confirmed", "make_cancelled"]

    @display(description="Xona")
    def room_display(self, obj):
        return obj.room.title if obj.room else (obj.room_name or "Tanlanmagan")

    @display(
        description="Holati",
        label={
            "confirmed": "success",
            "cancelled": "danger",
            "pending": "warning",
        }
    )
    def display_status(self, obj):
        labels = dict(Booking.STATUS_CHOICES)
        return obj.status, labels.get(obj.status, obj.status)

    @action(description="Tanlangan buyurtmalarni TASDIQLASH")
    def make_confirmed(self, request, queryset):
        count = 0
        for b in queryset:
            b.status = "confirmed"
            b.save()
            send_booking_sms_confirmation(b)
            count += 1
        self.message_user(request, f"{count} ta xona buyurtmasi tasdiqlandi.")

    @action(description="Tanlangan buyurtmalarni BEKOR QILISH")
    def make_cancelled(self, request, queryset):
        count = queryset.update(status="cancelled")
        self.message_user(request, f"{count} ta xona buyurtmasi bekor qilindi.")

    def save_model(self, request, obj, form, change):
        if change and 'status' in form.changed_data and obj.status == 'confirmed':
            send_booking_sms_confirmation(obj)
        super().save_model(request, obj, form, change)
