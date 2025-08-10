from telegram import Update
from telegram.ext import Updater, ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = '7977384112:AAHuuTeQe2S8yz3IbPq7Mt6BVpc8LB5w27w'
MESSAGE_FILE = 'message.txt'

import logging
from logging import Logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = 'Você sabia que o Lucas ama a Mari? Pois é menina...'
    )

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        with open(MESSAGE_FILE, 'a') as file:
            text = ' '.join(context.args)
            await update.message.reply_text(f'Sua mensagem: {text}')
            file.write(text + '\n')

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    handlers = {
        'start': CommandHandler('start', start),
        'add': CommandHandler('add', add)
    }

    for (k, v) in handlers.items():
        logging.info(f'Adding {k} handler...')
        app.add_handler(v)

    app.run_polling()

if __name__ == '__main__':
    main()