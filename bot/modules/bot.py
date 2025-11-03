import logging

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    Updater,
)

BOT_TOKEN = "7977384112:AAHuuTeQe2S8yz3IbPq7Mt6BVpc8LB5w27w"
REMOTE_CONTROL_API_KEY = "aa13c710bab642ca843ef59595d6341b"
CUSTOM_TEXT_URL = "http://localhost:8080/api/notification/CUSTOMTEXT_UPDATE"
APP = ApplicationBuilder().token(BOT_TOKEN).build()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Olá, digite /menu para ter acesso as opções do painel!"
    )


def run_bot():
    APP.add_handler(CommandHandler("start", start))
    APP.run_polling()
