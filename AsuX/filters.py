from typing import List, Union

from pyrogram import filters

COMMAND_PREFIXES = ["/", "!", ".", "*", "+"]


other_filters = filters.group & ~filters.via_bot & ~filters.forwarded
other_filters2 = filters.private & ~filters.via_bot & ~filters.forwarded


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
