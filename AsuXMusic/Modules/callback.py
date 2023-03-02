import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from youtubesearchpython import VideosSearch

from AsuX.inline import menu_markup, song_download_markup, stream_markup
from AsuX.queues import QUEUE
from AsuXMusic import BOT_NAME, BOT_USERNAME, F_OWNER
from AsuXMusic import bot as Client
from AsuXMusic.config import GROUP_SUPPORT, UPDATES_CHANNEL


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0


@Client.on_inline_query()
async def inline(client: Client, query: InlineQuery):
    answerss = [
        InlineQueryResultArticle(
            title="ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ",
            description=f"ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://te.legra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ",
            description=f"ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://te.legra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="ᴍᴜᴛᴇ sᴛʀᴇᴀᴍ",
            description=f"ᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://te.legra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="ᴜɴᴍᴜᴛᴇ sᴛʀᴇᴀᴍ",
            description=f"ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://te.legra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="sᴋɪᴘ sᴛʀᴇᴀᴍ",
            description=f"sᴋɪᴘ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ. | ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴛʀᴀᴄᴋ ɴᴜᴍʙᴇʀ: /skip [ɴᴜᴍʙᴇʀ] ",
            thumb_url="https://te.legra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="ᴇɴᴅ sᴛʀᴇᴀᴍ",
            description="sᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://te.legra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("/stop"),
        ),
    ]
    search_query = query.query.lower().strip().rstrip()

    if search_query == "":
        await client.answer_inline_query(
            query.id,
            results=answerss,
            switch_pm_text="ᴛʏᴘᴇ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴛʜᴇ sᴏɴɢ/ᴠɪᴅᴇᴏ ʏᴏᴜᴛᴜʙᴇ...",
            switch_pm_parameter="help",
            cache_time=0,
        )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏ ,ᴍʏ ɴᴀᴍᴇ ɪs {BOT_NAME}.

*๏ ᴀ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.*
*๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs*..
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    ),
                ],
                [
                    InlineKeyboardButton(text="❄ ʜᴇʟᴩ ❄", callback_data="cbbasic"),
                    InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀", user_id=F_OWNER),
                ],
                [
                    InlineKeyboardButton(
                        text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        text="💘 ᴄʜᴀɴɴᴇʟ 💘", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="☁ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ☁",
                        url="https://github.com/Abishnoi69/AsuXMusic",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ℹ️ ᴄᴏᴍᴍᴀɴᴅ ᴍᴇɴᴜ

🤷 » /id - ᴛᴏ ɢᴇᴛ ᴜsᴇʀ ɪᴅ

🤷 » /play - ᴛʏᴘᴇ ᴛʜɪs ᴡɪᴛʜ ɢɪᴠᴇ ᴛʜᴇ sᴏɴɢ ᴛɪᴛʟᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴏʀ ᴀᴜᴅɪᴏ ғɪʟᴇ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ. (Remember to don't play YouTube live stream by using this command!, because it will cause unforeseen problems.)

🤷 » /pause - ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ

🤷 » /skip - ᴛᴏ sᴋɪᴘ ᴄᴜʀʀᴇɴᴛ sᴏɴɢ

🤷 » /repo - ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʀᴇᴘᴏ

🙋 » /end - ᴛᴏ end ᴘʟᴀʏ sᴏɴɢ ɪɴ ᴠᴄ.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ɢᴏ ʙᴀᴄᴋ 🏡", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer(
            "💡 ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !",
            show_alert=True,
        )
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    if chat_id in QUEUE:
        await query.answer("ᴄᴏɴᴛʀᴏʟ ᴘᴀɴᴇʟ ᴏᴘᴇɴᴇᴅ")
        await query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        await query.answer("❌ ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Client.on_callback_query(filters.regex("cbdown"))
async def cbdown(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    buttons = song_download_markup(videoid)
    await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex(pattern=r"song_back"))
async def songs_back_helper(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    buttons = song_download_markup(videoid)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex(pattern=r"gets"))
async def song_helper_cb(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    videoid, user_id = callback_request.split("|")
    try:
        await CallbackQuery.answer("soon", show_alert=True)
    except:
        pass
    if stype == "audio":
        try:
            formats_available, link = await YouTube.formats(videoid, True)
        except:
            return await CallbackQuery.edit_message_text("ᴅᴏᴡɴʟᴏᴀᴅ ᴀᴜᴅɪᴏ")
        keyboard = InlineKeyboard()
        done = []
        for x in formats_available:
            check = x["format"]
            if "audio" in check:
                if x["filesize"] is None:
                    continue
                form = x["format_note"].title()
                if form not in done:
                    done.append(form)
                else:
                    continue
                sz = convert_bytes(x["filesize"])
                fom = x["format_id"]
                keyboard.row(
                    InlineKeyboardButton(
                        text=f"{form} ǫᴜᴀʟɪᴛʏ ᴀᴜᴅɪᴏ = {sz}",
                        callback_data=f"song_download {stype}|{fom}|{videoid}",
                    ),
                )
        keyboard.row(
            InlineKeyboardButton(
                text="🔙 ʙᴀᴄᴋ",
                callback_data=f"song_back {stype}|{videoid}",
            ),
            InlineKeyboardButton(text="✖️ ᴄʟᴏsᴇ ", callback_data=f"cls"),
        )
        return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)
    else:
        try:
            formats_available, link = await YouTube.formats(videoid, True)
        except Exception as e:
            print(e)
            return await CallbackQuery.edit_message_text("ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ")
        keyboard = InlineKeyboard()
        done = [160, 133, 134, 135, 136, 137, 298, 299, 264, 304, 266]
        for x in formats_available:
            check = x["format"]
            if x["filesize"] is None:
                continue
            if int(x["format_id"]) not in done:
                continue
            sz = convert_bytes(x["filesize"])
            ap = check.split("-")[1]
            to = f"{ap} = {sz}"
            keyboard.row(
                InlineKeyboardButton(
                    text=to,
                    callback_data=f"song_download {stype}|{x['format_id']}|{videoid}",
                )
            )
        keyboard.row(
            InlineKeyboardButton(
                text="🔙 ʙᴀᴄᴋ",
                callback_data=f"song_back {stype}|{videoid}",
            ),
            InlineKeyboardButton(text="✖️ ᴄʟᴏsᴇ", callback_data=f"cls"),
        )
        return await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)


@Client.on_callback_query(filters.regex(pattern=r"song_download"))
async def song_download_cb(client, CallbackQuery):
    try:
        await CallbackQuery.answer("ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ")
    except:
        pass
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    stype, format_id, videoid = callback_request.split("|")
    mystic = await CallbackQuery.edit_message_text(_["song_8"])
    yturl = f"https://www.youtube.com/watch?v={vidid}"
    with yt_dlp.YoutubeDL({"quiet": True}) as ytdl:
        x = ytdl.extract_info(yturl, download=False)
    title = (x["title"]).title()
    title = re.sub("\W+", " ", title)
    thumb_image_path = await CallbackQuery.message.download()
    duration = x["duration"]
    if stype == "video":
        thumb_image_path = await CallbackQuery.message.download()
        width = CallbackQuery.message.photo.width
        height = CallbackQuery.message.photo.height
        try:
            file_path = await YouTube.download(
                yturl,
                mystic,
                songvideo=True,
                format_id=format_id,
                title=title,
            )
        except Exception as e:
            return await mystic.edit_text("error".format(e))
        med = InputMediaVideo(
            media=file_path,
            duration=duration,
            width=width,
            height=height,
            thumb=thumb_image_path,
            caption=title,
            supports_streaming=True,
        )
        await mystic.edit_text("video")
        await app.send_chat_action(
            chat_id=CallbackQuery.message.chat.id,
            action="upload_video",
        )
        try:
            await CallbackQuery.edit_message_media(media=med)
        except Exception as e:
            print(e)
            return await mystic.edit_text("sᴏᴏɴᴠɪᴅᴇᴏ")
        os.remove(file_path)
    elif stype == "audio":
        try:
            filename = await YouTube.download(
                yturl,
                mystic,
                songaudio=True,
                format_id=format_id,
                title=title,
            )
        except Exception as e:
            return await mystic.edit_text("error".format(e))
        med = InputMediaAudio(
            media=filename,
            caption=title,
            thumb=thumb_image_path,
            title=title,
            performer=x["uploader"],
        )
        await mystic.edit_text("audio")
        await app.send_chat_action(
            chat_id=CallbackQuery.message.chat.id,
            action="upload_audio",
        )
        try:
            await CallbackQuery.edit_message_media(media=med)
        except Exception as e:
            print(e)
            return await mystic.edit_text("sᴏᴏɴᴀᴜᴅɪᴏ")
        os.remove(filename)


@Client.on_callback_query(filters.regex("cbhome"))
async def cbhome(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer(
            "💡 ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !",
            show_alert=True,
        )
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = stream_markup(user_id, dlurl)
    if chat_id in QUEUE:
        await query.answer("Back")
        await query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        await query.answer("❌ ɴᴏᴛʜɪɴɢ ɪs ᴄᴜʀʀᴇɴᴛʟʏ sᴛʀᴇᴀᴍɪɴɢ", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer(
            "💡 ᴏɴʟʏ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴘᴇʀᴍɪssɪᴏɴ ᴛʜᴀᴛ ᴄᴀɴ ᴛᴀᴘ ᴛʜɪs ʙᴜᴛᴛᴏɴ !",
            show_alert=True,
        )
    await query.message.delete()
