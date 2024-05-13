from pyrogram import Client, filters
from pyrogram.types import Message
from ANNIEMUSIC import app 

# Command to generate a direct WhatsApp link
@app.on_message(filters.command("WhatsApp"))
async def generate_whatsapp_link(client, message: Message):
    if len(message.command) < 2:
        await message.reply("𝐏ʟᴇᴀsᴇ enter your phone number after the command. Example: /WhatsApp +1234567890")
        return

    phone_number = message.command[1]

    # Generate the WhatsApp link
    whatsapp_link = f"https://wa.me/{phone_number}"

    await message.reply(f"𝐂ʟɪᴄᴋ 𝐓ʜᴇ 𝐋ɪɴᴋ 𝐓ᴏ 𝐎ᴘᴇɴ 𝐖ʜᴀᴛs𝐀ᴘᴘ 𝐖ɪᴛʜ 𝐓ʜᴇ 𝐍ᴜᴍʙᴇʀ {phone_number}:\n{whatsapp_link}")
