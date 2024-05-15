import asyncio
import os
from secrets import choice
import random
from urllib.parse import quote_plus
from collections import deque
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import InputMessagesFilterVoice

from WWWL5 import WWWL5

from WWWL5.core.logger import logging
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from . import ALIVE_NAME, mention
from ..helpers import get_user_from_event
from ..helpers.utils import _format

from . import reply_id


@WWWL5.on(admin_cmd(outgoing=True, pattern="fox Updates$"))
async def jepvois(Voice):
  url = f"https://t.me/vzo_a"
  await Voice.client.send_file(Voice.chat_id,url,caption="⎊︙ اخر تحديثات𝐒𝐎𝐔𝐑𝐂𝐄 𝐅𝐎𝐗&𝐍𝐎𝐑 𓅃\n⎊︙ BY : @vzo_a 👑",parse_mode="html")
  await Voice.delete()
