from modules.commands import send_message
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, ContextTypes
from pprint import pprint
from modules.bot import APP, MIRROR_URL
from modules import commands
import requests

user_state = {}

async def show_menu(update, context, text, keyboard):
    reply_markup = InlineKeyboardMarkup(keyboard)
        
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(text, reply_markup=reply_markup)

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💬 Recados", callback_data="menu_messages")],
        [InlineKeyboardButton("🪞 Display", callback_data="menu_display")],
        [InlineKeyboardButton("⚙️ Sistema", callback_data="menu_system")],
    ]

    await show_menu(update, context, 'Escolha uma categoria: ', keyboard)

# --- MESSAGES MENU ---
async def messages_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📝 Enviar recado", callback_data="send_message")],
        [InlineKeyboardButton("🧹 Apagar recado", callback_data="clear_message")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="back_main")],
    ]
    await show_menu(update, context, "💬 *Menu de recados*", keyboard)

# --- DISPLAY MENU ---
async def display_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🟢 ON", callback_data="screen_on"),
         InlineKeyboardButton("🔴 OFF", callback_data="screen_off")],
        [InlineKeyboardButton("💡 Brilho", callback_data="menu_brightness")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back_main")],
    ]
    await show_menu(update, context, "🪞 *Controles do display*", keyboard)

# --- BRIGHTNESS MENU ---
async def brightness_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("25%", callback_data="brightness_25"),
         InlineKeyboardButton("50%", callback_data="brightness_50")],
        [InlineKeyboardButton("75%", callback_data="brightness_75"),
         InlineKeyboardButton("100%", callback_data="brightness_100")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="menu_display")],
    ]
    await show_menu(update, context, "💡 *Controle de brilho*", keyboard)

# --- SYSTEM MENU ---
async def system_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔁 Reiniciar painel", callback_data="restart_mirror")],
        [InlineKeyboardButton("💡 Status", callback_data="status")],
        [InlineKeyboardButton("⬅️ Voltar", callback_data="back_main")],
    ]
    await show_menu(update, context, "⚙️ *Menu do sistema*", keyboard)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    user_id = query.from_user.id

    # Menus
    if data == "menu_messages":
        await messages_menu(update, context)
    elif data == "menu_display":
        await display_menu(update, context)
    elif data == "menu_system":
        await system_menu(update, context)
    elif data == "menu_brightness":
        await brightness_menu(update, context)
    elif data == "back_main":
            await main_menu(update, context)

    # Message Actions
    elif data == "send_message":
        user_state[user_id] = "awaiting_message"
        await query.edit_message_text("Send me the message to display 🪞")
    elif data == "clear_message":
        await commands.send_message('') # clearing custom-text widget
        await query.edit_message_text("Mensagem apagada 🧹")

    # Display Controls
    elif data == "screen_on":
        await commands.set_monitor_power(True)
        await query.edit_message_text("Screen turned ON 🟢")
    elif data == "screen_off":
        await commands.set_monitor_power(False)
        await query.edit_message_text("Screen turned OFF 🔴")

    # Brightness levels (replace with your actual API or command)
    elif data.startswith("brightness_"):
        level = int(data.split("_")[1])
        await commands.set_brightness(level)
        await query.edit_message_text(f"Selecione o nivel de brilho: {level}% 💡")

    # System
    elif data == "restart_mirror":
        await commands.refresh_monitor() 
        await query.edit_message_text("Painel reiniciado 🔁")
    elif data == "status":
        await query.edit_message_text("Painel esta rodando perfeitamente ✅")

# --- HANDLE TEXT INPUTS ---
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    text = update.message.text

    if user_state.get(user_id) == "awaiting_message":
        # requests.post(f"{MIRROR_URL}/custom-message", json={"message": text})
        await commands.send_message(text)
        await update.message.reply_text(f"🪞 Recado enviado: “{text}”")
        user_state[user_id] = None
    else:
        await update.message.reply_text("Use /menu para ter acesso as opcoes.")
