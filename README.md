# ProThemesRU Telegram Bot

🚀 Профессиональный Telegram бот для создания сайтов

## Возможности

* 📚 Библиотека готовых шаблонов
* 🧱 UI компоненты и блоки
* 🎨 Современные стили и эффекты
* 🛠️ Визуальный конструктор сайтов
* 📦 Заказ готовых сайтов

## Команды бота

* `/start` - Главное меню
* `/templates` - Просмотр шаблонов
* `/blocks` - UI компоненты
* `/styles` - Стили и эффекты
* `/constructor` - Конструктор сайтов
* `/order` - Заказать сайт
* `/pricing` - Цены и тарифы
* `/help` - Помощь

## Быстрый запуск

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Настройка переменных окружения

Скопируйте `env.example` в `.env` и заполните:

```bash
cp env.example .env
```

Отредактируйте `.env`:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_ADMIN_CHAT_ID=your_admin_chat_id_here
API_BASE_URL=http://localhost:5000
```

### 3. Получение токена бота

1. Найдите @BotFather в Telegram
2. Отправьте `/newbot`
3. Следуйте инструкциям
4. Скопируйте полученный токен в `.env`

### 4. Запуск бота

```bash
# Основной бот
python bot.py

# Или альтернативный запуск
python run_bot.py
```

## Деплой на Render

1. Создайте аккаунт на Render.com
2. Подключите GitHub репозиторий
3. Создайте **Worker Service** (не Web Service!)
4. Настройте переменные окружения
5. Деплой произойдет автоматически

### Переменные окружения для Render

```
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_ADMIN_CHAT_ID=your_admin_chat_id
API_BASE_URL=https://your-main-app.onrender.com
```

## Локальная разработка

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск Flask приложения (опционально)
python app.py

# Запуск бота
python run_bot.py
```

## Структура проекта

```
ProThemesRUBot/
├── bot.py              # Основной файл бота
├── run_bot.py          # Альтернативный запуск
├── app.py              # Flask приложение (опционально)
├── requirements.txt    # Зависимости
├── templates.json      # Шаблоны сайтов
├── env.example         # Пример переменных окружения
├── Procfile           # Конфигурация для Render
├── render.yaml        # Конфигурация деплоя
├── runtime.txt        # Версия Python
└── README.md          # Документация
```

## Функции бота

### 📚 Шаблоны
- Просмотр готовых шаблонов
- Детальная информация о каждом шаблоне
- Цены и описание

### 🧱 UI Компоненты
- Блоки для разных ниш
- Готовые элементы интерфейса
- Категории компонентов

### 🎨 Стили
- Современные градиенты
- Анимации и эффекты
- Готовые стили кнопок

### 🛠️ Конструктор
- Инструкции по созданию сайтов
- Пошаговые руководства
- Интеграция с основной платформой

### 📦 Заказы
- Тарифы и цены
- Форма заказа
- Связь с поддержкой

## Поддержка

* Telegram: @ProThemesSupport
* Email: support@prothemes.ru
* Сайт: https://prothemes.ru

## Лицензия

MIT License 