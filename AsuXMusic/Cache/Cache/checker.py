import config
from AsuXMusic import BOT_USERNAME, app
from AsuXMusic.Helpers.Database import is_gbanned_user, is_on_off


def checker(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "**» ʏᴏᴜ'ʀᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ.\n\n• ʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ғᴏʀ ᴜsɪɴɢ ᴍᴇ.**"
            )
        if await is_on_off(1):
            if int(message.chat.id) != int(LOGGER_ID):
                return await message.reply_text(
                    f"» {BOT_NAME} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ.\n\nɪғ ʏᴏᴜ ᴡᴀɴɴᴀ ᴋɴᴏᴡ ᴛʜᴇ ʀᴇᴀsᴏɴ ʏᴏᴜ ᴄᴀɴ ᴀsᴋ [ʜᴇʀᴇ]({config.SUPPORT_CHAT}) !",
                    disable_web_page_preview=True,
                )
        if await is_gbanned_user(message.from_user.id):
            return await message.reply_text(
                f"**» ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴᴇᴅ ᴜsᴇʀ «**\n\nᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ʀᴇ ɢʙᴀɴɴᴇᴅ ʙʏ ᴍʏ ᴏᴡɴᴇʀ, sᴏ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜsᴇ ᴍᴇ.\n\nᴠɪsɪᴛ : [sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ]({config.SUPPORT_CHAT})",
                 disable_web_page_preview=True,
            )
        return await mystic(_, message)

    return wrapper


def checkerCB(mystic):
    async def wrapper(_, CallbackQuery):
        if await is_on_off(1):
            if int(CallbackQuery.message.chat.id) != int(LOGGER_ID):
                return await CallbackQuery.answer(
                    "» {BOT_NAME} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ.",
                    show_alert=True,
                )
        if await is_gbanned_user(CallbackQuery.from_user.id):
            return await CallbackQuery.answer(
                "» ʙʟᴏᴏᴅʏ ᴍᴏᴛʜᴇʀғᴜ*ᴋᴇʀ\n\nʏᴏᴜ'ʀᴇ ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴᴇᴅ ғʀᴏᴍ ᴛʜɪs ʙᴏᴛ's ᴏᴡɴᴇʀ. sᴏ ᴛʜᴇ ᴏɴʟʏ ᴛʜɪɴɢ ʏᴏᴜ ᴄᴀɴ ᴅᴏ ɪs : ɢᴏ ᴀʜᴇᴀᴅ ᴀɴᴅ ғᴜ*ᴋ ᴏғғ.", show_alert=True
            )
        return await mystic(_, CallbackQuery)

    return wrapper
