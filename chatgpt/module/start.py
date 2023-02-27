# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from pyrogram import Client as ren
from pyrogram import *
from pyrogram.types import *

@ren.on_message(filters.command("start") & filters.private)
async def start_bot(c: Client, m: Message):
    start_welcome = f"Hello {m.from_user.mention} 🛐\n ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ, \n ɪ ᴄᴀɴ ғᴇᴛᴄʜ ʀᴇsᴜʟᴛs ᴜsɪɴɢ ᴄʜᴀᴛɢᴘᴛ ᴀᴘɪ ᴊᴜsᴛ ᴜsᴇ \n`/gpt Your Query`"
    start_button = InlineKeyboardMarkup([[InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{c.me.username}?startgroup=True")]])
    await m.reply_text(start_welcome, reply_markup=start_button)
