from pyrogram import Client, filters
import requests
import random
from ANNIEMUSIC import app

# Truth or Dare API URLs
truth_api_url = "https://api.truthordarebot.xyz/v1/truth"
dare_api_url = "https://api.truthordarebot.xyz/v1/dare"


@app.on_message(filters.command("truth"))
def get_truth(client, message):
    try:
        # Make a GET request to the Truth API
        response = requests.get(truth_api_url)
        if response.status_code == 200:
            truth_question = response.json()["question"]
            message.reply_text(f"𝐓ʀᴜᴛʜ 𝐐ᴜᴇsᴛɪᴏɴ:\n\n{truth_question}")
        else:
            message.reply_text("𝐅ᴀɪʟᴇᴅ 𝐓ᴏ 𝐅ᴇᴛᴄʜ 𝐀 𝐓ʀᴜᴛʜ 𝐐ᴜᴇsᴛɪᴏɴ. 𝐏ʟᴇᴀsᴇ 𝐓ʀʏ 𝐀ɢᴀɪɴ 𝐋ᴀᴛᴇʀ.")
    except Exception as e:
        message.reply_text("𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀᴇᴅ 𝐖ʜɪʟᴇ 𝐅ᴇᴛᴄʜɪɴɢ 𝐀 𝐓ʀᴜᴛʜ 𝐐ᴜᴇsᴛɪᴏɴ. 𝐏ʟᴇᴀsᴇ 𝐓ʀʏ 𝐀ɢᴀɪɴ 𝐋ᴀᴛᴇʀ")

@app.on_message(filters.command("dare"))
def get_dare(client, message):
    try:
        # Make a GET request to the Dare API
        response = requests.get(dare_api_url)
        if response.status_code == 200:
            dare_question = response.json()["question"]
            message.reply_text(f"𝐃ᴀʀᴇ 𝐐ᴜᴇsᴛɪᴏɴ:\n\n{dare_question}")
        else:
            message.reply_text("𝐅ᴀɪʟᴇᴅ 𝐓ᴏ 𝐅ᴇᴛᴄʜ 𝐀 𝐃ᴀʀᴇ 𝐐ᴜᴇsᴛɪᴏɴ. 𝐏ʟᴇᴀsᴇ 𝐓ʀʏ 𝐀ɢᴀɪɴ 𝐋ᴀᴛᴇʀ.")
    except Exception as e:
        message.reply_text("𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀᴇᴅ 𝐖ʜɪʟᴇ 𝐅ᴇᴛᴄʜɪɴɢ 𝐀 𝐃ᴀʀᴇ 𝐐ᴜᴇsᴛɪᴏɴ. 𝐏ʟᴇᴀsᴇ 𝐓ʀʏ 𝐀ɢᴀɪɴ 𝐋ᴀᴛᴇʀ")
