#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = config("20247370", default=True, cast=int)
API_HASH = config("813309fab8cd9fce260ce7269e543bdb", default=True)
BOT_TOKEN = config("6756415088:AAFd88wWnxGw2y73DXlcMXchCtkISLWE92A", default=True)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
