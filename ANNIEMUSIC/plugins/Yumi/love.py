from pyrogram import Client, filters
import random
from ANNIEMUSIC import app

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "❤️ 𝐋ᴏᴠᴇ 𝐈s 𝐈ɴ 𝐓ʜᴇ 𝐀ɪʀ, 𝐁ᴜᴛ 𝐍ᴇᴇᴅs 𝐀 𝐋ɪᴛᴛʟᴇ 𝐒ᴘᴀʀᴋ ⚡️.",
            "𝐀 𝐆ᴏᴏᴅ 𝐒ᴛᴀʀᴛ 𝐁ᴜᴛ ✨ 𝐓ʜᴇʀᴇ's 𝐑ᴏᴏᴍ 𝐓ᴏ 𝐆ʀᴏᴡ.",
            "𝐈ᴛ's 𝐈ᴜsᴛ 𝐓ʜᴇ 𝐁ᴇɢɪɴɴɪɴɢ 𝐎ғ 𝐒ᴏᴍᴇᴛʜɪɴɢ 𝐁ᴇᴀᴜᴛɪғᴜʟ ☘️."
        ])
    elif love_percentage <= 70:
        return random.choice([
            "𝐀 𝐒ᴛʀᴏɴɢ 𝐂ᴏɴɴᴇᴄᴛɪᴏɴ ɪs 𝐓ʜᴇʀᴇ. 𝐊ᴇᴇᴘ 𝐍ᴜʀᴛᴜʀɪɴɢ 𝐈ᴛ ❤️.",
            "𝐘ᴏᴜ'ᴠᴇ 𝐆ᴏᴛ 𝐀 𝐆ᴏᴏᴅ 𝐂ʜᴀɴᴄᴇ. 𝐖ᴏʀᴋ 𝐎ɴ 𝐈ᴛ 😘.",
            "𝐋ᴏᴠᴇ 𝐈s 𝐁ʟᴏssᴏᴍɪɴɢ, 🙈 𝐊ᴇᴇᴘ 𝐆ᴏɪɴɢ."
        ])
    else:
        return random.choice([
            "𝐖ᴏᴡ ❤️, 𝐈ᴛs 𝐀 𝐌ᴀᴛᴄʜ 𝐌ᴀᴅᴇ 𝐈𝐧 𝐇ᴇᴀᴠᴇɴ 😘",
            "𝐏ᴇʀғᴇᴄᴛ 𝐌ᴀᴛᴄʜ 🙈, 𝐂ʜᴇʀɪsʜ 𝐓ʜɪs 𝐁ᴏɴᴅ 😚.",
            "𝐋ᴏᴠᴇʟʏ 𝐂ᴏᴜᴘʟᴇs 🥰, 𝐂ᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs!!"
        ])
        
@app.on_message(filters.command("love", prefixes="/"))
def love_command(client, message):
    command, *args = message.text.split(" ")
    if len(args) >= 2:
        name1 = args[0].strip()
        name2 = args[1].strip()
        
        love_percentage = random.randint(10, 100)
        love_message = get_random_message(love_percentage)

        response = f"{name1}💕 + {name2}💕 = {love_percentage}%\n\n{love_message}"
    else:
        response = "𝐏ʟᴇᴀsᴇ 𝐄ɴᴛᴇʀ 𝐓ᴡᴏ 𝐍ᴀᴍᴇs 𝐀ғᴛᴇʀ /love 𝐂ᴏᴍᴍᴀɴᴅ."
    app.send_message(message.chat.id, response)
