import os
import time
import config
import asyncio

from os import listdir, mkdir
from rich.table import Table
from pyrogram import Client
from rich.console import Console as hehe
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as Bot

from AsuXMusic.Helpers.Logging import *
from AsuXMusic.Helpers.Changers import *
from AsuXMusic.Helpers.Clients import app, Ass


loop = asyncio.get_event_loop()
console = hehe()


## Startup Time
StartTime = time.time()

## Clients
app = app
Ass = Ass
aiohttpsession = ClientSession()

## Clients Info
BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""
ASSID = 0
ASSNAME = ""
ASSUSERNAME = ""
ASSMENTION = ""

## Config
OWNER_ID = config.OWNER_ID
F_OWNER = OWNER_ID[0]
LOGGER_ID = config.LOGGER_ID
SUDO_USERS = config.SUDO_USERS
MONGO_DB_URI = config.MONGO_DB_URI
DURATION_LIMIT = config.DURATION_LIMIT
DURATION_LIMIT_SEC = int(time_to_seconds(f"{config.DURATION_LIMIT}:00"))
ASS_HANDLER = config.ASS_HANDLER
PING_IMG = config.PING_IMG
START_IMG = config.START_IMG

## Modules
MOD_LOAD = []
MOD_NOLOAD = []

## MongoDB
MONGODB_CLI = Bot(config.MONGO_DB_URI)
db = MONGODB_CLI.AsuX


async def AsuX_boot():
    global OWNER_ID, SUDO_USERS
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID, ASSNAME, ASSMENTION, ASSUSERNAME
    os.system("clear")
    header = Table(show_header=True, header_style="bold yellow")
    header.add_column(
        "\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2661\u2664\u2661\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n\n\x41\x53\x55\x58\x20\x4d\x55\x53\x49\x43\x20\x20\x49\x53\x20\x53\x54\x41\x52\x54\x49\x4e\x47\x2e\x2e\x2e\x20\x20\x7c\x20\x41\x4e\x20\x41\x42\x47\x20\x50\x52\x4f\x4a\x45\x43\x54\x20\x50\x41\x52\x54\x20\x20\x7c\x20\x4c\x49\x43\x45\x4e\x53\x45\x44\x20\x55\x4e\x44\x45\x52\x20\x47\x50\x4c\x56\x33\x20\x7c\n\n\x50\x52\x4f\x4a\x45\x43\x54\x20\x4d\x41\x49\x4e\x54\x41\x49\x4e\x45\x44\x20\x42\x59\x20\x3a\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x67\x69\x74\x68\x75\x62\x2e\x63\x6f\x6d\x2f\x4b\x69\x6e\x67\x41\x62\x69\x73\x68\x6e\x6f\x69\x20\x28\x74\x2e\x6d\x65\x2f\x41\x62\x69\x73\x68\x6e\x6f\x69\x31\x4d\x20\x29\n\n\xa9\x20\x42\x59\x20\x40\x41\x42\x49\x53\x48\x4e\x4f\x49\x31\x4d\n\xae\x20\x20\x40\x61\x6e\x6f\x6e\x79\x6d\x6f\x75\x73\x5f\x77\x61\x73\x5f\x62\x6f\x74\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2661\u2664\u2661\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501"
    )
    console.print(header)
    with console.status(
        "[magenta] ʙᴏᴏᴛɪɴɢ ᴀsᴜx ᴍᴜsɪᴄ ʙᴏᴛ...",
    ) as status:
        console.print("┌ [red]ʙᴏᴏᴛɪɴɢ ᴀsᴜx ᴍᴜsɪᴄ ᴄʟɪᴇɴᴛs...\n")
        await app.start()
        await Ass.start()
        console.print("└ [green]ᴄʟɪᴇɴᴛs ʙᴏᴏᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ!")
        initial = await startup_msg("**» ʙᴏᴏᴛɪɴɢ ᴀsᴜ 𝚇 ᴍᴜsɪᴄ ʙᴏᴛ...**")
        await asyncio.sleep(0.1)
        all_over = await startup_msg("**» ᴄʜᴇᴄᴋɪɴɢ ᴀɴᴅ ᴄʀᴇᴀᴛɪɴɢ ᴍɪssɪɴɢ ᴅɪʀᴇᴄᴛᴏʀɪᴇs...**")
        console.print(
            "\n┌ [red]ᴄʜᴇᴄᴋɪɴɢ ᴛʜᴇ ᴇxɪsᴛᴇɴᴄᴇ ᴏғ ʀᴇǫᴜɪʀᴇᴅ ᴅɪʀᴇᴄᴛᴏʀɪᴇs..."
        )
        if "raw_files" not in listdir():
            mkdir("raw_files")
        if "downloads" not in listdir():
            mkdir("downloads")
        if "Cache" not in listdir():
            mkdir("Cache")
        console.print("└ [green]ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴜᴘᴅᴀᴛᴇᴅ!")
        await asyncio.sleep(0.1)
        ___ = await startup_edit(all_over, "**» ɢᴇᴛᴛɪɴɢ ᴄʟɪᴇɴᴛs ɪɴғᴏ...**")
        console.print("\n┌ [red]ɢᴇᴛᴛɪɴɢ ᴄʟɪᴇɴᴛs ɪɴғᴏ...")
        getme = await app.get_me()
        getass = await Ass.get_me()
        BOT_ID = getme.id
        ASSID = getass.id
        if getme.last_name:
            BOT_NAME = getme.first_name + " " + getme.last_name
        else:
            BOT_NAME = getme.first_name
        BOT_USERNAME = getme.username
        ASSNAME = (
            f"{getass.first_name} {getass.last_name}"
            if getass.last_name
            else getass.first_name
        )
        ASSUSERNAME = getass.username
        ASSMENTION = getass.mention
        console.print("└ [green]sᴜᴄᴄᴇssғᴜʟʟʏ ʟᴏᴀᴅᴇᴅ ᴄʟɪᴇɴᴛs ɪɴғᴏʀᴍᴀᴛɪᴏɴ !")
        await asyncio.sleep(0.1)
        ____ok = await startup_edit(___, "**» ʟᴏᴀᴅɪɴɢ sᴜᴅᴏ ᴜsᴇʀs...**")
        console.print("\n┌ [red]ʟᴏᴀᴅɪɴɢ sᴜᴅᴏ ᴜsᴇʀs...")
        SUDO_USERS = (SUDO_USERS + OWNER_ID)
        await asyncio.sleep(1)
        console.print("└ [green]ʟᴏᴀᴅᴇᴅ sᴜᴅᴏ ᴜsᴇʀs sᴜᴄᴄᴇssғᴜʟʟʏ!\n")
        await startup_del(____ok)
        await startup_del(initial)


loop.run_until_complete(AsuX_boot())


def init_db():
    global db_mem
    db_mem = {}


init_db()
