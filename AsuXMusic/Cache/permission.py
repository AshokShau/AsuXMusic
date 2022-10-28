from typing import Dict, List, Union

from AsuXMusic import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "» ᴩʟᴇᴀsᴇ ɢɪᴠᴇ ᴍᴇ ʙᴇʟᴏᴡ ᴩᴇʀᴍɪssɪᴏɴs :\n\n"
                + "\n• **ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs**"
                + "\n• **ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs**"
                + "\n• **ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ.**"
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "» ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴩᴇʀᴍɪssɪᴏɴs ᴛᴏ :"
                + "\n\n**ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs.**"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "» ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴩᴇʀᴍɪssɪᴏɴs ᴛᴏ :"
                + "\n\n**ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs.**"
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "» ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴩᴇʀᴍɪssɪᴏɴs ᴛᴏ :"
                + "\n\n**ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ.**"
            )
            return
        return await mystic(_, message)

    return wrapper
