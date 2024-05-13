from pyrogram import Client, filters
from ANNIEMUSIC import app


@app.on_message(filters.command("weather"))
def weather(client, message):
    try:
        # Get the location from user message
        user_input = message.command[1]
        location = user_input.strip()
        weather_url = f"https://wttr.in/{location}.png"
        
        # Reply with the weather information as a photo
        message.reply_photo(photo=weather_url, caption="Here's the weather for your location")
    except IndexError:
        # User didn't provide a location
        message.reply_text("𝐏ʟᴇᴀsᴇ 𝐏ʀᴏᴠɪᴅᴇ 𝐀 𝐋ᴏᴄᴀᴛɪᴏɴ. 𝐔sᴇ /weather CHENNAI")
