from rubpy import Client

from youtubesearchpython import VideosSearch

from pytube import YouTube

from os import system, remove


app = Client("ohcvqqwwxhhbmjvxmdpvummprnnqyrgg")


@app.handler
async def main(app, message):

    if await message.of_user() and await message.is_text():

        text = await message.text()

        if text in ('شروع'):

            info = await app.getUserInfo(await message.chat_id())

            name = info.get('user').get('first_name')

            id = info.get('user').get('username')

            await message.reply(f"**Hello Mr/Miss** {name}\n**Welcome To Tools Bot**\n Your Time Login: \n**Your ID:** @{id}")

        elif text.startswith("@vid "):

            tube = text.replace("@vid ", "")

            try:

                search = VideosSearch(tube, limit=5)

                result = ''

                for i, v in enumerate(search.result()['result']):

                    name = v['accessibility']['title'].split('by')[0]

                    id = v['id']

                    result += f"\n<b>{i+1} - {name} :\n📥 download :\n/dl_{id}\n\n----------------------\n\n"

                await message.reply(result)

            except:

                await message.reply("**Error**")

        elif text.startswith("/dl_"):

            link = text.replace("/dl_", "")

            try:

                await message.reply("**دانلود شروع شد. لطفا تا انتهای دانلود دستوری وارد نکنید**")

                Youtube = YouTube(f"https://www.youtube.com/watch?v={link}")

                stream = Youtube.streams.filter(
                    file_extension='mp4').get_by_itag(22)

                stream.download(filename='FreeTube.mp4', output_path='./')

                await app.sendVideo(await message.chat_id(), "FreeTube.mp4", "**Download Success**")

                remove("FreeTube.mp4")

            except:

                message.reply("**Error**")
