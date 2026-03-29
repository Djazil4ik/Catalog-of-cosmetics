# 🌸 Catalog Project

Элегантный интернет-каталог товаров на Django с минималистичным дизайном и удобной админ-панелью.

## 📋 Описание

Веб-приложение для презентации каталога товаров с категориями, галереями изображений и детальными описаниями. Выполнено в современном минималистичном стиле с использованием бежево-розовой цветовой палитры.

## ✨ Основные возможности

- 📦 Каталог товаров с категориями
- 🖼️ Галерея изображений для каждого товара
- ✅ Список преимуществ товара
- 📝 Богатый текстовый редактор (CKEditor 5) для описаний
- 📱 Адаптивный дизайн
- 📄 Пагинация каталога
- 🔍 Фильтрация по категориям
- 📞 Контактная информация в футере
- 🎨 Элегантный UI с эффектами наведения

## 🛠️ Технологии

- **Backend:** Django 5.1.4
- **Database:** SQLite (можно заменить на PostgreSQL)
- **Frontend:** HTML5, CSS3, JavaScript
- **Rich Text Editor:** django-ckeditor-5
- **Admin Panel:** Jazzmin
- **Deploy:** Docker, Nginx

## 📦 Установка и запуск

### Локальная установка

1. **Клонируйте репозиторий:**
```bash
git clone <repository-url>
cd catalog-project
```

2. **Создайте виртуальное окружение:**
```bash
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac
.venv\Scripts\activate     # для Windows
```

3. **Установите зависимости:**
```bash
pip install -r requirements.txt
```

4. **Создайте файл `.env`:**
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. **Выполните миграции:**
```bash
python manage.py migrate
```

6. **Создайте суперпользователя:**
```bash
python manage.py createsuperuser
```

7. **Соберите статические файлы:**
```bash
python manage.py collectstatic
```

8. **Запустите сервер:**
```bash
python manage.py runserver
```

Сайт будет доступен по адресу: `http://127.0.0.1:8000`

### Запуск через Docker

1. **Создайте `.env` файл:**
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
```

2. **Запустите контейнеры:**
```bash
docker-compose up -d --build
```

3. **Выполните миграции:**
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

Сайт будет доступен на localhost:8080.

## 📁 Структура проекта

```
.
├── catalog/              # Основное приложение
│   ├── migrations/       # Миграции БД
│   ├── templates/        # HTML шаблоны
│   ├── admin.py          # Настройка админ-панели
│   ├── models.py         # Модели данных
│   ├── views.py          # Представления
│   ├── urls.py           # URL маршруты
│   └── context_processors.py  # Контекстные процессоры
├── core/                 # Настройки проекта
│   ├── settings.py       # Основные настройки
│   └── urls.py           # Главные URL
├── static/               # Статические файлы
│   ├── sakura.png        # Изображение сакуры для футера
│   └── ...
├── media/                # Загруженные файлы
├── nginx/                # Конфигурация Nginx
├── requirements.txt      # Python зависимости
├── Dockerfile            # Docker образ
├── docker-compose.yml    # Docker Compose конфигурация
└── manage.py             # Django CLI
```

## 🎨 Модели данных

### Category (Категория)
- `name` - Название категории
- `slug` - ЧПУ (генерируется автоматически)

### Product (Товар)
- `name` - Название товара
- `description` - Описание (CKEditor)
- `price` - Цена
- `image` - Главное изображение
- `category` - Связь с категорией
- `slug` - ЧПУ (генерируется автоматически)

### ImageGallery (Галерея изображений)
- `product` - Связь с товаром
- `image` - Изображение

### Advantage (Преимущества)
- `product` - Связь с товаром
- `description` - Описание преимущества

### ContactInfo (Контактная информация)
- `phone_number` - Номер телефона
- `whatsapp_number` - WhatsApp (только цифры и +)
- `email` - Email

## 🔐 Админ-панель

Админ-панель доступна по адресу `/admin/`

**Особенности:**
- Стильная тема Jazzmin
- Возможность добавления нескольких изображений к товару
- Редактор CKEditor 5 для описаний
- Ограничение: только одна запись ContactInfo (нельзя удалять и создавать несколько)
- Автоматическая очистка номера WhatsApp от лишних символов

## 🌐 URL маршруты

- `/` - Главная страница с каталогом
- `/category/<slug>/` - Товары конкретной категории
- `/product/<slug>/` - Детальная страница товара
- `/admin/` - Админ-панель

## 🎯 Особенности реализации

### Контекстный процессор
Глобальные данные (категории, контакты) доступны во всех шаблонах автоматически через `context_processors.py`

### Пагинация
Каталог поддерживает пагинацию с сохранением фильтров по категориям

### Галерея изображений
- Главное изображение товара + дополнительные из галереи
- Переключение между изображениями по клику
- Подсветка активной миниатюры

### Адаптивный дизайн
Полностью адаптивная верстка для мобильных устройств и планшетов

## 🚀 Деплой

Проект готов к деплою через Docker:
- Nginx как reverse proxy
- Gunicorn как WSGI сервер
- Автоматический сбор статики
- Volume для media файлов

## 👤 Автор

Djazil / mustafaevdjaz@gmail.com

## 📄 Лицензия

MIT License

---

Сделано с 🌸 и любовью к минимализму