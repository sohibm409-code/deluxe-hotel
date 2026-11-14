from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Category, MenuItem, TableReservation
from .forms import TableReservationForm


class RestaurantView(View):
    template_name = 'restaurant/restaurant.html'

    def get_context_data(self, form=None):
        categories = Category.objects.filter(is_active=True).prefetch_related('items')
        menu_items = MenuItem.objects.filter(is_available=True).select_related('category')
        if form is None:
            form = TableReservationForm()
        return {
            'categories': categories,
            'menu_items': menu_items,
            'reservation_form': form,
        }

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = TableReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()

            # Telegram notification
            try:
                from core.telegram import notify_telegram
                notify_telegram(
                    f"🍽 <b>Yangi Stol Band Qilindi!</b>\n\n"
                    f"👤 <b>Mijoz:</b> {reservation.customer_name}\n"
                    f"📞 <b>Telefon:</b> {reservation.customer_phone}\n"
                    f"📅 <b>Sana va Vaqt:</b> {reservation.reservation_date} {reservation.reservation_time}\n"
                    f"👥 <b>Mehmonlar soni:</b> {reservation.guests} kishi\n"
                    f"💬 <b>Istaklar:</b> {reservation.special_requests or 'Yo\'q'}"
                )
            except Exception:
                pass

            messages.success(
                request,
                f"Hurmatli {reservation.customer_name}, stol band qilish so'rovingiz muvaffaqiyatli qabul qilindi! "
                f"Administratorimiz tez orada siz bilan bog'lanadi."
            )
            return redirect('restaurant:index')
        else:
            for field, errors in form.errors.items():
                for err in errors:
                    messages.error(request, f"{err}")
            context = self.get_context_data(form=form)
            return render(request, self.template_name, context)
