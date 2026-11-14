from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('super/admin/', admin.site.urls),
    path("", include("core.urls")),
    path("blog/", include("blog.urls")),
    path("book/", include("book.urls")),
    path("contact/", include("contact.urls")),
    path("restaurant/", include("restaurant.urls")),
    path("rooms/", include("rooms.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
