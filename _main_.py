import logging
import os
import platform

from Config.config import Config

   
    
      # 1 BOT
from telethon.sync import TelegramClient

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN1

bot1 = TelegramClient('bot1', api_id, api_hash).start(bot_token=bot_token)

i = 1
while i<10:
    async def main1(): 
        message = Config.MESSAGE
        chat = Config.CHAT_ID
        chat = int(Config.CHAT_ID)
        spam_message = str(Config.MESSAGE)
    
        await bot1.send_message(chat, spam_message ,)
            
with bot1:
    bot1.loop.run_until_complete(main1())

