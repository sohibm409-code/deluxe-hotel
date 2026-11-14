from datetime import date
from .models import Booking

def check_room_availability(room, check_in, check_out, exclude_booking_id=None):
    """
    Xona ko'rsatilgan sanalarda bo'shmi yoki tasdiqlangan (confirmed) bron bormi tekshiradi.
    Bo'sh bo'lsa True, band bo'lsa False qaytaradi.
    """
    if not room or not check_in or not check_out:
        return True

    qs = Booking.objects.filter(
        room=room,
        status='confirmed',
        check_in__lt=check_out,
        check_out__gt=check_in
    )
    if exclude_booking_id:
        qs = qs.exclude(id=exclude_booking_id)

    return not qs.exists()


def get_conflicting_booking(room, check_in, check_out, exclude_booking_id=None):
    """
    To'qnash kelayotgan (tasdiqlangan) bronni topib qaytaradi.
    """
    if not room or not check_in or not check_out:
        return None

    qs = Booking.objects.filter(
        room=room,
        status='confirmed',
        check_in__lt=check_out,
        check_out__gt=check_in
    )
    if exclude_booking_id:
        qs = qs.exclude(id=exclude_booking_id)

    return qs.first()
