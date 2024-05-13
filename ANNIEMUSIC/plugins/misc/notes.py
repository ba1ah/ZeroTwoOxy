from ANNIEMUSIC import app
from config import BOT_USERNAME
from pyrogram import filters
from ANNIEMUSIC.utils.jarvis_ban import admin_filter
from ANNIEMUSIC.mongo.notesdb import *
from ANNIEMUSIC.utils.notes_func import GetNoteMessage, exceNoteMessageSender, privateNote_and_admin_checker
from ANNIEMUSIC.utils.yumidb import user_admin
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.enums import ChatMemberStatus

# Command to save a note
@app.on_message(filters.command("save") & admin_filter)
@user_admin
async def save_note(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title
    if message.reply_to_message and len(message.command) < 2:
        return await message.reply_text("𝐘ᴏᴜ 𝐍ᴇᴇᴅ 𝐓ᴏ 𝐆ɪᴠᴇ 𝐀 𝐍ᴀᴍᴇ 𝐅ᴏʀ 𝐍ᴏᴛᴇ 🫣")

    if not message.reply_to_message and len(message.command) < 3:
        return await message.reply_text("𝐘ᴏᴜ 𝐍ᴇᴇᴅ 𝐓ᴏ 𝐆ɪᴠᴇ 𝐒ᴏᴍᴇ 𝐂ᴏɴᴛᴇɴᴛ 𝐅ᴏʀ 𝐍ᴏᴛᴇ 🫣")

    note_name = message.command[1]
    content, text, data_type = GetNoteMessage(message)
    
    try:
        await SaveNote(chat_id, note_name, content, text, data_type)
        await message.reply_text(f"𝐍ᴏᴛᴇ '{note_name}' 𝐇ᴀs 𝐁ᴇᴇɴ 𝐒ᴀᴠᴇᴅ 𝐈ɴ {chat_title}.")
    except Exception as e:
        await message.reply_text(f"𝐀ɴ 𝐄ʀʀᴏʀ 𝐎ᴄᴄᴜʀᴇᴅ 𝐖ʜɪʟᴇ 𝐒ᴀᴠɪɴɢ 𝐓ʜᴇ 𝐍ᴏᴛᴇ 😢: {str(e)}")

# Command to retrieve a note
@app.on_message(filters.command("get") & admin_filter)
async def get_note(client, message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        return await message.reply_text("𝐏ʟᴇᴀsᴇ 𝐒ᴘᴇᴄɪғʏ 𝐓ʜᴇ 𝐍ᴀᴍᴇ 𝐎ғ 𝐓ʜᴇ 𝐍ᴏᴛᴇ!")

    note_name = message.command[1]
    if not await isNoteExist(chat_id, note_name):
        return await message.reply_text("Note not found")

    await send_note(message, note_name)

# Regular expression to retrieve a note
@app.on_message(filters.regex(pattern=(r"^#[^\s]+")) & filters.group)
async def regex_get_note(client, message):
    chat_id = message.chat.id
    if message.from_user:
        note_name = message.text.split()[0].replace('#', '')
        if await isNoteExist(chat_id, note_name):
            await send_note(message, note_name)

# Command to toggle private notes setting
@app.on_message(filters.command("privatenotes") & filters.group)
@user_admin
async def private_notes(client, message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        return await message.reply_text("𝐏ʟᴇᴀsᴇ 𝐒ᴘᴇᴄɪғʏ 'on' 𝐎ʀ 'off'!")

    setting = message.command[1].lower()
    if setting in ['on', 'off']:
        await set_private_note(chat_id, setting == 'on')
        await message.reply_text(f"𝐏ʀɪᴠᴀᴛᴇ 𝐍ᴏᴛᴇs 𝐒ᴇᴛᴛɪɴɢs 𝐔ᴘᴅᴀᴛᴇᴅ 𝐓ᴏ '{setting}'.")
    else:
        await message.reply_text("𝐈ɴᴠᴀʟɪᴅ 𝐒ᴇᴛᴛɪɴɢ. 𝐏ʟᴇᴀsᴇ 𝐒ᴘᴇᴄɪғʏ 'on' 𝐎ʀ 'off'!")

# Command to clear a specific note
@app.on_message(filters.command("clear") & admin_filter)
@user_admin
async def clear_note(client, message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        return await message.reply_text("𝐏ʟᴇᴀsᴇ 𝐒ᴘᴇᴄɪғʏ 𝐓ʜᴇ 𝐍ᴀᴍᴇ 𝐎ғ 𝐓ʜᴇ 𝐍ᴏᴛᴇ!")

    note_name = message.command[1].lower()
    if await isNoteExist(chat_id, note_name):
        await ClearNote(chat_id, note_name)
        await message.reply_text(f"𝐍ᴏᴛᴇ '{note_name}' 𝐇ᴀs 𝐁ᴇᴇɴ 𝐃ᴇʟᴇᴛᴇᴅ.")
    else:
        await message.reply_text("Note not found.")

# Command to clear all notes
@app.on_message(filters.command("clearall") & admin_filter)
async def clear_all_notes(client, message):
    owner_id = message.from_user.id
    chat_id = message.chat.id
    chat_title = message.chat.title
    user = await client.get_chat_member(chat_id, owner_id)
    if user.status != ChatMemberStatus.OWNER:
        return await message.reply_text("𝐎ɴʟʏ 𝐎ᴡɴᴇʀ 𝐂ᴀɴ 𝐔sᴇ 𝐓ʜɪs 😛")

    note_list = await NoteList(chat_id)
    if not note_list:
        return await message.reply_text(f"No notes found in {chat_title}.")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='Delete all notes', callback_data=f'clearallnotes_clear_{owner_id}_{chat_id}')],
        [InlineKeyboardButton(text='Cancel', callback_data=f'clearallnotes_cancel_{owner_id}')]
    ])
    await message.reply_text(
        f"𝐀ʀᴇ 𝐘ᴏᴜ 𝐒ᴜʀᴇ 𝐖ᴀɴᴛ 𝐓ᴏ 𝐃ᴇʟᴇᴛᴇ **ALL** 𝐍ᴏᴛᴇs 𝐈ɴ {chat_title}? 𝐓ʜɪs 𝐀ᴄᴛɪᴏɴ 𝐈s 𝐈ʀʀᴇᴠᴇʀsɪʙʟᴇ.",
        reply_markup=keyboard
    )

# Callback query handler for clearing all notes
@app.on_callback_query(filters.regex("^clearallnotes_"))
async def clear_all_callback(client, callback_query: CallbackQuery):
    query_data = callback_query.data.split('_')[1]
    owner_id = int(callback_query.data.split('_')[2])
    user_id = callback_query.from_user.id

    if owner_id == user_id:
        if query_data == 'clear':
            chat_id = int(callback_query.data.split('_')[3])
            await ClearAllNotes(chat_id)
            await callback_query.answer("𝐀ʟʟ 𝐍ᴏᴛᴇs 𝐇ᴀs 𝐁ᴇᴇɴ 𝐃ᴇʟᴇᴛᴇᴅ.")
        elif query_data == 'cancel':
            await callback_query.answer("Cancelled.")
    else:
        await callback_query.answer("𝐎ɴʟʏ 𝐀ᴅᴍɪɴs 𝐂ᴀɴ 𝐄xᴇᴄᴜᴛᴇ 𝐓ʜɪs 𝐂ᴏᴍᴍᴀɴᴅ!")

# Command to list all saved notes
@app.on_message(filters.command(['notes', 'saved']) & filters.group)
async def list_notes(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title
    notes_list = await NoteList(chat_id)
    if notes_list:
        note_header = f"List of notes in {chat_title}:\n"
        note_list_str = '\n'.join([f" • `#{note}`" for note in notes_list])
        await message.reply_text(
            f"{note_header}{note_list_str}\n𝐘ᴏᴜ 𝐂ᴀɴ 𝐑ᴇᴛʀɪᴇᴠᴇ 𝐓ʜᴇsᴇ 𝐍ᴏᴛᴇs 𝐔sɪɴɢ `/get notename` 𝐎ʀ `#notename`.",
            quote=True
        )
    else:
        await message.reply_text(f"𝐍ᴏ 𝐍ᴏᴛᴇs 𝐅ᴏᴜɴᴅ 𝐈ɴ {chat_title}.", quote=True)

# Function to send a note message
async def send_note(message, note_name):
    chat_id = message.chat.id
    content, text, data_type = await GetNote(chat_id, note_name)
    private_note, allow = await privateNote_and_admin_checker(message, text)
    if allow:
        if private_note is None or private_note == await is_pnote_on(chat_id):
            if private_note:
                await private_note_button(message, chat_id, note_name)
            else:
                await exceNoteMessageSender(message, note_name)

# Function to send a private note button
async def private_note_button(message, chat_id, note_name):
    private_note_button = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='𝐂ʟɪᴄᴋ 𝐌ᴇ!', url=f'http://t.me/{BOT_USERNAME}?start=note_{chat_id}_{note_name}')]
    ])
    await message.reply_text(
        text=f"𝐓ᴀᴘ 𝐇ᴇʀᴇ 𝐓ᴏ 𝐕ɪᴇᴡ '{note_name}' 𝐈ɴ 𝐘ᴏᴜʀ 𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ.",
        reply_markup=private_note_button
    )
