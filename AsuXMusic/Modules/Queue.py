import os
import asyncio

from config import get_queue
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, CallbackQuery

from AsuXMusic import app, db_mem
from AsuXMusic.Helpers.Database import is_active_chat
from AsuXMusic.Helpers.Inline import primary_markup


__MODULE__ = "Qᴜᴇᴜᴇ"
__HELP__ = """
 
/queue
» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ɪɴ ᴛʜᴇ ǫᴜᴇᴜᴇ.

"""


@app.on_callback_query(filters.regex("pr_go_back_timer"))
async def pr_go_back_timer(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, user_id = callback_request.split("|")
    if await is_active_chat(CallbackQuery.message.chat.id):
        if db_mem[CallbackQuery.message.chat.id]["videoid"] == videoid:
            dur_left = db_mem[CallbackQuery.message.chat.id]["left"]
            duration_min = db_mem[CallbackQuery.message.chat.id]["total"]
            buttons = primary_markup(videoid, user_id)
            await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
   

@app.on_callback_query(filters.regex("timer_checkup_markup"))
async def timer_checkup_markup(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, user_id = callback_request.split("|")
    if await is_active_chat(CallbackQuery.message.chat.id):
        if db_mem[CallbackQuery.message.chat.id]["videoid"] == videoid:
            dur_left = db_mem[CallbackQuery.message.chat.id]["left"]
            duration_min = db_mem[CallbackQuery.message.chat.id]["total"]
            return await CallbackQuery.answer(
                f"ʀᴇᴍᴀɪɴɪɴɢ {dur_left} ᴏᴜᴛ ᴏғ {duration_min} ᴍɪɴᴜᴛᴇs.",
                show_alert=True,
            )
        return await CallbackQuery.answer(f"ɴᴏᴛʜɪɴɢ ɪs ᴩʟᴀʏɪɴɢ...", show_alert=True)
    else:
        return await CallbackQuery.answer(
            f"ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ ғᴏᴜɴᴅ.", show_alert=True
        )


@app.on_message(filters.command("queue"))
async def activevc(_, message: Message):
    global get_queue
    if await is_active_chat(message.chat.id):
        mystic = await message.reply_text("**» ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ, ɢᴇᴛᴛɪɴɢ ǫᴜᴇᴜᴇ...**")
        dur_left = db_mem[message.chat.id]["left"]
        duration_min = db_mem[message.chat.id]["total"]
        got_queue = get_queue.get(message.chat.id)
        if not got_queue:
            await mystic.edit("**» ǫᴜᴇᴜᴇ ᴇᴍᴩᴛʏ.**")
        fetched = []
        for get in got_queue:
            fetched.append(get)

        current_playing = fetched[0][0]
        user_name = fetched[0][1]

        msg = "**ǫᴜᴇᴜᴇᴅ ʟɪsᴛ**\n\n"
        msg += "**ᴩʟᴀʏɪɴɢ :**"
        msg += "\n‣" + current_playing[:30]
        msg += f"\n   ╚ ʙʏ : {user_name}"
        msg += f"\n   ╚ ᴅᴜʀᴀᴛɪᴏɴ : ʀᴇᴍᴀɪɴɪɴɢ `{dur_left}` ᴏᴜᴛ ᴏғ `{duration_min}` ᴍɪɴᴜᴛᴇs."
        fetched.pop(0)
        if fetched:
            msg += "\n\n"
            msg += "**ɴᴇxᴛ ɪɴ ǫᴜᴇᴜᴇ :**"
            for song in fetched:
                name = song[0][:30]
                usr = song[1]
                dur = song[2]
                msg += f"\n❚❚ {name}"
                msg += f"\n   ╠ ᴅᴜʀᴀᴛɪᴏɴ : {dur}"
                msg += f"\n   ╚ ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ : {usr}\n"
        if len(msg) > 4096:
            await mystic.delete()
            filename = "queue.txt"
            with open(filename, "w+", encoding="utf8") as out_file:
                out_file.write(str(msg.strip()))
            await message.reply_document(
                document=filename,
                caption="**ǫᴜᴇᴜᴇᴅ ʟɪsᴛ**",
                quote=False,
            )
            os.remove(filename)
        else:
            await mystic.edit(msg)
    else:
        await message.reply_text(f"**» ǫᴜᴇᴜᴇ ᴇᴍᴩᴛʏ.**")

