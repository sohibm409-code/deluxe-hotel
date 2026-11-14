from django.core.management.base import BaseCommand
from django.conf import settings
from core.telegram import send_telegram_message

class Command(BaseCommand):
    help = "Telegram Bot ulanishini tekshirish va sinov xabari yuborish"

    def handle(self, *args, **options):
        token = getattr(settings, 'TELEGRAM_BOT_TOKEN', '')
        chat_id = getattr(settings, 'TELEGRAM_ADMIN_CHAT_ID', '')

        self.stdout.write(self.style.NOTICE("--- Telegram Bot Ulanishini Tekshirish ---"))
        self.stdout.write(f"Bot Token: {'*' * (len(token) - 6) + token[-6:] if len(token) > 6 else (token or 'KIRITILMAGAN')}")
        self.stdout.write(f"Chat ID:   {chat_id or 'KIRITILMAGAN'}")

        if not token or not chat_id:
            self.stdout.write(self.style.ERROR(
                "\n[XATOLIK] Telegram bot token yoki chat_id .env faylida topilmadi!\n"
                "Iltimos, loyiha ildizidagi .env faylini ochib quyidagilarni kiriting:\n"
                "  TELEGRAM_BOT_TOKEN=bot_tokeningiz\n"
                "  TELEGRAM_ADMIN_CHAT_ID=shaxsiy_chat_idingiz\n"
            ))
            return

        self.stdout.write("Sinov xabari yuborilmoqda...")
        msg = (
            "🚀 <b>Tabriklaymiz!</b>\n\n"
            "Mehmonxona saytingiz Telegram botga muvaffaqiyatli ulandi!\n"
            "Endi yangi xona bron qilinganda xabarlar to'g'ridan-to'g'ri shu yerga keladi."
        )
        success = send_telegram_message(msg, async_mode=False)

        if success:
            self.stdout.write(self.style.SUCCESS("[MUVAFFAQIYATLI] Sinov xabari Telegramingizga yuborildi!"))
        else:
            self.stdout.write(self.style.ERROR("[XATOLIK] Xabar yuborilmadi. Bot token yoki chat ID to'g'riligini tekshiring."))
