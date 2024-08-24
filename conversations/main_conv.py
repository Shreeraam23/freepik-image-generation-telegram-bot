from telegram import Update
from telegram.ext import ContextTypes
from markups import reply_markups

MAIN, MAIN_MENU, GET_PROMPT, GET_STYLE, GENERATE, WAITING = range(6)

async def main_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    user = update.effective_user
    await query.answer()
    await query.edit_message_text(f"""Hi Piumal! 👋

Welcome to the Main Menu! 🎉

Feel free to explore the options and let me know how I can assist you today. Let's get started!""", reply_markup=reply_markups.reply_markup_auth())
    return MAIN