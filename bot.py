import json
from pyrogram import Client, filters
from pyrogram.types import ChatPrivileges, ChatPermissions

# قراءة الإعدادات من config.json
with open("config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

sourse_dev = config.get("sourse_dev", None)

DEVS = []
DEVS.append(7028046857)  # ID المطور
owner_id = sourse_dev
bot_id = config["BOT_TOKEN"].split(":")[0]


def register_handlers(app: Client, call_app=None):

    @app.on_message(filters.command("start"))
    async def start_handler(client, message):
        await message.reply_text("✅ تم تشغيل البوت بنجاح")

    @app.on_message(filters.user(DEVS) & filters.command("ping"))
    async def ping_handler(client, message):
        await message.reply_text("🏓 البوت شغال وعم يرد عليك يا مطور!")

    # هون فيك تضيف باقي الأوامر (من ملفات plugins لو عندك)
