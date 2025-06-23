import os
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv('TELEGRAM_TOKEN')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')
if not TOKEN:
    logger.error("TELEGRAM_TOKEN не установлен!")
    raise ValueError("TELEGRAM_TOKEN не установлен!")
if not ADMIN_CHAT_ID:
    logger.error("ADMIN_CHAT_ID не установлен!")
    raise ValueError("ADMIN_CHAT_ID не установлен!")

keyboard = ReplyKeyboardMarkup([['Заказ', 'Цены']], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f'Привет, {user.first_name}! Я бот ProThemesRU. Выберите действие:',
        reply_markup=keyboard
    )

async def prices(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Наши цены:\n\n"
        "- Простая тема: 500 руб.\n"
        "- Тема средней сложности: 1000 руб.\n"
        "- Сложная тема: 1500 руб.",
        reply_markup=keyboard
    )

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 Опишите ваш заказ (тему, требования, сроки):",
        reply_markup=keyboard
    )

async def forward_to_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    username = f"@{user.username}" if user.username else user.first_name
    await context.bot.send_message(
        chat_id=ADMIN_CHAT_ID,
        text=f"📨 Новый заказ от {username}:\n\n{update.message.text}"
    )
    await update.message.reply_text("✅ Ваш заказ принят!", reply_markup=keyboard)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Ошибка: {context.error}")
    if update and update.message:
        await update.message.reply_text("Произошла ошибка, попробуйте позже.")

def main():
    try:
        application = Application.builder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.Regex('^Цены$'), prices))
        application.add_handler(MessageHandler(filters.Regex('^Заказ$'), order))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & ~filters.Regex('^(Цены|Заказ)$'), forward_to_admin))
        application.add_error_handler(error_handler)

        if os.getenv('RENDER'):
            logger.info("Запуск в режиме webhook на Render")
            hostname = os.getenv('RENDER_EXTERNAL_HOSTNAME')
            if not hostname:
                logger.error("RENDER_EXTERNAL_HOSTNAME не установлен!")
                raise ValueError("RENDER_EXTERNAL_HOSTNAME не установлен!")
            application.run_webhook(
                listen="0.0.0.0",
                port=int(os.getenv('PORT', 8443)),
                url_path=TOKEN,
                webhook_url=f"https://{hostname}/{TOKEN}",
                secret_token=os.getenv('WEBHOOK_SECRET', TOKEN)
            )
        else:
            logger.info("Запуск в режиме polling")
            application.run_polling(allowed_updates=["message"])

    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
        raise

if __name__ == '__main__':
    main()