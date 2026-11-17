from django.urls import path
from .views import (
    IndexView,
    AboutView,
    service_request_view,
    submit_testimonial_view,
    telegram_webhook_view,
    setup_webhook_view,
    test_send_telegram_view,
)

app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("about/", AboutView.as_view(), name="about"),
    path("service-request/", service_request_view, name="service_request"),
    path("submit-review/", submit_testimonial_view, name="submit_review"),
    path("telegram/webhook/", telegram_webhook_view, name="telegram_webhook"),
    path("telegram/setup-webhook/", setup_webhook_view, name="setup_webhook"),
    path("telegram/test-send/", test_send_telegram_view, name="test_send_telegram"),
]
