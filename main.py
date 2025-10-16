import json
from pprint import pprint

from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          Updater)

TOKEN = '7977384112:AAHuuTeQe2S8yz3IbPq7Mt6BVpc8LB5w27w'
MESSAGE_FILE = '/tmp/test.txt'
REMOTE_FILE = '/tmp/remotefile.json'

import logging
from logging import Logger

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def recado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        with open(MESSAGE_FILE, 'w') as file:
            print("INFO: clearing message file.")

        with open(MESSAGE_FILE, 'a') as file:
            text = ' '.join(context.args)
            await update.message.reply_text(f'Sua mensagem: {text}')
            file.write(text + '\n')
         
        # with open(REMOTE_FILE, 'w') as remotefile:
        #     text = ' '.join(context.args)
        #     await update.message.reply_text(f'Sua mensagem: {text}')
        #     x = {'anytime' : text}
        #     remotefile.write(json.dumps(x))


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    handlers = {
        'recado': CommandHandler('recado', recado)
    }

    for (k, v) in handlers.items():
        logging.info(f'Adding {k} handler...')
        app.add_handler(v)

    app.run_polling()

if __name__ == '__main__':
    main() 