import os
import asyncio

from pyrogram import filters
from pyrogram.types import Message

from AsuXMusic import BOT_NAME, OWNER_ID, app
from AsuXMusic.Helpers.Database import add_off, add_on


__MODULE__ = "Mᴀɪɴᴛᴇɴᴀɴᴄᴇ"
__HELP__ = """

**ɴᴏᴛᴇ :**
ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs.


/maintenance on
» ᴇɴᴀʙʟᴇ ᴛʜᴇ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ᴏғ ᴛʜᴇ ʙᴏᴛ.

/maintenance off
» ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ᴏғ ᴛʜᴇ ʙᴏᴛ.
"""


@app.on_message(filters.command("maintenance") & filters.user(OWNER_ID))
async def maintenance(_, message):
    exp = "**ᴇxᴀᴍᴩʟᴇ :**\n/maintenance [on|off]"
    if len(message.command) != 2:
        return await message.reply_text(exp)
    chat_id = message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "on":
        user_id = 1
        await add_on(user_id)
        await message.reply_text(f"**» {BOT_NAME} ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ᴇɴᴀʙʟᴇ sᴜᴄᴄᴇssғᴜʟʟʏ.**")
    elif state == "off":
        user_id = 1
        await add_off(user_id)
        await message.reply_text(f"**» {BOT_NAME} ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ᴅɪsᴀʙʟᴇᴅ.**")
    else:
        await message.reply_text(exp)
