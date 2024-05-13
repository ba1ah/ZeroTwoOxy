from pyrogram import Client, filters
from pyrogram.types import Message
import traceback
from ANNIEMUSIC import app




@app.on_message(filters.command("python"))
async def execute_python_code(client, message: Message):
    if len(message.command) < 2:
        await message.reply("𝐏ʟᴇᴀsᴇ 𝐄ɴᴛᴇʀ 𝐘ᴏᴜʀ 𝐏ʏᴛʜᴏɴ 𝐂ᴏᴅᴇ 𝐀ғᴛᴇʀ 𝐓ʜᴇ 𝐂ᴏᴍᴍᴀɴᴅ. 𝐄xᴀᴍᴘʟᴇ: /python print ('𝐇ᴇʟʟᴏ, 𝐖ᴏʀʟᴅ!')")
        return

    python_code = " ".join(message.command[1:])
    
    try:
        # Execute the Python code
        exec_result = exec(python_code)
        await message.reply(f"𝐂ᴏᴅᴇ 𝐄xᴇᴄᴜᴛᴇᴅ 𝐒ᴜᴄᴄᴇssғᴜʟʟʏ. 𝐑ᴇsᴜʟᴛ: {exec_result}")
    except Exception as e:
        # Handle code execution errors
        traceback_str = traceback.format_exc()
        await message.reply(f"𝐂ᴏᴅᴇ 𝐄xᴇᴄᴜᴛɪᴏɴ 𝐄ʀʀᴏʀ: {str(e)}\nTraceback:\n{traceback_str}")
