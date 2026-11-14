import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# .env fayldan konfiguratsiyalarni yuklash
env_file = BASE_DIR / '.env'
if env_file.exists():
    with open(env_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!&$5rn2+sp#h-#!&h6+7+q3)57_zxp0)u@tpv5k2fa731r6(@h'

DEBUG = True

ALLOWED_HOSTS = ['*'] # Hamma hostlarga ruxsat berdik

INSTALLED_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Sizning app-laringiz
    'blog',
    'book',
    'contact',
    'restaurant',
    'rooms',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise joyida (2-o'rinda)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise Storage (Imlo xatosi 'storage' deb to'g'rilandi)
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Media fayllar (Rasmlar uchun)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Telegram Bot sozlamalari
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_ADMIN_CHAT_ID = os.getenv("TELEGRAM_ADMIN_CHAT_ID", "")

# SMS Xizmati sozlamalari (Eskiz.uz)
ESKIZ_EMAIL = os.getenv("ESKIZ_EMAIL", "")
ESKIZ_PASSWORD = os.getenv("ESKIZ_PASSWORD", "")

# Unfold Modern Admin Dashboard sozlamalari
UNFOLD = {
    "SITE_TITLE": "Deluxe Hotel Admin",
    "SITE_HEADER": "Deluxe Hotel",
    "SITE_SUBHEADER": "Mehmonxona boshqaruv tizimi",
    "SITE_URL": "/",
    "SITE_SYMBOL": "hotel",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "COLORS": {
        "primary": {
            "50": "250 245 238",
            "100": "243 234 220",
            "200": "231 213 186",
            "300": "216 188 147",
            "400": "201 161 109",
            "500": "193 155 118",
            "600": "173 133 93",
            "700": "144 105 76",
            "800": "119 87 66",
            "900": "99 73 57",
            "950": "55 38 28",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Buyurtmalar (Bookings)",
                "separator": True,
                "items": [
                    {
                        "title": "Xona bronlari",
                        "icon": "hotel",
                        "link": lambda request: "/super/admin/book/booking/",
                    },
                    {
                        "title": "Stol bronlari",
                        "icon": "restaurant",
                        "link": lambda request: "/super/admin/restaurant/tablereservation/",
                    },
                ],
            },
            {
                "title": "Mehmonxona va Xonalar",
                "separator": True,
                "items": [
                    {
                        "title": "Xonalar",
                        "icon": "bed",
                        "link": lambda request: "/super/admin/rooms/room/",
                    },
                    {
                        "title": "Xizmatlar",
                        "icon": "room_service",
                        "link": lambda request: "/super/admin/core/service/",
                    },
                    {
                        "title": "Mijozlar fikrlari",
                        "icon": "reviews",
                        "link": lambda request: "/super/admin/core/testimonial/",
                    },
                    {
                        "title": "Statistika",
                        "icon": "analytics",
                        "link": lambda request: "/super/admin/core/hotelstat/",
                    },
                ],
            },
            {
                "title": "Restoran va Taomlar",
                "separator": True,
                "items": [
                    {
                        "title": "Taom toifalari",
                        "icon": "category",
                        "link": lambda request: "/super/admin/restaurant/category/",
                    },
                    {
                        "title": "Menyu taomlari",
                        "icon": "dinner_dining",
                        "link": lambda request: "/super/admin/restaurant/menuitem/",
                    },
                ],
            },
            {
                "title": "Aloqa va Blog",
                "separator": True,
                "items": [
                    {
                        "title": "Blog maqolalari",
                        "icon": "article",
                        "link": lambda request: "/super/admin/blog/blog/",
                    },
                    {
                        "title": "Murojaatlar (Contact)",
                        "icon": "mail",
                        "link": lambda request: "/super/admin/contact/contact/",
                    },
                ],
            },
        ],
    },
}

# ==============================================================================
# TELEGRAM BOT NOTIFICATIONS
# ==============================================================================
# Yangi buyurtmalar (Xona, Stol, VIP Transfer, Xabar) haqida Telegramga xabar yuborish
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_ADMIN_CHAT_ID = os.getenv("TELEGRAM_ADMIN_CHAT_ID", "")



