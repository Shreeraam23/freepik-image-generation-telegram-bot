import aiohttp
from telegram import Update
from telegram.ext import ContextTypes


import base64
from io import BytesIO

import config
from markups import reply_markups

async def call_api(prompt: str, style: str) -> str:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post("https://api.freepik.com/v1/ai/text-to-image", json={"prompt": prompt,"styling": {'style': style}}, headers={"Accept": "application/json","x-freepik-api-key": config.FREEPIK_API_KEY}) as response:
                response.raise_for_status()
                return await response.json()
        except Exception as e:
            print(e)
            raise Exception(e)

async def send_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    prompt = context.user_data["prompt"]
    style = context.user_data["style"]
    try:
        response = await call_api(prompt, style)
        image_data = response['data'][0]['base64']
        image_bytes = base64.b64decode(image_data)
        image_io = BytesIO(image_bytes)
        image_io.name = 'image.jpeg'

        if update.callback_query:
            await update.callback_query.message.reply_photo(image_io, caption = f"Prompt: {prompt}\n\nStyle: {style}", reply_markup=reply_markups.regenerate_keyboard())
        else:
            await update.message.reply_photo(image_io, caption = f"Prompt: {prompt}\n\nStyle: {style}", reply_markup=reply_markups.regenerate_keyboard())
    except Exception as e:
        if update.callback_query:
            await update.callback_query.message.reply_text("Internal Server Error", reply_markup=reply_markups.back_keyboard())
        else:
            await update.message.reply_text("Internal Server Error", reply_markup=reply_markups.back_keyboard())
        raise Exception(e)
