from logging import Logger
from pprint import pprint

from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, filters
from modules.bot import run_bot, APP
from modules.menus import button_callback, main_menu, handle_message


def main():

    # endereça as funções responsáveis pela funcionalidade dos commandos
    APP.add_handler(CommandHandler('menu', main_menu))
    APP.add_handler(CallbackQueryHandler(button_callback))
    APP.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # inicia o bot
    run_bot()
    
if __name__ == '__main__':
    main() 
