import config

from inspect import getfullargspec
from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputTextMessageContent,
                            Message)

from AsuXMusic import (ASSID, ASSNAME, BOT_ID, BOT_USERNAME, BOT_NAME, SUDO_USERS, app, Ass)
from AsuXMusic.Helpers.Database import (approve_pmpermit, disapprove_pmpermit,
                            is_pmpermit_approved)


__MODULE__ = "Assɪsᴛᴀɴᴛ"
__HELP__ = f"""

**ɴᴏᴛᴇ :**
ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs

{config.ASS_HANDLER[0]}approve [ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ] 
» ᴀᴩᴩʀᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ᴛᴏ ᴩᴍ ᴏɴ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.

{config.ASS_HANDLER[0]}disapprove [ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ] 
» ᴅɪsᴀᴩᴩʀᴏᴠᴇs ᴛʜᴇ ᴜsᴇʀ ᴛᴏ ᴩᴍ ᴏɴ ʏᴏᴜʀ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.

{config.ASS_HANDLER[0]}pfp [ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴩʜᴏᴛᴏ] 
» ᴄʜᴀɴɢᴇs ᴛʜᴇ ᴩғᴩ ᴏғ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜᴜɴᴛ.

{config.ASS_HANDLER[0]}bio [ᴛᴇxᴛ] 
» ᴄʜᴀɴɢᴇs ᴛʜᴇ ʙɪᴏ ᴏғ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
"""

flood = {}


@Ass.on_message(
    filters.private
    & filters.incoming
    & ~filters.service
    & ~filters.edited
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.user(SUDO_USERS)
)
async def awaiting_message(_, message):
    user_id = message.from_user.id
    if await is_pmpermit_approved(user_id):
        return
    async for m in Ass.iter_history(user_id, limit=5):
        if m.reply_markup:
            await m.delete()
    if str(user_id) in flood:
        flood[str(user_id)] += 1
    else:
        flood[str(user_id)] = 1
    if flood[str(user_id)] > 9:
        await message.reply_text("**» sᴩᴀᴍ ᴅᴇᴛᴇᴄᴛᴇᴅ. ʙʟᴏᴄᴋɪɴɢ ᴛʜɪs ᴜsᴇʀ.**")
        await Ass.send_message(
            config.LOGGER_ID,
            f"**sᴩᴀᴍ ᴅᴇᴛᴇᴄᴛᴇᴅ**\n\n» **sᴩᴀᴍᴍᴇʀ :** {message.from_user.mention}\n» **ᴜsᴇʀ ɪᴅ:** {message.from_user.id}",
        )
        return await Ass.block_user(user_id)


@Ass.on_message(
    filters.command("approve", prefixes=config.ASS_HANDLER)
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def pm_approve(_, message):
    if not message.reply_to_message:
        return await eor(
            message, text="» ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴛᴏ ᴀᴩᴩʀᴏᴠᴇ."
        )
    user_id = message.reply_to_message.from_user.id
    if await is_pmpermit_approved(user_id):
        return await eor(message, text="» ᴀʟʀᴇᴀᴅʏ ᴀᴩᴩʀᴏᴠᴇᴅ ᴛᴏ ᴩᴍ.")
    await approve_pmpermit(user_id)
    await eor(message, text="» ᴀᴩᴩʀᴏᴠᴇᴅ ᴛᴏ ᴩᴍ.")


@Ass.on_message(
    filters.command("disapprove", prefixes=config.ASS_HANDLER)
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def pm_disapprove(_, message):
    if not message.reply_to_message:
        return await eor(
            message, text="» ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴛᴏ ᴅɪsᴀᴩᴩʀᴏᴠᴇ."
        )
    user_id = message.reply_to_message.from_user.id
    if not await is_pmpermit_approved(user_id):
        await eor(message, text="» ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀᴩᴩʀᴏᴠᴇᴅ ᴛᴏ ᴩᴍ.")
        async for m in Ass.iter_history(user_id, limit=5):
            if m.reply_markup:
                try:
                    await m.delete()
                except Exception:
                    pass
        return
    await disapprove_pmpermit(user_id)
    await eor(message, text="» ᴅɪsᴀᴩᴩʀᴏᴠᴇᴅ ᴛᴏ ᴩᴍ.")

    
@Ass.on_message(
    filters.command("pfp", prefixes=config.ASS_HANDLER)
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def set_pfp(_, message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await eor(message, text="» ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴩʜᴏᴛᴏ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴀssɪsᴛᴀɴᴛ ᴩғᴩ.")
    photo = await message.reply_to_message.download()
    try: 
        await Ass.set_profile_photo(photo=photo)   
        await eor(message, text="**» sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴩғᴩ ᴏғ ᴀssɪsᴛᴀɴᴛ.**")
    except Exception as e:
        await eor(message, text=e)
    
    
@Ass.on_message(
    filters.command("bio", prefixes=config.ASS_HANDLER)
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def set_bio(_, message):
    if len(message.command) == 1:
        return await eor(message , text="» ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴀssɪsᴛᴀɴᴛ ʙɪᴏ.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try: 
            await Ass.update_profile(bio=bio) 
            await eor(message , text="**» sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ʙɪᴏ ᴏғ ᴀssɪsᴛᴀɴᴛ.**")
        except Exception as e:
            await eor(message , text=e) 
    else:
        return await eor(message , text="» ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ᴀssɪsᴛᴀɴᴛ ʙɪᴏ.")


async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})
