import config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ping_ig = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="sᴜᴩᴩᴏʀᴛ",
                    url=config.SUPPORT_CHAT,
                ),
                InlineKeyboardButton(
                    text="sᴏᴜʀᴄᴇ",
                    url="https://github.com/Abishnoi69/AsuXMusic"
                )
            ]
        ]
    )
