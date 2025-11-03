from pprint import pprint

from telegram import Update
from telegram.ext import ContextTypes

from modules.bot import CUSTOM_TEXT_URL, REMOTE_CONTROL_API_KEY


# função de recado
async def send_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE, text: str
):
    header = {
        "Authorization": f"Bearer {REMOTE_CONTROL_API_KEY}",
        "Content-type": "application/json",
    }

    json = {"message": text}

    try:
        x = requests.post(CUSTOM_TEXT_URL, json=json, headers=header)
        pprint(f"RECADO POST REQUEST RESPONSE: {x.__dict__}")
        await update.message.reply_text(
            "Seu recado foi enviado ao MagicMirror!"
        )
    except requests.RequestException as e:
        pprint(f"failed to send message: {e}")
        await update.message.reply_text(f"Falha ao enviar seu recado: {e}")
