import json
import requests
import logging
from pprint import pprint
from logging import Logger
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes, Updater)

BOT_TOKEN = '7977384112:AAHuuTeQe2S8yz3IbPq7Mt6BVpc8LB5w27w'
MAGICMIRROR_URL = 'http://localhost:8080/custom-message'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def recado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        message = {"messageHeader": "alguem te deixou um recado: ", "message": ' '.join(context.args)}

        try:
            requests.post(MAGICMIRROR_URL, json=message)
            await update.message.reply_text('Sua mensagem foi entrege ao MagicMirror!')
        except requests.RequestException as e:
            await update.message.reply_text(f'Não foi possivel enviar seu recado!: {e}')

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    handlers = {
        'recado': CommandHandler('recado', recado)
    }

    for (k, v) in handlers.items():
        logging.info(f'Adding {k} handler...')
        app.add_handler(v)

    app.run_polling()

if __name__ == '__main__':
    main() 