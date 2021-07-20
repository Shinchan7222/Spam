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
     TIME = os.environ.get("TIME", None)
     CHAT_ID = os.environ.get("CHAT_ID", None)
     MESSAGE = os.environ.get("MESSAGE", None)
