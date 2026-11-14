import json
import logging
import threading
import time
import urllib.request
import urllib.error
from django.conf import settings

logger = logging.getLogger(__name__)

_polling_thread = None
_stop_event = threading.Event()

def handle_callback_query(cq: dict):
    from book.models import Booking
    from restaurant.models import TableReservation
    from book.utils import get_conflicting_booking
    from core.telegram import (
        answer_callback_query,
        edit_telegram_message,
        build_booking_message,
        build_table_reservation_message,
    )
    from core.sms import send_booking_sms_confirmation, normalize_phone_number

    cq_id = cq.get("id")
    data = cq.get("data", "")
    message = cq.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    msg_id = message.get("message_id")
    user = cq.get("from", {})
    admin_name = user.get("first_name", "Admin")

    if not data or not chat_id or not msg_id:
        return

    # Table Reservation callbacks
    if data.startswith("tblconfirm_") or data.startswith("tblcancel_"):
        parts = data.split("_")
        if len(parts) < 2:
            return
        action = parts[0]
        try:
            res_id = int(parts[1])
            reservation = TableReservation.objects.get(id=res_id)
        except (ValueError, TableReservation.DoesNotExist):
            answer_callback_query(cq_id, "❌ Bu stol buyurtmasi bazadan topilmadi!", show_alert=True)
            return

        if action == "tblconfirm":
            reservation.status = "confirmed"
            reservation.save()
            answer_callback_query(cq_id, f"✅ Stol buyurtmasi #{reservation.id} tasdiqlandi!")
            new_text, new_markup = build_table_reservation_message(reservation)
            new_text += f"\n\n👤 <i>Tasdiqladi: {admin_name}</i>"
            edit_telegram_message(chat_id, msg_id, new_text, new_markup)
        elif action == "tblcancel":
            reservation.status = "cancelled"
            reservation.save()
            answer_callback_query(cq_id, f"❌ Stol buyurtmasi #{reservation.id} bekor qilindi.")
            new_text, new_markup = build_table_reservation_message(reservation)
            new_text += f"\n\n👤 <i>Bekor qildi: {admin_name}</i>"
            edit_telegram_message(chat_id, msg_id, new_text, new_markup)
        return

    # Room Booking callbacks
    parts = data.split("_")
    if len(parts) < 2:
        return

    action = parts[0]
    try:
        booking_id = int(parts[1])
    except ValueError:
        return

    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        answer_callback_query(cq_id, "❌ Bu buyurtma bazadan topilmadi!", show_alert=True)
        return

    if action == "confirm":
        # Agar xona belgilangan bo'lsa, oldin tasdiqlangan boshqa buyurtmalar bilan to'qnashuvni tekshirish
        if booking.room:
            conflict = get_conflicting_booking(
                booking.room,
                booking.check_in,
                booking.check_out,
                exclude_booking_id=booking.id
            )
            if conflict:
                alert_text = (
                    f"⚠️ Diqqat: Bu xona ({booking.room.title}) allaqachon boshqa mijoz "
                    f"({conflict.customer_name}) tomonidan {conflict.check_in} dan {conflict.check_out} gacha "
                    f"tasdiqlab qo'yilgan!"
                )
                answer_callback_query(cq_id, alert_text, show_alert=True)
                return

        booking.status = "confirmed"
        booking.save()

        # Mijoz telefoniga SMS xabarnoma yuborish
        sms_sent = send_booking_sms_confirmation(booking)
        clean_phone = normalize_phone_number(booking.customer_phone)

        answer_callback_query(cq_id, f"✅ Buyurtma #{booking.id} tasdiqlandi! Mijozga SMS yuborildi.")
        new_text, new_markup = build_booking_message(booking)
        new_text += f"\n\n👤 <i>Tasdiqladi: {admin_name}</i>\n📲 <i>Mijozga SMS tasdiqnoma yuborildi: +{clean_phone}</i>"
        edit_telegram_message(chat_id, msg_id, new_text, new_markup)

    elif action == "cancel":
        booking.status = "cancelled"
        booking.save()
        answer_callback_query(cq_id, f"❌ Buyurtma #{booking.id} bekor qilindi (xona bo'shatildi).")
        new_text, new_markup = build_booking_message(booking)
        new_text += f"\n\n👤 <i>Bekor qildi: {admin_name}</i>"
        edit_telegram_message(chat_id, msg_id, new_text, new_markup)


def _poll_updates_loop():
    bot_token = getattr(settings, 'TELEGRAM_BOT_TOKEN', '')
    if not bot_token:
        return

    logger.info("Telegram Bot Listener (Polling) ishga tushdi...")
    offset = None
    while not _stop_event.is_set():
        try:
            url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
            payload = {"timeout": 20}
            if offset:
                payload["offset"] = offset

            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=30) as res:
                result = json.loads(res.read().decode("utf-8"))

            if result.get("ok"):
                for update in result.get("result", []):
                    offset = update["update_id"] + 1
                    if "callback_query" in update:
                        handle_callback_query(update["callback_query"])
        except urllib.error.URLError:
            time.sleep(2)
        except Exception as e:
            logger.error(f"Telegram polling loop xatolik: {e}")
            time.sleep(2)


def start_polling_thread():
    global _polling_thread
    if _polling_thread is not None and _polling_thread.is_alive():
        return
    _stop_event.clear()
    _polling_thread = threading.Thread(target=_poll_updates_loop, daemon=True, name="TelegramListener")
    _polling_thread.start()
