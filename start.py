from pyrogram import Client
from AsuXMusic import bot , Abishnoi
from AsuXMusic.config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls, idle



user = PyTgCalls(Abishnoi,
    cache_duration=100,
    overload_quiet_mode=True,)

call_py = PyTgCalls(Abishnoi, overload_quiet_mode=True)

with Client("AsuX", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with Abishnoi as app:
    me_Abishnoi = app.get_me()
