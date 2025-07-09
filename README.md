# ProThemesRU Telegram Bot

🚀 Профессиональный Telegram бот для создания сайтов

## Возможности

- 📚 Библиотека готовых шаблонов
- 🧱 UI компоненты и блоки
- 🎨 Современные стили и эффекты
- 🛠️ Визуальный конструктор сайтов
- 📦 Заказ готовых сайтов

## Команды бота

- `/start` - Главное меню
- `/templates` - Просмотр шаблонов
- `/blocks` - UI компоненты
- `/styles` - Стили и эффекты
- `/constructor` - Конструктор сайтов
- `/order` - Заказать сайт
- `/pricing` - Цены и тарифы
- `/help` - Помощь

## Деплой на Render

1. Создайте аккаунт на [Render.com](https://render.com)
2. Подключите GitHub репозиторий
3. Создайте два сервиса:
   - **Web Service** (для Flask приложения)
   - **Worker Service** (для Telegram бота)

### Переменные окружения

```
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_ADMIN_CHAT_ID=your_admin_chat_id
```

## Локальная разработка

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск Flask приложения
python app.py

# Запуск бота
python run_bot.py
```

## Структура проекта

```
telegram_bot/
├── app.py              # Flask приложение
├── run_bot.py          # Telegram бот
├── requirements.txt    # Зависимости
├── Procfile           # Конфигурация для Render
├── render.yaml        # Конфигурация деплоя
├── runtime.txt        # Версия Python
└── templates/         # Шаблоны и ресурсы
```

## Поддержка

- Telegram: @ProThemesSupport
- Email: support@prothemes.ru
- Сайт: https://prothemes.ru 