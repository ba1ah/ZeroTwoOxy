from pyrogram import Client, filters
import requests
from ANNIEMUSIC import app 

# Define a command handler for the /meme command
@app.on_message(filters.command("meme"))
def meme_command(client, message):
    # API endpoint for random memes
    api_url = "https://meme-api.com/gimme"

    try:
        # Make a request to the API
        response = requests.get(api_url)
        data = response.json()

        # Extract the meme image URL
        meme_url = data.get("url")
        title = data.get("title")

        # Mention the bot username in the caption
        caption = f"{title}\n\n🌟𝐑ᴇǫᴜᴇsᴛᴇᴅ 𝐁ʏ : {message.from_user.mention}\n⚡️𝐁ᴏᴛ 𝐔sᴇʀɴᴀᴍᴇ : @{app.get_me().username}"

        # Send the meme image to the user with the modified caption
        message.reply_photo(
            photo=meme_url,
            caption=caption
        )

    except Exception as e:
        print(f"Error fetching meme: {e}")
        message.reply_text("𝐒ᴏʀʀʏ, 𝐈 𝐂ᴏᴜʟᴅɴ'ᴛ 𝐅ᴇᴛᴄʜ 𝐀 𝐌ᴇᴍᴇ 𝐀ᴛ 𝐓ʜᴇ 𝐌ᴏᴍᴇɴᴛ.")
