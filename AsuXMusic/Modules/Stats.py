import os
import re
import json
import uuid
import time
import psutil
import socket
import logging
import asyncio
import platform

from datetime import datetime
from sys import version as pyver
from pymongo import MongoClient

from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import Message
from AsuXMusic import (BOT_NAME, SUDO_USERS, app, Ass, StartTime, MONGO_DB_URI)
from AsuXMusic.Helpers.Database import get_gbans_count, get_served_chats, get_served_users
from AsuXMusic.Helpers.Inline import stats_f, stats_b
from AsuXMusic.Modules import ALL_MODULES
from AsuXMusic.Helpers.Ping import get_readable_time


__MODULE__ = "Sᴛᴀᴛs"
__HELP__ = """

/stats
» sʜᴏᴡs ᴛʜᴇ sʏsᴛᴇᴍ, ᴀssɪsᴛᴀɴᴛ, ᴍᴏɴɢᴏ ᴀɴᴅ sᴛᴏʀᴀɢᴇ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
"""


@app.on_message(filters.command(["stats", "gstats"]) & ~filters.edited)
async def gstats(_, message):
    try:
        await message.delete()
    except:
        pass
    hehe = await message.reply_photo(
        photo="AsuXMusic/Utilities/Stats.jpeg", caption=f"**» ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...\n\n• ɢᴇᴛᴛɪɴɢ {BOT_NAME} sᴛᴀᴛs...**"
    )
    smex = f"""
**ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ғᴏʀ ɢᴇᴛᴛɪɴɢ {BOT_NAME} ɢᴇɴᴇʀᴀʟ sᴛᴀᴛs ᴏʀ ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs ᴏʀ ᴏᴠᴇʀᴀʟʟ sᴛᴀᴛs.**
    """
    await hehe.edit_text(smex, reply_markup=stats_f)
    return


@app.on_callback_query(
    filters.regex(
        pattern=r"^(sys_stats|bot_stats|get_back|mongo_stats|wait_stats)$"
    )
)
async def stats_markup(_, CallbackQuery):
    command = CallbackQuery.matches[0].group(1)
    if command == "sys_stats":
        await CallbackQuery.answer("ɢᴇᴛᴛɪɴɢ sʏsᴛᴇᴍ sᴛᴀᴛs...")
        mod = len(ALL_MODULES)
        sc = platform.system()
        arch = platform.machine()
        p_core = psutil.cpu_count(logical=False)
        t_core = psutil.cpu_count(logical=True)
        ram = (
            str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " ɢʙ"
        )
        hdd = psutil.disk_usage("/")
        total = hdd.total / (1024.0 ** 3)
        total = str(total)
        used = hdd.used / (1024.0 ** 3)
        used = str(used)
        free = hdd.free / (1024.0 ** 3)
        free = str(free)
        bot_uptime = int(time.time() - StartTime)
        uptime = f"{get_readable_time((bot_uptime))}"
        smex = f"""
➻ <u>**{BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs :**</u>

• **ᴜᴩᴛɪᴍᴇ :** {uptime}
• **ᴍᴏᴅᴜʟᴇs :** {mod}
• **ᴩʟᴀᴛғᴏʀᴍ :** {sc}
• **ᴀʀᴄʜɪᴛᴇᴄᴛᴜʀᴇ:** {arch}
• **ᴩʜʏsɪᴄᴀʟ ᴄᴏʀᴇs :** {p_core}
• **ᴛᴏᴛᴀʟ ᴄᴏʀᴇs :** {t_core}
• **ʀᴀᴍ :** {ram}
• **ᴩʏᴛʜᴏɴ :** v{pyver.split()[0]}
• **ᴩʏʀᴏɢʀᴀᴍ :** v{pyrover}


➻ <u>**{BOT_NAME} sᴛᴏʀᴀɢᴇ sᴛᴀᴛs :**</u>

• **ᴛᴏᴛᴀʟ :** {total[:4]} ɢɪʙ
• **ᴜsᴇᴅ :** {used[:4]} ɢɪʙ
• **ғʀᴇᴇ :** {free[:4]} ɢɪʙ
"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_b)
    if command == "bot_stats":
        await CallbackQuery.answer("ɢᴇᴛᴛɪɴɢ ʙᴏᴛ ᴀɴᴅ ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs...")
        groups_ub = channels_ub = bots_ub = privates_ub = total_ub = 0
        async for i in Ass.iter_dialogs():
            t = i.chat.type
            total_ub += 1
            if t in ["supergroup", "group"]:
                groups_ub += 1
            elif t == "channel":
                channels_ub += 1
            elif t == "bot":
                bots_ub += 1
            elif t == "private":
                privates_ub += 1

        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        blocked = await get_gbans_count()
        sudoers = len(SUDO_USERS)
        mod = len(ALL_MODULES)
        smex = f"""
➻ <u>**{BOT_NAME} ɢᴇɴᴇʀᴀʟ sᴛᴀᴛs :**</u>

• **ᴍᴏᴅᴜʟᴇs :** {mod}
• **ɢʙᴀɴɴᴇᴅ :** {blocked}
• **sᴜᴅᴏᴇʀs :** {sudoers}
• **ᴄʜᴀᴛs :** {served_chats}
• **ᴜsᴇʀs :** {served_users}

➻ <u>**{BOT_NAME} ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs :**</u>

• **ᴛᴏᴛᴀʟ :** {total_ub}
• **ɢʀᴏᴜᴩs :** {groups_ub}
• **ᴄʜᴀɴɴᴇʟs :** {channels_ub}
• **ʙᴏᴛs :** {bots_ub}
• **ᴜsᴇʀs :** {privates_ub}
"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_b)
    if command == "mongo_stats":
        await CallbackQuery.answer(
            "ɢᴇᴛᴛɪɴɢ ᴍᴏɴɢᴏᴅʙ sᴛᴀᴛs..."
        )
        try:
            pymongo = MongoClient(MONGO_DB_URI)
        except Exception as e:
            print(e)
            return await CallbackQuery.edit_message_text("**ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ᴍᴏɴɢᴏᴅʙ sᴛᴀᴛs...**", reply_markup=stats_b)
        try:
            db = pymongo.AsuX
        except Exception as e:
            print(e)
            return await CallbackQuery.edit_message_text("**ғᴀɪʟᴇᴅ ᴛᴏ ɢᴇᴛ ᴍᴏɴɢᴏᴅʙ sᴛᴀᴛs...**", reply_markup=stats_b)
        call = db.command("dbstats")
        database = call["db"]
        datasize = call["dataSize"] / 1024
        datasize = str(datasize)
        storage = call["storageSize"] / 1024
        objects = call["objects"]
        collections = call["collections"]
        status = db.command("serverStatus")
        query = status["opcounters"]["query"]
        mver = status["version"]
        mongouptime = status["uptime"] / 86400
        mongouptime = str(mongouptime)
        provider = status["repl"]["tags"]["provider"]
        smex = f"""
➻ <u>**{BOT_NAME} ᴍᴏɴɢᴏᴅʙ sᴛᴀᴛs :**</u>

**ᴜᴩᴛɪᴍᴇ :** {mongouptime[:4]} ᴅᴀʏs
**ᴠᴇʀsɪᴏɴ :** {mver}
**ᴅᴀᴛᴀʙᴀsᴇ :** {database}
**ᴩʀᴏᴠɪᴅᴇʀ :** {provider}
**ᴅʙ sɪᴢᴇ :** {datasize[:6]} ᴍʙ
**ᴅʙ sᴛᴏʀᴀɢᴇ :** {storage} ᴍʙ
**ᴄᴏʟʟᴇᴄᴛɪᴏɴs :** {collections}
**ᴋᴇʏs :** {objects}
**ǫᴜᴇʀɪᴇs :** `{query}`"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_b)
    if command == "get_back":
        smex = f"**ᴄʜᴏᴏsᴇ ᴀɴ ᴏᴩᴛɪᴏɴ ғᴏʀ ɢᴇᴛᴛɪɴɢ {BOT_NAME} ɢᴇɴᴇʀᴀʟ sᴛᴀᴛs ᴏʀ ᴀssɪsᴛᴀɴᴛ sᴛᴀᴛs ᴏʀ ᴏᴠᴇʀᴀʟʟ sᴛᴀᴛs.**"
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_f)
