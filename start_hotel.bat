@echo off
title Deluxe Hotel Server
cd /d "%~dp0"
echo ==============================================
echo       DELUXE HOTEL - SERVER ISHGA TUSHMOQDA
echo ==============================================
echo Manzil: http://127.0.0.1:8000/
echo Admin panel: http://127.0.0.1:8000/super/admin/
echo Telegram bot listener avtomatik ulandi.
echo Serverni to'xtatish uchun CTRL+C bosing.
echo ==============================================
call venv\Scripts\activate.bat
python manage.py runserver 127.0.0.1:8000
pause
