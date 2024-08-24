from telegram import Update
from telegram.ext import ContextTypes
import asyncio


from markups import reply_markups
from conversations import main_conv
from api import send

async def get_prompt_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.message.text:
        await query.edit_message_text("Please send me the prompt text", reply_markup=reply_markups.back_keyboard())
    else:
        await query.message.reply_text("Please send me the prompt text", reply_markup=reply_markups.back_keyboard())
    return main_conv.GET_PROMPT

async def get_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    prompt = update.message.text
    context.user_data["prompt"] = prompt
    await update.message.reply_text("Please select a style", reply_markup=reply_markups.ai_image_generator_styles())
    return main_conv.GET_STYLE

async def get_style(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    style = query.data
    context.user_data["style"] = style 
    await query.edit_message_text(f"Prompt: {context.user_data['prompt']}\nStyle: {style}", reply_markup=reply_markups.generate_keyboard())
    return main_conv.GENERATE

async def generate_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Generating image...")
    asyncio.create_task(send.send_image(update, context))

async def regenerate_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("Generating image...")
    asyncio.create_task(send.send_image(update, context))