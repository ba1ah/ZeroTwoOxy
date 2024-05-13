from pyrogram import filters
import asyncio
import pyfiglet 
from random import choice
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram.handlers import MessageHandler
from ANNIEMUSIC import app
def figle(text):
    x = pyfiglet.FigletFont.getFonts()
    font = choice(x)
    figled = str(pyfiglet.figlet_format(text,font=font))
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="𝐂ʜᴀɴɢᴇ 🐾", callback_data="figlet"),InlineKeyboardButton(text="𝐂ʟᴏsᴇ 👋", callback_data="close_reply")]])
    return figled, keyboard

@app.on_message(filters.command("figlet"))
async def echo(bot, message):
    global text
    try:
        text = message.text.split(' ',1)[1]
    except IndexError:
        return await message.reply_text("𝘌𝘹𝘢𝘮𝘱𝘭𝘦:\n\n`/figlet HELLO`")
    kul_text, keyboard = figle(text)
    await message.reply_text(f"𝘏𝘦𝘳𝘦 𝘪𝘴 𝘺𝘰𝘶𝘳 𝘧𝘪𝘨𝘭𝘦𝘵 👉 :\n<pre>{kul_text}</pre>", quote=True, reply_markup=keyboard)

@app.on_callback_query(filters.regex("figlet"))
async def figlet_handler(Client, query: CallbackQuery):
  try:
      kul_text, keyboard = figle(text)
      await query.message.edit_text(f"𝘏𝘦𝘳𝘦 𝘪𝘴 𝘺𝘰𝘶𝘳 𝘧𝘪𝘨𝘭𝘦𝘵 👉 :\n<pre>{kul_text}</pre>", reply_markup=keyboard)
  except Exception as e : 
      await message.reply(e)
__mod_name__ = "Fɪɢʟᴇᴛ" 
__help__="""
❍ /figlet*:* ᴍᴀᴋᴇs ғɪɢʟᴇᴛ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
Example:\n\n`/figlet ANNIE `"""
