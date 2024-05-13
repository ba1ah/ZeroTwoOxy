from pyrogram import filters
from pyrogram import *
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import  BOT_USERNAME
from datetime import datetime
from ANNIEMUSIC import app as app
import requests


@app.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text =message.text.split(None, 1)[1]
    m =await message.reply_text( "𝐏ʟᴇᴀsᴇ 𝐖ᴀɪᴛ...❄️,\n\n𝐖ʀɪᴛɪɴɢ 𝐘ᴏᴜʀ 𝐓ᴇxᴛ...🌱")
    write = requests.get(f"https://apis.xditya.me/write?text={text}").url

    caption = f"""
𝐒ᴜᴄᴄᴇssғᴜʟʟʏ 𝐖ʀɪᴛᴛᴇɴ 𝐓ᴇxᴛ 💘
✨ 𝐖ʀɪᴛᴛᴇɴ 𝐁ʏ : [𝐙ᴇʀᴏ 𝐓ᴡᴏ](https://t.me/{BOT_USERNAME})
🥀 𝐑ᴇǫᴜᴇsᴛᴇᴅ 𝐁ʏ : {message.from_user.mention}
"""
    await m.delete()
    await message.reply_photo(photo=write,caption=caption)

mod_name = "WʀɪᴛᴇTᴏᴏʟ"

help = """

 ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡʜɪᴛᴇ ᴘᴀɢᴇ ᴡɪᴛʜ ᴀ ᴘᴇɴ 🖊

❍ /write <ᴛᴇxᴛ> *:* ᴡʀɪᴛᴇs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
 """

#----------

@app.on_message(filters.command("day"))
def date_to_day_command(client: Client, message: Message):
    try:
        # Extract the date from the command message......
        command_parts = message.text.split(" ", 1)
        if len(command_parts) == 2:
            input_date = command_parts[1].strip()
            date_object = datetime.strptime(input_date, "%Y-%m-%d")
            day_of_week = date_object.strftime("%A")

            # Reply with the day of the week
            message.reply_text(f"𝐓ʜᴇ 𝐃ᴀʏ 𝐎ғ 𝐓ʜᴇ 𝐖ᴇᴇᴋ 𝐅ᴏʀ {input_date} 𝐈s {day_of_week}.")

        else:
            message.reply_text("𝐏ʟᴇᴀsᴇ 𝐏ʀᴏᴠɪᴅᴇ 𝐀 𝐕ᴀʟɪᴅ 𝐃ᴀᴛᴇ 𝐈ɴ 𝐓ʜᴇ 𝐅ᴏʀᴍᴀᴛ `/Day 𝟷𝟿𝟺𝟽-𝟶𝟾-𝟷𝟻` ")

    except ValueError as e:
        message.reply_text(f"Error: {str(e)}")
