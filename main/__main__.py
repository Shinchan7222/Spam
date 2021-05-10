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


import asyncio 
async def main1(): 
        message = Config.MESSAGE
        chat = Config.CHAT_ID
        chat = int(Config.CHAT_ID)
        counter = int(Config.TIME)
        spam_message = str(Config.MESSAGE)
        for i in range(1, counter):
            await bot1.send_message(chat, spam_message ,)
            await bot2.send_message(chat, spam_message ,)
            await bot3.send_message(chat, spam_message ,)
            await bot4.send_message(chat, spam_message ,)
            await bot5.send_message(chat, spam_message ,)
            await bot6.send_message(chat, spam_message ,)
            await bot7.send_message(chat, spam_message ,)
            await bot8.send_message(chat, spam_message ,)
            

asyncio.run(main1)



     


