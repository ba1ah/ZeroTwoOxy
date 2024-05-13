from pyrogram import Client, filters
import requests
from ANNIEMUSIC import app

@app.on_message(filters.command("slap") & ~filters.forwarded & ~filters.via_bot)
def slap_command(client, message):
    try:

        sender = message.from_user.mention(style='markdown')

        target = sender if not message.reply_to_message else message.reply_to_message.from_user.mention(style='markdown')

        
        response = requests.get("https://api.waifu.pics/sfw/slap")
        response.raise_for_status()

        gif_url = response.json().get("url")

        if gif_url:
            msg = f"{sender} 𝐒ʟᴀᴘᴘᴇᴅ 😁 {target}! 😒"
            message.reply_animation(animation=gif_url, caption=msg)
        else:
            message.reply_text("𝐂ᴏᴜʟᴅɴ'ᴛ 𝐑ᴇᴛʀɪᴇᴠᴇ 𝐓ʜᴇ 𝐀ɴɪᴍᴀᴛɪᴏɴ. 𝐏ʟᴇᴀsᴇ 𝐓ʀʏ 𝐀ɢᴀɪɴ.")
        
    except requests.exceptions.RequestException as e:
        message.reply_text(f"𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ 𝐖ʜɪʟᴇ 𝐌ᴀᴋɪɴɢ 𝐓ʜᴇ 𝐑ᴇǫᴜᴇsᴛ: {e}")
    except Exception as e:
        
        message.reply_text(f"𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ: {str(e)}")
