import json
import asyncio
from pyrogram import Client
from pytgcalls import PyTgCalls, idle
from pyromod import listen

# استيراد الهاندلرز من bot.py
from bot import register_handlers

# قراءة الإعدادات من config.json
with open("config.json", "r") as f:
    config = json.load(f)

API_ID = config["API_ID"]
API_HASH = config["API_HASH"]
BOT_TOKEN = config["BOT_TOKEN"]

# إنشاء عميل البوت
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# إنشاء PyTgCalls (لو بدك تستعمل المكالمات الصوتية)
call_app = PyTgCalls(app)

async def main():
    # تسجيل الهاندلرز من bot.py
    register_handlers(app, call_app)

    # تشغيل البوت
    await app.start()
    await call_app.start()
    print("🚀 البوت شغال...")
    await idle()
    await app.stop()
    await call_app.stop()

if __name__ == "__main__":
    asyncio.run(main())
