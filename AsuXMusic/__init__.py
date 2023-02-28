from pyrogram import Client
from pytgcalls import PyTgCalls, idle

from AsuXMusic.config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME

bot = Client(
    "AsuXMusic",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="AsuXMusic.Modules"),
)

Abishnoi = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
)

user = PyTgCalls(
    Abishnoi,
    cache_duration=100,
    overload_quiet_mode=True,
)

call_py = PyTgCalls(Abishnoi, overload_quiet_mode=True)

OWNER_NAME = "Abishnoi1M"

with Client("AsuXMusic", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    x = app.get_me()
    BOT_ID = x.id
    BOT_NAME = x.username # perfect 
    BOT_USERNAME = x.username
    BOT_MENTION = x.mention
    BOT_DC_ID = x.dc_id
with Abishnoi as ass:
    getass = ass.get_me()
    ASSISTANT_USERNAME = getass.username
