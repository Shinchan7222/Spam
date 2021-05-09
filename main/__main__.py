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


api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN2

bot2 = TelegramClient('bot2', api_id, api_hash).start(bot_token=bot_token)




api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN3

bot3 = TelegramClient('bot3', api_id, api_hash).start(bot_token=bot_token)




api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN4

bot4 = TelegramClient('bot4', api_id, api_hash).start(bot_token=bot_token)




api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN5

bot5 = TelegramClient('bot5', api_id, api_hash).start(bot_token=bot_token)



api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN6

bot6 = TelegramClient('bot6', api_id, api_hash).start(bot_token=bot_token)




api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN7

bot7 = TelegramClient('bot7', api_id, api_hash).start(bot_token=bot_token)



api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN8

bot8 = TelegramClient('bot8', api_id, api_hash).start(bot_token=bot_token)

hunter = [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8]

async def main1(): 

   for op in Hunter:
           message = Config.MESSAGE
        chat = Config.CHAT_ID
        chat = int(Config.CHAT_ID)
        counter = int(Config.TIME)
        spam_message = str(Config.MESSAGE)
        for i in range(1, counter):
            await op.send_message(chat, spam_message ,)


with op[0]:

     Hunter[0].loop.run_until_complete(main1())

     


