
import asyncio
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait,UserNotParticipant
import humanize
from info import *


@Client.on_message( filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    if (LAZY_MODE==True):
        if message.from_user.id in ADMINS :
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"""\n𝐌𝐚𝐯𝐢𝐌𝐨𝐝𝐬\n\n**Please tell, what should i do with this file.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝✧✧ S𝚝ar𝚝 re𝚗aᗰi𝚗g ✧✧📝", callback_data="rename") ],
                       [ InlineKeyboardButton("⨳  C L Ф S Ξ  ⨳", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))

        elif message.from_user.id in LAZY_RENAMERS :
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            try:
                text = f"""\n 𝐌𝐚𝐯𝐢𝐌𝐨𝐝𝐬\n\n**Please tell, what should i do with this file.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("📝✧✧ S𝚝ar𝚝 re𝚗aᗰi𝚗g ✧✧📝", callback_data="rename") ],
                           [ InlineKeyboardButton("⨳  C L Ф S Ξ  ⨳", callback_data="cancel") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
                await sleep(FLOOD)
            except FloodWait as e:
                await sleep(e.value)
                text = f"""\n 𝐌𝐚𝐯𝐢𝐌𝐨𝐝𝐬 \n\n**Please tell, what should i do with this file.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
                buttons = [[ InlineKeyboardButton("📝✧✧ S𝚝ar𝚝 re𝚗aᗰi𝚗g ✧✧📝", callback_data="rename") ],
                           [ InlineKeyboardButton("⨳  C L Ф S Ξ  ⨳", callback_data="cancel") ]]
                await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
            except:
                pass
        else:
            file = getattr(message, message.media.value)
            filesize = humanize.naturalsize(file.file_size) 
            filename = file.file_name
            text = f"""\n 𝐌𝐚𝐯𝐢𝐌𝐨𝐝𝐬 \n\n**Please tell, what should i do with this file.?**\n\n**🎞File Name** :- `{filename}`\n\n⚙️**File Size** :- `{filesize}`"""
            buttons = [[ InlineKeyboardButton("📝✧✧ S𝚝ar𝚝 re𝚗aᗰi𝚗g ✧✧📝", callback_data="requireauth") ],
                        [ InlineKeyboardButton("⨳  C L Ф S Ξ  ⨳", callback_data="cancel") ]]
            await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        return

