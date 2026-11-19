from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve
from core.views import set_language_view

urlpatterns = [
    path('set-language/', set_language_view, name='set_language_custom'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('super/admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += i18n_patterns(
    path("", include("core.urls")),
    path("blog/", include("blog.urls")),
    path("book/", include("book.urls")),
    path("contact/", include("contact.urls")),
    path("restaurant/", include("restaurant.urls")),
    path("rooms/", include("rooms.urls")),
    prefix_default_language=False,
)
