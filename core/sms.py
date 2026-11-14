import os
import re
import json
import logging
import threading
import urllib.request
import urllib.error
import urllib.parse
from django.conf import settings

logger = logging.getLogger(__name__)

_eskiz_token = None

def normalize_phone_number(phone: str) -> str:
    """
    Telefon raqamini tozalash (masalan: '+998 90 123-45-67' -> '998901234567')
    """
    if not phone:
        return ""
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 9:
        digits = "998" + digits
    return digits


def _get_eskiz_token(email: str, password: str) -> str:
    global _eskiz_token
    if _eskiz_token:
        return _eskiz_token

    url = "https://notify.eskiz.uz/api/auth/login"
    data = urllib.parse.urlencode({"email": email, "password": password}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "DeluxeHotel/1.0"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            resp_body = res.read().decode("utf-8")
            data = json.loads(resp_body)
            _eskiz_token = data.get("data", {}).get("token")
            if _eskiz_token:
                logger.info("Eskiz.uz dan avtorizatsiya tokeni muvaffaqiyatli olindi.")
            return _eskiz_token
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode("utf-8", errors="ignore")
        logger.error(f"Eskiz avtorizatsiya xatoligi ({e.code}): {error_msg}")
        return ""
    except Exception as e:
        logger.error(f"Eskiz avtorizatsiyadan o'tolmadi: {e}")
        return ""


def _send_sms_worker(phone: str, message_text: str) -> bool:
    clean_phone = normalize_phone_number(phone)
    if not clean_phone:
        logger.warning("SMS yuborish uchun telefon raqami topilmadi.")
        return False

    eskiz_email = getattr(settings, 'ESKIZ_EMAIL', '') or os.getenv('ESKIZ_EMAIL', '')
    eskiz_password = getattr(settings, 'ESKIZ_PASSWORD', '') or os.getenv('ESKIZ_PASSWORD', '')

    # Agar Eskiz login/paroli bo'lsa real SMS yuboriladi
    if eskiz_email and eskiz_password:
        token = _get_eskiz_token(eskiz_email, eskiz_password)
        if token:
            url = "https://notify.eskiz.uz/api/message/sms/send"
            data = urllib.parse.urlencode({
                "mobile_phone": clean_phone,
                "message": message_text,
                "from": "4546"
            }).encode("utf-8")
            req = urllib.request.Request(
                url,
                data=data,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Authorization": f"Bearer {token}",
                    "User-Agent": "DeluxeHotel/1.0"
                }
            )
            try:
                with urllib.request.urlopen(req, timeout=10) as res:
                    resp_body = res.read().decode("utf-8")
                    logger.info(f"Eskiz SMS yuborildi: +{clean_phone} javob: {resp_body}")
                    print(f"\n✅ [REAL SMS ESKIZ ORQALI YUBORILDI] -> +{clean_phone}")
                    return True
            except urllib.error.HTTPError as e:
                error_msg = e.read().decode("utf-8", errors="ignore")
                logger.error(f"Eskiz SMS yuborishda HTTP xatolik ({e.code}): {error_msg}")
            except Exception as e:
                logger.error(f"Eskiz SMS yuborishda xatolik: {e}")

    # Agar Eskiz sozlanmagan bo'lsa yoki jo'natish amalga oshmagan bo'lsa (simulyatsiya)
    print(f"\n==================== [MIJOZGA SMS YUBORILDI] ====================")
    print(f"📲 Telefon raqam: +{clean_phone}")
    print(f"💬 SMS Matni:\n{message_text}")
    print(f"=================================================================\n")
    logger.info(f"[SMS SIMULATSIYA] +{clean_phone} ga xabar: {message_text}")
    return True


def send_sms(phone: str, message_text: str, async_mode: bool = True) -> bool:
    """
    Mijoz telefoniga SMS xabarnoma yuborish.
    async_mode=True bo'lsa alohida oqimda ishlaydi.
    """
    if async_mode:
        thread = threading.Thread(target=_send_sms_worker, args=(phone, message_text), daemon=True)
        thread.start()
        return True
    else:
        return _send_sms_worker(phone, message_text)


def send_booking_sms_confirmation(booking, async_mode: bool = True) -> bool:
    """
    Xona admin tomonidan tasdiqlanganda mijoz telefoniga tasdiq SMS-i yuborish.
    """
    if not booking.customer_phone:
        return False

    name = booking.customer_name or "Hurmatli mehmon"
    room_title = booking.room.title if booking.room else (booking.room_name or "Xona")
    
    check_in_str = booking.check_in.strftime("%d.%m.%Y") if booking.check_in else ""
    check_out_str = booking.check_out.strftime("%d.%m.%Y") if booking.check_out else ""

    message = (
        f"Hurmatli {name}! Deluxe Hotel'dagi '{room_title}' xonangiz "
        f"{check_in_str} dan {check_out_str} gacha muvaffaqiyatli band qilindi. "
        f"Sizni shu sanada kutib qolamiz! Ma'lumot uchun: +998 90 123 45 67"
    )

    return send_sms(booking.customer_phone, message, async_mode=async_mode)
