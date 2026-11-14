import os
import json
import html
import logging
import threading
import urllib.request
import urllib.error
import time
from django.conf import settings

logger = logging.getLogger(__name__)

def _get_credentials():
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', '') or os.getenv('TELEGRAM_BOT_TOKEN', '')
    chat_id = getattr(settings, 'TELEGRAM_ADMIN_CHAT_ID', '') or os.getenv('TELEGRAM_ADMIN_CHAT_ID', '')
    return bot_token, chat_id


def _send_telegram_worker(text: str, reply_markup: dict = None) -> bool:
    bot_token, chat_id = _get_credentials()
    if not bot_token or not chat_id:
        logger.warning("Telegram Bot Token yoki Admin Chat ID sozlanmagan (.env faylini tekshiring).")
        return False

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    if reply_markup:
        payload["reply_markup"] = reply_markup

    data = json.dumps(payload).encode("utf-8")
    
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(
                url,
                data=data,
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=25) as response:
                if response.status == 200:
                    return True
        except urllib.error.HTTPError as e:
            error_body = e.read().decode('utf-8', errors='ignore')
            logger.error(f"Telegram HTTP Error {e.code} (urinish {attempt}/3): {error_body}")
            if e.code in [400, 401, 403, 404]:
                return False
        except Exception as e:
            logger.warning(f"Telegramga xabar yuborishda xatolik (urinish {attempt}/3): {e}")
            time.sleep(2)

    return False


def send_telegram_message(text: str, reply_markup: dict = None, async_mode: bool = True) -> bool:
    if async_mode:
        thread = threading.Thread(target=_send_telegram_worker, args=(text, reply_markup), daemon=True)
        thread.start()
        return True
    else:
        return _send_telegram_worker(text, reply_markup)


def edit_telegram_message(chat_id: int | str, message_id: int, text: str, reply_markup: dict = None) -> bool:
    bot_token, _ = _get_credentials()
    if not bot_token:
        return False

    url = f"https://api.telegram.org/bot{bot_token}/editMessageText"
    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "parse_mode": "HTML"
    }
    if reply_markup is not None:
        payload["reply_markup"] = reply_markup

    data = json.dumps(payload).encode("utf-8")
    try:
        req = urllib.request.Request(
            url,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=20) as response:
            return response.status == 200
    except Exception as e:
        logger.error(f"Telegram xabarni tahrirlashda xatolik: {e}")
        return False


def answer_callback_query(callback_query_id: str, text: str = None, show_alert: bool = False) -> bool:
    bot_token, _ = _get_credentials()
    if not bot_token:
        return False

    url = f"https://api.telegram.org/bot{bot_token}/answerCallbackQuery"
    payload = {"callback_query_id": callback_query_id}
    if text:
        payload["text"] = text
        payload["show_alert"] = show_alert

    data = json.dumps(payload).encode("utf-8")
    try:
        req = urllib.request.Request(
            url,
            data=data,
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status == 200
    except Exception as e:
        logger.error(f"Telegram answerCallbackQuery xatolik: {e}")
        return False


def build_booking_message(booking) -> tuple[str, dict]:
    """
    Booking holatiga qarab xabar matni va tugmalarni shakllantirish.
    """
    room_title = booking.room.title if booking.room else (booking.room_name or "Umumiy buyurtma (Xona tanlanmagan)")
    customer_name = html.escape(booking.customer_name or "Ko'rsatilmagan")
    phone = html.escape(booking.customer_phone or "Ko'rsatilmagan")
    email = html.escape(booking.customer_email or "Ko'rsatilmagan")
    room_name = html.escape(room_title)
    guests = html.escape(str(booking.guests or "1"))
    notes = html.escape(booking.notes or "Mavjud emas")
    
    if booking.created_at:
        created = booking.created_at.strftime("%d.%m.%Y, %H:%M")
    else:
        created = "Hozirgina"

    if booking.status == 'confirmed':
        status_line = "🟢 <b>HOLATI: TASDIQLANDI (XONA BAND QILINDI)</b> ✅"
        buttons = [
            [{"text": "❌ Bekor qilish", "callback_data": f"cancel_{booking.id}"}]
        ]
    elif booking.status == 'cancelled':
        status_line = "🔴 <b>HOLATI: BEKOR QILINDI (XONA BO'SH)</b> ❌"
        buttons = [
            [{"text": "✅ Qayta tasdiqlash", "callback_data": f"confirm_{booking.id}"}]
        ]
    else:
        status_line = "🟡 <b>HOLATI: KUTILMOQDA (Admin tasdig'i kerak)</b>"
        buttons = [
            [
                {"text": "✅ Tasdiqlash (Band qilish)", "callback_data": f"confirm_{booking.id}"},
                {"text": "❌ Bekor qilish", "callback_data": f"cancel_{booking.id}"}
            ]
        ]

    reply_markup = {"inline_keyboard": buttons}

    message = (
        "🛎 <b>YANGI XONA BUYURTMASI (BRON)</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"🏨 <b>Xona:</b> {room_name}\n"
        f"👤 <b>Mijoz:</b> {customer_name}\n"
        f"📞 <b>Telefon:</b> {phone}\n"
        f"📧 <b>Email:</b> {email}\n"
        f"📅 <b>Kelish:</b> {booking.check_in}\n"
        f"📅 <b>Ketish:</b> {booking.check_out}\n"
        f"👥 <b>Mehmonlar:</b> {guests}\n"
        f"📝 <b>Izoh:</b> {notes}\n"
        f"⏰ <b>Buyurtma vaqti:</b> {created}\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"{status_line}\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    return message, reply_markup


def send_booking_notification(booking, async_mode: bool = True) -> bool:
    message, reply_markup = build_booking_message(booking)
    return send_telegram_message(message, reply_markup=reply_markup, async_mode=async_mode)


def send_contact_notification(contact, async_mode: bool = True) -> bool:
    name = html.escape(contact.full_name or "Ko'rsatilmagan")
    phone = html.escape(contact.phone or "Ko'rsatilmagan")
    email = html.escape(contact.email or "Ko'rsatilmagan")
    subject = html.escape(contact.subject or "Mavzusiz")
    desc = html.escape(contact.description or "")
    
    if hasattr(contact, 'created_at') and contact.created_at:
        created = contact.created_at.strftime("%d.%m.%Y, %H:%M")
    else:
        created = "Hozirgina"

    message = (
        "📩 <b>YANGI MUROJAAT (CONTACT)</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 <b>Yuboruvchi:</b> {name}\n"
        f"📞 <b>Telefon:</b> {phone}\n"
        f"📧 <b>Email:</b> {email}\n"
        f"📌 <b>Mavzu:</b> {subject}\n"
        f"💬 <b>Xabar:</b>\n{desc}\n\n"
        f"⏰ <b>Vaqt:</b> {created}\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    return send_telegram_message(message, reply_markup=None, async_mode=async_mode)


def build_table_reservation_message(reservation) -> tuple[str, dict]:
    """
    Stol band qilish holatiga qarab xabar matni va inline tugmalarni shakllantirish.
    """
    customer_name = html.escape(reservation.customer_name or "Ko'rsatilmagan")
    phone = html.escape(reservation.customer_phone or "Ko'rsatilmagan")
    email = html.escape(reservation.customer_email or "Ko'rsatilmagan")
    guests = html.escape(str(reservation.guests or "2 kishi"))
    time_str = html.escape(str(reservation.reservation_time or "19:00"))
    requests = html.escape(reservation.special_requests or "Mavjud emas")
    
    if hasattr(reservation, 'created_at') and reservation.created_at:
        created = reservation.created_at.strftime("%d.%m.%Y, %H:%M")
    else:
        created = "Hozirgina"

    if reservation.status == 'confirmed':
        status_line = "🟢 <b>HOLATI: TASDIQLANDI (STOL BAND QILINDI)</b> ✅"
        buttons = [
            [{"text": "❌ Bekor qilish", "callback_data": f"tblcancel_{reservation.id}"}]
        ]
    elif reservation.status == 'cancelled':
        status_line = "🔴 <b>HOLATI: BEKOR QILINDI</b> ❌"
        buttons = [
            [{"text": "✅ Qayta tasdiqlash", "callback_data": f"tblconfirm_{reservation.id}"}]
        ]
    else:
        status_line = "🟡 <b>HOLATI: KUTILMOQDA (Admin tasdig'i kerak)</b>"
        buttons = [
            [
                {"text": "✅ Tasdiqlash", "callback_data": f"tblconfirm_{reservation.id}"},
                {"text": "❌ Bekor qilish", "callback_data": f"tblcancel_{reservation.id}"}
            ]
        ]

    reply_markup = {"inline_keyboard": buttons}

    message = (
        "🍽️ <b>YANGI STOL BUYURTMASI (RESTORAN)</b>\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 <b>Mijoz:</b> {customer_name}\n"
        f"📞 <b>Telefon:</b> {phone}\n"
        f"📧 <b>Email:</b> {email}\n"
        f"📅 <b>Sana:</b> {reservation.reservation_date}\n"
        f"⏰ <b>Vaqt:</b> {time_str}\n"
        f"👥 <b>Mehmonlar:</b> {guests}\n"
        f"📝 <b>Maxsus istaklar:</b> {requests}\n"
        f"⏱️ <b>Buyurtma vaqti:</b> {created}\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"{status_line}\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    return message, reply_markup


def send_table_reservation_notification(reservation, async_mode: bool = True) -> bool:
    message, reply_markup = build_table_reservation_message(reservation)
    return send_telegram_message(message, reply_markup=reply_markup, async_mode=async_mode)


def notify_telegram(text: str, reply_markup: dict = None) -> bool:
    """Convenience alias for sending text notifications."""
    return send_telegram_message(text, reply_markup=reply_markup, async_mode=True)
