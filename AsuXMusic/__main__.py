import asyncio
import importlib

from pytgcalls import idle

from AsuXMusic import BOT_USERNAME, bot, call_py
from AsuXMusic.Modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def AsuX_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("AsuXMusic.Modules." + all_module)
    print(f"@{BOT_USERNAME} is ready to run ")
    await bot.start()
    print("assistant started ")
    await call_py.start()
    await idle()
    print(f"ɢᴏᴏᴅʙʏᴇ!\nStopping @{BOT_USERNAME}")
    await bot.stop()


if __name__ == "__main__":
    loop.run_until_complete(AsuX_boot())
