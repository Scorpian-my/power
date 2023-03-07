
from os import system

from rubpy import Client, Methods, Message

app = Client(
    auth='dlpdkjbozjgvdsitygmwzxszyasmmvkj'

)

@app.handler
async def Downloader(bot: Methods, message: Message):
    if await message.of_group() and await message.is_text():
        text = await message.text()
        if text.startswith('/sms'):
            try:
                info = (await bot.getObjectByUsername(text.split()[1][1:])).get('user').get('user_guid')
                await bot.sendText(info, '📨 شما یک پیام ناشناس دارید:‌\n\n'+" ".join(text.split()[2:]))
                await message.reply('پیام شما با موفقیت ارسال شد...')
            except Exception as e:
                print(e)
    if await message.of_user() and await message.is_text():
        text = await message.text()
        if text.startswith("/join "):
            join = text.replace("/join ","")
            try:
                await message.reply("Loading..!")
                await app.joinGroup(join)
                await message.reply("Success")
            except:
              await message.reply("Error")