from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from unfold.decorators import display, action
from .models import Category, MenuItem, TableReservation


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'order', 'display_active', 'item_count')
    list_editable = ('order',)
    search_fields = ('name',)
    list_filter = ('is_active',)

    @display(description="Faolligi", label={True: "success", False: "danger"})
    def display_active(self, obj):
        return obj.is_active, "Faol" if obj.is_active else "Nofaol"

    @display(description="Taomlar soni")
    def item_count(self, obj):
        return f"{obj.items.count()} ta taom"


@admin.register(MenuItem)
class MenuItemAdmin(ModelAdmin):
    list_display = (
        'preview_image',
        'title',
        'category',
        'price_display',
        'display_featured',
        'display_available',
        'order',
    )
    list_filter = ('category', 'is_available', 'is_featured')
    search_fields = ('title', 'description')
    list_filter_submit = True

    fieldsets = (
        ("Taom ma'lumotlari", {
            "fields": ("title", "category", "price", "order")
        }),
        ("Holati", {
            "fields": ("is_featured", "is_available")
        }),
        ("Tavsif va Media", {
            "fields": ("description", "image", "image_url")
        }),
    )

    @display(description="Rasm")
    def preview_image(self, obj):
        img_url = obj.get_display_image()
        return format_html(
            '<img src="{}" style="width: 50px; height: 36px; object-fit: cover; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" />',
            img_url
        )

    @display(description="Narxi")
    def price_display(self, obj):
        return f"${obj.price}"

    @display(description="Tavsiya etilgan", label={True: "warning", False: "info"})
    def display_featured(self, obj):
        return obj.is_featured, "Ha" if obj.is_featured else "Yo'q"

    @display(description="Mavjud", label={True: "success", False: "danger"})
    def display_available(self, obj):
        return obj.is_available, "Mavjud" if obj.is_available else "Mavjud emas"


@admin.register(TableReservation)
class TableReservationAdmin(ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'customer_phone',
        'reservation_date',
        'reservation_time',
        'guests',
        'display_status',
        'created_at',
    )
    list_filter = ('status', 'reservation_date', 'created_at')
    search_fields = ('customer_name', 'customer_phone', 'customer_email', 'special_requests')
    list_filter_submit = True
    actions = ['make_confirmed', 'make_cancelled']

    fieldsets = (
        ("Mijoz ma'lumotlari", {
            "fields": ("customer_name", "customer_phone", "customer_email")
        }),
        ("Buyurtma tafsilotlari", {
            "fields": ("reservation_date", "reservation_time", "guests", "special_requests")
        }),
        ("Holat", {
            "fields": ("status",)
        }),
    )

    @display(
        description="Holati",
        label={
            "confirmed": "success",
            "cancelled": "danger",
            "pending": "warning",
        }
    )
    def display_status(self, obj):
        labels = dict(TableReservation.STATUS_CHOICES)
        return obj.status, labels.get(obj.status, obj.status)

    @action(description="Tanlanganlarni TASDIQLASH (Confirmed)")
    def make_confirmed(self, request, queryset):
        count = queryset.update(status='confirmed')
        self.message_user(request, f"{count} ta stol buyurtmasi muvaffaqiyatli tasdiqlandi.")

    @action(description="Tanlanganlarni BEKOR QILISH (Cancelled)")
    def make_cancelled(self, request, queryset):
        count = queryset.update(status='cancelled')
        self.message_user(request, f"{count} ta stol buyurtmasi bekor qilindi.")
