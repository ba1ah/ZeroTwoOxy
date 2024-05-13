from pyrogram import Client, filters
from pyrogram.types import Message
import requests
from ANNIEMUSIC import app


@app.on_message(filters.command("population"))
def country_command_handler(client: Client, message: Message):
    # Extract the country code from the command
    country_code = message.text.split(maxsplit=1)[1].strip()

    # Call the external API for country information
    api_url = f"https://restcountries.com/v3.1/alpha/{country_code}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        country_info = response.json()
        if country_info:
            # Extract relevant information from the API response
            country_name = country_info[0].get("name", {}).get("common", "N/A")
            capital = country_info[0].get("capital", ["N/A"])[0]
            population = country_info[0].get("population", "N/A")

            response_text = (
                f"Country Information\n\n"
                f"Name: {country_name}\n"
                f"Capital: {capital}\n"
                f"Population: {population}"
            )
        else:
            response_text = "𝐄ʀʀᴏʀ 𝐅ᴇᴛᴄʜɪɴɢ 𝐂ᴏᴜɴᴛʀʏ 𝐈ɴғᴏʀᴍᴀᴛɪᴏɴ 𝐅ʀᴏᴍ 𝐓ʜᴇ 𝐀𝐏𝐈."
    except requests.exceptions.HTTPError as http_err:
        response_text = f"𝐇𝐓𝐓𝐏 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀʀᴇᴅ 𝐄ɴᴛᴇʀ 𝐂ᴏʀʀᴇᴄᴛ 𝐂ᴏᴜɴᴛʀʏ 𝐂ᴏᴅᴇ"
    except Exception as err:
        response_text = f" Error @githubxd"

    # Send the response to the Telegram chat
    message.reply_text(response_text)
