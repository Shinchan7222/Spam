import os

import heroku3
from dotenv import load_dotenv
from distutils.util import strtobool

if os.path.exists("local.env"):
    load_dotenv("local.env")
    
class Config(object):
     API_ID = int(os.environ.get("API_ID", 1))
     API_HASH = os.environ.get("API_HASH", None)
     BOT_TOKEN1 = os.environ.get("BOT_TOKEN1", None)
     BOT_TOKEN2 = os.environ.get("BOT_TOKEN2", None)
     BOT_TOKEN3 = os.environ.get("BOT_TOKEN3", None)
     BOT_TOKEN4 = os.environ.get("BOT_TOKEN4", None)
     BOT_TOKEN5 = os.environ.get("BOT_TOKEN5", None)
     BOT_TOKEN6 = os.environ.get("BOT_TOKEN6", None)
     BOT_TOKEN7 = os.environ.get("BOT_TOKEN7", None)
     BOT_TOKEN8 = os.environ.get("BOT_TOKEN8", None)
     TIME = os.environ.get("TIME", None)
     CHAT_ID = os.environ.get("CHAT_ID", None)
     MESSAGE = os.environ.get("MESSAGE", None)