import os
import aiohttp
import aiofiles
from aiohttp import ContentTypeError
from ANNIEMUSIC import app as app
from pyrogram import filters

API_KEY = "23nfCEipDijgVv6SH14oktJe"

def check_filename(filroid):
    if os.path.exists(filroid):
        no = 1
        while True:
            ult = "{0}_{2}{1}".format(*os.path.splitext(filroid) + (no,))
            if os.path.exists(ult):
                no += 1
            else:
                return ult
    return filroid

async def RemoveBG(input_file_name):
    headers = {"X-API-Key": API_KEY}
    files = {"image_file": open(input_file_name, "rb").read()}
    async with aiohttp.ClientSession() as ses:
        async with ses.post(
            "https://api.remove.bg/v1.0/removebg", headers=headers, data=files
        ) as y:
            contentType = y.headers.get("content-type")
            if "image" not in contentType:
                return False, (await y.json())

            name = check_filename("alpha.png")
            file = await aiofiles.open(name, "wb")
            await file.write(await y.read())
            await file.close()
            return True, name


@app.on_message(filters.command("rmbg"))
async def rmbg(bot, message):
    rmbg = await message.reply("𝐏ʀᴏᴄᴇssɪɴɢ.... 🌚") 
    replied = message.reply_to_message
    if not replied:
        return await rmbg.edit("𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐏ʜᴏᴛᴏ 𝐑ᴇᴍᴏᴠᴇ 𝐈ᴛs 𝐁ᴀᴄᴋɢʀᴏᴜɴᴅ ✨👩🏻‍💻")

    if replied.photo:
        photo = await bot.download_media(replied)
        x, y = await RemoveBG(photo)
        os.remove(photo)
        if not x:
            bruh = y["errors"][0]
            details = bruh.get("detail", "")
            return await rmbg.edit(f"ERROR ~ {bruh['title']},\n{details}")
        await message.reply_photo(photo=y, caption="𝐇ᴇʀᴇ 𝐈s 𝐘ᴏᴜʀ 𝐈ᴍᴀɢᴇ 🏞 𝐖ɪᴛʜᴏᴜᴛ 𝐁ᴀᴄᴋɢʀᴏᴜɴᴅs ❤️‍🔥")
        await message.reply_document(document=y)
        await rmbg.delete()
        os.remove(y)
    else:
        await rmbg.edit("𝐏ʟᴇᴀsᴇ 𝐑ᴇᴘʟʏ 𝐎ɴʟʏ 𝐓ᴏ ᴀ 𝐏ʜᴏᴛᴏ 𝐓ᴏ 𝐑ᴇᴍᴏᴠᴇ 𝐁ᴀᴄᴋɢʀᴏᴜɴᴅ 👀")
