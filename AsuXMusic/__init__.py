import logging

from pyrogram import Client
from pytgcalls import PyTgCalls, idle

from AsuXMusic.config import API_HASH, API_ID, BOT_TOKEN, OWNER_ID, SESSION_NAME
from AsuXMusic.Modules import ALL_MODULES

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)


bot = Client(
    "AsuXMusic",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
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
F_OWNER = OWNER_ID[0]

with Client("AsuXMusic", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    x = app.get_me()
    BOT_ID = x.id
    BOT_NAME = x.first_name + (x.last_name or "")
    BOT_USERNAME = x.username
    BOT_MENTION = x.mention
    BOT_DC_ID = x.dc_id
with Abishnoi as ass:
    getass = ass.get_me()
    ASSISTANT_USERNAME = getass.username
