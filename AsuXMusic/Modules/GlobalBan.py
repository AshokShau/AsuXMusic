import os
import config
import asyncio

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from AsuXMusic import BOT_ID, BOT_NAME, SUDO_USERS, app
from AsuXMusic.Helpers.Database import (add_gban_user, get_served_chats, is_gbanned_user, remove_gban_user)


__MODULE__ = "Gʟᴏʙᴀʟ Bᴀɴ"
__HELP__ = """

**ɴᴏᴛᴇ :**
ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs.

/gban [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ]
» ɢʟᴏʙᴀʟʟʏ ʙᴀɴs ᴀ ᴜsᴇʀ ɪɴ ᴀʟʟ ᴛʜᴇ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs.

/ungban [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ]
» ɢʟᴏʙᴀʟʟʏ ᴜɴʙᴀɴs ᴛʜᴇ ɢ-ʙᴀɴɴᴇᴅ ᴜsᴇʀ.
"""


@app.on_message(filters.command("gban") & filters.user(SUDO_USERS))
async def ban_globally(_, message):
    if not message.reply_to_message:
        if len(message.command) < 2:
            await message.reply_text("**ᴇxᴀᴍᴩʟᴇ :**\n/gban [ᴜsᴇʀɴᴀᴍᴇ|ᴜsᴇʀ ɪᴅ]")
            return
        user = message.text.split(None, 2)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        from_user = message.from_user
        if user.id == from_user.id:
            return await message.reply_text(
                "**» ʏᴏᴜ ᴄᴀɴ'ᴛ ɢʙᴀɴ ʏᴏᴜʀsᴇʟғ ʙᴀʙʏ !**"
            )
        elif user.id == BOT_ID:
            await message.reply_text("» ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ɢʙᴀɴ ᴍʏsᴇʟғ, ʙʟᴏᴏᴅʏ ɴᴏᴏʙs !")
        elif user.id in SUDO_USERS:
            await message.reply_text("» ʏᴏᴜ ʙʟᴏᴏᴅʏ ᴍᴏᴛʜᴇʀғᴜ*ᴋᴇʀ, ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ɢʙᴀɴ ᴍʏ ʙᴀʙʏ, ɪ ᴡɪʟʟ ғᴜ*ᴋ ʏᴏᴜ ʜᴀʀᴅ ᴀɴᴅ ʏᴏᴜ ᴡɪʟʟ ɴᴏᴛ ʙᴇ ᴀʙʟᴇ ᴛᴏ ғᴜ*ᴋ ᴀɴʏᴏɴᴇ ᴀɢᴀɪɴ !")
        else:
            await add_gban_user(user.id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"**ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴɪɴɢ {user.mention}**\n\nᴇxᴩᴇᴄᴛᴇᴅ ᴛɪᴍᴇ : {len(served_chats)}"
            )
            number_of_chats = 0
            for sex in served_chats:
                try:
                    await app.kick_chat_member(sex, user.id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
**ɢʟᴏʙᴀʟ ʙᴀɴ ᴏɴ {BOT_NAME}**

**• ᴄʜᴀᴛ :** {message.chat.title} [`{message.chat.id}`]
**• sᴜᴅᴏᴇʀ :** {from_user.mention}
**• ᴜsᴇʀ :** {user.mention}
**• ᴜsᴇʀ ɪᴅ:** `{user.id}`
**• ʙᴀɴɴᴇᴅ ɪɴ :** {number_of_chats} ᴄʜᴀᴛs"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
        return
    from_user_id = message.from_user.id
    from_user_mention = message.from_user.mention
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    if user_id == from_user_id:
        await message.reply_text("» ʏᴏᴜ ᴄᴀɴ'ᴛ ɢʙᴀɴ ʏᴏᴜʀsᴇʟғ ʙᴀʙʏ !")
    elif user_id == BOT_ID:
        await message.reply_text("» ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ɢʙᴀɴ ᴍʏsᴇʟғ, ʙʟᴏᴏᴅʏ ɴᴏᴏʙs !")
    elif user_id in SUDO_USERS:
        await message.reply_text("» ʏᴏᴜ ʙʟᴏᴏᴅʏ ᴍᴏᴛʜᴇʀғᴜ*ᴋᴇʀ, ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ɢʙᴀɴ ᴍʏ ʙᴀʙʏ, ɪ ᴡɪʟʟ ғᴜ*ᴋ ʏᴏᴜ ʜᴀʀᴅ ᴀɴᴅ ʏᴏᴜ ᴡɪʟʟ ɴᴏᴛ ʙᴇ ᴀʙʟᴇ ᴛᴏ ғᴜ*ᴋ ᴀɴʏᴏɴᴇ ᴀɢᴀɪɴ !")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if is_gbanned:
            await message.reply_text("**ᴀʟʀᴇᴀᴅʏ ɢʙᴀɴɴᴇᴅ ᴛʜᴀᴛ ᴍᴏᴛʜᴇʀғᴜ*ᴋᴇʀ.**")
        else:
            await add_gban_user(user_id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"**ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴɪɴɢ {mention}**\n\nᴇxᴩᴇᴄᴛᴇᴅ ᴛɪᴍᴇ : {len(served_chats)}"
            )
            number_of_chats = 0
            for sex in served_chats:
                try:
                    await app.kick_chat_member(sex, user_id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
**ɢʟᴏʙᴀʟ ʙᴀɴ ᴏɴ {BOT_NAME}**

**• ᴄʜᴀᴛ :** {message.chat.title} [`{message.chat.id}`]
**• sᴜᴅᴏᴇʀ :** {from_user_mention}
**• ᴜsᴇʀ :** {mention}
**• ᴜsᴇʀ ɪᴅ:** `{user_id}`
**• ʙᴀɴɴᴇᴅ ɪɴ :** {number_of_chats} ᴄʜᴀᴛs"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
            return


@app.on_message(filters.command("ungban") & filters.user(SUDO_USERS))
async def unban_globally(_, message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**ᴇxᴀᴍᴩʟᴇ :**\n/ungban [ᴜsᴇʀɴᴀᴍᴇ|ᴜsᴇʀ ɪᴅ]"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        from_user = message.from_user
        if user.id == from_user.id:
            await message.reply_text("» ɪ ᴀʟʀᴇᴀᴅʏ ᴛᴏʟᴅ ʏᴏᴜ ᴛʜᴀᴛ ʏᴏᴜ ᴄᴀɴ'ᴛ ɢʙᴀɴ ʏᴏᴜʀsᴇʟғ sᴏ ʜᴏᴡ ᴛʜᴇ ғᴜ*ᴋ ʏᴏᴜ'ʀᴇ ᴛʀʏɪɴɢ ᴛᴏ ᴜɴɢʙᴀɴ ʏᴏᴜʀsᴇʟғ !")
        elif user.id == BOT_ID:
            await message.reply_text("» ʏᴏᴜ ʙʟᴏᴏᴅʏ ɴᴏᴏʙ, ɪ ᴀᴍ ᴛᴇʟʟɪɴɢ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴄᴏᴍᴇ ʙᴀᴄᴋ ᴀɢᴀɪɴ ᴇʟsᴇ ɪ ᴡɪʟʟ ᴛᴇʟʟ ᴍʏ ʙᴀʙʏ ᴛᴏ ғᴜ*ᴋ ʏᴏᴜ ᴜᴩ !")
        elif user.id in SUDO_USERS:
            await message.reply_text("» ʀᴇᴀᴅ ᴛʜɪs sᴛᴀᴛᴇᴍᴇɴᴛ ʟᴀsᴛ ᴛɪᴍᴇ, ɪ'ᴍ ɴᴏᴛ ɢᴏɴɴᴀ ᴛᴇʟʟ ʏᴏᴜ ᴀɢᴀɪɴ-ɴ-ᴀɢᴀɪɴ ᴛʜᴀᴛ ʏᴏᴜ ᴄᴀɴ'ᴛ ɢʙᴀɴ ᴍʏ ʙᴀʙʏ !")
        else:
            is_gbanned = await is_gbanned_user(user.id)
            if not is_gbanned:
                await message.reply_text("» ᴛʜɪs ᴜsᴇʀ ɪs ɴᴏᴛ ɢʙᴀɴɴᴇᴅ !")
            else:
                await remove_gban_user(user.id)
                await message.reply_text(f"» ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ɢʙᴀɴɴᴇᴅ ᴜsᴇʀs ʟɪsᴛ...")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    if user_id == from_user_id:
        await message.reply_text("» ɪ ᴀʟʀᴇᴀᴅʏ ᴛᴏʟᴅ ʏᴏᴜ ᴛʜᴀᴛ ʏᴏᴜ ᴄᴀɴ'ᴛ ɢʙᴀɴ ʏᴏᴜʀsᴇʟғ sᴏ ʜᴏᴡ ᴛʜᴇ ғᴜ*ᴋ ʏᴏᴜ'ʀᴇ ᴛʀʏɪɴɢ ᴛᴏ ᴜɴɢʙᴀɴ ʏᴏᴜʀsᴇʟғ !")
    elif user_id == BOT_ID:
        await message.reply_text(
            "» ʏᴏᴜ ʙʟᴏᴏᴅʏ ɴᴏᴏʙ, ɪ ᴀᴍ ᴛᴇʟʟɪɴɢ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴄᴏᴍᴇ ʙᴀᴄᴋ ᴀɢᴀɪɴ ᴇʟsᴇ ɪ ᴡɪʟʟ ᴛᴇʟʟ ᴍʏ ʙᴀʙʏ ᴛᴏ ғᴜ*ᴋ ʏᴏᴜ ᴜᴩ !"
        )
    elif user_id in SUDO_USERS:
        await message.reply_text("» ʀᴇᴀᴅ ᴛʜɪs sᴛᴀᴛᴇᴍᴇɴᴛ ʟᴀsᴛ ᴛɪᴍᴇ, ɪ'ᴍ ɴᴏᴛ ɢᴏɴɴᴀ ᴛᴇʟʟ ʏᴏᴜ ᴀɢᴀɪɴ-ɴ-ᴀɢᴀɪɴ ᴛʜᴀᴛ ʏᴏᴜ ᴄᴀɴ'ᴛ ɢʙᴀɴ ᴍʏ ʙᴀʙʏ !")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if not is_gbanned:
            await message.reply_text("» ᴛʜɪs ᴜsᴇʀ ɪs ɴᴏᴛ ɢʙᴀɴɴᴇᴅ !")
        else:
            await remove_gban_user(user_id)
            await message.reply_text(f"» ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ ɢʙᴀɴɴᴇᴅ ᴜsᴇʀs ʟɪsᴛ...")



chat_watcher_group = 5

@app.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message):
    try:
        userid = message.from_user.id
    except Exception:
        return
    checking = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_gbanned_user(userid):
        try:
            await message.chat.kick_member(userid)
        except Exception:
            return
        await message.reply_text(
            f"{checking} ɪs ɢʟᴏʙᴀʟʟʏ ʙᴀɴɴᴇᴅ ᴏɴ {BOT_NAME}\n\n**ʀᴇᴀsᴏɴ :** ʙʜᴀᴅᴠᴀ sᴀᴀʟᴀ, ʀᴀɴᴅɪʙᴀᴀᴢ, ʙᴇʜᴇɴ ᴋᴀ ʟᴏᴅᴀ."
        )
