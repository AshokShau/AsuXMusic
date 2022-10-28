import os
import asyncio
import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery
from asyncio import QueueEmpty
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream, InputStream

from config import get_queue
from AsuXMusic.Cache.checker import checkerCB
from AsuXMusic.Cache.admins import AdminRightsCheck, AdminRightsCheckCB
from AsuXMusic.Helpers.Thumbnails import thumb_init
from AsuXMusic.Helpers.Ytinfo import get_yt_info_id
from AsuXMusic.Helpers.PyTgCalls import Queues, AsuX
from AsuXMusic.Helpers.Changers import time_to_seconds
from AsuXMusic.Helpers.PyTgCalls.Converter import convert
from AsuXMusic.Helpers.PyTgCalls.Downloader import download
from AsuXMusic import BOT_USERNAME, BOT_NAME, app, db_mem
from AsuXMusic.Helpers.Inline import (audio_markup, primary_markup, close_key)
from AsuXMusic.Helpers.Database import (add_active_chat, is_active_chat, remove_active_chat, is_music_playing, music_off, music_on)


loop = asyncio.get_event_loop()


@app.on_callback_query(
    filters.regex(pattern=r"^(pausecb|skipcb|stopcb|resumecb)$")
)
@AdminRightsCheckCB
@checkerCB
async def admin_risghts(_, CallbackQuery):
    global get_queue
    command = CallbackQuery.matches[0].group(1)
    if not await is_active_chat(CallbackQuery.message.chat.id):
        return await CallbackQuery.answer(
            "» ᴅɪᴅ ʏᴏᴜ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ᴩʟᴀʏᴇᴅ sᴏᴍᴇᴛʜɪɴɢ ?", show_alert=True
        )
    chat_id = CallbackQuery.message.chat.id
    if command == "pausecb":
        if not await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                "» sᴛʀᴇᴀᴍ ᴀʟʀᴇᴀᴅʏ ᴩᴀᴜsᴇᴅ.", show_alert=True
            )
        await music_off(chat_id)
        await AsuX.pytgcalls.pause_stream(chat_id)
        await CallbackQuery.message.reply_text(
            f"➻ **sᴛʀᴇᴀᴍ ᴩᴀᴜsᴇᴅ** ☁️\n│ \n└ʙʏ : {CallbackQuery.from_user.first_name} 🥀",
            reply_markup=audio_markup,
        )
        await CallbackQuery.answer("» sᴛʀᴇᴀᴍ ᴩᴀᴜsᴇᴅ.")
    if command == "resumecb":
        if await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                "» ᴅɪᴅ ʏᴏᴜ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ'ᴠᴇ ᴩᴀᴜsᴇᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ?", show_alert=True
            )
        await music_on(chat_id)
        await AsuX.pytgcalls.resume_stream(chat_id)
        await CallbackQuery.message.reply_text(
            f"➻ **sᴛʀᴇᴀᴍ ʀᴇsᴜᴍᴇᴅ** ✨\n│ \n└ʙʏ : {CallbackQuery.from_user.first_name} 🥀",
            reply_markup=audio_markup,
        )
        await CallbackQuery.answer("» sᴛʀᴇᴀᴍ ʀᴇsᴜᴍᴇᴅ.")
    if command == "stopcb":
        try:
            Queues.clear(chat_id)
        except QueueEmpty:
            pass
        await remove_active_chat(chat_id)
        await AsuX.pytgcalls.leave_group_call(chat_id)
        await CallbackQuery.message.reply_text(
            f"➻ **sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ/sᴛᴏᴩᴩᴇᴅ** ❄\n│ \n└ʙʏ : {CallbackQuery.from_user.first_name} 🥀",
            reply_markup=close_key,
        )
        await CallbackQuery.message.delete()
        await CallbackQuery.answer("» sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ.")
    if command == "skipcb":
        Queues.task_done(chat_id)
        if Queues.is_empty(chat_id):
            await remove_active_chat(chat_id)
            await CallbackQuery.message.reply_text(
                f"➻ **sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ** 🥺\n│ \n└ʙʏ : {CallbackQuery.from_user.first_name} 🥀\n\n» ɴᴏ ᴍᴏʀᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ɪɴ {CallbackQuery.message.chat.title}, **ʟᴇᴀᴠɪɴɢ ᴠɪᴅᴇᴏᴄʜᴀᴛ.**",
              reply_markup=close_key,
            )
            await AsuX.pytgcalls.leave_group_call(chat_id)
            await CallbackQuery.message.delete()
            await CallbackQuery.answer(
                "» sᴋɪᴩᴩᴇᴅ, ɴᴏ ᴍᴏʀᴇ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ."
            )
            return
        else:
            videoid = Queues.get(chat_id)["file"]
            got_queue = get_queue.get(CallbackQuery.message.chat.id)
            if got_queue:
                got_queue.pop(0)
            finxx = f"{videoid[0]}{videoid[1]}{videoid[2]}"
            aud = 0
            if str(finxx) != "raw":
                await CallbackQuery.message.delete()
                await CallbackQuery.answer(
                    "sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ..."
                )
                mystic = await CallbackQuery.message.reply_text(
                    f"**ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ɴᴇxᴛ ᴛʀᴀᴄᴋ ғʀᴏᴍ ᴩʟᴀʏʟɪsᴛ...\n\nsᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ ʙʏ  {CallbackQuery.from_user.mention} !**🥀"
                )
                (
                    title,
                    duration_min,
                    duration_sec,
                    thumbnail,
                ) = get_yt_info_id(videoid)
                await mystic.edit(
                    f"**{BOT_NAME} ᴅᴏᴡɴʟᴏᴀᴅᴇʀ**\n\n**ᴛɪᴛʟᴇ :** {title[:40]}\n\n0% ■■■■■■■■■■■■ 100%"
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
                chat_title = CallbackQuery.message.chat.title
                thumb = await thumb_init(videoid)
                buttons = primary_markup(
                    videoid,
                    CallbackQuery.from_user.id
                )
                await mystic.delete()
                mention = db_mem[videoid]["username"]
                final_output = await CallbackQuery.message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=(
                        f"<b>➻ sᴛᴀʀᴛᴇᴅ sᴛʀᴇᴀᴍɪɴɢ</b>\n\n<b>✨ ᴛɪᴛʟᴇ :</b> [{title[:40]}](https://www.youtube.com/watch?v={videoid})\n☁ <b>ᴅᴜʀᴀᴛɪᴏɴ :</b> {duration_min} ᴍɪɴᴜᴛᴇs\n🥀 <b>ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :</b> {mention}"
                    ),
                )
                os.remove(thumb)

            else:
                await CallbackQuery.message.delete()
                await CallbackQuery.answer("sᴛʀᴇᴀᴍ sᴋɪᴩᴩᴇᴅ...")
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
                    buttons = primary_markup(
                        videoid,
                        CallbackQuery.from_user.id,
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
                    thumb = f"AsuXMusic/Cache/{_path_}final.png"
                    buttons = primary_markup(
                        videoid,
                        CallbackQuery.from_user.id,
                    )
                final_output = await CallbackQuery.message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"<b>➻ sᴛᴀʀᴛᴇᴅ sᴛʀᴇᴀᴍɪɴɢ</b>\n\n<b>✨ ᴛɪᴛʟᴇ :</b> {title[:40]}\n☁ <b>ᴅᴜʀᴀᴛɪᴏɴ :</b> {duration_min} ᴍɪɴᴜᴛᴇs\n🥀 <b>ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :</b> {mention}",
                )


@app.on_callback_query(filters.regex("close"))
async def closed(_, query: CallbackQuery):
    await query.message.delete()
    await query.answer()

