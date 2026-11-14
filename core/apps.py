import os
import sys
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    verbose_name = "Asosiy sahifa sozlamalari (Core)"

    def ready(self):
        is_runserver = any('runserver' in arg for arg in sys.argv)
        is_main_worker = os.environ.get('RUN_MAIN') == 'true'

        if is_runserver and (is_main_worker or '--noreload' in sys.argv):
            from core.telegram_listener import start_polling_thread
            start_polling_thread()
