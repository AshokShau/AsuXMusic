import re
import os

import lyricsgenius
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch

from AsuXMusic import BOT_NAME, app


__MODULE__ = "Lʏʀɪᴄs"
__HELP__ = """

/lyrics [sᴏɴɢ]
» sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ ʟʏʀɪᴄs ᴏғ ᴛʜᴇ sᴇᴀʀᴄʜᴇᴅ sᴏɴɢ.
"""


@app.on_message(filters.command(["lyrics", "lyric"]))
async def lrsearch(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**ᴇxᴀᴍᴩʟᴇ :**\n\n/lyrics [ᴩᴀʀsʜᴀᴡᴀɴ]")
    m = await message.reply_text("**» sᴇᴀʀᴄʜɪɴɢ...**")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("**» ʟʏʀɪᴄs ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ ᴛʜɪs sᴏɴɢ.**")
    xxx = f"""
**ʟʏʀɪᴄs ᴩᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME}**

**sᴇᴀʀᴄʜᴇᴅ :-** __{query}__
**ᴛɪᴛʟᴇ :-** __{S.title}__
**ᴀʀᴛɪsᴛ :-** {S.artist}

**ʟʏʀɪᴄs :**

{S.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**OUTPUT:**\n\n`Lyrics`",
            quote=False,
        )
        os.remove(filename)
    else:
        await m.edit(xxx)

