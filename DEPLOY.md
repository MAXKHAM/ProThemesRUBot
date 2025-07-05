# 🚀 Деплой Telegram Bot на GitHub

> **ВНИМАНИЕ! Никогда не публикуйте токен бота публично. Если вы случайно его раскрыли — немедленно замените через @BotFather.**
> 
> **Файл .env должен быть в кодировке UTF-8 без BOM!**

Инструкция по развертыванию телеграм бота ProThemesRU на различных платформах через GitHub Actions.

## 📋 Подготовка

### 1. Создание Telegram Bot

1. Найдите @BotFather в Telegram
2. Отправьте команду `/newbot`
3. Следуйте инструкциям для создания бота
4. Сохраните токен бота

### 2. Получение Admin Chat ID

1. Напишите боту @userinfobot в Telegram
2. Отправьте любое сообщение
3. Бот вернет ваш Chat ID
4. Сохраните этот ID

## 🔧 Настройка GitHub Secrets

Перейдите в настройки вашего GitHub репозитория:
`Settings` → `Secrets and variables` → `Actions`

Добавьте следующие секреты:

### Обязательные:
- `TELEGRAM_BOT_TOKEN` - токен вашего бота
- `TELEGRAM_ADMIN_CHAT_ID` - ID чата администратора

### Опциональные (для деплоя):
- `API_BASE_URL` - URL вашего API сервера
- `RAILWAY_TOKEN` - токен Railway (для деплоя на Railway)
- `RENDER_TOKEN` - токен Render (для деплоя на Render)
- `RENDER_SERVICE_ID` - ID сервиса Render
- `HEROKU_API_KEY` - API ключ Heroku
- `HEROKU_APP_NAME` - имя приложения Heroku
- `HEROKU_EMAIL` - email для Heroku

## 🌐 Деплой на различные платформы

### Railway

1. Зарегистрируйтесь на [Railway](https://railway.app)
2. Создайте новый проект
3. Подключите GitHub репозиторий
4. Добавьте переменные окружения:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_ADMIN_CHAT_ID`
   - `API_BASE_URL`
5. Получите токен Railway и добавьте в GitHub Secrets
6. При пуше в main ветку бот автоматически деплоится

### Render

1. Зарегистрируйтесь на [Render](https://render.com)
2. Создайте новый Web Service
3. Подключите GitHub репозиторий
4. Настройте:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python webhook_bot.py`
   - **Environment**: Python 3
   - **Procfile**: (опционально) `web: python webhook_bot.py`
5. Добавьте переменные окружения
6. Получите токен и Service ID, добавьте в GitHub Secrets

### Heroku

1. Зарегистрируйтесь на [Heroku](https://heroku.com)
2. Создайте новое приложение
3. Установите Heroku CLI
4. Добавьте переменные окружения:
   ```bash
   heroku config:set TELEGRAM_BOT_TOKEN=your_token
   heroku config:set TELEGRAM_ADMIN_CHAT_ID=your_chat_id
   heroku config:set API_BASE_URL=your_api_url
   ```
5. Добавьте Procfile с содержимым:
   ```
   web: python webhook_bot.py
   ```
6. Получите API ключ и добавьте в GitHub Secrets

## 🔄 Автоматический деплой

После настройки GitHub Actions:

1. При каждом пуше в `main` ветку автоматически:
   - Запускаются тесты
   - Деплоится на выбранные платформы
   - Отправляются уведомления

2. Проверьте статус деплоя:
   - GitHub Actions → Workflows
   - Логи деплоя в реальном времени

## 📊 Мониторинг

### Логи
- GitHub Actions: вкладка Actions
- Railway: вкладка Deployments
- Render: вкладка Logs
- Heroku: `heroku logs --tail`

### Статус бота
- Проверьте `/health` эндпоинт
- Отправьте `/start` боту
- Проверьте уведомления администратора

## 🛠️ Локальная разработка

```bash
# Клонирование
git clone <your-repo>
cd telegram_bot

# Установка зависимостей
pip install -r requirements.txt

# Создание .env
cp .env.example .env        # Linux/Mac
copy .env.example .env      # Windows
# Отредактируйте .env

# Запуск
python bot.py  # для локальной разработки
python webhook_bot.py  # для тестирования веб-хуков
```

## 🔧 Конфигурация

### Переменные окружения

```env
# Обязательные
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_ADMIN_CHAT_ID=your_chat_id

# Опциональные
API_BASE_URL=https://your-api.com
WEBHOOK_URL=https://your-domain.com
LOG_LEVEL=INFO
PORT=8080
```

### Настройка веб-хуков

Для продакшена рекомендуется использовать веб-хуки:

```python
# Установка веб-хука
bot.set_webhook(url='https://your-domain.com/webhook')

# Удаление веб-хука
bot.delete_webhook()
```

## 🐛 Устранение неполадок

### Бот не отвечает
1. Проверьте токен в переменных окружения
2. Убедитесь, что бот не заблокирован
3. Проверьте логи деплоя
4. Проверьте, что файл .env в кодировке UTF-8 без BOM

### Ошибки деплоя
1. Проверьте GitHub Secrets
2. Убедитесь, что все зависимости установлены
3. Проверьте права доступа к платформам

### Проблемы с веб-хуками
1. Проверьте SSL сертификат
2. Убедитесь, что домен доступен
3. Проверьте настройки файрвола

## 📞 Поддержка

При возникновении проблем:
1. Проверьте логи в GitHub Actions
2. Создайте issue в репозитории
3. Обратитесь в поддержку платформы

## 🔄 Обновления

Для обновления бота:
1. Внесите изменения в код
2. Запушьте в main ветку
3. GitHub Actions автоматически деплоит обновления

## 📈 Масштабирование

Для увеличения производительности:
1. Добавьте Redis для кэширования
2. Используйте базу данных PostgreSQL
3. Настройте мониторинг и алерты
4. Добавьте CDN для статических файлов 