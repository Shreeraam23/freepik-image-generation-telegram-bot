#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.


import logging
from logging import config

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, ConversationHandler, CallbackQueryHandler

import config
import database.db_init
from markups import reply_markups
from conversations import main_conv
from conversations import generator

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"""Hi {user.first_name}! 👋

Welcome to the Image Generation Bot! 🎨✨

We're excited to have you on board. Get ready to create stunning images with just a few taps. I'll guide you through everything. Let's get started on your next masterpiece! 🖌️""", reply_markup=reply_markups.reply_markup_auth()
    )
    return main_conv.MAIN

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(config.TOKEN).build()

    # on different commands - answer in Telegram
     # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            # main_conv.MAIN: [
            #     CallbackQueryHandler(main_conv.main_callback, pattern="^" + "main" + "$"),
            # ],
            main_conv.MAIN: [
                CallbackQueryHandler(generator.get_prompt_callback, pattern="^" + "generate_start" + "$"),
                # CallbackQueryHandler(main_conv.main_callback, pattern="^" + "back" + "$"),
            ],
            main_conv.GET_PROMPT: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, generator.get_prompt),
                CallbackQueryHandler(main_conv.main_callback, pattern="^" + "back" + "$"),
            ],
            main_conv.GET_STYLE: [
                CallbackQueryHandler(generator.get_style, pattern=config.STYLES_REGEX),
                CallbackQueryHandler(generator.get_prompt_callback, pattern="^" + "back" + "$"),
            ],
            main_conv.GENERATE: [
                CallbackQueryHandler(generator.generate_callback, pattern="^" + "generate" + "$"),
                CallbackQueryHandler(generator.regenerate_callback, pattern="^" + "regenerate" + "$"),
                CallbackQueryHandler(generator.get_prompt_callback, pattern="^" + "back" + "$"),
            ],

            
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()