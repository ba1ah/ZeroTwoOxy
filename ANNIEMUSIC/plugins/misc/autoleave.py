import asyncio
from datetime import datetime

from pyrogram.enums import ChatType

import config
from ANNIEMUSIC import app
from ANNIEMUSIC.core.call import JARVIS, autoend
from ANNIEMUSIC.utils.database import get_client, is_active_chat, is_autoend


async def auto_leave():
    pass  # This function does nothing, effectively disabling the auto leave assistant feature


async def auto_end():
    while not await asyncio.sleep(5):
        ender = await is_autoend()
        if not ender:
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue
                autoend[chat_id] = {}
                try:
                    await JARVIS.stop_stream(chat_id)
                except:
                    continue
                try:
                    await app.send_message(
                        chat_id,
                        "» » 𝐁ᴏᴛ 𝐀ᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ 𝐋ᴇғᴛ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ 𝐁ᴇᴄᴀᴜsᴇ 𝐍ᴏ 𝐎ɴᴇ 𝐖ᴀs 𝐋ɪsᴛᴇɴɪɴɢ 𝐎ɴ 𝐕ɪᴅᴇᴏᴄʜᴀᴛ.",
                    )
                except:
                    continue


asyncio.create_task(auto_leave())
asyncio.create_task(auto_end())
