from django.urls import path
from .views import QuickBookingView, BookingCreateView, BookingStatusView

app_name = "book"

urlpatterns = [
    path("quick-booking/", QuickBookingView.as_view(), name="quick_booking"),
    path("create/", BookingCreateView.as_view(), name="create"),
    path("create/<int:room_id>/", BookingCreateView.as_view(), name="book_room"),
    path("status/", BookingStatusView.as_view(), name="status"),
]
