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

    # --- FAQ Section ---
    "Check-in and Check-out policy question": {
        "uz": "Check-in va Check-out vaqtlari qanday belgilangan?",
        "ru": "Как установлены часы заезда (Check-in) и выезда (Check-out)?",
        "en": "What are the check-in and check-out times?",
    },
    "Check-in and Check-out policy answer": {
        "uz": "Xonaga kirish (Check-in) soat 14:00 dan boshlanadi, xonani topshirish (Check-out) esa soat 12:00 gacha amalga oshiriladi. 24/7 qabulxonamiz bilan kelishilgan holda bepul yoki qo'shimcha qulaylik bilan erta kelish/kech ketishga ruxsat beriladi.",
        "ru": "Заезд (Check-in) начинается с 14:00, а выезд (Check-out) осуществляется до 12:00. При наличии свободных номеров и по согласованию с круглосуточной стойкой регистрации возможен ранний заезд или поздний выезд.",
        "en": "Check-in starts at 14:00 and check-out is until 12:00. Early check-in or late check-out is available upon request with our 24/7 front desk subject to room availability.",
    },
    "Breakfast included question": {
        "uz": "Nonushta xona narxiga kiritilganmi va qaysi vaqtda beriladi?",
        "ru": "Включен ли завтрак в стоимость номера и в какое время он подается?",
        "en": "Is breakfast included in the room rate and what are the serving hours?",
    },
    "Breakfast included answer": {
        "uz": "Ha, Deluxe Hotelning barcha xonalar toifasi uchun shohona shved stoli (Buffet) nonushtasi narxga to'liq kiritilgan. Nonushta har kuni 07:00 dan 10:30 gacha restoranimizda tortiladi yoki xonangizga keltiriladi.",
        "ru": "Да, для всех категорий номеров Deluxe Hotel роскошный завтрак «шведский стол» (Buffet) полностью включен в стоимость. Завтрак сервируется ежедневно с 07:00 до 10:30 в ресторане или доставляется в номер.",
        "en": "Yes, a lavish buffet breakfast is complimentary for all room categories at Deluxe Hotel. Breakfast is served daily from 07:00 to 10:30 in our main restaurant or delivered to your room.",
    },
    "Accepted payment methods question": {
        "uz": "Qanday to‘lov usullari qabul qilinadi?",
        "ru": "Какие способы оплаты принимаются?",
        "en": "What payment methods are accepted?",
    },
    "Accepted payment methods answer": {
        "uz": "Biz barcha ommabop to'lov tizimlarini qabul qilamiz: UzCard, Humo, Visa, MasterCard, naqd to'lov, shuningdek Payme va Click ilovalari orqali to'lovlar.",
        "ru": "Мы принимаем все популярные платежные системы: карты UzCard, Humo, Visa, MasterCard, наличный расчет, а также платежи через приложения Payme и Click.",
        "en": "We accept all major payment systems: UzCard, Humo, Visa, MasterCard, cash upon arrival, as well as mobile payments via Payme and Click.",
    },
    "Airport transfer order question": {
        "uz": "Aeroport yoki vokzaldan transfer qanday buyurtma qilinadi?",
        "ru": "Как заказать трансфер из аэропорта или вокзала?",
        "en": "How can I arrange an airport or railway transfer?",
    },
    "Airport transfer order answer": {
        "uz": "Mehmonxonamiz shaxsiy biznes-klass avtoparkiga (Mercedes E-Class, VIP Minivan) ega. Saytimizdagi VIP Transfer oynasi orqali yoki resepshnga murojaat qilib reys raqamini aytsangiz, shaxsiy haydovchimiz sizni kutib oladi.",
        "ru": "У нас собственный автопарк бизнес-класса (Mercedes E-Class, VIP Minivan). Закажите трансфер через онлайн-форму на сайте или свяжитесь со стойкой регистрации, указав номер рейса.",
        "en": "Our hotel operates an executive fleet (Mercedes E-Class, VIP Minivans). You can order a transfer via our online modal or inform reception of your flight details for a personal pickup.",
    },
    "Children accommodation policy question": {
        "uz": "Bolalar bilan tashrif buyurganda shartlar qanaqa?",
        "ru": "Каковы условия проживания с детьми?",
        "en": "What is the policy for children staying at the hotel?",
    },
    "Children accommodation policy answer": {
        "uz": "6 yoshgacha bo'lgan bolalar ota-onasi bilan alohida o'rin talab qilinmagan holda mutlaqo bepul istiqomat qilishadi. Shuningdek, talabingizga binoan bepul bolalar karavotcha (Baby cot) taqdim etiladi.",
        "ru": "Дети до 6 лет проживают бесплатно без предоставления отдельного спального места. По запросу в номер бесплатно предоставляется детская кроватка.",
        "en": "Children under 6 stay free of charge when sharing existing bedding. Complimentary baby cots are also available upon request.",
    },
    "Cancellation policy question": {
        "uz": "Bronni bekor qilish (Cancellation policy) tartibi qanday?",
        "ru": "Каковы правила и условия отмены бронирования?",
        "en": "What is the cancellation policy?",
    },
    "Cancellation policy answer": {
        "uz": "Mehmonxonaga kelish rejalashtirilgan sanadan kamida 24 soat oldin xonani bekor qilsangiz, jarimasiz to'liq qaytariladi yoki boshqa sanaga ko'chiriladi.",
        "ru": "При отмене бронирования не менее чем за 24 часа до заезда штраф не взимается, предоплата возвращается в полном объеме или бронь переносится на другие даты.",
        "en": "Free cancellation is available up to 24 hours prior to scheduled arrival with 100% refund or free date modification.",
    },

    # --- Services & Stats ---
    "24/7 Resepshn & Konsyerj": {
        "uz": "24/7 Resepshn & Konsyerj",
        "ru": "24/7 Ресепшн и Консьерж",
        "en": "24/7 Front Desk & Concierge",
    },
    "Kechayu-kunduz professional qabulxona va konsyerj xizmati. Mehmonlarimizning har qanday iltimos yoki savollariga istalgan vaqtda darhol javob beramiz.": {
        "uz": "Kechayu-kunduz professional qabulxona va konsyerj xizmati. Mehmonlarimizning har qanday iltimos yoki savollariga istalgan vaqtda darhol javob beramiz.",
        "ru": "Круглосуточная профессиональная служба приема и консьерж-сервис. Мы оперативно реагируем на любые пожелания и вопросы наших гостей.",
        "en": "Round-the-clock professional reception and concierge service. We attend to every guest request and inquiry promptly at any time.",
    },
    "24/7 XIZMAT": {
        "uz": "24/7 XIZMAT",
        "ru": "24/7 СЕРВИС",
        "en": "24/7 SERVICE",
    },
    "Bog'lanish / Qo'ng'iroq": {
        "uz": "Bog'lanish / Qo'ng'iroq",
        "ru": "Связаться / Позвонить",
        "en": "Call / Contact",
    },
    "Tezkor ro'yxatga olish & Checkout": {
        "uz": "Tezkor ro'yxatga olish & Checkout",
        "ru": "Экспресс регистрация и выезд",
        "en": "Express Check-in & Check-out",
    },
    "Bagaj saqlash va eltib berish": {
        "uz": "Bagaj saqlash va eltib berish",
        "ru": "Хранение и доставка багажа",
        "en": "Luggage Storage & Delivery",
    },
    "24/7 konsyerj va qo'llab-quvvatlash": {
        "uz": "24/7 konsyerj va qo'llab-quvvatlash",
        "ru": "24/7 поддержка и консьерж",
        "en": "24/7 Concierge Support",
    },
    "Restoran & Bar": {
        "uz": "Restoran & Bar",
        "ru": "Ресторан & Бар",
        "en": "Restaurant & Bar",
    },
    "Yevropa va sharqona taomlarning boy mualliflik menyusi, elit sharoblar kolleksiyasi hamda shinam muhitda sokin jonli musiqa sadolari.": {
        "uz": "Yevropa va sharqona taomlarning boy mualliflik menyusi, elit sharoblar kolleksiyasi hamda shinam muhitda sokin jonli musiqa sadolari.",
        "ru": "Богатое авторское меню европейских и восточных блюд, коллекция элитных вин и живая музыка в уютной атмосфере.",
        "en": "Rich signature menu of European and Oriental cuisine, fine wine selection and live acoustic music in a sophisticated ambiance.",
    },
    "GOURMET": {
        "uz": "GOURMET",
        "ru": "ГУРМЕ",
        "en": "GOURMET",
    },
    "Menyu & Stol band qilish": {
        "uz": "Menyu & Stol band qilish",
        "ru": "Меню и Бронь столика",
        "en": "Menu & Reserve Table",
    },
    "Shohona shved stoli nonushtasi": {
        "uz": "Shohona shved stoli nonushtasi",
        "ru": "Королевский завтрак «шведский стол»",
        "en": "Lavish Buffet Breakfast",
    },
    "A-la-carte kechki ovqat menyusi": {
        "uz": "A-la-carte kechki ovqat menyusi",
        "ru": "Меню ужина a-la-carte",
        "en": "A-la-carte Dinner Menu",
    },
    "Onlayn stol band qilish xizmati": {
        "uz": "Onlayn stol band qilish xizmati",
        "ru": "Онлайн бронирование столиков",
        "en": "Online Table Reservation",
    },
    "VIP Transfer Xizmati": {
        "uz": "VIP Transfer Xizmati",
        "ru": "VIP Трансфер сервис",
        "en": "VIP Transfer Service",
    },
    "Toshkent xalqaro aeroporti va vokzallardan hashamatli biznes-klass avtomobillarda kutib olish hamda manzilga qulay yetkazish xizmati.": {
        "uz": "Toshkent xalqaro aeroporti va vokzallardan hashamatli biznes-klass avtomobillarda kutib olish hamda manzilga qulay yetkazish xizmati.",
        "ru": "Встреча в международном аэропорту Ташкента и на вокзалах на роскошных автомобилях бизнес-класса и комфортная доставка.",
        "en": "Luxury business-class airport and railway transfers with personal meet-and-greet in Tashkent.",
    },
    "PREMIUM TRANSPORT": {
        "uz": "PREMIUM TRANSPORT",
        "ru": "ПРЕМИУМ ТРАНСПОРТ",
        "en": "PREMIUM TRANSPORT",
    },
    "Transfer buyurtma qilish": {
        "uz": "Transfer buyurtma qilish",
        "ru": "Заказать трансфер",
        "en": "Book Transfer",
    },
    "Aeroportda kutib olish va kuzatish": {
        "uz": "Aeroportda kutib olish va kuzatish",
        "ru": "Встреча и проводы в аэропорту",
        "en": "Airport Meet & Greet",
    },
    "Mercedes & VIP Minivan avtoparki": {
        "uz": "Mercedes & VIP Minivan avtoparki",
        "ru": "Автопарк Mercedes и VIP Minivan",
        "en": "Mercedes & VIP Minivan Fleet",
    },
    "Konditsioner, Wi-Fi va ichimliklar": {
        "uz": "Konditsioner, Wi-Fi va ichimliklar",
        "ru": "Кондиционер, Wi-Fi и прохладительные напитки",
        "en": "Climate Control, Wi-Fi & Drinks",
    },
    "Mamnun Mehmonlar": {
        "uz": "Mamnun Mehmonlar",
        "ru": "Довольных гостей",
        "en": "Satisfied Guests",
    },
    "Hashamatli Xonalar": {
        "uz": "Hashamatli Xonalar",
        "ru": "Роскошных номеров",
        "en": "Luxury Rooms",
    },
    "Professional Xodimlar": {
        "uz": "Professional Xodimlar",
        "ru": "Профессиональных сотрудников",
        "en": "Professional Staff",
    },
    "Yillik Tajriba": {
        "uz": "Yillik Tajriba",
        "ru": "Лет безупречного опыта",
        "en": "Years of Experience",
    },

    # --- Modals ---
    "Or leave your contact information and our front desk will call you back within 3 minutes:": {
        "uz": "Yoki aloqa ma'lumotlaringizni qoldiring, resepshn navbatchi xodimi 3 daqiqa ichida sizga qo'ng'iroq qiladi:",
        "ru": "Или оставьте свои контактные данные, и дежурный администратор перезвонит вам в течение 3 минут:",
        "en": "Or leave your contact details and our front desk will call you back within 3 minutes:",
    },
    "Your Name": {
        "uz": "Ismingiz",
        "ru": "Ваше имя",
        "en": "Your Name",
    },
    "Your Phone Number": {
        "uz": "Telefon raqamingiz",
        "ru": "Номер телефона",
        "en": "Your Phone Number",
    },
    "Request or Question (Optional)": {
        "uz": "Iltimos yoki savolingiz (ixtiyoriy)",
        "ru": "Пожелание или вопрос (необязательно)",
        "en": "Request or Question (Optional)",
    },
    "Room service, wake-up call or special request...": {
        "uz": "Xona xizmati, uyg'otish vaqti yoki qo'shimcha so'rov...",
        "ru": "Обслуживание в номере, будильник или пожелание...",
        "en": "Room service, wake-up call or special request...",
    },
    "Submit Request": {
        "uz": "Murojaatni yuborish",
        "ru": "Отправить заявку",
        "en": "Submit Request",
    },
    "Islam Karimov Tashkent Airport (TAS)": {
        "uz": "Islom Karimov Toshkent Aeroporti (TAS)",
        "ru": "Аэропорт Ташкента им. Ислама Каримова (TAS)",
        "en": "Islam Karimov Tashkent Airport (TAS)",
    },
    "Northern Railway Station (Central)": {
        "uz": "Shimoliy Vokzal (Toshkent)",
        "ru": "Северный вокзал (Центральный)",
        "en": "Northern Railway Station (Central)",
    },
    "Southern Railway Station": {
        "uz": "Janubiy Vokzal",
        "ru": "Южный вокзал",
        "en": "Southern Railway Station",
    },
    "Hotel to Airport Transfer": {
        "uz": "Mehmonxonadan Aeroportga kuzatish",
        "ru": "Трансфер из отеля в аэропорт",
        "en": "Hotel to Airport Transfer",
    },
    "Custom City Route": {
        "uz": "Shahar ichida shaxsiy marshrut",
        "ru": "Индивидуальный маршрут по городу",
        "en": "Custom City Route",
    },
    "Business Sedan (Mercedes E-Class / BYD)": {
        "uz": "Business Sedan (Mercedes E-Class / BYD)",
        "ru": "Бизнес-седан (Mercedes E-Class / BYD)",
        "en": "Business Sedan (Mercedes E-Class / BYD)",
    },
    "VIP Minivan (Mercedes V-Class, 6-7 pax)": {
        "uz": "VIP Minivan (Mercedes V-Class, 6-7 kishi)",
        "ru": "VIP Минивэн (Mercedes V-Class, 6-7 мест)",
        "en": "VIP Minivan (Mercedes V-Class, 6-7 pax)",
    },
    "Executive SUV (Lexus / Land Cruiser)": {
        "uz": "Executive SUV (Lexus / Land Cruiser)",
        "ru": "Представительский внедорожник (Lexus / Land Cruiser)",
        "en": "Executive SUV (Lexus / Land Cruiser)",
    },
    "Deluxe Hotel - Virtual Video Tour": {
        "uz": "Deluxe Hotel - Virtual Video Sayohat",
        "ru": "Deluxe Hotel — Виртуальный видеотур",
        "en": "Deluxe Hotel - Virtual Video Tour",
    },
    "Open on YouTube": {
        "uz": "YouTube'da ochish",
        "ru": "Открыть на YouTube",
        "en": "Open on YouTube",
    },
    "Virtual video overview of Deluxe Hotel 5-star luxury destination": {
        "uz": "Deluxe Hotel 5-yulduzli hashamat maskanining virtual video sharhi",
        "ru": "Виртуальный видеообзор 5-звездочного роскошного отеля Deluxe",
        "en": "Virtual video overview of Deluxe Hotel 5-star luxury destination",
    },
    "Subscribe to YouTube Channel": {
        "uz": "YouTube kanalimizga obuna bo'ling",
        "ru": "Подписывайтесь на наш YouTube канал",
        "en": "Subscribe to YouTube Channel",
    },
    "Leave A Guest Review": {
        "uz": "Mehmonxona Haqida Fikr Bildirish",
        "ru": "Оставить отзыв об отеле",
        "en": "Leave A Guest Review",
    },
    "Your feedback is very valuable to us! Leave your honest review about your stay at Deluxe Hotel:": {
        "uz": "Sizning samimiy fikringiz biz uchun juda qadrlidir! Deluxe Hotelda o'tkazgan dam olishingiz yoki xizmat sifati haqida o'z xolis taassurotlaringizni qoldiring:",
        "ru": "Ваш отзыв очень важен для нас! Поделитесь впечатлениями о вашем отдыхе и сервисе в Deluxe Hotel:",
        "en": "Your feedback is very valuable to us! Leave your honest review about your stay at Deluxe Hotel:",
    },
    "Your Rating": {
        "uz": "Bahoyingiz (Reyting)",
        "ru": "Ваша оценка",
        "en": "Your Rating",
    },
    "5 stars (Excellent!)": {
        "uz": "5 yulduz (A'lo darajada!)",
        "ru": "5 звезд (Превосходно!)",
        "en": "5 stars (Excellent!)",
    },
    "City or Status": {
        "uz": "Shahar yoki Maqomingiz",
        "ru": "Город или статус",
        "en": "City or Status",
    },
    "e.g. Tourist, Tashkent": {
        "uz": "Masalan: Sayyoh, Toshkent",
        "ru": "Например: Турист, Санкт-Петербург",
        "en": "e.g. Tourist, London",
    },
    "Your Review & Impressions": {
        "uz": "Fikr va taassurotlaringiz",
        "ru": "Ваш отзыв и впечатления",
        "en": "Your Review & Impressions",
    },
    "Cleanliness, hospitality, restaurant and general impressions...": {
        "uz": "Xonalar tozaligi, mehmondo'stlik, restoran va umumiy taassurotlaringiz...",
        "ru": "Чистота номеров, гостеприимство, ресторан и общие впечатления...",
        "en": "Room cleanliness, hospitality, restaurant and impressions...",
    },
    "Photo or Selfie (Optional)": {
        "uz": "Rasmingiz yoki selfi (ixtiyoriy)",
        "ru": "Фотография или селфи (необязательно)",
        "en": "Photo or Selfie (Optional)",
    },
    "Submit Review": {
        "uz": "Fikrimni e'lon qilish",
        "ru": "Опубликовать отзыв",
        "en": "Submit Review",
    },

    # --- Payment Methods & Hints ---
    "Cash Payment": {
        "uz": "Naqd to'lov",
        "ru": "Оплата наличными",
        "en": "Cash Payment",
    },
    "Pay cash at the front desk upon check-in": {
        "uz": "Mehmonxonaga joylashish vaqtida qabulxonada naqd to'lash",
        "ru": "Оплата наличными на стойке регистрации при заселении",
        "en": "Pay cash at the front desk upon check-in",
    },
    "National bank card payment (terminal or online)": {
        "uz": "Milliy bank kartasi orqali to'lov (terminal yoki onlayn)",
        "ru": "Оплата национальной картой UzCard (через терминал или онлайн)",
        "en": "National bank card payment (terminal or online)",
    },
    "Contactless Humo bank card payment": {
        "uz": "Humo kontaktsiz bank kartasi orqali to'lov",
        "ru": "Оплата бесконтактной картой Humo",
        "en": "Contactless Humo bank card payment",
    },
    "International bank card payment": {
        "uz": "Xalqaro xorijiy bank kartalari orqali to'lov",
        "ru": "Оплата международными банковскими картами Visa / MasterCard",
        "en": "International bank card payment",
    },
    "Direct payment link via Payme app": {
        "uz": "Payme ilovasi orqali to'g'ridan-to'g'ri to'lov havolasi",
        "ru": "Прямой платеж через приложение Payme",
        "en": "Direct payment link via Payme app",
    },
    "Convenient and fast payment via Click Up": {
        "uz": "Click Up ilovasi orqali qulay va tezkor to'lov",
        "ru": "Удобная и быстрая оплата через Click Up",
        "en": "Convenient and fast payment via Click Up",
    },
    "Cash payment hint": {
        "uz": "Mehmonxonaga tashrif buyurib (Check-in), qabulxonada naqd pul (so'm yoki valyuta) shaklida to'lashingiz mumkin.",
        "ru": "Вы можете оплатить проживание наличными (в сумах или валюте) на стойке регистрации при заселении (Check-in).",
        "en": "You can pay in cash (UZS or foreign currency) directly at the front desk upon arrival (Check-in).",
    },
    "UzCard payment hint": {
        "uz": "UzCard bank kartasi orqali to'lov qabulxonadagi terminal orqali yoki administrator yuboradigan to'lov havolasi yordamida amalga oshiriladi.",
        "ru": "Оплата картой UzCard производится через терминал на стойке регистрации или по платежной ссылке администратора.",
        "en": "UzCard payment can be processed via terminal at reception or through a secure payment link sent by the manager.",
    },
    "Humo payment hint": {
        "uz": "Humo kontaktsiz to'lov kartasi orqali qabulxonada bir zumda yoki onlayn to'lov orqali hisob-kitob qilish mumkin.",
        "ru": "Оплата бесконтактной картой Humo возможна моментально на стойке регистрации или онлайн.",
        "en": "Humo contactless card payments can be settled instantly at reception or online.",
    },
    "Visa payment hint": {
        "uz": "Visa yoki MasterCard xalqaro kartalari qabulxonadagi ko'p valyutali POS-terminallar orqali qulay qabul qilinadi.",
        "ru": "Международные карты Visa и MasterCard принимаются через мультивалютные POS-терминалы отеля.",
        "en": "International Visa and MasterCard cards are accepted via our multicurrency POS terminals.",
    },
    "Payme payment hint": {
        "uz": "Buyurtma berilgach, administratorimiz siz bilan bog'lanib, Payme to'lov havolasi yoki QR-kodini taqdim etadi.",
        "ru": "После оформления администратор свяжется с вами и предоставит платежную ссылку или QR-код Payme.",
        "en": "Upon booking, our manager will contact you with a Payme payment link or QR code.",
    },
    "Click payment hint": {
        "uz": "Buyurtmangiz qabul qilingach, Click Up orqali bir martalik to'lov hisobi yuboriladi yoki qabulxonada to'lashingiz mumkin.",
        "ru": "После оформления вам будет выставлен счет в приложении Click Up или вы можете оплатить на месте.",
        "en": "An invoice will be generated in your Click Up app, or you can pay via Click at the front desk.",
    },

    # --- Booking Model Choices & Status ---
    "Kutilmoqda": {
        "uz": "Kutilmoqda",
        "ru": "Ожидает подтверждения",
        "en": "Pending",
    },
    "Tasdiqlangan": {
        "uz": "Tasdiqlangan",
        "ru": "Подтверждено",
        "en": "Confirmed",
    },
    "Bekor qilingan": {
        "uz": "Bekor qilingan",
        "ru": "Отменено",
        "en": "Cancelled",
    },
    "Naqd to'lov (Mehmonxonada to'lash)": {
        "uz": "Naqd to'lov (Mehmonxonada to'lash)",
        "ru": "Наличный расчет (в отеле)",
        "en": "Cash payment (at hotel)",
    },
    "UzCard (Bank kartasi)": {
        "uz": "UzCard (Bank kartasi)",
        "ru": "UzCard (Банковская карта)",
        "en": "UzCard (Bank card)",
    },
    "Humo (Bank kartasi)": {
        "uz": "Humo (Bank kartasi)",
        "ru": "Humo (Банковская карта)",
        "en": "Humo (Bank card)",
    },
    "Visa / MasterCard (Xalqaro karta)": {
        "uz": "Visa / MasterCard (Xalqaro karta)",
        "ru": "Visa / MasterCard (Международная карта)",
        "en": "Visa / MasterCard (International card)",
    },
    "Payme ilovasi": {
        "uz": "Payme ilovasi",
        "ru": "Приложение Payme",
        "en": "Payme app",
    },
    "Click ilovasi": {
        "uz": "Click ilovasi",
        "ru": "Приложение Click",
        "en": "Click app",
    },
    "Kelganda to'lanadi": {
        "uz": "Kelganda to'lanadi",
        "ru": "Оплата при заезде",
        "en": "Pay on arrival",
    },
    "To'lov kutilmoqda": {
        "uz": "To'lov kutilmoqda",
        "ru": "Ожидается оплата",
        "en": "Payment pending",
    },
    "To'langan": {
        "uz": "To'langan",
        "ru": "Оплачено",
        "en": "Paid",
    },
    "Hotel Rooms": {
        "uz": "Mehmonxona Xonalari",
        "ru": "Номера в отеле",
        "en": "Hotel Rooms",
    },
    "Restaurant Table Reservations": {
        "uz": "Restoran Stol Bronlari",
        "ru": "Бронирование столиков в ресторане",
        "en": "Restaurant Table Reservations",
    },
    "Table Reservation:": {
        "uz": "Stol bron:",
        "ru": "Бронь столика:",
        "en": "Table Reservation:",
    },
    "Check-in:": {
        "uz": "Kelish:",
        "ru": "Заезд:",
        "en": "Check-in:",
    },
    "Check-out:": {
        "uz": "Ketish:",
        "ru": "Выезд:",
        "en": "Check-out:",
    },
    "Guests:": {
        "uz": "Mehmonlar:",
        "ru": "Гости:",
        "en": "Guests:",
    },
    "Payment:": {
        "uz": "To'lov:",
        "ru": "Оплата:",
        "en": "Payment:",
    },
    "Total:": {
        "uz": "Jami summa:",
        "ru": "Итого:",
        "en": "Total:",
    },
    "Booking Date:": {
        "uz": "Buyurtma sanasi:",
        "ru": "Дата заказа:",
        "en": "Booking Date:",
    },
    "Guest Name:": {
        "uz": "Mijoz ismi:",
        "ru": "Имя гостя:",
        "en": "Guest Name:",
    },
    "Special Request:": {
        "uz": "Maxsus istaklar:",
        "ru": "Особые пожелания:",
        "en": "Special Request:",
    },
    "No Bookings Found": {
        "uz": "Hech qanday buyurtma topilmadi",
        "ru": "Бронирований не найдено",
        "en": "No Bookings Found",
    },
    "No booking found with this phone number. Please check the entered number.": {
        "uz": "Ushbu telefon raqami bilan rasmiylashtirilgan bron topilmadi. Raqamni tekshirib qayta urinib ko'ring.",
        "ru": "По указанному номеру телефона бронирований не найдено. Проверьте правильность введенного номера.",
        "en": "No booking was found with this phone number. Please check the number and try again.",
    },
    "Track your reservation status easily!": {
        "uz": "Buyurtma holatini bilish oson!",
        "ru": "Узнайте статус вашей брони легко!",
        "en": "Track your reservation status easily!",
    },
    "Enter your phone number above to see the current status of all your room and table bookings.": {
        "uz": "Yuqoridagi maydonga telefon raqamingizni kiriting va barcha xona hamda restoran buyurtmalaringiz holatini bilib oling.",
        "ru": "Введите номер телефона выше, чтобы проверить статус всех ваших бронирований номеров и столиков.",
        "en": "Enter your phone number above to check the status of all your room and restaurant table bookings.",
    },

    # --- Room Details, Views, Amenities ---
    "Sea View": {
        "uz": "Dengiz manzarasi",
        "ru": "Вид на море",
        "en": "Sea View",
    },
    "City View": {
        "uz": "Shahar manzarasi",
        "ru": "Вид на город",
        "en": "City View",
    },
    "Garden View": {
        "uz": "Bog' manzarasi",
        "ru": "Вид на сад",
        "en": "Garden View",
    },
    "Mountain View": {
        "uz": "Tog' manzarasi",
        "ru": "Вид на горы",
        "en": "Mountain View",
    },
    "Ocean View": {
        "uz": "Okean manzarasi",
        "ru": "Вид на океан",
        "en": "Ocean View",
    },
    "beds": {
        "uz": "ta karavot",
        "ru": "кровати",
        "en": "beds",
    },
    "Fast Wi-Fi (Free)": {
        "uz": "Tezkor Wi-Fi (Bepul)",
        "ru": "Скоростной Wi-Fi (Бесплатно)",
        "en": "Fast Wi-Fi (Free)",
    },
    "Air Conditioning & Heating": {
        "uz": "Konditsioner & Isitish",
        "ru": "Кондиционер и отопление",
        "en": "Air Conditioning & Heating",
    },
    "55 4K Smart TV": {
        "uz": "55\" 4K Smart TV",
        "ru": "55\" 4K Smart TV",
        "en": "55\" 4K Smart TV",
    },
    "Coffee Machine & Tea": {
        "uz": "Qahva mashinasi & Choy",
        "ru": "Кофемашина и чайный набор",
        "en": "Coffee Machine & Tea",
    },
    "Jacuzzi / Marble Bath": {
        "uz": "Jakuzzi / Marmar vanna",
        "ru": "Джакузи / Мраморная ванна",
        "en": "Jacuzzi / Marble Bath",
    },
    "Private Balcony & View": {
        "uz": "Shaxsiy balkon & Manzara",
        "ru": "Личный балкон с панорамой",
        "en": "Private Balcony & View",
    },
    "Personal Safe": {
        "uz": "Shaxsiy seyf",
        "ru": "Сейф в номере",
        "en": "Personal Safe",
    },
    "24/7 Room Service": {
        "uz": "24/7 Xona xizmati",
        "ru": "Круглосуточное обслуживание в номерах",
        "en": "24/7 Room Service",
    },
    "Laundry & Ironing": {
        "uz": "Kir yuvish & Dazmol",
        "ru": "Прачечная и глажка",
        "en": "Laundry & Ironing",
    },
    "Room Photo Gallery": {
        "uz": "Xona fotogalereyasi",
        "ru": "Фотогалерея номера",
        "en": "Room Photo Gallery",
    },
    "Explore every corner and amenity of this room": {
        "uz": "Ushbu xonaning har bir go'shasi va qulayliklari bilan yaqindan tanishing",
        "ru": "Ознакомьтесь с каждым уголком и удобствами этого номера",
        "en": "Explore every corner and amenity of this room",
    },
    "This luxury room at Deluxe Hotel offers you premier elegance, peace and comfort. Featuring modern interior design, free high-speed Wi-Fi, individual climate control, fully stocked minibar and private marble bathroom at your service.": {
        "uz": "Deluxe mehmonxonasidagi ushbu xona sizga yuqori darajadagi hashamat, osoyishtalik va qulaylikni taqdim etadi. Zamonaviy dizayn, bepul yuqori tezlikdagi Wi-Fi, mikroiqlim konditsioneri, to'liq jihozlangan mini-bar hamda shaxsiy marmar vanna xonasi sizning xizmatingizda.",
        "ru": "Этот роскошный номер в Deluxe Hotel дарит вам непревзойденный комфорт и умиротворение. К вашим услугам современный авторский интерьер, скоростной Wi-Fi, климат-контроль, укомплектованный мини-бар и ванная комната из натурального мрамора.",
        "en": "This luxury room at Deluxe Hotel offers you premier elegance, peace and comfort. Featuring modern interior design, free high-speed Wi-Fi, individual climate control, fully stocked minibar and private marble bathroom at your service.",
    },

    # --- Restaurant Categories ---
    "O'zbek Milliy Taomlari": {
        "uz": "O'zbek Milliy Taomlari",
        "ru": "Узбекские национальные блюда",
        "en": "Uzbek National Cuisine",
    },
    "Asosiy taomlar": {
        "uz": "Asosiy taomlar",
        "ru": "Основные блюда",
        "en": "Main Courses",
    },
    "Salatlar va Gazaklar": {
        "uz": "Salatlar va Gazaklar",
        "ru": "Салаты и закуски",
        "en": "Salads & Appetizers",
    },
    "Nonushta": {
        "uz": "Nonushta",
        "ru": "Завтраки",
        "en": "Breakfast",
    },
    "Shirinliklar va Ichimliklar": {
        "uz": "Shirinliklar va Ichimliklar",
        "ru": "Десерты и напитки",
        "en": "Desserts & Beverages",
    },
    "Recommended": {
        "uz": "Tavsiya etiladi",
        "ru": "Рекомендуем",
        "en": "Recommended",
    },
    "Delicious dish prepared according to our chef's signature recipe.": {
        "uz": "Oshpazimizning maxsus retsepti asosida tayyorlangan lazzatli taom.",
        "ru": "Изысканное блюдо, приготовленное по авторскому рецепту шеф-повара.",
        "en": "Delicious dish prepared according to our chef's signature recipe.",
    },

    # --- Blog Categories ---
    "Mehmonxona yangiliklari": {
        "uz": "Mehmonxona yangiliklari",
        "ru": "Новости отеля",
        "en": "Hotel News",
    },
    "Restoran & Taomlar": {
        "uz": "Restoran & Taomlar",
        "ru": "Ресторан и кухня",
        "en": "Restaurant & Cuisine",
    },
    "Tadbirlar & To'ylar": {
        "uz": "Tadbirlar & To'ylar",
        "ru": "События и торжества",
        "en": "Events & Weddings",
    },
    "Toshkent Bo'ylab Sayohat": {
        "uz": "Toshkent Bo'ylab Sayohat",
        "ru": "Путешествия по Ташкенту",
        "en": "Tashkent Travel Guide",
    },
    "Mehmonlar uchun Maslahatlar": {
        "uz": "Mehmonlar uchun Maslahatlar",
        "ru": "Советы для гостей",
        "en": "Tips for Guests",
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
