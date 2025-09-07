import os
import json
from pyrogram import Client, idle
from pyromod import listen  # noqa: F401
from pyrogram.types import ChatPrivileges, ChatPermissions  # noqa: F401

# Load config
CONFIG_PATH = os.getenv("CONFIG_PATH", "config.json")
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = json.load(f)

api_id = int(os.getenv("API_ID", config.get("api_id", 0)))
api_hash = os.getenv("API_HASH", config.get("api_hash", ""))
bot_token = os.getenv("BOT_TOKEN", config.get("bot_token", ""))

# Core metadata
sourse_dev = config.get("sourse_dev")
DEVS = []
if sourse_dev:
    DEVS.append(sourse_dev)

# Init bot client
bot = Client(
    "m4o",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    plugins=dict(root="MZombie"),
)

async def start_zombiebot():
    await bot.start()
    # Notify dev(s)
    for dev in DEVS:
        try:
            await bot.send_message(dev, "◍ تم تشغيل الصانع بنجاح 🚦\n√")
        except Exception:
            pass
    await idle()
