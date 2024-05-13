from pyrogram import Client, filters
from ANNIEMUSIC import app
from config import BOT_USERNAME


def hex_to_text(hex_string):
    try:
        text = bytes.fromhex(hex_string).decode('utf-8')
        return text
    except Exception as e:
        return f"Error decoding hex: {str(e)}"


def text_to_hex(text):
    hex_representation = ' '.join(format(ord(char), 'x') for char in text)
    return hex_representation


# YOU KNOW ME VERY WELL...........................

@app.on_message(filters.command("code"))
def convert_text(_, message):
    if len(message.command) > 1:
        input_text = " ".join(message.command[1:])

        hex_representation = text_to_hex(input_text)
        decoded_text = hex_to_text(input_text)

        response_text = f"𝐈ɴᴘᴜᴛ 𝐓ᴇxᴛ ➪\n {input_text}\n\n𝐇ᴇx 𝐑ᴇᴘʀᴇsᴇɴᴛᴀᴛɪᴏɴ ➪\n {hex_representation}\n\n𝐃ᴇᴄᴏᴅᴇ 𝐓ᴇxᴛ ➪\n {decoded_text}\n\n\n𝐁ʏ ➪@{BOT_USERNAME}"

        message.reply_text(response_text)
    else:
        message.reply_text("𝐏ʟᴇᴀsᴇ 𝐏ʀᴏᴠɪᴅᴇ 𝐓ᴇxᴛ 𝐀ғᴛᴇʀ 𝐓𝐡𝐞 /code 𝐂ᴏᴍᴍᴀɴᴅ 👀.")
