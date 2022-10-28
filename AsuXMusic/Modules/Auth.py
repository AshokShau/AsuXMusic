from pyrogram import Client, filters
from pyrogram.types import Message

from AsuXMusic import app
from AsuXMusic.Cache.admins import AdminActual
from AsuXMusic.Helpers.Changers import int_to_alpha
from AsuXMusic.Helpers.Database import (_get_authusers, delete_authuser, get_authuser,
                            get_authuser_count, get_authuser_names,
                            save_authuser)


__MODULE__ = "Aᴜᴛʜ"
__HELP__ = """

**ɴᴏᴛᴇ :**
• ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴄᴀɴ sᴋɪᴩ, ᴩᴀᴜsᴇ, ʀᴇsᴜᴍᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ᴡɪᴛʜᴏᴜᴛ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.


/auth [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ] 
» ᴀᴅᴅ ᴀ ᴜsᴇʀ ᴛᴏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.

/unauth [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ] 
» ʀᴇᴍᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ.

/authusers 
» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.
"""


@app.on_message(filters.command("auth") & filters.group)
@AdminActual
async def auth(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**» ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ ɪᴅ.**"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        user_id = message.from_user.id
        token = await int_to_alpha(user.id)
        from_user_name = message.from_user.first_name
        from_user_id = message.from_user.id
        _check = await get_authuser_names(message.chat.id)
        count = 0
        for smex in _check:
            count += 1
        if int(count) == 15:
            return await message.reply_text(
                "**» ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴀᴅᴅ 15 ᴜsᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴩ's ᴀᴜᴛʜ ʟɪsᴛ.**"
            )
        if token not in _check:
            assis = {
                "auth_user_id": user.id,
                "auth_name": user.first_name,
                "admin_id": from_user_id,
                "admin_name": from_user_name,
            }
            await save_authuser(message.chat.id, token, assis)
            await message.reply_text(
                f"**» sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴅᴅᴇᴅ {user.first_name} ᴛᴏ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.**"
            )
            return
        else:
            await message.reply_text(f"**» {user.first_name} ɪs ᴀʟʀᴇᴀᴅʏ ɪɴ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ.**")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.first_name
    token = await int_to_alpha(user_id)
    from_user_name = message.from_user.first_name
    _check = await get_authuser_names(message.chat.id)
    count = 0
    for smex in _check:
        count += 1
    if int(count) == 15:
        return await message.reply_text(
            "**» ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴀᴅᴅ 15 ᴜsᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴩ's ᴀᴜᴛʜ ʟɪsᴛ.**"
        )
    if token not in _check:
        assis = {
            "auth_user_id": user_id,
            "auth_name": user_name,
            "admin_id": from_user_id,
            "admin_name": from_user_name,
        }
        await save_authuser(message.chat.id, token, assis)
        await message.reply_text(
            f"**» sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴅᴅᴇᴅ {user_name} ᴛᴏ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.**"
        )
        return
    else:
        await message.reply_text(f"**» {user_name} ɪs ᴀʟʀᴇᴀᴅʏ ɪɴ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ.**")


@app.on_message(filters.command("unauth") & filters.group)
@AdminActual
async def unauth_fe(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**» ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ ɪᴅ.**"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        token = await int_to_alpha(user.id)
        deleted = await delete_authuser(message.chat.id, token)
        if deleted:
            return await message.reply_text(
                f"**» ʀᴇᴍᴏᴠᴇᴅ {user.first_name} ғʀᴏᴍ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.**"
            )
        else:
            return await message.reply_text("**» ɴᴏᴛ ɪɴ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ.**")
    user_id = message.reply_to_message.from_user.id
    token = await int_to_alpha(user_id)
    deleted = await delete_authuser(message.chat.id, token)
    if deleted:
        return await message.reply_text(
            f"**» ʀᴇᴍᴏᴠᴇᴅ {message.reply_to_message.from_user.first_name} ғʀᴏᴍ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴩ.**"
        )
    else:
        return await message.reply_text("**» ɴᴏᴛ ɪɴ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ.**")


@app.on_message(filters.command("authusers") & filters.group)
async def authusers(_, message: Message):
    _playlist = await get_authuser_names(message.chat.id)
    if not _playlist:
        return await message.reply_text(
            "**» ɴᴏ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ғᴏᴜɴᴅ ɪɴ ʏʜɪs ɢʀᴏᴜᴩ.**"
        )
    else:
        j = 0
        m = await message.reply_text(
            "**» ɢᴇᴛᴛɪɴɢ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴜsᴇʀs ʟɪsᴛ ғʀᴏᴍ ᴍᴏɴɢᴏᴅʙ...**"
        )
        msg = "**🥀 ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜsᴇʀs ʟɪsᴛ :**\n\n"
        for note in _playlist:
            _note = await get_authuser(message.chat.id, note)
            user_id = _note["auth_user_id"]
            user_name = _note["auth_name"]
            admin_id = _note["admin_id"]
            admin_name = _note["admin_name"]
            try:
                user = await app.get_users(user_id)
                user = user.first_name
                j += 1
            except Exception:
                continue
            msg += f"{j}➤ {user}[`{user_id}`]\n"
            msg += f"    ┗ ᴀᴅᴅᴇᴅ ʙʏ : {admin_name}[`{admin_id}`]\n\n"
        await m.edit_text(msg)
