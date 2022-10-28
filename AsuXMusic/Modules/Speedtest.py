import asyncio
import speedtest

from pyrogram import filters
from AsuXMusic import app, SUDO_USERS


__MODULE__ = "SᴩᴇᴇᴅTᴇsᴛ"
__HELP__ = """

/speedtest 
» ᴄʜᴇᴄᴋᴇʀ sᴇʀᴠᴇʀ sᴩᴇᴇᴅ ᴀɴᴅ ʟᴀᴛᴇɴᴄʏ ᴀɴᴅ ᴩɪɴɢ.

"""


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...**")
        test.download()
        m = m.edit("**⇆ ʀᴜɴɴɪɴɢ ᴜᴩʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ sʜᴀʀɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "sptest", "spt"]) & filters.user(SUDO_USERS))
async def speedtest_function(client, message):
    m = await message.reply_text("**» ʀᴜɴɴɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs** ✯
    
<u>**❥͜͡ᴄʟɪᴇɴᴛ :**</u>
**» __ɪsᴩ :__** {result['client']['isp']}
**» __ᴄᴏᴜɴᴛʀʏ :__** {result['client']['country']}
  
<u>**❥͜͡sᴇʀᴠᴇʀ :**</u>
**» __ɴᴀᴍᴇ :__** {result['server']['name']}
**» __ᴄᴏᴜɴᴛʀʏ :__** {result['server']['country']}, {result['server']['cc']}
**» __sᴩᴏɴsᴏʀ :__** {result['server']['sponsor']}
**» __ʟᴀᴛᴇɴᴄʏ :__** {result['server']['latency']}  
**» __ᴩɪɴɢ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
