from django.urls import path
from .views import RoomsView, RoomDetailView

app_name = "rooms"

urlpatterns = [
    path("", RoomsView.as_view(), name="index"),
    path("<int:pk>/", RoomDetailView.as_view(), name="detail"),
]
