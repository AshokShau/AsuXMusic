import asyncio
import importlib

from pytgcalls import idle

from AsuXMusic import BOT_USERNAME, bot, call_py
from AsuXMusic.Modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def AsuX_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("AsuXMusic.Modules." + all_module)
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()
    print(f"GoodBye!\nStopping @{BOT_USERNAME}")


if __name__ == "__main__":
    loop.run_until_complete(AsuX_boot())
