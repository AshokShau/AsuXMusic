import asyncio
from AsuXMusic import BOT_UEERNAME, bot as Abishnoi
from AsuXMusic.config import SUDO_USERS
from AsuX import authorized_users_only, sudo_users_only, errors
from AsuX.filters import command, other_filters
from AsuXMusic import user as USER
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant


@Abishnoi.on_message(
    command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot
)
@authorized_users_only
@errors
async def join_group(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except BaseException:
        await message.reply_text(
            "• **I ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ:**\n\n» ❌ __ᴀᴅᴅ ᴜsᴇʀs__",
        )
        return

    try:
        user = await USER.get_me()
    except BaseException:
        user.first_name = "ᴍᴜsɪᴄ ᴀssɪsᴛᴀɴᴛ"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"🛑 ғʟᴏᴏᴅ ᴡᴀɪᴛ ᴇʀʀᴏʀ 🛑 \n\n**ᴜsᴇʀʙᴏᴛ ᴄᴏᴜʟᴅɴ'ᴛ ᴊᴏɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴅᴜᴇ ᴛᴏ ʜᴇᴀᴠʏ ᴊᴏɪɴ ʀᴇǫᴜᴇsᴛs ғᴏʀ ᴜsᴇʀʙᴏᴛ**"
            "\n\n**ᴏʀ ᴀᴅᴅ ᴀssɪsᴛᴀɴᴛ ᴍᴀɴᴜᴀʟʟʏ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ**",
        )
        return
    await message.reply_text(
        f"**Userbot Succesfully Entered Chat**",
    )


@Abishnoi.on_message(command(["userbotleave",
                            f"leave@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def leave_one(client, message):
    try:
        await USER.send_message(message.chat.id, "✅ ᴜsᴇʀʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴇғᴛ ᴄʜᴀᴛ")
        await USER.leave_chat(message.chat.id)
    except BaseException:
        await message.reply_text(
            "❌ **ᴜsᴇʀʙᴏᴛ ᴄᴏᴜʟᴅɴ'ᴛ ʟᴇᴀᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ᴍᴀʏ ʙᴇ ғʟᴏᴏᴅᴡᴀɪᴛs.**\n\n**» ᴏʀ ᴍᴀɴᴜᴀʟʟʏ ᴋɪᴄᴋ ᴜsᴇʀʙᴏᴛ ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘ**"
        )

        return


