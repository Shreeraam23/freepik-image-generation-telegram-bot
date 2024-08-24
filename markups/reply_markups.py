from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import config

back = [InlineKeyboardButton("Back", callback_data="back")]
def reply_markup_main():
    keyboard = [[InlineKeyboardButton("Main Menu", callback_data="main")]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    return reply_markup

def reply_markup_auth():

    keyboard = [[InlineKeyboardButton("Ai image generator", callback_data="generate_start")], 
                # [InlineKeyboardButton("Admin panel", callback_data="admin")],
                # back
                ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    return reply_markup

def back_keyboard():
    keyboard = [back]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def ai_image_generator_styles():
    styles = config.STYLES    
    keyboard = [[InlineKeyboardButton(style["style"], callback_data=style["callback_data"]) for style in styles[i:i+2]] for i in range(0, len(styles), 2)]
    keyboard.append(back)
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def generate_keyboard():
    keyboard = [[InlineKeyboardButton("Generate", callback_data="generate")], back]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

def regenerate_keyboard():
    keyboard = [[InlineKeyboardButton("Regenerate", callback_data="regenerate")], back]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup