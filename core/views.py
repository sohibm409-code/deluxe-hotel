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

        return JsonResponse({
            "status": "ok",
            "message": "Buyurtmangiz muvaffaqiyatli qabul qilindi! Menejerimiz tez orada siz bilan bog'lanadi."
        })
    except Exception as e:
        return JsonResponse({"status": "error", "message": "Xatolik yuz berdi: " + str(e)}, status=500)
