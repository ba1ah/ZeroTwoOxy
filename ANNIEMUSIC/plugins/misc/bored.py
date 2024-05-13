from pyrogram import Client, filters
import requests
from ANNIEMUSIC import app

# URL for the Bored API
bored_api_url = "https://apis.scrimba.com/bored/api/activity"


# Function to handle /bored command
@app.on_message(filters.command("bored", prefixes="/"))
async def bored_command(client, message):
    # Fetch a random activity from the Bored API
    response = requests.get(bored_api_url)
    if response.status_code == 200:
        data = response.json()
        activity = data.get("activity")
        if activity:
            # Send the activity to the user who triggered the command
            await message.reply(f"𝐅ᴇᴇʟɪɴɢ 𝐁ᴏʀᴇᴅ? 😦 𝐇ᴏᴡ 𝐀ʙᴏᴜᴛ:\n\n {activity}")
        else:
            await message.reply("𝐍ᴏ 𝐀ᴄᴛɪᴠɪᴛʏ 𝐅ᴏᴜɴᴅ.")
    else:
        await message.reply("𝐅ᴀɪʟᴇᴅ 𝐓ᴏ 𝐅ᴇᴛᴄʜ 𝐀ᴄᴛɪᴠɪᴛʏ.")
