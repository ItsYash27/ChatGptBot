# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

import requests
import os
import json
import random
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren 
from pyrogram.errors import MessageNotModified
from chatgpt.module.what import *
from config import OPENAI_API 

@ren.on_message(filters.command("gpt") & filters.private | filters.group)
async def chatgpt(c: Client, m: Message):
    randydev = (
        m.text.split(None, 1)[1]
        if len(
            m.command,
        )
        != 1
        else None
    )
    if not randydev:
       await m.reply(f"use command <code>/{m.command[0]} [question]</code> to ask questions using the API.")
       return
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "prompt": crazyyash,
        "model": "text-davinci-003",
        "temperature": 0.5,
        "max_tokens": 1024,
        "n": 1,
        "stop": None,
        "temperature": 0.9,
        "top_p": 0.3,
        "frequency_penalty": 0.5,
    }
    ran = await m.reply("ʟᴏᴏᴋɪɴɢ ғᴏʀ ʀᴇsᴜʟᴛs/n ⭐ᴡʜɪʟᴇ ᴡᴀɪᴛɪɴɢ ᴇᴀᴛ ғɪᴠᴇ sᴛᴀʀ ᴀɴᴅ ᴅᴏ ɴᴏᴛʜɪɴɢ...", quote=True)
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await ran.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await ran.edit("ʏᴇᴀʜ, ɴᴏ ʀᴇsᴜʟᴛs ғᴏᴜɴᴅ")
