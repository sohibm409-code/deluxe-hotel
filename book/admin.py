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
        "total_price_display",
        "payment_method_display",
        "display_payment_status",
        "display_status",
        "created_at",
    )
    list_filter = (
        "status",
        "payment_method",
        "payment_status",
        "check_in",
        "check_out",
        "created_at",
    )
    search_fields = (
        "customer_name",
        "customer_phone",
        "customer_email",
        "room_name",
        "room__title",
    )
    list_filter_submit = True
    actions = ["make_confirmed", "make_cancelled", "mark_payment_paid", "mark_payment_on_arrival"]

    @display(description="Xona")
    def room_display(self, obj):
        return obj.room.title if obj.room else (obj.room_name or "Tanlanmagan")

    @display(description="Jami summa")
    def total_price_display(self, obj):
        return f"${obj.total_price} ({obj.nights_count} kecha)" if obj.total_price else "$0.00"

    @display(description="To'lov turi")
    def payment_method_display(self, obj):
        return obj.get_payment_method_display()

    @display(
        description="To'lov holati",
        label={
            "paid": "success",
            "pending": "warning",
            "pay_on_arrival": "info",
        }
    )
    def display_payment_status(self, obj):
        labels = dict(Booking.PAYMENT_STATUS_CHOICES)
        return obj.payment_status, labels.get(obj.payment_status, obj.payment_status)

    @display(
        description="Bron holati",
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

    @action(description="To'lovni TO'LANGAN deb belgilash")
    def mark_payment_paid(self, request, queryset):
        count = queryset.update(payment_status="paid")
        self.message_user(request, f"{count} ta buyurtma to'langan deb belgilandi.")

    @action(description="To'lovni KELGANDA TO'LANADI deb belgilash")
    def mark_payment_on_arrival(self, request, queryset):
        count = queryset.update(payment_status="pay_on_arrival")
        self.message_user(request, f"{count} ta buyurtma kelganda to'lanadi deb belgilandi.")

    def save_model(self, request, obj, form, change):
        if change and 'status' in form.changed_data and obj.status == 'confirmed':
            send_booking_sms_confirmation(obj)
        super().save_model(request, obj, form, change)
