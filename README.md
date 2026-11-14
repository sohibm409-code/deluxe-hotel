# 🏨 Deluxe Hotel & Resort — Hashamatli 5 Yulduzli Mehmonxona Veb-Ilovasi

Toshkent shahrining qoq markazida joylashgan **Deluxe Hotel & Resort** uchun ishlab chiqilgan zamonaviy, to'liq funksional va hashamatli veb-platforma. Loyiha mehmonlarga xonalarni onlayn bron qilish, restoranda stol band qilish, xizmatlardan foydalanish, haqiqiy mehmonlar fikrlarini o'qish va bildirish hamda administratorlar uchun Telegram orqali tezkor boshqaruv imkonini beradi.

---

## ✨ Asosiy Imkoniyatlar va Funksiyalar

* **👑 Zamonaviy va Hashamatli Dizayn**: Oltin (`#c19b76`) va to'q ranglar uyg'unligi, Playfair Display va Poppins shriftlari, noutbuk va mobil qurilmalarda bir xil chiroyli aks etuvchi qat'iy tartib.
* **🛏 Xonalar va Onlayn Bron Qilish (`rooms`, `book`)**:
  * Xonalarni toifasi, sig'imi va narxi bo'yicha saralash va filtrlash.
  * Interaktiv fotogalereya (Thumbnails + Asosiy ko'rish oynasi).
  * Bandlik sanalarini avtomatik tekshirish va to'qnashuvlarni oldini olish tizimi.
  * Telefon raqami orqali bron holatini (tasdiqlangan / kutilmoqda / bekor qilingan) onlayn tekshirish.
* **🍽 Deluxe Royal Restoran & O'zbek Milliy Taomlari (`restaurant`)**:
  * 10 ta eng sara o'zbek milliy taomlari (Toshkent to'y oshi, Samarqandcha tandir kabob, qozon kabob, norin, tandir somsa, manti, shashliklar va h.k.) va Yevropa taomlari menyusi.
  * Kategoriyalar bo'yicha tezkor JavaScript filtri.
  * Restoranda onlayn stol band qilish (Table Reservation).
* **📍 Toshkent Markazi Google Maps Integratsiyasi (`contact`)**:
  * Amir Temur shoh ko'chasidagi real joylashuv xaritasi.
  * Kontakt ma'lumotlari va interaktiv xabar yuborish formasi.
* **📸 Instagram Integratsiyasi**:
  * Barcha sahifalarda foydalanuvchining rasmiy Instagram profiliga ([@jovliyev1626](https://www.instagram.com/jovliyev1626/)) ulangan interaktiv galereya.
* **⭐ Haqiqiy Mehmonlar Fikrlari & Reyting (`core`)**:
  * 1-5 yulduzli interaktiv reyting selektori bilan fikr qoldirish modali.
* **🛎 Eksklyuziv Xizmat Modallari**:
  * 24/7 Resepshn va konsyerj bilan tezkor bog'lanish modali.
  * Aeroportdan kutib olish va kuzatib qo'yish uchun VIP Transfer buyurtma modali.
  * Virtual YouTube video sayohat modali.
* **🤖 Telegram Bot Bildirishnomalari**:
  * Har bir yangi xona bron qilinganda, stol band qilinganda yoki aloqa xabari kelganda admin Telegramiga zudlik bilan avtomatik bildirishnoma boradi.
* **📰 Mehmonxona Blogi va Izohlar Tizimi (`blog`)**:
  * Yangiliklar va maqolalar, toifalar bo'yicha saralash, o'quvchilar tomonidan haqiqiy izoh qoldirish imkoniyati.
* **🛠 Premium Admin Panel (Django Unfold)**:
  * Zamonaviy Tailwind asosidagi qulay boshqaruv paneli.

---

## 🛠 Texnologiyalar Steki

* **Backend**: Python 3.13, Django 6.0
* **Admin**: Django Unfold (zamonaviy UI)
* **Frontend**: HTML5, CSS3, JavaScript (ES6+), Font Awesome 6
* **Database**: SQLite3 (Ishlab chiqish uchun) / PostgreSQL (Production uchun)
* **Static Assets**: WhiteNoise, AOS (Animate on Scroll)

---

## 🚀 O'rnatish va Ishga Tushirish

### 1. Repozitoriyani klonlash:
```bash
git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME
```

### 2. Virtual muhit yaratish va faollashtirish:
```bash
# Windows uchun:
python -m venv venv
venv\Scripts\activate

# Linux / MacOS uchun:
python3 -m venv venv
source venv/bin/activate
```

### 3. Bog'liqliklarni o'rnatish:
```bash
pip install -r requirements.txt
```

### 4. Ma'lumotlar bazasi migratsiyasi:
```bash
python manage.py migrate
```

### 5. Superuser (Administrator) yaratish:
```bash
python manage.py createsuperuser
```

### 6. Loyihani ishga tushirish:
```bash
python manage.py runserver
```

Brauzerda oching:
* Asosiy sayt: **`http://127.0.0.1:8000/`**
* Admin panel: **`http://127.0.0.1:8000/super/admin/`**

---

## 📱 Aloqa va Ijtimoiy Tarmoqlar

* **Instagram**: [@jovliyev1626](https://www.instagram.com/jovliyev1626/)
* **Telegram**: [@deluxe_hotel_resort](https://t.me/deluxe_hotel_resort)
* **Telefon**: +998 (94) 055-08-55 / +998 (94) 759-26-16
* **Manzil**: Toshkent sh., Amir Temur shoh ko'chasi, 45-uy

---

## 📄 Litsenziya

Ushbu loyiha shaxsiy va tijoriy foydalanish uchun ochiq. Barcha huquqlar himoyalangan © 2026 Deluxe Hotel & Resort.
