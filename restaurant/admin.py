from django.contrib import admin
from django.utils.html import format_html
from .models import Category, MenuItem, TableReservation


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active', 'item_count')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)

    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = "Taomlar soni"


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('preview_image', 'title', 'category', 'price', 'is_featured', 'is_available', 'order')
    list_editable = ('price', 'is_featured', 'is_available', 'order')
    list_filter = ('category', 'is_available', 'is_featured')
    search_fields = ('title', 'description')

    def preview_image(self, obj):
        img_url = obj.get_display_image()
        return format_html('<img src="{}" style="width: 48px; height: 36px; object-fit: cover; border-radius: 4px;" />', img_url)
    preview_image.short_description = "Rasm"


@admin.register(TableReservation)
class TableReservationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'customer_phone',
        'reservation_date',
        'reservation_time',
        'guests',
        'status_badge',
        'created_at'
    )
    list_filter = ('status', 'reservation_date', 'created_at')
    search_fields = ('customer_name', 'customer_phone', 'customer_email', 'special_requests')
    actions = ['make_confirmed', 'make_cancelled']

    def status_badge(self, obj):
        colors = {
            'confirmed': '#28a745',
            'cancelled': '#dc3545',
            'pending': '#ffc107',
        }
        color = colors.get(obj.status, '#6c757d')
        text_color = '#000' if obj.status == 'pending' else '#fff'
        label = dict(TableReservation.STATUS_CHOICES).get(obj.status, obj.status)
        return format_html(
            '<span style="background-color: {}; color: {}; padding: 4px 10px; border-radius: 12px; font-weight: bold; font-size: 11px;">{}</span>',
            color, text_color, label
        )
    status_badge.short_description = "Holati"

    @admin.action(description="Tanlanganlarni TASDIQLASH (Confirmed)")
    def make_confirmed(self, request, queryset):
        count = queryset.update(status='confirmed')
        self.message_user(request, f"{count} ta stol buyurtmasi muvaffaqiyatli tasdiqlandi.")

    @admin.action(description="Tanlanganlarni BEKOR QILISH (Cancelled)")
    def make_cancelled(self, request, queryset):
        count = queryset.update(status='cancelled')
        self.message_user(request, f"{count} ta stol buyurtmasi bekor qilindi.")
