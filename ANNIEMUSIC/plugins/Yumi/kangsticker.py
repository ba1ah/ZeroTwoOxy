
import imghdr
import os
from asyncio import gather
from traceback import format_exc

from pyrogram import filters
from pyrogram.errors import (
    PeerIdInvalid,
    ShortnameOccupyFailed,
    StickerEmojiInvalid,
    StickerPngDimensions,
    StickerPngNopng,
    UserIsBlocked,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from ANNIEMUSIC import app
from config import BOT_USERNAME
from ANNIEMUSIC.utils.errors import capture_err

from ANNIEMUSIC.utils.files import (
    get_document_from_file_id,
    resize_file_to_sticker_size,
    upload_document,
)

from ANNIEMUSIC.utils.stickerset import (
    add_sticker_to_set,
    create_sticker,
    create_sticker_set,
    get_sticker_set_by_name,
)

# -----------

MAX_STICKERS = (
    120  # would be better if we could fetch this limit directly from telegram
)
SUPPORTED_TYPES = ["jpeg", "png", "webp"]
# ------------------------------------------
@app.on_message(filters.command("get_sticker"))
@capture_err
async def sticker_image(_, message: Message):
    r = message.reply_to_message

    if not r:
        return await message.reply("𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐒ᴛɪᴄᴋᴇʀ 🙆‍♂.")

    if not r.sticker:
        return await message.reply("𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐒ᴛɪᴄᴋᴇʀ 🙆‍♂.")

    m = await message.reply("𝐒ᴇɴᴅɪɴɢ....💫")
    f = await r.download(f"{r.sticker.file_unique_id}.png")

    await gather(
        *[
            message.reply_photo(f),
            message.reply_document(f),
        ]
    )

    await m.delete()
    os.remove(f)
#----------------
@app.on_message(filters.command("kang"))
@capture_err
async def kang(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("𝐑ᴇᴘʟʏ 𝐓ᴏ 𝐀 𝐒ᴛɪᴄᴋᴇʀ / 𝐈ᴍᴀɢᴇ 𝐓ᴏ 𝐊ᴀɴɢ 𝐈ᴛ.")
    if not message.from_user:
        return await message.reply_text(
            "𝐘ᴏᴜ 𝐀ʀᴇ 𝐍ᴏᴡ 𝐀ɴᴏɴʏᴍᴏᴜs 𝐀ᴅᴍɪɴ, 𝐊ᴀɴɢ 𝐒ᴛɪᴄᴋᴇʀs 𝐈ɴ 𝐌ʏ 𝐏ᴍ."
        )
    msg = await message.reply_text("𝐊ᴀɴɢɪɴɢ 𝐒ᴛɪᴄᴋᴇʀs...💫")

    # Find the proper emoji
    args = message.text.split()
    if len(args) > 1:
        sticker_emoji = str(args[1])
    elif (
        message.reply_to_message.sticker
        and message.reply_to_message.sticker.emoji
    ):
        sticker_emoji = message.reply_to_message.sticker.emoji
    else:
        sticker_emoji = "🤔"

    # Get the corresponding fileid, resize the file if necessary
    doc = message.reply_to_message.photo or message.reply_to_message.document
    try:
        if message.reply_to_message.sticker:
            sticker = await create_sticker(
                await get_document_from_file_id(
                    message.reply_to_message.sticker.file_id
                ),
                sticker_emoji,
            )
        elif doc:
            if doc.file_size > 10000000:
                return await msg.edit("𝐅ɪʟᴇ 𝐒ɪᴢᴇ 𝐓ᴏᴏ 𝐋ᴀʀɢᴇ 🍌.")

            temp_file_path = await app.download_media(doc)
            image_type = imghdr.what(temp_file_path)
            if image_type not in SUPPORTED_TYPES:
                return await msg.edit(
                    "Format not supported! ({})".format(image_type)
                )
            try:
                temp_file_path = await resize_file_to_sticker_size(
                    temp_file_path
                )
            except OSError as e:
                await msg.edit_text("𝐒ᴏᴍᴇᴛʜɪɴɢ 𝐖ᴇɴᴛ 𝐖𝐫𝐨𝐧𝐠 🍒.")
                raise Exception(
                    f"Something went wrong while resizing the sticker (at {temp_file_path}); {e}"
                )
            sticker = await create_sticker(
                await upload_document(client, temp_file_path, message.chat.id),
                sticker_emoji,
            )
            if os.path.isfile(temp_file_path):
                os.remove(temp_file_path)
        else:
            return await msg.edit("𝐎ᴏᴘs, 𝐂ᴀɴ'ᴛ 𝐊ᴀɴɢ 𝐓ʜᴀᴛ 🚨.")
    except ShortnameOccupyFailed:
        await message.reply_text("𝐂ʜᴀɴɢᴇ 𝐘ᴏᴜʀ 𝐍ᴀᴍᴇ 𝐎ʀ 𝐔sᴇʀɴᴀᴍᴇ 𝐏ʟᴇᴀsᴇ")
        return

    except Exception as e:
        await message.reply_text(str(e))
        e = format_exc()
        return print(e)
#-------
    packnum = 0
    packname = "f" + str(message.from_user.id) + "_by_" + BOT_USERNAME
    limit = 0
    try:
        while True:
            # Prevent infinite rules
            if limit >= 50:
                return await msg.delete()

            stickerset = await get_sticker_set_by_name(client, packname)
            if not stickerset:
                stickerset = await create_sticker_set(
                    client,
                    message.from_user.id,
                    f"{message.from_user.first_name[:32]}'s kang pack",
                    packname,
                    [sticker],
                )
            elif stickerset.set.count >= MAX_STICKERS:
                packnum += 1
                packname = (
                    "f"
                    + str(packnum)
                    + "_"
                    + str(message.from_user.id)
                    + "_by_"
                    + BOT_USERNAME
                )
                limit += 1
                continue
            else:
                try:
                    await add_sticker_to_set(client, stickerset, sticker)
                except StickerEmojiInvalid:
                    return await msg.edit("[ERROR]: INVALID_EMOJI_IN_ARGUMENT")
            limit += 1
            break

        await msg.edit(
            "Sticker Kanged To [Pack](t.me/addstickers/{})\nEmoji: {}".format(
                packname, sticker_emoji
            )
        )
    except (PeerIdInvalid, UserIsBlocked):
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="Start", url=f"t.me/{BOT_USERNAME}")]]
        )
        await msg.edit(
            "𝐘ᴏᴜ 𝐍ᴇᴇᴅ 𝐓ᴏ 𝐒ᴛᴀʀᴛ 𝐀 𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ 𝐖ɪᴛʜ 𝐌ᴇ.",
            reply_markup=keyboard,
        )
    except StickerPngNopng:
        await message.reply_text(
            "𝐒ᴛɪᴄᴋᴇʀs 𝐌ᴜsᴛ 𝐁ᴇ 𝐈ɴ 𝐏ɴɢ 𝐅ᴏʀᴍᴀᴛ 🚧"
        )
    except StickerPngDimensions:
        await message.reply_text("𝐓ʜᴇ 𝐒ᴛɪᴄᴋᴇᴛ 𝐏ɴɢ 𝐃ɪᴍᴇɴsɪᴏɴs 𝐀ʀᴇ 𝐈ɴᴠᴀʟɪᴅ.")
