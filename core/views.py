import json
import logging
import urllib.request
import urllib.error
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from blog.models import Blog
from contact.models import Contact
from rooms.models import Room
from .models import Service, Testimonial, HotelStat

logger = logging.getLogger(__name__)

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


@csrf_exempt
def telegram_webhook_view(request):
    """
    Telegram Bot Webhook Controller.
    Render va jonli serverlarda callback (tugmalar) va xabarlarni qabul qiladi.
    """
    if request.method == "POST":
        try:
            body = request.body.decode("utf-8")
            update = json.loads(body)
            logger.info(f"Telegram webhook update: id={update.get('update_id')}")

            # 1. Inline Button Callback (Tasdiqlash / Bekor qilish)
            if "callback_query" in update:
                from .telegram_listener import handle_callback_query
                handle_callback_query(update["callback_query"])

            # 2. Oddiy xabar (/start, /id, /status)
            elif "message" in update:
                msg = update["message"]
                chat_id = msg.get("chat", {}).get("id")
                text = (msg.get("text") or "").strip()
                first_name = msg.get("from", {}).get("first_name", "Mehmon")

                if text.startswith("/start"):
                    from .telegram import send_telegram_message
                    reply = (
                        f"👋 Assalomu alaykum, <b>{first_name}</b>!\n\n"
                        f"🏨 <b>Deluxe Hotel & Resort</b> rasmiy bildirishnoma boti faol ishlamoqda.\n"
                        f"🆔 Sizning Chat ID: <code>{chat_id}</code>\n\n"
                        f"Sayt orqali kelgan barcha yangi xona bronlari, restoran stollari va "
                        f"murojaatlar shu yerga avtomatik yetkaziladi."
                    )
                    send_telegram_message(reply, async_mode=True)
                elif text == "/id":
                    from .telegram import send_telegram_message
                    send_telegram_message(f"🆔 Sizning Chat ID: <code>{chat_id}</code>", async_mode=True)

            return JsonResponse({"ok": True})
        except Exception as e:
            logger.error(f"Telegram webhook xatolik: {e}", exc_info=True)
            return JsonResponse({"ok": False, "error": str(e)}, status=200)

    # GET so'rovi yuborilganda webhook holatini ko'rsatish
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', '')
    masked_token = bot_token[:10] + "..." if bot_token else "Kiritilmagan"
    return JsonResponse({
        "status": "online",
        "service": "Deluxe Hotel Telegram Webhook",
        "bot_token": masked_token,
        "instructions": "Bu URL Telegram Bot API webhook manzili sifatida xizmat qiladi."
    })


def setup_webhook_view(request):
    """
    Telegram Bot Webhookni avtomatik ulash yoki holatini tekshirish.
    Faqat staff user yoki secret kalit bilan ishlaydi.
    """
    secret = request.GET.get("secret", "")
    if not (request.user.is_staff or secret == "deluxe2026"):
        return JsonResponse({"error": "Ruxsat etilmadi. Administrator bo'lishingiz kerak."}, status=403)

    action = request.GET.get("action", "set")
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', '')
    render_url = getattr(settings, 'RENDER_EXTERNAL_URL', '') or "https://deluxe-hotel-y0w8.onrender.com"
    webhook_url = f"{render_url.rstrip('/')}/telegram/webhook/"

    if action == "set":
        url = f"https://api.telegram.org/bot{bot_token}/setWebhook?url={webhook_url}&drop_pending_updates=True"
    elif action == "delete":
        url = f"https://api.telegram.org/bot{bot_token}/deleteWebhook?drop_pending_updates=True"
    else:
        url = f"https://api.telegram.org/bot{bot_token}/getWebhookInfo"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "DeluxeHotel/1.0"})
        with urllib.request.urlopen(req, timeout=15) as res:
            data = json.loads(res.read().decode("utf-8"))
            return JsonResponse({
                "action": action,
                "target_webhook_url": webhook_url,
                "telegram_response": data
            })
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def test_send_telegram_view(request):
    """
    Telegramga xabar borishini sinab ko'rish uchun test view.
    """
    secret = request.GET.get("secret", "")
    if not (request.user.is_staff or secret == "deluxe2026"):
        return JsonResponse({"error": "Ruxsat etilmadi."}, status=403)

    from .telegram import send_telegram_message, _get_credentials
    bot_token, chat_id = _get_credentials()
    
    test_text = (
        "🚀 <b>Deluxe Hotel & Resort — Jonli Test Xabarnomasi!</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "✅ Telegram tizimi internetda va mahalliy serverda 100% muvaffaqiyatli ishga tushirildi!\n"
        f"🤖 Bot Token: <code>{bot_token[:10]}...</code>\n"
        f"👤 Qabul qiluvchi Chat ID: <code>{chat_id}</code>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "Endi saytdagi har bir xona broni va stol buyurtmasi shu yerga keladi."
    )
    success = send_telegram_message(test_text, async_mode=False)
    return JsonResponse({
        "success": success,
        "chat_id": chat_id,
        "message": "Xabar Telegramga muvaffaqiyatli yetkazildi!" if success else "Xabar yuborishda xatolik yuz berdi."
    })


def set_language_view(request):
    """
    Sayt tilini aniq va xavfsiz almashtiruvchi view (UZ, RU, EN).
    GET va POST so'rovlarini qabul qiladi, oldingi sahifani saqlab, yangi til prefiksiga yo'naltiradi.
    """
    from django.http import HttpResponseRedirect
    from django.utils.translation import activate, get_language_from_path, check_for_language
    from django.urls import translate_url

    lang_code = request.POST.get("language") or request.GET.get("language")
    next_url = request.POST.get("next") or request.GET.get("next") or request.META.get("HTTP_REFERER") or "/"

    if lang_code and check_for_language(lang_code):
        curr_lang = get_language_from_path(next_url) or settings.LANGUAGE_CODE
        activate(curr_lang)
        target_url = translate_url(next_url, lang_code)

        response = HttpResponseRedirect(target_url or "/")
        cookie_age = getattr(settings, 'LANGUAGE_COOKIE_AGE', None) or (365 * 24 * 60 * 60)
        response.set_cookie(
            getattr(settings, 'LANGUAGE_COOKIE_NAME', 'django_language'),
            lang_code,
            max_age=cookie_age,
            path=getattr(settings, 'LANGUAGE_COOKIE_PATH', '/'),
            domain=getattr(settings, 'LANGUAGE_COOKIE_DOMAIN', None),
            secure=getattr(settings, 'LANGUAGE_COOKIE_SECURE', False),
            httponly=getattr(settings, 'LANGUAGE_COOKIE_HTTPONLY', False),
            samesite=getattr(settings, 'LANGUAGE_COOKIE_SAMESITE', 'Lax'),
        )
        if hasattr(request, "session"):
            request.session["_language"] = lang_code
        return response

    return HttpResponseRedirect(next_url or "/")


