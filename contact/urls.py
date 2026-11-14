from django.urls import path
from .views import ContactView

app_name = "contact"

urlpatterns = [
    # "contact/" ni olib tashlang va shunchaki bo'sh joy qo'ying
    path("", ContactView.as_view(), name="index"),
]