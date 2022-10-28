import config
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


stats_f = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Gᴇɴᴇʀᴀʟ", callback_data=f"bot_stats"
            )
        ],
        [
            InlineKeyboardButton(
                text="Sʏsᴛᴇᴍ", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="MᴏɴɢᴏDB", callback_data=f"mongo_stats"
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=config.SUPPORT_CHAT
            ),
                        InlineKeyboardButton(
                text="↻ ᴄʟᴏsᴇ ↺", callback_data=f"close"
            )
        ],
    ]
)



stats_b = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="ʙᴀᴄᴋ", callback_data=f"get_back"
            ),
            InlineKeyboardButton(
                text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=config.SUPPORT_CHAT
            )
        ],
    ]
)

