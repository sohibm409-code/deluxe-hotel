from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.utils.dateparse import parse_date
from rooms.models import Room
from .models import Booking
from .forms import BookingForm
from .utils import get_conflicting_booking

class QuickBookingView(View):
    def post(self, request, *args, **kwargs):
        check_in_str = request.POST.get("check_in")
        check_out_str = request.POST.get("check_out")
        room_title = request.POST.get("room")
        guests = request.POST.get("guests", "1 Adult")
        customer_name = request.POST.get("customer_name", "").strip()
        customer_phone = request.POST.get("customer_phone", "").strip()
        customer_email = request.POST.get("customer_email", "").strip()

        check_in = parse_date(check_in_str) if check_in_str else None
        check_out = parse_date(check_out_str) if check_out_str else None

        if not check_in or not check_out:
            messages.error(request, "Iltimos, kelish va ketish sanalarini to'g'ri tanlang.")
            return redirect(request.META.get("HTTP_REFERER", "core:index"))

        if check_out <= check_in:
            messages.error(request, "Ketish sanasi kelish sanasidan keyin bo'lishi kerak.")
            return redirect(request.META.get("HTTP_REFERER", "core:index"))

        if check_in < date.today():
            messages.error(request, "O'tib ketgan sanalarni tanlab bo'lmaydi.")
            return redirect(request.META.get("HTTP_REFERER", "core:index"))

        room = None
        if room_title:
            room = Room.objects.filter(title__icontains=room_title).first()

        if room:
            conflict = get_conflicting_booking(room, check_in, check_out)
            if conflict:
                messages.error(
                    request,
                    f"Kechirasiz, '{room.title}' xonasi {conflict.check_in.strftime('%d.%m.%Y')} dan {conflict.check_out.strftime('%d.%m.%Y')} gacha allaqachon band qilingan! Iltimos, boshqa sanalarni tanlang."
                )
                return redirect(request.META.get("HTTP_REFERER", "core:index"))

        # Agar mijoz telefon raqamini kiritmagan bo'lsa (bosh sahifadagi quick booking),
        # uni to'liq ma'lumotlarni to'ldirish uchun bron sahifasiga yo'naltiramiz:
        if not customer_phone:
            from urllib.parse import urlencode
            params = {
                "check_in": check_in.strftime("%Y-%m-%d"),
                "check_out": check_out.strftime("%Y-%m-%d"),
                "guests": guests,
            }
            if room:
                params["room_id"] = room.id
            elif room_title:
                params["room_name"] = room_title
            
            return redirect(f"/book/create/?{urlencode(params)}")

        payment_method = request.POST.get("payment_method", "cash")

        Booking.objects.create(
            room=room,
            room_name=room_title or (room.title if room else "Noma'lum xona"),
            check_in=check_in,
            check_out=check_out,
            guests=guests,
            customer_name=customer_name or "Mijoz",
            customer_phone=customer_phone,
            customer_email=customer_email,
            payment_method=payment_method
        )

        messages.success(request, "Xonani bron qilish so'rovingiz qabul qilindi! Admin Telegram orqali tasdiqlashi bilanoq xona siz uchun rasman band qilinadi.")
        return redirect(request.META.get("HTTP_REFERER", "core:index"))


class BookingCreateView(View):
    def get(self, request, room_id=None):
        room = None
        initial = {}
        if room_id:
            room = get_object_or_404(Room, pk=room_id)
            initial['room'] = room
            initial['room_name'] = room.title
        elif request.GET.get("room_id"):
            room = Room.objects.filter(pk=request.GET.get("room_id")).first()
            if room:
                initial['room'] = room
                initial['room_name'] = room.title

        if request.GET.get("check_in"):
            initial['check_in'] = request.GET.get("check_in")
        if request.GET.get("check_out"):
            initial['check_out'] = request.GET.get("check_out")
        if request.GET.get("guests"):
            initial['guests'] = request.GET.get("guests")
        if request.GET.get("payment_method"):
            initial['payment_method'] = request.GET.get("payment_method")
        if request.GET.get("room_name") and not room:
            initial['room_name'] = request.GET.get("room_name")

        form = BookingForm(initial=initial)
        all_rooms = Room.objects.all()
        return render(request, "book/booking.html", {"form": form, "room": room, "all_rooms": all_rooms})

    def post(self, request, room_id=None):
        room = None
        data = request.POST.copy()
        if room_id:
            room = get_object_or_404(Room, pk=room_id)
            data['room'] = room.id

        form = BookingForm(data)
        if form.is_valid():
            booking = form.save(commit=False)
            if room:
                booking.room = room
                booking.room_name = room.title
            elif booking.room:
                booking.room_name = booking.room.title
            elif not booking.room_name:
                booking.room_name = "Umumiy buyurtma"
            
            # Booking.save() calculates total_price and signals.py sends Telegram notification
            booking.save()

            messages.success(
                request, 
                "Xonani bron qilish so'rovingiz qabul qilindi! Administratorimiz tez orada siz bilan bog'lanib, buyurtmangizni tasdiqlaydi."
            )
            return redirect("rooms:index")

        all_rooms = Room.objects.all()
        return render(request, "book/booking.html", {"form": form, "room": room, "all_rooms": all_rooms})


class BookingStatusView(View):
    template_name = "book/booking_status.html"

    def get(self, request, *args, **kwargs):
        import re
        from restaurant.models import TableReservation

        phone_query = request.GET.get("phone", "").strip()
        room_bookings = []
        table_reservations = []
        searched = False

        if phone_query:
            searched = True
            digits_only = re.sub(r"\D", "", phone_query)
            last_numbers = digits_only[-7:] if len(digits_only) >= 7 else digits_only

            if last_numbers:
                room_bookings = Booking.objects.filter(
                    customer_phone__icontains=last_numbers
                ).select_related("room").order_by("-created_at")
                table_reservations = TableReservation.objects.filter(
                    customer_phone__icontains=last_numbers
                ).order_by("-created_at")

        return render(
            request,
            self.template_name,
            {
                "phone_query": phone_query,
                "room_bookings": room_bookings,
                "table_reservations": table_reservations,
                "searched": searched,
            }
        )

