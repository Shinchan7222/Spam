import logging
import os
import platform

import pyrogram
from config import Config

from pyrogram import Client



#1 bot
app1 = Client(
    "my_bot1",
    bot_token=Config.BOT_TOKEN1
)

app1.run()



async def spam(client, message):

    if not count:
        await app1.send_message("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return 
   count = Config.TIME
   count = int(count)
    x = 0
    for x in range(count):
        await client.copy_message(
            from_chat_id=Config.CHAT_ID,
            chat_id=Config.CHAT_ID,
            message_id=Config.MESSAGE,
        )
        x += 1


#2 bot
app2 = Client(
    "my_bot2",
    bot_token=Config.BOT_TOKEN2
)

app2.run()



async def spam(client, message):

    if not count:
        await app2.send_message("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return 
   count = Config.TIME
   count = int(count)
    x = 0
    for x in range(count):
        await client.copy_message(
            from_chat_id=Config.CHAT_ID,
            chat_id=Config.CHAT_ID,
            message_id=Config.MESSAGE,
        )
        x += 1


#3 
app3 = Client(
    "my_bot3",
    bot_token=Config.BOT_TOKEN3
)

app3.run()



async def spam(client, message):

    if not count:
        await app3.send_message("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return 
   count = Config.TIME
   count = int(count)
    x = 0
    for x in range(count):
        await client.copy_message(
            from_chat_id=Config.CHAT_ID,
            chat_id=Config.CHAT_ID,
            message_id=Config.MESSAGE,
        )
        x += 1



#4
app4 = Client(
    "my_bot4",
    bot_token=Config.BOT_TOKEN4
)

app4.run()




async def spam(client, message):

    if not count:
        await app4.send_message("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return 
   count = Config.TIME
   count = int(count)
    x = 0
    for x in range(count):
        await client.copy_message(
            from_chat_id=Config.CHAT_ID,
            chat_id=Config.CHAT_ID,
            message_id=Config.MESSAGE,
        )
        x += 1
#5
app5 = Client(
    "my_bot5",
    bot_token=Config.BOT_TOKEN5
)

app5.run()



async def spam(client, message):

    if not count:
        await app5.send_message("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return 
   count = Config.TIME
   count = int(count)
    x = 0
    for x in range(count):
        await client.copy_message(
            from_chat_id=Config.CHAT_ID,
            chat_id=Config.CHAT_ID,
            message_id=Config.MESSAGE,
        )
        x += 1


#6
app6 = Client(
    "my_bot6",
    bot_token=Config.BOT_TOKEN6
)

app6.run()



async def spam(client, message):

    if not count:
        await app6.send_message("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return 
   count = Config.TIME
   count = int(count)
    x = 0
    for x in range(count):
        await client.copy_message(
            from_chat_id=Config.CHAT_ID,
            chat_id=Config.CHAT_ID,
            message_id=Config.MESSAGE,
        )
        x += 1

#7
app7 = Client(
    "my_bot7",
    bot_token=Config.BOT_TOKEN7
)

app7.run()



async def spam(client, message):

    if not count:
        await app7.send_message("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return 
   count = Config.TIME
   count = int(count)
    x = 0
    for x in range(count):
        await client.copy_message(
            from_chat_id=Config.CHAT_ID,
            chat_id=Config.CHAT_ID,
            message_id=Config.MESSAGE,
        )
        x += 1

#8

app8 = Client(
    "my_bot8",
    bot_token=Config.BOT_TOKEN8
)

app8.run()



async def spam(client, message):

    if not count:
        await app8.send_message("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return 
   count = Config.TIME
   count = int(count)
    x = 0
    for x in range(count):
        await client.copy_message(
            from_chat_id=Config.CHAT_ID,
            chat_id=Config.CHAT_ID,
            message_id=Config.MESSAGE,
        )
        x += 1



if __name__ == "__main__":
    Friday.loop.run_until_complete(run_bot())
