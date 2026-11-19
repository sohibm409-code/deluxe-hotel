# -*- coding: utf-8 -*-
"""
Deluxe Hotel - Complete Multilingual Translation Generator (UZ, RU, EN)
Uses polib to compile .po to .mo directly on Windows without external gettext binaries.
"""
from pathlib import Path
import polib

BASE_DIR = Path(__file__).resolve().parent
LOCALE_DIR = BASE_DIR / 'locale'

TRANSLATIONS = {
    # --- Navigation & General ---
    "Home": {
        "uz": "Bosh sahifa",
        "ru": "Главная",
        "en": "Home",
    },
    "Rooms": {
        "uz": "Xonalar",
        "ru": "Номера",
        "en": "Rooms",
    },
    "Restaurant": {
        "uz": "Restoran",
        "ru": "Ресторан",
        "en": "Restaurant",
    },
    "About": {
        "uz": "Biz haqimizda",
        "ru": "О нас",
        "en": "About Us",
    },
    "About Us": {
        "uz": "Biz haqimizda",
        "ru": "О нас",
        "en": "About Us",
    },
    "Blog": {
        "uz": "Blog",
        "ru": "Блог",
        "en": "Blog",
    },
    "Contact": {
        "uz": "Aloqa",
        "ru": "Контакты",
        "en": "Contact",
    },
    "My Booking": {
        "uz": "Mening bronim",
        "ru": "Моя бронь",
        "en": "My Booking",
    },
    "Book Now": {
        "uz": "Band qilish",
        "ru": "Забронировать",
        "en": "Book Now",
    },
    "Deluxe Hotel & Resort — 5-Star Luxury Hotel in Tashkent": {
        "uz": "Deluxe Hotel & Resort — Toshkentdagi 5 Yulduzli Hashamatli Mehmonxona",
        "ru": "Deluxe Hotel & Resort — 5-Звездочный Роскошный Отель в Ташкенте",
        "en": "Deluxe Hotel & Resort — 5-Star Luxury Hotel in Tashkent",
    },

    # --- Hero (Home) ---
    "Welcome To Deluxe": {
        "uz": "Deluxe Hotelga Xush Kelibsiz",
        "ru": "Добро пожаловать в Deluxe",
        "en": "Welcome To Deluxe",
    },
    "Hotels & Resorts": {
        "uz": "Mehmonxona & Dam Olish Maskani",
        "ru": "Отели & Курорты",
        "en": "Hotels & Resorts",
    },
    "Enjoy A Luxury Experience": {
        "uz": "Shohona Hashamat va Qulaylikdan Bahramand Bo'ling",
        "ru": "Насладитесь непревзойденной роскошью",
        "en": "Enjoy A Luxury Experience",
    },
    "Choose Rooms": {
        "uz": "Xonalarni tanlash",
        "ru": "Выбрать номер",
        "en": "Choose Rooms",
    },
    "Explore Restaurant": {
        "uz": "Restoranni ko'rish",
        "ru": "Наш ресторан",
        "en": "Explore Restaurant",
    },

    # --- About Section ---
    "5-STAR LUXURY & COMFORT": {
        "uz": "5-YULDUZLI HASHAMAT VA QULAYLIK",
        "ru": "5-ЗВЕЗДОЧНАЯ РОСКОШЬ И КОМФОРТ",
        "en": "5-STAR LUXURY & COMFORT",
    },
    "Welcome to Deluxe Hotel": {
        "uz": "Deluxe Hotelga Xush Kelibsiz",
        "ru": "Добро пожаловать в Deluxe Hotel",
        "en": "Welcome to Deluxe Hotel",
    },
    "About Welcome Lead": {
        "uz": "Sharqona samimiy mehmondo‘stlik va xalqaro 5 yulduzli qulaylik uyg‘unlashgan muazzam maskan.",
        "ru": "Уникальное сочетание восточного гостеприимства и международных стандартов пятизвездочного сервиса.",
        "en": "A magnificent haven blending warm oriental hospitality with international 5-star comfort.",
    },
    "About Welcome Desc": {
        "uz": "Toshkentning eng nufuzli manzilida joylashgan Deluxe Hotel — nafis interyer, sokin muhit va har bir mehmonga ko‘rsatiladigan individual e'tibor bilan ajralib turadi. Biz sizga shunchaki xona emas, balki betakror dam olish lahzalari va unutilmas xotiralarni tortiq etamiz.",
        "ru": "Расположенный в самом престижном районе Ташкента, Deluxe Hotel отличается изысканным интерьером, спокойной атмосферой и безупречным персональным вниманием к каждому гостю.",
        "en": "Situated at Tashkent's most prestigious address, Deluxe Hotel features refined interiors, serene ambiance, and tailored attention for every guest.",
    },
    "Years of Experience": {
        "uz": "Yillik Tajriba",
        "ru": "Лет Опыта",
        "en": "Years of Experience",
    },
    "15+ Years Experience": {
        "uz": "15+ Yillik Tajriba",
        "ru": "15+ Лет Опыта",
        "en": "15+ Years Experience",
    },
    "Watch Video Tour": {
        "uz": "Video sayohatni ko'rish",
        "ru": "Посмотреть видеотур",
        "en": "Watch Video Tour",
    },
    "Video Tour": {
        "uz": "Video sayohat",
        "ru": "Видеотур",
        "en": "Video Tour",
    },
    "Satisfied Guests": {
        "uz": "Mamnun Mehmonlar",
        "ru": "Довольных Гостей",
        "en": "Satisfied Guests",
    },
    "Luxury Rooms": {
        "uz": "Lyuks Xonalar",
        "ru": "Люкс Номеров",
        "en": "Luxury Rooms",
    },
    "Professional Staff": {
        "uz": "Professional Xodimlar",
        "ru": "Профессиональных Сотрудников",
        "en": "Professional Staff",
    },
    "Read More": {
        "uz": "Batafsil o'qish",
        "ru": "Читать далее",
        "en": "Read More",
    },
    "Explore Rooms": {
        "uz": "Xonalar bilan tanishish",
        "ru": "Ознакомиться с номерами",
        "en": "Explore Rooms",
    },
    "50+ Luxury Rooms": {
        "uz": "50+ Hashamatli Xonalar",
        "ru": "50+ Роскошных Номеров",
        "en": "50+ Luxury Rooms",
    },
    "Panoramic windows, orthopedic beds and royal comfort.": {
        "uz": "Panoramali derazalar, ortopedik karavotlar va shohona qulaylik.",
        "ru": "Панорамные окна, ортопедические кровати и королевский комфорт.",
        "en": "Panoramic windows, orthopedic beds and royal comfort.",
    },
    "Gourmet Restaurant": {
        "uz": "Gourmet Restoran",
        "ru": "Ресторан Авторской Кухни",
        "en": "Gourmet Restaurant",
    },
    "Rich author menu of European and national dishes.": {
        "uz": "Yevropa va milliy taomlarning boy mualliflik menyusi.",
        "ru": "Богатое авторское меню европейских и национальных блюд.",
        "en": "Rich author menu of European and national dishes.",
    },
    "Prime Central Location": {
        "uz": "Qulay Markaziy Lokatsiya",
        "ru": "Удобное Центральное Расположение",
        "en": "Prime Central Location",
    },
    "A few minutes from the airport and city attractions.": {
        "uz": "Aeroport va shahar diqqatga sazovor joylariga bir necha daqiqa.",
        "ru": "В нескольких минутах от аэропорта и главных достопримечательностей.",
        "en": "A few minutes from the airport and city attractions.",
    },
    "24/7 Personal Concierge": {
        "uz": "24/7 Shaxsiy Konsyerj",
        "ru": "24/7 Персональный Консьерж",
        "en": "24/7 Personal Concierge",
    },
    "Round-the-clock individual attention for each guest.": {
        "uz": "Har bir mehmonimiz uchun kechayu-kunduz individual e'tibor.",
        "ru": "Круглосуточное индивидуальное внимание к каждому гостю.",
        "en": "Round-the-clock individual attention for each guest.",
    },
    "Guest Recognition Rating": {
        "uz": "2,800+ mamnun mehmonlar e'tirofi (Booking.com & TripAdvisor)",
        "ru": "Признание более 2,800 гостей (Booking.com & TripAdvisor)",
        "en": "Recognition by 2,800+ happy guests (Booking.com & TripAdvisor)",
    },

    # --- Services Section ---
    "EXCLUSIVE AMENITIES": {
        "uz": "EKSKLYUZIV QULAYLIKLAR",
        "ru": "ЭКСКЛЮЗИВНЫЕ УДОБСТВА",
        "en": "EXCLUSIVE AMENITIES",
    },
    "Hotel Services": {
        "uz": "Mehmonxona Xizmatlari",
        "ru": "Услуги Отеля",
        "en": "Hotel Services",
    },
    "Exclusive Hotel Services": {
        "uz": "Eksklyuziv Mehmonxona Xizmatlari",
        "ru": "Эксклюзивные Услуги Отеля",
        "en": "Exclusive Hotel Services",
    },
    "Designed for Your Utmost Comfort": {
        "uz": "Sizning oliy darajadagi qulayligingiz uchun",
        "ru": "Создано для вашего безупречного отдыха",
        "en": "Designed for Your Utmost Comfort",
    },
    "24/7 Reception & Concierge": {
        "uz": "24/7 Resepshn va Konsyerj",
        "ru": "24/7 Ресепшн и Консьерж",
        "en": "24/7 Reception & Concierge",
    },
    "Round-the-clock front desk": {
        "uz": "Kechayu-kunduz resepshn",
        "ru": "Круглосуточный ресепшн",
        "en": "Round-the-clock front desk",
    },
    "Call Desk": {
        "uz": "Qo'ng'iroq qilish",
        "ru": "Позвонить",
        "en": "Call Desk",
    },
    "VIP Transfer Service": {
        "uz": "VIP Transfer xizmati",
        "ru": "VIP Трансфер сервис",
        "en": "VIP Transfer Service",
    },
    "SPA & Wellness Center": {
        "uz": "SPA & Salomatlik markazi",
        "ru": "СПА и Оздоровительный центр",
        "en": "SPA & Wellness Center",
    },
    "Swimming Pool": {
        "uz": "Suzish havzasi",
        "ru": "Плавательный бассейн",
        "en": "Swimming Pool",
    },
    "Fast Free Wi-Fi": {
        "uz": "Tezkor bepul Wi-Fi",
        "ru": "Скоростной Wi-Fi",
        "en": "Fast Free Wi-Fi",
    },
    "Order VIP Transfer": {
        "uz": "VIP Transfer buyurtma qilish",
        "ru": "Заказать VIP трансфер",
        "en": "Order VIP Transfer",
    },
    "Menu & Table Reservation": {
        "uz": "Menyu & Stol band qilish",
        "ru": "Меню и Бронь стола",
        "en": "Menu & Table Reservation",
    },
    "24/7 SERVICE": {
        "uz": "24/7 XIZMAT",
        "ru": "24/7 СЕРВИС",
        "en": "24/7 SERVICE",
    },
    "GOURMET": {
        "uz": "GOURMET",
        "ru": "ГУРМЭ",
        "en": "GOURMET",
    },
    "VIP TRANSPORT": {
        "uz": "VIP TRANSPORT",
        "ru": "VIP ТРАНСПОРТ",
        "en": "VIP TRANSPORT",
    },

    # --- Rooms Section ---
    "Our Hotel Rooms": {
        "uz": "Bizning Xonalarimiz",
        "ru": "Номера Отеля",
        "en": "Our Hotel Rooms",
    },
    "Our Rooms": {
        "uz": "Xonalarimiz",
        "ru": "Наши Номера",
        "en": "Our Rooms",
    },
    "Rooms & Suites": {
        "uz": "Xonalar va Lyukslar",
        "ru": "Номера и Люксы",
        "en": "Rooms & Suites",
    },
    "Discover Comfort & Elegance": {
        "uz": "Shohona qulaylik va nafislikni kashf eting",
        "ru": "Откройте для себя комфорт и элегантность",
        "en": "Discover Comfort & Elegance",
    },
    "View All Rooms": {
        "uz": "Barcha xonalarni ko'rish",
        "ru": "Все номера",
        "en": "View All Rooms",
    },
    "per night": {
        "uz": "/ tun",
        "ru": "/ ночь",
        "en": "/ night",
    },
    "Capacity": {
        "uz": "Sig'imi",
        "ru": "Вместимость",
        "en": "Capacity",
    },
    "Capacity:": {
        "uz": "Sig'imi:",
        "ru": "Вместимость:",
        "en": "Capacity:",
    },
    "Size": {
        "uz": "Maydoni",
        "ru": "Площадь",
        "en": "Size",
    },
    "Size:": {
        "uz": "Maydoni:",
        "ru": "Площадь:",
        "en": "Size:",
    },
    "View": {
        "uz": "Manzara",
        "ru": "Вид",
        "en": "View",
    },
    "View:": {
        "uz": "Manzara:",
        "ru": "Вид:",
        "en": "View:",
    },
    "Bed": {
        "uz": "Yotoq",
        "ru": "Кровать",
        "en": "Bed",
    },
    "Bed:": {
        "uz": "Yotoq:",
        "ru": "Кровать:",
        "en": "Bed:",
    },
    "guests": {
        "uz": "kishi",
        "ru": "гостя",
        "en": "guests",
    },
    "photos": {
        "uz": "ta rasm",
        "ru": "фото",
        "en": "photos",
    },
    "View Details": {
        "uz": "Batafsil ko'rish",
        "ru": "Подробнее",
        "en": "View Details",
    },
    "Book This Room": {
        "uz": "Ushbu xonani band qilish",
        "ru": "Забронировать этот номер",
        "en": "Book This Room",
    },
    "Room Amenities & Features": {
        "uz": "Xona qulayliklari va jihozlari",
        "ru": "Удобства и оснащение номера",
        "en": "Room Amenities & Features",
    },
    "Description": {
        "uz": "Tavsif",
        "ru": "Описание",
        "en": "Description",
    },
    "Gallery": {
        "uz": "Galereya",
        "ru": "Галерея",
        "en": "Gallery",
    },
    "Search & Filter": {
        "uz": "Qidiruv va Filtr",
        "ru": "Поиск и Фильтр",
        "en": "Search & Filter",
    },
    "All Room Types": {
        "uz": "Barcha xona toifalari",
        "ru": "Все категории номеров",
        "en": "All Room Types",
    },
    "All Guests": {
        "uz": "Barcha mehmonlar",
        "ru": "Все гости",
        "en": "All Guests",
    },
    "Clear Filter": {
        "uz": "Filtrni tozalash",
        "ru": "Сбросить фильтр",
        "en": "Clear Filter",
    },
    "Exclusive Amenities": {
        "uz": "Eksklyuziv Qulayliklar",
        "ru": "Эксклюзивные Удобства",
        "en": "Exclusive Amenities",
    },
    "Sorry, no rooms found": {
        "uz": "Kechirasiz, xonalar topilmadi",
        "ru": "К сожалению, номера не найдены",
        "en": "Sorry, no rooms found",
    },
    "No rooms available at the moment.": {
        "uz": "Hozircha xonalar mavjud emas.",
        "ru": "На данный момент номера отсутствуют.",
        "en": "No rooms available at the moment.",
    },

    # --- Restaurant & Table Reservation ---
    "Gourmet Restaurant & Bar": {
        "uz": "Restoran va Gourmet Oshxona",
        "ru": "Ресторан и Авторская Кухня",
        "en": "Gourmet Restaurant & Bar",
    },
    "Authentic Culinary Excellence": {
        "uz": "Nafis ta'mlar va unutilmas mehmondo'stlik",
        "ru": "Кулинарные шедевры и непревзойденный сервис",
        "en": "Authentic Culinary Excellence",
    },
    "Reserve A Table": {
        "uz": "Stol Band Qilish",
        "ru": "Забронировать Стол",
        "en": "Reserve A Table",
    },
    "Book Table": {
        "uz": "Stol band qilish",
        "ru": "Забронировать стол",
        "en": "Book Table",
    },
    "All Dishes": {
        "uz": "Barcha taomlar",
        "ru": "Все блюда",
        "en": "All Dishes",
    },
    "All": {
        "uz": "Barchasi",
        "ru": "Все",
        "en": "All",
    },
    "Breakfast": {
        "uz": "Nonushta",
        "ru": "Завтрак",
        "en": "Breakfast",
    },
    "Main Dishes": {
        "uz": "Asosiy taomlar",
        "ru": "Основные блюда",
        "en": "Main Dishes",
    },
    "Desserts": {
        "uz": "Shirinliklar",
        "ru": "Десерты",
        "en": "Desserts",
    },
    "Drinks & Wine": {
        "uz": "Ichimliklar & Kokteyllar",
        "ru": "Напитки и Винная карта",
        "en": "Drinks & Wine",
    },
    "ROYAL FEAST": {
        "uz": "SHOHONA DASTURXON",
        "ru": "КОРОЛЕВСКИЙ СТОЛ",
        "en": "ROYAL FEAST",
    },
    "National & European Cuisine Menu": {
        "uz": "Milliy va Yevropa Taomlari Menyusi",
        "ru": "Меню Национальной и Европейской Кухни",
        "en": "National & European Cuisine Menu",
    },
    "Recommended": {
        "uz": "Tavsiya etiladi",
        "ru": "Рекомендуем",
        "en": "Recommended",
    },
    "Full Name": {
        "uz": "To'liq ismingiz",
        "ru": "Ваше имя",
        "en": "Full Name",
    },
    "Phone Number": {
        "uz": "Telefon raqamingiz",
        "ru": "Номер телефона",
        "en": "Phone Number",
    },
    "Reservation Date": {
        "uz": "Band qilish sanasi",
        "ru": "Дата бронирования",
        "en": "Reservation Date",
    },
    "Reservation Time": {
        "uz": "Band qilish vaqti",
        "ru": "Время бронирования",
        "en": "Reservation Time",
    },
    "Number of Persons": {
        "uz": "Mehmonlar soni",
        "ru": "Количество персон",
        "en": "Number of Persons",
    },
    "Special Wishes (Optional)": {
        "uz": "Qo'shimcha istaklar (ixtiyoriy)",
        "ru": "Особые пожелания (необязательно)",
        "en": "Special Wishes (Optional)",
    },
    "Confirm Table Reservation": {
        "uz": "Stolni band qilish",
        "ru": "Забронировать стол",
        "en": "Confirm Table Reservation",
    },
    "100% Halal & Premium Quality": {
        "uz": "100% Halol & Premium Sifat",
        "ru": "100% Халяль и Премиум Качество",
        "en": "100% Halal & Premium Quality",
    },

    # --- Testimonials & Reviews ---
    "GUEST REVIEWS": {
        "uz": "MEHMONLARIMIZ FIKRLARI",
        "ru": "ОТЗЫВЫ ГОСТЕЙ",
        "en": "GUEST REVIEWS",
    },
    "What Our Guests Say": {
        "uz": "Mehmonlarimiz Fikrlari",
        "ru": "Отзывы Наших Гостей",
        "en": "What Our Guests Say",
    },
    "What Our Clients Say": {
        "uz": "Mijozlarimiz Nima Deydi?",
        "ru": "Что Говорят Наши Клиенты",
        "en": "What Our Clients Say",
    },
    "Leave a Review About Hotel": {
        "uz": "Mehmonxona Haqida Fikr Qoldirish",
        "ru": "Оставить Отзыв об Отеле",
        "en": "Leave a Review About Hotel",
    },

    # --- FAQ Section ---
    "QUESTIONS & ANSWERS": {
        "uz": "SAVOLLAR VA JAVOBLAR",
        "ru": "ВОПРОСЫ И ОТВЕТЫ",
        "en": "QUESTIONS & ANSWERS",
    },
    "Frequently Asked Questions (FAQ)": {
        "uz": "Ko‘p Beriladigan Savollar (FAQ)",
        "ru": "Часто Задаваемые Вопросы (FAQ)",
        "en": "Frequently Asked Questions (FAQ)",
    },
    "What are the check-in and check-out times?": {
        "uz": "Check-in va Check-out vaqtlari qanday belgilangan?",
        "ru": "Каковы правила и время заезда (Check-in) и выезда (Check-out)?",
        "en": "What are the check-in and check-out times?",
    },
    "Is breakfast included in the room rate and what time is it served?": {
        "uz": "Nonushta xona narxiga kiritilganmi va qaysi vaqtda beriladi?",
        "ru": "Включен ли завтрак в стоимость проживания и в какое время он подается?",
        "en": "Is breakfast included in the room rate and what time is it served?",
    },
    "What payment methods are accepted?": {
        "uz": "Qanday to‘lov usullari qabul qilinadi?",
        "ru": "Какие способы оплаты принимаются в отеле?",
        "en": "What payment methods are accepted?",
    },
    "How to book an airport or train station transfer?": {
        "uz": "Aeroport yoki vokzaldan transfer qanday buyurtma qilinadi?",
        "ru": "Как заказать трансфер из аэропорта или вокзала?",
        "en": "How to book an airport or train station transfer?",
    },
    "What are the policies when traveling with children?": {
        "uz": "Bolalar bilan tashrif buyurganda shartlar qanaqa?",
        "ru": "Каковы условия проживания с детьми?",
        "en": "What are the policies when traveling with children?",
    },
    "What is the cancellation policy for bookings?": {
        "uz": "Bronni bekor qilish (Cancellation policy) tartibi qanday?",
        "ru": "Каковы правила отмены бронирования?",
        "en": "What is the cancellation policy for bookings?",
    },

    # --- Blog ---
    "Hotel News & Articles": {
        "uz": "Mehmonxona Yangiliklari va Maqolalar",
        "ru": "Новости Отеля и Статьи",
        "en": "Hotel News & Articles",
    },
    "Latest News": {
        "uz": "So'nggi Yangiliklar",
        "ru": "Свежие Новости",
        "en": "Latest News",
    },
    "Recent Blog": {
        "uz": "Mehmonxona Blogi",
        "ru": "Блог Отеля",
        "en": "Recent Blog",
    },
    "Read Article": {
        "uz": "Maqolani o'qish",
        "ru": "Читать статью",
        "en": "Read Article",
    },
    "comments": {
        "uz": "ta izoh",
        "ru": "комментариев",
        "en": "comments",
    },
    "No blog posts available at the moment.": {
        "uz": "Hozircha bloglar mavjud emas.",
        "ru": "На данный момент статей нет.",
        "en": "No blog posts available at the moment.",
    },

    # --- Instagram Gallery ---
    "Instagram Gallery": {
        "uz": "Instagram Galereya",
        "ru": "Инстаграм Галерея",
        "en": "Instagram Gallery",
    },
    "Follow us on Instagram: @jovliyev1626": {
        "uz": "Instagram'da kuzatib boring: @jovliyev1626",
        "ru": "Подписывайтесь на Instagram: @jovliyev1626",
        "en": "Follow us on Instagram: @jovliyev1626",
    },

    # --- Booking & Booking Status ---
    "Online Room Reservation": {
        "uz": "Onlayn Xona Band Qilish",
        "ru": "Онлайн Бронирование Номера",
        "en": "Online Room Reservation",
    },
    "1. Room & Travel Dates": {
        "uz": "1. Xona va Tashrif Sanalari",
        "ru": "1. Номер и Даты Заезда",
        "en": "1. Room & Travel Dates",
    },
    "Check-in Date": {
        "uz": "Kelish sanasi",
        "ru": "Дата заезда",
        "en": "Check-in Date",
    },
    "Check-out Date": {
        "uz": "Ketish sanasi",
        "ru": "Дата выезда",
        "en": "Check-out Date",
    },
    "Select Room": {
        "uz": "Xonani tanlang",
        "ru": "Выберите номер",
        "en": "Select Room",
    },
    "Adults": {
        "uz": "Kattalar",
        "ru": "Взрослые",
        "en": "Adults",
    },
    "Children": {
        "uz": "Bolalar",
        "ru": "Дети",
        "en": "Children",
    },
    "Guests": {
        "uz": "Mehmonlar",
        "ru": "Гости",
        "en": "Guests",
    },
    "Selected Room": {
        "uz": "Tanlangan xona",
        "ru": "Выбранный номер",
        "en": "Selected Room",
    },
    "Duration": {
        "uz": "Davomiyligi",
        "ru": "Длительность",
        "en": "Duration",
    },
    "Total Price": {
        "uz": "Jami to'lov summasi",
        "ru": "Итоговая сумма к оплате",
        "en": "Total Price",
    },
    "2. Select Payment Method": {
        "uz": "2. To'lov Turini Tanlang",
        "ru": "2. Выберите Способ Оплаты",
        "en": "2. Select Payment Method",
    },
    "Cash": {
        "uz": "Naqd to'lov",
        "ru": "Наличный расчет",
        "en": "Cash",
    },
    "3. Guest Details": {
        "uz": "3. Mehmon Ma'lumotlari",
        "ru": "3. Данные Гостя",
        "en": "3. Guest Details",
    },
    "Email (Optional)": {
        "uz": "Elektron pochta (ixtiyoriy)",
        "ru": "Электронная почта (необязательно)",
        "en": "Email (Optional)",
    },
    "Confirm Booking": {
        "uz": "Xonani xavfsiz band qilish",
        "ru": "Безопасно забронировать номер",
        "en": "Confirm Booking",
    },
    "Check Booking Status": {
        "uz": "Bron Holatini Tekshirish",
        "ru": "Проверить Статус Брони",
        "en": "Check Booking Status",
    },
    "Enter your phone number or booking code:": {
        "uz": "Telefon raqamingiz yoki bron kodini kiriting:",
        "ru": "Введите ваш номер телефона или код бронирования:",
        "en": "Enter your phone number or booking code:",
    },
    "Search": {
        "uz": "Qidirish",
        "ru": "Найти",
        "en": "Search",
    },
    "Booking Code": {
        "uz": "Bron kodi",
        "ru": "Код бронирования",
        "en": "Booking Code",
    },
    "Status": {
        "uz": "Holati",
        "ru": "Статус",
        "en": "Status",
    },
    "Confirmed": {
        "uz": "Tasdiqlangan",
        "ru": "Подтверждено",
        "en": "Confirmed",
    },
    "Pending": {
        "uz": "Kutilmoqda",
        "ru": "В ожидании",
        "en": "Pending",
    },
    "Cancelled": {
        "uz": "Bekor qilingan",
        "ru": "Отменено",
        "en": "Cancelled",
    },

    # --- Contact Section ---
    "Contact Us": {
        "uz": "Biz Bilan Bog'lanish",
        "ru": "Связаться с Нами",
        "en": "Contact Us",
    },
    "Our Address": {
        "uz": "Manzilimiz",
        "ru": "Наш Адрес",
        "en": "Our Address",
    },
    "Tashkent city, Amir Temur Ave, 107": {
        "uz": "Toshkent sh., Amir Temur shox ko'chasi, 107-uy",
        "ru": "г. Ташкент, пр-т Амира Темура, 107",
        "en": "107 Amir Temur Ave, Tashkent, Uzbekistan",
    },
    "Open on Google Maps": {
        "uz": "Xaritada ochish",
        "ru": "Открыть на карте",
        "en": "Open on Google Maps",
    },
    "Phone": {
        "uz": "Telefon",
        "ru": "Телефон",
        "en": "Phone",
    },
    "Email": {
        "uz": "Elektron pochta",
        "ru": "Электронная почта",
        "en": "Email",
    },
    "Working Hours": {
        "uz": "Ish vaqti",
        "ru": "Режим работы",
        "en": "Working Hours",
    },
    "24/7 Round-the-clock": {
        "uz": "24/7 Kechayu-kunduz xizmat",
        "ru": "24/7 Круглосуточный сервис",
        "en": "24/7 Round-the-clock service",
    },
    "Send Us A Message": {
        "uz": "Bizga Xabar Yuboring",
        "ru": "Напишите Нам Сообщение",
        "en": "Send Us A Message",
    },
    "Subject": {
        "uz": "Mavzu",
        "ru": "Тема",
        "en": "Subject",
    },
    "Your Message": {
        "uz": "Xabaringiz",
        "ru": "Ваше сообщение",
        "en": "Your Message",
    },
    "Send Message": {
        "uz": "Xabarni yuborish",
        "ru": "Отправить сообщение",
        "en": "Send Message",
    },

    # --- Footer ---
    "Useful Links": {
        "uz": "Foydali Havolalar",
        "ru": "Полезные Ссылки",
        "en": "Useful Links",
    },
    "Exclusive Services": {
        "uz": "Eksklyuziv Xizmatlar",
        "ru": "Эксклюзивные Услуги",
        "en": "Exclusive Services",
    },
    "Contact Information": {
        "uz": "Aloqa Ma'lumotlari",
        "ru": "Контактная Информация",
        "en": "Contact Information",
    },
    "Footer About Text": {
        "uz": "Toshkentning qoq markazida joylashgan 5 yulduzli hashamat maskani. Biz har bir mehmonimizga shohona qulaylik, sharqona mehmondo‘stlik va unutilmas xotiralarni taqdim etamiz.",
        "ru": "5-звездочный оазис роскоши в самом сердце Ташкента. Мы дарим каждому гостю королевский комфорт, восточное гостеприимство и незабываемые впечатления.",
        "en": "A 5-star haven of luxury in the heart of Tashkent. We offer royal comfort, genuine hospitality, and unforgettable memories to every guest.",
    },
    "Accepted Payments:": {
        "uz": "Qabul qilinadigan to'lovlar:",
        "ru": "Принимаемые способы оплаты:",
        "en": "Accepted Payments:",
    },
    "100% Secure Booking System": {
        "uz": "100% Xavfsiz bron qilish tizimi",
        "ru": "100% Безопасная система бронирования",
        "en": "100% Secure Booking System",
    },
    "All Rights Reserved": {
        "uz": "Barcha huquqlar himoyalangan.",
        "ru": "Все права защищены.",
        "en": "All Rights Reserved.",
    },

    # --- Floating Widgets & Modals ---
    "Quick Contact": {
        "uz": "Tezkor Aloqa",
        "ru": "Быстрая Связь",
        "en": "Quick Contact",
    },
    "Telegram Chat": {
        "uz": "Telegram orqali bog'lanish",
        "ru": "Связаться в Telegram",
        "en": "Telegram Chat",
    },
    "Call": {
        "uz": "Qo'ng'iroq qilish",
        "ru": "Позвонить нам",
        "en": "Call",
    },
    "Back to top": {
        "uz": "Yuqoriga qaytish",
        "ru": "Наверх",
        "en": "Back to top",
    },
    "Close": {
        "uz": "Yopish",
        "ru": "Закрыть",
        "en": "Close",
    },
    "Submit Request": {
        "uz": "Murojaatni yuborish",
        "ru": "Отправить заявку",
        "en": "Submit Request",
    },
    "VIP Transfer Booking": {
        "uz": "VIP Transfer Buyurtma Qilish",
        "ru": "Заказ VIP Трансфера",
        "en": "VIP Transfer Booking",
    },
    "Pickup Location": {
        "uz": "Kutib olish joyi",
        "ru": "Место встречи",
        "en": "Pickup Location",
    },
    "Car Category": {
        "uz": "Avtomobil toifasi",
        "ru": "Категория автомобиля",
        "en": "Car Category",
    },
    "Arrival Date": {
        "uz": "Kutib olish sanasi",
        "ru": "Дата прибытия",
        "en": "Arrival Date",
    },
    "Approximate Time / Flight Number": {
        "uz": "Taxminiy vaqt / Reys raqami",
        "ru": "Время / Номер рейса",
        "en": "Approximate Time / Flight Number",
    },
}

def generate_translations():
    languages = ['uz', 'ru', 'en']
    for lang in languages:
        lang_dir = LOCALE_DIR / lang / 'LC_MESSAGES'
        lang_dir.mkdir(parents=True, exist_ok=True)
        
        po_path = lang_dir / 'django.po'
        mo_path = lang_dir / 'django.mo'
        
        po = polib.POFile()
        po.metadata = {
            'Project-Id-Version': 'Deluxe Hotel 1.0',
            'Report-Msgid-Bugs-To': 'info@deluxe-hotel.uz',
            'POT-Creation-Date': '2026-11-19 22:30+0500',
            'PO-Revision-Date': '2026-11-19 22:30+0500',
            'Last-Translator': 'Antigravity <support@deluxe.uz>',
            'Language-Team': f'{lang}',
            'Language': lang,
            'MIME-Version': '1.0',
            'Content-Type': 'text/plain; charset=UTF-8',
            'Content-Transfer-Encoding': '8bit',
        }
        
        for msgid, translations in TRANSLATIONS.items():
            msgstr = translations.get(lang, msgid)
            entry = polib.POEntry(
                msgid=msgid,
                msgstr=msgstr,
            )
            po.append(entry)
            
        po.save(str(po_path))
        po.save_as_mofile(str(mo_path))
        print(f"Generated {lang}: {len(po)} entries -> {mo_path}")

if __name__ == '__main__':
    generate_translations()
