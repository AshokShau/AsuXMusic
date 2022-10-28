import os
import random
import asyncio

from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton, Message)
from config import get_queue
from asyncio import QueueEmpty
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream, InputStream

from AsuXMusic import BOT_NAME, app, db_mem
from AsuXMusic.Cache.admins import AdminRightsCheck
from AsuXMusic.Cache.checker import checker, checkerCB
from AsuXMusic.Helpers.Ytinfo import get_yt_info_id
from AsuXMusic.Helpers.Thumbnails import thumb_init
from AsuXMusic.Helpers.Changers import time_to_seconds
from AsuXMusic.Helpers.PyTgCalls import Queues, AsuX
from AsuXMusic.Helpers.PyTgCalls.Converter import convert
from AsuXMusic.Helpers.PyTgCalls.Downloader import download
from AsuXMusic.Helpers.Inline import primary_markup, close_key, audio_markup
from AsuXMusic.Helpers.Database import (is_active_chat, is_music_playing, music_off,
                            music_on, remove_active_chat)


loop = asyncio.get_event_loop()


__MODULE__ = "Aᴅᴍɪɴs"
__HELP__ = """


/pause
» ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.

/resume
» ʀᴇsᴜᴍᴇᴅ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.

/skip ᴏʀ /next
» sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴏɴɢᴏɪɴɢ sᴛʀᴇᴀᴍ.

/end ᴏʀ /stop
» ᴇɴᴅ ᴛʜᴇ ᴄᴜʀᴇᴇɴᴛ ᴏɴɢᴏɪɴ sᴛʀᴇᴀᴍ.

/queue
» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs.

"""


@app.on_message(
    filters.command(["pause", "skip", "next", "resume", "stop", "end"])
    & filters.group
)
@AdminRightsCheck
@checker
async def admins(_, message: Message):
    global get_queue
    if not len(message.command) == 1:
        return await message.reply_text("**ᴡᴛғ ʙᴀʙʏ !**")
    if not await is_active_chat(message.chat.id):
        return await message.reply_text("**» ᴅɪᴅ ʏᴏᴜ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ᴩʟᴀʏᴇᴅ sᴏᴍᴇᴛʜɪɴɢ ?**")
    chat_id = message.chat.id
    if message.command[0][1] == "a":
        if not await is_music_playing(message.chat.id):
            return await message.reply_text("**» sᴛʀᴇᴀᴍ ᴀʟʀᴇᴀᴅʏ ᴩᴀᴜsᴇᴅ.**")
        await music_off(chat_id)
        await AsuX.pytgcalls.pause_stream(chat_id)
        await message.reply_text(
            f"➻ **sᴛʀᴇᴀᴍ ᴩᴀᴜsᴇᴅ** ☁️\n│ \n└ʙʏ : {message.from_user.first_name} 🥀",
            reply_markup=audio_markup,
        )
    if message.command[0][1] == "e":
        if await is_music_playing(message.chat.id):
            return await message.reply_text("**» ᴅɪᴅ ʏᴏᴜ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ᴩᴀᴜsᴇᴅ sᴏᴍᴇᴛʜɪɴɢ ?**")
        await music_on(chat_id)
        await AsuX.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(
            f"➻ **sᴛʀᴇᴀᴍ ʀᴇsᴜᴍᴇᴅ** ✨\n│ \n└ʙʏ : {message.from_user.first_name} 🥀",
            reply_markup=audio_markup,
        )
    if message.command[0][1] == "t" or message.command[0][1] == "n":
        try:
            Queues.clear(message.chat.id)
        except QueueEmpty:
            pass
        await remove_active_chat(chat_id)
        await AsuX.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text(
            f"➻ **sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ/sᴛᴏᴩᴩᴇᴅ** ❄\n│ \n└ʙʏ : {message.from_user.first_name} 🥀",
            reply_markup=close_key,
        )
    if message.command[0][1] == "k" or message.command[0][2] == "x":
        Queues.task_done(chat_id)
        if Queues.is_empty(chat_id):
            await remove_active_chat(chat_id)
            await message.reply_text(
                f"➻ **sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ** 🥺\n│ \n└ʙʏ : {message.from_user.first_name} 🥀\n\n» ɴᴏ ᴍᴏʀᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ɪɴ {message.chat.title}, **ʟᴇᴀᴠɪɴɢ ᴠɪᴅᴇᴏᴄʜᴀᴛ.**",
                reply_markup=close_key,
            )
            await AsuX.pytgcalls.leave_group_call(message.chat.id)
            return
        else:
            videoid = Queues.get(chat_id)["file"]
            got_queue = get_queue.get(chat_id)
            if got_queue:
                got_queue.pop(0)
            finxx = f"{videoid[0]}{videoid[1]}{videoid[2]}"
            aud = 0
            if str(finxx) != "raw":
                mystic = await message.reply_text(
                    f"**» ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ɴᴇxᴛ ᴛʀᴀᴄᴋ ғʀᴏᴍ ᴩʟᴀʏʟɪsᴛ...**"
                )
                (
                    title,
                    duration_min,
                    duration_sec,
                    thumbnail,
                ) = get_yt_info_id(videoid)
                await mystic.edit(
                    f"**» {BOT_NAME} ᴅᴏᴡɴʟᴏᴀᴅᴇʀ**\n\n**ᴛɪᴛʟᴇ :** {title}\n\n0% ▓▓▓▓▓▓▓▓▓▓▓▓ 100%"
                )
                downloaded_file = await loop.run_in_executor(
                    None, download, videoid, mystic, title
                )
                raw_path = await convert(downloaded_file)
                await AsuX.pytgcalls.change_stream(
                    chat_id,
                    InputStream(
                        InputAudioStream(
                            raw_path,
                        ),
                    ),
                )
                chat_title = message.chat.title
                thumb = await thumb_init(videoid)
                buttons = primary_markup(
                    videoid, message.from_user.id
                )
                await mystic.delete()
                mention = db_mem[videoid]["username"]
                final_output = await message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=(
                        f"<b>➻ sᴛᴀʀᴛᴇᴅ sᴛʀᴇᴀᴍɪɴɢ</b>\n\n<b>✨ ᴛɪᴛʟᴇ :</b> [{title[:40]}](https://www.youtube.com/watch?v={videoid})\n☁ <b>ᴅᴜʀᴀᴛɪᴏɴ :</b> {duration_min} ᴍɪɴᴜᴛᴇs\n🥀 <b>ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :</b> {mention}"
                    ),
                )
                os.remove(thumb)
            else:
                await AsuX.pytgcalls.change_stream(
                    chat_id,
                    InputStream(
                        InputAudioStream(
                            videoid,
                        ),
                    ),
                )
                afk = videoid
                title = db_mem[videoid]["title"]
                duration_min = db_mem[videoid]["duration"]
                duration_sec = int(time_to_seconds(duration_min))
                mention = db_mem[videoid]["username"]
                videoid = db_mem[videoid]["videoid"]
                if str(videoid) == "smex1":
                    buttons = buttons = primary_markup(
                        videoid,
                        message.from_user.id,
                    )
                    thumb = "AsuXMusic/Utilities/Audio.jpeg"
                    aud = 1
                else:
                    _path_ = _path_ = (
                        (str(afk))
                        .replace("_", "", 1)
                        .replace("/", "", 1)
                        .replace(".", "", 1)
                    )
                    thumb = f"AsuXMusic/Cache/{_path_}.png"
                    buttons = primary_markup(
                        videoid,
                        message.from_user.id,
                    )
                final_output = await message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"<b>➻ sᴛᴀʀᴛᴇᴅ sᴛʀᴇᴀᴍɪɴɢ</b>\n\n<b>✨ ᴛɪᴛʟᴇ :</b> {title[:40]}\n☁ <b>ᴅᴜʀᴀᴛɪᴏɴ :</b> {duration_min} ᴍɪɴᴜᴛᴇs\n🥀 <b>ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :</b> {mention}",
                )
