from modules.commands import send_message
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, ContextTypes
from pprint import pprint
from modules.bot import APP


async def show_menu(update, context, text, keyboard):
    reply_markup = InlineKeyboardMarkup(keyboard)
        
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text, reply_markup=reply_markup)
    else:
        await query.edit_message_text(text, reply_markup=reply_markup)

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💬 Messages", callback_data="menu_messages")],
        [InlineKeyboardButton("🪞 Display", callback_data="menu_display")],
        [InlineKeyboardButton("⚙️ System", callback_data="menu_system")],
    ]

    await show_menu(update, context, 'Escolha uma categoria: ', keyboard)

# --- MESSAGES MENU ---
async def messages_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📝 Send message", callback_data="send_message")],
        [InlineKeyboardButton("🧹 Clear message", callback_data="clear_message")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back_main")],
    ]
    await show_menu(update, context, "💬 *Messages Menu*", keyboard)

# --- DISPLAY MENU ---
async def display_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🟢 Turn ON", callback_data="screen_on"),
         InlineKeyboardButton("🔴 Turn OFF", callback_data="screen_off")],
        [InlineKeyboardButton("💡 Brightness", callback_data="menu_brightness")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back_main")],
    ]
    await show_menu(update, context, "🪞 *Display Controls*", keyboard)

# --- BRIGHTNESS MENU ---
async def brightness_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("25%", callback_data="brightness_25"),
         InlineKeyboardButton("50%", callback_data="brightness_50")],
        [InlineKeyboardButton("75%", callback_data="brightness_75"),
         InlineKeyboardButton("100%", callback_data="brightness_100")],
        [InlineKeyboardButton("⬅️ Back", callback_data="menu_display")],
    ]
    await show_menu(update, context, "💡 *Brightness Control*", keyboard)

# --- SYSTEM MENU ---
async def system_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔁 Restart Mirror", callback_data="restart_mirror")],
        [InlineKeyboardButton("💡 Status", callback_data="status")],
        [InlineKeyboardButton("⬅️ Back", callback_data="back_main")],
    ]
    await show_menu(update, context, "⚙️ *System Menu*", keyboard)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

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

    
