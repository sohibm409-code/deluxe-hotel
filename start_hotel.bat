@echo off
title Deluxe Hotel Server
cd /d "%~dp0"
echo ==============================================
echo       DELUXE HOTEL - SERVER ISHGA TUSHMOQDA
echo ==============================================
echo Manzil (O'zingiz uchun): http://127.0.0.1:8000/
echo Manzil (Bir xil Wi-Fi dagi boshqalar uchun): http://192.168.243.187:8000/
echo Admin panel: http://127.0.0.1:8000/super/admin/
echo Telegram bot listener avtomatik ulandi.
echo Serverni to'xtatish uchun CTRL+C bosing.
echo ==============================================
call "%~dp0venv\Scripts\activate.bat"
"%~dp0venv\Scripts\python.exe" manage.py runserver 0.0.0.0:8000
pause
