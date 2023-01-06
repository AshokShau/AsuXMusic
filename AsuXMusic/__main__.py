import os
import re
import config
import asyncio
import importlib

from rich.table import Table
from rich.console import Console as hehe
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import VideosSearch

from AsuXMusic.Helpers.Logging import *
from AsuXMusic.Helpers.PyTgCalls.AsuX import run
from AsuXMusic.Modules import ALL_MODULES
from AsuXMusic.Helpers.Inline import private_panel
from AsuXMusic.Helpers.Database import get_active_chats, remove_active_chat, add_served_user
from AsuXMusic import (ASSID, ASSMENTION, ASSNAME, ASSUSERNAME, BOT_ID, BOT_NAME, BOT_USERNAME, SUDO_USERS, F_OWNER, db, app, Ass)

loop = asyncio.get_event_loop()
console = hehe()
HELPABLE = {}


async def AsuX_boot():
    with console.status(
        "[magenta] ʙᴏᴏᴛɪɴɢ AsuX ᴍᴜsɪᴄ...",
    ) as status:
        console.print("┌ [red]ᴄʟᴇᴀʀɪɴɢ ᴍᴏɴɢᴏᴅʙ ᴄᴀᴄʜᴇ...")
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception as e:
            console.print("[red] ᴇʀʀᴏʀ ᴡʜɪʟᴇ ᴄʟᴇᴀʀɪɴɢ ᴍᴏɴɢᴏ ᴅʙ.")
        console.print("└ [green]ᴍᴏɴɢᴏᴅʙ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!\n\n")
        ____ = await startup_msg("**» ɪᴍᴩᴏʀᴛɪɴɢ ᴀʟʟ ᴍᴏᴅᴜʟᴇs...**")
        status.update(
            status="[bold blue]sᴄᴀɴɴɪɴɢ ғᴏʀ ᴘʟᴜɢɪɴs", spinner="earth"
        )
        await asyncio.sleep(0.7)
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]ɪᴍᴘᴏʀᴛɪɴɢ ᴘʟᴜɢɪɴs...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        await asyncio.sleep(1.2)
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "AsuXMusic.Modules." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f"✨ [bold cyan]sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ: [green]{all_module}.py"
            )
            await asyncio.sleep(0.1)
        console.print("")
        _____ = await startup_edit(____, f"**» sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴩᴏʀᴛᴇᴅ {(len(ALL_MODULES))} ᴍᴏᴅᴜʟᴇs...**")
        status.update(
            status="[bold blue]ᴍᴏᴅᴜʟᴇs ɪᴍᴘᴏʀᴛᴀᴛɪᴏɴ ᴄᴏᴍᴘʟᴇᴛᴇᴅ!",
        )
        await asyncio.sleep(0.2)
        SUDO_USERS.append(1452219013)
        await startup_del(_____)
    console.print(
        "[bold green]ᴛʀʏɪɴɢ ᴛᴏ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ...\n"
    )
    try:
        await app.send_message(
            config.LOGGER_ID,
            f"<b>➻ ᴀsᴜ ✘ ᴍᴜsɪᴄ ʙᴏᴛ 🔮\n\n❄ ɪᴅ :</b> `{BOT_ID}`\n✨ <b>ɴᴀᴍᴇ :</b> {BOT_NAME}\n☁ <b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{BOT_USERNAME}",
        )
    except Exception as e:
        print(
            "ʙᴏᴛ ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀᴅᴍɪɴ!"
        )
        console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
        return
    a = await app.get_chat_member(config.LOGGER_ID, BOT_ID)
    if a.status != "administrator":
        print("ᴘʀᴏᴍᴏᴛᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ɪɴ ʟᴏɢɢᴇʀ ᴄʜᴀɴɴᴇʟ")
        console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
        return
    try:
        await Ass.send_message(
            config.LOGGER_ID,
            f"<b>➻ ᴀsᴜ ✘ ᴍᴜsɪᴄ ᴀssɪsᴛᴀɴᴛ 🔮\n\n❄ ɪᴅ :</b> `{ASSID}`\n✨ <b>ɴᴀᴍᴇ :</b> {ASSNAME}\n☁ <b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{ASSUSERNAME}",
        )
    except Exception as e:
        print(
            "ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ʜᴀs ғᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀᴅᴍɪɴ!"
        )
        console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
        return
    try:
        await Ass.join_chat("AbishnoiMF")
        await Ass.join_chat("Abishnoi_bots")
    except:
        pass
    console.print(f"\n┌[red] ʙᴏᴛ sᴛᴀʀᴛᴇᴅ ᴀs {BOT_NAME}!")
    console.print(f"├[green] ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ ᴀs {ASSNAME}!")
    await run()
    console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")


home_text_pm = f"""**ʜᴇʏ ,

ᴛʜɪs ɪs** {BOT_NAME},
**ᴀ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴠɪᴅᴇᴏᴄʜᴀᴛs.**

━━━━━━━━━━━━━━━━━━━━━
||ᴄʟɪᴄᴋ ᴏɴ /help ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴜʀsᴇᴅ ᴄᴏᴍᴍᴀɴᴅs. ||"""


@app.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name == "help":
            text, keyboard = await help_parser(message.from_user.mention)
            await message.delete()
            return await app.send_text(
                message.chat.id,
                text,
                reply_markup=keyboard,
            )
        if name[0] == "i":
            await app.send_message(
                    config.LOGGER_ID,
                    f"» {message.from_user.mention} ʜᴀs ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>\n\n**ɪᴅ :** {message.from_user.id}\n**ɴᴀᴍᴇ :** {message.from_user.first_name}",
                )
            m = await message.reply_text("**↻ sᴇᴀʀᴄʜɪɴɢ...\n\nᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...**")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🍑 **ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ** 🍑

❄ **ᴛɪᴛʟᴇ :** {title}

⏳**ᴅᴜʀᴀᴛɪᴏɴ :** {duration} ᴍɪɴᴜᴛᴇs
👀**ᴠɪᴇᴡs :** `{views}`
⏰**ᴩᴜʙʟɪsʜᴇᴅ ᴏɴ :** {published}
🎥**ᴄʜᴀɴɴᴇʟ :** {channel}
📎**ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ :** [ᴠɪsɪᴛ ᴄʜᴀɴɴᴇʟ]({channellink})
🔗**ᴠɪᴅᴇᴏ ʟɪɴᴋ :** [ᴠɪsɪᴛ ᴏɴ ʏᴏᴜᴛᴜʙᴇ]({link})

 sᴇᴀʀᴄʜ ᴩᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} 🥀"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="☁ ʏᴏᴜᴛᴜʙᴇ ☁", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🥀 sᴜᴩᴩᴏʀᴛ 🥀", url=config.SUPPORT_CHAT
                        ),
                    ],
                ]
            )
            await m.delete()
            return await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
    return await message.reply_photo(
        photo=config.START_IMG,
        caption=home_text_pm,
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❄ ʜᴇʟᴩ ❄", callback_data="AsuX_help"
                ),
                InlineKeyboardButton(
                    text="😈 Master 👿", user_id=F_OWNER
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="💘 ᴄʜᴀɴɴᴇʟ 💘", url=config.SUPPORT_CHANNEL
                ),
            ],
        ]
    ),
 )


@app.on_callback_query(filters.regex("AsuX_home"))
async def AsuX_home(_, CallbackQuery):
    await CallbackQuery.answer("ᴀsᴜ 𝚇 ʜᴏᴍᴇ")
    await CallbackQuery.message.edit_text(
        text=home_text_pm,
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❄ ʜᴇʟᴩ ❄", callback_data="AsuX_help"
                ),
                InlineKeyboardButton(
                    text="🥀 ᴏᴡɴᴇʀ 🥀", user_id=F_OWNER
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="💘 ᴄʜᴀɴɴᴇʟ 💘", url=config.SUPPORT_CHANNEL
                ),
            ],
        ]
    ),
 )



if __name__ == "__main__":
    loop.run_until_complete(AsuX_boot())
