import logging
import os
import platform

from Config.config import Config


from telethon.sync import TelegramClient

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN1

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

async def main():

        message = Config.MESSAGE
        chat = Config.CHAT_ID
        counter = int(Config.TIME)
        spam_message = str(Config.MESSAGE)
        for i in range(1, counter):
            await bot.send_message(chat, spam_message ,)


with bot:
    bot.loop.run_until_complete(main())
