import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from blog.models import Blog
from contact.models import Contact
from rooms.models import Room
from .models import Service, Testimonial, HotelStat

class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent_blogs"] = Blog.objects.order_by("-created_at")[:4]
        context["rooms"] = Room.objects.filter(is_featured=True)[:6]
        context["services"] = Service.objects.filter(is_active=True)[:6]
        context["testimonials"] = Testimonial.objects.filter(is_active=True)[:6]
        context["stats"] = HotelStat.objects.filter(is_active=True)
        context["all_rooms"] = Room.objects.all()
        return context

class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.filter(is_active=True)[:6]
        context["stats"] = HotelStat.objects.filter(is_active=True)
        context["all_rooms"] = Room.objects.all()
        return context


@require_POST
def service_request_view(request):
    try:
        if request.content_type == "application/json":
            data = json.loads(request.body.decode("utf-8"))
        else:
            data = request.POST

        name = data.get("name", "").strip()
        phone = data.get("phone", "").strip()
        service_type = data.get("service_type", "Xizmat buyurtmasi").strip()
        email = data.get("email", "").strip() or "guest@deluxe.uz"
        notes = data.get("notes", "").strip()
        date = data.get("date", "").strip()
        time = data.get("time", "").strip()
        pickup = data.get("pickup", "").strip()
        car_type = data.get("car_type", "").strip()

        if not name or not phone:
            return JsonResponse({
                "status": "error",
                "message": "Iltimos, ism va telefon raqamingizni kiriting."
            }, status=400)

        details = [f"Xizmat: {service_type}"]
        if pickup:
            details.append(f"Kutib olish/Borish joyi: {pickup}")
        if date or time:
            details.append(f"Sana va vaqt: {date} {time}")
        if car_type:
            details.append(f"Avtomobil toifasi: {car_type}")
        if notes:
            details.append(f"Qo'shimcha izoh: {notes}")

        Contact.objects.create(
            full_name=name,
            phone=phone,
            email=email,
            subject=f"[{service_type}] Buyurtma / Murojaat",
            description="\n".join(details),
        )

        try:
            from .telegram import notify_telegram
            notify_telegram(
                f"🛎 <b>Yangi Xizmat So'rovi ({service_type})!</b>\n\n"
                f"👤 <b>Ism:</b> {name}\n"
                f"📞 <b>Telefon:</b> {phone}\n"
                f"📧 <b>Email:</b> {email or 'Kiritilmagan'}\n"
                f"📋 <b>Tafsilotlar:</b>\n" + "\n".join(details)
            )
        except Exception:
            pass

        return JsonResponse({
            "status": "ok",
            "message": "Buyurtmangiz muvaffaqiyatli qabul qilindi! Menejerimiz tez orada siz bilan bog'lanadi."
        })
    except Exception as e:
        return JsonResponse({"status": "error", "message": "Xatolik yuz berdi: " + str(e)}, status=500)


@require_POST
def submit_testimonial_view(request):
    try:
        name = request.POST.get("name", "").strip()
        role = request.POST.get("role", "").strip() or "Mehmon"
        content = request.POST.get("content", "").strip()
        try:
            rating = int(request.POST.get("rating", 5))
        except (ValueError, TypeError):
            rating = 5
        image = request.FILES.get("image", None)

        if not name or not content:
            return JsonResponse({
                "status": "error",
                "message": "Iltimos, ismingiz va fikringizni kiriting."
            }, status=400)

        rating = max(1, min(5, rating))
        avatar_url = f"https://ui-avatars.com/api/?name={name.replace(' ', '+')}&background=c19b76&color=fff&size=128"

        testimonial = Testimonial.objects.create(
            name=name,
            role=role,
            content=content,
            rating=rating,
            image=image,
            image_url=avatar_url if not image else None,
            is_active=True,
            order=0,
        )

        try:
            from .telegram import notify_telegram
            notify_telegram(
                f"⭐ <b>Yangi Mehmon Fikri (Sayt orqali)!</b>\n\n"
                f"👤 <b>Ism:</b> {name} ({role})\n"
                f"⭐ <b>Reyting:</b> {'★' * rating} ({rating}/5)\n"
                f"💬 <b>Fikr:</b>\n{content}"
            )
        except Exception:
            pass

        return JsonResponse({
            "status": "ok",
            "message": "Katta rahmat! Fikringiz muvaffaqiyatli qabul qilindi va e'lon qilindi.",
            "name": testimonial.name,
            "role": testimonial.role,
            "content": testimonial.content,
            "rating": testimonial.rating,
            "image": testimonial.get_display_image()
        })
    except Exception as e:
        return JsonResponse({"status": "error", "message": "Xatolik yuz berdi: " + str(e)}, status=500)
