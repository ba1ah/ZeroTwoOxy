import random 
from pyrogram import filters,Client,enums
from ANNIEMUSIC import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram.types import ChatPermissions
from ANNIEMUSIC.mongo.nightmodedb import nightdb,nightmode_on,nightmode_off,get_nightchats 



CLOSE_CHAT = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages = False,
    can_send_other_messages = False,
    can_send_polls = False,
    can_change_info = False,
    can_add_web_page_previews = False,
    can_pin_messages = False,
    can_invite_users = False )


OPEN_CHAT = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages = True,
    can_send_other_messages = True,
    can_send_polls = True,
    can_change_info = True,
    can_add_web_page_previews = True,
    can_pin_messages = True,
    can_invite_users = True )
    
buttons = InlineKeyboardMarkup([[InlineKeyboardButton("𝐄ɴᴀʙʟᴇ 🌟", callback_data="add_night"),InlineKeyboardButton("𝐃ɪsᴀʙʟᴇ 🌑", callback_data="rm_night")]])         

@app.on_message(filters.command("nightmode") & filters.group)
async def _nightmode(_, message):
    return await message.reply_photo(photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg", caption="**𝐂ʟɪᴄᴋ 𝐎ɴ 𝐓ʜᴇ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐄ɴᴀʙʟᴇ / 𝐃ɪsᴀʙʟᴇ 𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐈ɴ 𝐓ʜɪs 𝐂ʜᴀᴛ.**",reply_markup=buttons)
              
     
@app.on_callback_query(filters.regex("^(add_night|rm_night)$"))
async def nightcb(_, query : CallbackQuery):
    data = query.data 
    chat_id = query.message.chat.id
    user_id = query.from_user.id
    check_night = await nightdb.find_one({"chat_id" : chat_id})
    administrators = []
    async for m in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m.user.id)     
    if user_id in administrators:   
        if data == "add_night":
            if check_night:        
                await query.message.edit_caption("**𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐈s 𝐀ʟʀᴇᴀᴅʏ 𝐄ɴᴀʙʟᴇᴅ 𝐈ɴ 𝐓ʜɪs 𝐂ʜᴀᴛ.**")
            elif not check_night :
                await nightmode_on(chat_id)
                await query.message.edit_caption("**𝐀ᴅᴅᴇᴅ 𝐂ʜᴀᴛ 𝐓ᴏ 𝐌ʏ 𝐃ᴀᴛᴀʙᴀsᴇ . 𝐓ʜɪs 𝐆ʀᴏᴜᴘ 𝐖ɪʟʟ 𝐁ᴇ 𝐂ʟᴏsᴇᴅ 𝐎ɴ 𝟷𝟸𝐀ᴍ [𝐈𝐒𝐓] 𝐀ɴᴅ 𝐖ɪʟʟ 𝐎ᴘᴇɴᴇᴅ 𝐎ɴ 𝟶𝟼𝐀ᴍ [𝐈𝐒𝐓]**") 
        if data == "rm_night":
            if check_night:  
                await nightmode_off(chat_id)      
                await query.message.edit_caption("**𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐑ᴇᴍᴏᴠᴇᴅ 𝐅ʀᴏᴍ 𝐌ʏ 𝐃ᴀᴛᴀʙᴀsᴇ**")
            elif not check_night:
                await query.message.edit_caption("**𝐍ɪɢʜᴛᴍᴏᴅᴇ 𝐈s 𝐀ʟʀᴇᴀᴅʏ 𝐃ɪsᴀʙʟᴇᴅ 𝐈ɴ 𝐓ʜɪs 𝐂ʜᴀᴛ.**") 
            
    
    
async def start_nightmode() :
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for add_chat in chats:
        try:
            await app.send_photo(
                add_chat,
                photo="https://telegra.ph//file/06649d4d0bbf4285238ee.jpg",
                caption= f"**𝐌ᴀʏ 𝐓ʜᴇ 𝐀ɴɢᴇʟs 𝐅ʀᴏᴍ 𝐓ʜᴇ 𝐇ᴇᴀᴠᴇɴ 𝐁ʀɪɴɢ 𝐓ʜᴇ 𝐒ᴡᴇᴇᴛᴇsᴛ 𝐎ғ 𝐀ʟʟ 𝐃ʀᴇᴀᴍs 𝐅ᴏʀ 𝐘ᴏᴜ. 𝐌ᴀʏ 𝐘ᴏᴜ 𝐇ᴀᴠᴇ 𝐋ᴏɴɢ 𝐀ɴᴅ 𝐁ʟɪssғᴜʟʟ 𝐒ʟᴇᴇᴘ 𝐖ɪᴛʜ 𝐅ᴜʟʟ 𝐎ғ 𝐇ᴀᴘᴘʏ 𝐃ʀᴇᴀᴍs.\n\n𝐆ʀᴏᴜᴏ 𝐈s 𝐂ʟᴏsɪɴɢ 𝐆ᴏᴏᴅ 𝐍ɪɢʜᴛ 𝐄ᴠᴇʀʏᴏɴᴇ 🥱**")
            
            await app.set_chat_permissions(add_chat,CLOSE_CHAT)

        except Exception as e:
            print(f"[bold red] 𝐔ɴᴀʙʟᴇ 𝐓ᴏ 𝐂ʟᴏsᴇ 𝐆ʀᴏᴜᴘ {add_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(start_nightmode, trigger="cron", hour=23, minute=59)
scheduler.start()

async def close_nightmode():
    chats = []
    schats = await get_nightchats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    if len(chats) == 0:
        return
    for rm_chat in chats:
        try:
            await app.send_photo(
                rm_chat,
                photo="https://telegra.ph//file/14ec9c3ff42b59867040a.jpg",
                caption= f"**ɢʀᴏᴜᴘ ɪs ᴏᴘᴇɴɪɴɢ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴇᴠᴇʀʏᴏɴᴇ !\n\nᴍᴀʏ ᴛʜɪs ᴅᴀʏ ᴄᴏᴍᴇ ᴡɪᴛʜ ᴀʟʟ ᴛʜᴇ ʟᴏᴠᴇ ʏᴏᴜʀ ʜᴇᴀʀᴛ ᴄᴀɴ ʜᴏʟᴅ ᴀɴᴅ ʙʀɪɴɢ ʏᴏᴜ ᴇᴠᴇʀʏ sᴜᴄᴄᴇss ʏᴏᴜ ᴅᴇsɪʀᴇ. Mᴀʏ ᴇᴀᴄʜ ᴏғ ʏᴏᴜʀ ғᴏᴏᴛsᴛᴇᴘs ʙʀɪɴɢ Jᴏʏ ᴛᴏ ᴛʜᴇ ᴇᴀʀᴛʜ ᴀɴᴅ ʏᴏᴜʀsᴇʟғ. ɪ ᴡɪsʜ ʏᴏᴜ ᴀ ᴍᴀɢɪᴄᴀʟ ᴅᴀʏ ᴀɴᴅ ᴀ ᴡᴏɴᴅᴇʀғᴜʟ ʟɪғᴇ ᴀʜᴇᴀᴅ.**")
            
            await app.set_chat_permissions(rm_chat,OPEN_CHAT)

        except Exception as e:
            print(f"[bold red] 𝐔ɴᴀʙʟᴇ 𝐓ᴏ 𝐎ᴘᴇɴ 𝐆ʀᴏᴜᴘ {rm_chat} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(close_nightmode, trigger="cron", hour=6, minute=1)
scheduler.start()



