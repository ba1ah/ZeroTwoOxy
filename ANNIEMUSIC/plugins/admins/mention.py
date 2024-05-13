import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from ANNIEMUSIC import app
from ANNIEMUSIC.utils.jarvis_ban import admin_filter



spam_chats = []


@app.on_message(filters.command(["utag", "all", "mention"]) & filters.group & admin_filter)
async def tag_all_users(_,message): 
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("**𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐌ᴇssᴀɢᴇ 𝐎ʀ 𝐆ɪᴠᴇ 𝐒ᴏᴍᴇ 𝐓ᴇxᴛ 𝐓ᴏ 𝐓ᴀɢ 𝐀ʟʟ**") 
        return                  
    if replied:
        spam_chats.append(message.chat.id)      
        usernum= 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id): 
            if message.chat.id not in spam_chats:
                break       
            usernum += 5
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 1:
                await replied.reply_text(usertxt)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        try :
            spam_chats.remove(message.chat.id)
        except Exception:
            pass
    else:
        text = message.text.split(None, 1)[1]
        
        spam_chats.append(message.chat.id)
        usernum= 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):       
            if message.chat.id not in spam_chats:
                break 
            usernum += 1
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 5:
                await app.send_message(message.chat.id,f'{text}\n{usertxt}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""                          
        try :
            spam_chats.remove(message.chat.id)
        except Exception:
            pass        
           
@app.on_message(filters.command(["cancel", "ustop"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂ᴜʀʀᴇɴᴛʟʏ 𝐈'ᴍ 𝐍ᴏᴛ 𝐓ᴀɢɢɪɴɢ 𝐁ᴀʙʏ 😊")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ 𝐘ᴏᴜ 𝐀ʀᴇ 𝐍ᴏᴛ 𝐀ᴅᴍɪɴ 𝐁ᴀʙʏ, 𝐎ɴʟʏ 𝐀ᴅᴍɪɴs 𝐂ᴀɴ 𝐓ᴀɢ 𝐌ᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("**🦋 𝐌ᴇɴᴛɪᴏɴ 𝐏ʀᴏᴄᴇss 𝐒ᴛᴏᴘᴘᴇᴅ**")
