#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = config("API_ID", "20247370", default=True, cast=int)
API_HASH = config("API_HASH", "813309fab8cd9fce260ce7269e543bdb", default=True)
BOT_TOKEN = config("BOT_TOKEN", "6305234380:AAHPc-GGWKGc2b7Fs5_TDzh1xCVGTNUz5wA", default=True)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 