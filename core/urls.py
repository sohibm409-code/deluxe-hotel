from django.urls import path
from .views import IndexView, AboutView, service_request_view

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("service-request/", service_request_view, name="service_request"),
]
