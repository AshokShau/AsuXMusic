import os
import asyncio
import subprocess

from pyrogram import filters
from pyrogram.types import Message

from AsuXMusic import BOT_NAME, OWNER_ID, SUDO_USERS, app
from AsuXMusic.Helpers.Database import (get_active_chats, get_served_chats, remove_active_chat)


__MODULE__ = "Sᴜᴅᴏ"
__HELP__ = """

/sudolist 
» sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ sᴜᴅᴏᴇʀs.

**ɴᴏᴛᴇ :**
ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs.

/restart 
» ʀᴇsᴛᴀʀᴛs ᴛʜᴇ ʙᴏᴛ ᴏɴ ʏᴏᴜʀ sᴇʀᴠᴇʀ.

/update 
» ғᴇᴛᴄʜ ᴜᴩᴅᴀᴛᴇs ғʀᴏᴍ ᴛʜᴇ ʀᴇᴩᴏ.

/clean
» ᴄʟᴇᴀɴ ᴀʟʟ ᴛʜᴇ ᴛᴇᴍᴩ ᴅɪʀᴇᴄᴛᴏʀɪᴇs.
"""


@app.on_message(filters.command(["sudolist", "listsudo", "sudo", "owner"]))
async def sudoers_list(_, message: Message):
    sudoers = SUDO_USERS
    text = "<u>🥀 **ᴏᴡɴᴇʀ :**</u>\n"
    wtf = 0
    for x in OWNER_ID:
        try:
            user = await app.get_users(x)
            user = user.first_name if not user.mention else user.mention
            wtf += 1
        except Exception:
            continue
        text += f"{wtf}➻ {user}\n"
    smex = 0
    for count, user_id in enumerate(sudoers, 1):
        if user_id not in OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += "\n✨<u> **sᴜᴅᴏᴇʀs :**</u>\n"
                wtf += 1
                text += f"{wtf}➻ {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text("**» ɴᴏ sᴜᴅᴏ ᴜsᴇʀs ғᴏᴜɴᴅ.**")
    else:
        await message.reply_text(text)



## Restart

@app.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def theme_func(_, message):
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        pass
    for x in served_chats:
        try:
            await app.send_message(
                x,
                f"» {BOT_NAME} ᴊᴜsᴛ ʀᴇsᴛᴀʀᴛᴇᴅ ғᴏʀ ғᴇᴛᴄʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ғʀᴏᴍ ᴛʜᴇ sᴇʀᴠᴇʀ.\n\nsᴏʀʀʏ ғᴏʀ ᴛʜᴇ ɪɴᴄᴏɴᴠᴇɴɪᴇɴᴄᴇ.",
            )
            await remove_active_chat(x)
        except Exception:
            pass
    x = await message.reply_text(f"**ʀᴇsᴛᴀʀᴛɪɴɢ {BOT_NAME}\n\nᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...**")
    os.system(f"kill -9 {os.getpid()} && python3 -m AsuXMusic")



## Update

@app.on_message(filters.command("update") & filters.user(SUDO_USERS))
async def update(_, message):
    m = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    if str(m[0]) != "A":
        x = await message.reply_text("**» ғᴇᴛᴄʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ғʀᴏᴍ ʀᴇᴩᴏ ᴀɴᴅ ᴛʀʏɪɴɢ ᴛᴏ ʀᴇsᴛᴀʀᴛ...**")
        return os.system(f"kill -9 {os.getpid()} && python3 -m AsuXMusic")
    else:
        await message.reply_text(f"**» {BOT_NAME} ɪs ᴀʟʀᴇᴀᴅʏ ᴜᴩ-ᴛᴏ-ᴅᴀᴛᴇ !**")



## Broadcast

@app.on_message(filters.command("broadcast") & filters.user(SUDO_USERS))
async def broadcast(_, message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(f"**sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs.**")
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**ᴇxᴀᴍᴩʟᴇ :**\n/broadcast [ᴍᴇssᴀɢᴇ] ᴏʀ [ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"**» sᴜᴄᴄᴇssғᴜʟʟʏ ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴛʜᴇ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs.**")



@app.on_message(filters.command("broadcast_pin") & filters.user(SUDO_USERS))
async def broadcast_message_pin_silent(_, message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=True)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(
            f"**» ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs ᴀɴᴅ ᴩɪɴɴᴇᴅ ɪɴ {pin} ᴄʜᴀᴛs.**"
        )
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**ᴇxᴀᴍᴩʟᴇ :**\n/broadcast [ᴍᴇssᴀɢᴇ] ᴏʀ [ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ]"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)
            try:
                await m.pin(disable_notification=False)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(
        f"**» ʙʀᴏᴀᴅᴄᴀsᴛᴇᴅ ᴍᴇssᴀɢᴇ ɪɴ {sent} ᴄʜᴀᴛs ᴀɴᴅ ᴩɪɴɴᴇᴅ ɪɴ {pin} ᴄʜᴀᴛs.**"
    )


# Clean

@app.on_message(filters.command("clean") & filters.user(SUDO_USERS))
async def clean(_, message):
    dir = "AsuXMusic/Cache"
    ls_dir = os.listdir(dir)
    if ls_dir:
        for dta in os.listdir(dir):
            os.system("rm -rf *.png *.jpg")
        await message.reply_text("**» sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʟᴇᴀɴᴇᴅ ᴀʟʟ ᴛᴇᴍᴩᴏʀᴀʀʏ ᴅɪʀᴇᴄᴛᴏʀɪᴇs !**")
    else:
        await message.reply_text("**» sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʟᴇᴀɴᴇᴅ ᴀʟʟ ᴛᴇᴍᴩᴏʀᴀʀʏ ᴅɪʀᴇᴄᴛᴏʀɪᴇs !**")
