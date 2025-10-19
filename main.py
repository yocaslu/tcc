import json
import logging
from logging import Logger
from pprint import pprint

import requests
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          Updater)

from server import REMOTE_CONTROL_API_KEY

BOT_TOKEN = '7977384112:AAHuuTeQe2S8yz3IbPq7Mt6BVpc8LB5w27w'
CUSTOM_MESSAGE_URL = 'http://localhost:8080/custom-message'
REMOTE_CONTROL_API_KEY = 'aa13c710bab642ca843ef59595d6341b'
CUSTOM_TEXT_URL = 'http://localhost:8080/api/notification/CUSTOMTEXT_UPDATE'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def recado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        header = {'Authorization': f"Bearer {REMOTE_CONTROL_API_KEY}", 'Content-type': 'application/json'}
        json = {"message": " ".join(context.args)}

        try:
            x = requests.post(CUSTOM_TEXT_URL, json=json, headers=header)
            pprint(f'POST REQUEST RESPONSE: {x.__dict__}')
            await update.message.reply_text('Seu recado foi enviado ao MagicMirror!')
        except requests.RequestException as e:
            await update.message.reply_text(f'Falha ao enviar seu recado: {e}')

           
#           USING CUSTOM-MESSAGE
# async def recado(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if context.args:
#         message = {
#             "messageHeader" : "Novo recado: ",
#             "message" : ' '.join(context.args)
#         }

#         try:
#             requests.post(MAGICMIRROR_URL, json=message)
#             await update.message.reply_text('Seu recado foi entrege ao MagicMirror!')
#         except requests.RequestException as e:
#             await update.message.reply_text(f'Não foi possivel enviar seu recado!: {e}')

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