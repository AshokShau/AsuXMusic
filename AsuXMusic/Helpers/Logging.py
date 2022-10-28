import config
from .Clients import app, Ass

failure = "ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜʀ ʙᴏᴛ ɪs ɪɴ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɪs ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀɴ ᴀᴅᴍɪɴ ᴡɪᴛʜ ғᴜʟʟ ʀɪɢʜᴛs !"


async def startup_msg(_message_):
    try:
        AsuXwtf = await app.send_message(
            config.LOGGER_ID, f"{_message_}"
        )
        return AsuXwtf
    except:
        print(failure)
        return


async def startup_edit(_message_id, _message_):
    try:
        AsuXwtf = await app.edit_message_text(
            config.LOGGER_ID, _message_id.message_id, f"{_message_}"
        )
        return AsuXwtf
    except:
        AsuXwtf = await startup_send_new(_message_)
        return AsuXwtf


async def startup_del(_message_id):
    try:
        await app.delete_messages(config.LOGGER_ID, _message_id.message_id)
        return bool(1)
    except:
        pass
