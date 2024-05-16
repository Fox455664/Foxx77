#الملف بحقوق سورس سبايدر @vzo_a
import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from WWWL5 import WWWL5
from ..helpers.utils import reply_id


@WWWL5.on(admin_cmd(outgoing=True, pattern="آيه قصيره$"))
async def jepvois(vois):
  rl = random.randint(111,210)
  url = f"https://t.me/Fox455664/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎊︙ BY : @vzo_a 🌺",parse_mode="html")
  await vois.delete()


@WWWL5.on(admin_cmd(outgoing=True, pattern="سوره الفاتحة$"))
async def jepvois(Voice):
  url = f"https://t.me/vzo_a"
  await Voice.client.send_file(Voice.chat_id,url,caption="⎊︙ سوره الفاتحة\n⎊︙ بصوت القارئ ماهر المعيقلي\n⎊︙ BY : @vzo_a 🌺",parse_mode="html")
  await Voice.delete()
