import os
from dotenv import load_dotenv
load_dotenv()

# Get the value of the environment variable
TOKEN = os.getenv('TOKEN')
STYLES = [{"style": "Photo", "callback_data": "photo"},
        {"style": "Cartoon", "callback_data": "cartoon"},
                {"style": "3d", "callback_data": "3d"},
                # {"style": "Vector", "callback_data": "style_4"},
                {"style": "Cyberpunk", "callback_data": "cyberpunk"},
                {"style": "Studio Shot", "callback_data": "studio-shot"},
                {"style": "Painting", "callback_data": "painting"},
                # {"style": "Dark", "callback_data": "dark"},
                {"style": "Comic", "callback_data": "comic"},
                {"style": "Pixel Art", "callback_data": "pixel-art"},
                # {"style": "70s Vibe", "callback_data": "70s_vibe"},
                # {"style": "Fantasy", "callback_data": "fantasy"},
                # {"style": "Mockup", "callback_data": "mockup"},
                {"style": "Anime", "callback_data": "anime"},
                # {"style": "Watercolor", "callback_data": "watercolor"},
                {"style": "Sketch", "callback_data": "sketch"},
                {"style": "Digital Art", "callback_data": "digital-art"},
                {"style": "Origami", "callback_data": "origami"},
                # {"style": "Sureal", "callback_data": "sureal"},
                # {"style": "Art Noveau", "callback_data": "art-noveau"},
                # {"style": "2000s Phone", "callback_data": "2000s_phone"},
                # {"style": "All Styles", "callback_data": "all-styles"}
                ]

STYLES_REGEX = "^" + "|".join([style["callback_data"] for style in STYLES]) + "$"

FREEPIK_API_KEY = os.getenv('FREEPIK_API_KEY')
