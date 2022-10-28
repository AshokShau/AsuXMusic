import config

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery, Message

from AsuXMusic import app, SUDO_USERS
from AsuXMusic.Helpers import Help
from AsuXMusic.Helpers.Inline import help_panel, help_markup



@app.on_callback_query(filters.regex("AsuX_help"))
async def help_menu(_, CallbackQuery):
    await CallbackQuery.message.edit(
       text=f"""ʜᴇʏ {CallbackQuery.from_user.first_name},

ᴀʟʟ ᴏғ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴀʀᴇ ʟɪsᴛᴇᴅ ɪɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ, ʏᴏᴜ ᴄᴀɴ ᴏᴩᴇɴ ᴛʜᴇᴍ ᴀɴᴅ ɢᴇᴛ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.

ᴀʟʟ ᴏғ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : `/`
""",
       reply_markup=help_panel)


@app.on_callback_query(filters.regex("help_callback"))
async def helper_cb(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    if cb == "ADMIN":
        await CallbackQuery.edit_message_text(
            Help.ADMIN, reply_markup=help_markup
        )
    elif cb == "AUTH":
        await CallbackQuery.edit_message_text(
            Help.AUTH, reply_markup=help_markup
        )
    elif cb == "PLAY":
        await CallbackQuery.edit_message_text(
            Help.PLAY, reply_markup=help_markup
        )
    elif cb == "OWNER":
        await CallbackQuery.edit_message_text(
            Help.OWNER, reply_markup=help_markup
        )
    elif cb == "SUDO":
        await CallbackQuery.edit_message_text(
            Help.SUDO, reply_markup=help_markup
        )
    elif cb == "TOOLS":
        await CallbackQuery.edit_message_text(
            Help.TOOLS, reply_markup=help_markup
        )
