from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta
from pyromod import listen 
from pyrogram.types import Message
import random 
import asyncio
import shutil
from pyrogram.types import CallbackQuery
from pyrogram import Client, filters, idle
import re
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
import os
from pyrogram.types import Message
from pyromod import listen
import os
import pyrogram
import re
import asyncio
from pyrogram import Client, idle
from pyrogram import Client as app
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram import Client, filters
from pyrogram import Client as app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, ChatPrivileges
from pyrogram.enums import ChatType
import asyncio
import random
from pyrogram.types import ChatPrivileges, ChatPermissions
from dotenv import load_dotenv
from pytgcalls import PyTgCalls
import asyncio
from pyrogram import Client,filters,enums,idle
import re
import pyrogram
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
from random import randint
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)
from pytgcalls import PyTgCalls, StreamType
from pyrogram import Client, filters
from os import remove
from asyncio import sleep
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
import re
from pyrogram.types import Message
import random
import time
from asyncio import gather
import os, time
from telegraph import upload_file
from os import remove
import time
from PIL import Image
from io import BytesIO
from asyncio import sleep
from pyrogram import Client, filters
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from pytgcalls.types import Update
from pytgcalls.types.stream import StreamAudioEnded
from pytgcalls import PyTgCalls, StreamType
from pyrogram.enums import ChatType, ChatMemberStatus
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (HighQualityAudio,
                                                  HighQualityVideo,
                                                  LowQualityAudio,
                                                  LowQualityVideo,
                                                  MediumQualityAudio,
                                                  MediumQualityVideo)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import asyncio
import random
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram.enums import ChatMembersFilter
from pyrogram.enums import ChatMemberStatus
import aiofiles
import aiohttp
from io import BytesIO
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps
from unidecode import unidecode
from pyrogram import *
from dotenv import load_dotenv
from os import getenv
import os
import random
from pyrogram.types import *
from pyrogram.errors import PeerIdInvalid
import asyncio
import aiohttp
import requests
from datetime import datetime
from random import choice
from collections import defaultdict
from pyrogram import enums
from pyrogram.types import ChatPermissions, ChatPrivileges
from datetime import datetime
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
import time
from aiohttp import ClientSession
from traceback import format_exc
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from pymongo import MongoClient
import textwrap
from googletrans import Translator
import json

load_dotenv()


API_ID = int(getenv("API_ID", "28375705"))
API_HASH = getenv("API_HASH", '8a1479ad70ce4230ad0d7168804b60d0')
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(getenv("OWNER_ID"))
appusername = getenv("appusername")
BOT_USERNAME = getenv("appusername")
num_design = getenv("num_design")
app = Client("zombie", API_ID, API_HASH, bot_token=BOT_TOKEN)

translator = Translator()

bot_id = BOT_TOKEN.split(":")[0]

with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

audio_bass = "/root/hamo/"
photo_bot = f"/root/photos/{appusername}.jpg"
BOT_NAME = config['BOT_NAME']
co_dev_name = config['co_dev_name']
zombie_id = config['zombie_id']
photo_source = config['photo_source']
photo_path = config['photo_path']
gr = config['gr']
channel_userss = config['channel_userss']
channel_source = config['channel_source']
c_channel_source = config['c_channel_source']
source_devv = config['source_devv']
design = config['design']
sourse_dev = config['sourse_dev']
c_gr = config['c_gr']
dev = []
dev.append(7028046857)
###################################################### data_base ####################################################

MONGO_URI = "mongodb+srv://amrabdo14a:uCbZL3RlhU4lfz41@cluster0.m4tgelc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
db_client = MongoClient(MONGO_URI)
db = db_client["telegram_factory"]

###################################################### data_base ####################################################

###################################################### رفع تلقائي ####################################################
unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)
mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False, 
    can_send_other_messages=False,
    can_send_polls=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_pin_messages=False,
    can_invite_users=True,
)
@app.on_chat_member_updated(filters.group)
async def chat_member_updated(client, chat_member_update):
    if chat_member_update.new_chat_member:
        user = chat_member_update.new_chat_member.user
        user_id = user.id
        if user_id == zombie_id:
            await app.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(can_promote_members=True,can_manage_video_chats=True,can_pin_messages=True,can_invite_users=True,can_restrict_members=True,can_delete_messages=True,can_change_info=False)
            )
            await app.send_message(chat_id=chat_member_update.chat.id,text=f"**♪ انضم المبرمج محمد صالح للشات  🥷 .\n♪ مرحبا بك : @R_9_9_0  🥷 .**")
        elif user_id == OWNER_ID:
            await app.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(can_promote_members=True,can_manage_video_chats=True,can_pin_messages=True,can_invite_users=True,can_restrict_members=True,can_delete_messages=True,can_change_info=False)

            )
            await app.send_message(chat_id=chat_member_update.chat.id,text=f"**♪ انضم مطور البوت للشات  🥷**")
        elif user_id == sourse_dev:
            await app.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(can_promote_members=True,can_manage_video_chats=True,can_pin_messages=True,can_invite_users=True,can_restrict_members=True,can_delete_messages=True,can_change_info=False)
            )
            await app.send_message(chat_id=chat_member_update.chat.id,text=f"**♪ انضم مطور السورس للشات  🥷**")

@app.on_chat_member_updated(filters.channel)
async def chat_memr_updated(client, chat_member_update):
    if chat_member_update.new_chat_member:
        user = chat_member_update.new_chat_member.user
        user_id = user.id
        if user_id == zombie_id:
            await app.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(can_promote_members=False,can_manage_video_chats=True,can_post_messages=True,can_invite_users=True,can_edit_messages=True,can_delete_messages=True,can_change_info=False)
            )
            await app.send_message(chat_id=chat_member_update.chat.id,text=f"**♪ انضم المبرمج محمد صالح للشات  🥷 .\n♪ مرحبا بك : @R_9_9_0  🥷 .**")
        elif user_id == OWNER_ID:
            await app.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(can_promote_members=False,can_manage_video_chats=True,can_post_messages=True,can_invite_users=True,can_edit_messages=True,can_delete_messages=True,can_change_info=False)
            )
            await app.send_message(chat_id=chat_member_update.chat.id,text=f"**♪ انضم مطور البوت للشات  🥷**")
        elif user_id == sourse_dev:
            await app.promote_chat_member(
                chat_id=chat_member_update.chat.id,
                user_id=user_id,
                privileges=ChatPrivileges(can_promote_members=False,can_manage_video_chats=True,can_post_messages=True,can_invite_users=True,can_edit_messages=True,can_delete_messages=True,can_change_info=False)
            )
            await app.send_message(chat_id=chat_member_update.chat.id,text=f"**♪ انضم مطور السورس للشات  🥷**")
###################################################### رفع تلقائي ####################################################
#####################################  المالك والتاك  ##################################################
@app.on_message(filters.command(["المالك", "صاحب الخرابه", "المنشي"], ""))
async def gak_owne(client: Client, message: Message):
    if len(message.command) > 1:
        return
    chat_id = message.chat.id
    async for member in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            id = member.user.id
            key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
            m = await client.get_chat(id)
            if m.photo:
                photo = await app.download_media(m.photo.big_file_id)
                return await message.reply_photo(photo, caption=f"🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{m.first_name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{m.username}\n🎃 ¦𝙸𝙳 :`{m.id}`\n💌 ¦𝙱𝙸𝙾 :{m.bio}\n✨ ¦𝙲𝙷𝙰𝚃: {message.chat.title}\n♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :`{message.chat.id}`", reply_markup=key)
            else:
                return await message.reply("◍ " + member.user.mention)     

array = []
@app.on_message(filters.command(["@all", "تاك","تاك للكل"], ""))
async def nummmm(client, message):
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  await message.reply_text("**جاري بدأ المنشن ، لايقاف الامر اضغط **\n /cancel او اكتب بس منشن")
  i = 0
  txt = ""
  zz = message.text
  if message.photo:
          photo_id = message.photo.file_id
          photo = await client.download_media(photo_id)
          zz = message.caption
  try:
   zz = zz.replace("@all","").replace("تاك","").replace("نادي الكل","")
  except:
    pass
  array.append(message.chat.id)
  async for x in app.get_chat_members(message.chat.id):
      if message.chat.id not in array:
        return
      if not x.user.is_deleted:
       i += 1
       txt += f"{x.user.mention} ،"
       if i == 30:
        try:
              if not message.photo:
                    await client.send_message(message.chat.id, f"{zz}\n{txt}")
              else:
                    await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
              i = 0
              txt = ""
              await asyncio.sleep(3)
        except FloodWait as e:
                    flood_time = int(e.x)
                    if flood_time > 500:
                        continue
                    await asyncio.sleep(flood_time)
        except Exception:
              array.remove(message.chat.id)
  array.remove(message.chat.id)


@app.on_message(filters.command(["بس المنشن", "/cancel","بس منشن","ايقاف التاك"], ""))
async def stop(client, message):
  chek = await client.get_chat_member(message.chat.id, message.from_user.id)
  if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    await message.reply("**يجب انت تكون مشرف لاستخدام الامر 🖱️")
    return
  if message.chat.id not in array:
     await message.reply("**المنشن متوقف بالفعل**")
     return 
  if message.chat.id in array:
    array.remove(message.chat.id)
    await message.reply("**تم ايقاف المنشن بنجاح✅**")
    return
#####################################  المالك والتاك  ##################################################
###################################################  التسليه وبوت  ##################################################

selections = [
    f"{BOT_NAME} يصحبي والله",
    f"قولتلك اسمي {BOT_NAME} ياهلًا",
    f"نعم يحب {BOT_NAME} يتفضل",
    f"قول يقلب {BOT_NAME} موجود",
    "هوا عشان بحبك تصعدني؟",
    f"والله بحبك بس ناديلي ب{BOT_NAME}",
    f"تعرف بالله هحبك اكتر لو ناديتلي {BOT_NAME}",
    "اي ي معلم مين مزعلك",
    "متصلي علي النبي كدا",
    "مش فاضيلك نصايه وكلمني",
    "قولي مين مزعلك وعايزك تقعد وتتفرج ع اخوك",
    "عايزني اشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا",
    f"ورحمه ابويا اسمي {BOT_NAME} مش غلط",
    f"يا حبيبي {BOT_NAME} تحت أمرك",
    f"{BOT_NAME} حاضر لك يا كبير",
    f"أنا سمعتك بتناديني {BOT_NAME}"
]

async def get_bot_name():
    global BOT_NAME
    return BOT_NAME

@app.on_message(filters.group, group=54100054)
async def trmessage(client, message):
    global BOT_NAME
    bar = random.choice(selections).format(BOT_NAME=BOT_NAME)
    if message.from_user:
        if message.text:
            if BOT_NAME.lower() == message.text.lower():
                await message.reply(
                    f'<a href="{channel_source}">{bar}</a>',
                    disable_web_page_preview=True
                )

@app.on_message(filters.command(["ضع اسم للبوت 🤖", "تعين اسم البوت"], ""),group=5478789)
async def set_bot(client: Client, message):
    NAME = await client.ask(message.chat.id, "**◍ ارسل اسم البوت الجديد الأن 🤖\n√**", filters=filters.text, timeout=30)
    global BOT_NAME
    BOT_NAME = NAME.text
    await message.reply_text("**◍ تم تعيين اسم البوت بنجاح ✅\n√**")

#################################################### بوت  ###################################################
@app.on_message(filters.command(["بوت", "البوت"], ""), group=5487)
async def botzomnbie(client: Client, message: Message):
    BOT_NAME = await get_bot_name()
    bar = random.choice(selections).format(BOT_NAME=BOT_NAME)
    await message.reply(
        f'<a href="{channel_source}">{bar}</a>',
        disable_web_page_preview=True
    )
####################################################  الكول ###################################################
########################################### الاشتراك الاجباري ################################################

colletion_channel = db[f"bot_chanels_{BOT_USERNAME}"]

def add_bot_chanel(channel):
    if not colletion_channel.find_one({"channel": channel}):
        colletion_channel.insert_one({"channel": channel})

def del_bot_chanel(channel):
    colletion_channel.delete_one({"channel": channel})

def get_bot_chanels():
    channels = [doc["channel"] for doc in colletion_channel.find()]
    return channels


async def check_chat_member_status(user_id, message, client):
    required_channels = get_bot_chanels()
    for channel in required_channels:
        try:
            await client.get_chat_member(channel, user_id)
        except Exception:
            await message.delete()
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("**اضغط هنا للاشتراك بالقناة 🚦**", url=f"https://t.me/{channel}")]]
            )
            text = f"🚦 **عذرا عزيزي يجب عليك الاشتراك في القناة أولًا.**\n\n📌 **قناة البوت:**\n➜ [@{channel}](https://t.me/{channel})"
            await client.send_message(chat_id=message.chat.id, text=text, reply_markup=keyboard)
            return False
    return True

@app.on_message(filters.command(["اضف قناة الاشتراك الخاص 📢"], "") & filters.private,group=12124688756)
async def asads_sub(client, message):
    if get_premium_status() and message.from_user.id == OWNER_ID or message.from_user.id in dev or message.from_user.id == sourse_dev:
        cancel_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
        ])
        ask = await client.ask(
            message.chat.id,
            "**◍ أرسل معرف القناة مثال: @ChannelName\n**"
            "**◍ وتأكد من رفع البوت مشرف فالقناة 👮🏻‍♂️\n**"
            "**√**",
            timeout=300,
            reply_markup=cancel_markup
        )
        if hasattr(ask, 'data') and ask.data == "cancel_add":
            return await ask.message.edit_text("**✅ تم إلغاء عملية الإضافة**")      
        channel_username = ask.text.strip().replace("@", "")
        add_bot_chanel(channel_username)
        await client.send_message(message.chat.id, f"**◍ تم اضافة القناة للبوت ✅\n√**")
    else:
        await message.reply_text(f"**◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√**")

@app.on_message(filters.command(["حذف قناة الاشتراك الخاص 🗑"], "") & filters.private,group=1982112456)
async def aaddel_sub(client, message):
    if get_premium_status() and message.from_user.id == OWNER_ID or message.from_user.id in dev or message.from_user.id == sourse_dev:
        cancel_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
        ])
        ask = await client.ask(
            message.chat.id,
            "**◍ أرسل معرف القناة مثال: @ChannelName\n**"
            "**√**",
            timeout=300,
            reply_markup=cancel_markup
        )
        if hasattr(ask, 'data') and ask.data == "cancel_add":
            return await ask.message.edit_text("**✅ تم إلغاء عملية الإضافة**")   
        channel_username = ask.text.strip().replace("@", "")
        del_bot_chanel(channel_username)
        await client.send_message(message.chat.id, "**◍ تم حذف القناة ❌\n√**")
    else:
        await message.reply_text(f"**◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√**")

  
@app.on_message(filters.command(["قنوات الاشتراك الخاص 📩"], "") & filters.private,group=1531445465)
async def channells(client, message):
    if get_premium_status() and message.from_user.id == OWNER_ID or message.from_user.id in dev or message.from_user.id == sourse_dev:
        channels = get_bot_chanels()
        if not channels:
            return await message.reply_text(f"❌ لا توجد قنوات اشتراك إجبارية للبوت @{BOT_USERNAME}.")
        text = f"📋 **قنوات الاشتراك الإجباري للبوت @{BOT_USERNAME}:**\n\n"
        text += "\n".join([f"{i + 1}- @{channel}" for i, channel in enumerate(channels)])
        await message.reply_text(text)
    else:
        await message.reply_text(f"**◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√**")



async def checkg_member_status(user_id, message, client):
    user_id = message.from_user.id if message.from_user else "None"
    required_channels = get_bot_channels()
    for channel in required_channels:
        try:
            await app.get_chat_member(channel, user_id)
        except Exception as e:
            await message.delete()
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton("**اضغط هنا للاشتراك بالقناة 🚦**", url=f"https://t.me/{channel}")]]
            )
            text = f"🚦 **عذرا عزيزي يجب عليك الاشتراك في القناة أولًا.**\n\n📌 **قناة البوت:**\n➜ [@{channel}](https://t.me/{channel})"
            await app.send_message(chat_id=message.chat.id, text=text, reply_markup=keyboard)
            return False
    return True


collection_channel = db[f"bot_channels_{BOT_USERNAME}"]

def add_bot_channel(channel):
    if not collection_channel.find_one({"channel": channel}):
        collection_channel.insert_one({"channel": channel})

def del_bot_channel(channel):
    collection_channel.delete_one({"channel": channel})

def get_bot_channels():
    channels = [doc["channel"] for doc in collection_channel.find()]
    return channels

@app.on_message(filters.command("اضف قناة الاشتراك 📎", "") & filters.private, group=54888)
async def add_bot_subscription(client, message):
    if get_premium_status() and message.from_user.id == OWNER_ID or message.from_user.id in dev or message.from_user.id == sourse_dev:
        cancel_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
        ])
        ask = await client.ask(
            message.chat.id,
            "**◍ أرسل معرف القناة مثال: @ChannelName\n**"
            "**◍ وتأكد من رفع البوت مشرف فالقناة 👮🏻‍♂️\n**"
            "**√**",
            timeout=300,
            reply_markup=cancel_markup
        )
        if hasattr(ask, 'data') and ask.data == "cancel_add":
            return await ask.message.edit_text("**✅ تم إلغاء عملية الإضافة**")   
        channel_username = ask.text.strip().replace("@", "")
        add_bot_channel(channel_username)
        await client.send_message(message.chat.id, f"**◍ تم اضافة القناة للبوت ✅\n√**")
    else:
        await message.reply_text(f"**◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√**")

@app.on_message(filters.command("حذف قناة الاشتراك 🗑", "") & filters.private, group=544547)
async def remove_bot_subscription(client, message):
    if get_premium_status() and message.from_user.id == OWNER_ID or message.from_user.id in dev or message.from_user.id == sourse_dev:
        cancel_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
        ])
        ask = await client.ask(
            message.chat.id,
            "**◍ أرسل معرف القناة مثال: @ChannelName\n**"
            "**√**",
            timeout=300,
            reply_markup=cancel_markup
        )
        if hasattr(ask, 'data') and ask.data == "cancel_add":
            return await ask.message.edit_text("**✅ تم إلغاء عملية الإضافة**")   
        channel_username = ask.text.strip().replace("@", "")
        del_bot_channel(channel_username)
        await client.send_message(message.chat.id, f"**◍ تم حذف القناة ❌\n√**")
    else:
        await message.reply_text(f"**◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√**")

@app.on_message(filters.command("قنوات الاشتراك 📥", "") & filters.private, group=54454)
async def list_bot_subscriptions(client, message):
    if get_premium_status() and message.from_user.id == OWNER_ID or message.from_user.id in dev or message.from_user.id == sourse_dev:
        channels = get_bot_channels()
        if not channels:
            return await message.reply_text(f"❌ لا توجد قنوات اشتراك إجبارية للبوت @{BOT_USERNAME}.")
        text = f"📋 **قنوات الاشتراك الإجباري للبوت @{BOT_USERNAME}:**\n\n"
        text += "\n".join([f"{i + 1}- @{channel}" for i, channel in enumerate(channels)])
        await message.reply_text(text)
    else:
        await message.reply_text(f"**◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√**")

########################################### الاشتراك الاجباري ################################################



########################################### الاشتراك الاجباري ################################################
async def check_group_member_status(user_id, message, client, group_id):
    required_channels = get_group_channels(group_id)
    if not required_channels:
        return True
        
    for channel in required_channels:
        try:
            await app.get_chat_member(channel, user_id)
        except Exception as e:
            try:
                await message.delete()
            except Exception as e:
                print(f"Failed to delete message: {e}")
            keyboard = InlineKeyboardMarkup(
                [[InlineKeyboardButton(f"اضغط هنا للاشتراك بالقناة 🚦", url=f"https://t.me/{channel}")]]
            )
            text = f"🚦**عذرا عزيزي يجب عليك الاشتراك في القناة أولًا.**\n\n📌 **قناة المجموعة:**\n➜ [@{channel}](https://t.me/{channel})"
            dd = await app.send_message(chat_id=message.chat.id, text=text, reply_markup=keyboard)
            await asyncio.sleep(60)
            await dd.delete()
            return False
    return True

collection_group_channels = db[f"group_subscription_channels_{BOT_USERNAME}"]

def add_group_channel(group_id, channel):
    if not collection_group_channels.find_one({"group_id": group_id, "channel": channel}):
        collection_group_channels.insert_one({"group_id": group_id, "channel": channel})

def del_group_channel(group_id, channel):
    collection_group_channels.delete_one({"group_id": group_id, "channel": channel})

def get_group_channels(group_id):
    channels = [doc["channel"] for doc in collection_group_channels.find({"group_id": group_id})]
    return channels

def clear_group_channels(group_id):
    collection_group_channels.delete_many({"group_id": group_id})

@app.on_message(filters.command("اضف قناه الاشتراك", prefixes="") & filters.group, group=51397188)
async def add_group_subscription(client, message):
    if not await i_group_admin(client, message.chat.id, message.from_user.id):
        return await message.reply("❌ يجب أن تكون مشرفًا في المجموعة لاستخدام هذا الأمر.")
    
    ask_channel = await client.ask(message.chat.id, "🔹 أرسل معرف القناة مع علامة @", filters=filters.user(message.from_user.id), timeout=300)
    channel_username = ask_channel.text.strip().replace("@", "")
    add_group_channel(message.chat.id, channel_username)
    await client.send_message(message.chat.id, f"✅ تم إضافة القناة @{channel_username} إلى قائمة الاشتراك الإجباري لهذه المجموعة.")

@app.on_message(filters.command("حذف قناه الاشتراك", prefixes="") & filters.group, group=10547)
async def remove_group_subscription(client, message):
    if not await i_group_admin(client, message.chat.id, message.from_user.id):
        return await message.reply("❌ يجب أن تكون مشرفًا في المجموعة لاستخدام هذا الأمر.")
    ask_channel = await client.ask(message.chat.id, "🔹 أرسل معرف القناة مع علامة @", filters=filters.user(message.from_user.id), timeout=300)
    channel_username = ask_channel.text.strip().replace("@", "")
    del_group_channel(message.chat.id, channel_username)
    await client.send_message(message.chat.id, f"❌ تم حذف القناة @{channel_username} من قائمة الاشتراك الإجباري لهذه المجموعة.")

@app.on_message(filters.command("قنوات الاشتراك", prefixes="") & filters.group, group=5124584)
async def list_group_subscriptions(client, message):
    channels = get_group_channels(message.chat.id)
    if not channels:
        return await message.reply_text("❌ لا توجد قنوات اشتراك إجبارية لهذه المجموعة.")
    text = "📋 **قنوات الاشتراك الإجباري لهذه المجموعة:**\n\n"
    text += "\n".join([f"{i + 1}- @{channel}" for i, channel in enumerate(channels)])
    await message.reply_text(text)

@app.on_message(filters.command("مسح قنوات الاشتراك", prefixes="") & filters.group, group=54984)
async def clear_group_subscriptions(client, message):
    if not await i_group_admin(client, message.chat.id, message.from_user.id):
        return await message.reply("❌ يجب أن تكون مشرفًا في المجموعة لاستخدام هذا الأمر.")
    clear_group_channels(message.chat.id)
    await message.reply("✅ تم مسح جميع قنوات الاشتراك الإجباري لهذه المجموعة.")

async def i_group_admin(client, chat_id, user_id):
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]
    except:
        return False
    
async def i_group_owner(client, chat_id, user_id):
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [enums.ChatMemberStatus.ADMINISTRATOR]
    except:
        return False
    
async def i_group_owner_admin(client, chat_id, user_id):
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [enums.ChatMemberStatus.ADMINISTRATOR]
    except:
        return False

@app.on_message(filters.group, group=54531)
async def hadle_group_message(client, message):
    if not await check_group_member_status(message.from_user.id, message, client, message.chat.id):
        return
########################################### الاشتراك الاجباري ################################################
Keyboarddev = ReplyKeyboardMarkup(
  [
    ["🔻 قفل الكيبورد 🔻"],
    ["التفعيل والتعطيل 🔏", "قسم السورس 🚦"],
    ["الاحصائيات 📊"],
    ["قسم الاشتراك الاجباري 🎭", "قسم الاذاعة 🔊"],
    ["ضع اسم للبوت 🤖"],
    ["المطورين الثانويين 🧑🏻‍💻", "المطورين 🕵🏻‍♂️"],
    ["قسم العام 🚧"],
    ["حذف رد عام 🗑", "اضف رد عام 💬"],
    ["الردود العامة 📝"],
    ["قسم الترويج 💥"],
    ["سرعة السيرفر 🚀", "معلومات السيرفر ℹ️"],
    ["الاصدار ⚙️"],
    ["رستر البوت ♻️", "تحديث السورس 📥"]
  ],
  resize_keyboard=True
)

glsobal_ban = ReplyKeyboardMarkup(
    [
        ["الغاء حظر عام 🛑", "حظر عام 📛"],
        ["المحظورين عام 🙅🏻‍♂️"],
        ["الغاء كتم عام 🔔", "كتم عام 🔕"],
        ["المكتومين عام 🤐"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

Dev_kSouoard = ReplyKeyboardMarkup(
  [
    ["سورس ⚡️", "مطور السورس 👨🏻‍💻"],
    ["تعيين جروب السورس 👥", "تعيين قناة السورس 📣"],
    ["رجوع 🔙"]
  ],
  resize_keyboard=True
)

enableaa = ReplyKeyboardMarkup(
  [
    ["تعطيل التواصل 🔰", "تفعيل التواصل ⚡️"],
    ["تعطيل الميوزك 🔇", "تفعيل الميوزك 🎸"],
    ["تعطيل التنزيل 🛠", "تفعيل التنزيل ⚙️"],
    ["رجوع 🔙"]
  ],
  resize_keyboard=True
)

prodcast = ReplyKeyboardMarkup(
  [
    ["اذاعة للجروبات 👥", "اذاعة للمستخدمين 👤"],
    ["اذاعة للقنوات 📢"],
    ["اذاعة بالتوجية للجروبات 🔂", "اذاعة بالتوجية للمستخدمين 〽️"],
    ["اذاعة بالتوجية للقنوات 🧭"],
    ["رجوع 🔙"]
  ],
  resize_keyboard=True
)

mustjoin = ReplyKeyboardMarkup(
  [
    ["حذف قناة الاشتراك 🗑", "اضف قناة الاشتراك 📎"],
    ["قنوات الاشتراك 📥"],
    ["حذف قناة الاشتراك الخاص 🗑", "اضف قناة الاشتراك الخاص 📢"],
    ["قنوات الاشتراك الخاص 📩"],
    ["رجوع 🔙"]
  ],
  resize_keyboard=True
)

tarwekk = ReplyKeyboardMarkup(
  [
    ["ترويج للميوزك 🎸", "ترويج للحماية 🛡"],
    ["ترويج السماح بالتحدث 🗣", "ترويج للاذان 🕌"],
    ["رجوع 🔙"]
  ],
  resize_keyboard=True
)


@app.on_message(filters.regex(r"^قسم التحكم في المساعد 🕹$") & filters.private)
async def iqwdofus(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return await message.reply("⚠️ هذا الأمر متاح للمطورين فقط!")
    await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي │⎋ اليك قسم التحكم في المساعد", reply_markup=Dev_kSouoard)

@app.on_message(filters.regex(r"^قسم العام 🚧$") & filters.private)
async def iqwsaawus(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return await message.reply("⚠️ هذا الأمر متاح للمطورين فقط!")
    await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي │⎋ اليك قسم التحكم في المساعد", reply_markup=glsobal_ban)

@app.on_message(filters.regex(r"^قسم السورس 🚦$"))
async def iWQqws(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return await message.reply("⚠️ هذا الأمر متاح للمطورين فقط!")
    await message.reply("**💌╖أهلا بك عزيزي في قسم السورس\n🔰╢ تقدر تغير حقوق بوتك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة السورس دوس هنا**", reply_markup=Dev_kSouoard)

@app.on_message(filters.regex(r"^التفعيل والتعطيل 🔏$"))
async def iofrewus(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return await message.reply("⚠️ هذا الأمر متاح للمطورين فقط!")
    await message.reply("**💌╖أهلا بك في قسم التفعيل والتعطيل\n📲╢ تقدر تتحكم في مهام بوتك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة السورس دوس هنا**", reply_markup=enableaa)

@app.on_message(filters.regex(r"^قسم الاشتراك الاجباري 🎭$"))
async def iqwofdus(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return await message.reply("⚠️ هذا الأمر متاح للمطورين فقط!")
    await message.reply("╮⦿ اليك قسم الاشتراك الاجباري", reply_markup=mustjoin)

@app.on_message(filters.regex(r"^قسم الاذاعة 🔊$"))
async def iofawus(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return await message.reply("⚠️ هذا الأمر متاح للمطورين فقط!")
    await message.reply("╮⦿ اليك قسم الاذاعة", reply_markup=prodcast)

@app.on_message(filters.regex(r"^قسم الترويج 💥$"))
async def iofawqweus(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return await message.reply("⚠️ هذا الأمر متاح للمطورين فقط!")
    await message.reply("╮⦿ اليك قسم الترويج", reply_markup=tarwekk)

import speedtest
from pyrogram import Client, filters
import psutil
import platform
import datetime
from pyrogram import Client, filters
import psutil
import platform
from datetime import datetime
from pyrogram import Client, filters

@app.on_message(filters.regex(r"^معلومات السيرفر ℹ️$"))
async def server_info(client, message):
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)
    ram = psutil.virtual_memory()
    ram_total = ram.total / (1024 ** 3)
    ram_used = ram.used / (1024 ** 3)
    ram_percent = ram.percent
    disk = psutil.disk_usage('/')
    disk_total = disk.total / (1024 ** 3)
    disk_used = disk.used / (1024 ** 3)
    disk_percent = disk.percent
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_time_timestamp)
    uptime = datetime.now() - boot_time
    uptime_str = str(uptime).split('.')[0]
    uname = platform.uname()
    text = f"""🖥️ **معلومات السيرفر:**

- نظام التشغيل: {uname.system} {uname.release}
- اسم الجهاز: {uname.node}
- نسخة النظام: {uname.version}
- نوع المعالج: {uname.processor}
- عدد الأنوية: {cpu_count}
- استخدام CPU: {cpu_percent}%

💾 **الرام:**
- الكلي: {ram_total:.2f} GB
- المستخدم: {ram_used:.2f} GB
- النسبة: {ram_percent}%

🗄️ **مساحة القرص:**
- الكلي: {disk_total:.2f} GB
- المستخدم: {disk_used:.2f} GB
- النسبة: {disk_percent}%

⏱️ **زمن التشغيل:** {uptime_str}
"""
    await message.reply(text)



@app.on_message(filters.regex(r"^سرعة السيرفر 🚀$"))
async def speed_test(client, message):
    msg = await message.reply("⏳ جارِ قياس سرعة الانترنت...")
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000  
        ping = st.results.ping
        text = f"""🌐 **نتيجة اختبار سرعة الانترنت:**
📥 سرعة التحميل: {download_speed:.2f} Mbps
📤 سرعة الرفع: {upload_speed:.2f} Mbps
🏓 زمن الاستجابة (Ping): {ping} ms
"""
        await msg.edit(text)
    except Exception as e:
        await msg.edit(f"⚠️ فشل في قياس سرعة الانترنت.\n\n{e}")


@app.on_message(filters.regex(r"^الاصدار ⚙️$"))
async def show_version(client, message):
    version_info = """
    🚀 **إصدار البوت الحالي** 
    
    ✨ **الإصدار:** 2
    📅 **تاريخ التحديث:** 2023-12-01
    🔒 **الحالة:** نشط
    
    🔄 آخر التحديثات:
    - تحسين أداء النظام
    - إصلاح الأخطاء المعروفة
    """
    await message.reply(version_info)

@app.on_message(filters.regex(r"^تحديث السورس 📥$"))
async def update_source(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return await message.reply("⚠️ هذا الأمر متاح للمطورين فقط!")
    progress_msg = await message.reply("🔄 **جاري تحديث السورس...**")    
    for i in range(1, 4):
        await asyncio.sleep(1)
        await progress_msg.edit(f"🔄 **جاري تحديث السورس...** {i*25}%")
    await asyncio.sleep(1)
    await progress_msg.edit("✅ **تم التحديث بنجاح!**\n\n✨ تم تحديث السورس إلى أحدث إصدار")

@app.on_message(filters.regex(r"^رستر البوت ♻️$"))
async def restart_bot(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return await message.reply("⚠️ هذا الأمر متاح للمطورين فقط!")
    warning_msg = await message.reply("""
⚠️ **تحذير: إعادة تشغيل البوت**
    
هل أنت متأكد من أنك تريد إعادة تشغيل البوت؟
""", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ نعم", callback_data="confirm_restart")],
        [InlineKeyboardButton("❌ إلغاء", callback_data="cancel_restart")]
    ]))

@app.on_callback_query(filters.regex("^confirm_restart$"))
async def confirm_restart(client, callback):
    progress_msg = await callback.message.edit("🔄 **جاري إعادة التشغيل...**")
    for i in range(3):
        await asyncio.sleep(1)
        await progress_msg.edit(f"🔄 **جاري إعادة التشغيل...** {'🟢'*(i+1)}")    
    await progress_msg.edit("✅ **تم إعادة التشغيل بنجاح!**\n\nالبوت الآن يعمل بشكل طبيعي")

@app.on_callback_query(filters.regex("^cancel_restart$"))
async def cancel_restart(client, callback):
    await callback.message.edit("✅ **تم إلغاء عملية إعادة التشغيل**")

@app.on_message(filters.regex("يشسيشسيشسيشسيشيشس"), group=7113)
async def set_bot_name(client, message):
    global source_devv
    if message.from_user.id in dev or message.from_user.id == OWNER_ID or message.from_user.id == sourse_dev:
        ask = await app.ask(message.chat.id, "ارسل يوزر مطور السورس بدون علامه@", timeout=300)
        source_devv = ask.text
        await message.reply_text("تم تعيين يوزر مطور السورس",disable_web_page_preview=True)
    else:
        await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**",disable_web_page_preview=True)
       
@app.on_message(filters.regex("تعيين قناة السورس 📣"), group=71113)
async def set_bot_channel_source(client, message):
    global channel_source
    if get_premium_status() and message.from_user.id == OWNER_ID or message.from_user.id in dev or message.from_user.id == sourse_dev:
        if message.from_user.id in dev or message.from_user.id == OWNER_ID or message.from_user.id == sourse_dev:
            ask = await app.ask(message.chat.id, "**◍ ارسل رابط قناة السورس 📢\n√**", timeout=300)
            channel_source = ask.text
            await message.reply_text("**◍ تم تعيين قناة السورس بنجاح ⚡️\n√**",disable_web_page_preview=True)
        else:
            await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**",disable_web_page_preview=True)
    else:
        await message.reply_text(f"****◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√****")

@app.on_message(filters.regex("تعيين جروب السورس 👥"), group=71213)
async def set_bot_gr(client, message):
    global gr
    if get_premium_status() and message.from_user.id == OWNER_ID or message.from_user.id in dev or message.from_user.id == sourse_dev:
        if message.from_user.id in dev or message.from_user.id == OWNER_ID or message.from_user.id == sourse_dev:
            ask = await app.ask(message.chat.id, "**◍ ارسل رابط جروب السورس 👥\n√**", timeout=300)
            gr = ask.text
            await message.reply_text("**◍ تم تعيين جروب السورس بنجاح ⚡️\n√**",disable_web_page_preview=True)
        else:
            await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**",disable_web_page_preview=True)
    else:
        await message.reply_text(f"****◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√****")

@app.on_message(filters.regex("بسششسيبسبس"), group=712513)
async def set_bot_photo_source(client, message):
    global photo_source
    if message.from_user.id in dev or message.from_user.id == OWNER_ID or message.from_user.id == sourse_dev:
        ask = await app.ask(message.chat.id, f"ارسل لان رابط تليجراف ميديا مثال  {photo_source}", timeout=300)
        photo_source = ask.text
        await message.reply_text("تم تعيين لوجو السورس",disable_web_page_preview=True)
    else:
        await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**",disable_web_page_preview=True)

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def gen_ot(CASER, message):
    try:
        bot_chat = await app.get_chat(bot_id)
        CASR = bot_chat.username 
        owner_chat = await app.get_chat(OWNER_ID)
        CASER = owner_chat.username 
        if bot_chat.photo:
            original_image = Image.open(f"{photo_bot}")
            resized_image = original_image.resize((1280, 720))
            background = resized_image.convert("RGBA").filter(ImageFilter.BoxBlur(5))
            enhancer = ImageEnhance.Brightness(background)
            background = enhancer.enhance(0.6)
            Xcenter, Ycenter = original_image.width / 2, original_image.height / 2
            crop_box = (Xcenter - 250, Ycenter - 250, Xcenter + 250, Ycenter + 250)
            logo = original_image.crop(crop_box)
            logo.thumbnail((520, 520), Image.LANCZOS)
            logo = ImageOps.expand(logo, border=15, fill="white")
            background.paste(logo, (50, 100))
            draw = ImageDraw.Draw(background)
            font_large = ImageFont.truetype("font2.ttf", 70)
            font_medium = ImageFont.truetype("font2.ttf", 45)
            font_small = ImageFont.truetype("font2.ttf", 40)
            users_count, groups_count, channels_count = get_stats()
            draw.text((600, 150), "🎵 Music Player BoT 🎵", fill="white", stroke_width=2, stroke_fill="white", font=font_large)
            draw.text((600, 280), "🎧 Playing Music & Video 🎥", fill="white", stroke_width=2, stroke_fill="white", font=font_medium)
            draw.text((600, 340), f"👨‍💻 Dev : {co_dev_name}", fill="white", stroke_width=2, stroke_fill="white", font=font_medium)
            draw.text((600, 400), f"👤 Users : {users_count}", fill="white", stroke_width=2, font=font_small)
            draw.text((600, 450), f"💬 Chats : {groups_count}", fill="white", stroke_width=2, font=font_small)
            draw.text((600, 500), f"📢 Groups : {channels_count}", fill="white", stroke_width=2, font=font_small)
            draw.text((600, 550), f"🤖 Bot : t.me/{CASR}", fill="white", stroke_width=2, font=font_small)
            output_filename = f"{CASER}.png"
            background.save(output_filename)
            return output_filename
    except Exception as e:
        print(f"An error occurred: {e}")


@app.on_message(filters.command(["/start", "رجوع 🔙"], "") & filters.private, group=1201676)
async def for_users(app, message):
    global channel_source, photo_source, channel_userss
    bot_username = (await app.get_me()).username
    CASER = bot_username
    photo = await gen_ot(CASER, message)
    try:
        if message.from_user.id in dev or message.from_user.id == sourse_dev:
            await message.reply_text(f"مرحبا بك مطور السورس {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keyboarddev)
            return
        elif message.from_user.id == OWNER_ID:
            await message.reply_text(f'💌╖أهلا بك عزيزي المطور `{message.from_user.mention}`\n🕹╢ تقدر تتحكم في بوتك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة السورس <a href="https://t.me/uu_u_e">دوس هنا</a>', reply_markup=Keyboarddev)
            return
        else:
            is_subscribed = await check_chat_member_status(message.from_user.id, message, app)
            if not is_subscribed:
                return False
            await message.reply_photo(
                photo=photo,
                caption=f"""
✎﹏﹏Source ✘ 𝙼𝙰𝚁𝙻𝙾𝚆 ♪

 ╮⦿ اهـلا بڪ عزيـزي ⁽ {message.from_user.mention} ₎  
 │⎋ آنا بـوت لتشغيـل الموسيقـي والفيديـو 
 │⎋ البـوت يدعـم القنـوآت والمجموعـآت 
 │⎋ أضِـف البـوت إلـى مجموعتـڪ وارفعـه ( مشـرف) 
 │⎋ سيتـم التفعيـل تلقائـي وانضمـام المساعـد 
 ╯⦿ قنـاة سـورس مارلو : ❲ @{channel_userss} ❳ 

 ⍟ 𝗧𝗛𝗘 𝗕𝗘𝗦𝗧 𝗦𝗢𝗨𝗥𝗖𝗘 𝗢𝗡 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗠
""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗦𝗼𝘂𝗿𝗰𝗲", url=f"{channel_source}"),
                            InlineKeyboardButton("𝗚𝗿𝗼𝘂𝗽 𝗦𝗼𝘂𝗿𝗰𝗲", url=f"{gr}"),
                        ],
                        [
                            InlineKeyboardButton("𝗗𝗲𝘃 𝗦𝗼𝘂𝗿𝗰𝗲 ™", url=f"https://t.me/{source_devv}")
                        ],
                        [
                            InlineKeyboardButton("𝗕𝗼𝘁 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿", url=f"https://t.me/{OWNER_ID}")
                        ],
                        [
                            InlineKeyboardButton("اضف البوت الى مجموعتك ✅", url=f"https://t.me/{appusername}?startgroup=new"),
                        ],
                    ]
                )
            )
            kep = ReplyKeyboardMarkup([["السورس🚦"], ["المطور 👨🏻‍💻", "مطور السورس 🕵🏻‍♂️"], ["اقتباس 💬", "قران 🕋"], ["تويت 🕊", "صراحة 💭"], ["متحركه 🎬", "استوريهات 📱"], ["أعلام 🇪🇬", "ممثلين 🕺🏻"], ["مشاهير 🎩", "فزورة 🎭"], ["نكتة 😹", "المختلف 🧠"], ["لاعبين ⛹🏻‍♂️", "مغنين 👨‍🎤"], ["صور 🖼", "انمي 🪭"], ["صور بنات 🧚🏻‍♀️", "صور شباب 🧜🏻‍♂️"]], resize_keyboard=True)
            await message.reply_text("** صلي علي النبي محمد ❤️ **",reply_markup=kep)
    except Exception as e:
        pass
       

#..................................................... تواصل ...........................................


twaseeel = False

@app.on_message(filters.command(["تفعيل التواصل ⚡️"], "") & filters.private, group=713877765578)
async def hable_twasell(client, message):
    if message.from_user.id in dev or message.from_user.id == sourse_dev or message.from_user.id == OWNER_ID:
        global twaseeel
        twaseeel = True
        await app.send_message(message.chat.id, f"**◍ تم تفعيل التواصل بنجاح 📱\n√**")
    else:
        pass

@app.on_message(filters.command(["تعطيل التواصل 🔰"], "") & filters.private, group=713977578)
async def yble_twasell(client, message):
    if message.from_user.id in dev or message.from_user.id == sourse_dev or message.from_user.id == OWNER_ID:
        global twaseeel
        twaseeel = False
        await app.send_message(message.chat.id, f"**◍ تم تعطيل التواصل بنجاح 📲\n√**")
    else:
        await app.send_message(message.chat.id, f"ليس لديك صلاحيه")
        pass


@app.on_message(filters.private, group=459)
async def twasel(client: Client, message: Message):

    if twaseeel == False:
        return
    
    if message.from_user.id not in [OWNER_ID, zombie_id, sourse_dev]:
        await message.forward(OWNER_ID)

    if message.from_user.id == OWNER_ID:
        if message.reply_to_message:
            if message.reply_to_message.forward_from:
                await message.reply(f"◍ تم إرسال رسالتك إلى {message.reply_to_message.forward_from.first_name} بنجاح", quote=True)
                try:
                    await message.copy(message.reply_to_message.forward_from.id)
                except:
                    pass

#..................................................... تواصل ...........................................

#..................................................... مستخدمين ...........................................
users_collection = db[f"users_{BOT_USERNAME}"]

if not users_collection.find_one({"_id": "bot_stats"}):
    users_collection.insert_one({"_id": "bot_stats", "total_users": 0})

def update_user_count():
    total_users = users_collection.count_documents({"_id": {"$ne": "bot_stats"}})
    users_collection.update_one({"_id": "bot_stats"}, {"$set": {"total_users": total_users}})

@app.on_message(filters.text & filters.private, group=625447854)
async def users_me(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    first_name = message.from_user.first_name
    existing_user = users_collection.find_one({"user_id": user_id})
    if not existing_user:
        users_collection.insert_one({"user_id": user_id, "first_name": first_name})
        update_user_count()
        total_users = users_collection.find_one({"_id": "bot_stats"})["total_users"]
        text = (
            f"🙍 **شخص جديد دخل الى البوت!**\n\n"
            f"🎯 **الاسم:** {first_name}\n"
            f"♻️ **الايدي:** `{user_id}`\n\n"
            f"🌐 **أصبح عدد المستخدمين:** {total_users}"
        )
        await client.send_message(OWNER_ID, text)

@app.on_message(filters.command(["اذاعة للمستخدمين 👤"], "") & filters.private, group=544444544)
async def broadcaast_users_message(client, message):
    if message.from_user.id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply("**◍ عذرا عزيزي ليس لديك صلاحية للاذاعة 🚦\n√**")
    ask = await client.ask(message.chat.id, "**◍ ارسل النص المراد اذاعته 📝\n√**", timeout=300)
    text = ask.text
    ask = await client.ask(message.chat.id, "**◍ اذا كنت تريد الاذاعة بالتثبيت ارسل `نعم` ✅\n√**", timeout=300)
    pin_message = ask.text.lower() == "نعم"
    users = users_collection.find({"_id": {"$ne": "bot_stats"}})
    for user in users:
        user_id = user["user_id"]
        try:
            msg = await client.send_message(user_id, text)
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
        except Exception as e:
            print(f"Error sending message to user {user_id}: {e}")
    await message.reply("✅ تم إرسال الإذاعة لجميع المستخدمين!")

@app.on_message(filters.command(["اذاعة بالتوجية للمستخدمين 〽️"], "") & filters.private, group=548178744544)
async def broadcast_mese_message(client, message):
    if message.from_user.id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply("**◍ عذرا عزيزي ليس لديك صلاحية للاذاعة 🚦\n√**")
    forwarded_message = await client.ask(message.chat.id, "**◍ ارسل الرسالة الموجهة الآن 🚦\n√**", timeout=300)
    if not forwarded_message:
        return await message.reply("❌ لم يتم إرسال أي رسالة.")
    users = users_collection.find({"_id": {"$ne": "bot_stats"}})
    for user in users:
        user_id = user["user_id"]
        try:
            await forwarded_message.forward(user_id)
        except Exception as e:
            print(f"Error forwarding message to {user_id}: {e}")
    await message.reply("✅ تم إرسال الإذاعة لجميع المستخدمين!")
    
#.............................................. مستخدمين ...........................................


#.............................................. جروبات ...........................................

groups_collection = db[f"groups_{BOT_USERNAME}"]


if not groups_collection.find_one({"_id": "bot_stats"}):
    groups_collection.insert_one({"_id": "bot_stats", "total_groups": 0})

def update_group_count():
    total_groups = groups_collection.count_documents({"_id": {"$ne": "bot_stats"}})
    groups_collection.update_one({"_id": "bot_stats"}, {"$set": {"total_groups": total_groups}})

@app.on_message(filters.text & filters.group, group=625414788854)
async def groupsss_me(client, message):
    group_id = message.chat.id
    group_name = message.chat.title
    if not groups_collection.find_one({"group_id": group_id}):
        groups_collection.insert_one({"group_id": group_id, "group_name": group_name})
        update_group_count()
        text = f"✅ تم تفعيل البوت في مجموعة جديدة\n\n"
        text += f"🏷 اسم المجموعة: {group_name}\n"
        if message.chat.username:
            text += f"🔗 رابط المجموعة: https://t.me/{message.chat.username}\n"
        text += "\n👤 معلومات الشخص الذي قام بالتفعيل:\n"
        text += f"◍ الاسم: {message.from_user.mention}\n"
        text += f"◍ الايدي: {message.from_user.id}\n"
        text += f"\n📊 عدد الجروبات الآن: {groups_collection.count_documents({'_id': {'$ne': 'bot_stats'}})}"
        await client.send_message(OWNER_ID, text)

@app.on_message(filters.command(["اذاعة للجروبات 👥"], "") & filters.private, group=512531544)
async def broadcast_groups_message(client, message):
    if message.from_user.id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply("**◍ عذرا عزيزي ليس لديك صلاحية للاذاعة 🚦\n√**")
    ask = await client.ask(message.chat.id, "**◍ ارسل النص المراد اذاعته 📝\n√**", timeout=300)
    text = ask.text
    ask = await client.ask(message.chat.id, "**◍ اذا كنت تريد الاذاعة بالتثبيت ارسل `نعم` ✅\n√**", timeout=300)
    pin_message = ask.text.lower() == "نعم"
    groups = groups_collection.find({"_id": {"$ne": "bot_stats"}})
    for group in groups:
        group_id = group["group_id"]
        try:
            msg = await client.send_message(group_id, text)
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
        except Exception as e:
            print(f"Error sending message to group {group_id}: {e}")
    await message.reply("✅ تم إرسال الإذاعة لجميع الجروبات!")

@app.on_message(filters.command(["اذاعة بالتوجية للجروبات 🔂"], "") & filters.private, group=5497828544)
async def broadcast_forward_groups(client, message):
    if message.from_user.id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply("**◍ عذرا عزيزي ليس لديك صلاحية للاذاعة 🚦\n√**")
    forwarded_message = await client.ask(message.chat.id, "**◍ ارسل الرسالة الموجهة الآن 🚦\n√**", timeout=300)
    if not forwarded_message:
        return await message.reply("❌ لم يتم إرسال أي رسالة.")
    groups = groups_collection.find({"_id": {"$ne": "bot_stats"}})
    for group in groups:
        group_id = group["group_id"]
        try:
            await forwarded_message.forward(group_id)
        except Exception as e:
            print(f"Error forwarding message to group {group_id}: {e}")
    await message.reply("✅ تم إرسال الإذاعة لجميع الجروبات!")
#.............................................. جروبات ...........................................


#------------------------------------------------ القنوات ------------------------------------------------


channels_collection = db[f"channels_{BOT_USERNAME}"]

if not channels_collection.find_one({"_id": "bot_stats"}):
    channels_collection.insert_one({"_id": "bot_stats", "total_channels": 0})

def update_channel_count():
    total_channels = channels_collection.count_documents({"_id": {"$ne": "bot_stats"}})
    channels_collection.update_one({"_id": "bot_stats"}, {"$set": {"total_channels": total_channels}})

@app.on_message(filters.text & filters.channel, group=625454)
async def channel_group(client, message):
    chat_id = message.chat.id
    chat_title = message.chat.title

    if not channels_collection.find_one({"channel_id": chat_id}):
        channels_collection.insert_one({"channel_id": chat_id, "channel_name": chat_title})
        update_channel_count()
        text = f"✅ تم إضافة البوت إلى قناة جديدة\n\n"
        text += f"🏷 اسم القناة: {chat_title}\n"
        if message.chat.username:
            text += f"🔗 رابط القناة: https://t.me/{message.chat.username}\n"
        text += f"\n📊 عدد القنوات الآن: {channels_collection.count_documents({'_id': {'$ne': 'bot_stats'}})}"
        await client.send_message(OWNER_ID, text)

@app.on_message(filters.command(["اذاعة للقنوات 📢"], "") & filters.private, group=54544)
async def broadcast_channels_message(client, message):
    if message.from_user.id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply("**◍ عذرا عزيزي ليس لديك صلاحية للاذاعة 🚦\n√**")
    ask = await client.ask(message.chat.id, "**◍ ارسل النص المراد اذاعته 📝\n√**", timeout=300)
    text = ask.text
    ask = await client.ask(message.chat.id, "**◍ اذا كنت تريد الاذاعة بالتثبيت ارسل `نعم` ✅\n√**", timeout=300)
    pin_message = ask.text.lower() == "نعم"
    channels = channels_collection.find({"_id": {"$ne": "bot_stats"}})
    for channel in channels:
        channel_id = channel["channel_id"]
        try:
            msg = await client.send_message(channel_id, text)
            if pin_message:
                await msg.pin(disable_notification=False)
        except Exception as e:
            print(f"Error sending message to channel {channel_id}: {e}")
    await message.reply("✅ تم إرسال الإذاعة لجميع القنوات!")

@app.on_message(filters.command(["اذاعة بالتوجية للقنوات 🧭"], "") & filters.private, group=548787544)
async def broadcast_forward_channels(client, message):
    if message.from_user.id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply("**◍ عذرا عزيزي ليس لديك صلاحية للاذاعة 🚦\n√**")
    forwarded_message = await client.ask(message.chat.id, "**◍ ارسل الرسالة الموجهة الآن 🚦\n√**", timeout=300)
    if not forwarded_message:
        return await message.reply("❌ لم يتم إرسال أي رسالة.")
    channels = channels_collection.find({"_id": {"$ne": "bot_stats"}})
    for channel in channels:
        channel_id = channel["channel_id"]
        try:
            await forwarded_message.forward(channel_id)
        except Exception as e:
            print(f"Error forwarding message to channel {channel_id}: {e}")
    await message.reply("✅ تم إرسال الإذاعة لجميع القنوات!")

@app.on_message(filters.command(["ترويج للميوزك 🎸", "ترويج الميوزك"], ""), group=1588024)
async def promote_music_bot(client, message):
    bot_username = client.me.username
    bot_mention = client.me.mention
    owner = await client.get_chat(OWNER_ID)
    owner_username = owner.username
    pin_buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("نعم بالتثبيت ✅", callback_data="pin_yes")],
        [InlineKeyboardButton("لا بدون تثبيت ❌", callback_data="pin_no")]
    ])
    await message.reply_text(
        "**هل تريد تثبيت رسالة الترويج في المجموعات والقنوات؟**",
        reply_markup=pin_buttons
    )

@app.on_callback_query(filters.regex("^pin_(yes|no)$"))
async def handle_pin_choice(client, callback_query):
    choice = callback_query.data.split("_")[1]
    pin_message = (choice == "yes")
    channels = channels_collection.find({"_id": {"$ne": "bot_stats"}})
    groups = groups_collection.find({"_id": {"$ne": "bot_stats"}})
    users = users_collection.find({"_id": {"$ne": "bot_stats"}})
    await callback_query.message.edit_text("جاري بدء الترويج...")    
    owner = await client.get_chat(OWNER_ID)
    owner_username = owner.username
    promotion_text = f"""**
    اقوي بوت ميوزك قنوات و جروبات سرعه وجوده خارقه وبدون تهنيج او تقطيع او توقف وكمان ان البوت في مميزات جامدة⚡️♥️.
    
    ارفع البوت ادمن فقناتك او جروبك واستمتع بجوده الصوت و السرعه الخياليه للبوت ⚡️♥️

    معرف البوت 🎸  [ @{BOT_USERNAME}]
    ➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 ♩🎸 
    
    -𝙱𝙾𝚃 ➤ @{BOT_USERNAME}
    -𝙳𝙴𝚅 ➤ @{owner_username}
    **"""    
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("أضف البوت إلى مجموعتك أو قناتك ❤️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
    ])
    sent_groups = 0
    sent_users = 0
    sent_channels = 0
    for group in groups:
        try:
            msg = await client.send_message(
                group["group_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
            sent_groups += 1
        except Exception as e:
            pass
    
    # إرسال للأشخاص
    for user in users:
        try:
            msg = await client.send_message(
                user["user_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
            sent_users += 1
        except Exception as e:
            pass
    
    # إرسال للقنوات
    for channel in channels:
        try:
            msg = await client.send_message(
                channel["channel_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False)
            sent_channels += 1
        except Exception as e:
            pass
    result_message = f"""
**✅ تم الانتهاء من الترويج بنجاح**

◍ عدد المجموعات: {sent_groups}
◍ عدد الأشخاص: {sent_users}
◍ عدد القنوات: {sent_channels}
◍ التثبيت: {"✅ مفعل" if pin_message else "❌ غير مفعل"}
    
**المجموع الكلي: {sent_groups + sent_users + sent_channels} رسالة**
    """
    
    await callback_query.message.edit_text(result_message)
    await callback_query.answer(f"تم الترويج بنجاح في {sent_groups + sent_users + sent_channels} مكان")

@app.on_message(filters.command(["ترويج الحماية", "ترويج للحماية 🛡"], ""), group=158024)
async def prom_music_bot(client, message):
    bot_username = client.me.username
    bot_mention = client.me.mention
    owner = await client.get_chat(OWNER_ID)
    owner_username = owner.username
    pin_buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("نعم بالتثبيت ✅", callback_data="pi_yes")],
        [InlineKeyboardButton("لا بدون تثبيت ❌", callback_data="pi_no")]
    ])
    await message.reply_text(
        "**هل تريد تثبيت رسالة الترويج في المجموعات والقنوات؟**",
        reply_markup=pin_buttons
    )

@app.on_callback_query(filters.regex("^pi_(yes|no)$"))
async def handle_picoice(client, callback_query):
    choice = callback_query.data.split("_")[1]
    pin_message = (choice == "yes")
    channels = channels_collection.find({"_id": {"$ne": "bot_stats"}})
    groups = groups_collection.find({"_id": {"$ne": "bot_stats"}})
    users = users_collection.find({"_id": {"$ne": "bot_stats"}})
    await callback_query.message.edit_text("جاري بدء الترويج...")    
    owner = await client.get_chat(OWNER_ID)
    owner_username = owner.username
    promotion_text = f"""**
- البوت ده من افضل بوتات التليجرام الموجوده

البوت دا يقدر يحمي مجموعتك او قناتك من كل انواع الازعاج 

تقدر من خلال اوامر البوت تمنع الحاجات دي 

- الروابط - الاباحي - التوجيه - الاسائه - الميديا 

- منع التوجيه تحذف الاستوري أيضاً 

- بالاضافه الي منع التصفيه مفعله تلقائياً 

تكتب الامر وتختار العقوبه المناسبه وتحدد بعد كدا العقوبه هتكون لمين

معرف البوت 🎸  [ @{BOT_USERNAME}]

➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 ♩🎸 

-𝙱𝙾𝚃 ➤ @{BOT_USERNAME}
-𝙳𝙴𝚅 ➤ @{owner_username}
    **"""    
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("أضف البوت إلى مجموعتك أو قناتك ❤️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
    ])
    sent_groups = 0
    sent_users = 0
    sent_channels = 0
    for group in groups:
        try:
            msg = await client.send_message(
                group["group_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
            sent_groups += 1
        except Exception as e:
            pass
    
    # إرسال للأشخاص
    for user in users:
        try:
            msg = await client.send_message(
                user["user_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
            sent_users += 1
        except Exception as e:
            pass
    
    # إرسال للقنوات
    for channel in channels:
        try:
            msg = await client.send_message(
                channel["channel_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False)
            sent_channels += 1
        except Exception as e:
            pass
    result_message = f"""
**✅ تم الانتهاء من الترويج بنجاح**

◍ عدد المجموعات: {sent_groups}
◍ عدد الأشخاص: {sent_users}
◍ عدد القنوات: {sent_channels}
◍ التثبيت: {"✅ مفعل" if pin_message else "❌ غير مفعل"}
    
**المجموع الكلي: {sent_groups + sent_users + sent_channels} رسالة**
    """
    
    await callback_query.message.edit_text(result_message)
    await callback_query.answer(f"تم الترويج بنجاح في {sent_groups + sent_users + sent_channels} مكان")

@app.on_message(filters.command(["ترويج الاذان", "ترويج للاذان 🕌"], ""), group=158023424)
async def p_music_bot(client, message):
    bot_username = client.me.username
    bot_mention = client.me.mention
    owner = await client.get_chat(OWNER_ID)
    owner_username = owner.username
    pin_buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("نعم بالتثبيت ✅", callback_data="pai_yes")],
        [InlineKeyboardButton("لا بدون تثبيت ❌", callback_data="pai_no")]
    ])
    await message.reply_text(
        "**هل تريد تثبيت رسالة الترويج في المجموعات والقنوات؟**",
        reply_markup=pin_buttons
    )

@app.on_callback_query(filters.regex("^pai_(yes|no)$"))
async def hndle_picoice(client, callback_query):
    choice = callback_query.data.split("_")[1]
    pin_message = (choice == "yes")
    channels = channels_collection.find({"_id": {"$ne": "bot_stats"}})
    groups = groups_collection.find({"_id": {"$ne": "bot_stats"}})
    users = users_collection.find({"_id": {"$ne": "bot_stats"}})
    await callback_query.message.edit_text("جاري بدء الترويج...")    
    owner = await client.get_chat(OWNER_ID)
    owner_username = owner.username
    promotion_text = f"""**
- البوت ده من افضل بوتات التليجرام الموجوده

من اهم اوامر البوت امر »»  تفعيل الاذان

تكتب تفعيل الاذان في المحادثه المطلوبه 
والبوت هيبعتلك تنبيه بتوقيت كل صلاة ويطلع الكول يشغل اذان بصوت شيوخ مختلفه

معرف البوت 🎸  [ @{BOT_USERNAME}]

➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 ♩🎸 

-𝙱𝙾𝚃 ➤ @{BOT_USERNAME}
-𝙳𝙴𝚅 ➤ @{owner_username}
    **"""    
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("أضف البوت إلى مجموعتك أو قناتك ❤️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
    ])
    sent_groups = 0
    sent_users = 0
    sent_channels = 0
    for group in groups:
        try:
            msg = await client.send_message(
                group["group_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
            sent_groups += 1
        except Exception as e:
            pass
    
    # إرسال للأشخاص
    for user in users:
        try:
            msg = await client.send_message(
                user["user_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
            sent_users += 1
        except Exception as e:
            pass
    
    # إرسال للقنوات
    for channel in channels:
        try:
            msg = await client.send_message(
                channel["channel_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False)
            sent_channels += 1
        except Exception as e:
            pass
    result_message = f"""
**✅ تم الانتهاء من الترويج بنجاح**

◍ عدد المجموعات: {sent_groups}
◍ عدد الأشخاص: {sent_users}
◍ عدد القنوات: {sent_channels}
◍ التثبيت: {"✅ مفعل" if pin_message else "❌ غير مفعل"}
    
**المجموع الكلي: {sent_groups + sent_users + sent_channels} رسالة**
    """
    
    await callback_query.message.edit_text(result_message)
    await callback_query.answer(f"تم الترويج بنجاح في {sent_groups + sent_users + sent_channels} مكان")

@app.on_message(filters.command(["ترويج السماح بالتحدث", "ترويج السماح بالتحدث 🗣"], ""), group=1893424)
async def psic_bot(client, message):
    bot_username = client.me.username
    bot_mention = client.me.mention
    owner = await client.get_chat(OWNER_ID)
    owner_username = owner.username
    pin_buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("نعم بالتثبيت ✅", callback_data="paai_yes")],
        [InlineKeyboardButton("لا بدون تثبيت ❌", callback_data="paai_no")]
    ])
    await message.reply_text(
        "**هل تريد تثبيت رسالة الترويج في المجموعات والقنوات؟**",
        reply_markup=pin_buttons
    )

@app.on_callback_query(filters.regex("^paai_(yes|no)$"))
async def hle_picoice(client, callback_query):
    choice = callback_query.data.split("_")[1]
    pin_message = (choice == "yes")
    channels = channels_collection.find({"_id": {"$ne": "bot_stats"}})
    groups = groups_collection.find({"_id": {"$ne": "bot_stats"}})
    users = users_collection.find({"_id": {"$ne": "bot_stats"}})
    await callback_query.message.edit_text("جاري بدء الترويج...")    
    owner = await client.get_chat(OWNER_ID)
    owner_username = owner.username
    promotion_text = f"""**
- البوت ده من افضل بوتات التليجرام الموجوده

من الاوامر المخصصه للقنوات 
امر »» السماح بالتحدث 
تكتب السماح بالتحدث في القناة المطلوبه 
وتلقائي البوت بيفك ميوت للناس الي بتطلع الكول

معرف البوت 🎸  [ @{BOT_USERNAME}]

➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤𝘦 𝘤𝘩𝘢𝘵𝘴 ♩🎸 

-𝙱𝙾𝚃 ➤ @{BOT_USERNAME}
-𝙳𝙴𝚅 ➤ @{owner_username}
    **"""    
    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("أضف البوت إلى مجموعتك أو قناتك ❤️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
    ])
    sent_groups = 0
    sent_users = 0
    sent_channels = 0
    for group in groups:
        try:
            msg = await client.send_message(
                group["group_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
            sent_groups += 1
        except Exception as e:
            pass
    
    # إرسال للأشخاص
    for user in users:
        try:
            msg = await client.send_message(
                user["user_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
            sent_users += 1
        except Exception as e:
            pass
    
    # إرسال للقنوات
    for channel in channels:
        try:
            msg = await client.send_message(
                channel["channel_id"],
                promotion_text,
                reply_markup=button,
                disable_web_page_preview=True
            )
            if pin_message:
                await msg.pin(disable_notification=False)
            sent_channels += 1
        except Exception as e:
            pass
    result_message = f"""
**✅ تم الانتهاء من الترويج بنجاح**

◍ عدد المجموعات: {sent_groups}
◍ عدد الأشخاص: {sent_users}
◍ عدد القنوات: {sent_channels}
◍ التثبيت: {"✅ مفعل" if pin_message else "❌ غير مفعل"}
    
**المجموع الكلي: {sent_groups + sent_users + sent_channels} رسالة**
    """
    
    await callback_query.message.edit_text(result_message)
    await callback_query.answer(f"تم الترويج بنجاح في {sent_groups + sent_users + sent_channels} مكان")
#------------------------------------------------ القنوات ------------------------------------------------
def get_stats():
    users_count = users_collection.count_documents({"_id": {"$ne": "bot_stats"}})
    groups_count = groups_collection.count_documents({"_id": {"$ne": "bot_stats"}})
    channels_count = channels_collection.count_documents({"_id": {"$ne": "bot_stats"}})
    return users_count, groups_count, channels_count

@app.on_message(filters.command(["● الاحصائيات ●", "الاحصائيات 📊"], "") & filters.private, group=54553153)
async def send_statistics(client, message):
    if message.from_user.id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply("❌ ليس لديك صلاحية!")
    
    users_count, groups_count, channels_count = get_stats()
    bot_username = (await app.get_me()).username
    CASER = bot_username
    photo = await gen_ot(CASER, message)
    text = (
        f"◍ مرحبا بك عزيزي ⸢ {message.from_user.mention} ⸥\n"
        f"◍ هذه هي الاحصائيات الخاصة بي\n"
        f"√"
    )
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"◍ عدد المستخدمين ↦↦ {users_count}", callback_data="stats_users")],
        [InlineKeyboardButton(f"◍ عدد الجروبات ↦↦ {groups_count}", callback_data="stats_groups")],
        [InlineKeyboardButton(f"◍ عدد القنوات ↦↦ {channels_count}", callback_data="stats_channels")],
        [InlineKeyboardButton("اضف البوت الى مجموعتك ✅", url=f"https://t.me/{appusername}?startgroup=new"),],
    ])
    await message.reply_photo(
        photo=photo,
        caption=text,
        reply_markup=keyboard
    )

@app.on_message(filters.command(["سورس","السورس","سورس ⚡️","السورس🚦"], ""), group=54587)
async def khkhjalid(client: Client, message: Message):
    global channel_source, gr, channel_userss, source_devv

    try:
        dev_info = await client.get_chat(source_devv)
        dev_name = dev_info.first_name
        if dev_info.last_name:
            dev_name += f" {dev_info.last_name}"
    except Exception as e:
        dev_name = "المطور"

    await message.reply_video(
        video="https://t.me/uu_u_e/17",
        caption="""⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("ᏟᎻᎪΝΝᎬᏞ", url=f"https://t.me/{channel_source}"),
                InlineKeyboardButton("ᏀᎡØႮᏢ", url=f"https://t.me/{gr}")
            ],
            [
                InlineKeyboardButton(f"{dev_name}", url=f"https://t.me/{source_devv}")
            ],
            [
                InlineKeyboardButton("اضف البوت الى مجموعتك ❤️", url=f"https://t.me/{appusername}?startgroup=new")
            ],
        ]),
    )

collection_premium = db[f"premium_status_{BOT_USERNAME}"]

def set_premium_status(status: bool):
    collection_premium.update_one({}, {"$set": {"premium": status}}, upsert=True)

def get_premium_status():
    premium_data = collection_premium.find_one({})
    return premium_data.get("premium", False) if premium_data else False

        
@app.on_message(filters.command(["الاوامر","اوامر السورس","اوامر البوت"], ""), group=73)
async def kggalid(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⨳ م1", callback_data="m1 " + str(message.from_user.id))] +
        [InlineKeyboardButton("⨳ م2", callback_data="m2 " + str(message.from_user.id))],
        [InlineKeyboardButton("⨳ م3", callback_data="m3 " + str(message.from_user.id))] +
        [InlineKeyboardButton("⨳ م4", callback_data="m4 " + str(message.from_user.id))],
        [InlineKeyboardButton("⨳ م5", callback_data="m5 " + str(message.from_user.id))] +
        [InlineKeyboardButton("⨳ م6", callback_data="m6 " + str(message.from_user.id))],
        [InlineKeyboardButton("⨳ م7", callback_data="m7 " + str(message.from_user.id))],

        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await message.reply_text("""
⚙️╖⁩ ❬ م1 ❭ اوامر حماية المجموعه ⇊
🥳╢ ❬ م2 ❭ اوامر التسليه ⇊
💫╢ ❬ م3 ❭ اوامر الاعضاء ⇊
👮‍♂️╢ ❬ م4 ❭ اوامر اصحاب الرتب ⇊
🚦╢ ❬ م5 ❭  اوامر منع التصفيه ⇊
💎╢ ❬ م6 ❭ اوامر المطورين ⇊
🏦╜ ❬ م7 ❭ اوامر لعبه البنك ⇊
""", reply_markup=keyboard)
   

@app.on_callback_query(filters.regex("^command (\\d+)$"))
async def command(c: Client, m: Message):
    global mid
    mid = m.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⨳ م1", callback_data="m1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م2", callback_data="m2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م3", callback_data="m3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م4", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م5", callback_data="m5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م6", callback_data="m6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م7", callback_data="m7 " + str(m.from_user.id))],

        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.reply_text("""
⚙️╖⁩ ❬ م1 ❭ اوامر حماية المجموعه ⇊
🥳╢ ❬ م2 ❭ اوامر التسليه ⇊
💫╢ ❬ م3 ❭ اوامر الاعضاء ⇊
👮‍♂️╢ ❬ م4 ❭ اوامر اصحاب الرتب ⇊
🚦╢ ❬ م5 ❭  اوامر منع التصفيه ⇊
💎╢ ❬ م6 ❭ اوامر المطورين ⇊
🏦╜ ❬ م7 ❭ اوامر لعبه البنك ⇊
""", reply_markup=keyboard)

@app.on_callback_query(filters.regex("^m7 (\\d+)$"))
async def m7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺️", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
么 [<a href="https://t.me/uu_u_e ">ᏚᎾᏌᎡᏟᎬ mhmad saleh </a>]

🏦 اوامر لعبه البنك ⇊

👮‍♂️ « المطور » ⇊
么 [<a href="https://t.me/uu_u_e ">ᏚᎾᏌᎡᏟᎬ mhmad saleh </a>]\n
➕╖ اضف فلوس + المبلغ «» ❬ بالرد علي الشخص المراد اضافه الفلوس له ❭
🗑╢ حذف حسابه «» ❬ بالرد علي الشخص المراد حذف حسابه ❭
❌╢ حذف حساب + اليوزر «» ❬ لحذف حساب الشخص ❭
😵╜ تصفير البنك «» ❬ لمسح كل الحسابات ❭

👨‍🦳 « الاعضاء » ⇊
么 [<a href="https://t.me/uu_u_e ">ᏚᎾᏌᎡᏟᎬ mhmad saleh </a>]\n
📑╖ انشاء «» فتح حساب بنكي
🤑╢ فلوسي «» اموالي
💸╢ فلوسه «» امواله ❬ بالرد علي الشخص ❭
🏦╢ بنكي «» حسابي
💰╢ بنكه «» حسابه ❬ بالرد علي الشخص ❭
♻️╢ تحويل + المبلغ
☠️╢ كنز
🤖╢ استثمار + المبلغ
🍃╢ حظ + المبلغ
⏫╢ مضاعفه «» مضاربه + المبلغ
🎯╢ عجله الحظ
🤞╢ رشوه
🥺╢ بقشيش
⏳╢ راتب
📎╢ سرقه «» اسرق ❬ بالرد علي الشخص ❭
🚔╢ شرطه «» شرطة ❬ بالرد علي الشخص ❭
⭐️╢ حمايه اموالي «» ❬ لحمايه اموالك من السرقه ❭
👮╢ شرطه + اليوزر
💂‍♀️╢ توب الحراميه «» توب السرقه
⤴️╜ توب الفلوس «» توب فلوس

么 <a href="https://t.me/uu_u_e ">[ᏚᎾᏌᎡᏟᎬ mhmad saleh ]</a>
    """, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^command2 (\\d+)$"))
async def command2(c: Client, m: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⨳ م1", callback_data="m1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م2", callback_data="m2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م3", callback_data="m3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م4", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م5", callback_data="m5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م6", callback_data="m6 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م7", callback_data="m7 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
⚙️╖⁩ ❬ م1 ❭ اوامر حماية المجموعه ⇊
🥳╢ ❬ م2 ❭ اوامر التسليه ⇊
💫╢ ❬ م3 ❭ اوامر الاعضاء ⇊
👮‍♂️╢ ❬ م4 ❭ اوامر اصحاب الرتب ⇊
🚦╢ ❬ م5 ❭  اوامر منع التصفيه ⇊
💎╢ ❬ م6 ❭ اوامر المطورين ⇊
🏦╜ ❬ م7 ❭ اوامر لعبه البنك ⇊
                              
""", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^m1 (\\d+)$"))
async def m1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
⚙️⁩ ❬ م1 ❭ اوامر حماية المجموعه ⇊
════════ ××× ════════ٴ
🔐 ╖ قفل «» فتح + الامر 
⁦♻️⁩ ╜ قفل «» فتح ❬ الكـــل ❭ 
════════ ××× ════════ٴ
📮╖ الدردشه
📜╢ المعرفات
📸╢ الصور
📽️╢ الفيديوهات
🎟╢ الاستيكر
📂╢ الملفات
🎥╢ المتحركه
⏏️╢ الرفع
🔊╢ الريكورد
🎧╢ الصوت
📞╢ الجهات
🔊╢ الترحيب
🚫╢ المغادره
🎧╢ الاغاني
🏨╢ الزخرفه
🍿╢ الافلام
🎬╢ اليوتيوب
💱╢ الترجمه
🔄╢ الردود
🚿╢ التوجيه
🔮╢ الهمسه
🗳️╢ الاشعارات
💳╢ التاج
🧾╢ رابط الحذف
🆔╢ الايدي بالصوره
🔈╢ اطردني
🤔╢ مين ضافني
🏓╢ الالعاب
🎁╢ الروايات
🎆╢ الابراج
🔍╢ معاني الاسماء
💬╜ الترحيب
════════ ××× ════════ٴ
⚠️ ❬ بالكتم, بالطرد ❭
════════ ××× ════════ٴ
🌐╖ الروابط
🔄╢ التوجيه
🍿╢ الفشار
⚜️╢ البوتات
⚠️╜ الممنوعه
════════ ××× ════════ٴ
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^mxx (\\d+)$"))
async def mxx(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اوامر التسليه 1⃣", callback_data="mx1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر التسليه 2⃣", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text(" ◍ اهلا بك فى اوامر التسليه\n√", reply_markup=keyboard)

@app.on_callback_query(filters.regex("^m2 (\\d+)$"))
async def m2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اوامر التسليه 1⃣", callback_data="mx1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر التسليه 2⃣", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text(" ◍ اهلا بك فى اوامر التسليه\n√", reply_markup=keyboard)

@app.on_callback_query(filters.regex("^mx1 (\\d+)$"))
async def mx1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("➡️ التالي", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""🥳╖ ❬ م2 ❭ 1⃣ اوامر التسليه ⇊
🔐╜ رفع «» تنزيل + الامر 
════════ ××× ════════ٴ
🐣╖ متوحد «» متوحده
💬╢ تاج للمتوحدين 
📎╜ مسح المتوحدين
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
💢╖ بقره 
💬╢ تاج للبقرات
📎╜ مسح البقرات
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🐒╖ غبي
💬╢ تاج للاغبيه
📎╜ مسح الاغبيه
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🤪╖ حمار
💬╢ تاج للحمير
📎╜ مسح الحمير
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🐕╖ كلب
💬╢ تاج للكلاب
📎╜ مسح الكلاب
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🐰╖ قرد
💬╢ تاج للقرود
📎╜ مسح القرود
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🤡╖ فرسه
💬╢ تاج للفرسات
📎╜ مسح الفرسات
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🤰╖ عره
💬╢ تاج للعرر
📎╜ مسح العرر
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
👰╖ زوجتي
💬╢ تاج للزوجات
📎╜ مسح المتزوجات
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
👩‍❤️‍👨╖ زواج «» طلاق
💬╢ تاج للمتزوجين 
📎╜ مسح المتزوجين
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
💘╖ رفع بقلبي «» تنزيل من قلبي
💬╢ تاج للي بقلبي
📎╜ مسح من قلبي
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🙊╖ بيستي 
💬╢ تاج للبيست
📎╜ مسح البيستيه
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ

    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^mx2 (\\d+)$"))
async def mx2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""🥳╖ ❬ م2 ❭ 2⃣ اوامر التسليه ⇊
🔐╜ رفع «» تنزيل + الامر 
════════ ××× ════════ٴ
🐣╖ وتكه
💬╢ تاج للوتكات 
📎╜ مسح الوتكات
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
💢╖ رقاصه 
💬╢ تاج للرقاصات
📎╜ مسح الرقاصات
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🐒╖ مهزء
💬╢ تاج للمهزئين
📎╜ مسح المهزئين
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🤪╖ حيوان
💬╢ تاج للحيوانات
📎╜ الحيوانات 
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🐕╖ فاشل
💬╢ تاج للفشله
📎╜ مسح الفشله
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🐰╖ دكري
💬╢ تاج للدكور
📎╜ مسح الدكور
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🤡╖ قطتي
💬╢ تاج للقطط
📎╜ مسح القطط
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🤰╖ ابني
💬╢ تاج للابناء
📎╜ مسح الابناء
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
👰╖ بنتي
💬╢ تاج للبنوتات
📎╜ مسح البنوتات
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
👩‍❤️‍👨╖ حبيبي
💬╢ تاج للحبايب 
📎╜ مسح الحبايب
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
💘╖ زوجي
💬╢ تاج للازواج
📎╜ مسح الازواج
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🙊╖ زوجتي 
💬╢ تاج للزوجات
📎╜ مسح الزوجات
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
👰╖ خاين
💬╢ تاج للخونه
📎╜ مسح الخونه
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
👩‍❤️‍👨╖ خاينه
💬╢ تاج للخاينين 
📎╜ مسح الخاينين
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
💘╖ عبيط
💬╢ تاج للعبط
📎╜ مسح العبط
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🙊╖ متخزوق 
💬╢ تاج للمتخزوقين
📎╜ مسح المتخزوقين
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·

    """, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^m3 (\\d+)$"))
async def m3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
💫 ❬ م3 ❭ اوامر الاعضاء ⇊
════════ ××× ════════ٴ
🎤╖ غنيلي «» حساب العمر
🖼️╢ صورتي «» نسبه جمالي
📸╢ استوري «» رمزيات
📖╢ قرءان
⚙️╢ الاعدادات
🔘╢ نقاطي
⚜️╢ حذف «» بيع ❬ نقاطي ❭
💌╢ رسائلي «» حذف ❬ رسائلي ❭
🔊╢ زخرفه «» اغاني 
🎥╢ افلام «» كارتون
🧭╢ ترجمه + روايات
📼╢ يوتيوب «» العاب
🌡╢ طقس + المنطقة 
🦞╢ الايطالي «» الرابط
🥱╢ اسمي «» الرتبه
💞╢ بحبك «» تتجوزيني
⚕️╢ جهاتي «» حذف جهاتي
☣️╢ صلاحياتي «» بينج
🔉╢ قول + الكلمه
⛔️╢ الكلمات الممنوعه
⭐️╢ انا مين «» انا فين
♻️╢ قول + الكلمه
🐕╢ قطه «» كلب 
💔╢ اطردني «» اكتمني
🌐╢ تاك للاونلاين «» تاك للاعضاء
👨‍🏫╢ سورس «» المطور
♋️╢ الرابط «» ايدي
⬆️╢ رتبتي «» كشف
📊╢ رد  انت يا بوت
🤔╢ اي رايك يابوت
😈╢ هينو «» هينها
💋╢ بوسو «» بوسها
🙊╢ بتحب دي «» بتحب ده
🌀╢ الايطالي
⚠️╜ رابط الحذف
════════ ××× ════════ٴ
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^m4 (\\d+)$"))
async def m4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
👮‍♂️╖ ❬ م4 ❭ اوامر اصحاب الرتب ⇊
⚠️╜ الادمن «» المنشئ «» المالك
════════ ××× ════════ٴ
🥳 « المميز » ⇊
════════ ××× ════════ٴ
🙈╖ كشف
🔇╢ المحظورين
🔕╢ المكتومين
🍿╜ بس كده 😹💔
════════ ××× ════════ٴ
🐣 « الادمن » ⇊
════════ ××× ════════ٴ
🥳╖ رفع مميز «» تنزيل مميز
🙋╢ الترحيب
🤬╢ اضف مغادره «» مسح المغادره
💩╢ رساله المغادره
🤖╢ كشف البوتات
🥳╢ المميزين «» حذف المميزين
🛡╢ حظر «» الغاء حظر
🗡╢ كتم «» الغاء كتم
🗑╢ حظر لمده + المده
🧺╢ كتم لمده + المده
😠╢ طرد «» تطهير 
📌╢ تثبيت «» تثبيت بدون اشعار
🧷╢ الغاء تثبيت الكل
📚╜ ❬ + ❭ جميع ماسبق
════════ ××× ════════ٴ
🤵 « المنشئ » ⇊
════════ ××× ════════ٴ
🐣╖ رفع «» تنزيل ادمن
💌╢ اضف «» حذف  ❬ رد ❭
👨‍🎨╢ الردود «» حذف الردود
🔕╢ ايقاف المنشن
💫╢ تعيين «» مسح  ❬ الايدي ❭
🍫╢ الادمنيه «» حذف الادمنيه
🍻╢ اضف ترحيب
🎲╢ حذف المحظورين «» المكتومين
🎯╢ منع + الكلمه
🚜╢ الغاء منع + الكلمه
🚨╢ حذف الكلمات الممنوعه
🔍╢ المميزين عام
📚╜ ❬ + ❭ جميع ماسبق
════════ ××× ════════ٴ
👮‍♂️ « المالك » ⇊
════════ ××× ════════ٴ
🔼╖ اضف صوره «» وصف (للجروب)
🤵╢ رفع منشئ «» تنزيل منشئ
🔊╢ تاج للاعضاء «» للكل
🔗╢ اضف رابط «» مسح الرابط
🔖╢ اضف «» حذف  ❬ امر ❭
📝╢ الاوامر المضافه
🗑╢ حذف الاوامر المضافه
🔏╢ اضف اسم «» تحديث
🍿╢ المنشئين «» حذف المنشئين
📚╜ ❬ + ❭ جميع ماسبق
════════ ××× ════════ٴ
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^m5 (\\d+)$"))
async def m5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
🚦╢ ❬ م5 ❭  اوامر منع التصفيه ⇊
🤵╜ « المنشئ » ⇊
════════ ××× ════════ٴ
🗣️╢رفع مشرف - تنزيل مشرف 
🔐╢منع التصفيه مفعله تلقائيا
════════ ××× ════════ٴ
🎥 ╢ تلجراف ميديا - رفع ميديا+ميديا +رابط صوره
════════ ××× ════════ٴ
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^m6 (\\d+)$"))
async def m6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
💎╖ ❬ م6 ❭ اوامر المطورين ⇊
👮‍♂️╜ « المطور » ⇊
════════ ××× ════════ٴ
??╖ رفع «» تنزيل ❬ مالك ❭
🔂╢ تغيير رابط الجروب
🔊╢ اذاعه بالمجموعات
👨‍🏭╢ اذاعه بالتوجيه للمجموعات
🤹‍♀╢ اذاعه موجهه بالتثبيت
☀️╢ اذاعه خاص
💘╢ اذاعه بالتوجيه خاص
🎙️╢ اذاعه بالتثبيت
📶╢ جلب نسخه احتياطيه
🏋‍♂╢ رفع نسخه احتياطيه
🍃╢ الاحصائيات
🚷╢ حذف المالكين
📚╜ ❬ + ❭ جميع ماسبق
════════ ××× ════════ٴ
💎 « المطور الاساسي » ⇊
════════ ××× ════════ٴ
📑╖ اضف «» حذف رد عام
🤴╢ رفع «» تنزيل ❬ مميز عام ❭
💎╢ مسح المميزين عام
🗃️╢ الردود العامه
🧨╢ حذف الردود العامه
🛠╢ اذاعه بالتوجيه خاص
🍃╢ اذاعه بالتوجيه للمجموعات
🎯╢ اذاعه بالتثبيت
☀️╢ اذاعه موجهه بالتثبيت
🧲╢ جلب «» رفع ❬نسخه احتياطيه❭
⏳╢ الاحصائيات
🤴╢ رفع «» تنزيل ❬ مطور ❭
🤖╢ المطورين «» حذف المطورين
🔗╢ ضع اسم للبوت
📝╢ تغيير رساله المغادره
🚫╢ حظر «» كتم  ❬ عام ❭
🥺╢ المكتومين  عام 
💔╢ المحظورين عام
♻️╢ الغاء العام
📚╜ ❬ + ❭ جميع ماسبق
════════ ××× ════════ٴ
    """, reply_markup=keyboard)


@app.on_message(filters.command(["🔻 قفل الكيبورد 🔻", "🥺 ¦ حذف الكيبورد"], ""), group=71328934)
async def keplook(client: Client, message):
          m = await message.reply("**- تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية اكتب /start**", reply_markup= ReplyKeyboardRemove(selective=True))
      
@app.on_message(filters.command(["محمد صالح", "المبرمج", "الهكر"], ""), group=9998799787)
async def daeassev(client: Client, message: Message):
    user = await client.get_chat(chat_id=f"7028046857")
    name = user.first_name
    username = user.username
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)
    title = message.chat.title if message.chat.title else message.chat.first_name
    caption = f"""
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐍𝐚𝐦𝐞 : {name} **
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : @{username} **
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐈𝐃 : @{OWNER_ID} **
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐁𝐢𝐨 : {bio} **
**⤶ صلـي علـى النبـۍ وتـبـسم ✨♥️ ≯ -**
    """
    await message.reply_photo(
        photo=photo,
        caption=caption,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]])
    )
    try:
        os.remove(photo)
    except:
        pass

@app.on_message(filters.command(["حمو", "صاحب السورس", "مطور السورس 👨🏻‍💻", "مطور السورس 🕵🏻‍♂️"], ""), group=99987997)
async def daeaev(client: Client, message: Message):
    user = await client.get_chat(chat_id=f"7028046857")
    name = user.first_name
    username = user.username
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)
    title = message.chat.title if message.chat.title else message.chat.first_name
    caption = f"""
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐍𝐚𝐦𝐞 : {name} **
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : @{username} **
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐈𝐃 : @{OWNER_ID} **
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐁𝐢𝐨 : {bio} **
**⤶ صلـي علـى النبـۍ وتـبـسم ✨♥️ ≯ -**
    """
    await message.reply_photo(
        photo=photo,
        caption=caption,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]])
    )
    try:
        os.remove(photo)
    except:
        pass

@app.on_message(filters.command(["المطور", "مطور البوت"], ""), group=7348787)
async def deev(client: Client, message: Message):
    global channel_source, OWNER_ID, gr, photo_source
    user = await client.get_chat(chat_id=f"{int(OWNER_ID)}")
    name = user.first_name
    username = user.username
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)
    link = f"https://t.me/{message.chat.username}"
    title = message.chat.title if message.chat.title else message.chat.first_name
    chat_title = f"👤 User: {message.from_user.mention} \n📛 Chat Name: {title}" if message.from_user else f"📛 Chat Name: {message.chat.title}"
    try:
        await client.send_message(
            username,
            f"⚡ **هناك شخص في حاجة إليك عزيزي المطور**\n{chat_title}\n🔗 **Chat ID**: `{message.chat.id}`",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"🔗 {title}", url=f"{link}")]])
        )
    except:
        pass
    await message.reply_photo(
        photo=photo,
        caption = f"""
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐍𝐚𝐦𝐞 : {name} **
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 : @{username} **
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐈𝐃 : @{OWNER_ID} **
**◈ 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐁𝐢𝐨 : {bio} **
**⤶ صلـي علـى النبـۍ وتـبـسم ✨♥️ ≯ -**
    """,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]])
    )
    try:
        os.remove(photo)
    except:
        pass
        
@app.on_message(filters.command("رتبتي", ""), group=73774717)
async def check_role(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    group_id = message.chat.id
    user_id = str(message.from_user.id)
    user_username = message.from_user.username
    
    if user_id == "7028046857":
        await message.reply("**🎖️ رتبتك: المبرمج محمد صالح شخصياً 🥷✨**")
        return
    
    if user_username in source_devv:
        await message.reply("**🎖️ رتبتك: صاحب السورس شخصياً 👑🔥**")
        return
    
    if user_id == str(OWNER_ID):
        await message.reply("**🎖️ رتبتك: مطور البوت الرئيسي 💻🌟**")
        return

    member = await client.get_chat_member(group_id, int(user_id))

    if member.status == ChatMemberStatus.OWNER:
        await message.reply("**🎖️ رتبتك: مالك المجموعة 👑**")
    elif is_group_creator(group_id, user_id):
        await message.reply("**◍ رتبتك في البوت » منشئ 🛠**")
    elif is_group_owner(group_id, user_id):
        await message.reply("**◍ رتبتك في البوت » مالك 👑**")
    elif is_group_vip(group_id, user_id):
        await message.reply("**◍ رتبتك في البوت » مميز 🌟**")
    elif is_main_developer(user_id):
        await message.reply("**◍ رتبتك في البوت » مطور اساسي 🕵🏻‍♂️**")
    elif is_sub_developer(user_id):
        await message.reply("**◍ رتبتك في البوت » مطور ثانوي 👨🏻‍💻**")
    elif is_group_admin(group_id, user_id):
        await message.reply("**◍ رتبتك في البوت » ادمن 🛡**")
    elif is_manager(group_id, user_id):
        await message.reply("**◍ رتبتك في البوت » مدير 📋**")
    elif member.status == ChatMemberStatus.ADMINISTRATOR:
        await message.reply("**◍ رتبتك في البوت » مشرف عام 🎖**")
    else:
        await message.reply("**رتبتك: عضو عادي 👤**")

@app.on_message(filters.command("رتبته", ""), group=7377894717)
async def checawk_role(client, message: Message):
    target_user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    target_id = str(target_user.id)
    target_username = target_user.username or "بدون معرف"
    group_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    if target_id == "7028046857":
        return await message.reply(f"**🎖️ {target_username} هو: المبرمج محمد صالح شخصياً 🥷✨**")

    if target_username in source_devv:
        return await message.reply(f"**🎖️ {target_username} هو: صاحب السورس شخصياً 👑🔥**")

    if target_id == str(OWNER_ID):
        return await message.reply(f"**🎖️ {target_username} هو: مطور البوت الرئيسي 💻🌟**")

    try:
        member = await client.get_chat_member(group_id, int(target_id))
    except Exception:
        return await message.reply("❌ لم أتمكن من جلب معلومات العضو في المجموعة.")

    if member.status == ChatMemberStatus.OWNER:
        return await message.reply(f"**🎖️ {target_username} هو: مالك المجموعة 👑**")

    if member.status == ChatMemberStatus.ADMINISTRATOR:
        return await message.reply(f"**◍ {target_username} هو: مشرف عام 🎖**")

    if is_group_owner(group_id, target_id):
        return await message.reply(f"**◍ {target_username} هو: مالك 👑**")

    if is_group_creator(group_id, target_id):
        return await message.reply(f"**◍ {target_username} هو: منشئ 🛠**")

    if is_group_admin(group_id, target_id):
        return await message.reply(f"**◍ {target_username} هو: أدمن 🛡**")

    if is_manager(group_id, target_id):
        return await message.reply(f"**◍ {target_username} هو: مدير 📋**")

    if is_main_developer(target_id):
        return await message.reply(f"**◍ {target_username} هو: مطور أساسي 🕵🏻‍♂️**")

    if is_sub_developer(target_id):
        return await message.reply(f"**◍ {target_username} هو: مطور ثانوي 👨🏻‍💻**")

    if is_group_vip(group_id, target_id):
        return await message.reply(f"**◍ {target_username} هو: عضو مميز 🌟**")

    return await message.reply(f"**◍ {target_username} هو: عضو عادي 👤**")

#..........................................  التاك والايدي ................................................................





@app.on_message(filters.command(["◍ احكام ◍"], ""),group=514345)
async def bottttt(client, message):
    selections = [" ※ صورة وجهك او رجلك او خشمك او يدك ؟ ",
" ※ اصدر اي صوت يطلبه منك الاعبين ؟ ",
" ※ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
" ※ روح الى اي قروب عندك في الواتس اب و اكتب اي شيء يطلبه منك الاعبينالحد الاقصى 3 رسائل ؟ ",
" ※ قول نكتة ولازم احد الاعبين يضحك اذا ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
" ※ سمعنا صوتك و غن اي اغنية من اختيار الاعبين الي معك ؟ ",
" ※ ذي المرة لك لا تعيدها ؟ ",
" ※ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
" ※ صور اي شيء يطلبه منك الاعبين ؟ ",
" ※ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
" ※ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
" ※ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوته ؟ ",
" ※ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
" ※ روح عند اي احد بالخاص و قول له انك تحبه و الخ ؟ ",
" ※ اكتب في الشات اي شيء يطلبه منك الاعبين في الخاص ؟ ",
" ※ قول نكتة اذا و لازم احد الاعبين يضحك اذا محد ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
" ※ سامحتك خلاص مافيه عقاب لك  ؟ ",
" ※ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
" ※ غير اسمك الى اسم من اختيار الاعبين الي معك ؟ ",
" ※ اتصل على امك و قول لها انك تحبها  ؟ ",
" ※ لا يوجد سؤال لك سامحتك  ؟ ",
" ※ قل لواحد ماتعرفه عطني كف ؟ ",
" ※ منشن الجميع وقل انا اكرهكم ؟ ",
" ※ اتصل لاخوك و قول له انك سويت حادث و الخ.... ؟ ",
" ※ روح المطبخ و اكسر صحن  ؟ ",
" ※ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوت الكف ؟ ",
" ※ قول لاي بنت موجود في الروم كلمة حلوه ؟ ",
" ※ تكلم باللغة الانجليزية الين يجي دورك مرة ثانية لازم تتكلم اذا ما تكلمت تنفذ عقاب ثاني ؟ ",
" ※ لا تتكلم ولا كلمة الين يجي دورك مرة ثانية و اذا تكلمت يجيك باند لمدة يوم كامل من السيرفر ؟ ",
" ※ قول قصيدة  ؟ ",
" ※ تكلم باللهجة السودانية الين يجي دورك مرة ثانية ؟ ",
" ※ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
" ※ اول واحد تشوفه عطه كف ؟ ",
" ※ سو مشهد تمثيلي عن اي شيء يطلبه منك الاعبين ؟ ",
" ※ سامحتك خلاص مافيه عقاب لك  ؟ ",
" ※ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
" ※ روح اكل ملح + ليمون اذا مافيه اكل اي شيء من اختيار الي معك ؟ ",
" ※ تاخذ عقابين ؟ ",
" ※ قول اسم امك افتخر بأسم امك ؟ ",
" ※ ارمي اي شيء قدامك على اي احد موجود او على نفسك ؟ ",
" ※ اذا انت ولد اكسر اغلى او احسن عطور عندك اذا انتي بنت اكسري الروج حقك او الميك اب حقك ؟ ",
" ※ اذهب الى واحد ماتعرفه وقل له انا كيوت وابي بوسه ؟ ",
" ※ تتصل على الوالدهو تقول لها خطفت شخص ؟ ",
" ※ تتصل على الوالدهو تقول لها تزوجت با سر ؟ ",
" ※ اتصل على الوالدهو تقول لهااحب وحده ؟ ",
" ※ تتصل على شرطي تقول له عندكم مطافي ؟ ",
" ※ خلاص سامحتك ؟ ",
" ※ تصيح في الشارع انامجنوون ؟ ",
" ※ تروح عند شخص وقول له احبك ؟"]
    bar = random.choice(selections)
    await message.reply(
        f'**<a href="{channel_source}">{bar}</a>**',
        disable_web_page_preview=True  # تعطيل عرض المعاينة لضمان عدم وجود أخطاء
    )




saraha = [

            "هل تخربني اسم والدتك ما هو.",


            "ليك اسم شهره بتحبو ؟",
            

            "ممكن تعمل اي في حياتك",
            
            
            "انت راضي عن حياتك",
            
            
            "اسم حببتك الاوله ايه",
            
            
            "ما هو هدفك في الحياه",
            
            
            "كم مجموعك الدراسي",
            
            
            "ما هو الاكل المفضل لك",
            
            
            "هل تحب سماع القران الكريم",
            
            
            "هل تامن بالحب",
            
            
            "ماهو اخطر سر اليك",
            
            
            "هل تامن بالارتباط السوشيال",
            
            
            "متي ستتزوج",
            
            
            "هل تحب الفتيات ام الصبيان",
            
            
            "ماهو قولك عندما تره ما تحب",
            
            
            "مانوع هاتفك الجوال",
            
            
            "ماذا تفعل في الشتاء",
            
            
            "هل تحب والديك ام خوتك",
            
            
            "هل لك اسم شهره",
            
            
            "سبق و فعلت شي ندمان علي فعله",
            
            
            "ما هو هدفك في الوقت الحالي",
            
            
            "ما اسم فلمك المفضل",
            
            
            "هل تحب الصراحه ام الكذب",
            
            
            "◍ أوصف نفسك بكلمة؟",
            
            
            "ممكن تقدم نصيحه لاحدهم بعنوان متغلطش غلطتي",
            
            "تاريخ ميلادك ايه?",
            
            
            "مرتبط ولا سنجل ؟",
            
            
            "انت بخير حاليا ؟",
            
            
            "اسمك ايه",
            
            
            "منين داهيه",
            
            
            "عندك صحاب بنات",
            
            
            "عندك صحاب ولاد",
            
            
            "لونك المفضل",
            
            
            "جربت حاجه نجحت واي هي ؟",
            
            
            "رايك في البار",
            
            
            "مين اكتر حد بتحبه هنا",
            
            
            "هات رقمك",
            
            
            "بتحب المغامره",
            
            
            "احسن حاجه حصلتلك الفتره دي",
            
            
            "بتصلي",
            
            
            "كم فرد في الاسلام",
            
            
            "ممكن تقدم نصيحه لاحدهم بعنوان متغلطش غلطتي",
            
            
            "كم ركعه في صلاه العصر",
            
            
            "ما هيا اليلله التي خير من الف شهر",
            
            
            "سرقت قبل كدا",
            
            
            "هل تحب الموسيقى",
            
            
            "هل تحب مصر",
            
            
            "لو الحمه غلت تاكل ايه",
            
            
            "ايه رايك فيا كابوت موز",
            
            
            "بتحب مين من الفنانين",
            
            
            "امك حلوه",
            
            
            "عندك كم اخ",
            
            
            "تقدر تنصح غيرك",
            
            
            "عاوز تعمل نصيبه امتي",
            
            
            "اي اللي مخليك فجروب الزباله دا",
            
            
            "لابس ايه دلوقتي",
            
            
            "لابسه ايه دلوقتي",
            
            
            "حد باسك قبل كدا",
            
            
            "بوست حد قبل كدا",
            
            
            "بتحب الفلوس",
            
            
            "بتحب الكشري",
            
            
            "نفسك تسافر فيه",
            
            
            "عالطلاق انت كحيااان",
            
            
            "بتعرف ترقص",
            
            
            "بتعرف تغني",
            
            
            "بتحب المدرسه",
            
            
            "ارتبط من المدرسه قبل كدا",
            
            
            "اكتر اتنين بتحب تخرج معاهم",
            
            
            "بتحب الفصح",
            
            
            "بتحب المناسبات",
            
            
            "بتحب الفول",
            
            
            "عاوز تخرج فين",
            
            
            "جربت تموت من الجوع قبل كدا",
            
            
            "بتحب تربي القطط",
            
            
            "مامتك عايشه",
            
            
            "ايه رايك في تليجرام",
            
            
            "ايه رايك في بت اللي فكول دي",
            
            
            "ايه رايك في اسعار في البلد",
            
            
            "ناوي تغير فونك امتي",
            
            
            "تعرف تشتم حد بتحبو",
            
            
            "بتحب الصعيد",
            
            
            "بتحب اسكندريه",
            
            
            "متابع ايه في مسلسلات التركي",
            
            
            "عندك واتساب",
            
            
            "ايه رايك في الشتاء",
            
            
            "ايه رايك في الصيف",
            
            
            "ايه رايك في الخريف",
            
            
            "كم فصل في سنه",
            
            
            "قاعد فين دلوقتي",
            
            
            "شربت حشيش قبل كدا",
            
            
            "بتشرب سجاير",
            
            
            "بتشربي سجاير",
            
            
            "عيط علي حاجه قبل كدا",
            
            
            "بتنام امتي",
            
            
            "شغال ايه",
            
            
            "شغاله ايه",
            
            
            "بتحب شغالك",
            
            
            "نفسك تبقي غني",
            
            
            "بتعرف تخبي مشعارك",
            
            
            "لون عيونك ايه",
            
            
            "لون شعرك ايه",
             "حبيت كام مره 💏",
             
                "اتعاكست كام مره☹️☹️",
                
                "خونت كام مره 😈",
                
                "موقف محرج حصلك😳",
                
                "اكتر شخص حبيته وكسرك💔",
                
                "شايف نفسك فين  بعد 5 سنين🤑",
                
                "لو بقيت بنت ليوم اول حاجه هتعملها ايه والعكس لو بقيتي ولد ليوم اول حاجه هتعمليها ايه🤐🤐",
                
                "اغرب موقف حصلك🤨",
                
                "اقرب انسان لقلبك 💑",
                
                "قولي اغلي 5 اشخاص في حياتك 👨‍👩‍👦‍👦",
                
                "اوصف نفسك في كلمتين👼",
                
                "لو ليك 3 امنيات هيبقوا ايه 🧚‍♂️🧚‍♀️",
                
                "اكتر شخص بتحبه هنا مين😍",
                
                "اوصف صاحب ليك في 3 كلمات😌",
                
                "عاكست قبل كده وكان مين😘",
                
                "اتخانت قبل كده ؟🤣",
                
                "لو اتجبرت علي جواز صالونات هتوافق 👰🤵",
                
                "لو هترتبط بحد في الروم هيبقي مين 😉",
                
                "اهلك بيدلعوك بيقولولك ايه 😁😁",
                
                "صوتك حلو؟",
                
                "لقيت الناس اللي بوشين؟",
                
                "شيء وكنت تحقق اللسان؟",
                
                "أنا شخص ضعيف عندما؟",
                
                "هل ترغب في إظهار حبك ومرفق لشخص أو رؤية هذا الضعف؟",
                "هل الكذب يكون ضروري وقتا ما؟",
                
                "أتشعر بالوحدة على الرغم انه يحاط بك الكثير من البشر؟",
                
                "كيفية الكشف عن من يكمن عليك؟",
                
                "إذا حاول شخص ما أن يكرهه أن يقترب منك ويهتم بك تعطيه فرصة؟",
                
                "أشجع حاجه حلوه ف حياتك؟",
                
                "طريقة جيدة يقنع حتى لو كانت الفكرة خاطئة" 
                
                "كيف تتصرف مع من يسيئون فهمك ويأخذ على ذهنه ثم ينتظر أن يرفض؟",
                
                "التغيير العادي عندما يكون الشخص الذي يحبه؟",
                
                "المواقف الصعبة تضعف لك ولا ترفع؟",
                
                "نظرة و يفسد الصداقة؟",
                
                "تاخد بكلام اللي ينصحك وماتعملش اللي انت عاوزة؟",
                
                "اي تتمني الناس تعرفه عليك؟",
                
                "ابيع المجرة عشان؟",
                
                "أحيانا بحس ان الناس ، كمل؟",
                
                "صدفة العمر الحلوة هي اني؟",
                
                "الكُره العظيم دايم يجي بعد حُب قوي "
                "صفة تحبها في نفسك؟",
                
                "اشجع شيء عملته ف حياتك؟",
                
                "ناوي تعمل اي النهارده؟",
                
                "اي بيكون شعورك لما بتشوف المطر؟",
                "غيرتك هاديه ومابتعملش مشاكل؟",
                "اي اكتر حاجه ندمت عليها؟",
                "اي الدول اللي تتمنى تزورها؟",
                "اخره مره بكيت امتي؟",
                "تقييم حظك ؟ من عشره؟",
                "هل تعتقد ان حظك سيئ؟",
                "شـخــص تتمنــي الإنتقــام منـــه؟",
                "كلمة تود سماعها كل يوم؟",
                "**هل تُتقن عملك أم تشعر بالممل؟",
                "هل قمت بانتحال أحد الشخصيات لتكذب على من حولك؟",
                "متى آخر مرة قمت بعمل مُشكلة كبيرة وتسببت في خسائر؟",
                "ما هو اسوأ خبر سمعته بحياتك؟",
                "هل قمت بالبكاء أمام من تُحب؟",
                
                "ماذا تختار حبيبك أم صديقك؟",
                
                "هل حياتك سعيدة أم حزينة؟",
                
                "ما هي أجمل سنة عشتها بحياتك؟",
                
                "ما هو عمرك الحقيقي؟",
                
                "ما هي أمنياتك المُستقبلية؟"
        ]

@app.on_message(filters.command(["صراحه","اسال","س","سوال","اس","✨اسال","صراحة 💭"], ""),group=454545454787)
async def cutt(client: Client, message: Message):
      a = random.choice(saraha)
      await message.reply(
        f'**<a href="{channel_source}">{a}</a>**',
        disable_web_page_preview=True  # تعطيل عرض المعاينة لضمان عدم وجود أخطاء
    )



txayat = [


            "لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",


            "شخص تحب تستفزه ؟",


            "لو حلمت في شخص وصحيت وحصلت رساله من نفس الشخص . ارسل ايموجيي مثل ردة فعلك.",


            "هات صورة تحس إنك ابدعت بتصويرها.",


            "على إيش سهران ؟",


            "مين تتوقع يطالعك طول الوقت بدون ملل ؟",


            "وين جالس الحين ؟",


            "كم من عشرة تقيم يومك ؟",


            "أطول مدة نمت فيها كم ساعه ؟",


            "أجمل سنة ميلادية مرت عليك ؟",


            "أخر رسالة بالواتس جاتك من مين ؟",


            "ليه مانمت ؟",


            "تعتقد فيه أحد يراقبك ؟",


            "كم من عشره تعطي حظك ؟",


            "كلمه ماسكه معك الفترة هذي ؟",


            "شيء مستحيل تمل منه ؟",


            "متى تنام بالعادة ؟",


            "كم من عشرة جاهز للدراسة ؟",


            "منشن صديقك الفزعة",


            "يوم نفسك يرجع بكل تفاصيله ؟",


            "أجمل صورة بجوالك ؟",


            "ايش أغرب مكان قد صحتوا فيه؟",


            "اذا جاك خبر مفرح اول واحد تعلمه فيه مين ؟",


            "شيء لو يختفي تصير الحياة جميلة ؟",


            "كم من عشرة تشوف نفسك محظوظ ؟",


            "امدح نفسك بكلمة وحدة بس",


            "كلمة لأقرب شخص لقلبك ؟",


            "قوة الصداقة بالمدة ولا بالمواقف ؟",


            "تتابع مسلسلات ولا م تهتم ؟",


            "تاريخ يعني لك الكثير ؟",


            "كم عدد اللي معطيهم بلوك ؟",


            "من الغباء انك ؟",


            "اكثر شيء محتاجه الحين ؟",


            "ايش مسهرك ؟.",


            "حزين ولا مبسوط ؟",


            "تحب سوالف مين ؟",


            "كم من عشرة روتينك ممل ؟",


            "شيء مستحيل ترفضه ؟.",


            "كم من عشرة الإيجابية فيك ؟.",


            "تعتقد اشباهك الاربعين عايشين حياة حلوة ؟.",


            "مين جالس عندك ؟",


            "كم من عشرة تشوف نفسك انسان ناجح ؟",


            "شيء حظك فيه حلو ؟.",


            "كم من عشرة الصبر عندك ؟",


            "أخر مرة نزل عندكم مطر ؟",


            "اكثر مشاكلك بسبب ؟",


            "اكره شعور ممكن يحسه انسان ؟",


            "شخص تحب تنشبله ؟",


            "تنتظر شيء ؟",


            "جربت تسكن وحدك ؟",


            "اكثر لونين تحبهم مع بعض ؟",


            "متى تكره نفسك ؟",


            "كم من عشرة مروق ؟",


            "مدينة تتمنى تعيش وتستقر فيها طول عمرك ؟",


            "اكثر شيء تحبه فالشتاء ...",


            "شيء ودك تتركه ...",


            "كم تعطي نفسك من 10 فاللغة الانجليزية ؟",


            "شخص فرحتك مرتبطة فيه ...",


            "اكتب اسم .. واكتب كيف تحس بيكون شكله ...",


            "متى اخر مره قلت ليتني سكت ؟",


            "ممكن تكره احد بدون سبب ؟",


            "اكثر وقت باليوم تحبه ...",


            "اكثر شيء حظك سيء فيه ...",


            "متى صحيت ؟",


            "كلمة صعب تقولها وثقيلة عليك ...",


            "ردك الدائم على الكلام الحلو ...",


            "سؤال دايم تتهرب من الاجابة عليه ...",


            "مين الشخص اللي مستعد تأخذ حزنه بس م تشوفه حزين ؟.",


            "جربت تروح اختبار بدون م تذاكر ؟",


            "كم مرة غشيت ف الاختبارات ؟",


            "وش اسم اول شخص تعرفت عليه فالديسكورد ؟",


            "تعطي فرصة ثانية للشخص الي كسرك ؟",


            "لو احتاج الشخص الي كسرك مساعدة بتوقف معه ؟",


            "@منشن... شخص ودك تطرده من السيرفر ...",


            "دعاء له اثر إبجابي في حياتك ...",


            "قل حقيقه عنك ؟",


            "انسان م تحب تتعامل معه ابد",


            "اشياء اذا سويتها لشخص تدل على انك تحبه كثير ؟",


            "الانتقاد الكثير يغيرك للافضل ولا يحطمك ويخليك للأسوأ ؟",


            "كيف تعرف اذا هذا الشخص يكذب ولا لا ؟",


            "مع او ضد : العتاب على قدر المحبة ...",


            "شيء عندك اهم من الناس",


            "تتفاعل مع الاشياء اللي تصير بالمجتمع ولا ماتهتم ؟.",


            "وش الشيء الحلو الي يميزك عن غيرك ؟",


            "كذبة كنت تصدقها وانت صغير ..",


            "@منشن .. شخص تخاف منه اذا عصب ...",


            "كلمة بـ لهجتك تحس م احد بيعرفها ...",


            "كمل ... انا من الاشخاص الي ...",


            "تراقب احد بالديسكورد ؟",


            "كيف تعرف ان هالشخص يحبك ؟",


            "هواية او تجربة كان ودك تستمر و تركتها ؟",


            "الديسكورد اشغلك عن حياتك الواقعية ؟",


            "اكمل ... تستمر علاقتك بالشخص اذا كان ...",


            "لو احد قالك اكرهك وش بتقول له ؟",


            "مع او ضد : عامل الناس كما يعاملوك ؟",


            "ارسل اخر صورة فـ الالبوم ...",


            "الصق وارسل اخر شيء نسخته ...",


            "ماهي اخر وجبة اكلتها ",


            "اكثر شيء تحس انه مات ف مجتمعنا",


            "برأيك ماهو افضل انتقام ...",


            "اكثر ريحة تجيب راسك ...",


            "شعور ودك يموت ...",


            "عمرك فضفضت لـ شخص وندمت ؟",


            "تقدر تتحمل عيوب شخص تحبه ؟",


            "يكبر الشخص ف عيونك لما ...",


            "وش تقول للشخص الي معك دائماً ف وقت ضيقتك ؟",


            "مقولة او حكمة تمشي عليها ...",


            "منشن ... شخص اذا وضعه على الجرح يلتهب زيادة",


            "منشن ... شخص يعجبك كلامه و اسلوبه ...",


            "لو السرقة حلال ... وش اول شيء بتسرقه ؟",


            "مع او ضد : المرأة تحتاج لرجل يقودها ويرشدها ...",


            "مع او ضد : لو دخل الشك ف اي علاقة ستنتهي ...",


            "منشن... اي شخص واوصفه بـ كلام بسيط ...",


            "مع او ضد : قلة العلاقات راحة ...",


            "لو خيروك : تعض لسانك بالغلط ، ولا يسكر على صبعك الباب؟",


            "كلمة غريبه و معناها ...",


            "نصيحة تقدمها للشخص الثرثار ...",


            "مع او ضد :  مساعدة الزوجة في اعمال المنزل مهما كانت ...",


            "منشن... شخص يجيك فضول تشوف وجهه ...",


            "كلمة لـ شخص عزيز عليك ...",


            "اكثر كذبة تقولها ...",


            "معروف عند اهلك انك ...",


            "وش اول طريقة تتبعها اذا جيت تراضي شخص",


            "ع او ضد : ما تعرف قيمة الشخص اذا فقدته ...",


            "تحب تختار ملابسك بنفسك ولا تحب احد يختار معك ...",


            "وش اكثر شيء انجلدت بسببه وانت صغير ؟",


            "فـ اي برنامج كنت قبل تجي الديسكورد ؟",


            "تنسد نفسك عن الاكل لو زعلت ؟",


            "وش الشيء الي تطلع حرتك فيه و زعلت ؟",


            "مع او ضد : الصحبة تغني عن الحب ... ",


            "منشن... اخر شخص خلاك تبتسم",


            "لو نطق قلبك ماذا سيقول ...",


            "ماذا يوجد على يسارك حالياً ؟",


            "مع او ضد : الشخص الي يثق بسرعة غبي ...",


            "شخصية كرتونية تأثرت فيها وانت صغير ...",


            "مع او ضد : الاهتمام الزائد يضايق",


            "لو خيروك : تتزوج ولا تكمل دراستك ...",


            "منشن... لو بتختار شخص تفضفض له مين بيكون ؟",


            "كمل : مهما كبرت بخاف من ....",


            "اخر عيدية جاتك وش كانت ...",


            "وش حذفت من قاموس حياتك ...",


            "شيء تتمنى م ينتهي ...",


            "اكره شعور ممكن يحس فيه الانسان هو ...",


            "مع او ضد : يسقط جمال المراة بسبب قبح لسانها ...",


            "ماهي الخسارة في نظرك ...",


            "لو المطعم يقدم الوجبه على حسب شكلك وش راح تكون وجبتك ؟",


            "مع او ضد : يموت الحب لو طال الغياب",


            "وش الشيء الي يحبه اغلب الناس وانت م تحبه ..",


            "تحدث عن نفسك ؟",


            "اقوى جملة عتاب وصلتك",


            "على ماذا ندمت ؟",


            "اخر مرة انضربت فيها من احد اهلك ، ولماذا ؟",


            "افضل طريقة تراضي فيها شخص قريب منك",


            "لو بإمكانك تقابل شخص من الديسكورد مين بيكون ؟",


            "كمل : كذاب من يقول ان ...",


            "طبعك صريح ولا تجامل ؟",


            "مين اقرب لك ؟ اهل امك ، اهل ابوك  ...",


            "وش لون عيونك ؟",


            "مع او ضد : الرجال اكثر حقداً من النساء",


            "مع او ضد : ينحب الشخص من اهتمامه",


            "@منشن: شخص تقوله اشتقت لك",


            "بصراحة : تحب تفضفض وقت زعلك ، ولا تنعزل ؟",


            "مع او ضد : حبيبك يطلب منك حذف اصحابك بحكم الغيرة",


            "متى تحس بـ شعور حلو ؟",


            "لو حياتك عبارة عن كتاب .. وش بيكون اسمه ؟",


            "@منشن: شخص واسأله سؤال ...",


            "كم مره سويت نفسك غبي وانت فاهم ،  ومع مين ؟",


            "اكتب شطر من اغنية او قصيدة جا فـ بالك",


            "كم عدد الاطفال عندكم فالبيت ؟",


            "@منشن : شخص وعطه وظيفة تحس تناسبه",


            "اخر مكالمة فـ الخاص كانت مع مين ؟",


            "عمرك ضحيت باشياء لاجل شخص م يسوى ؟",


            "كمل : حلو يومك بـ وجود ...",


            "مع او ضد : المرأة القوية هي اكثر انسانه انكسرت",


            "نصيحة تقدمها للغارقين فالحب ...",


            "مبدأ تعتمد عليه فـ حياتك",


            "ترد بالمثل على الشخص لو قذفك ؟",


            "شيء مهما حطيت فيه فلوس بتكون مبسوط",


            "@منشن: اكثر شخص يفهمك",


            "تاريخ ميلادك + هدية بخاطرك تجيك",


            "كم كان عمرك لما اخذت اول جوال ؟",


            "عمرك كتبت كلام كثير بعدين مسحته ، مع مين كان؟",


            "برأيك : وش اكثر شيء يرضي البنت الزعلانه ؟",


            "مساحة فارغة (..............) اكتب اي شيء تبين",


            "تترك احد عشان ماضيه سيء ؟",


            "تهتم بالابراج ، واذا تهتم وش برجك ؟",


            "لو ستبدأ حياتك من جديد ، وش راح تغير بـ نفسك ؟",


            "تتوقع فيه احد حاقد عليك ويكرهك ؟",


            "وش يقولون لك لما تغني ؟",


            "مين المغني المفضل عندك ؟",


            "ميزة ودك يضيفها البرنامج",


            "وش الي مستحيل يكون لك اهتمام فيه ؟",


            "البنت : تتزوجين احد اصغر منك ",


            "الرجل : تتزوج وحده اكبر منك",


            "احقر الناس هو من ...",


            "البنت : وش تتمنين تكون وظيفة زوجك ",
            "الرجل : وش تتمنى وظيفة زوجتك",
            "برأيك : هل الانتقام من الشخص الذي اخطأ بحقك راحة ؟",
            "اهم شيء يكون معك فـ كل طلعاتك ؟",
            "وش الخدمة الالكترونية الي تتمنى تصير ؟",
            "كلمة تخليك تلبي الطلب حق الشخص بدون تفكير",
            "وش الفايدة الي اخذتها من الديسكورد ؟",
            "مع ام ضد : غيرة البنات حب تملك وانانية",
            "هل سبق ان ندمت انك رفضت شيء ، وش كان ؟",
            "تشوف انك قادر على تحمل المسؤولية ؟",
            "مع او ضد : الناس يفضلون الصداقة وعندما يأتي الحب يتركون الصداقة",
            "اعلى نسبة جبتها ف حياتك الدراسية",
            "تحب احد يتدخل ف امورك الشخصية  ؟",
            "لو واحد يتدخل ف امورك وانت م طلبت منه وش بتقوله ؟",
            "تاخذ بنصيحة  الاهل ام من الاصحاب ؟",
            "فيه شيء م تقدر تسيطر عليه ؟",
            "@منشن : شخص تحب سوالفه",
            "وش الكذبة المعتادة الي تسويها لو بتقفل من احد ؟",
            "@منشن: الشخص الي عادي تقوله اسرارك",
            "لو زعلت بقوة وش بيرضيك ؟",
            "كلمة تقولها لـ بعض الاشخاص في حياتك",


            "ندمت انك اعترف بمشاعرك لـ شخص",


            "وش الاكلة المفضلة عندك ؟",


            "وش تتخيل يصير معك فـ المستقبل ؟",


            "اسم الطف شخص مر عليك الكترونياً",


            "مع او ضد : الاستقرار النفسي اهم استقرار",


            "مع او ضد : كل شيء راح يتعوض",


            "برأيك : وش الشيء الي مستحيل يتعوض ؟",


            "تفضل : الدجاج ، اللحم ، السمك",


            "◍ ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",


            "◍ أطول مدة نمت فيها كم ساعة؟",


            "◍ كلمة غريبة من لهجتك ومعناها؟🤓",


            "◍ ردة فعلك لو مزح معك شخص م تعرفه ؟",


            "◍ شخص تحب تستفزه😈؟",


            "◍ ردة فعلك لو مزح معك شخص م تعرفه ؟",


            "◍ اذا شفت حد واعجبك وعندك الجرأه انك تروح وتتعرف عليه ، مقدمة الحديث وش راح تكون ؟.",


            "◍ كلمة لشخص أسعدك رغم حزنك في يومٍ من الأيام ؟",


            "◍ حاجة تشوف نفسك مبدع فيها ؟",


            "◍ يهمك ملابسك تكون ماركة ؟",


            "◍ يومك ضاع على؟",


            "◍ اذا اكتشفت أن أعز أصدقائك يضمر لك",


            " السوء، موقفك الصريح؟",


            "◍ هل من الممكن أن تقتل أحدهم من أجل المال؟",


            "◍ كلمه ماسكه معك الفترة هذي ؟",


            "◍ كيف هي أحوال قلبك؟",


            "◍ صريح، مشتاق؟",


            "◍ اغرب اسم مر عليك ؟",


            "◍ تختار أن تكون غبي أو قبيح؟",


            "◍ آخر مرة أكلت أكلتك المفضّلة؟",


            "◍ اشياء صعب تتقبلها بسرعه ؟",


            "◍ كلمة لشخص غالي اشتقت إليه؟",


            "◍ اكثر شيء تحس انه مات ف مجتمعنا؟",


            "◍ هل يمكنك مسامحة شخص أخطأ بحقك لكنه قدم الاعتذار وشعر بالندم؟",


            "◍ آخر شيء ضاع منك؟",


            "◍ تشوف الغيره انانيه او حب؟",


            "◍ لو فزعت/ي لصديق/ه وقالك مالك دخل وش بتسوي/ين؟",


            "◍ شيء كل م تذكرته تبتسم ...",


            "◍ هل تحبها ولماذا قمت باختيارها؟",


            "◍ هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",


            "◍ متى تكره الشخص الذي أمامك حتى لو كنت مِن أشد معجبينه؟",


            "◍ أقبح القبحين في العلاقة: الغدر أو الإهمال🤷🏼؟",


            "◍ هل وصلك رسالة غير متوقعة من شخص وأثرت فيك ؟",


            "◍ هل تشعر أن هنالك مَن يُحبك؟",


            "◍ وش الشيء الي تطلع حرتك فيه و زعلت ؟",


            "◍ صوت مغني م تحبه",


            "◍ كم في حسابك البنكي ؟",


            "◍ اذكر موقف ماتنساه بعمرك؟",


            "◍ ردة فعلك لو مزح معك شخص م تعرفه ؟",


            "◍ عندك حس فكاهي ولا نفسية؟",


            "◍ من وجهة نظرك ما هي الأشياء التي تحافظ على قوة وثبات العلاقة؟",


            "◍ ما هو نوع الموسيقى المفضل لديك والذي تستمع إليه دائمًا؟ ولماذا قمت باختياره تحديدًا؟",


            "◍ لو قالوا لك  تناول صنف واحد فقط من الطعام لمدة شهر .",


            "◍ هل تنفق مرتبك بالكامل أم أنك تمتلك هدف يجعلك توفر المال؟",


            "◍ آخر مرة ضحكت من كل قلبك؟",


            "◍ وش الشيء الي تطلع حرتك فيه و زعلت ؟",


            "◍ تزعلك الدنيا ويرضيك ؟",


            "◍ تعتقد فيه أحد يراقبك؟",


            "◍ احقر الناس هو من ...",


            "◍ شيء من صغرك ماتغير فيك؟",


            "◍ وين نلقى السعاده برايك؟",


            "◍ هل تغارين من صديقاتك؟",


            "◍ أكثر جملة أثرت بك في حياتك؟",


            "◍ كم عدد اللي معطيهم بلوك؟",


            "◍ أجمل سنة ميلادية مرت عليك ؟",


            "◍ أوصف نفسك بكلمة؟",


        ]


        


@app.on_message(filters.command(["كت","تويت","✨كت","✨تويت","تويت 🕊"], ""),group=4878787121)
async def cutt(client: Client, message: Message):
      a = random.choice(txayat)
      await message.reply(
        f'**<a href="{channel_source}">{a}</a>**',
        disable_web_page_preview=True  # تعطيل عرض المعاينة لضمان عدم وجود أخطاء
    )
        
taaaaxt = [
"عامل الناس بأخلاقك ولا بأخلاقهم", 
"الجمال يلفت الأنظار لكن الطيبه تلفت القلوب ", 
"الاعتذار عن الأخطاء لا يجرح كرامتك بل يجعلك كبير في نظر الناس ",
"لا ترجي السماحه من بخيل.. فما في البار لظمان ماء",
"لا تحقرون صغيره إن الجبال من الحصي",
"لا تستحي من إعطاء فإن الحرمان أقل منه ", 
"لا تظلم حتى لا تتظلم ",
"لا تقف قصاد الريح ولا تمشي معها ",
"لا تكسب موده التحكم الا بالتعقل",
"لا تمد عينك في يد غيرك ",
"لا تملح الا لمن يستحقاها ويحافظ عليها",
"لا حياه للإنسان بلا نبات",
"لا حياه في الرزق.. ولا شفاعه في الموت",
"كما تدين تدان",
"لا دين لمن لا عهد له ",
"لا سلطان على الدوق فيما يحب أو بكره",
"لا مروه لمن لادين له ",
"لا يدخل الجنه من لايأمن من جازه بوائقه",
"يسروا ولا تعسروا... ويشورا ولا تنفروا",
"يدهم الصدر ما يبني العقل الواسع ",
"أثقل ما يوضع في الميزان يوم القيامة حسن الخلق ",
"أجهل الناس من ترك يقين ما عنده لظن ما عند الناس ",
"أحياناً.. ويصبح الوهم حقيقه ",
"مينفعش تعاتب حد مبيعملش حساب لزعلك عشان متزعلش مرتين . ",
"السفر ومشاهده اماكن مختلفه وجديده ",
"عدم تضيع الفرص واسثمارها لحظه مجبئها ",
" اعطاء الاخرين اكثر من ما يتوقعون",
"معامله الناس بلطف ولكن عدم السماح لاحد بستغالال ذالك ",
"تكوين صدقات جديده مع الحفظ بلاصدقاء القودامي ",
"تعلم اصول المهنه بدلا من تضيع الوقت ف تعلم حيل المهنه ",
"مدح ع الاقل ثلاث اشخاص يوميا ",
"النظر ف عيون الشخاص عند مخاطبتهم ",
"التحلي بلسماح مع الاخرين او النفس ",
"الاكثار من قول كلمه شكرا ",
" مصافحه الاخرين بثبات وقوة ",
"الابتعاد عن المناطق السيئه السمعه لتجنب الاحداث السئه ",
" ادخار 10٪ع الاقل من الدخل",
" تجنب المخاوف من خلال التعلم من تجارب مختلفه",
" الحفاظ ع السمعه لانها اغلي ما يملك الانسان",
" تحويل الاعداء الي اصدقاء من خلال القيام بعمل جيد",
"لا تصدق كل ما تسمعع. ولا تنفق كل ما تمتلك . ولا تنم قدر ما ترغب ",
" اعتني بسمعتك جيدا فستثبت للك الايام انها اغلي ما تملك",
"حين تقول والدتك ستندم ع فعل ذالك ستندم عليه غالبا.. ",
" لا تخش العقبات الكبيره فخلفها تقع الفرص العظيمه",
"قد لا يتطلب الامر اكثر من شخص واحد لقلب حياتك رأس ع عقب ",
"اختر رفيقه حياتك بحرص فهو قرار سيشكل 90٪من سعادتك او بؤسك ",
" اقلب اداءك الاصدقاء بفعل شي جميل ومفجائ لهم",
"حين تدق الفرصه ع باباك ادعوها للبيت ",
"تعلم القواعد جيدا ثن اكسر بعدها ",
"احكم ع نجاحك من خلال قدرتك ع العطاء وليس الاخذ ",
" لا تتجاهل الشيطان مهما بدل ثيابه",
"ركز ع جعل الاشياء افضل وليس اكبر او اعظم ",
"كن سعيد  بما تمتلك واعمل لامتلاك ما تريد ",
"اعط الناس اكثر من ما يتوقعون ",
" لا تكن منشغل لدرجه عدم التعرف ع اصدقاء جدد",
"استحمه يوم العيد يمعفن🐰",
"مش تحب اي حد يقرب منك ",
" خليك مع البت راجل خليك تقيل",
" انصح نفسك بنفسك بمت😂",
" كنت نصحت نفسي ياخويا🗿", 

        ]


        


@app.on_message(filters.command(["انصحني","✨انصحني"], ""),group=4564478)

async def anshny(client: Client, message: Message):

      a = random.choice(taaaaxt)

      await message.reply(
        f'**<a href="{channel_source}">{a}</a>**',
        disable_web_page_preview=True  # تعطيل عرض المعاينة لضمان عدم وجود أخطاء
    )
      


txnokatt = [


"واحد مشغول أتجوز واحدة مشغولة خلفوا عيل مش فاضيلهم 👻😹",
"مرة القمر كان عايز يتجوز الشمس قالتله أتجوز واحد صايع طول الليل 👻😹",
"ولد بيسأل أبوه هو الحب أعمى رد عليه أبوه بص في وش أمك وأنت تعرف 👻😹",
"مرة مفتاح مات أهله ما زعلوش عليه عشان معاهم نسخة تانية 👻😹",
"ممرضة خلفت توأم سمت واحد عضل والتاني وليد 👻😹",
"مسطول أتجوز صينية قالتله مالك ساكت ليه؟ قالها مش عارف افتكرتك نايمة 👻😹",
"واحدة صعيدية جوزها رماها من الدور الثالث طلعتله وقالتله بلاش الهزار البايخ ده 👻😹",
"اتنين مساطيل حبوا يسرقوا عمارة فقالوا لبعض إحنا ناخد العمارة بعيد ونسرقها برحتنا 👻😹",
"منهم بص ورا ملقاش الهدوم فقال له كفاية كدة احنا بعدنا أوى 👻😹",
"حر جدًا، قالتله مفيش مشكلة نطلعها بالليل 👻😹",
"واحد رجع في كلامه خبط اللي وراه 👻😹",
"واحد خلقه ضاق أعطاه لأخوه الصغير 👻😹",
"مرة مدرس رياضيات خلف ولدين واستنتج التالت 👻😹",
"واحد كهربائي أتجوز أربعة جابلهم مشترك 👻😹",
"كفايه عليك كده ياد يبن الحلوهه 👻😹",
"واحدة اسمها ساندي دخلت هندسة بقت ساندي متر مربع 👻😹",
"مرة شرطي مرور خلّف ولد بيتكلم بالإشارة 👻😹",
"مره واحد اسمو جابوا  كان بيرجم ابليس ف الحج قالولو ليه؟ قال عشان يمكن احتاجو 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه  👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
" مرة واحد مصري دخل سوبر ماركت في الكويت عشان يشتري ولاعة راح عشان يحاسب بيقوله الولاعة ديه بكام قاله دينار قاله منا عارف ان هي نار بس بكام 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"واحد بيشتكي لصاحبه بيقوله أنا مافيش حد بيحبني ولا يفتكرني أبدًا، ومش عارف أعمل إيه قاله سهلة استلف من الناس فلوس هيسألوا عليك كل يوم 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ؟ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"واحده ست سايقه على الجي بي اي قالها انحرفي قليلًا قلعت الطرحة 👻😹",
"مرة واحد غبي معاه عربية قديمة جدًا وبيحاول يبيعها وماحدش راضي يشتريها.. راح لصاحبه حكاله المشكلة صاحبه قاله عندي لك فكرة جهنمية هاتخليها تتباع الصبح أنت تجيب علامة مرسيدس وتحطها عليها. بعد أسبوعين صاحبه شافه صدفة قاله بعت العربية ولا لاء؟ قاله انت  مجنون حد يبيع مرسيدس 👻😹",
"مره واحد بلديتنا كان بيدق مسمار فى الحائط فالمسمار وقع منه فقال له :تعالى ف مجاش, فقال له: تعالي ف مجاش. فراح بلديتنا رامي على المسمار شوية مسمامير وقال: هاتوه 👻😹",
"واحدة عملت حساب وهمي ودخلت تكلم جوزها منه ومبسوطة أوي وبتضحك سألوها بتضحكي على إيه قالت لهم أول مرة يقول لي كلام حلو من ساعة ما اتجوزنا 👻😹",
"بنت حبت تشتغل مع رئيس عصابة شغلها في غسيل الأموال 👻😹",
"مره واحد اشترى فراخ علشان يربيها فى قفص صدره 👻😹",
"مرة واحد من الفيوم مات اهله صوصوا عليه 👻😹",
"ﻣﺮه واﺣﺪ ﻣﺴﻄﻮل ﻣﺎﺷﻰ ﻓﻰ اﻟﺸﺎرع ﻟﻘﻰ مذﻳﻌﻪ ﺑﺘﻘﻮﻟﻪ ﻟﻮ ﺳﻤﺤﺖ ﻓﻴﻦ اﻟﻘﻤﺮ ﻗﺎﻟﻬﺎ اﻫﻮه ﻗﺎﻟﺘﻠﻮ ﻣﺒﺮوك ﻛﺴﺒﺖ ﻋﺸﺮﻳﻦ ﺟﻨﻴﻪ ﻗﺎﻟﻬﺎ ﻓﻰ واﺣﺪ ﺗﺎﻧﻰ ﻫﻨﺎك اﻫﻮه 👻😹",
"مره واحد شاط كرة فى المقص اتخرمت. 👻😹",
"مرة واحد رايح لواحد صاحبهفا البواب وقفه بيقول له انت طالع لمين قاله طالع أسمر شوية لبابايا قاله يا أستاذ طالع لمين في العماره 👻😹",
" وهه عاوز تانيي 👻😹 "


        ]


        


@app.on_message(filters.command(["نكته","نكتة 😹"], ""),group=54548878787)

async def nokt(client: Client, message: Message):

      a = random.choice(txnokatt)

      await message.reply(
        f'**<a href="{channel_source}">{a}</a>**',
        disable_web_page_preview=True  # تعطيل عرض المعاينة لضمان عدم وجود أخطاء
    )
      


@app.on_message(filters.command(["احكام"], ""),group=545854787)
async def bottttt(client, message):
    selections = [" ※ صورة وجهك او رجلك او خشمك او يدك ؟ ",
" ※ اصدر اي صوت يطلبه منك الاعبين ؟ ",
" ※ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
" ※ روح الى اي قروب عندك في الواتس اب و اكتب اي شيء يطلبه منك الاعبينالحد الاقصى 3 رسائل ؟ ",
" ※ قول نكتة ولازم احد الاعبين يضحك اذا ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
" ※ سمعنا صوتك و غن اي اغنية من اختيار الاعبين الي معك ؟ ",
" ※ ذي المرة لك لا تعيدها ؟ ",
" ※ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
" ※ صور اي شيء يطلبه منك الاعبين ؟ ",
" ※ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
" ※ سكر خشمك و قول كلمة من اختيار الاعبين الي معك ؟ ",
" ※ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوته ؟ ",
" ※ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام ؟ ",
" ※ روح عند اي احد بالخاص و قول له انك تحبه و الخ ؟ ",
" ※ اكتب في الشات اي شيء يطلبه منك الاعبين في الخاص ؟ ",
" ※ قول نكتة اذا و لازم احد الاعبين يضحك اذا محد ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية ؟ ",
" ※ سامحتك خلاص مافيه عقاب لك  ؟ ",
" ※ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
" ※ غير اسمك الى اسم من اختيار الاعبين الي معك ؟ ",
" ※ اتصل على امك و قول لها انك تحبها  ؟ ",
" ※ لا يوجد سؤال لك سامحتك  ؟ ",
" ※ قل لواحد ماتعرفه عطني كف ؟ ",
" ※ منشن الجميع وقل انا اكرهكم ؟ ",
" ※ اتصل لاخوك و قول له انك سويت حادث و الخ.... ؟ ",
" ※ روح المطبخ و اكسر صحن  ؟ ",
" ※ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوت الكف ؟ ",
" ※ قول لاي بنت موجود في الروم كلمة حلوه ؟ ",
" ※ تكلم باللغة الانجليزية الين يجي دورك مرة ثانية لازم تتكلم اذا ما تكلمت تنفذ عقاب ثاني ؟ ",
" ※ لا تتكلم ولا كلمة الين يجي دورك مرة ثانية و اذا تكلمت يجيك باند لمدة يوم كامل من السيرفر ؟ ",
" ※ قول قصيدة  ؟ ",
" ※ تكلم باللهجة السودانية الين يجي دورك مرة ثانية ؟ ",
" ※ اتصل على احد من اخوياكخوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك ؟ ",
" ※ اول واحد تشوفه عطه كف ؟ ",
" ※ سو مشهد تمثيلي عن اي شيء يطلبه منك الاعبين ؟ ",
" ※ سامحتك خلاص مافيه عقاب لك  ؟ ",
" ※ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل.... ؟ ",
" ※ روح اكل ملح + ليمون اذا مافيه اكل اي شيء من اختيار الي معك ؟ ",
" ※ تاخذ عقابين ؟ ",
" ※ قول اسم امك افتخر بأسم امك ؟ ",
" ※ ارمي اي شيء قدامك على اي احد موجود او على نفسك ؟ ",
" ※ اذا انت ولد اكسر اغلى او احسن عطور عندك اذا انتي بنت اكسري الروج حقك او الميك اب حقك ؟ ",
" ※ اذهب الى واحد ماتعرفه وقل له انا كيوت وابي بوسه ؟ ",
" ※ تتصل على الوالدهو تقول لها خطفت شخص ؟ ",
" ※ تتصل على الوالدهو تقول لها تزوجت با سر ؟ ",
" ※ اتصل على الوالدهو تقول لهااحب وحده ؟ ",
" ※ تتصل على شرطي تقول له عندكم مطافي ؟ ",
" ※ خلاص سامحتك ؟ ",
" ※ تصيح في الشارع انامجنوون ؟ ",
" ※ تروح عند شخص وقول له احبك ؟"]
    bar = random.choice(selections)
    await message.reply(
        f'**<a href="{channel_source}">{bar}</a>**',
        disable_web_page_preview=True  # تعطيل عرض المعاينة لضمان عدم وجود أخطاء
    )

    
@app.on_message(filters.command(["صور 🎑", "🕷", "صورهه", "صور"], ""),group=231213221)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption=f"🐉 ¦ تـم اختيـار صوره لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
    
@app.on_message(filters.command(["◍ استوري ◍", "استوريهات 📱", "استوري"], ""),group=23123121344)
async def ihd(client: Client, message: Message):
    rl = random.randint(1,50)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id,url,caption=f"🐉 ¦ تـم اختيـار استوري لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["قران 🕋", "قران"], ""),group=546487)
async def ihd(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/opuml/{rl}"
    await client.send_voice(message.chat.id,url,caption=F"🐉 ¦ تـم اختيـار قران لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
@app.on_message(filters.command(["انمي 🪭", "انمي"], ""),group=548878787)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption=f"🐉 ¦ تـم اختيـار انمي لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
@app.on_message(filters.command(["اقتباس 💬", "اقتباس"], ""),group=454679999)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption=f"🐉 ¦ تـم اختيـار اقتباس لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
@app.on_message(filters.command(["متحركه 🎬", "◍ متحركه ◍"], ""),group=77897987)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption=f"🐉 ¦ تـم اختيـار متحركه لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
@app.on_message(filters.command(["صور بنات 🧚🏻‍♀️","صور بنات","صوره بنات"], ""),group=797787745)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption=f"🐉 ¦ تـم اختيـار افتار لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    
@app.on_message(filters.command(["صور شباب", "صور شباب 🧜🏻‍♂️", "صوره شباب"], ""),group=6454879)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vgbmm/{rl}"
    await client.send_photo(message.chat.id,url,caption=f"🐉 ¦ تـم اختيـار افتار لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )

@app.on_message(filters.command(["◍ اغنيه عشوائيه ◍","غنيلي"], ""),group=54641215454)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/gukygn/{rl}"
    await client.send_voice(message.chat.id,url,caption=f"🐉 ¦ تـم اختيـار الاغنيه لـك",parse_mode=enums.ParseMode.HTML)
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )



cpaesr2 = {}              
upsrs2 = {}        

patos = [
    {"name": "ماليزيا", "photo": "https://envs.sh/wfz.jpg"},
    {"name": "الاردن", "photo": "https://envs.sh/wfl.jpg"},
    {"name": "الفاتيكان", "photo": "https://envs.sh/wfJ.jpg"},
    {"name": "الصين", "photo": "https://envs.sh/wfs.jpg"},
    {"name": "النيجر", "photo": "https://envs.sh/wf9.jpg"},
    {"name": "مصر", "photo": "https://envs.sh/wfN.jpg"},
    {"name": "سويسرا", "photo": "https://envs.sh/wfM.jpg"},
    {"name": "جزر الباهاما", "photo": "https://envs.sh/wfX.jpg"},
    {"name": "تشاد", "photo": "https://envs.sh/wf6.jpg"},
    {"name": "استونيا", "photo": "https://envs.sh/wfx.jpg"},
    {"name": "ليتوانيا", "photo": "https://envs.sh/waD.jpg"},
    {"name": "انجلترا", "photo": "https://envs.sh/waE.jpg"},
    {"name": "البرازيل", "photo": "https://envs.sh/wah.jpg"},
    {"name": "الارجنتين", "photo": "https://envs.sh/wau.jpg"},
    {"name": "تونس", "photo": "https://envs.sh/wab.jpg"},
    {"name": "ليبيريا", "photo": "https://envs.sh/waP.jpg"},
    {"name": "مالي", "photo": "https://envs.sh/waw.jpg"},
    {"name": "الكونغو", "photo": "https://envs.sh/wa0.jpg"},
    {"name": "العراق", "photo": "https://envs.sh/waS.jpg"},
    {"name": "ارمينيا", "photo": "https://envs.sh/waI.jpg"},
    {"name": "اسبانيا", "photo": "https://envs.sh/waA.jpg"},
    {"name": "السنغال", "photo": "https://envs.sh/waj.jpg"},
    {"name": "البرتغال", "photo": "https://envs.sh/wac.jpg"},
    {"name": "ليتوانيا", "photo": "https://envs.sh/waD.jpg"},
    {"name": "لوكسمبورغ", "photo": "https://envs.sh/waZ.jpg"},
    {"name": "البوسنه", "photo": "https://envs.sh/waL.jpg"},
    {"name": "فلسطين", "photo": "https://envs.sh/wa5.jpg"},
    {"name": "كينيا", "photo": "https://envs.sh/waK.jpg"},
    {"name": "سان مارينو", "photo": "https://envs.sh/waz.jpg"},
    {"name": "الفلبين", "photo": "https://envs.sh/wa-.jpg"},
    {"name": "المكسيك", "photo": "https://envs.sh/wOE.jpg"},
    {"name": "لاوس", "photo": "https://envs.sh/wOQ.jpg"},
    {"name": "باكستان", "photo": "https://envs.sh/wOh.jpg"},
    {"name": "الجبل الاسود", "photo": "https://envs.sh/wO2.jpg"},
    {"name": "موزمبيق", "photo": "https://envs.sh/wOi.jpg"},
    {"name": "روسيا", "photo": "https://envs.sh/wOw.jpg"},
    {"name": "افغانستان", "photo": "https://envs.sh/wap.jpg"},
    {"name": "البرتغال", "photo": "https://envs.sh/wac.jpg"},
    {"name": "اندونيسيا", "photo": "https://envs.sh/wO0.jpg"},
    {"name": "الرأس الاخضر", "photo": "https://envs.sh/wOS.jpg"},
    {"name": "هولندا", "photo": "https://envs.sh/wOI.jpg"},
    {"name": "اندونسيا", "photo": "https://envs.sh/wO0.jpg"},
    {"name": "فنلندا", "photo": "https://envs.sh/wmu.jpg"},
    {"name": "الكونغو الديموقراطية", "photo": "https://envs.sh/wmt.jpg"},
    {"name": "النمسا", "photo": "https://envs.sh/wmP.jpg"},
    {"name": "ايطاليا", "photo": "https://envs.sh/wmq.jpg"},
    {"name": "لوكسمبورغ", "photo": "https://envs.sh/waZ.jpg"},
    {"name": "السعوديه", "photo": "https://envs.sh/wmS.jpg"},
    {"name": "كولومبيا", "photo": "https://envs.sh/wmW.jpg"},
    {"name": "نيجريا", "photo": "https://envs.sh/wmB.jpg"},
    {"name": "نيبال", "photo": "https://envs.sh/wmI.jpg"},
    {"name": "الاردن", "photo": "https://envs.sh/wfl.jpg"},
    {"name": "السويد", "photo": "https://envs.sh/wmA.jpg"},
    {"name": "ليبيريا", "photo": "https://envs.sh/waP.jpg"},
    {"name": "انغولا", "photo": "https://envs.sh/wmc.jpg"},
    {"name": "جيبوتي", "photo": "https://envs.sh/wmZ.jpg"},
    {"name": "المجر", "photo": "https://envs.sh/wfv.jpg"},
    {"name": "سوريا", "photo": "https://envs.sh/wmL.jpg"},
    {"name": "ايرلندا", "photo": "https://envs.sh/wm5.jpg"},
    {"name": "كازاخستان", "photo": "https://envs.sh/wmz.jpg"},
    {"name": "بنين", "photo": "https://envs.sh/wan.jpg"},
    {"name": "بنغلاديش", "photo": "https://envs.sh/wOt.jpg"},
    {"name": "قبرص", "photo": "https://envs.sh/wmk.jpg"},
    {"name": "تنزانيا", "photo": "https://envs.sh/wm8.jpg"},
    {"name": "افريقيا الوسطى", "photo": "https://envs.sh/wm7.jpg"},
    {"name": "مقدونيا", "photo": "https://envs.sh/PgC.jpg"},
    {"name": "موريتانيا", "photo": "https://envs.sh/wmr.jpg"},
    {"name": "غنيا الاستوائية", "photo": "https://envs.sh/wms.jpg"},
    {"name": "فرنسا", "photo": "https://envs.sh/wMF.jpg"},
    {"name": "اليابان", "photo": "https://envs.sh/wMt.jpg"},
    {"name": "فيتنام", "photo": "https://envs.sh/wMi.jpg"},
    {"name": "مالطا", "photo": "https://envs.sh/wMP.jpg"},
    {"name": "تايوان", "photo": "https://envs.sh/wM0.jpg"},
    {"name": "بوروندي", "photo": "https://envs.sh/wMB.jpg"},
    {"name": "مالاوي", "photo": "https://envs.sh/wMT.jpg"},
    {"name": "اثيوبيا", "photo": "https://envs.sh/wMp.jpg"},
    {"name": "لبنان", "photo": "https://envs.sh/wM_.jpg"},
    {"name": "البانيا", "photo": "https://envs.sh/wMj.jpg"},
    {"name": "تايلاند", "photo": "https://envs.sh/wMc.jpg"},
    {"name": "جنوب افريقيا", "photo": "https://envs.sh/wMZ.jpg"},
    {"name": "طاجيكستان", "photo": "https://envs.sh/wfk.jpg"},
    {"name": "تونس", "photo": "https://envs.sh/wab.jpg"},
    {"name": "استراليا", "photo": "https://envs.sh/wMK.jpg"},
    {"name": "السودان", "photo": "https://envs.sh/wM3.jpg"},
    {"name": "غانا", "photo": "https://envs.sh/wMC.jpg"},
    {"name": "الفاتيكان", "photo": "https://envs.sh/wfJ.jpg"},
    {"name": "قطر", "photo": "https://envs.sh/wM4.jpg"},
    {"name": "الجزائر", "photo": "https://envs.sh/wMU.jpg"},
    {"name": "جزر القمر", "photo": "https://envs.sh/wMk.jpg"},
    {"name": "البوسنه", "photo": "https://envs.sh/waL.jpg"},
    {"name": "الدنمارك", "photo": "https://envs.sh/wfm.jpg"},
    {"name": "صربيا", "photo": "https://envs.sh/wM8.jpg"},
    {"name": "البحرين", "photo": "https://envs.sh/wOu.jpg"},
    {"name": "سنغافورة", "photo": "https://envs.sh/wMo.jpg"},
    {"name": "ايران", "photo": "https://envs.sh/wMr.jpg"},
    {"name": "جيبوتي", "photo": "https://envs.sh/wmZ.jpg"},
    {"name": "أذربيجاني", "photo": "https://envs.sh/wMN.jpg"},
    {"name": "الارجنتين", "photo": "https://envs.sh/wau.jpg"},
    {"name": "اوغندا", "photo": "https://envs.sh/wfo.jpg"},
    {"name": "الارجنتين", "photo": "https://envs.sh/wmB.jpg"},
    {"name": "بلجيكا", "photo": "https://envs.sh/wMa.jpg"},
    {"name": "ايسلندا", "photo": "https://envs.sh/wMO.jpg"},
    {"name": "تشاد", "photo": "https://envs.sh/wf6.jpg"},
    {"name": "اريتريا", "photo": "https://envs.sh/wMy.jpg"},
    {"name": "سيشل", "photo": "https://envs.sh/wMx.jpg"},
    {"name": "لاوس", "photo": "https://envs.sh/wOQ.jpg"},
    {"name": "الامارات", "photo": "https://envs.sh/wXD.jpg"},
    {"name": "النرويج", "photo": "https://envs.sh/wXE.jpg"},
    {"name": "زامبيا", "photo": "https://envs.sh/wXh.jpg"},
    {"name": "ماليزيا", "photo": "https://envs.sh/wfz.jpg"},
    {"name": "المانيا", "photo": "https://envs.sh/wXd.jpg"},
    {"name": "السنغال", "photo": "https://envs.sh/waj.jpg"},
    {"name": "اوكرانيا", "photo": "https://envs.sh/wXu.jpg"},
    {"name": "الصومال", "photo": "https://envs.sh/wXt.jpg"},
    {"name": "بوركينافاسو", "photo": "https://envs.sh/wXb.jpg"},
    {"name": "ليتوانيا", "photo": "https://envs.sh/waD.jpg"},
    {"name": "سلوفينيا", "photo": "https://envs.sh/wVY.jpg"},
    {"name": "ليبيا", "photo": "https://envs.sh/wVJ.jpg"},
    {"name": "جزر المالديف", "photo": "https://envs.sh/wVo.jpg"},
    {"name": "كندا", "photo": "https://envs.sh/wVs.jpg"},
    {"name": "روسيا", "photo": "https://envs.sh/wOw.jpg"},
    {"name": "اليونان", "photo": "https://envs.sh/wVH.jpg"}
]

points = {}  

@app.on_message(filters.command(["اعلام", "علم","أعلام 🇪🇬"], ""), group=101237782131)
async def aalame(client, message):
    actor = random.choice(patos)
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    cpaesr2[user_id] = actor['name']
    upsrs2[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا العلم...؟ ")

@app.on_message(filters.text, group=11026439870)
async def alamy(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in upsrs2:
        correct_actor = cpaesr2.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            points[user_id]= points.get(user_id, 0) + 1
            await message.reply_text(f"**◍ الإجابة صحيحة ✅\n◍ الأن معك {points[user_id]} نقاط 🔹\n√**")
            del cpaesr2[user_id]
            del upsrs2[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"◍ عذرا عزيزي اجابتك خطا ❌\n◍ الاجابة الصحيحة هي [{correct_actor}] ✅\n√")
                del cpaesr2[user_id]
                del upsrs2[user_id]


c0aesar = {}              
u0sers = {}        

ph0otos = [
    {"name": "محمد سعد", "photo": "https://envs.sh/wl8.jpg"},
    {"name": "نرمين الفقي", "photo": "https://envs.sh/wlJ.jpg"},
    {"name": "عبله كامل", "photo": "https://envs.sh/wlr.jpg"},
    {"name": "دينا الشربيني", "photo": "https://envs.sh/wls.jpg"},
    {"name": "ليلي احمد زاهر", "photo": "https://envs.sh/wl9.jpg"},
    {"name": "روبي", "photo": "https://envs.sh/wlv.jpg"},
    {"name": "غاده عادل", "photo": "https://envs.sh/wlN.jpg"},
    {"name": "ياسمين عبد العزيز", "photo": "https://envs.sh/wlH.jpg"},
    {"name": "اسماء جلال", "photo": "https://envs.sh/wlg.jpg"},
    {"name": "امينه خليل", "photo": "https://envs.sh/wla.jpg"},
    {"name": "احمد فهمي", "photo": "https://envs.sh/PHf.jpg"},
    {"name": "رنا رئيس", "photo": "https://envs.sh/wlM.jpg"},
    {"name": "باسم سمره", "photo": "https://envs.sh/wlX.jpg"},
    {"name": "محمد سلام", "photo": "https://envs.sh/wly.jpg"},
    {"name": "ميرنا نور الدين", "photo": "https://envs.sh/wlV.jpg"},
    {"name": "رشدي اباظه", "photo": "https://envs.sh/wlx.jpg"},
    {"name": "كريم عبد العزيز", "photo": "https://envs.sh/PgJ.jpg"},
    {"name": "ملك قوره", "photo": "https://envs.sh/wkE.jpg"},
    {"name": "هدي المفتي", "photo": "https://envs.sh/wkD.jpg"},
    {"name": "اسماء ابو اليزيد", "photo": "https://envs.sh/wkQ.jpg"},
    {"name": "عمرو عبد الجليل", "photo": "https://envs.sh/wkd.jpg"},
    {"name": "محمد هنيدي", "photo": "https://envs.sh/wkF.jpg"},
    {"name": "حسين فهمي", "photo": "https://envs.sh/wkb.jpg"},
    {"name": "ماجد الكدواني", "photo": "https://envs.sh/wki.jpg"},
    {"name": "مصطفي خاطر", "photo": "https://envs.sh/wkw.jpg"},
    {"name": "اثر ياسين", "photo": "https://envs.sh/wkq.jpg"},
    {"name": "كارولين عزمي", "photo": "https://envs.sh/wk0.jpg"},
    {"name": "احمد ذكي", "photo": "https://envs.sh/wkS.jpg"},
    {"name": "رانيا يوسف", "photo": "https://envs.sh/wkB.jpg"},
    {"name": "ريهام عبد الغفور", "photo": "https://envs.sh/wkT.jpg"},
    {"name": "هاجر احمد", "photo": "https://envs.sh/wkn.jpg"},
    {"name": "زينه", "photo": "https://envs.sh/wkp.jpg"},
    {"name": "ريهام حجاج", "photo": "https://envs.sh/wkA.jpg"},
    {"name": "يسرا اللوزي", "photo": "https://envs.sh/wk_.jpg"},
    {"name": "هنا الزاهد", "photo": "https://envs.sh/wkL.jpg"},
    {"name": "رحاب الجمل", "photo": "https://envs.sh/wk5.jpg"},
    {"name": "مي الغيطي", "photo": "https://envs.sh/wkY.jpg"},
    {"name": "مني ذكي", "photo": "https://envs.sh/wkC.jpg"},
    {"name": "مروه انور", "photo": "https://envs.sh/wkR.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/wk1.jpg"},
    {"name": "شريف منير", "photo": "https://envs.sh/wk4.jpg"},
    {"name": "شيري عادل", "photo": "https://envs.sh/PHg.jpg"},
    {"name": "شيماء سيف", "photo": "https://envs.sh/wkU.jpg"},
    {"name": "هاني سلامه", "photo": "https://envs.sh/wk8.jpg"},
    {"name": "كريم فهمي", "photo": "https://envs.sh/wko.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/PHa.jpg"},
    {"name": "شيرين رضا", "photo": "https://envs.sh/PHO.jpg"},
    {"name": "هنا شيحه", "photo": "https://envs.sh/wkf.jpg"},
    {"name": "احمد عز", "photo": "https://envs.sh/wkm.jpg"},
    {"name": "داليا البحيري", "photo": "https://envs.sh/wkX.jpg"},
    {"name": "نور ايهاب", "photo": "https://envs.sh/wky.jpg"},
    {"name": "هاني رمزي", "photo": "https://envs.sh/wkx.jpg"},
    {"name": "امير كراره", "photo": "https://envs.sh/w8h.jpg"},
    {"name": "ايه سماحه", "photo": "https://envs.sh/w82.jpg"},
    {"name": "خالد الصاوي", "photo": "https://envs.sh/w8u.jpg"},
    {"name": "عادل امام", "photo": "https://envs.sh/w8F.jpg"},
    {"name": "نيلي كريم", "photo": "https://envs.sh/w8I.jpg"},
    {"name": "ياسمين صبري", "photo": "https://envs.sh/Pgd.jpg"},
    {"name": "احمد السقا", "photo": "https://envs.sh/w8p.jpg"},
    {"name": "سيد رجب", "photo": "https://envs.sh/w8_.jpg"},
    {"name": "حنان مطاوع", "photo": "https://envs.sh/w8s.jpg"},
    {"name": "عمر يوسف", "photo": "https://envs.sh/w8a.jpg"},
    {"name": "عمرو واكد", "photo": "https://envs.sh/w8O.jpg"},
    {"name": "سلمي ابو ضيف", "photo": "https://envs.sh/w8m.jpg"},
    {"name": "اكرم حسني", "photo": "https://envs.sh/w8X.jpg"},
    {"name": "ساره الشامي", "photo": "https://envs.sh/w8y.jpg"},
    {"name": "نور", "photo": "https://envs.sh/w86.jpg"},
    {"name": "احمد خاتم", "photo": "https://envs.sh/w8x.jpg"}
]

@app.on_message(filters.command(["ممثل", "ممثلين","ممثلين 🕺🏻"], ""), group=1024682131)
async def dhjfyuh(client, message):
    actor = random.choice(ph0otos)
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    c0aesar[user_id] = actor['name']
    u0sers[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا الممثل...؟ ")

@app.on_message(filters.text, group=10790430)
async def yfugry(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in u0sers:
        correct_actor = c0aesar.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text(f"**◍ الإجابة صحيحة ✅\n◍ الأن معك {points[user_id]} نقاط 🔹\n√**")
            points[user_id]= points.get(user_id, 0) + 1
            del c0aesar[user_id]
            del u0sers[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"◍ عذرا عزيزي اجابتك خطا ❌\n◍ الاجابة الصحيحة هي [{correct_actor}] ✅\n√")
                del c0aesar[user_id]
                del u0sers[user_id]

caesar1 = {}              
users1 = {}        

potss = [
    {"name": "بهاء سلطان", "photo": "https://envs.sh/wvE.jpg"},
    {"name": "محمد فؤاد", "photo": "https://envs.sh/wvh.jpg"},
    {"name":"شرين", "photo": "https://envs.sh/w9R.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/w9v.jpg"},
    {"name": "عمرو دياب", "photo": "https://envs.sh/wvF.jpg"},
    {"name": "اصاله", "photo": "https://envs.sh/PMT.jpg"},
    {"name": "عامر منيب", "photo": "https://envs.sh/wve.jpg"},
    {"name": "تامر حسني", "photo": "https://envs.sh/wNj.jpg"},
    {"name": "مدحت صالح", "photo": "https://envs.sh/wNL.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/wNG.jpg"},
    {"name": "محمد سعيد", "photo": "https://envs.sh/wNz.jpg"},
    {"name": "مصطفى قمر", "photo": "https://envs.sh/wNY.jpg"},
    {"name": "المغيني", "photo": "https://envs.sh/wHt.jpg"},
    {"name": "حكيم", "photo": "https://envs.sh/wHe.jpg"},
    {"name": "كاظم الساهر", "photo": "https://envs.sh/wHi.jpg"},
    {"name": "تامر عاشور", "photo": "https://envs.sh/wHw.jpg"},
    {"name": "هاني شاكر", "photo": "https://envs.sh/wHS.jpg"},
    {"name": "حسين الجسمي", "photo": "https://envs.sh/wHI.jpg"},
    {"name": "محمد منير", "photo": "https://envs.sh/PMi.jpg"},
    {"name": "رامي صبري", "photo": "https://envs.sh/wHn.jpg"},
    {"name": "ويجز", "photo": "https://envs.sh/Pf2.jpg"},
    {"name": "رامي جمال", "photo": "https://envs.sh/wHT.jpg"},
    {"name": "احمد شيبه", "photo": "https://envs.sh/PgX.jpg"},
    {"name": "نانسي عجرم", "photo": "https://envs.sh/wHp.jpg"},
    {"name": "راغب علامه", "photo": "https://envs.sh/wH_.jpg"},
    {"name": "عبد الحليم حافظ", "photo": "https://envs.sh/PfF.jpg"},
    {"name": "امال ماهر", "photo": "https://envs.sh/wHj.jpg"},
    {"name": "عبدالرحمن محمد", "photo": "https://envs.sh/Pga.jpg"},
    {"name": "احمد سعد", "photo": "https://envs.sh/wHZ.jpg"},
    {"name": "كارول سماحه", "photo": "https://envs.sh/wHL.jpg"},
    {"name": "ادهم نابلسي", "photo": "https://envs.sh/Pfi.jpg"},
    {"name": "محمود العسيلي", "photo": "https://envs.sh/Pg9.jpg"},
    {"name": "انغام", "photo": "https://envs.sh/wHG.jpg"},
    {"name": "كارمن سليمان", "photo": "https://envs.sh/wHz.jpg"},
    {"name": "سعد المجرد", "photo": "https://envs.sh/wHC.jpg"},
    {"name": "فيروز", "photo": "https://envs.sh/Pgm.jpg"},
    {"name": "ام كلثوم", "photo": "https://envs.sh/wH4.jpg"},
    {"name": "حماده هلال", "photo": "https://envs.sh/PMn.jpg"},
    {"name": "كايروكي", "photo": "https://envs.sh/wHk.jpg"},
    {"name": "لؤي", "photo": "https://envs.sh/wH8.jpg"},
    {"name": "ارسينك", "photo": "https://envs.sh/wH7.jpg"},
    {"name": "عاصي الحلاني", "photo": "https://envs.sh/PMB.jpg"},
    {"name": "احلام", "photo": "https://envs.sh/wHJ.jpg"},
    {"name": "اليسا", "photo": "https://envs.sh/wvB.jpg"},
    {"name": "محمد حماقي", "photo": "https://envs.sh/wHo.jpg"},
    {"name": "احمد مكي", "photo": "https://envs.sh/wHr.jpg"},
    {"name": "ابو الانوار", "photo": "https://envs.sh/PMb.jpg"}
]

@app.on_message(filters.command(["مغنين", "مغاني","مغنين 👨‍🎤"], ""), group=107082131)
async def moganen(client, message):
    actor = random.choice(potss)
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    caesar1[user_id] = actor['name']
    users1[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا المغني...؟ ")

@app.on_message(filters.text, group=10126430)
async def mogany(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in users1:
        correct_actor = caesar1.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text(f"**◍ الإجابة صحيحة ✅\n◍ الأن معك {points[user_id]} نقاط 🔹\n√**")
            points[user_id]= points.get(user_id, 0) + 1
            del caesar1[user_id]
            del users1[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"◍ عذرا عزيزي اجابتك خطا ❌\n◍ الاجابة الصحيحة هي [{correct_actor}] ✅\n√")
                del caesar1[user_id]
                del users1[user_id]



            
caesar3 = {}              
users3 = {}        

photn = [
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "حسين الشحات", "photo": "https://envs.sh/wHM.jpg"},
    {"name": "كهربا", "photo": "https://envs.sh/wHX.jpg"},
    {"name": "هاري كين", "photo": "https://envs.sh/PmT.jpg"},
    {"name": "رياض محرز", "photo": "https://envs.sh/wHy.jpg"},
    {"name": "حمدي فتحي", "photo": "https://envs.sh/wH6.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "داني الفيس", "photo": "https://envs.sh/wg2.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "فابينيو", "photo": "https://envs.sh/wgF.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "طاهر محمد", "photo": "https://envs.sh/POa.jpg"},
    {"name": "مارسيلو", "photo": "https://envs.sh/wge.jpg"},
    {"name": "أفشة", "photo": "https://envs.sh/PyU.jpg"},
    {"name": "سيرجيو بوسكيتس", "photo": "https://envs.sh/wDP.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "انطونيو جريزمان", "photo": "https://envs.sh/wgw.jpg"},
    {"name": "احمد حسام ميدو", "photo": "https://envs.sh/Py9.jpg"},
    {"name": "أدريان رابيو", "photo": "https://envs.sh/PyR.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "مانويل نوير", "photo": "https://envs.sh/Py1.jpg"},
    {"name": "رافاييل فاران", "photo": "https://envs.sh/PmW.jpg"},
    {"name": "توني كروس", "photo": "https://envs.sh/wgB.jpg"},
    {"name": "جاريث بيل", "photo": "https://envs.sh/Pyo.jpg"},
    {"name": "نيمار", "photo": "https://envs.sh/wgT.jpg"},
    {"name": "كارفاخال", "photo": "https://envs.sh/Pmm.jpg"},
    {"name": "دي ماريا", "photo": "https://envs.sh/Py0.jpg"},
    {"name": "زين الدين زيدان", "photo": "https://envs.sh/Py4.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "حكيم زياش", "photo": "https://envs.sh/wgZ.jpg"},
    {"name": "جونزالو هيجواين", "photo": "https://envs.sh/wgL.jpg"},
    {"name": "جوردي ألبا", "photo": "https://envs.sh/wgG.jpg"},
    {"name": "باولو ديبالا", "photo": "https://envs.sh/wgK.jpg"},
    {"name": "دييجو كوستا", "photo": "https://envs.sh/Pys.jpg"},
    {"name": "بيليه", "photo": "https://envs.sh/Pme.jpg"},
    {"name": "هالاند", "photo": "https://envs.sh/PmO.jpg"},
    {"name": "بول بوجبا", "photo": "https://envs.sh/wgz.jpg"},
    {"name": "إدين هازارد", "photo": "https://envs.sh/wg3.jpg"},
    {"name": "نجولو كانتي", "photo": "https://envs.sh/PmV.jpg"},
    {"name": "عصام الحضري", "photo": "https://envs.sh/wgY.jpg"},
    {"name": "لوكاكو", "photo": "https://envs.sh/POg.jpg"},
    {"name": "إنييستا", "photo": "https://envs.sh/wgC.jpg"},
    {"name": "اسماعيل بن ناصر", "photo": "https://envs.sh/wgR.jpg"},
    {"name": "ساديو ماني", "photo": "https://envs.sh/wg1.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ريفالدو", "photo": "https://envs.sh/Pyk.jpg"},
    {"name": "لورينزو إنسيني", "photo": "https://envs.sh/Pyw.jpg"},
    {"name": "جابرييل جيسوس", "photo": "https://envs.sh/Pmc.jpg"},
    {"name": "أرتورو فيدال", "photo": "https://envs.sh/wgU.jpg"},
    {"name": "ماتس هاملز", "photo": "https://envs.sh/wgl.jpg"},
    {"name": "تيو كورتوا", "photo": "https://envs.sh/wgk.jpg"},
    {"name": "ماركو اسينسيو", "photo": "https://envs.sh/wg8.jpg"},
    {"name": "محمد النيني", "photo": "https://envs.sh/Pyr.jpg"},
    {"name": "محمد صلاح", "photo": "https://envs.sh/POO.jpg"},
    {"name": "فيليب كوتينيو", "photo": "https://envs.sh/wgJ.jpg"},
    {"name": "مسعود اوزيل", "photo": "https://envs.sh/PyI.jpg"},
    {"name": "ماركوس راشفورد", "photo": "https://envs.sh/wgo.jpg"},
    {"name": "بونو", "photo": "https://envs.sh/wgr.jpg"},
    {"name": "لوكا مودريتش", "photo": "https://envs.sh/wg9.jpg"},
    {"name": "نيمانيا ماتيتش", "photo": "https://envs.sh/PmP.jpg"},
    {"name": "سيرجيو أجويرو", "photo": "https://envs.sh/wgv.jpg"},
    {"name": "إيفان راكيتيتش", "photo": "https://envs.sh/wgN.jpg"},
    {"name": "ميسي", "photo": "https://envs.sh/wgH.jpg"},
    {"name": "بيكيه", "photo": "https://envs.sh/Pgg.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "كرويف", "photo": "https://envs.sh/wgg.jpg"},
    {"name": "رادجا ناينجولان", "photo": "https://envs.sh/Px6.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "كاسيميرو", "photo": "https://envs.sh/wgm.jpg"},
    {"name": "جيمي فاردي", "photo": "https://envs.sh/wgX.jpg"},
    {"name": "ليروي ساني", "photo": "https://envs.sh/wgy.jpg"},
    {"name": "آلابا", "photo": "https://envs.sh/wgx.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ديلي آلي", "photo": "https://envs.sh/Pyb.jpg"},
    {"name": "جوتا", "photo": "https://envs.sh/wfD.jpg"},
    {"name": "علي معلول", "photo": "https://envs.sh/wfE.jpg"},
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "مارادونا", "photo": "https://envs.sh/Py_.jpg"},
    {"name": "جورجيو كيليني", "photo": "https://envs.sh/Pyu.jpg"},
    {"name": "سيرجيو راموس", "photo": "https://envs.sh/PME.jpg"},
    {"name": "صامويل أومتيتي", "photo": "https://envs.sh/PmX.jpg"},
    {"name": "زلاتان", "photo": "https://envs.sh/Pyt.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "اشرف حكيمي", "photo": "https://envs.sh/wfh.jpg"},
    {"name": "نايف اكرد", "photo": "https://envs.sh/Pmt.jpg"},
    {"name": "ماورو إيكاردي", "photo": "https://envs.sh/PyW.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "فودين", "photo": "https://envs.sh/Py8.jpg"},
    {"name": "لويس سواريز", "photo": "https://envs.sh/wf2.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "كريستيانو رونالدو", "photo": "https://envs.sh/PO6.jpg"},
    {"name": "كفين دي بروين", "photo": "https://envs.sh/Pmx.jpg"},
    {"name": "آريين روبن", "photo": "https://envs.sh/wfe.jpg"}
]

@app.on_message(filters.command(["لاعبين", "لاعب","لاعبين ⛹🏻‍♂️"], ""), group=9827065)
async def laaban(client, message):
    actor = random.choice(photn)
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    caesar3[user_id] = actor['name']
    users3[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا الاعب..؟ ")

@app.on_message(filters.text, group=458678)
async def alaeb(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in users3:
        correct_actor = caesar3.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text(f"**◍ الإجابة صحيحة ✅\n◍ الأن معك {points[user_id]} نقاط 🔹\n√**")
            points[user_id]= points.get(user_id, 0) + 1
            del caesar3[user_id]
            del users3[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"◍ عذرا عزيزي اجابتك خطا ❌\n◍ الاجابة الصحيحة هي [{correct_actor}] ✅\n√")
                del caesar3[user_id]
                del users3[user_id]




cesar4 = {}              
urers4 = {}        

soraa = [
    {"name": "بهاء سلطان", "photo": "https://envs.sh/wvE.jpg"},
    {"name": "محمد فؤاد", "photo": "https://envs.sh/wvh.jpg"},
    {"name":"شرين", "photo": "https://envs.sh/w9R.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/w9v.jpg"},
    {"name": "عمرو دياب", "photo": "https://envs.sh/wvF.jpg"},
    {"name": "اصاله", "photo": "https://envs.sh/PMT.jpg"},
    {"name": "عامر منيب", "photo": "https://envs.sh/wve.jpg"},
    {"name": "تامر حسني", "photo": "https://envs.sh/wNj.jpg"},
    {"name": "مدحت صالح", "photo": "https://envs.sh/wNL.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/wNG.jpg"},
    {"name": "محمد سعيد", "photo": "https://envs.sh/wNz.jpg"},
    {"name": "مصطفى قمر", "photo": "https://envs.sh/wNY.jpg"},
    {"name": "المغيني", "photo": "https://envs.sh/wHt.jpg"},
    {"name": "حكيم", "photo": "https://envs.sh/wHe.jpg"},
    {"name": "كاظم الساهر", "photo": "https://envs.sh/wHi.jpg"},
    {"name": "تامر عاشور", "photo": "https://envs.sh/wHw.jpg"},
    {"name": "هاني شاكر", "photo": "https://envs.sh/wHS.jpg"},
    {"name": "حسين الجسمي", "photo": "https://envs.sh/wHI.jpg"},
    {"name": "محمد منير", "photo": "https://envs.sh/PMi.jpg"},
    {"name": "رامي صبري", "photo": "https://envs.sh/wHn.jpg"},
    {"name": "ويجز", "photo": "https://envs.sh/Pf2.jpg"},
    {"name": "رامي جمال", "photo": "https://envs.sh/wHT.jpg"},
    {"name": "احمد شيبه", "photo": "https://envs.sh/PgX.jpg"},
    {"name": "نانسي عجرم", "photo": "https://envs.sh/wHp.jpg"},
    {"name": "راغب علامه", "photo": "https://envs.sh/wH_.jpg"},
    {"name": "عبد الحليم حافظ", "photo": "https://envs.sh/PfF.jpg"},
    {"name": "امال ماهر", "photo": "https://envs.sh/wHj.jpg"},
    {"name": "عبدالرحمن محمد", "photo": "https://envs.sh/Pga.jpg"},
    {"name": "احمد سعد", "photo": "https://envs.sh/wHZ.jpg"},
    {"name": "كارول سماحه", "photo": "https://envs.sh/wHL.jpg"},
    {"name": "ادهم نابلسي", "photo": "https://envs.sh/Pfi.jpg"},
    {"name": "محمود العسيلي", "photo": "https://envs.sh/Pg9.jpg"},
    {"name": "انغام", "photo": "https://envs.sh/wHG.jpg"},
    {"name": "كارمن سليمان", "photo": "https://envs.sh/wHz.jpg"},
    {"name": "سعد المجرد", "photo": "https://envs.sh/wHC.jpg"},
    {"name": "فيروز", "photo": "https://envs.sh/Pgm.jpg"},
    {"name": "ام كلثوم", "photo": "https://envs.sh/wH4.jpg"},
    {"name": "حماده هلال", "photo": "https://envs.sh/PMn.jpg"},
    {"name": "كايروكي", "photo": "https://envs.sh/wHk.jpg"},
    {"name": "لؤي", "photo": "https://envs.sh/wH8.jpg"},
    {"name": "ارسينك", "photo": "https://envs.sh/wH7.jpg"},
    {"name": "عاصي الحلاني", "photo": "https://envs.sh/PMB.jpg"},
    {"name": "احلام", "photo": "https://envs.sh/wHJ.jpg"},
    {"name": "اليسا", "photo": "https://envs.sh/wvB.jpg"},
    {"name": "محمد حماقي", "photo": "https://envs.sh/wHo.jpg"},
    {"name": "احمد مكي", "photo": "https://envs.sh/wHr.jpg"},
    {"name": "ابو الانوار", "photo": "https://envs.sh/PMb.jpg"}, 
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "حسين الشحات", "photo": "https://envs.sh/wHM.jpg"},
    {"name": "كهربا", "photo": "https://envs.sh/wHX.jpg"},
    {"name": "هاري كين", "photo": "https://envs.sh/PmT.jpg"},
    {"name": "رياض محرز", "photo": "https://envs.sh/wHy.jpg"},
    {"name": "حمدي فتحي", "photo": "https://envs.sh/wH6.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "داني الفيس", "photo": "https://envs.sh/wg2.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "فابينيو", "photo": "https://envs.sh/wgF.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "طاهر محمد", "photo": "https://envs.sh/POa.jpg"},
    {"name": "مارسيلو", "photo": "https://envs.sh/wge.jpg"},
    {"name": "أفشة", "photo": "https://envs.sh/PyU.jpg"},
    {"name": "سيرجيو بوسكيتس", "photo": "https://envs.sh/wDP.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "انطونيو جريزمان", "photo": "https://envs.sh/wgw.jpg"},
    {"name": "احمد حسام ميدو", "photo": "https://envs.sh/Py9.jpg"},
    {"name": "أدريان رابيو", "photo": "https://envs.sh/PyR.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "مانويل نوير", "photo": "https://envs.sh/Py1.jpg"},
    {"name": "رافاييل فاران", "photo": "https://envs.sh/PmW.jpg"},
    {"name": "توني كروس", "photo": "https://envs.sh/wgB.jpg"},
    {"name": "جاريث بيل", "photo": "https://envs.sh/Pyo.jpg"},
    {"name": "نيمار", "photo": "https://envs.sh/wgT.jpg"},
    {"name": "كارفاخال", "photo": "https://envs.sh/Pmm.jpg"},
    {"name": "دي ماريا", "photo": "https://envs.sh/Py0.jpg"},
    {"name": "زين الدين زيدان", "photo": "https://envs.sh/Py4.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "حكيم زياش", "photo": "https://envs.sh/wgZ.jpg"},
    {"name": "جونزالو هيجواين", "photo": "https://envs.sh/wgL.jpg"},
    {"name": "جوردي ألبا", "photo": "https://envs.sh/wgG.jpg"},
    {"name": "باولو ديبالا", "photo": "https://envs.sh/wgK.jpg"},
    {"name": "دييجو كوستا", "photo": "https://envs.sh/Pys.jpg"},
    {"name": "بيليه", "photo": "https://envs.sh/Pme.jpg"},
    {"name": "هالاند", "photo": "https://envs.sh/PmO.jpg"},
    {"name": "بول بوجبا", "photo": "https://envs.sh/wgz.jpg"},
    {"name": "إدين هازارد", "photo": "https://envs.sh/wg3.jpg"},
    {"name": "نجولو كانتي", "photo": "https://envs.sh/PmV.jpg"},
    {"name": "عصام الحضري", "photo": "https://envs.sh/wgY.jpg"},
    {"name": "لوكاكو", "photo": "https://envs.sh/POg.jpg"},
    {"name": "إنييستا", "photo": "https://envs.sh/wgC.jpg"},
    {"name": "اسماعيل بن ناصر", "photo": "https://envs.sh/wgR.jpg"},
    {"name": "ساديو ماني", "photo": "https://envs.sh/wg1.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ريفالدو", "photo": "https://envs.sh/Pyk.jpg"},
    {"name": "لورينزو إنسيني", "photo": "https://envs.sh/Pyw.jpg"},
    {"name": "جابرييل جيسوس", "photo": "https://envs.sh/Pmc.jpg"},
    {"name": "أرتورو فيدال", "photo": "https://envs.sh/wgU.jpg"},
    {"name": "ماتس هاملز", "photo": "https://envs.sh/wgl.jpg"},
    {"name": "تيو كورتوا", "photo": "https://envs.sh/wgk.jpg"},
    {"name": "ماركو اسينسيو", "photo": "https://envs.sh/wg8.jpg"},
    {"name": "محمد النيني", "photo": "https://envs.sh/Pyr.jpg"},
    {"name": "محمد صلاح", "photo": "https://envs.sh/POO.jpg"},
    {"name": "فيليب كوتينيو", "photo": "https://envs.sh/wgJ.jpg"},
    {"name": "مسعود اوزيل", "photo": "https://envs.sh/PyI.jpg"},
    {"name": "ماركوس راشفورد", "photo": "https://envs.sh/wgo.jpg"},
    {"name": "بونو", "photo": "https://envs.sh/wgr.jpg"},
    {"name": "لوكا مودريتش", "photo": "https://envs.sh/wg9.jpg"},
    {"name": "نيمانيا ماتيتش", "photo": "https://envs.sh/PmP.jpg"},
    {"name": "سيرجيو أجويرو", "photo": "https://envs.sh/wgv.jpg"},
    {"name": "إيفان راكيتيتش", "photo": "https://envs.sh/wgN.jpg"},
    {"name": "ميسي", "photo": "https://envs.sh/wgH.jpg"},
    {"name": "بيكيه", "photo": "https://envs.sh/Pgg.jpg"},
    {"name": "كيليان مبابي", "photo": "https://envs.sh/PyC.jpg"},
    {"name": "ابوتريكه", "photo": "https://envs.sh/Py7.jpg"},
    {"name": "كرويف", "photo": "https://envs.sh/wgg.jpg"},
    {"name": "رادجا ناينجولان", "photo": "https://envs.sh/Px6.jpg"},
    {"name": "أوباميانج", "photo": "https://envs.sh/wg_.jpg"},
    {"name": "كاسيميرو", "photo": "https://envs.sh/wgm.jpg"},
    {"name": "جيمي فاردي", "photo": "https://envs.sh/wgX.jpg"},
    {"name": "ليروي ساني", "photo": "https://envs.sh/wgy.jpg"},
    {"name": "آلابا", "photo": "https://envs.sh/wgx.jpg"},
    {"name": "شيكابالا", "photo": "https://envs.sh/wg4.jpg"},
    {"name": "ديلي آلي", "photo": "https://envs.sh/Pyb.jpg"},
    {"name": "جوتا", "photo": "https://envs.sh/wfD.jpg"},
    {"name": "علي معلول", "photo": "https://envs.sh/wfE.jpg"},
    {"name": "سالم الدوسري", "photo": "https://envs.sh/PyF.jpg"},
    {"name": "مارادونا", "photo": "https://envs.sh/Py_.jpg"},
    {"name": "جورجيو كيليني", "photo": "https://envs.sh/Pyu.jpg"},
    {"name": "سيرجيو راموس", "photo": "https://envs.sh/PME.jpg"},
    {"name": "صامويل أومتيتي", "photo": "https://envs.sh/PmX.jpg"},
    {"name": "زلاتان", "photo": "https://envs.sh/Pyt.jpg"},
    {"name": "روبرت ليفاندوفسكي", "photo": "https://envs.sh/wHO.jpg"},
    {"name": "اشرف حكيمي", "photo": "https://envs.sh/wfh.jpg"},
    {"name": "نايف اكرد", "photo": "https://envs.sh/Pmt.jpg"},
    {"name": "ماورو إيكاردي", "photo": "https://envs.sh/PyW.jpg"},
    {"name": "كريم بنزيما", "photo": "https://envs.sh/wgW.jpg"},
    {"name": "فودين", "photo": "https://envs.sh/Py8.jpg"},
    {"name": "لويس سواريز", "photo": "https://envs.sh/wf2.jpg"},
    {"name": "محمد شريف", "photo": "https://envs.sh/wgb.jpg"},
    {"name": "الشناوي", "photo": "https://envs.sh/wgt.jpg"},
    {"name": "كريستيانو رونالدو", "photo": "https://envs.sh/PO6.jpg"},
    {"name": "كفين دي بروين", "photo": "https://envs.sh/Pmx.jpg"},
    {"name": "آريين روبن", "photo": "https://envs.sh/wfe.jpg"}, 
    {"name": "محمد سعد", "photo": "https://envs.sh/wl8.jpg"},
    {"name": "نرمين الفقي", "photo": "https://envs.sh/wlJ.jpg"},
    {"name": "عبله كامل", "photo": "https://envs.sh/wlr.jpg"},
    {"name": "دينا الشربيني", "photo": "https://envs.sh/wls.jpg"},
    {"name": "ليلي احمد زاهر", "photo": "https://envs.sh/wl9.jpg"},
    {"name": "روبي", "photo": "https://envs.sh/wlv.jpg"},
    {"name": "غاده عادل", "photo": "https://envs.sh/wlN.jpg"},
    {"name": "ياسمين عبد العزيز", "photo": "https://envs.sh/wlH.jpg"},
    {"name": "اسماء جلال", "photo": "https://envs.sh/wlg.jpg"},
    {"name": "امينه خليل", "photo": "https://envs.sh/wla.jpg"},
    {"name": "احمد فهمي", "photo": "https://envs.sh/PHf.jpg"},
    {"name": "رنا رئيس", "photo": "https://envs.sh/wlM.jpg"},
    {"name": "باسم سمره", "photo": "https://envs.sh/wlX.jpg"},
    {"name": "محمد سلام", "photo": "https://envs.sh/wly.jpg"},
    {"name": "ميرنا نور الدين", "photo": "https://envs.sh/wlV.jpg"},
    {"name": "رشدي اباظه", "photo": "https://envs.sh/wlx.jpg"},
    {"name": "كريم عبد العزيز", "photo": "https://envs.sh/PgJ.jpg"},
    {"name": "ملك قوره", "photo": "https://envs.sh/wkE.jpg"},
    {"name": "هدي المفتي", "photo": "https://envs.sh/wkD.jpg"},
    {"name": "اسماء ابو اليزيد", "photo": "https://envs.sh/wkQ.jpg"},
    {"name": "عمرو عبد الجليل", "photo": "https://envs.sh/wkd.jpg"},
    {"name": "محمد هنيدي", "photo": "https://envs.sh/wkF.jpg"},
    {"name": "حسين فهمي", "photo": "https://envs.sh/wkb.jpg"},
    {"name": "ماجد الكدواني", "photo": "https://envs.sh/wki.jpg"},
    {"name": "مصطفي خاطر", "photo": "https://envs.sh/wkw.jpg"},
    {"name": "اثر ياسين", "photo": "https://envs.sh/wkq.jpg"},
    {"name": "كارولين عزمي", "photo": "https://envs.sh/wk0.jpg"},
    {"name": "احمد ذكي", "photo": "https://envs.sh/wkS.jpg"},
    {"name": "رانيا يوسف", "photo": "https://envs.sh/wkB.jpg"},
    {"name": "ريهام عبد الغفور", "photo": "https://envs.sh/wkT.jpg"},
    {"name": "هاجر احمد", "photo": "https://envs.sh/wkn.jpg"},
    {"name": "زينه", "photo": "https://envs.sh/wkp.jpg"},
    {"name": "ريهام حجاج", "photo": "https://envs.sh/wkA.jpg"},
    {"name": "يسرا اللوزي", "photo": "https://envs.sh/wk_.jpg"},
    {"name": "هنا الزاهد", "photo": "https://envs.sh/wkL.jpg"},
    {"name": "رحاب الجمل", "photo": "https://envs.sh/wk5.jpg"},
    {"name": "مي الغيطي", "photo": "https://envs.sh/wkY.jpg"},
    {"name": "مني ذكي", "photo": "https://envs.sh/wkC.jpg"},
    {"name": "مروه انور", "photo": "https://envs.sh/wkR.jpg"},
    {"name": "محمد رمضان", "photo": "https://envs.sh/wk1.jpg"},
    {"name": "شريف منير", "photo": "https://envs.sh/wk4.jpg"},
    {"name": "شيري عادل", "photo": "https://envs.sh/PHg.jpg"},
    {"name": "شيماء سيف", "photo": "https://envs.sh/wkU.jpg"},
    {"name": "هاني سلامه", "photo": "https://envs.sh/wk8.jpg"},
    {"name": "كريم فهمي", "photo": "https://envs.sh/wko.jpg"},
    {"name": "احمد حلمي", "photo": "https://envs.sh/PHa.jpg"},
    {"name": "شيرين رضا", "photo": "https://envs.sh/PHO.jpg"},
    {"name": "هنا شيحه", "photo": "https://envs.sh/wkf.jpg"},
    {"name": "احمد عز", "photo": "https://envs.sh/wkm.jpg"},
    {"name": "داليا البحيري", "photo": "https://envs.sh/wkX.jpg"},
    {"name": "نور ايهاب", "photo": "https://envs.sh/wky.jpg"},
    {"name": "هاني رمزي", "photo": "https://envs.sh/wkx.jpg"},
    {"name": "امير كراره", "photo": "https://envs.sh/w8h.jpg"},
    {"name": "ايه سماحه", "photo": "https://envs.sh/w82.jpg"},
    {"name": "خالد الصاوي", "photo": "https://envs.sh/w8u.jpg"},
    {"name": "عادل امام", "photo": "https://envs.sh/w8F.jpg"},
    {"name": "نيلي كريم", "photo": "https://envs.sh/w8I.jpg"},
    {"name": "ياسمين صبري", "photo": "https://envs.sh/Pgd.jpg"},
    {"name": "احمد السقا", "photo": "https://envs.sh/w8p.jpg"},
    {"name": "سيد رجب", "photo": "https://envs.sh/w8_.jpg"},
    {"name": "حنان مطاوع", "photo": "https://envs.sh/w8s.jpg"},
    {"name": "عمر يوسف", "photo": "https://envs.sh/w8a.jpg"},
    {"name": "عمرو واكد", "photo": "https://envs.sh/w8O.jpg"},
    {"name": "سلمي ابو ضيف", "photo": "https://envs.sh/w8m.jpg"},
    {"name": "اكرم حسني", "photo": "https://envs.sh/w8X.jpg"},
    {"name": "ساره الشامي", "photo": "https://envs.sh/w8y.jpg"},
    {"name": "نور", "photo": "https://envs.sh/w86.jpg"},
    {"name": "احمد خاتم", "photo": "https://envs.sh/w8x.jpg"}
]

@app.on_message(filters.command(["مشاهير", "مشهور","مشاهير 🎩"], ""), group=700953)
async def masher(client, message):
    actor = random.choice(soraa)
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    cesar4[user_id] = actor['name']
    urers4[user_id] = user_id
    await message.reply_photo(photo=actor['photo'], caption="ماهو اسم هذا المشهور...؟ ")

@app.on_message(filters.text, group=75205)
async def mashor(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in urers4:
        correct_actor = cesar4.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text(f"**◍ الإجابة صحيحة ✅\n◍ الأن معك {points[user_id]} نقاط 🔹\n√**")
            points[user_id]= points.get(user_id, 0) + 1
            del cesar4[user_id]
            del urers4[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"◍ عذرا عزيزي اجابتك خطا ❌\n◍ الاجابة الصحيحة هي [{correct_actor}] ✅\n√")
                del cesar4[user_id]
                del urers4[user_id]


uss2 = {}        
cear2 = {}        

qustions = [
    {"photo": "🏨🏨🏨🏨🏨🏣🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨🏨", "name": "🏣"},
    {"photo": "❤️❤️❤️❤️❤️❤️❤️❤️❤️♥️❤️❤️❤️❤️❤️❤️", "name": "♥️"},
    {"photo": "↗️↗️↗️↗️↗️↗️↗️↗️↗️⬆️↗️↗️↗️↗️↗️↗️↗️↗️↗️↗️", "name": "⬆️"},
    {"photo": "🍅🍅🍅🍅🍅🍅🍎🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅🍅", "name": "🍎"},
    {"photo": "📫📫📫📫📫📫📫📪📫📫📫📫📫📫📫📫📫📫📫📫", "name": "📪"},
    {"photo": "🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇬🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫🇳🇫", "name": "🇳🇬"},
    {"photo": "💗💗💗💗💗💗💗💗💗🩷💗💗💗💗💗💗💗", "name": "🩷"},
    {"photo": "🔂🔂🔂🔂🔂🔂🔂🔁🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂🔂", "name": "🔁"},
    {"photo": "😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰😰??😰😰😰😰😰😰😰😰😰😰", "name": "😨"},
    {"photo": "📥📥📥📤📥📥📥📥📥📥📥📥📥📥📥📥", "name": "📤"},
    {"photo": "🦡🦡🦡🦡🦝🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡🦡", "name": "🦝"},
    {"photo": "👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂👮‍♂", "name": "👮"},
    {"photo": "🔼🔼🔼🔼🔼🔼🔽🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼🔼", "name": "🔽"},
    {"photo": "👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕🧑‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕👨‍⚕", "name": "🧑‍⚕"},
    {"photo": "💓💓💓💓💓💓💗💓💓💓💓💓💓💓💓💓💓💓💓", "name": "💗"},
    {"photo": "🚞🚞🚞🚞🚞🚃🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞🚞", "name": "🚃"},
    {"photo": "😫😫😫😫😫😫😩😫😫😫😫😫😫😫😫😫😫😫😫😫😫", "name": "😩"},
    {"photo": "🧚‍♂🧚🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♂", "name": "🧚"},
    {"photo": "😥😥😥😥😥😥😥😢😥😥😥😥😥😥😥😥😥😥😥😥😥", "name": "😢"},
    {"photo": "⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⌛️⏳⌛️⌛️⌛️", "name": "⏳"},
    {"photo": "🦌🦌🦌🦌🦌🦌🦌🐂🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌", "name": "🐂"},
    {"photo": "🌇🌇🌇🌇🌇🌆🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇🌇", "name": "🌆"},
    {"photo": "🌗🌗🌗🌗🌗🌗🌓🌗🌗🌗🌗🌗🌗🌗🌗🌗", "name": "🌓"},
    {"photo": "🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🤭🫢🤭🤭🤭🤭🤭🤭", "name": "🫢"},
    {"photo": "◼️◼️◼️🔳◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️◼️", "name": "🔳"},
    {"photo": "🐓🐓🐓🐓🐓🪿🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓🐓", "name": "🪿"},
    {"photo": "🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂🧖‍♂", "name": "🧖"},
    {"photo": "🛠🛠🛠🛠🛠⚒🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠", "name": "⚒"},
    {"photo": "🕖🕖🕖🕖🕖🕖🕦🕖🕖🕖🕖🕖🕖🕖🕖🕖🕖", "name": "🕦"},
    {"photo": "😏😏😏😏😏😏😒😏😏😏😏😏😏😏😏😏😏😏", "name": "😒"},
    {"photo": "😮😮😮😮😮😮😮😦😮😮😮😮😮😮😮😮😮😮😮😮😮😮😮", "name": "😦"},
    {"photo": "🛬🛬🛬🛬🛫🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬🛬", "name": "🛫"},
    {"photo": "🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂🙂😶🙂🙂", "name": "😶"},
    {"photo": "🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙉🙊🙉🙉", "name": "🙊"},
    {"photo": "🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇸🇩🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸🇵🇸", "name": "🇸🇩"},
    {"photo": "🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇹🇩🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪🇧🇪", "name": "🇹🇩"},
    {"photo": "🎥🎥🎥🎥🎥🎥🎥🎥🎥📹🎥🎥🎥🎥🎥🎥🎥🎥🎥🎥🎥🎥", "name": "📹"},
    {"photo": "🖊🖊🖊🖊🖊🖋🖊🖊🖊🖊🖊🖊🖊🖊🖊🖊🖊🖊", "name": "🖋"},
    {"photo": "🛌🛌🛌🛏🛌🛌🛌🛌🛌🛌🛌🛌🛌🛌🛌🛌", "name": "🛌"},
    {"photo": "🔒🔒🔒🔒🔒🔒🔒🔓🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒", "name": "🔓"},
    {"photo": "👨‍💻👨‍💻👨‍💻👨‍💻🧑‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻👨‍💻", "name": "👨‍💻"},
    {"photo": "📑📑📑📑📑📑📑📑📑📑📑📑📑📑📑📑📑📄📑📑📑📑📑📑📑📑", "name": "📄"},
    {"photo": "🦻🦻🦻🦻🦻🦻👂🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻🦻", "name": "👂"},
    {"photo": "⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈⛈🌨⛈⛈⛈⛈", "name": "🌨"},
    {"photo": "😚😚😚😚😚☺️😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚", "name": "☺️"},
    {"photo": "🦏🦏🦏🦏🦏🦏🦏🦏🦏🐘🦏🦏🦏🦏🦏🦏🦏🦏🦏🦏", "name": "🐘"},
    {"photo": "💿💿💿💿💿💿💿💿📀💿💿💿💿💿💿💿", "name": "📀"},
    {"photo": "😐😐😐😐😐😐😑😐😐😐😐😐😐😐😐😐😐😐😐😐😐", "name": "😑"},
    {"photo": "❤️❤️❤️❤️❤️❤️❤️❤️❤️♥️❤️❤️❤️❤️❤️❤️", "name": "♥️"},
    {"photo": "🩶🩶🩶🩶🩶🩶🩶🩶🤍🩶🩶🩶🩶🩶🩶🩶🩶", "name": "🤍"},
    {"photo": "🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♀🏋‍♂🏋‍♂🏋‍♂🏋‍♂🏋‍♂", "name": "🏋‍♀"},
    {"photo": "🇪🇬🇪🇬🇪🇬🇪🇬🇾🇪🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬🇪🇬", "name": "🇾🇪"},
    {"photo": "📸📸📸📸📸📸📸📷📸📸📸📸📸📸📸📸📸📸📸📸📸📸📸📸", "name": "📷"},
    {"photo": "📲📲📲📲📲📲📲📲📲📲📲📲📲📲📲📲📱📲📲📲📲📲📲📲📲📲", "name": "📱"},
    {"photo": "🔆🔆🔆🔆🔆🔅🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆", "name": "🔅"},
    {"photo": "🏬🏬🏬🏬🏬🏬🏬🏬🏢🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬🏬", "name": "🏢"},
    {"photo": "🥋🥋🥋🥋🥋🥋🥋🥼🥋🥋🥋🥋🥋🥋🥋🥋🥋🥋🥋", "name": "🥼"},
    {"photo": "🦌🦌🦌🦌🦌🦌🦌🐂🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌🦌", "name": "🐂"},
    {"photo": "😧😧😧😧😧😧😧😧😧😧😯😧😧😧😧😧😧😧😧😧😧😧", "name": "😯"},
    {"photo": "🍽🍽🍽🍽??🍽🍽🍽🍽🍴🍽🍽🍽🍽🍽🍽🍽🍽🍽🍽", "name": "🍴"},
    {"photo": "📆📆📆📆📆📅📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆📆", "name": "📅"},
    {"photo": "🍀🍀🍀🍀🍀🍀🍀🍀☘🍀🍀🍀🍀🍀🍀🍀", "name": "☘"},
    {"photo": "🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚄🚅🚄🚄🚄🚄🚄🚄🚄", "name": "🚅"},
    {"photo": "👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👨‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨", "name": "👨‍❤️‍👨"},
    {"photo": "🌍🌍🌍🌍🌍🌏🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍", "name": "🌏"},
    {"photo": "🤹‍♀🤹‍♀🤹‍♀🤹🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀🤹‍♀", "name": "🤹"},
    {"photo": "🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔈🔉🔈🔈🔈🔈🔈", "name": "🔉"},
    {"photo": "⛰⛰⛰⛰⛰⛰🏔⛰⛰⛰⛰⛰⛰⛰⛰⛰", "name": "🏔"},
    {"photo": "😸😸😸😺😸😸😸😸😸😸😸😸😸😸😸😸😸", "name": "😺"},
    {"photo": "👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯🚶‍♀👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯👩‍🦯", "name": "🚶‍♀"},
    {"photo": "❓❓❓❓❔❓❓❓❓❓❓❓❓❓❓❓❓", "name": "❔"},
    {"photo": "🔕🔕🔕🔕🔕🔕🔕🔕🔕🔔🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕🔕", "name": "🔔"},
    {"photo": "🖐🖐🖐🖖🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐🖐", "name": "🖖"},
    {"photo": "☃️☃️☃️☃️☃️☃️☃️⛄️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️☃️", "name": "⛄️"},
    {"photo": "😌😌😌😌😌😌😌😌😌😌☺️😌😌😌😌😌", "name": "☺️"},
    {"photo": "👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍??👨‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨👩‍❤️‍👨", "name": "👨‍❤️‍👨"},
    {"photo": "🧥🧥🧥🧥🧥🧥🧥🧥🧥🧥🧥🥼🧥🧥🧥🧥🧥🧥🧥🧥", "name": "🥼"},
    {"photo": "⏯⏯⏯⏯⏯⏸⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯⏯", "name": "⏸"},
    {"photo": "😚😚😚😚😚☺️😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚😚", "name": "☺️"},
    {"photo": "🔨🔨🔨🔨⛏🔨🔨🔨🔨🔨🔨🔨🔨🔨🔨🔨🔨", "name": "⛏"},
    {"photo": "📂📂📂📂📂📂📁📂📂📂📂📂📂📂📂📂", "name": "📁"},
    {"photo": "🦀🦀🦀🦀🦀🦀🦀🦞🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀🦀", "name": "🦞"},
    {"photo": "👿👿👿👿👿😈👿👿👿👿👿👿👿👿👿👿👿👿👿👿👿", "name": "😈"},
    {"photo": "🔳🔳🔳🔳🔳🔳🔳🔳🔳◼️🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳", "name": "◼️"},
    {"photo": "🐼🐼🐼🐼🐼🐼🐼🐻‍❄️🐼🐼🐼🐼🐼🐼🐼🐼🐼🐼", "name": "🐻‍❄️"},
    {"photo": "🔎🔎🔎🔎🔎🔎🔎🔎🔎🔍🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎🔎", "name": "🔍"},
    {"photo": "🤼‍♂🤼🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂🤼‍♂", "name": "🤼"},
    {"photo": "👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀🧑‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀👩‍🚀", "name": "🧑‍🚀"}
]

@app.on_message(filters.command(["مختلف", "اختلاف","الاختلاف","المختلف 🧠"], ""), group=6565065)
async def moktlf(client, message):
    actor = random.choice(qustions)
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    cear2[user_id] = actor['name']
    uss2[user_id] = user_id
    await message.reply_text(actor['photo'])

@app.on_message(filters.text, group=5012465)
async def alatlaf(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in uss2:
        correct_actor = cear2.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text(f"**◍ الإجابة صحيحة ✅\n◍ الأن معك {points[user_id]} نقاط 🔹\n√**")
            points[user_id]= points.get(user_id, 0) + 1
            del cear2[user_id]
            del uss2[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"◍ عذرا عزيزي اجابتك خطا ❌\n◍ الاجابة الصحيحة هي [{correct_actor}] ✅\n√")
                del cear2[user_id]
                del uss2[user_id]

uses1 = {}        
caear1 = {}        

questions = [
    {"photo": "ما هو عدد الكواكب في النظام الشمسي؟", "name": "8"},
    {"photo": "ما هو لون الشمس؟", "name": "أبيض"},
    {"photo": "اسمه من خمسة حروف اذا حذفت اوله بقا ثمان؟", "name": "عثمان"},
    {"photo": "ما الشئ الذي يمتلك أسنان ولا يمكنه العض؟", "name": "المشط"},
    {"photo": "شيء يتجمد إذا تم تسخينه؟", "name": "البيض"},
    {"photo": "يحملك إلى اي مكان اذا حذفت اوله اصبح عظيم الشأن واذا حذفت اخره اصبح غالي الأثمان واذا عكسته تقشعر منه الأبدان؟", "name": "درب"},
    {"photo": "نوع من أنواع الحيوانات يقوم بحك أذنه من خلال أنفه فما هو؟", "name": "الفيل"},
    {"photo": "من هو خال ابن عمتك؟", "name": "ابوك"},
    {"photo": "ما هو الشي الذي يعتبر غير نظيف اذا ابيض لونه؟", "name": "اللسان"},
    {"photo": "ماهو الشيء الذي تراه ولا يراك؟", "name": "الظل"},
    {"photo": "يطير مثل الطيور ولكنه لا يغادر مكانه؟", "name": "العلم"},
    {"photo": "ماهو الشيء الذي لايقطع إلا اذا ادخلت اصابعك في عينيه؟", "name": "المقص"},
    {"photo": "ما هو الشيء الذي يمر خلال الباب ولا يدخل؟", "name": "المفتاح"},
    {"photo": "بيت لا يوجد له أبواب ولا نوافذ فما هو؟", "name": "بيت الشعر"},
    {"photo": "ما هو الطائر الذي يستطيع تكرار كلام الإنسان بالتدريب؟", "name": "الببغاء"},
    {"photo": "اين يوجد البحر الذي بدون ماء؟", "name": "الخريطه"},
    {"photo": "لي رقبة وليس لدي رأس ولي ذراعين وليس لدي يدين ما هذا؟", "name": "القميص"},
    {"photo": "ما الشخص الي يبدو بسيط لكن يحني له الملك رأسه؟", "name": "الحلاق"},
    {"photo": "شيء اذا رايناه لا نركبه واذا ركبناه فلا نره فما هو؟", "name": "النعش"},
    {"photo": "اوله ثالث تفاحة واخر التفاح ثانيه ورابع العمر له ثالث واخر الورد باقيه؟", "name": "احمد"},
    {"photo": "من هو النبي الذي مات ولم يولد؟", "name": "ادم"},
    {"photo": "شيء من الممكن ان يكون له خيال من الامام او الخلف ومن الممكن يكون بداخله؟", "name": "الحفرة"},
    {"photo": "شيء يستطيع التحدث بكل لغات العالم؟", "name": "صدى الصوت"},
    {"photo": "لا يبتل حتى وإن دخل الماء؟", "name": "الضوء"},
    {"photo": "حيوان يمشي ويقف بالرغم من أنه ليس لديه أقدام؟", "name": "الثعبان"},
    {"photo": "نوع من انواع الطيور يتكون من حرفين واذا قلبت الكلمة صارت اسم مهنة؟", "name": "بط"},
    {"photo": "مدينة لا يطحن فيها الدقيق ولا يموت فيها الميت؟", "name": "كل المدن"},
    {"photo": "ما هو الشيء الذي يعبر البحر دون أن يتبلل غير العجل في بطن أمه؟", "name": "الطائره"},
    {"photo": "ماهو الشيء الذي يبكي اذا لففت راسه؟", "name": "الحنفيه"},
    {"photo": "انا لا املك حياة ولكنني اموت فما اكون؟", "name": "البطاريه"},
    {"photo": "ما هو الشيء الذي يطلبه الناس دائمًا وإذا جاء هربوا منه؟", "name": "المطر"},
    {"photo": "فاكهة اسمها على اسم طائر؟", "name": "الكيوي"},
    {"photo": "ما هو الجرح الذي لا ينزف دم في جسم الإنسان؟", "name": "جرح المشاعر"},
    {"photo": "يطلع من بطن امه ويحك ظهر ابوه ويموت فما هو؟", "name": "عود الكبريت"},
    {"photo": "ماهو الشيء الذي تأكل منه مع إنه لا يؤكل؟", "name": "الصحن"},
    {"photo": "ماهو الشيء الذي نرميه بعد العصر؟", "name": "البرتقال"},
    {"photo": "ما الاسم الذي إذا حذفت اوله صار اسمين؟", "name": "ياسمين"},
    {"photo": "ماهو الشيء الذي يقرصك ولا تراه؟", "name": "الجوع"},
    {"photo": "شيء موجود في الليل ثلاث مرات وفي النهار مرة واحدة؟", "name": "حرف اللام"},
    {"photo": "ما هو الطائر الذي يستطيع تكرار كلام الإنسان بالتدريب؟", "name": "حرف اللام"},
    {"photo": "كلما كان هناك المزيد قل ما تراه ما هذا؟", "name": "الضباب"},
    {"photo": "ماهو الشيء الذي يسير ولا يمتلك أقدام؟", "name": "الساعه"},
    {"photo": "يتم أخذها منك قبل أن تأخذها؟", "name": "الصوره"},
    {"photo": "ماهو الشيء الذي يوجد وسط باريس؟", "name": "حرف الراء"},
    {"photo": "هو اليف ولكن اذا صار بالأبيض والاسود صار متوحش فما يكون؟", "name": "الحمار"},
    {"photo": "شيء تسمعه ولكن لا يسمعك تراه ولكن لا يراك؟", "name": "التلفاز"},
    {"photo": "شئ قلبه ابيض ويرتدي قبعة خضراء لكن لونه اسود؟", "name": "الباذنجان"},
    {"photo": "ماهو الشيء الذي له اعين ثلاث بينما له قدم واحدة؟", "name": "اشارة المرور"},
    {"photo": "ما هو الحيوان الأبكم الذي لا يتكلم ولا نسمع له صوت؟", "name": "الزرافه"},
    {"photo": "شيء اذا لمسته يصرخ؟", "name": "الجرس"},
    {"photo": "انا املك كل المعلومات التي تعرفها وانا اصغر من قبضة يدك من اكون؟", "name": "العقل"},
    {"photo": "ما هو الشيء الذي درجة حرارته ثابته سواء وضعته في الثلاجه أو على النار؟", "name": "الفلفل"},
    {"photo": "ماهي الفاكهة الصلبة التي يوجد بداخلها حليب؟", "name": "جوز الهند"},
    {"photo": "تاجر من التجار إذا اقتلعنا عينه طار فمن هو؟", "name": "عطار"},
    {"photo": "ماهو الذي خلف الكلب اينما ذهب؟", "name": "ذيله"},
    {"photo": "بلد إسلامي اوله عبادة واخره نقود فما هو؟", "name": "الصومال"},
    {"photo": "ما هي الفاكهة التي تُجفف لتصبح زبيب؟", "name": "العنب"},
    {"photo": "شيء يغلبك دون ان يؤذيك؟", "name": "النوم"},
    {"photo": "ماهو الشيء الذي تشتريه لونه أسود ولكنك لاتستفيد منه إلا بعد أن يصبح لونه أحمر؟", "name": "الفحم"},
    {"photo": "طوله حوالي شبر ويحمل أطول من متر ماهو؟", "name": "الحذاء"},
    {"photo": "صغير الحجم لا تلقى له بال ولكن بوجهه تفتح الأبواب؟", "name": "المفتاح"},
    {"photo": "ماهما الميتتان التي يجوز اكلهما بدون اثم؟", "name": "السمك والجراد"},
    {"photo": "سيد وسيدة لديهما ست بنات وكل ابنة لها أخ واحد كم عدد أفراد العائلة؟", "name": "تسعه"},
    {"photo": "إذا كان سعيد على يمين سمير وجابر على يمين سعيد فمن يكون في الوسط؟", "name": "سعيد"},
    {"photo": "احمر وليس احمر اسود وليس اسود وابيض وليس ابيض ماهو؟", "name": "البحر"},
    {"photo": "ان ابتسمت لها ابتسمت لك ماهي؟", "name": "المراه"},
    {"photo": "ما هو أهون موجود و أعز مفقود؟", "name": "الماء"},
    {"photo": "الشيء الذي إذا ذبح بكى عليه الجميع؟", "name": "البصل"},
    {"photo": "من هو الشخص الذي يمشي على الأرض ولكنه يطول النجوم أيضًا؟", "name": "الظابط"},
    {"photo": "إنسان وزوجته لا هو من بني آدم ولا هي من بنات حواء من هما؟", "name": "ادم وحواء"},
    {"photo": "ما هو الشيء الذي يحمل طعامه فوق رأسه فإذا مشى أكل منه وإذا سكن غطى رأسه ونام؟", "name": "قلم الحبر"},
    {"photo": "ما هو الشيء الذي يحيا في أول الشهر ويموت في آخر الشهر؟", "name": "القمر"},
    {"photo": "ما الذي يمكنه أن يملأ الغرفة دون أن يشغل حيزا؟", "name": "النور"},
    {"photo": "طائر إذا قمت بقلب حروف اسمه رأيت عجب؟", "name": "بجع"},
    {"photo": "ينام بالحذاء ولا يخلعه؟", "name": "الحصان"},
    {"photo": "ما هي الكلمة الوحيدة التي تلفظ غلط دائمًا؟", "name": "غلط"},
    {"photo": "لا يبتل حتى وإن دخل الماء؟", "name": "الضوء"},
    {"photo": "اسم حيوان اذا قمت بتغيير اول حرف منه اصبح اهم عضو في جسم الإنسان؟", "name": "قلب"},
    {"photo": "ماهو الشئ الموجود في كل شيء؟", "name": "الاسم"},
    {"photo": "امرأة عقيم هل تنجب ابنتها أطفال؟", "name": "العقيم لا تلد"},
    {"photo": "ما هو الشئ الذي يمكن كسره دون ان نلمسه؟", "name": "الوعد"},
    {"photo": "قلعة خضراء وأرضها حمراء وسكانها لونهم أسود فما هي؟", "name": "البطيخه"},
    {"photo": "ماهو الذي خلف الكلب اينما ذهب؟", "name": "ذيله"},
    {"photo": "ماهي الدولة التي حارب اهلها الذباب والعصافير لخطورتها؟", "name": "الصين"},
    {"photo": "ما هي اسم الفاكهة التي سُميت بإحدى سور القرآن الكريم باسمها؟", "name": "التين"},
    {"photo": "شيء كلما كان موجود كلما قل ماتراه؟", "name": "الظلام"},
    {"photo": "عقرب لا يلدغ ولا يسبب الذعر لأي أحد حتى الأطفال؟", "name": "عقرب الساعه"},
    {"photo": "فاكهة بها حبات اللؤلؤ؟", "name": "الرمان"},
    {"photo": "شيء موجود في الدقيقة مرتين ولا يوجد في الساعة؟", "name": "حرف القاف"},
    {"photo": "مدينة سعودية اسمها على اسم نبات فما هي؟", "name": "عرعر"},
    {"photo": "ماهو الشيء الذي كلما عرضته للشمس ازداد بللا؟", "name": "الثلج"},
    {"photo": "ما هو الشيء الذى كلما خطا خطوه فقد شيئًا من ذيله؟", "name": "ابره الخياطه"},
    {"photo": "ماهو الشيء الذي يتحرك بدون أرجل ويبكي بدون عيون؟", "name": "السحاب"},
    {"photo": "ما هو الشيء الذي بإمكانك تحقيقه دون بذل عناء؟", "name": "الفشل"},
    {"photo": "شيء اذا اطعمناه لا يشبع واذا سقيناه يموت؟", "name": "النار"},
    {"photo": "شيء ليس له بداية ولا نهاية ما هو هذا الشيء؟", "name": "الدائره"},
    {"photo": "طائر يلد ولايبيض فما هو؟", "name": "الخفاش"},
    {"photo": "شيء في السماء وليس في الماء فما هو؟", "name": "حرف السين"},
    {"photo": "شيء تملكه انت ولكن يستخدمه الآخرون اكثر منك؟", "name": "الاسم"},
    {"photo": "جزء من الجنة يعيش معنا في الأرض ما هو؟", "name": "الحجر الاسود"},
    {"photo": "يمتلك بحيرات بلا ماء وأراضي بلا زرع وجبال بلا أحجار؟", "name": "الخريطه"},
    {"photo": "اي كلمة تصبح اقصر اذا اضفت لها حرف؟", "name": "قصر"},
    {"photo": "ما هي درجة القرابة طفل من والده الحقيقي لكن هذا الطفل ليس ابنه؟", "name": "ابنته"},
    {"photo": "ماهو الشجر الذي يسميه الناس قاتل ابيه؟", "name": "الموز"},
    {"photo": "شيء يمكن قياسه لكن لايمكن رؤيته؟", "name": "الوقت"},
    {"photo": "ماهو الشيء الذي ينام ولا يقوم؟", "name": "الرماد"},
    {"photo": "شيء يمشي أمامك ولا تستطيع رؤيته؟", "name": "المستقبل"},
    {"photo": "شهر هجري اذا حذفت وسطه يتحول الي فاكهة؟", "name": "رمضان"}, 
    {"photo": "هو شيء يكون لونه أخضر في الأرض وأسود في الأسواق وأحمر في الأكواب، فما هو؟", "name": "الشاي"},
    {"photo": "يمكنه رفع الأثقال، لكنه لا يستطيع أن يمسك مسمار", "name": "البحر"},
    {"photo": "يقول الحقيقة ويكذب عندما يكون جائعا", "name": "الساعه"} 
]

@app.on_message(filters.command(["لغز", "فزوره","فزورة 🎭"], ""), group=6456565)
async def fazoraa(client, message):
    actor = random.choice(questions)
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    caear1[user_id] = actor['name']
    uses1[user_id] = user_id
    await message.reply_text(actor['photo'])

@app.on_message(filters.text, group=5013245)
async def logzee(client, message):
    bot_username = client.me.username
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in uses1:
        correct_actor = caear1.get(user_id)
        if correct_actor and message.text.lower() == correct_actor.lower():
            await message.reply_text(f"**◍ الإجابة صحيحة ✅\n◍ الأن معك {points[user_id]} نقاط 🔹\n√**")
            points[user_id]= points.get(user_id, 0) + 1
            del caear1[user_id]
            del uses1[user_id]
        else:
            if correct_actor:
                await message.reply_text(f"◍ عذرا عزيزي اجابتك خطا ❌\n◍ الاجابة الصحيحة هي [{correct_actor}] ✅\n√")
                del caear1[user_id]
                del uses1[user_id]
            
@app.on_message(filters.command("نقاطي", ""), group=908070)
async def check_points(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in points:
        point = points.get(user_id)
        await message.reply_text(f"لديك {point} نقطة.")
    else:
        await message.reply_text("معكش نقاط اصلا")

@app.on_message(filters.command("توب النقاط", ""), group=918171)
async def top_points(client, message):
    user_id = message.from_user.id if message.from_user else "None"	
    sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)   
    k = 0
    text = "اكثر الاشخاص الي معاها نقاط:\n\n"    
    for user_id, point in sorted_points:
        user = await client.get_users(user_id)
        k += 1
        text += f"{k}: {user.mention} : {point}\n"
        if k >= 5:
            break
    await message.reply_text(text)

iddof = []
@app.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "")& filters.group,group=12147770)
async def iddlock(client: Client, message):
    get = await client.get_chat_member(message.chat.id, message.from_user.id)  
    if message.text.lower() in ["تعطيل الايدي", "قفل الايدي"]:
        if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            if message.chat.id in iddof:
                return await message.reply_text("**♪ الامر معطل من قبل  💎 .**")
            iddof.append(message.chat.id)
            return await message.reply_text("**♪ تم تعطيل الايدي بنجاح  💎 .**")
        else:
            return await message.reply_text("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "")& filters.group,group=125448)
async def iddopen(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if message.text.lower() in ["تفعيل الايدي", "فتح الايدي"]:
        if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            if not message.chat.id in iddof:
                return await message.reply_text("**♪ الايدي مفعل من قبل  💎 .**")
            iddof.remove(message.chat.id)
            return await message.reply_text("**♪ تم تفعيل الايدي بنجاح  💎 .**")
        else:
            return await message.reply_text("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")
   
iddphotoof = []
@app.on_message(filters.command(["تفعيل الايدي بالصوره"], "")& filters.group,group=1214723)
async def iddlck(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)  
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddphotoof:
        return await message.reply_text("**♪ الامر مفعيل من قبل  💎 .**")
      iddphotoof.append(message.chat.id)
      return await message.reply_text("**♪ تم تفعيل الايدي بالصوره بنجاح  💎 .**")
   else:
      return await message.reply_text("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")

@app.on_message(filters.command(["تعطيل الايدي بالصوره"], "")& filters.group,group=1288448)
async def idopen(client: Client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in iddphotoof:
        return await message.reply_text("**♪ الايدي بالصوره معطل من قبل  💎 .**")
      iddphotoof.remove(message.chat.id)
      return await message.reply_text("**♪ تم تعطيل الايدي بالصوره بنجاح  💎 .**")
   else:
      return await message.reply_text("**♪ عذرا عزيزي هذا الامر للادمن الجروب فقط  💎 .**")

DATA_FILE = "likes.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if "groups" not in data:
                data["groups"] = {}
            return data
    return {"groups": {}}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


data = load_data()

@app.on_message(filters.command(["ايدي", "أ", "ا"], "") & filters.group, group=54788)
async def muid(client: Client, message: Message):
    user = message.from_user
    user_id = str(user.id)
    group_id = str(message.chat.id)
    if message.chat.id in iddof:
        return await message.reply_text("**🎵 تم تعطيل أمر الايدي من قبل المشرفين 💎.**")
    rank = "عضو عادي 👤"
    if user_id == "7028046857":
        rank = "المبرمج محمد صالح شخصياً 🥷✨"
    elif user.username in source_devv:
        rank = "صاحب السورس شخصياً 👑🔥"
    elif user_id == str(OWNER_ID):
        rank = "مطور البوت الرئيسي 💻🌟"
    else:
        member = await client.get_chat_member(group_id, int(user_id))
        if member.status == ChatMemberStatus.OWNER:
            rank = "مالك المجموعة 👑"
        elif is_group_creator(group_id, user_id):
            rank = "منشئ للبوت في هذه المجموعة 🛡️"
        elif is_group_admin(group_id, user_id):
            rank = "أدمن للبوت في هذه المجموعة 🔥"
        elif member.status == ChatMemberStatus.ADMINISTRATOR:
            rank = "مشرف عام 🛡️"
    
    profile = await client.get_chat(user.id)
    photo = await client.download_media(profile.photo.big_file_id) if profile.photo else None
    data = load_group_data()
    if group_id not in data["groups"]:
        data["groups"][group_id] = {"members": {}}
    if user_id not in data["groups"][group_id]["members"]:
        data["groups"][group_id]["members"][user_id] = {"messages_count": 0}
        save_data(data)

    member_data = data["groups"][group_id]["members"][user_id]
    total = member_data["messages_count"]
     
    if user_id not in data:
        data[user_id] = {"count": 0, "likers": []}
        save_data(data)

    caption = (
        f"**│⎋ الاسم:** {user.first_name}\n"
        f"**│⎋ المعرف:** `{user.id}`\n"
        f"**│⎋ رتبتك:** {rank}\n" 
        f"**│⎋ اليوزر:** [@{user.username}]\n"
        f"**│⎋ عدد رسايلك:** {total}\n"
        f"**│⎋ البايو:** {profile.bio or '—'}"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"ʟɪᴋᴇ ❤️ ⤏ {data[user_id]['count']}", callback_data=f"heart_{user_id}"),
         InlineKeyboardButton("ʟɪᴋᴇʀѕ ⤏👤", callback_data=f"show_{user_id}")]
    ])

    if photo and message.chat.id in iddphotoof:
        msg = await message.reply_photo(photo=photo, caption=caption, reply_markup=keyboard)
    else:
        msg = await message.reply_text(caption, reply_markup=keyboard)


@app.on_callback_query(filters.regex("heart_"))
async def heart_callback(client: Client, query: CallbackQuery):
    target_id = query.data.split("_")[1]
    user_id = str(query.from_user.id)
    group_id = str(query.message.chat.id)
    if group_id not in data["groups"]:
        data["groups"][group_id] = {"members": {}}
    if target_id not in data["groups"][group_id]["members"]:
        return

    member_data = data["groups"][group_id]["members"][target_id]
    liker = f"{query.from_user.first_name}"

    if target_id not in data:
        data[target_id] = {"count": 0, "likers": []}

    if liker in data[target_id]["likers"]:
        data[target_id]["likers"].remove(liker)
        data[target_id]["count"] -= 1
    else:
        data[target_id]["likers"].append(liker)
        data[target_id]["count"] += 1

    save_data(data)

    rank = "عضو عادي 👤"  
    if target_id == "7028046857":
        rank = "المبرمج محمد صالح شخصياً 🥷✨"
    elif target_id == str(OWNER_ID):
        rank = "مطور البوت الرئيسي 💻🌟"
    else:
        member = await client.get_chat_member(group_id, int(target_id))
        if member.status == ChatMemberStatus.OWNER:
            rank = "مالك المجموعة 👑"
        elif is_group_creator(group_id, target_id):
            rank = "منشئ للبوت في هذه المجموعة 🛡️"
        elif is_group_admin(group_id, target_id):
            rank = "أدمن للبوت في هذه المجموعة 🔥"
        elif member.status == ChatMemberStatus.ADMINISTRATOR:
            rank = "مشرف عام 🛡️"
    
    user = await client.get_chat(int(target_id))
    caption = (
        f"**│⎋ الاسم:** {user.first_name}\n"
        f"**│⎋ المعرف:** `{user.id}`\n"
        f"**│⎋ رتبتك:** {rank}\n" 
        f"**│⎋ اليوزر:** [@{user.username}]\n"
        f"**│⎋ عدد رسايلك:** {member_data['messages_count']}\n"
        f"**│⎋ البايو:** {user.bio or '—'}"
    )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(f"ʟɪᴋᴇ ❤️ ⤏ {data[target_id]['count']}", callback_data=f"heart_{target_id}"),
         InlineKeyboardButton("ʟɪᴋᴇʀѕ ⤏👤", callback_data=f"show_{target_id}")]
    ])

    try:
        await query.edit_message_caption(caption=caption, reply_markup=keyboard)
    except Exception as e:
        print(f"Error while editing message caption: {e}")

@app.on_callback_query(filters.regex("show_"))
async def show_likers(client: Client, query: CallbackQuery):
    target_id = query.data.split("_")[1]
    if str(query.from_user.id) != target_id:
        return await query.answer("❌ هذا الزر خاص بصاحب الرسالة فقط!", show_alert=True)

    likers = data.get(target_id, {}).get("likers", [])
    if not likers:
        return await query.answer("لا يوجد معجبين حتى الآن 💔", show_alert=True)

    names = "\n".join([l.split("@")[-1] for l in likers])
    await query.answer(f"👤 معجبينك:\n{names}", show_alert=True)


@app.on_message(filters.command(["قلوبي", "لايكاتي", "المعجبين"], "") & filters.group, group=547878)
async def heart_count(client: Client, message: Message):
    user = message.from_user
    user_id = str(user.id)
    group_id = str(message.chat.id)
    data = load_data()
    caption = (
        f"**│⎋ الاسم:** {user.first_name}\n"
        f"**│⎋ المعرف:** `{user.id}`\n"
        f"**│⎋ عدد القلوب:** {data[user_id]['count']} ❤️\n"
    )
    await message.reply_text(caption)


@app.on_message(filters.command(["اضف قلوب"], "") & filters.group, group=5481288)
async def add_hearts(client: Client, message: Message):
    user = message.from_user
    user_id = str(user.id)
    group_id = str(message.chat.id)
    if message.from_user.id not in [OWNER_ID, zombie_id, sourse_dev]:
        return
    ask_user = await client.ask(message.chat.id, "من فضلك، أرسل يوزر الشخص الذي تريد زيادة القلوب له (بدون @):", filters=filters.user(message.from_user.id))
    target_username = ask_user.text.strip()

    try:
        target_user = await client.get_users(target_username)
    except Exception as e:
        await ask_user.reply(f"❌ لم أتمكن من العثور على هذا اليوزر. الخطأ: {e}")
        return

    if not target_user:
        await ask_user.reply("❌ لم أتمكن من العثور على هذا اليوزر.")
        return
    ask_heart_count = await client.ask(message.chat.id, "من فضلك، أرسل عدد القلوب الذي تريد إضافته:", filters=filters.user(message.from_user.id))
    try:
        heart_count = int(ask_heart_count.text)
        if heart_count <= 0:
            await ask_heart_count.reply("❌ العدد يجب أن يكون أكبر من 0!")
            return

        target_user_id = str(target_user.id)
        data[target_user_id]["count"] += heart_count
        save_data(data)
        caption = f"**│⎋ الاسم:** {target_user.first_name}\n**│⎋ المعرف:** `{target_user.id}`\n**│⎋ تم إضافة {heart_count} قلب**"
        await ask_heart_count.reply(caption)
    except ValueError:
        await ask_heart_count.reply("❌ يرجى إدخال عدد صحيح للقلب.")

#...................................................................................................................
#...................................................................................................................
#...................................................................................................................


@app.on_message(filters.command(["زخرفه"], ""), group=7538989787)
async def zahrafa(c: Client, m: Message):
    ask = await app.ask(m.chat.id, "ارسل الاسم المراد زخرفته", filters=filters.user(m.from_user.id), timeout=300)
    text = ask.text
    if len(text) > 100:
        await m.reply_text("◍ لا يمكنك تشكيل أكثر من 100 حرفاً، يرجى المحاولة مرة أخرى!\n√")
        return
    
    else:
        if re.match("\n", str(text)):
            await m.reply_text("◍ لا يمكن زخرفه نص يحتوي على اكثر من سطر\n√")
            return
    EmojeS = [
        ' 𓁻 ',
        ' 𓏴  ',
        ' 𓏶 ',
        ' 𓏡 ',
        ' 𓏢 ',
        ' 𓏣 ',
        ' ☽ ',
        ' 𖠱 ',
        '☂ ',
        ' ◑ ',
        ' ꧁ ',
        ' ◌ ',
        ' ★ ',
        ' ℡ ',
        ' § ',
        ' ☆ '
    ]
    Emoje = [
        ' ♕ ',
        ' 𖤍 ',
        ' 𖤓 ',
        ' ✾ ',
        ' ♡ ',
        ' ꧂ ',
        ' ☫: ',
        ' ♫ ',
        ' ❈ ',
        ' ➽ ',
        ' ✺ ',
        ' ⚘ ',
        ' 𖤐 ',
        ' ❣ ',
        ' ❿ '
    ]

    zhrf = re.sub('ض', 'ضِٰـِۢ', text)
    zhrf = re.sub('ص', 'صِٰـِۢ', zhrf)
    zhrf = re.sub('ث', 'ثِٰـِۢ', zhrf)
    zhrf = re.sub('ق', 'قِٰـِۢ', zhrf)
    zhrf = re.sub('ف', 'فِٰ͒ـِۢ', zhrf)
    zhrf = re.sub('غ', 'غِٰـِۢ', zhrf)
    zhrf = re.sub('ع', 'عِٰـِۢ', zhrf)
    zhrf = re.sub('خ', 'خِٰ̐ـِۢ', zhrf)
    zhrf = re.sub('ح', 'حِٰـِۢ', zhrf)
    zhrf = re.sub('ج', 'جِٰـِۢ', zhrf)
    zhrf = re.sub('ش', 'شِٰـِۢ', zhrf)
    zhrf = re.sub('س', 'سِٰـِۢ', zhrf)
    zhrf = re.sub('ي', 'يِٰـِۢ', zhrf)
    zhrf = re.sub('ب', 'بِٰـِۢ', zhrf)
    zhrf = re.sub('ل', 'لِٰـِۢ', zhrf)
    zhrf = re.sub('ا', 'آ', zhrf)
    zhrf = re.sub('ت', 'تِٰـِۢ', zhrf)
    zhrf = re.sub('ن', 'نِٰـِۢ', zhrf)
    zhrf = re.sub('م', 'مِٰـِۢ', zhrf)
    zhrf = re.sub('ك', 'ڪِٰـِۢ', zhrf)
    zhrf = re.sub('ط', 'طِٰـِۢ', zhrf)
    zhrf = re.sub('ظ', 'ظِٰـِۢ', zhrf)
    zhrf = re.sub('ء', 'ء', zhrf)
    zhrf = re.sub('ؤ', 'ؤ', zhrf)
    zhrf = re.sub('ر', 'ر', zhrf)
    zhrf = re.sub('ى', 'ى', zhrf)
    zhrf = re.sub('ز', 'ز', zhrf)
    zhrf = re.sub('و', 'ﯛ̲୭', zhrf)
    zhrf = re.sub('ه', 'ۿۿہ', zhrf)
    zhrf = re.sub('a', '𝗮', zhrf)
    zhrf = re.sub('A', '𝗔', zhrf)
    zhrf = re.sub("b", "𝗯", zhrf)
    zhrf = re.sub("B", "𝗕", zhrf)
    zhrf = re.sub("c", "𝗰", zhrf)
    zhrf = re.sub("C", "𝗖", zhrf)
    zhrf = re.sub("d", "𝗱", zhrf)
    zhrf = re.sub("D", "𝗗", zhrf)
    zhrf = re.sub("e", "𝗲", zhrf)
    zhrf = re.sub("E", "𝗘", zhrf)
    zhrf = re.sub("f", "𝗳", zhrf)
    zhrf = re.sub("F", "𝗙", zhrf)
    zhrf = re.sub("g", "𝗴", zhrf)
    zhrf = re.sub("G", "𝗚", zhrf)
    zhrf = re.sub("h", "𝗵", zhrf)
    zhrf = re.sub("H", "𝗛", zhrf)
    zhrf = re.sub("i", "𝗹", zhrf)
    zhrf = re.sub("I", "𝗜", zhrf)
    zhrf = re.sub("j", "𝗝", zhrf)
    zhrf = re.sub("J", "𝗝", zhrf)
    zhrf = re.sub("k", "𝗸", zhrf)
    zhrf = re.sub("K", "𝗞", zhrf)
    zhrf = re.sub("l", "𝗹", zhrf)
    zhrf = re.sub("L", "𝗟", zhrf)
    zhrf = re.sub("m", "𝗺", zhrf)
    zhrf = re.sub("M", "𝗠", zhrf)
    zhrf = re.sub("n", "𝗻", zhrf)
    zhrf = re.sub("N", "𝗡", zhrf)
    zhrf = re.sub("o", "𝗼", zhrf)
    zhrf = re.sub("O", "𝗢", zhrf)
    zhrf = re.sub("p", "𝗽", zhrf)
    zhrf = re.sub("P", "𝗣", zhrf)
    zhrf = re.sub("q", "𝗾", zhrf)
    zhrf = re.sub("Q", "𝗤", zhrf)
    zhrf = re.sub("r", "𝗿", zhrf)
    zhrf = re.sub("R", "𝗥", zhrf)
    zhrf = re.sub("s", "𝘀", zhrf)
    zhrf = re.sub("S", "𝗦", zhrf)
    zhrf = re.sub("t", "𝘁", zhrf)
    zhrf = re.sub("T", "𝗧", zhrf)
    zhrf = re.sub("u", "𝘂", zhrf)
    zhrf = re.sub("U", "𝗨", zhrf)
    zhrf = re.sub("v", "𝘃", zhrf)
    zhrf = re.sub("V", "𝗩", zhrf)
    zhrf = re.sub("w", "𝘄", zhrf)
    zhrf = re.sub("W", "𝗪", zhrf)
    zhrf = re.sub("x", "𝘅", zhrf)
    zhrf = re.sub("X", "𝗫", zhrf)
    zhrf = re.sub("y", "𝘆", zhrf)
    zhrf = re.sub("Y", "𝗬", zhrf)
    zhrf = re.sub("z", "𝘇", zhrf)
    zhrf = re.sub("Z", "𝗭", zhrf)

    zhrf2 = re.sub('ض', 'ضَٰـُـٰٓ', text)
    zhrf2 = re.sub('ص', 'صَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ث', 'ثَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ق', 'قَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ف', 'فَٰ͒ـُـٰٓ', zhrf2)
    zhrf2 = re.sub('غ', 'غَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ع', 'عَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('خ', 'خَٰ̐ـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ح', 'حَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ج', 'جَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ش', 'شَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('س', 'سَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ي', 'يَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ب', 'بَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ل', 'لَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ا', 'آ', zhrf2)
    zhrf2 = re.sub('ت', 'تَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ن', 'نَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('م', 'مَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ك', 'ڪَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ط', 'طَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ظ', 'ظَٰـُـٰٓ', zhrf2)
    zhrf2 = re.sub('ء', 'ء', zhrf2)
    zhrf2 = re.sub('ؤ', 'ؤ', zhrf2)
    zhrf2 = re.sub('ر', 'ر', zhrf2)
    zhrf2 = re.sub('ى', 'ى', zhrf2)
    zhrf2 = re.sub('ز', 'ز', zhrf2)
    zhrf2 = re.sub('و', 'ﯛ̲୭', zhrf2)
    zhrf2 = re.sub("ه", "ۿۿہ", zhrf2)
    zhrf2 = re.sub('a', "𝖆", zhrf2)
    zhrf2 = re.sub('A', "𝖆", zhrf2)
    zhrf2 = re.sub("b", "𝖇", zhrf2)
    zhrf2 = re.sub("B", "𝖇", zhrf2)
    zhrf2 = re.sub("c", "𝖈", zhrf2)
    zhrf2 = re.sub("C", "𝖈", zhrf2)
    zhrf2 = re.sub("d", "𝖉", zhrf2)
    zhrf2 = re.sub("D", "𝖉", zhrf2)
    zhrf2 = re.sub("e", "𝖊", zhrf2)
    zhrf2 = re.sub("E", "𝖊", zhrf2)
    zhrf2 = re.sub("f", "𝖋", zhrf2)
    zhrf2 = re.sub("F", "𝖋", zhrf2)
    zhrf2 = re.sub("g", "𝖌", zhrf2)
    zhrf2 = re.sub("G", "𝖌", zhrf2)
    zhrf2 = re.sub("h", "𝖍", zhrf2)
    zhrf2 = re.sub("H", "𝖍", zhrf2)
    zhrf2 = re.sub("i", "𝖎", zhrf2)
    zhrf2 = re.sub("I", "𝖎", zhrf2)
    zhrf2 = re.sub("j", "𝖏", zhrf2)
    zhrf2 = re.sub("J", "𝖏", zhrf2)
    zhrf2 = re.sub("k", "𝖐", zhrf2)
    zhrf2 = re.sub("K", "𝖐", zhrf2)
    zhrf2 = re.sub("l", "𝖑", zhrf2)
    zhrf2 = re.sub("L", "𝖑", zhrf2)
    zhrf2 = re.sub("m", "𝖒", zhrf2)
    zhrf2 = re.sub("M", "𝖒", zhrf2)
    zhrf2 = re.sub("n", "𝖓", zhrf2)
    zhrf2 = re.sub("N", "𝖓", zhrf2)
    zhrf2 = re.sub("o", "𝖔", zhrf2)
    zhrf2 = re.sub("O", "𝖔", zhrf2)
    zhrf2 = re.sub("p", "𝖕", zhrf2)
    zhrf2 = re.sub("P", "𝖕", zhrf2)
    zhrf2 = re.sub("q", "𝖖", zhrf2)
    zhrf2 = re.sub("Q", "𝖖", zhrf2)
    zhrf2 = re.sub("r", "𝖗", zhrf2)
    zhrf2 = re.sub("R", "𝖗", zhrf2)
    zhrf2 = re.sub("s", "𝖘", zhrf2)
    zhrf2 = re.sub("S", "𝖘", zhrf2)
    zhrf2 = re.sub("t", "𝖙", zhrf2)
    zhrf2 = re.sub("T", "𝖙", zhrf2)
    zhrf2 = re.sub("u", "𝖚", zhrf2)
    zhrf2 = re.sub("U", "𝖚", zhrf2)
    zhrf2 = re.sub("v", "𝖛", zhrf2)
    zhrf2 = re.sub("V", "𝖛", zhrf2)
    zhrf2 = re.sub("w", "𝖜", zhrf2)
    zhrf2 = re.sub("W", "𝖜", zhrf2)
    zhrf2 = re.sub("x", "𝖝", zhrf2)
    zhrf2 = re.sub("X", "𝖝", zhrf2)
    zhrf2 = re.sub("y", "𝖞", zhrf2)
    zhrf2 = re.sub("Y", "𝖞", zhrf2)
    zhrf2 = re.sub("z", "𝖟", zhrf2)
    zhrf2 = re.sub("Z", "𝖟", zhrf2)

    zhrf3 = re.sub('ض', 'ض', text)
    zhrf3 = re.sub('ص', 'ص', zhrf3)
    zhrf3 = re.sub('ث', 'ثہ', zhrf3)
    zhrf3 = re.sub('ق', 'ق', zhrf3)
    zhrf3 = re.sub('ف', 'فُہ', zhrf3)
    zhrf3 = re.sub('غ', 'غہ', zhrf3)
    zhrf3 = re.sub('ع', 'عہ', zhrf3)
    zhrf3 = re.sub('ه', 'هٰہٰٖ', zhrf3)
    zhrf3 = re.sub('خ', 'خہ', zhrf3)
    zhrf3 = re.sub('ح', 'حہ', zhrf3)
    zhrf3 = re.sub('ج', 'جہ', zhrf3)
    zhrf3 = re.sub('د', 'د', zhrf3)
    zhrf3 = re.sub('ذ', 'ذ', zhrf3)
    zhrf3 = re.sub('ش', 'شہ', zhrf3)
    zhrf3 = re.sub('س', 'سہ', zhrf3)
    zhrf3 = re.sub('ي', 'يہ', zhrf3)
    zhrf3 = re.sub('ب', 'بّ', zhrf3)
    zhrf3 = re.sub('ل', 'لہ', zhrf3)
    zhrf3 = re.sub('ا', 'ا', zhrf3)
    zhrf3 = re.sub('ت', 'تہ', zhrf3)
    zhrf3 = re.sub('ن', 'نٰہٰٖ', zhrf3)
    zhrf3 = re.sub('م', 'مٰہٰٖ', zhrf3)
    zhrf3 = re.sub('ك', 'كُہ', zhrf3)
    zhrf3 = re.sub('ط', 'طہ', zhrf3)
    zhrf3 = re.sub('ئ', 'ئ ْٰ', zhrf3)
    zhrf3 = re.sub('ء', 'ء', zhrf3)
    zhrf3 = re.sub('ؤ', 'ؤ', zhrf3)
    zhrf3 = re.sub('ر', 'رَ', zhrf3)
    zhrf3 = re.sub('لا', 'لہا', zhrf3)
    zhrf3 = re.sub('ى', 'ىْ', zhrf3)
    zhrf3 = re.sub('ة', 'ة', zhrf3)
    zhrf3 = re.sub('و', 'و', zhrf3)
    zhrf3 = re.sub('ز', 'ز', zhrf3)
    zhrf3 = re.sub('ظ', 'ظۗہٰٰ', zhrf3)
    zhrf3 = re.sub('q', '𝐪', zhrf3)
    zhrf3 = re.sub('Q', '𝐪', zhrf3)
    zhrf3 = re.sub('w', '𝐰', zhrf3)
    zhrf3 = re.sub('W', '𝐰', zhrf3)
    zhrf3 = re.sub('e', '𝐞', zhrf3)
    zhrf3 = re.sub('E', '𝐞', zhrf3)
    zhrf3 = re.sub('r', '𝐫', zhrf3)
    zhrf3 = re.sub('R', '𝐫', zhrf3)
    zhrf3 = re.sub('t', '𝐭', zhrf3)
    zhrf3 = re.sub('T', '𝐭', zhrf3)
    zhrf3 = re.sub('y', '𝐲', zhrf3)
    zhrf3 = re.sub('Y', '𝐲', zhrf3)
    zhrf3 = re.sub('u', '𝐮', zhrf3)
    zhrf3 = re.sub('i', '𝐢', zhrf3)
    zhrf3 = re.sub('o', '𝐨', zhrf3)
    zhrf3 = re.sub('p', '𝐩', zhrf3)
    zhrf3 = re.sub('a', '𝐚', zhrf3)
    zhrf3 = re.sub('s', '𝐬', zhrf3)
    zhrf3 = re.sub('d', '𝐝', zhrf3)
    zhrf3 = re.sub('f', '𝐟', zhrf3)
    zhrf3 = re.sub('g', '𝐠', zhrf3)
    zhrf3 = re.sub('h', '𝐡', zhrf3)
    zhrf3 = re.sub('j', '𝐣', zhrf3)
    zhrf3 = re.sub('k', '𝐤', zhrf3)
    zhrf3 = re.sub('U', '𝐮', zhrf3)
    zhrf3 = re.sub('I', '𝐢', zhrf3)
    zhrf3 = re.sub('O', '𝐨', zhrf3)
    zhrf3 = re.sub('P', '𝐩', zhrf3)
    zhrf3 = re.sub('A', '𝐚', zhrf3)
    zhrf3 = re.sub('S', '𝐬', zhrf3)
    zhrf3 = re.sub('D', '𝐝', zhrf3)
    zhrf3 = re.sub('F', '𝐟', zhrf3)
    zhrf3 = re.sub('G', '𝐠', zhrf3)
    zhrf3 = re.sub('H', '𝐡', zhrf3)
    zhrf3 = re.sub('J', '𝐣', zhrf3)
    zhrf3 = re.sub('K', '𝐤', zhrf3)
    zhrf3 = re.sub('L', '𝐥', zhrf3)
    zhrf3 = re.sub('l', '𝐥', zhrf3)
    zhrf3 = re.sub('z', '𝐳', zhrf3)
    zhrf3 = re.sub('Z', '𝐳', zhrf3)
    zhrf3 = re.sub('x', '𝐱', zhrf3)
    zhrf3 = re.sub('X', 'ẋ', zhrf3)
    zhrf3 = re.sub('c', '𝐜', zhrf3)
    zhrf3 = re.sub('C', '𝐜', zhrf3)
    zhrf3 = re.sub('v', '𝐯', zhrf3)
    zhrf3 = re.sub('V', '𝐯', zhrf3)
    zhrf3 = re.sub('b', '𝐛', zhrf3)
    zhrf3 = re.sub('B', '𝐛', zhrf3)
    zhrf3 = re.sub('n', '𝐧', zhrf3)
    zhrf3 = re.sub('N', '𝐧', zhrf3)
    zhrf3 = re.sub('m', '𝐦', zhrf3)
    zhrf3 = re.sub('M', '𝐦', zhrf3)

    zhrf4 = re.sub('ض', 'ضۜہٰٰ', text)
    zhrf4 = re.sub('ص', 'ضۜہٰٰ', zhrf4)
    zhrf4 = re.sub('ث', 'ثہٰٰ', zhrf4)
    zhrf4 = re.sub('ق', 'قྀ̲ہٰٰ', zhrf4)
    zhrf4 = re.sub('ف', 'ف͒ہٰٰ', zhrf4)
    zhrf4 = re.sub('غ', 'غہٰٰ', zhrf4)
    zhrf4 = re.sub('ع', 'عہٰٰ', zhrf4)
    zhrf4 = re.sub('ه', 'هٰہٰٖ', zhrf4)
    zhrf4 = re.sub('خ', 'خٰ̐ہ ', zhrf4)
    zhrf4 = re.sub('ح', 'حہٰٰ', zhrf4)
    zhrf4 = re.sub('ج', 'جـٰ̲ـہْۧ', zhrf4)
    zhrf4 = re.sub('د', 'دٰ', zhrf4)
    zhrf4 = re.sub('ذ', 'ذِٰ', zhrf4)
    zhrf4 = re.sub('ش', 'شِٰہٰٰ', zhrf4)
    zhrf4 = re.sub('س', 'سٰٓ', zhrf4)
    zhrf4 = re.sub('ي', 'يِٰہ', zhrf4)
    zhrf4 = re.sub('ب', 'بّہ', zhrf4)
    zhrf4 = re.sub('ل', 'لـٰ̲ـہ', zhrf4)
    zhrf4 = re.sub('ا', 'آ', zhrf4)
    zhrf4 = re.sub('ت', 'تَہَٰ', zhrf4)
    zhrf4 = re.sub('ن', 'نَِہ', zhrf4)
    zhrf4 = re.sub('م', 'مٰ̲ہ', zhrf4)
    zhrf4 = re.sub('ك', 'ڪٰྀہٰٰ', zhrf4)
    zhrf4 = re.sub('ط', 'طۨہٰٰ', zhrf4)
    zhrf4 = re.sub('ئ', 'ئ ْٰ', zhrf4)
    zhrf4 = re.sub('ء', 'ء', zhrf4)
    zhrf4 = re.sub('ؤ', 'ؤ', zhrf4)
    zhrf4 = re.sub('ر', 'رَ', zhrf4)
    zhrf4 = re.sub('لا', 'لہا', zhrf4)
    zhrf4 = re.sub('ى', 'ىْ', zhrf4)
    zhrf4 = re.sub('ة', 'ة', zhrf4)
    zhrf4 = re.sub('و', 'وِٰ', zhrf4)
    zhrf4 = re.sub('ز', 'زَٰ', zhrf4)
    zhrf4 = re.sub('ظ', 'ظۗہٰٰ', zhrf4)
    zhrf4 = re.sub('q', '𝑸', zhrf4)
    zhrf4 = re.sub('Q', '𝑸', zhrf4)
    zhrf4 = re.sub('w', '𝑾', zhrf4)
    zhrf4 = re.sub('W', '𝑾', zhrf4)
    zhrf4 = re.sub('e', '𝑬', zhrf4)
    zhrf4 = re.sub('E', '𝑬', zhrf4)
    zhrf4 = re.sub('r', '𝑹', zhrf4)
    zhrf4 = re.sub('R', '𝑹', zhrf4)
    zhrf4 = re.sub('t', '𝑻', zhrf4)
    zhrf4 = re.sub('T', '𝑻', zhrf4)
    zhrf4 = re.sub('y', '𝒀', zhrf4)
    zhrf4 = re.sub('Y', '𝒀', zhrf4)
    zhrf4 = re.sub('u', '𝑼', zhrf4)
    zhrf4 = re.sub('U', '𝑼', zhrf4)
    zhrf4 = re.sub('i', '𝑰', zhrf4)
    zhrf4 = re.sub('I', '𝑰', zhrf4)
    zhrf4 = re.sub('o', '𝑶', zhrf4)
    zhrf4 = re.sub('O', '𝑶', zhrf4)
    zhrf4 = re.sub('p', '𝑷', zhrf4)
    zhrf4 = re.sub('P', '𝑷', zhrf4)
    zhrf4 = re.sub('a', '𝑨', zhrf4)
    zhrf4 = re.sub('A', '𝑨', zhrf4)
    zhrf4 = re.sub('s', '𝑺', zhrf4)
    zhrf4 = re.sub('S', '𝑺', zhrf4)
    zhrf4 = re.sub('d', '𝑫', zhrf4)
    zhrf4 = re.sub('D', '𝑫', zhrf4)
    zhrf4 = re.sub('f', '𝑭', zhrf4)
    zhrf4 = re.sub('F', '𝑭', zhrf4)
    zhrf4 = re.sub('g', '𝑮', zhrf4)
    zhrf4 = re.sub('G', '𝑮', zhrf4)
    zhrf4 = re.sub('h', '𝑯', zhrf4)
    zhrf4 = re.sub('H', '𝑯', zhrf4)
    zhrf4 = re.sub('j', '𝑱', zhrf4)
    zhrf4 = re.sub('J', '𝑱', zhrf4)
    zhrf4 = re.sub('k', '𝑲', zhrf4)
    zhrf4 = re.sub('K', '𝑲', zhrf4)
    zhrf4 = re.sub('l', '𝑳', zhrf4)
    zhrf4 = re.sub('L', '𝑳', zhrf4)
    zhrf4 = re.sub('z', '𝒁', zhrf4)
    zhrf4 = re.sub('Z', '𝒁', zhrf4)
    zhrf4 = re.sub('x', '𝑿', zhrf4)
    zhrf4 = re.sub('X', '𝑿', zhrf4)
    zhrf4 = re.sub('c', '𝑪', zhrf4)
    zhrf4 = re.sub('C', '𝑪', zhrf4)
    zhrf4 = re.sub('v', '𝑽', zhrf4)
    zhrf4 = re.sub('V', '𝑽', zhrf4)
    zhrf4 = re.sub('b', '𝑩', zhrf4)
    zhrf4 = re.sub('B', '𝑩', zhrf4)
    zhrf4 = re.sub('n', '𝑵', zhrf4)
    zhrf4 = re.sub('N', '𝑵', zhrf4)
    zhrf4 = re.sub('m', '𝑴', zhrf4)
    zhrf4 = re.sub('M', '𝑴', zhrf4)

    zhrf5 = re.sub('ض', 'ضَ', text)
    zhrf5 = re.sub('ص', 'صً', zhrf5)
    zhrf5 = re.sub('ث', 'ثَ', zhrf5)
    zhrf5 = re.sub('ق', 'قُ', zhrf5)
    zhrf5 = re.sub('ف', 'فّ', zhrf5)
    zhrf5 = re.sub('غ', 'غِ', zhrf5)
    zhrf5 = re.sub('ع', 'عُ', zhrf5)
    zhrf5 = re.sub('ه', 'ﮭ', zhrf5)
    zhrf5 = re.sub('خ', 'خِ', zhrf5)
    zhrf5 = re.sub('ح', 'حٌ', zhrf5)
    zhrf5 = re.sub('ج', 'جُ', zhrf5)
    zhrf5 = re.sub('د', 'دِ', zhrf5)
    zhrf5 = re.sub('ذ', 'ذَ', zhrf5)
    zhrf5 = re.sub('ش', 'شِ', zhrf5)
    zhrf5 = re.sub('س', 'سً', zhrf5)
    zhrf5 = re.sub('ي', 'يْ', zhrf5)
    zhrf5 = re.sub('ب', 'بّ', zhrf5)
    zhrf5 = re.sub('ل', 'لَ', zhrf5)
    zhrf5 = re.sub('ا', 'أُ', zhrf5)
    zhrf5 = re.sub('ت', 'تٌ', zhrf5)
    zhrf5 = re.sub('ن', 'نً', zhrf5)
    zhrf5 = re.sub('م', 'مِ', zhrf5)
    zhrf5 = re.sub('ك', 'ڳّ', zhrf5)
    zhrf5 = re.sub('ط', 'طٌ', zhrf5)
    zhrf5 = re.sub('ئ', 'ئ', zhrf5)
    zhrf5 = re.sub('ء', 'ء', zhrf5)
    zhrf5 = re.sub('ؤ', 'ؤ', zhrf5)
    zhrf5 = re.sub('ر', 'رٌ', zhrf5)
    zhrf5 = re.sub('لا', 'لٌأً', zhrf5)
    zhrf5 = re.sub('ى', 'ى', zhrf5)
    zhrf5 = re.sub('ة', 'ةَ', zhrf5)
    zhrf5 = re.sub('و', 'وِ', zhrf5)
    zhrf5 = re.sub('ز', 'زُ', zhrf5)
    zhrf5 = re.sub('ظ', 'ظ', zhrf5)
    zhrf5 = re.sub('q', '𝒒', zhrf5)
    zhrf5 = re.sub('Q', '𝒒', zhrf5)
    zhrf5 = re.sub('w', '𝒘', zhrf5)
    zhrf5 = re.sub('W', '𝒘', zhrf5)
    zhrf5 = re.sub('e', '𝒆', zhrf5)
    zhrf5 = re.sub('E', '𝒆', zhrf5)
    zhrf5 = re.sub('r', '𝒓', zhrf5)
    zhrf5 = re.sub('R', '𝒓', zhrf5)
    zhrf5 = re.sub('t', '𝒕', zhrf5)
    zhrf5 = re.sub('T', '𝒕', zhrf5)
    zhrf5 = re.sub('y', '𝒚', zhrf5)
    zhrf5 = re.sub('Y', '𝒚', zhrf5)
    zhrf5 = re.sub('u', '𝒖', zhrf5)
    zhrf5 = re.sub('U', '𝒖', zhrf5)
    zhrf5 = re.sub('i', '𝒊', zhrf5)
    zhrf5 = re.sub('I', '𝒊', zhrf5)
    zhrf5 = re.sub('o', '𝒐', zhrf5)
    zhrf5 = re.sub('O', '𝒐', zhrf5)
    zhrf5 = re.sub('p', '𝒑', zhrf5)
    zhrf5 = re.sub('P', '𝒑', zhrf5)
    zhrf5 = re.sub('a', '𝒂', zhrf5)
    zhrf5 = re.sub('A', '𝒂', zhrf5)
    zhrf5 = re.sub('s', '𝒔', zhrf5)
    zhrf5 = re.sub('S', '𝒔', zhrf5)
    zhrf5 = re.sub('d', '𝒅', zhrf5)
    zhrf5 = re.sub('D', '𝒅', zhrf5)
    zhrf5 = re.sub('f', '𝒇', zhrf5)
    zhrf5 = re.sub('F', '𝒇', zhrf5)
    zhrf5 = re.sub('g', '𝒈', zhrf5)
    zhrf5 = re.sub('G', '𝒈', zhrf5)
    zhrf5 = re.sub('h', '𝒉', zhrf5)
    zhrf5 = re.sub('H', '𝒉', zhrf5)
    zhrf5 = re.sub('j', '𝒋', zhrf5)
    zhrf5 = re.sub('J', '𝒋', zhrf5)
    zhrf5 = re.sub('K', '𝒌', zhrf5)
    zhrf5 = re.sub('k', '??', zhrf5)
    zhrf5 = re.sub('L', '𝒍', zhrf5)
    zhrf5 = re.sub('l', '𝒍', zhrf5)
    zhrf5 = re.sub('z', '𝒛', zhrf5)
    zhrf5 = re.sub('Z', '𝒛', zhrf5)
    zhrf5 = re.sub('x', '𝒙', zhrf5)
    zhrf5 = re.sub('X', '𝒙', zhrf5)
    zhrf5 = re.sub('c', '𝒄', zhrf5)
    zhrf5 = re.sub('C', '𝒄', zhrf5)
    zhrf5 = re.sub('v', '𝒗', zhrf5)
    zhrf5 = re.sub('V', '𝒗', zhrf5)
    zhrf5 = re.sub('b', '𝒃', zhrf5)
    zhrf5 = re.sub('B', '𝒃', zhrf5)
    zhrf5 = re.sub('n', '𝒏', zhrf5)
    zhrf5 = re.sub('N', '𝒏', zhrf5)
    zhrf5 = re.sub('m', '𝒎', zhrf5)
    zhrf5 = re.sub('M', '𝒎', zhrf5)

    zhrf6 = re.sub('ض', 'ﺿ̭͠', text)
    zhrf6 = re.sub('ص', 'ﺻ͡', zhrf6)
    zhrf6 = re.sub('ث', 'ﺜ̲', zhrf6)
    zhrf6 = re.sub('ق', 'ﭰ', zhrf6)
    zhrf6 = re.sub('ف', 'ﻓ̲', zhrf6)
    zhrf6 = re.sub('غ', 'ﻏ̲', zhrf6)
    zhrf6 = re.sub('ع', 'ﻌ̲', zhrf6)
    zhrf6 = re.sub('ه', 'ﮬ̲̌', zhrf6)
    zhrf6 = re.sub('خ', 'خٌ', zhrf6)
    zhrf6 = re.sub('ح', 'ﺣ̅', zhrf6)
    zhrf6 = re.sub('ج', 'جُ', zhrf6)
    zhrf6 = re.sub('د', 'ډ̝', zhrf6)
    zhrf6 = re.sub('ذ', 'ذً', zhrf6)
    zhrf6 = re.sub('ش', 'ﺷ̲', zhrf6)
    zhrf6 = re.sub('س', 'ﺳ̉', zhrf6)
    zhrf6 = re.sub('ي', 'ﯾ̃̐', zhrf6)
    zhrf6 = re.sub('ب', 'ﺑ̲', zhrf6)
    zhrf6 = re.sub('ل', 'ا̄ﻟ', zhrf6)
    zhrf6 = re.sub('ا', 'ﺈ̃', zhrf6)
    zhrf6 = re.sub('ت', 'ټُ', zhrf6)
    zhrf6 = re.sub('ن', 'ﻧ̲', zhrf6)
    zhrf6 = re.sub('م', 'ﻣ̲̉', zhrf6)
    zhrf6 = re.sub('ك', 'گ', zhrf6)
    zhrf6 = re.sub('ط', 'ﻁ̲', zhrf6)
    zhrf6 = re.sub('ئ', ' ْٰئ', zhrf6)
    zhrf6 = re.sub('ء', 'ء', zhrf6)
    zhrf6 = re.sub('ؤ', 'ؤ', zhrf6)
    zhrf6 = re.sub('ر', 'ہڕ', zhrf6)
    zhrf6 = re.sub('لا', 'ﻟ̲ﺂ̲', zhrf6)
    zhrf6 = re.sub('ى', 'ى', zhrf6)
    zhrf6 = re.sub('ة', 'ة', zhrf6)
    zhrf6 = re.sub('و', 'ۇۈۉ', zhrf6)
    zhrf6 = re.sub('ز', 'زُ', zhrf6)
    zhrf6 = re.sub('ظ', 'ﻇ̲', zhrf6)
    zhrf6 = re.sub('q', 'ǫ', zhrf6)
    zhrf6 = re.sub('Q', 'ǫ', zhrf6)
    zhrf6 = re.sub('w', 'ᴡ', zhrf6)
    zhrf6 = re.sub('W', 'ᴡ', zhrf6)
    zhrf6 = re.sub('e', 'ᴇ', zhrf6)
    zhrf6 = re.sub('E', 'ᴇ', zhrf6)
    zhrf6 = re.sub('r', 'ʀ', zhrf6)
    zhrf6 = re.sub('R', 'ʀ', zhrf6)
    zhrf6 = re.sub('t', 'ᴛ', zhrf6)
    zhrf6 = re.sub('T', 'ᴛ', zhrf6)
    zhrf6 = re.sub('y', 'ʏ', zhrf6)
    zhrf6 = re.sub('Y', 'ʏ', zhrf6)
    zhrf6 = re.sub('u', 'ụ', zhrf6)
    zhrf6 = re.sub('U', 'ụ', zhrf6)
    zhrf6 = re.sub('i', 'ɪ', zhrf6)
    zhrf6 = re.sub('I', 'ɪ', zhrf6)
    zhrf6 = re.sub('o', 'ᴏ', zhrf6)
    zhrf6 = re.sub('O', 'ᴏ', zhrf6)
    zhrf6 = re.sub('p', 'ᴘ', zhrf6)
    zhrf6 = re.sub('P', 'ᴘ', zhrf6)
    zhrf6 = re.sub('a', 'ᴀ', zhrf6)
    zhrf6 = re.sub('A', 'ᴀ', zhrf6)
    zhrf6 = re.sub('s', 'ѕ', zhrf6)
    zhrf6 = re.sub('S', 'ѕ', zhrf6)
    zhrf6 = re.sub('d', 'ᴅ', zhrf6)
    zhrf6 = re.sub('D', 'ᴅ', zhrf6)
    zhrf6 = re.sub('f', 'ғ', zhrf6)
    zhrf6 = re.sub('F', 'ғ', zhrf6)
    zhrf6 = re.sub('g', 'ɢ', zhrf6)
    zhrf6 = re.sub('G', 'ɢ', zhrf6)
    zhrf6 = re.sub('h', 'ʜ', zhrf6)
    zhrf6 = re.sub('H', 'ʜ', zhrf6)
    zhrf6 = re.sub('j', 'ᴊ', zhrf6)
    zhrf6 = re.sub('J', 'ᴊ', zhrf6)
    zhrf6 = re.sub('K', 'ᴋ', zhrf6)
    zhrf6 = re.sub('k', 'ᴋ', zhrf6)
    zhrf6 = re.sub('L', 'ʟ', zhrf6)
    zhrf6 = re.sub('l', 'ʟ', zhrf6)
    zhrf6 = re.sub('z', 'ᴢ', zhrf6)
    zhrf6 = re.sub('Z', 'ᴢ', zhrf6)
    zhrf6 = re.sub('x', 'х', zhrf6)
    zhrf6 = re.sub('X', 'х', zhrf6)
    zhrf6 = re.sub('c', 'ᴄ', zhrf6)
    zhrf6 = re.sub('C', 'ᴄ', zhrf6)
    zhrf6 = re.sub('v', 'ᴠ', zhrf6)
    zhrf6 = re.sub('V', 'ᴠ', zhrf6)
    zhrf6 = re.sub('b', 'ʙ', zhrf6)
    zhrf6 = re.sub('B', 'ʙ', zhrf6)
    zhrf6 = re.sub('n', 'ɴ', zhrf6)
    zhrf6 = re.sub('N', 'ɴ', zhrf6)
    zhrf6 = re.sub('m', 'ᴍ', zhrf6)
    zhrf6 = re.sub('M', 'ᴍ', zhrf6)

    zhrf7 = re.sub('ض', 'ﺿ', text)
    zhrf7 = re.sub('ص', 'ﺻ', zhrf7)
    zhrf7 = re.sub('ث', 'ﭥ', zhrf7)
    zhrf7 = re.sub('ق', 'ﻗ̮ـ̃', zhrf7)
    zhrf7 = re.sub('ف', 'ﭬ', zhrf7)
    zhrf7 = re.sub('غ', 'ﻏ̣̐', zhrf7)
    zhrf7 = re.sub('ع', 'ﻋ', zhrf7)
    zhrf7 = re.sub('ه', 'ھَہّ', zhrf7)
    zhrf7 = re.sub('خ', 'ﺧ', zhrf7)
    zhrf7 = re.sub('ح', 'פ', zhrf7)
    zhrf7 = re.sub('ج', 'ﭴ', zhrf7)
    zhrf7 = re.sub('د', 'ﮃ', zhrf7)
    zhrf7 = re.sub('ذ', 'ذ', zhrf7)
    zhrf7 = re.sub('ش', 'ﺷ', zhrf7)
    zhrf7 = re.sub('س', 'ﺳ', zhrf7)
    zhrf7 = re.sub('ي', 'ﯾ', zhrf7)
    zhrf7 = re.sub('ب', 'ﺑ', zhrf7)
    zhrf7 = re.sub('ل', 'ﻟ', zhrf7)
    zhrf7 = re.sub('ا', 'ﺂ', zhrf7)
    zhrf7 = re.sub('ت', 'ﭠ', zhrf7)
    zhrf7 = re.sub('ن', 'ﻧ', zhrf7)
    zhrf7 = re.sub('م', 'ﻣ̝̚', zhrf7)
    zhrf7 = re.sub('ك', 'گـ', zhrf7)
    zhrf7 = re.sub('ط', 'ﻁْ', zhrf7)
    zhrf7 = re.sub('ئ', 'ٰئـ', zhrf7)
    zhrf7 = re.sub('ء', 'ء', zhrf7)
    zhrf7 = re.sub('ؤ', 'ﯗ', zhrf7)
    zhrf7 = re.sub('ر', 'ړُ', zhrf7)
    zhrf7 = re.sub('لا', 'ﻟآ', zhrf7)
    zhrf7 = re.sub('ى', 'ـﮯ', zhrf7)
    zhrf7 = re.sub('ة', 'ة', zhrf7)
    zhrf7 = re.sub('و', 'ۆ', zhrf7)
    zhrf7 = re.sub('ز', 'ژ', zhrf7)
    zhrf7 = re.sub('ظ', 'ﻅ', zhrf7)
    zhrf7 = re.sub('q', '𝘘', zhrf7)
    zhrf7 = re.sub('Q', '𝘘', zhrf7)
    zhrf7 = re.sub('w', '𝘞', zhrf7)
    zhrf7 = re.sub('W', '𝘞', zhrf7)
    zhrf7 = re.sub('e', '𝘌', zhrf7)
    zhrf7 = re.sub('E', '𝘌', zhrf7)
    zhrf7 = re.sub('r', '𝘙', zhrf7)
    zhrf7 = re.sub('R', '𝘙', zhrf7)
    zhrf7 = re.sub('t', '𝘛', zhrf7)
    zhrf7 = re.sub('T', '𝘛', zhrf7)
    zhrf7 = re.sub('y', '𝘠', zhrf7)
    zhrf7 = re.sub('Y', '𝘠', zhrf7)
    zhrf7 = re.sub('u', '𝘜', zhrf7)
    zhrf7 = re.sub('U', '𝘜', zhrf7)
    zhrf7 = re.sub('i', '𝘐', zhrf7)
    zhrf7 = re.sub('I', '𝘐', zhrf7)
    zhrf7 = re.sub('o', '𝘖', zhrf7)
    zhrf7 = re.sub('O', '𝘖', zhrf7)
    zhrf7 = re.sub('p', '𝘗', zhrf7)
    zhrf7 = re.sub('P', '𝘗', zhrf7)
    zhrf7 = re.sub('a', '𝘈', zhrf7)
    zhrf7 = re.sub('A', '𝘈', zhrf7)
    zhrf7 = re.sub('s', '𝘚', zhrf7)
    zhrf7 = re.sub('S', '𝘚', zhrf7)
    zhrf7 = re.sub('d', '𝘋', zhrf7)
    zhrf7 = re.sub('D', '𝘋', zhrf7)
    zhrf7 = re.sub('f', '𝘍', zhrf7)
    zhrf7 = re.sub('F', '𝘍', zhrf7)
    zhrf7 = re.sub('g', '𝘎', zhrf7)
    zhrf7 = re.sub('G', '𝘎', zhrf7)
    zhrf7 = re.sub('h', '𝘏', zhrf7)
    zhrf7 = re.sub('H', '𝘏', zhrf7)
    zhrf7 = re.sub('j', '𝘑', zhrf7)
    zhrf7 = re.sub('J', '𝘑', zhrf7)
    zhrf7 = re.sub('k', '𝘒', zhrf7)
    zhrf7 = re.sub('K', '𝘒', zhrf7)
    zhrf7 = re.sub('L', '𝘓', zhrf7)
    zhrf7 = re.sub('l', '𝘓', zhrf7)
    zhrf7 = re.sub('z', '𝘡', zhrf7)
    zhrf7 = re.sub('Z', '𝘡', zhrf7)
    zhrf7 = re.sub('x', '𝘟', zhrf7)
    zhrf7 = re.sub('X', '𝘟', zhrf7)
    zhrf7 = re.sub('c', '𝘊', zhrf7)
    zhrf7 = re.sub('C', '𝘊', zhrf7)
    zhrf7 = re.sub('v', '𝘝', zhrf7)
    zhrf7 = re.sub('V', '𝘝', zhrf7)
    zhrf7 = re.sub('b', '𝘉', zhrf7)
    zhrf7 = re.sub('B', '𝘉', zhrf7)
    zhrf7 = re.sub('n', '𝘕', zhrf7)
    zhrf7 = re.sub('N', '𝘕', zhrf7)
    zhrf7 = re.sub('m', '𝘔', zhrf7)
    zhrf7 = re.sub('M', '𝘔', zhrf7)

    zhrf8 = re.sub('ض', 'ض', text)
    zhrf8 = re.sub('ص', 'صہٰ', zhrf8)
    zhrf8 = re.sub('ث', 'ثہٰـ', zhrf8)
    zhrf8 = re.sub('ق', 'قہٰ', zhrf8)
    zhrf8 = re.sub('ف', 'فہٰ', zhrf8)
    zhrf8 = re.sub('غ', 'غـْ', zhrf8)
    zhrf8 = re.sub('ع', 'ع', zhrf8)
    zhrf8 = re.sub('ه', 'هٰہٰٖ', zhrf8)
    zhrf8 = re.sub('خ', 'خخَـ', zhrf8)
    zhrf8 = re.sub('ح', 'حہٰ', zhrf8)
    zhrf8 = re.sub('ج', 'ججہٰ', zhrf8)
    zhrf8 = re.sub('د', 'دَ', zhrf8)
    zhrf8 = re.sub('ذ', 'ذّ', zhrf8)
    zhrf8 = re.sub('ش', 'ششہٰ', zhrf8)
    zhrf8 = re.sub('س', 'سہٰ', zhrf8)
    zhrf8 = re.sub('ي', 'يٰ', zhrf8)
    zhrf8 = re.sub('ب', 'بٰٰ', zhrf8)
    zhrf8 = re.sub('ل', 'لہٰ', zhrf8)
    zhrf8 = re.sub('ا', 'آ', zhrf8)
    zhrf8 = re.sub('ت', 'تہٰ', zhrf8)
    zhrf8 = re.sub('ن', 'نہٰ', zhrf8)
    zhrf8 = re.sub('م', 'مہٰ', zhrf8)
    zhrf8 = re.sub('ك', 'ككہٰ', zhrf8)
    zhrf8 = re.sub('ط', 'طہٰ', zhrf8)
    zhrf8 = re.sub('ئ', ' ْئٰ', zhrf8)
    zhrf8 = re.sub('ء', 'ء', zhrf8)
    zhrf8 = re.sub('ؤ', 'ؤؤَ', zhrf8)
    zhrf8 = re.sub('ر', 'رَ', zhrf8)
    zhrf8 = re.sub('لا', 'لہٰا', zhrf8)
    zhrf8 = re.sub('ى', 'ىہٰ', zhrf8)
    zhrf8 = re.sub('ة', 'ة', zhrf8)
    zhrf8 = re.sub('و', 'ہٰو', zhrf8)
    zhrf8 = re.sub('ز', 'ز', zhrf8)
    zhrf8 = re.sub('ظ', 'ظہٰ', zhrf8)
    zhrf8 = re.sub('q', '𝚀', zhrf8)
    zhrf8 = re.sub('Q', '𝚀', zhrf8)
    zhrf8 = re.sub('w', '𝚆', zhrf8)
    zhrf8 = re.sub('W', '𝚆', zhrf8)
    zhrf8 = re.sub('e', '𝙴', zhrf8)
    zhrf8 = re.sub('E', '𝙴', zhrf8)
    zhrf8 = re.sub('r', '𝚁', zhrf8)
    zhrf8 = re.sub('R', '𝚁', zhrf8)
    zhrf8 = re.sub('t', '𝚃', zhrf8)
    zhrf8 = re.sub('T', '𝚃', zhrf8)
    zhrf8 = re.sub('y', '𝚈', zhrf8)
    zhrf8 = re.sub('Y', '𝚈', zhrf8)
    zhrf8 = re.sub('u', '𝚄', zhrf8)
    zhrf8 = re.sub('U', '𝚄', zhrf8)
    zhrf8 = re.sub('i', '𝙸', zhrf8)
    zhrf8 = re.sub('I', '𝙸', zhrf8)
    zhrf8 = re.sub('o', '𝙾', zhrf8)
    zhrf8 = re.sub('O', '𝙾', zhrf8)
    zhrf8 = re.sub('p', '𝙿', zhrf8)
    zhrf8 = re.sub('P', '𝙿', zhrf8)
    zhrf8 = re.sub('a', '𝙰', zhrf8)
    zhrf8 = re.sub('A', '𝙰', zhrf8)
    zhrf8 = re.sub('s', '𝚂', zhrf8)
    zhrf8 = re.sub('S', '𝚂', zhrf8)
    zhrf8 = re.sub('d', '𝙳', zhrf8)
    zhrf8 = re.sub('D', '𝙳', zhrf8)
    zhrf8 = re.sub('f', '𝙵', zhrf8)
    zhrf8 = re.sub('F', '𝙵', zhrf8)
    zhrf8 = re.sub('g', '𝙶', zhrf8)
    zhrf8 = re.sub('G', '𝙶', zhrf8)
    zhrf8 = re.sub('h', '𝙷', zhrf8)
    zhrf8 = re.sub('H', '𝙷', zhrf8)
    zhrf8 = re.sub('j', '𝙹', zhrf8)
    zhrf8 = re.sub('J', '𝙹', zhrf8)
    zhrf8 = re.sub('k', '𝙺', zhrf8)
    zhrf8 = re.sub('K', '𝙺', zhrf8)
    zhrf8 = re.sub('L', '𝙻', zhrf8)
    zhrf8 = re.sub('l', '𝙻', zhrf8)
    zhrf8 = re.sub('z', '𝚉', zhrf8)
    zhrf8 = re.sub('Z', '𝚉', zhrf8)
    zhrf8 = re.sub('x', '𝚇', zhrf8)
    zhrf8 = re.sub('X', '𝚇', zhrf8)
    zhrf8 = re.sub('c', '𝙲', zhrf8)
    zhrf8 = re.sub('C', '𝙲', zhrf8)
    zhrf8 = re.sub('v', '𝚅', zhrf8)
    zhrf8 = re.sub('V', '𝚅', zhrf8)
    zhrf8 = re.sub('b', '𝙱', zhrf8)
    zhrf8 = re.sub('B', '𝙱', zhrf8)
    zhrf8 = re.sub('n', '𝙽', zhrf8)
    zhrf8 = re.sub('N', '𝙽', zhrf8)
    zhrf8 = re.sub('m', '𝙼', zhrf8)
    zhrf8 = re.sub('M', '𝙼', zhrf8)

    zhrf9 = re.sub('ض', 'ض', text)
    zhrf9 = re.sub('ص', 'ص', zhrf9)
    zhrf9 = re.sub('ث', 'ث', zhrf9)
    zhrf9 = re.sub('ق', 'قٌ', zhrf9)
    zhrf9 = re.sub('ف', 'فُ', zhrf9)
    zhrf9 = re.sub('غ', 'غ', zhrf9)
    zhrf9 = re.sub('ع', 'عٍ', zhrf9)
    zhrf9 = re.sub('ه', 'هـ', zhrf9)
    zhrf9 = re.sub('خ', 'خـ', zhrf9)
    zhrf9 = re.sub('ح', 'حٍ', zhrf9)
    zhrf9 = re.sub('ج', 'جٍ', zhrf9)
    zhrf9 = re.sub('د', 'دِ', zhrf9)
    zhrf9 = re.sub('ذ', 'ذَ', zhrf9)
    zhrf9 = re.sub('ش', 'شُ', zhrf9)
    zhrf9 = re.sub('س', 'س', zhrf9)
    zhrf9 = re.sub('ي', 'ي', zhrf9)
    zhrf9 = re.sub('ب', 'بَ', zhrf9)
    zhrf9 = re.sub('ل', 'لُِ', zhrf9)
    zhrf9 = re.sub('ا', 'آ', zhrf9)
    zhrf9 = re.sub('ت', 'ت', zhrf9)
    zhrf9 = re.sub('ن', 'ن', zhrf9)
    zhrf9 = re.sub('م', 'م', zhrf9)
    zhrf9 = re.sub('ك', 'ڪ', zhrf9)
    zhrf9 = re.sub('ط', 'طُ', zhrf9)
    zhrf9 = re.sub('ئ', 'ئ ْٰ', zhrf9)
    zhrf9 = re.sub('ء', 'ء', zhrf9)
    zhrf9 = re.sub('ؤ', 'ؤ', zhrf9)
    zhrf9 = re.sub('ر', 'ر', zhrf9)
    zhrf9 = re.sub('لا', 'لُِآ', zhrf9)
    zhrf9 = re.sub('ى', 'ىْ', zhrf9)
    zhrf9 = re.sub('ة', 'ة', zhrf9)
    zhrf9 = re.sub('و', 'وو', zhrf9)
    zhrf9 = re.sub('ز', 'ز', zhrf9)
    zhrf9 = re.sub('ظ', 'ظهُ', zhrf9)
    zhrf9 = re.sub('q', 'ℚ', zhrf9)
    zhrf9 = re.sub('Q', 'ℚ', zhrf9)
    zhrf9 = re.sub('w', '𝕎', zhrf9)
    zhrf9 = re.sub('W', '𝕎', zhrf9)
    zhrf9 = re.sub('e', '𝔼', zhrf9)
    zhrf9 = re.sub('E', '𝔼', zhrf9)
    zhrf9 = re.sub('r', 'ℝ', zhrf9)
    zhrf9 = re.sub('R', 'ℝ', zhrf9)
    zhrf9 = re.sub('t', '𝕋', zhrf9)
    zhrf9 = re.sub('T', '𝕋', zhrf9)
    zhrf9 = re.sub('y', '𝕐', zhrf9)
    zhrf9 = re.sub('Y', '𝕐', zhrf9)
    zhrf9 = re.sub('u', '𝕌', zhrf9)
    zhrf9 = re.sub('U', '𝕌', zhrf9)
    zhrf9 = re.sub('i', '𝕀', zhrf9)
    zhrf9 = re.sub('I', '𝕀', zhrf9)
    zhrf9 = re.sub('o', '𝕆', zhrf9)
    zhrf9 = re.sub('O', '𝕆', zhrf9)
    zhrf9 = re.sub('p', 'ℙ', zhrf9)
    zhrf9 = re.sub('P', 'ℙ', zhrf9)
    zhrf9 = re.sub('a', '𝔸', zhrf9)
    zhrf9 = re.sub('A', '𝔸', zhrf9)
    zhrf9 = re.sub('s', '𝕊', zhrf9)
    zhrf9 = re.sub('S', '𝕊', zhrf9)
    zhrf9 = re.sub('d', '𝔻', zhrf9)
    zhrf9 = re.sub('D', '𝔻', zhrf9)
    zhrf9 = re.sub('f', '𝔽', zhrf9)
    zhrf9 = re.sub('F', '𝔽', zhrf9)
    zhrf9 = re.sub('g', '𝔾', zhrf9)
    zhrf9 = re.sub('G', '𝔾', zhrf9)
    zhrf9 = re.sub('h', 'ℍ', zhrf9)
    zhrf9 = re.sub('H', 'ℍ', zhrf9)
    zhrf9 = re.sub('j', '𝕁', zhrf9)
    zhrf9 = re.sub('J', '𝕁', zhrf9)
    zhrf9 = re.sub('k', '𝕂', zhrf9)
    zhrf9 = re.sub('K', '𝕂', zhrf9)
    zhrf9 = re.sub('L', '𝕃', zhrf9)
    zhrf9 = re.sub('l', '𝕃', zhrf9)
    zhrf9 = re.sub('z', 'ℤ', zhrf9)
    zhrf9 = re.sub('Z', 'ℤ', zhrf9)
    zhrf9 = re.sub('x', '𝕏', zhrf9)
    zhrf9 = re.sub('X', '𝕏', zhrf9)
    zhrf9 = re.sub('c', 'ℂ', zhrf9)
    zhrf9 = re.sub('C', 'ℂ', zhrf9)
    zhrf9 = re.sub('v', '𝕍', zhrf9)
    zhrf9 = re.sub('V', '𝕍', zhrf9)
    zhrf9 = re.sub('b', '𝔹', zhrf9)
    zhrf9 = re.sub('B', '𝔹', zhrf9)
    zhrf9 = re.sub('n', 'ℕ', zhrf9)
    zhrf9 = re.sub('N', 'ℕ', zhrf9)
    zhrf9 = re.sub('m', '𝕄', zhrf9)
    zhrf9 = re.sub('M', '𝕄', zhrf9)
    
    zhrf10 = re.sub('ض', 'ضۜہٰٰ', text)
    zhrf10 = re.sub('ص', 'ضۜہٰٰ', zhrf10)
    zhrf10 = re.sub('ث', 'ثہٰٰ', zhrf10)
    zhrf10 = re.sub('ق', 'قྀ̲ہٰٰ', zhrf10)
    zhrf10 = re.sub('ف', 'ف͒ہٰٰ', zhrf10)
    zhrf10 = re.sub('غ', 'غہٰٰ', zhrf10)
    zhrf10 = re.sub('ع', 'عہٰٰ', zhrf10)
    zhrf10 = re.sub('ه', 'هٰہٰٖ', zhrf10)
    zhrf10 = re.sub('خ', 'خٰ̐ہ', zhrf10)
    zhrf10 = re.sub('ح', 'حہٰٰ', zhrf10)
    zhrf10 = re.sub('ج', 'جـٰ̲ـہْۧ', zhrf10)
    zhrf10 = re.sub('د', 'دٰ', zhrf10)
    zhrf10 = re.sub('ذ', 'ذِٰ', zhrf10)
    zhrf10 = re.sub('ش', 'شِٰہٰٰ', zhrf10)
    zhrf10 = re.sub('س', 'سٰٓ', zhrf10)
    zhrf10 = re.sub('ي', 'يِٰہ', zhrf10)
    zhrf10 = re.sub('ب', 'بّہ', zhrf10)
    zhrf10 = re.sub('ل', 'لـٰ̲ـہ', zhrf10)
    zhrf10 = re.sub('ا', 'آ', zhrf10)
    zhrf10 = re.sub('ت', 'تَہَ', zhrf10)
    zhrf10 = re.sub('ن', 'نَِہ', zhrf10)
    zhrf10 = re.sub('م', 'مٰ̲ہ', zhrf10)
    zhrf10 = re.sub('ك', 'ڪٰྀہٰٰ', zhrf10)
    zhrf10 = re.sub('ط', 'طۨہٰٰ', zhrf10)
    zhrf10 = re.sub('ئ', 'ئ ْ', zhrf10)
    zhrf10 = re.sub('ء', 'ء', zhrf10)
    zhrf10 = re.sub('ؤ', 'ؤ', zhrf10)
    zhrf10 = re.sub('ر', 'رَ', zhrf10)
    zhrf10 = re.sub('لا', 'لـٰ̲ـہآ', zhrf10)
    zhrf10 = re.sub('ى', 'ىْ', zhrf10)
    zhrf10 = re.sub('ة', 'ة', zhrf10)
    zhrf10 = re.sub('و', 'وِٰ', zhrf10)
    zhrf10 = re.sub('ز', 'زَٰ', zhrf10)
    zhrf10 = re.sub('ظ', 'ظۗہٰٰ', zhrf10)
    zhrf10 = re.sub('a', "Ⓐ", zhrf10)
    zhrf10 = re.sub('A', "Ⓐ", zhrf10)
    zhrf10 = re.sub("b", "Ⓑ", zhrf10)
    zhrf10 = re.sub("B", "Ⓑ", zhrf10)
    zhrf10 = re.sub("c", "Ⓒ", zhrf10)
    zhrf10 = re.sub("C", "Ⓒ", zhrf10)
    zhrf10 = re.sub("d", "Ⓓ", zhrf10)
    zhrf10 = re.sub("D", "Ⓓ", zhrf10)
    zhrf10 = re.sub("e", "Ⓔ", zhrf10)
    zhrf10 = re.sub("E", "Ⓔ", zhrf10)
    zhrf10 = re.sub("f", "Ⓕ", zhrf10)
    zhrf10 = re.sub("F", "Ⓕ", zhrf10)
    zhrf10 = re.sub("g", "Ⓖ", zhrf10)
    zhrf10 = re.sub("G", "Ⓖ", zhrf10)
    zhrf10 = re.sub("h", "Ⓗ", zhrf10)
    zhrf10 = re.sub("H", "Ⓗ", zhrf10)
    zhrf10 = re.sub("i", "Ⓘ", zhrf10)
    zhrf10 = re.sub("I", "Ⓘ", zhrf10)
    zhrf10 = re.sub("j", "Ⓙ", zhrf10)
    zhrf10 = re.sub("J", "Ⓙ", zhrf10)
    zhrf10 = re.sub("k", "Ⓚ", zhrf10)
    zhrf10 = re.sub("K", "Ⓚ", zhrf10)
    zhrf10 = re.sub("l", "Ⓛ", zhrf10)
    zhrf10 = re.sub("L", "Ⓛ", zhrf10)
    zhrf10 = re.sub("m", "Ⓜ", zhrf10)
    zhrf10 = re.sub("M", "Ⓜ", zhrf10)
    zhrf10 = re.sub("n", "Ⓝ", zhrf10)
    zhrf10 = re.sub("N", "Ⓝ", zhrf10)
    zhrf10 = re.sub("o", "Ⓞ", zhrf10)
    zhrf10 = re.sub("O", "Ⓞ", zhrf10)
    zhrf10 = re.sub("p", "Ⓟ", zhrf10)
    zhrf10 = re.sub("P", "Ⓟ", zhrf10)
    zhrf10 = re.sub("q", "Ⓠ", zhrf10)
    zhrf10 = re.sub("Q", "Ⓠ", zhrf10)
    zhrf10 = re.sub("r", "Ⓡ", zhrf10)
    zhrf10 = re.sub("R", "Ⓡ", zhrf10)
    zhrf10 = re.sub("s", "Ⓢ", zhrf10)
    zhrf10 = re.sub("S", "Ⓢ", zhrf10)
    zhrf10 = re.sub("t", "Ⓣ", zhrf10)
    zhrf10 = re.sub("T", "Ⓣ", zhrf10)
    zhrf10 = re.sub("u", "Ⓤ", zhrf10)
    zhrf10 = re.sub("U", "Ⓤ", zhrf10)
    zhrf10 = re.sub("v", "Ⓥ", zhrf10)
    zhrf10 = re.sub("V", "Ⓥ", zhrf10)
    zhrf10 = re.sub("w", "Ⓦ", zhrf10)
    zhrf10 = re.sub("W", "Ⓦ", zhrf10)
    zhrf10 = re.sub("x", "Ⓧ", zhrf10)
    zhrf10 = re.sub("X", "Ⓧ", zhrf10)
    zhrf10 = re.sub("y", "Ⓨ", zhrf10)
    zhrf10 = re.sub("Y", "Ⓨ", zhrf10)
    zhrf10 = re.sub("z", "Ⓩ", zhrf10)
    zhrf10 = re.sub("Z", "Ⓩ", zhrf10)

    zhrf11 = re.sub('ض', 'ضـ🌙ـ', text)
    zhrf11 = re.sub('ص', 'صـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ث', 'ثـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ق', 'قـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ف', 'فـ🌙ـ', zhrf11)
    zhrf11 = re.sub('غ', 'غـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ع', 'عـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ه', 'هّ', zhrf11)
    zhrf11 = re.sub('خ', 'خـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ح', 'حـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ج', 'جـ🌙ـ', zhrf11)
    zhrf11 = re.sub('د', 'د', zhrf11)
    zhrf11 = re.sub('ذ', 'ذ', zhrf11)
    zhrf11 = re.sub('ش', 'شـ🌙ـ', zhrf11)
    zhrf11 = re.sub('س', 'سـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ي', 'يـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ب', 'بـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ل', 'لَ', zhrf11)
    zhrf11 = re.sub('ا', 'آ', zhrf11)
    zhrf11 = re.sub('ت', 'تـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ن', 'نـ🌙ـ', zhrf11)
    zhrf11 = re.sub('م', 'مـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ك', 'كـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ط', 'طـ🌙ـ', zhrf11)
    zhrf11 = re.sub('ئ', 'ئ', zhrf11)
    zhrf11 = re.sub('ء', 'ء', zhrf11)
    zhrf11 = re.sub('ؤ', 'ؤ', zhrf11)
    zhrf11 = re.sub('ر', 'ر', zhrf11)
    zhrf11 = re.sub('لا', 'لَآ', zhrf11)
    zhrf11 = re.sub('ى', 'ى', zhrf11)
    zhrf11 = re.sub('ة', 'ةّ', zhrf11)
    zhrf11 = re.sub('و', 'وٌ', zhrf11)
    zhrf11 = re.sub('ز', 'زِّ', zhrf11)
    zhrf11 = re.sub('ظ', 'ظـ🌙ـ', zhrf11)
    zhrf11 = re.sub('a', "‌🇦", zhrf11)
    zhrf11 = re.sub('A', "‌🇦", zhrf11)
    zhrf11 = re.sub("b", "‌🇧", zhrf11)
    zhrf11 = re.sub("B", "‌🇧", zhrf11)
    zhrf11 = re.sub("c", "‌🇨", zhrf11)
    zhrf11 = re.sub("C", "‌🇨", zhrf11)
    zhrf11 = re.sub("d", "‌🇩", zhrf11)
    zhrf11 = re.sub("D", "‌🇩", zhrf11)
    zhrf11 = re.sub("e", "‌🇪", zhrf11)
    zhrf11 = re.sub("E", "‌🇪", zhrf11)
    zhrf11 = re.sub("f", "‌🇫", zhrf11)
    zhrf11 = re.sub("F", "‌🇫", zhrf11)
    zhrf11 = re.sub("g", "‌🇬", zhrf11)
    zhrf11 = re.sub("G", "‌🇬", zhrf11)
    zhrf11 = re.sub("h", "‌🇭", zhrf11)
    zhrf11 = re.sub("H", "‌🇭", zhrf11)
    zhrf11 = re.sub("i", "‌🇮", zhrf11)
    zhrf11 = re.sub("I", "‌🇮", zhrf11)
    zhrf11 = re.sub("j", "‌🇯", zhrf11)
    zhrf11 = re.sub("J", "‌🇯", zhrf11)
    zhrf11 = re.sub("k", "‌🇰", zhrf11)
    zhrf11 = re.sub("K", "‌🇰", zhrf11)
    zhrf11 = re.sub("l", "‌🇱", zhrf11)
    zhrf11 = re.sub("L", "‌🇱", zhrf11)
    zhrf11 = re.sub("m", "‌🇲", zhrf11)
    zhrf11 = re.sub("M", "‌🇲", zhrf11)
    zhrf11 = re.sub("n", "‌🇳", zhrf11)
    zhrf11 = re.sub("N", "‌🇳", zhrf11)
    zhrf11 = re.sub("o", "‌🇴", zhrf11)
    zhrf11 = re.sub("O", "‌🇴", zhrf11)
    zhrf11 = re.sub("p", "‌🇵", zhrf11)
    zhrf11 = re.sub("P", "‌🇵", zhrf11)
    zhrf11 = re.sub("q", "‌🇶", zhrf11)
    zhrf11 = re.sub("Q", "‌🇶", zhrf11)
    zhrf11 = re.sub("r", "‌🇷", zhrf11)
    zhrf11 = re.sub("R", "‌🇷", zhrf11)
    zhrf11 = re.sub("s", "‌🇸", zhrf11)
    zhrf11 = re.sub("S", "‌🇸", zhrf11)
    zhrf11 = re.sub("t", "‌🇹", zhrf11)
    zhrf11 = re.sub("T", "‌🇹", zhrf11)
    zhrf11 = re.sub("u", "‌🇺", zhrf11)
    zhrf11 = re.sub("U", "‌🇺", zhrf11)
    zhrf11 = re.sub("v", "‌🇻", zhrf11)
    zhrf11 = re.sub("V", "‌🇻", zhrf11)
    zhrf11 = re.sub("w", "‌🇼", zhrf11)
    zhrf11 = re.sub("W", "‌🇼", zhrf11)
    zhrf11 = re.sub("x", "‌🇽", zhrf11)
    zhrf11 = re.sub("X", "‌🇽", zhrf11)
    zhrf11 = re.sub("y", "‌🇾", zhrf11)
    zhrf11 = re.sub("Y", "‌🇾", zhrf11)
    zhrf11 = re.sub("z", "‌🇿", zhrf11)
    zhrf11 = re.sub("Z", "‌🇿", zhrf11)
    
    zhrf12 = re.sub('ض', 'ضـ❣ـہ', text)
    zhrf12 = re.sub('ص', 'صـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ث', 'ثـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ق', 'قـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ف', 'فـ❣ـہ', zhrf12)
    zhrf12 = re.sub('غ', 'غـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ع', 'عـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ه', 'هـ❣ـہ', zhrf12)
    zhrf12 = re.sub('خ', 'خـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ح', 'حـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ج', 'جـ❣ـہ', zhrf12)
    zhrf12 = re.sub('د', 'د', zhrf12)
    zhrf12 = re.sub('ذ', 'ذ', zhrf12)
    zhrf12 = re.sub('ش', 'شـ❣ـہ', zhrf12)
    zhrf12 = re.sub('س', 'سـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ي', 'ي', zhrf12)
    zhrf12 = re.sub('ب', 'بـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ل', 'ل', zhrf12)
    zhrf12 = re.sub('ا', 'آ', zhrf12)
    zhrf12 = re.sub('ت', 'تـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ن', 'نـ❣ـہ', zhrf12)
    zhrf12 = re.sub('م', 'مـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ك', 'كـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ط', 'طـ❣ـہ', zhrf12)
    zhrf12 = re.sub('ئ', 'ئ', zhrf12)
    zhrf12 = re.sub('ء', 'ء', zhrf12)
    zhrf12 = re.sub('ؤ', 'ؤ', zhrf12)
    zhrf12 = re.sub('ر', 'ر', zhrf12)
    zhrf12 = re.sub('لا', 'لآ', zhrf12)
    zhrf12 = re.sub('ى', 'ى', zhrf12)
    zhrf12 = re.sub('ة', 'ةّ', zhrf12)
    zhrf12 = re.sub('و', 'وُ', zhrf12)
    zhrf12 = re.sub('ز', 'ز', zhrf12)
    zhrf12 = re.sub('ظ', 'ظـ❣ـہ', zhrf12)
    zhrf12 = re.sub('a', "Ã", zhrf12)
    zhrf12 = re.sub('A', "Ã", zhrf12)
    zhrf12 = re.sub("b", "β", zhrf12)
    zhrf12 = re.sub("B", "β", zhrf12)
    zhrf12 = re.sub("c", "Č", zhrf12)
    zhrf12 = re.sub("C", "Č", zhrf12)
    zhrf12 = re.sub("d", "Ď", zhrf12)
    zhrf12 = re.sub("D", "Ď", zhrf12)
    zhrf12 = re.sub("e", "Ẹ", zhrf12)
    zhrf12 = re.sub("E", "Ẹ", zhrf12)
    zhrf12 = re.sub("f", "Ƒ", zhrf12)
    zhrf12 = re.sub("F", "Ƒ", zhrf12)
    zhrf12 = re.sub("g", "Ğ", zhrf12)
    zhrf12 = re.sub("G", "Ğ", zhrf12)
    zhrf12 = re.sub("h", "Ĥ", zhrf12)
    zhrf12 = re.sub("H", "Ĥ", zhrf12)
    zhrf12 = re.sub("i", "Į", zhrf12)
    zhrf12 = re.sub("I", "Į", zhrf12)
    zhrf12 = re.sub("j", "Ĵ", zhrf12)
    zhrf12 = re.sub("J", "Ĵ", zhrf12)
    zhrf12 = re.sub("k", "Ќ", zhrf12)
    zhrf12 = re.sub("K", "Ќ", zhrf12)
    zhrf12 = re.sub("l", "Ĺ", zhrf12)
    zhrf12 = re.sub("L", "Ĺ", zhrf12)
    zhrf12 = re.sub("m", "ϻ", zhrf12)
    zhrf12 = re.sub("M", "ϻ", zhrf12)
    zhrf12 = re.sub("n", "Ň", zhrf12)
    zhrf12 = re.sub("N", "Ň", zhrf12)
    zhrf12 = re.sub("o", "Ỗ", zhrf12)
    zhrf12 = re.sub("O", "Ỗ", zhrf12)
    zhrf12 = re.sub("p", "Ƥ", zhrf12)
    zhrf12 = re.sub("P", "Ƥ", zhrf12)
    zhrf12 = re.sub("q", "Q", zhrf12)
    zhrf12 = re.sub("Q", "Q", zhrf12)
    zhrf12 = re.sub("r", "Ř", zhrf12)
    zhrf12 = re.sub("R", "Ř", zhrf12)
    zhrf12 = re.sub("s", "Ŝ", zhrf12)
    zhrf12 = re.sub("S", "Ŝ", zhrf12)
    zhrf12 = re.sub("t", "Ť", zhrf12)
    zhrf12 = re.sub("T", "Ť", zhrf12)
    zhrf12 = re.sub("u", "Ǘ", zhrf12)
    zhrf12 = re.sub("U", "Ǘ", zhrf12)
    zhrf12 = re.sub("v", "ϋ", zhrf12)
    zhrf12 = re.sub("V", "ϋ", zhrf12)
    zhrf12 = re.sub("w", "Ŵ", zhrf12)
    zhrf12 = re.sub("W", "Ŵ", zhrf12)
    zhrf12 = re.sub("x", "Ж", zhrf12)
    zhrf12 = re.sub("X", "Ж", zhrf12)
    zhrf12 = re.sub("y", "Ў", zhrf12)
    zhrf12 = re.sub("Y", "Ў", zhrf12)
    zhrf12 = re.sub("z", "Ż", zhrf12)
    zhrf12 = re.sub("Z", "Ż", zhrf12)

    zhrf13 = re.sub('ض', 'ضـ❤ـ', text)
    zhrf13 = re.sub('ص', 'صـ❤ـ', zhrf13)
    zhrf13 = re.sub('ث', 'ثـ❤ـ', zhrf13)
    zhrf13 = re.sub('ق', 'قـ❤ـ', zhrf13)
    zhrf13 = re.sub('ف', 'فـ❤ـ', zhrf13)
    zhrf13 = re.sub('غ', 'غـ❤ـ', zhrf13)
    zhrf13 = re.sub('ع', 'عـ❤ـ', zhrf13)
    zhrf13 = re.sub('ه', 'هّ', zhrf13)
    zhrf13 = re.sub('خ', 'خـ❤ـ', zhrf13)
    zhrf13 = re.sub('ح', 'حـ❤ـ', zhrf13)
    zhrf13 = re.sub('ج', 'جـ❤ـ', zhrf13)
    zhrf13 = re.sub('د', 'د', zhrf13)
    zhrf13 = re.sub('ذ', 'ذ', zhrf13)
    zhrf13 = re.sub('ش', 'شـ❤ـ', zhrf13)
    zhrf13 = re.sub('س', 'سـ❤ـ', zhrf13)
    zhrf13 = re.sub('ي', 'يـ❤ـ', zhrf13)
    zhrf13 = re.sub('ب', 'بـ❤ـ', zhrf13)
    zhrf13 = re.sub('ل', 'لَ', zhrf13)
    zhrf13 = re.sub('ا', 'آ', zhrf13)
    zhrf13 = re.sub('ت', 'تـ❤ـ', zhrf13)
    zhrf13 = re.sub('ن', 'نـ❤ـ', zhrf13)
    zhrf13 = re.sub('م', 'مـ❤ـ', zhrf13)
    zhrf13 = re.sub('ك', 'كـ❤ـ', zhrf13)
    zhrf13 = re.sub('ط', 'طـ❤ـ', zhrf13)
    zhrf13 = re.sub('ئ', 'ئ', zhrf13)
    zhrf13 = re.sub('ء', 'ء', zhrf13)
    zhrf13 = re.sub('ؤ', 'ؤ', zhrf13)
    zhrf13 = re.sub('ر', 'ر', zhrf13)
    zhrf13 = re.sub('لا', 'لَآ', zhrf13)
    zhrf13 = re.sub('ى', 'ى', zhrf13)
    zhrf13 = re.sub('ة', 'ةّ', zhrf13)
    zhrf13 = re.sub('و', 'وٌ', zhrf13)
    zhrf13 = re.sub('ز', 'زِّ', zhrf13)
    zhrf13 = re.sub('ظ', 'ظـ❤ـ', zhrf13)
    zhrf13 = re.sub('a', "❤a", zhrf13)
    zhrf13 = re.sub('A', "❤A", zhrf13)
    zhrf13 = re.sub("b", "❤b", zhrf13)
    zhrf13 = re.sub("B", "❤B", zhrf13)
    zhrf13 = re.sub("c", "❤c", zhrf13)
    zhrf13 = re.sub("C", "❤C", zhrf13)
    zhrf13 = re.sub("d", "❤d", zhrf13)
    zhrf13 = re.sub("D", "❤D", zhrf13)
    zhrf13 = re.sub("e", "❤e", zhrf13)
    zhrf13 = re.sub("E", "❤E", zhrf13)
    zhrf13 = re.sub("f", "❤f", zhrf13)
    zhrf13 = re.sub("F", "❤F", zhrf13)
    zhrf13 = re.sub("g", "❤g", zhrf13)
    zhrf13 = re.sub("G", "❤G", zhrf13)
    zhrf13 = re.sub("h", "❤h", zhrf13)
    zhrf13 = re.sub("H", "❤H", zhrf13)
    zhrf13 = re.sub("i", "❤i", zhrf13)
    zhrf13 = re.sub("I", "❤I", zhrf13)
    zhrf13 = re.sub("j", "❤j", zhrf13)
    zhrf13 = re.sub("J", "❤J", zhrf13)
    zhrf13 = re.sub("k", "❤k", zhrf13)
    zhrf13 = re.sub("K", "❤K", zhrf13)
    zhrf13 = re.sub("l", "❤l", zhrf13)
    zhrf13 = re.sub("L", "❤L", zhrf13)
    zhrf13 = re.sub("m", "❤m", zhrf13)
    zhrf13 = re.sub("M", "❤M", zhrf13)
    zhrf13 = re.sub("n", "❤n", zhrf13)
    zhrf13 = re.sub("N", "❤N", zhrf13)
    zhrf13 = re.sub("o", "❤o", zhrf13)
    zhrf13 = re.sub("O", "❤O", zhrf13)
    zhrf13 = re.sub("p", "❤p", zhrf13)
    zhrf13 = re.sub("P", "❤P", zhrf13)
    zhrf13 = re.sub("q", "❤q", zhrf13)
    zhrf13 = re.sub("Q", "❤Q", zhrf13)
    zhrf13 = re.sub("r", "❤r", zhrf13)
    zhrf13 = re.sub("R", "❤R", zhrf13)
    zhrf13 = re.sub("s", "❤s", zhrf13)
    zhrf13 = re.sub("S", "❤S", zhrf13)
    zhrf13 = re.sub("t", "❤t", zhrf13)
    zhrf13 = re.sub("T", "❤T", zhrf13)
    zhrf13 = re.sub("u", "❤u", zhrf13)
    zhrf13 = re.sub("U", "❤U", zhrf13)
    zhrf13 = re.sub("v", "❤v", zhrf13)
    zhrf13 = re.sub("V", "❤V", zhrf13)
    zhrf13 = re.sub("w", "❤w", zhrf13)
    zhrf13 = re.sub("W", "❤W", zhrf13)
    zhrf13 = re.sub("x", "❤x", zhrf13)
    zhrf13 = re.sub("X", "❤X", zhrf13)
    zhrf13 = re.sub("y", "❤y", zhrf13)
    zhrf13 = re.sub("Y", "❤Y", zhrf13)
    zhrf13 = re.sub("z", "❤z", zhrf13)
    zhrf13 = re.sub("Z", "❤Z", zhrf13)

    zhrf14 = re.sub('ض', 'ضـ༈ۖ҉ـ', text)
    zhrf14 = re.sub('ص', 'صـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ث', 'ثـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ق', 'قـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ف', 'فـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('غ', 'غـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ع', 'عـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ه', 'هـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('خ', 'خـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ح', 'حـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ج', 'جـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('د', 'د', zhrf14)
    zhrf14 = re.sub('ذ', 'ذ', zhrf14)
    zhrf14 = re.sub('ش', 'شـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('س', 'سـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ي', 'يـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ب', 'بـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ل', 'لَ', zhrf14)
    zhrf14 = re.sub('ا', 'آ', zhrf14)
    zhrf14 = re.sub('ت', 'تـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ن', 'نـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('م', 'مـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ك', 'كـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('ط', 'ط', zhrf14)
    zhrf14 = re.sub('ئ', 'ئ', zhrf14)
    zhrf14 = re.sub('ء', 'ء', zhrf14)
    zhrf14 = re.sub('ؤ', 'ؤ', zhrf14)
    zhrf14 = re.sub('ر', 'ر', zhrf14)
    zhrf14 = re.sub('لا', 'لَآ', zhrf14)
    zhrf14 = re.sub('ى', 'ى', zhrf14)
    zhrf14 = re.sub('ة', 'ة', zhrf14)
    zhrf14 = re.sub('و', 'ؤُ', zhrf14)
    zhrf14 = re.sub('ز', 'ز', zhrf14)
    zhrf14 = re.sub('ظ', 'ظـ༈ۖ҉ـ', zhrf14)
    zhrf14 = re.sub('a', "α", zhrf14)
    zhrf14 = re.sub('A', "Α", zhrf14)
    zhrf14 = re.sub("b", "в", zhrf14)
    zhrf14 = re.sub("B", "В", zhrf14)
    zhrf14 = re.sub("c", "c", zhrf14)
    zhrf14 = re.sub("C", "C", zhrf14)
    zhrf14 = re.sub("d", "ɒ", zhrf14)
    zhrf14 = re.sub("D", "Ɒ", zhrf14)
    zhrf14 = re.sub("e", "є", zhrf14)
    zhrf14 = re.sub("E", "Є", zhrf14)
    zhrf14 = re.sub("f", "f", zhrf14)
    zhrf14 = re.sub("F", "F", zhrf14)
    zhrf14 = re.sub("g", "ɢ", zhrf14)
    zhrf14 = re.sub("G", "ɢ", zhrf14)
    zhrf14 = re.sub("h", "н", zhrf14)
    zhrf14 = re.sub("H", "Н", zhrf14)
    zhrf14 = re.sub("i", "i", zhrf14)
    zhrf14 = re.sub("I", "I", zhrf14)
    zhrf14 = re.sub("j", "j", zhrf14)
    zhrf14 = re.sub("J", "J", zhrf14)
    zhrf14 = re.sub("k", "ĸ", zhrf14)
    zhrf14 = re.sub("K", "ĸ", zhrf14)
    zhrf14 = re.sub("l", "ℓ", zhrf14)
    zhrf14 = re.sub("L", "ℓ", zhrf14)
    zhrf14 = re.sub("m", "м", zhrf14)
    zhrf14 = re.sub("M", "М", zhrf14)
    zhrf14 = re.sub("n", "и", zhrf14)
    zhrf14 = re.sub("N", "И", zhrf14)
    zhrf14 = re.sub("o", "σ", zhrf14)
    zhrf14 = re.sub("O", "Σ", zhrf14)
    zhrf14 = re.sub("p", "ρ", zhrf14)
    zhrf14 = re.sub("P", "Ρ", zhrf14)
    zhrf14 = re.sub("q", "q", zhrf14)
    zhrf14 = re.sub("Q", "Q", zhrf14)
    zhrf14 = re.sub("r", "я", zhrf14)
    zhrf14 = re.sub("R", "Я", zhrf14)
    zhrf14 = re.sub("s", "s", zhrf14)
    zhrf14 = re.sub("S", "S", zhrf14)
    zhrf14 = re.sub("t", "τ", zhrf14)
    zhrf14 = re.sub("T", "Τ", zhrf14)
    zhrf14 = re.sub("u", "υ", zhrf14)
    zhrf14 = re.sub("U", "Υ", zhrf14)
    zhrf14 = re.sub("v", "v", zhrf14)
    zhrf14 = re.sub("V", "V", zhrf14)
    zhrf14 = re.sub("w", "ω", zhrf14)
    zhrf14 = re.sub("W", "Ω", zhrf14)
    zhrf14 = re.sub("x", "x", zhrf14)
    zhrf14 = re.sub("X", "X", zhrf14)
    zhrf14 = re.sub("y", "y", zhrf14)
    zhrf14 = re.sub("Y", "Y", zhrf14)
    zhrf14 = re.sub("z", "z", zhrf14)
    zhrf14 = re.sub("Z", "Z", zhrf14)
    
    zhrf15 = re.sub('ض', 'ض', text)
    zhrf15 = re.sub('ص', 'صُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ث', 'ُثُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ق', 'قُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ف', 'فُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('غ', 'غُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ع', 'عُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ه', 'هـُ‘ـُ', zhrf15)
    zhrf15 = re.sub('خ', 'خُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ح', 'حُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ج', 'جُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('د', 'ډ', zhrf15)
    zhrf15 = re.sub('ذ', 'ڏ', zhrf15)
    zhrf15 = re.sub('ش', 'شُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('س', 'سُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ي', 'يُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ب', 'بُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ل', 'لُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ا', 'ٱ', zhrf15)
    zhrf15 = re.sub('ت', 'تُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ن', 'نُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('م', 'مُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ك', 'كُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ط', 'طُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('ئ', 'ئ', zhrf15)
    zhrf15 = re.sub('ء', 'ء', zhrf15)
    zhrf15 = re.sub('ؤ', 'ؤ', zhrf15)
    zhrf15 = re.sub('ر', 'ر', zhrf15)
    zhrf15 = re.sub('لا', 'لُـ‘ـُٱ', zhrf15)
    zhrf15 = re.sub('ى', 'ﮯ', zhrf15)
    zhrf15 = re.sub('ة', 'ةّ', zhrf15)
    zhrf15 = re.sub('و', 'وٌ', zhrf15)
    zhrf15 = re.sub('ز', 'زٍ', zhrf15)
    zhrf15 = re.sub('ظ', 'ظُـ‘ـُ', zhrf15)
    zhrf15 = re.sub('a', "ค", zhrf15)
    zhrf15 = re.sub('A', "ค", zhrf15)
    zhrf15 = re.sub("b", "๒", zhrf15)
    zhrf15 = re.sub("B", "๒", zhrf15)
    zhrf15 = re.sub("c", "ς", zhrf15)
    zhrf15 = re.sub("C", "Σ", zhrf15)
    zhrf15 = re.sub("d", "๔", zhrf15)
    zhrf15 = re.sub("D", "๔", zhrf15)
    zhrf15 = re.sub("e", "є", zhrf15)
    zhrf15 = re.sub("E", "Є", zhrf15)
    zhrf15 = re.sub("f", "Ŧ", zhrf15)
    zhrf15 = re.sub("F", "Ŧ", zhrf15)
    zhrf15 = re.sub("g", "ƃ", zhrf15)
    zhrf15 = re.sub("G", "Ƃ", zhrf15)
    zhrf15 = re.sub("h", "ђ", zhrf15)
    zhrf15 = re.sub("H", "Ђ", zhrf15)
    zhrf15 = re.sub("i", "เ", zhrf15)
    zhrf15 = re.sub("I", "เ", zhrf15)
    zhrf15 = re.sub("j", "ן", zhrf15)
    zhrf15 = re.sub("J", "ן", zhrf15)
    zhrf15 = re.sub("k", "к", zhrf15)
    zhrf15 = re.sub("K", "К", zhrf15)
    zhrf15 = re.sub("l", "l", zhrf15)
    zhrf15 = re.sub("L", "L", zhrf15)
    zhrf15 = re.sub("m", "๓", zhrf15)
    zhrf15 = re.sub("M", "๓", zhrf15)
    zhrf15 = re.sub("n", "ภ", zhrf15)
    zhrf15 = re.sub("N", "ภ", zhrf15)
    zhrf15 = re.sub("o", "๏", zhrf15)
    zhrf15 = re.sub("O", "๏", zhrf15)
    zhrf15 = re.sub("p", "ρ", zhrf15)
    zhrf15 = re.sub("P", "Ρ", zhrf15)
    zhrf15 = re.sub("q", "ც", zhrf15)
    zhrf15 = re.sub("Q", "Ც", zhrf15)
    zhrf15 = re.sub("r", "г", zhrf15)
    zhrf15 = re.sub("R", "Г", zhrf15)
    zhrf15 = re.sub("s", "ร", zhrf15)
    zhrf15 = re.sub("S", "ร", zhrf15)
    zhrf15 = re.sub("t", "t", zhrf15)
    zhrf15 = re.sub("T", "T", zhrf15)
    zhrf15 = re.sub("u", "ย", zhrf15)
    zhrf15 = re.sub("U", "ย", zhrf15)
    zhrf15 = re.sub("v", "ʌ", zhrf15)
    zhrf15 = re.sub("V", "Ʌ", zhrf15)
    zhrf15 = re.sub("w", "ฬ", zhrf15)
    zhrf15 = re.sub("W", "ฬ", zhrf15)
    zhrf15 = re.sub("x", "א", zhrf15)
    zhrf15 = re.sub("X", "א", zhrf15)
    zhrf15 = re.sub("y", "ץ", zhrf15)
    zhrf15 = re.sub("Y", "ץ", zhrf15)
    zhrf15 = re.sub("z", "z", zhrf15)
    zhrf15 = re.sub("Z", "Z", zhrf15)

    zhrf16 = re.sub('ض', 'ض', text)
    zhrf16 = re.sub('ص', 'صُـ,ـ', zhrf16)
    zhrf16 = re.sub('ث', 'ثُ', zhrf16)
    zhrf16 = re.sub('ق', 'قٌـ,ـ', zhrf16)
    zhrf16 = re.sub('ف', 'فُـ,ـ', zhrf16)
    zhrf16 = re.sub('غ', 'غٍـُـُُـُُُـُُُُـُُُـُُـُ', zhrf16)
    zhrf16 = re.sub('ع', 'عٌـِـِِـِـ', zhrf16)
    zhrf16 = re.sub('ه', 'ﮩ', zhrf16)
    zhrf16 = re.sub('خ', 'ځـٌٌـٌٌ', zhrf16)
    zhrf16 = re.sub('ح', 'حـًـًًـًًًـًًـًـ', zhrf16)
    zhrf16 = re.sub('ج', 'جـ,ـ', zhrf16)
    zhrf16 = re.sub('د', 'ڊ', zhrf16)
    zhrf16 = re.sub('ذ', 'ڏ', zhrf16)
    zhrf16 = re.sub('ش', 'شُـُـُُـُ', zhrf16)
    zhrf16 = re.sub('س', 'ڛـ,ـ', zhrf16)
    zhrf16 = re.sub('ي', 'ي', zhrf16)
    zhrf16 = re.sub('ب', 'بـٌـٌٌـٌٌٌـٌٌـٌ', zhrf16)
    zhrf16 = re.sub('ل', 'لُـِـِِـِِِـِِـِـ', zhrf16)
    zhrf16 = re.sub('ا', 'آ', zhrf16)
    zhrf16 = re.sub('ت', 'تـٌـٌٌـ', zhrf16)
    zhrf16 = re.sub('ن', 'نـِِـِـ', zhrf16)
    zhrf16 = re.sub('م', 'مـْـْْـْ', zhrf16)
    zhrf16 = re.sub('ك', 'كُـُ', zhrf16)
    zhrf16 = re.sub('ط', 'طُـٌـٌٌـٌ', zhrf16)
    zhrf16 = re.sub('ئ', 'ئ', zhrf16)
    zhrf16 = re.sub('ء', 'ء', zhrf16)
    zhrf16 = re.sub('ؤ', 'ؤ', zhrf16)
    zhrf16 = re.sub('ر', 'ر', zhrf16)
    zhrf16 = re.sub('لا', 'لُـِـِِـِِِـِِـِـآ', zhrf16)
    zhrf16 = re.sub('ى', 'ﮯ', zhrf16)
    zhrf16 = re.sub('ة', 'ة', zhrf16)
    zhrf16 = re.sub('و', 'وُ', zhrf16)
    zhrf16 = re.sub('ز', 'ڒٍ', zhrf16)
    zhrf16 = re.sub('ظ', 'ظً', zhrf16)
    zhrf16 = re.sub('a', "α", zhrf16)
    zhrf16 = re.sub('A', "Α", zhrf16)
    zhrf16 = re.sub("b", "Ⴆ", zhrf16)
    zhrf16 = re.sub("B", "Ⴆ", zhrf16)
    zhrf16 = re.sub("c", "ƈ", zhrf16)
    zhrf16 = re.sub("C", "Ƈ", zhrf16)
    zhrf16 = re.sub("d", "ԃ", zhrf16)
    zhrf16 = re.sub("D", "Ԃ", zhrf16)
    zhrf16 = re.sub("e", "ҽ", zhrf16)
    zhrf16 = re.sub("E", "Ҽ", zhrf16)
    zhrf16 = re.sub("f", "ϝ", zhrf16)
    zhrf16 = re.sub("F", "Ϝ", zhrf16)
    zhrf16 = re.sub("g", "ɠ", zhrf16)
    zhrf16 = re.sub("G", "Ɠ", zhrf16)
    zhrf16 = re.sub("h", "ԋ", zhrf16)
    zhrf16 = re.sub("H", "Ԋ", zhrf16)
    zhrf16 = re.sub("i", "ι", zhrf16)
    zhrf16 = re.sub("I", "Ι", zhrf16)
    zhrf16 = re.sub("j", "ʝ", zhrf16)
    zhrf16 = re.sub("J", "Ʝ", zhrf16)
    zhrf16 = re.sub("k", "ƙ", zhrf16)
    zhrf16 = re.sub("K", "Ƙ", zhrf16)
    zhrf16 = re.sub("l", "ʅ", zhrf16)
    zhrf16 = re.sub("L", "ʅ", zhrf16)
    zhrf16 = re.sub("m", "ɱ", zhrf16)
    zhrf16 = re.sub("M", "Ɱ", zhrf16)
    zhrf16 = re.sub("n", "ɳ", zhrf16)
    zhrf16 = re.sub("N", "ɳ", zhrf16)
    zhrf16 = re.sub("o", "σ", zhrf16)
    zhrf16 = re.sub("O", "Σ", zhrf16)
    zhrf16 = re.sub("p", "ρ", zhrf16)
    zhrf16 = re.sub("P", "Ρ", zhrf16)
    zhrf16 = re.sub("q", "ϙ", zhrf16)
    zhrf16 = re.sub("Q", "Ϙ", zhrf16)
    zhrf16 = re.sub("r", "ɾ", zhrf16)
    zhrf16 = re.sub("R", "ɾ", zhrf16)
    zhrf16 = re.sub("s", "ʂ", zhrf16)
    zhrf16 = re.sub("S", "ʂ", zhrf16)
    zhrf16 = re.sub("t", "ƚ", zhrf16)
    zhrf16 = re.sub("T", "Ƚ", zhrf16)
    zhrf16 = re.sub("u", "υ", zhrf16)
    zhrf16 = re.sub("U", "Υ", zhrf16)
    zhrf16 = re.sub("v", "ʋ", zhrf16)
    zhrf16 = re.sub("V", "Ʋ", zhrf16)
    zhrf16 = re.sub("w", "ɯ", zhrf16)
    zhrf16 = re.sub("W", "Ɯ", zhrf16)
    zhrf16 = re.sub("x", "x", zhrf16)
    zhrf16 = re.sub("X", "X", zhrf16)
    zhrf16 = re.sub("y", "ყ", zhrf16)
    zhrf16 = re.sub("Y", "Ყ", zhrf16)
    zhrf16 = re.sub("z", "ȥ", zhrf16)
    zhrf16 = re.sub("Z", "Ȥ", zhrf16)
    
    zhrf17 = re.sub('ض', 'ضےـ', text)
    zhrf17 = re.sub('ص', 'صےـ', zhrf17)
    zhrf17 = re.sub('ث', 'ثےـ', zhrf17)
    zhrf17 = re.sub('ق', 'قےـ', zhrf17)
    zhrf17 = re.sub('ف', 'فےـ', zhrf17)
    zhrf17 = re.sub('غ', 'غےـ', zhrf17)
    zhrf17 = re.sub('ع', 'عےـ', zhrf17)
    zhrf17 = re.sub('ه', 'هےـِ', zhrf17)
    zhrf17 = re.sub('خ', 'خےـ', zhrf17)
    zhrf17 = re.sub('ح', 'حےـ', zhrf17)
    zhrf17 = re.sub('ج', 'جےـ', zhrf17)
    zhrf17 = re.sub('د', 'د', zhrf17)
    zhrf17 = re.sub('ذ', 'ذ', zhrf17)
    zhrf17 = re.sub('ش', 'شےـ', zhrf17)
    zhrf17 = re.sub('س', 'سےـ', zhrf17)
    zhrf17 = re.sub('ي', 'يےـ', zhrf17)
    zhrf17 = re.sub('ب', 'بےـ', zhrf17)
    zhrf17 = re.sub('ل', 'ل', zhrf17)
    zhrf17 = re.sub('ا', 'آ', zhrf17)
    zhrf17 = re.sub('ت', 'تےـ', zhrf17)
    zhrf17 = re.sub('ن', 'نےـ', zhrf17)
    zhrf17 = re.sub('م', 'مےـ', zhrf17)
    zhrf17 = re.sub('ك', 'كےـ', zhrf17)
    zhrf17 = re.sub('ط', 'طےـ', zhrf17)
    zhrf17 = re.sub('ئ', 'ئ', zhrf17)
    zhrf17 = re.sub('ء', 'ء', zhrf17)
    zhrf17 = re.sub('ؤ', 'ؤ', zhrf17)
    zhrf17 = re.sub('ر', 'ر', zhrf17)
    zhrf17 = re.sub('لا', 'لآ', zhrf17)
    zhrf17 = re.sub('ى', 'ى', zhrf17)
    zhrf17 = re.sub('ة', 'ة', zhrf17)
    zhrf17 = re.sub('و', 'و', zhrf17)
    zhrf17 = re.sub('ز', 'ز', zhrf17)
    zhrf17 = re.sub('ظ', 'ظےـ', zhrf17)
    zhrf17 = re.sub('a', "🄰", zhrf17)
    zhrf17 = re.sub('A', "🄰", zhrf17)
    zhrf17 = re.sub("b", "🄱", zhrf17)
    zhrf17 = re.sub("B", "🄱", zhrf17)
    zhrf17 = re.sub("c", "🄲", zhrf17)
    zhrf17 = re.sub("C", "🄲", zhrf17)
    zhrf17 = re.sub("d", "🄳", zhrf17)
    zhrf17 = re.sub("D", "🄳", zhrf17)
    zhrf17 = re.sub("e", "🄴", zhrf17)
    zhrf17 = re.sub("E", "🄴", zhrf17)
    zhrf17 = re.sub("f", "🄵", zhrf17)
    zhrf17 = re.sub("F", "🄵", zhrf17)
    zhrf17 = re.sub("g", "🄶", zhrf17)
    zhrf17 = re.sub("G", "🄶", zhrf17)
    zhrf17 = re.sub("h", "🄷", zhrf17)
    zhrf17 = re.sub("H", "🄷", zhrf17)
    zhrf17 = re.sub("i", "🄸", zhrf17)
    zhrf17 = re.sub("I", "🄸", zhrf17)
    zhrf17 = re.sub("j", "🄹", zhrf17)
    zhrf17 = re.sub("J", "🄹", zhrf17)
    zhrf17 = re.sub("k", "🄺", zhrf17)
    zhrf17 = re.sub("K", "🄺", zhrf17)
    zhrf17 = re.sub("l", "🄻", zhrf17)
    zhrf17 = re.sub("L", "🄻", zhrf17)
    zhrf17 = re.sub("m", "🄼", zhrf17)
    zhrf17 = re.sub("M", "🄼", zhrf17)
    zhrf17 = re.sub("n", "🄽", zhrf17)
    zhrf17 = re.sub("N", "🄽", zhrf17)
    zhrf17 = re.sub("o", "🄾", zhrf17)
    zhrf17 = re.sub("O", "🄾", zhrf17)
    zhrf17 = re.sub("p", "🄿", zhrf17)
    zhrf17 = re.sub("P", "🄿", zhrf17)
    zhrf17 = re.sub("q", "🅀", zhrf17)
    zhrf17 = re.sub("Q", "🅀", zhrf17)
    zhrf17 = re.sub("r", "🅁", zhrf17)
    zhrf17 = re.sub("R", "🅁", zhrf17)
    zhrf17 = re.sub("s", "🅂", zhrf17)
    zhrf17 = re.sub("S", "🅂", zhrf17)
    zhrf17 = re.sub("t", "🅃", zhrf17)
    zhrf17 = re.sub("T", "🅃", zhrf17)
    zhrf17 = re.sub("u", "🅄", zhrf17)
    zhrf17 = re.sub("U", "🅄", zhrf17)
    zhrf17 = re.sub("v", "🅅", zhrf17)
    zhrf17 = re.sub("V", "🅅", zhrf17)
    zhrf17 = re.sub("w", "🅆", zhrf17)
    zhrf17 = re.sub("W", "🅆", zhrf17)
    zhrf17 = re.sub("x", "🅇", zhrf17)
    zhrf17 = re.sub("X", "🅇", zhrf17)
    zhrf17 = re.sub("y", "🅈", zhrf17)
    zhrf17 = re.sub("Y", "🅈", zhrf17)
    zhrf17 = re.sub("z", "🅉", zhrf17)
    zhrf17 = re.sub("Z", "🅉", zhrf17)
    
    zhrf18 = re.sub('ض', 'ضـ░ـ', text)
    zhrf18 = re.sub('ص', 'صـ░ـ', zhrf18)
    zhrf18 = re.sub('ث', 'ثـ░ـ', zhrf18)
    zhrf18 = re.sub('ق', 'قـ░ـ', zhrf18)
    zhrf18 = re.sub('ف', 'فـ░ـ', zhrf18)
    zhrf18 = re.sub('غ', 'غـ░ـ', zhrf18)
    zhrf18 = re.sub('ع', 'عـ░ـ', zhrf18)
    zhrf18 = re.sub('ه', 'هّ', zhrf18)
    zhrf18 = re.sub('خ', 'خـ░ـ', zhrf18)
    zhrf18 = re.sub('ح', 'حـ░ـ', zhrf18)
    zhrf18 = re.sub('ج', 'جـ░ـ', zhrf18)
    zhrf18 = re.sub('د', 'دٍ', zhrf18)
    zhrf18 = re.sub('ذ', 'ذِ', zhrf18)
    zhrf18 = re.sub('ش', 'شـ░ـ', zhrf18)
    zhrf18 = re.sub('س', 'سـ░ـ', zhrf18)
    zhrf18 = re.sub('ي', 'يـ░ـ', zhrf18)
    zhrf18 = re.sub('ب', 'بـ░ـ', zhrf18)
    zhrf18 = re.sub('ل', 'لَ', zhrf18)
    zhrf18 = re.sub('ا', 'آ', zhrf18)
    zhrf18 = re.sub('ت', 'تـ░ـ', zhrf18)
    zhrf18 = re.sub('ن', 'نـ░ـ', zhrf18)
    zhrf18 = re.sub('م', 'مـ░ـ', zhrf18)
    zhrf18 = re.sub('ك', 'كـ░ـ', zhrf18)
    zhrf18 = re.sub('ط', 'طـ░ـ', zhrf18)
    zhrf18 = re.sub('ئ', 'ﮯء', zhrf18)
    zhrf18 = re.sub('ء', 'ء', zhrf18)
    zhrf18 = re.sub('ؤ', 'ؤ', zhrf18)
    zhrf18 = re.sub('ر', 'رٍ', zhrf18)
    zhrf18 = re.sub('لا', 'لَآ', zhrf18)
    zhrf18 = re.sub('ى', 'ﮯ', zhrf18)
    zhrf18 = re.sub('ة', 'ةّ', zhrf18)
    zhrf18 = re.sub('و', 'وٌ', zhrf18)
    zhrf18 = re.sub('ز', 'زٍ', zhrf18)
    zhrf18 = re.sub('ظ', 'ظـ░ـ', zhrf18)
    zhrf18 = re.sub('a', "ḁ", zhrf18)
    zhrf18 = re.sub('A', "Ḁ", zhrf18)
    zhrf18 = re.sub("b", "ḅ", zhrf18)
    zhrf18 = re.sub("B", "Ḅ", zhrf18)
    zhrf18 = re.sub("c", "ḉ", zhrf18)
    zhrf18 = re.sub("C", "Ḉ", zhrf18)
    zhrf18 = re.sub("d", "ḍ", zhrf18)
    zhrf18 = re.sub("D", "Ḍ", zhrf18)
    zhrf18 = re.sub("e", "ḙ", zhrf18)
    zhrf18 = re.sub("E", "Ḙ", zhrf18)
    zhrf18 = re.sub("f", "ḟ", zhrf18)
    zhrf18 = re.sub("F", "Ḟ", zhrf18)
    zhrf18 = re.sub("g", "ḡ", zhrf18)
    zhrf18 = re.sub("G", "Ḡ", zhrf18)
    zhrf18 = re.sub("h", "ḣ", zhrf18)
    zhrf18 = re.sub("H", "Ḣ", zhrf18)
    zhrf18 = re.sub("i", "ḭ", zhrf18)
    zhrf18 = re.sub("I", "Ḭ", zhrf18)
    zhrf18 = re.sub("j", "ɉ", zhrf18)
    zhrf18 = re.sub("J", "Ɉ", zhrf18)
    zhrf18 = re.sub("k", "ḱ", zhrf18)
    zhrf18 = re.sub("K", "Ḱ", zhrf18)
    zhrf18 = re.sub("l", "ḷ", zhrf18)
    zhrf18 = re.sub("L", "Ḷ", zhrf18)
    zhrf18 = re.sub("m", "ḿ", zhrf18)
    zhrf18 = re.sub("M", "Ḿ", zhrf18)
    zhrf18 = re.sub("n", "ṅ", zhrf18)
    zhrf18 = re.sub("N", "Ṅ", zhrf18)
    zhrf18 = re.sub("o", "ṍ", zhrf18)
    zhrf18 = re.sub("O", "Ṍ", zhrf18)
    zhrf18 = re.sub("p", "ṕ", zhrf18)
    zhrf18 = re.sub("P", "Ṕ", zhrf18)
    zhrf18 = re.sub("q", "ҩ", zhrf18)
    zhrf18 = re.sub("Q", "Ҩ", zhrf18)
    zhrf18 = re.sub("r", "ṙ", zhrf18)
    zhrf18 = re.sub("R", "Ṙ", zhrf18)
    zhrf18 = re.sub("s", "ṡ", zhrf18)
    zhrf18 = re.sub("S", "Ṡ", zhrf18)
    zhrf18 = re.sub("t", "ṫ", zhrf18)
    zhrf18 = re.sub("T", "Ṫ", zhrf18)
    zhrf18 = re.sub("u", "ṳ", zhrf18)
    zhrf18 = re.sub("U", "Ṳ", zhrf18)
    zhrf18 = re.sub("v", "ṽ", zhrf18)
    zhrf18 = re.sub("V", "Ṽ", zhrf18)
    zhrf18 = re.sub("w", "ẁ", zhrf18)
    zhrf18 = re.sub("W", "Ẁ", zhrf18)
    zhrf18 = re.sub("x", "ẋ", zhrf18)
    zhrf18 = re.sub("X", "Ẋ", zhrf18)
    zhrf18 = re.sub("y", "ẏ", zhrf18)
    zhrf18 = re.sub("Y", "Ẏ", zhrf18)
    zhrf18 = re.sub("z", "ẑ", zhrf18)
    zhrf18 = re.sub("Z", "Ẑ", zhrf18)
    
    zhrf19 = re.sub('ض', 'ض', text)
    zhrf19 = re.sub('ص', 'ص̷', zhrf19)
    zhrf19 = re.sub('ث', 'ث̷', zhrf19)
    zhrf19 = re.sub('ق', 'ق̷', zhrf19)
    zhrf19 = re.sub('ف', 'ف̷َ', zhrf19)
    zhrf19 = re.sub('غ', 'غ̷', zhrf19)
    zhrf19 = re.sub('ع', 'ع̷ٍ', zhrf19)
    zhrf19 = re.sub('ه', 'ہ̷', zhrf19)
    zhrf19 = re.sub('خ', 'خ̷', zhrf19)
    zhrf19 = re.sub('ح', 'ح̷', zhrf19)
    zhrf19 = re.sub('ج', 'ج̷', zhrf19)
    zhrf19 = re.sub('د', 'د̷ِ', zhrf19)
    zhrf19 = re.sub('ذ', 'ذ̷', zhrf19)
    zhrf19 = re.sub('ش', 'ش̷ُ', zhrf19)
    zhrf19 = re.sub('س', 'س̷', zhrf19)
    zhrf19 = re.sub('ي', 'ي̷', zhrf19)
    zhrf19 = re.sub('ب', 'ب̷', zhrf19)
    zhrf19 = re.sub('ل', 'ل̷', zhrf19)
    zhrf19 = re.sub('ا', 'ٵ̷', zhrf19)
    zhrf19 = re.sub('ت', 'ت̷', zhrf19)
    zhrf19 = re.sub('ن', 'ن̷', zhrf19)
    zhrf19 = re.sub('م', 'م̷', zhrf19)
    zhrf19 = re.sub('ك', 'گ̷', zhrf19)
    zhrf19 = re.sub('ط', 'ط̷ُ', zhrf19)
    zhrf19 = re.sub('ئ', 'ﮯ̷ء', zhrf19)
    zhrf19 = re.sub('ء', 'ء', zhrf19)
    zhrf19 = re.sub('ؤ', 'ؤ', zhrf19)
    zhrf19 = re.sub('ر', 'ر̷', zhrf19)
    zhrf19 = re.sub('لا', 'ل̷ٵ̷ ', zhrf19)
    zhrf19 = re.sub('ى', 'ﮯ̷', zhrf19)
    zhrf19 = re.sub('ة', 'ة', zhrf19)
    zhrf19 = re.sub('و', 'ۆ̷', zhrf19)
    zhrf19 = re.sub('ز', 'ز̷', zhrf19)
    zhrf19 = re.sub('ظ', 'ظ̷ً', zhrf19)
    zhrf19 = re.sub('a', "ﾑ", zhrf19)
    zhrf19 = re.sub('A', "ﾑ", zhrf19)
    zhrf19 = re.sub("b", "乃", zhrf19)
    zhrf19 = re.sub("B", "乃", zhrf19)
    zhrf19 = re.sub("c", "c", zhrf19)
    zhrf19 = re.sub("C", "C", zhrf19)
    zhrf19 = re.sub("d", "d", zhrf19)
    zhrf19 = re.sub("D", "D", zhrf19)
    zhrf19 = re.sub("e", "乇", zhrf19)
    zhrf19 = re.sub("E", "乇", zhrf19)
    zhrf19 = re.sub("f", "ｷ", zhrf19)
    zhrf19 = re.sub("F", "ｷ", zhrf19)
    zhrf19 = re.sub("g", "g", zhrf19)
    zhrf19 = re.sub("G", "G", zhrf19)
    zhrf19 = re.sub("h", "ん", zhrf19)
    zhrf19 = re.sub("H", "ん", zhrf19)
    zhrf19 = re.sub("i", "ﾉ", zhrf19)
    zhrf19 = re.sub("I", "ﾉ", zhrf19)
    zhrf19 = re.sub("j", "ﾌ", zhrf19)
    zhrf19 = re.sub("J", "ﾌ", zhrf19)
    zhrf19 = re.sub("k", "ズ", zhrf19)
    zhrf19 = re.sub("K", "ズ", zhrf19)
    zhrf19 = re.sub("l", "ﾚ", zhrf19)
    zhrf19 = re.sub("L", "ﾚ", zhrf19)
    zhrf19 = re.sub("m", "ﾶ", zhrf19)
    zhrf19 = re.sub("M", "ﾶ", zhrf19)
    zhrf19 = re.sub("n", "刀", zhrf19)
    zhrf19 = re.sub("N", "刀", zhrf19)
    zhrf19 = re.sub("o", "o", zhrf19)
    zhrf19 = re.sub("O", "O", zhrf19)
    zhrf19 = re.sub("p", "ｱ", zhrf19)
    zhrf19 = re.sub("P", "ｱ", zhrf19)
    zhrf19 = re.sub("q", "q", zhrf19)
    zhrf19 = re.sub("Q", "Q", zhrf19)
    zhrf19 = re.sub("r", "尺", zhrf19)
    zhrf19 = re.sub("R", "尺", zhrf19)
    zhrf19 = re.sub("s", "丂", zhrf19)
    zhrf19 = re.sub("S", "丂", zhrf19)
    zhrf19 = re.sub("t", "ｲ", zhrf19)
    zhrf19 = re.sub("T", "ｲ", zhrf19)
    zhrf19 = re.sub("u", "u", zhrf19)
    zhrf19 = re.sub("U", "U", zhrf19)
    zhrf19 = re.sub("v", "√", zhrf19)
    zhrf19 = re.sub("V", "√", zhrf19)
    zhrf19 = re.sub("w", "w", zhrf19)
    zhrf19 = re.sub("W", "W", zhrf19)
    zhrf19 = re.sub("x", "ﾒ", zhrf19)
    zhrf19 = re.sub("X", "ﾒ", zhrf19)
    zhrf19 = re.sub("y", "ﾘ", zhrf19)
    zhrf19 = re.sub("Y", "ﾘ", zhrf19)
    zhrf19 = re.sub("z", "乙", zhrf19)
    zhrf19 = re.sub("Z", "乙", zhrf19)
    
    zhrf20 = re.sub('ض', 'ض', text)
    zhrf20 = re.sub('ص', 'ص̯͡', zhrf20)
    zhrf20 = re.sub('ث', 'ث̯͡', zhrf20)
    zhrf20 = re.sub('ق', 'ق̯͡', zhrf20)
    zhrf20 = re.sub('ف', 'ف̯͡', zhrf20)
    zhrf20 = re.sub('غ', 'غ̯͡', zhrf20)
    zhrf20 = re.sub('ع', 'ع̯͡', zhrf20)
    zhrf20 = re.sub('ه', 'ہ̯͡', zhrf20)
    zhrf20 = re.sub('خ', 'خ̯͡', zhrf20)
    zhrf20 = re.sub('ح', 'ح̯͡', zhrf20)
    zhrf20 = re.sub('ج', 'ج̯͡', zhrf20)
    zhrf20 = re.sub('د', 'د̯͡', zhrf20)
    zhrf20 = re.sub('ذ', 'ذ̯͡', zhrf20)
    zhrf20 = re.sub('ش', 'ش̯͡', zhrf20)
    zhrf20 = re.sub('س', 'س̯͡', zhrf20)
    zhrf20 = re.sub('ي', 'ي̯͡', zhrf20)
    zhrf20 = re.sub('ب', 'ب̯͡', zhrf20)
    zhrf20 = re.sub('ل', 'ل̯͡', zhrf20)
    zhrf20 = re.sub('ا', 'آ̯͡', zhrf20)
    zhrf20 = re.sub('ت', 'ت̯͡', zhrf20)
    zhrf20 = re.sub('ن', 'ن̯͡', zhrf20)
    zhrf20 = re.sub('م', 'م̯͡', zhrf20)
    zhrf20 = re.sub('ك', 'ك̯͡', zhrf20)
    zhrf20 = re.sub('ط', 'ط̯͡', zhrf20)
    zhrf20 = re.sub('ئ', 'ﮯ̯͡ء', zhrf20)
    zhrf20 = re.sub('ء', 'ء', zhrf20)
    zhrf20 = re.sub('ؤ', 'ؤ', zhrf20)
    zhrf20 = re.sub('ر', 'ر̯͡', zhrf20)
    zhrf20 = re.sub('لا', 'ل̯͡آ̯͡', zhrf20)
    zhrf20 = re.sub('ى', 'ﮯ̯͡', zhrf20)
    zhrf20 = re.sub('ة', 'ة', zhrf20)
    zhrf20 = re.sub('و', 'ۆ̯͡', zhrf20)
    zhrf20 = re.sub('ز', 'ز̯͡', zhrf20)
    zhrf20 = re.sub('ظ', 'ظ̯͡', zhrf20)
    zhrf20 = re.sub('a', "【a】", zhrf20)
    zhrf20 = re.sub('A', "【A】", zhrf20)
    zhrf20 = re.sub("b", "【b】", zhrf20)
    zhrf20 = re.sub("B", "【B】", zhrf20)
    zhrf20 = re.sub("c", "【c】", zhrf20)
    zhrf20 = re.sub("C", "【C】", zhrf20)
    zhrf20 = re.sub("d", "【d】", zhrf20)
    zhrf20 = re.sub("D", "【D】", zhrf20)
    zhrf20 = re.sub("e", "【e】", zhrf20)
    zhrf20 = re.sub("E", "【E】", zhrf20)
    zhrf20 = re.sub("f", "【f】", zhrf20)
    zhrf20 = re.sub("F", "【F】", zhrf20)
    zhrf20 = re.sub("g", "【g】", zhrf20)
    zhrf20 = re.sub("G", "【G】", zhrf20)
    zhrf20 = re.sub("h", "【h】", zhrf20)
    zhrf20 = re.sub("H", "【H】", zhrf20)
    zhrf20 = re.sub("i", "【i】", zhrf20)
    zhrf20 = re.sub("I", "【I】", zhrf20)
    zhrf20 = re.sub("j", "【j】", zhrf20)
    zhrf20 = re.sub("J", "【J】", zhrf20)
    zhrf20 = re.sub("k", "【k】", zhrf20)
    zhrf20 = re.sub("K", "【K】", zhrf20)
    zhrf20 = re.sub("l", "【l】", zhrf20)
    zhrf20 = re.sub("L", "【L】", zhrf20)
    zhrf20 = re.sub("m", "【m】", zhrf20)
    zhrf20 = re.sub("M", "【M】", zhrf20)
    zhrf20 = re.sub("n", "【n】", zhrf20)
    zhrf20 = re.sub("N", "【N】", zhrf20)
    zhrf20 = re.sub("o", "【o】", zhrf20)
    zhrf20 = re.sub("O", "【O】", zhrf20)
    zhrf20 = re.sub("p", "【p】", zhrf20)
    zhrf20 = re.sub("P", "【P】", zhrf20)
    zhrf20 = re.sub("q", "【q】", zhrf20)
    zhrf20 = re.sub("Q", "【Q】", zhrf20)
    zhrf20 = re.sub("r", "【r】", zhrf20)
    zhrf20 = re.sub("R", "【R】", zhrf20)
    zhrf20 = re.sub("s", "【s】", zhrf20)
    zhrf20 = re.sub("S", "【S】", zhrf20)
    zhrf20 = re.sub("t", "【t】", zhrf20)
    zhrf20 = re.sub("T", "【T】", zhrf20)
    zhrf20 = re.sub("u", "【u】", zhrf20)
    zhrf20 = re.sub("U", "【U】", zhrf20)
    zhrf20 = re.sub("v", "【v】", zhrf20)
    zhrf20 = re.sub("V", "【V】", zhrf20)
    zhrf20 = re.sub("w", "【w】", zhrf20)
    zhrf20 = re.sub("W", "【W】", zhrf20)
    zhrf20 = re.sub("x", "【x】", zhrf20)
    zhrf20 = re.sub("X", "【X】", zhrf20)
    zhrf20 = re.sub("y", "【y】", zhrf20)
    zhrf20 = re.sub("Y", "【Y】", zhrf20)
    zhrf20 = re.sub("z", "【z】", zhrf20)
    zhrf20 = re.sub("Z", "【Z】", zhrf20)
    
    zhrf21 = re.sub('ض', 'ضـ⫍⫎ـ', text)
    zhrf21 = re.sub('ص', 'صـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ث', 'ثـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ق', 'قـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ف', 'فـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('غ', 'غـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ع', 'عـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ه', 'هّ', zhrf21)
    zhrf21 = re.sub('خ', 'خـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ح', 'حـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ج', 'جـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('د', 'دٍ', zhrf21)
    zhrf21 = re.sub('ذ', 'ذِ', zhrf21)
    zhrf21 = re.sub('ش', 'شـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('س', 'سـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ي', 'يـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ب', 'بـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ل', 'لَ', zhrf21)
    zhrf21 = re.sub('ا', 'آ', zhrf21)
    zhrf21 = re.sub('ت', 'تـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ن', 'نـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('م', 'مـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ك', 'كـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ط', 'طـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('ئ', 'ﮯء', zhrf21)
    zhrf21 = re.sub('ء', 'ء', zhrf21)
    zhrf21 = re.sub('ؤ', 'ؤ', zhrf21)
    zhrf21 = re.sub('ر', 'رٍ', zhrf21)
    zhrf21 = re.sub('لا', 'لَآ', zhrf21)
    zhrf21 = re.sub('ى', 'ﮯ', zhrf21)
    zhrf21 = re.sub('ة', 'ةّ', zhrf21)
    zhrf21 = re.sub('و', 'وٌ', zhrf21)
    zhrf21 = re.sub('ز', 'زٍ', zhrf21)
    zhrf21 = re.sub('ظ', 'ظـ⫍⫎ـ', zhrf21)
    zhrf21 = re.sub('a', "a̺͆", zhrf21)
    zhrf21 = re.sub('A', "A̺͆", zhrf21)
    zhrf21 = re.sub("b", "b̺͆", zhrf21)
    zhrf21 = re.sub("B", "B̺͆", zhrf21)
    zhrf21 = re.sub("c", "c̺͆", zhrf21)
    zhrf21 = re.sub("C", "C̺͆", zhrf21)
    zhrf21 = re.sub("d", "d̺͆", zhrf21)
    zhrf21 = re.sub("D", "D̺͆", zhrf21)
    zhrf21 = re.sub("e", "e̺͆", zhrf21)
    zhrf21 = re.sub("E", "E̺͆", zhrf21)
    zhrf21 = re.sub("f", "f̺͆", zhrf21)
    zhrf21 = re.sub("F", "F̺͆", zhrf21)
    zhrf21 = re.sub("g", "g̺͆", zhrf21)
    zhrf21 = re.sub("G", "G̺͆", zhrf21)
    zhrf21 = re.sub("h", "h̺͆", zhrf21)
    zhrf21 = re.sub("H", "H̺͆", zhrf21)
    zhrf21 = re.sub("i", "i̺͆", zhrf21)
    zhrf21 = re.sub("I", "I̺͆", zhrf21)
    zhrf21 = re.sub("j", "j̺͆", zhrf21)
    zhrf21 = re.sub("J", "J̺͆", zhrf21)
    zhrf21 = re.sub("k", "k̺͆", zhrf21)
    zhrf21 = re.sub("K", "K̺͆", zhrf21)
    zhrf21 = re.sub("l", "l̺͆", zhrf21)
    zhrf21 = re.sub("L", "L̺͆", zhrf21)
    zhrf21 = re.sub("m", "m̺͆", zhrf21)
    zhrf21 = re.sub("M", "M̺͆", zhrf21)
    zhrf21 = re.sub("n", "n̺͆", zhrf21)
    zhrf21 = re.sub("N", "N̺͆", zhrf21)
    zhrf21 = re.sub("o", "o̺͆", zhrf21)
    zhrf21 = re.sub("O", "O̺͆", zhrf21)
    zhrf21 = re.sub("p", "p̺͆", zhrf21)
    zhrf21 = re.sub("P", "P̺͆", zhrf21)
    zhrf21 = re.sub("q", "q̺͆", zhrf21)
    zhrf21 = re.sub("Q", "Q̺͆", zhrf21)
    zhrf21 = re.sub("r", "r̺͆", zhrf21)
    zhrf21 = re.sub("R", "R̺͆", zhrf21)
    zhrf21 = re.sub("s", "s̺͆", zhrf21)
    zhrf21 = re.sub("S", "S̺͆", zhrf21)
    zhrf21 = re.sub("t", "t̺͆", zhrf21)
    zhrf21 = re.sub("T", "T̺͆", zhrf21)
    zhrf21 = re.sub("u", "u̺͆", zhrf21)
    zhrf21 = re.sub("U", "U̺͆", zhrf21)
    zhrf21 = re.sub("v", "v̺͆", zhrf21)
    zhrf21 = re.sub("V", "V̺͆", zhrf21)
    zhrf21 = re.sub("w", "w̺͆", zhrf21)
    zhrf21 = re.sub("W", "W̺͆", zhrf21)
    zhrf21 = re.sub("x", "x̺͆", zhrf21)
    zhrf21 = re.sub("X", "X̺͆", zhrf21)
    zhrf21 = re.sub("y", "Y̺͆", zhrf21)
    zhrf21 = re.sub("Y", "Y̺͆", zhrf21)
    zhrf21 = re.sub("z", "z̺͆", zhrf21)
    zhrf21 = re.sub("Z", "Z̺͆", zhrf21)
    
    
    Text_Zhrfa = "1- `" + zhrf + random.choice(EmojeS) \
                 + "`\n\n2-` " + zhrf2 + random.choice(EmojeS) \
                 + "`\n\n3-` " + zhrf3 + random.choice(EmojeS) \
                 + "`\n\n4-` " + zhrf4 + random.choice(EmojeS) \
                 + "`\n\n5-` " + zhrf5 + random.choice(EmojeS) \
                 + "`\n\n6-` " + zhrf6 + random.choice(EmojeS) \
                 + "`\n\n7-` " + zhrf7 + random.choice(EmojeS) \
                 + "`\n\n8-` " + zhrf8 + random.choice(EmojeS) \
                 + "`\n\n9-` " + zhrf9 + random.choice(EmojeS) \
                 + "`\n\n10-` " + zhrf10 + random.choice(Emoje) \
                 + "`\n\n11-` " + zhrf11 + random.choice(Emoje) \
                 + "`\n\n12-` " + zhrf12 + random.choice(Emoje) \
                 + "`\n\n13-` " + zhrf13 + random.choice(Emoje) \
                 + "`\n\n14-` " + zhrf14 + random.choice(Emoje) \
                 + "`\n\n15-` " + zhrf15 + random.choice(Emoje) \
                 + "`\n\n16-` " + zhrf16 + random.choice(Emoje) \
                 + "`\n\n17-` " + zhrf17 + random.choice(Emoje) \
                 + "`\n\n18-` " + zhrf18 + random.choice(Emoje) \
                 + "`\n\n19-` " + zhrf19 + random.choice(Emoje) \
                 + "`\n\n20-` " + zhrf20 + random.choice(Emoje) \
                 + "`\n\n21-` " + zhrf21 + random.choice(Emoje) \
                 + "`\n\n22-` " + zhrf5 + random.choice(EmojeS) 
    Text_Zhrfa = Text_Zhrfa + "`\n\n اضغط علـي الاسـم ليـتم النـسخ \n│ \n🐉"
    await m.reply_text(Text_Zhrfa)

#..........................................   الهمسه    ................................................................
import pyromod, random, string
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton as Button, InlineKeyboardMarkup as Markup


hms = {}

def randCode():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(7))

async def check_user_in_channel(user_id, channel_id, client):
    try:
        member = await client.get_chat_member(channel_id, user_id)
        return member.status in ("member", "administrator", "creator")
    except (UserNotParticipant, PeerIdInvalid):
        return False

@app.on_message(filters.command(["همسه", "همسة"], prefixes=["/", ""]) & filters.group)
async def whisper_handler(client, message: Message):

    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    
    if not message.reply_to_message:
        await message.reply("⚠️ يجب الرد على رسالة المستخدم!", quote=True)
        return

    from_user = message.from_user
    to_user = message.reply_to_message.from_user

    if from_user.id == to_user.id:
        await message.reply("😂 لا يمكنك إرسال همسة لنفسك!", quote=True)
        return
    elif to_user.is_bot:
        await message.reply("🤖 لا يمكنك إرسال همسة لبوت!", quote=True)
        return

    code = randCode()
    hms[code] = {
        "chat_id": message.chat.id,
        "from_id": from_user.id,
        "to_id": to_user.id,
        "msg_id": message.reply_to_message.id
    }

    button = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            "📩 اضغط هنا لإرسال الهمسة",
            url=f"https://t.me/{client.me.username}?start={code}"
        )
    ]])

    await message.reply(
        f"📨 تم إعداد همسة لـ {to_user.mention}\n"
        "🔽 اضغط الزر أدناه لكتابة الهمسة",
        reply_markup=button,
        quote=True
    )

@app.on_message(filters.private & filters.regex(r"^/start (\w{7})$"))
async def start_whisper(client, message: Message):
    code = message.text.split()[1]
    if code not in hms:
        await message.reply("❌ رابط الهمسة غير صالح أو منتهي الصلاحية!", quote=True)
        return

    data = hms[code]
    if message.from_user.id != data["from_id"]:
        await message.reply("🚫 هذه الهمسة ليست لك!", quote=True)
        return

    ask = await client.ask(
        message.chat.id,
        "✍️ أرسل الهمسة الآن (نص، صورة، فيديو، ملصق، صوت...):",
        filters=filters.user(data["from_id"]),
        timeout=300
    )
    content_type = None
    content = None
    file_id = None
    if ask.text:
        content_type = "text"
        content = ask.text
    elif ask.photo:
        content_type = "photo"
        content = ask.caption
        file_id = ask.photo.file_id
    elif ask.sticker:
        content_type = "sticker"
        file_id = ask.sticker.file_id
    elif ask.video:
        content_type = "video"
        content = ask.caption
        file_id = ask.video.file_id
    elif ask.voice:
        content_type = "voice"
        content = ask.caption
        file_id = ask.voice.file_id
    else:
        await message.reply("❌ نوع المحتوى غير مدعوم!", quote=True)
        return
    hms[code].update({
        "content_type": content_type,
        "content": content,
        "file_id": file_id
    })
    reply_code = randCode()
    hms[reply_code] = {
        "chat_id": data["chat_id"],
        "from_id": data["to_id"],
        "to_id": data["from_id"],
        "msg_id": data["msg_id"]
    }
    to_user = await client.get_users(data["to_id"])
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "🔓 فتح الهمسة",
            url=f"https://t.me/{client.me.username}?start=open_{code}"
        )],
        [InlineKeyboardButton(
            "📩 أرسل همسة",
            url=f"https://t.me/{client.me.username}?start={reply_code}"
        )]
    ])
    await client.send_message(
        data["chat_id"],
        f"📬 لديك همسة سرية من {message.from_user.mention} إلى {to_user.mention}",
        reply_to_message_id=data["msg_id"],
        reply_markup=buttons
    )
    await message.reply("✅ تم إرسال الهمسة بنجاح!", quote=True)

@app.on_message(filters.private & filters.regex(r"^/start open_(\w{7})$"))
async def open_whisper(client, message: Message):
    code = message.text.split("_")[1]
    if code not in hms:
        await message.reply("❌ رابط الهمسة غير صالح أو منتهي الصلاحية!", quote=True)
        return

    data = hms[code]
    if message.from_user.id not in [data["from_id"], data["to_id"], zombie_id, OWNER_ID, sourse_dev]:
        await message.reply("🚫 ليس لديك صلاحية لرؤية هذه الهمسة!", quote=True)
        return

    if data["content_type"] == "text":
        await message.reply(data["content"], quote=True)
    elif data["content_type"] == "photo":
        await message.reply_photo(data["file_id"], caption=data["content"], quote=True)
    elif data["content_type"] == "sticker":
        await message.reply_sticker(data["file_id"], quote=True)
    elif data["content_type"] == "video":
        await message.reply_video(data["file_id"], caption=data["content"], quote=True)
    elif data["content_type"] == "voice":
        await message.reply_voice(data["file_id"], caption=data["content"], quote=True)

                
#..........................................   الهمسه    ................................................................
#..........................................   دعوه    ................................................................
@app.on_message(filters.video_chat_members_invited)
async def zoharyy(client, message): 
           text = f"- قام {message.from_user.mention}\n - بدعوة : "
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} ")
           except:
             pass               
#..........................................   دعوه    ................................................................


@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {da} ثواني**")        
    elif 60 < da < 3600:
        if 1 <= ma[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها دقيقه**")
        elif 2 <= ma[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها دقيقتين**")
        elif 3 <= ma[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {ma[0]} دقايق**")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {ma[0]} دقيقه**")
    elif 3600 < da < 86400:
        if 1 <= ho[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها ساعه**")
        elif 2 <= ho[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها ساعتين**")
        elif 3 <= ho[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {ho[0]} ساعات**")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {ho[0]} ساعة**")
    else:
        if 1 <= day[0] < 2:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها يوم**")
        elif 2 <= day[0] < 3:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها يومين**")
        elif 3 <= day[0] < 11:
            await message.reply(f"**- تم انهاء مكالمة الفيديو مدتها {day[0]} ايام**")  
        else:
            await message.reply(f"**- تم إنهاء مكالمة الفيديو مدتها {day[0]} يوم**")


###################################################### منع تصفيه ####################################################
max_warnings = 3
group_settings = {}
ban_count = {}

@app.on_message(filters.command("تفعيل منع التصفيه", "") & filters.group, group=54533101)
async def enable_ban_protection(client, message):
    chat_id = message.chat.id
    group_settings[chat_id] = True
    await message.reply("✅ تم تفعيل نظام منع التصفية في هذه المجموعة")

@app.on_message(filters.command("تعطيل منع التصفيه", "") & filters.group, 5453311401)
async def disable_ban_protection(client, message):
    chat_id = message.chat.id
    group_settings[chat_id] = False
    await message.reply("❌ تم تعطيل نظام منع التصفية في هذه المجموعة")

        
@app.on_chat_member_updated(filters.group, group=4545417815)
async def welcome_handler(client: Client, chat_member_updated: ChatMemberUpdated):
    try:
        chat_id = chat_member_updated.chat.id
        if chat_id not in group_settings or not group_settings[chat_id]:
            return
        if not chat_member_updated.new_chat_member:
            return
        if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
            kicked_by = chat_member_updated.new_chat_member.restricted_by
            user = chat_member_updated.new_chat_member.user
            chat_id = chat_member_updated.chat.id
            if kicked_by is None:
                return
            if kicked_by.is_self:
                pass
            else:
                if kicked_by.id != zombie_id:
                    admin_id = kicked_by.id
                    admin_name = kicked_by.first_name
                    user_mention = f"[{user.first_name}](tg://user?id={user.id})"
                    admin_mention = f"[{admin_name}](tg://user?id={admin_id})"
                    ban_count[admin_id] = ban_count.get(admin_id, 0) + 1
                    warnings_left = max_warnings - ban_count[admin_id]
                    message = (
                        "🚨 قام أحد المشرفين بطرد مستخدم**\n"
                        f"👤 **المستخدم: {user_mention}\n"
                        f"🆔 User ID: `{user.id}`\n"
                        f"👮 المشرف المسؤول: {admin_mention}\n"
                        f"📊 عدد الأشخاص الذين طردهم: `{ban_count[admin_id]}`\n"
                        f"⚠️ عدد التحذيرات المتبقية: `{warnings_left if warnings_left > 0 else '🚫 تم تجاوز الحد!'}`\n"
                    )
                    if warnings_left <= 0:
                        try:
                            await client.ban_chat_member(chat_id, admin_id)
                            message += "\n❌ تم حظر المشرف بسبب تجاوز الحد المسموح به!"
                        except Exception:
                            message += "\n⚠️ لم يتمكن البوت من حظر المشرف!"
            await client.send_message(chat_id, message)
    except Exception as e:
        pass
###################################################### منع تصفيه ####################################################

welcome_enabled = True

@app.on_chat_member_updated(filters.channel, group=4545417815)
async def welcome_handler(client: Client, chat_member_updated: ChatMemberUpdated):
    try:
        if not welcome_enabled:
            return
        if not chat_member_updated.new_chat_member:
            return
        if chat_member_updated.new_chat_member.status == ChatMemberStatus.BANNED:
            kicked_by = chat_member_updated.new_chat_member.restricted_by
            user = chat_member_updated.new_chat_member.user
            chat_id = chat_member_updated.chat.id
            if kicked_by is None:
                return
            if kicked_by.is_self:
                pass
            else:
                if kicked_by.id != zombie_id:
                    admin_id = kicked_by.id
                    admin_name = kicked_by.first_name
                    user_mention = f"[{user.first_name}](tg://user?id={user.id})"
                    admin_mention = f"[{admin_name}](tg://user?id={admin_id})"
                    ban_count[admin_id] = ban_count.get(admin_id, 0) + 1
                    warnings_left = max_warnings - ban_count[admin_id]
                    message = (
                        "🚨 قام أحد المشرفين بطرد مستخدم**\n"
                        f"👤 **المستخدم: {user_mention}\n"
                        f"🆔 User ID: `{user.id}`\n"
                        f"👮 المشرف المسؤول: {admin_mention}\n"
                        f"📊 عدد الأشخاص الذين طردهم: `{ban_count[admin_id]}`\n"
                        f"⚠️ عدد التحذيرات المتبقية: `{warnings_left if warnings_left > 0 else '🚫 تم تجاوز الحد!'}`\n"
                    )
                    if warnings_left <= 0:
                        try:
                            await client.ban_chat_member(chat_id, admin_id)
                            message += "\n❌ تم حظر المشرف بسبب تجاوز الحد المسموح به!"
                        except Exception:
                            message += "\n⚠️ لم يتمكن البوت من حظر المشرف!"
            await client.send_message(chat_id, message)
    except Exception as e:
        pass
###################################################### منع تصفيه ####################################################
###################################################### رفع المشرف ####################################################
admin_edit_cache = {}

@app.on_message(filters.command("تعديل صلاحيات", "") & filters.group)
async def edit_admin_permissions(client, message):
    if not await is_admin(message.from_user.id, message.chat.id):
        await message.reply_text("⚠️ تحتاج إلى صلاحية المشرف لاستخدام هذا الأمر")
        return

    if message.reply_to_message and message.reply_to_message.from_user:
        target_admin = message.reply_to_message.from_user
    elif len(message.text.split()) > 2:
        username = message.text.split()[2]
        try:
            target_admin = await client.get_users(username.strip("@"))
        except:
            await message.reply_text("❌ لم يتم العثور على المستخدم")
            return
    else:
        ask = await app.ask(message.chat.id, "🔍 يرجى إرسال معرف المشرف أو الرد على رسالته:", filters=filters.user(message.from_user.id), timeout=120)
        try:
            target_admin = await client.get_users(ask.text)
        except:
            await message.reply_text("❌ بيانات المستخدم غير صحيحة")
            return

    try:
        admin_status = await client.get_chat_member(message.chat.id, target_admin.id)
        if admin_status.status not in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            await message.reply_text("⚠️ هذا العضو ليس مشرفاً في المجموعة")
            return
    except:
        await message.reply_text("❌ حدث خطأ في التحقق من الصلاحيات")
        return

    buttons = [
        [
            InlineKeyboardButton("🗑️ حذف الرسائل", callback_data=f"editperm_del_{target_admin.id}"),
            InlineKeyboardButton("🔇 تقييد أعضاء", callback_data=f"editperm_ban_{target_admin.id}")
        ],
        [
            InlineKeyboardButton("📌 تثبيت رسائل", callback_data=f"editperm_pin_{target_admin.id}"),
            InlineKeyboardButton("📞 إدارة المكالمات", callback_data=f"editperm_call_{target_admin.id}")
        ],
        [
            InlineKeyboardButton("➕ دعوة مستخدمين", callback_data=f"editperm_invite_{target_admin.id}"),
            InlineKeyboardButton("✏️ تعديل المجموعة", callback_data=f"editperm_info_{target_admin.id}")
        ],
        [
            InlineKeyboardButton("🔼 رفع مشرفين", callback_data=f"editperm_promo_{target_admin.id}")
        ],
        [
            InlineKeyboardButton("✅ حفظ التعديلات", callback_data=f"save_perms_{target_admin.id}")
        ]
    ]
    current_perms = admin_status.privileges
    perm_status = {
        "del": "✅" if current_perms.can_delete_messages else "❌",
        "ban": "✅" if current_perms.can_restrict_members else "❌",
        "pin": "✅" if current_perms.can_pin_messages else "❌",
        "call": "✅" if current_perms.can_manage_video_chats else "❌",
        "invite": "✅" if current_perms.can_invite_users else "❌",
        "info": "✅" if current_perms.can_change_info else "❌",
        "promo": "✅" if current_perms.can_promote_members else "❌"
    }
    buttons[0][0].text = f"{perm_status['del']} حذف الرسائل"
    buttons[0][1].text = f"{perm_status['ban']} تقييد أعضاء"
    buttons[1][0].text = f"{perm_status['pin']} تثبيت رسائل"
    buttons[1][1].text = f"{perm_status['call']} إدارة المكالمات"
    buttons[2][0].text = f"{perm_status['invite']} دعوة مستخدمين"
    buttons[2][1].text = f"{perm_status['info']} تعديل المجموعة"
    buttons[3][0].text = f"{perm_status['promo']} رفع مشرفين"
    admin_edit_cache[f"edit_{target_admin.id}"] = {
        "chat_id": message.chat.id,
        "admin_id": target_admin.id,
        "promoter_id": message.from_user.id,
        "current_perms": current_perms,
        "new_perms": {
            "del": current_perms.can_delete_messages,
            "ban": current_perms.can_restrict_members,
            "pin": current_perms.can_pin_messages,
            "call": current_perms.can_manage_video_chats,
            "invite": current_perms.can_invite_users,
            "info": current_perms.can_change_info,
            "promo": current_perms.can_promote_members
        }
    }
    await message.reply_text(
        f"⚙️ **تعديل صلاحيات المشرف:**\n"
        f"👤 المستخدم: {target_admin.mention}\n"
        f"🔽 اختر الصلاحيات المطلوبة:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@app.on_callback_query(filters.regex("^editperm_.*"))
async def update_permission(client, callback):
    data = callback.data
    _, perm, admin_id = data.split('_')
    cache_key = f"edit_{admin_id}"
    if cache_key not in admin_edit_cache:
        await callback.answer("❌ انتهت الجلسة!", show_alert=True)
        return
    
    perm_names = {
        "del": "حذف الرسائل",
        "ban": "تقييد الأعضاء",
        "pin": "تثبيت الرسائل",
        "call": "إدارة المكالمات",
        "invite": "دعوة مستخدمين",
        "info": "تعديل المجموعة",
        "promo": "رفع مشرفين"
    }
    current_state = admin_edit_cache[cache_key]["new_perms"][perm]
    admin_edit_cache[cache_key]["new_perms"][perm] = not current_state
    new_state = "✅" if not current_state else "❌"
    button_icons = {
        "del": "🗑️",
        "ban": "🔇",
        "pin": "📌",
        "call": "📞",
        "invite": "➕",
        "info": "✏️",
        "promo": "🔼"
    }
    
    for row in callback.message.reply_markup.inline_keyboard:
        for button in row:
            if button.callback_data.endswith(f"{perm}_{admin_id}"):
                button.text = f"{button_icons[perm]} {perm_names[perm]}: {new_state}"
                break
    
    await callback.message.edit_reply_markup(callback.message.reply_markup)
    await callback.answer(f"تم تغيير صلاحية {perm_names[perm]}")

@app.on_callback_query(filters.regex("^save_perms_.*"))
async def save_permissions(client, callback):
    admin_id = callback.data.split('_')[-1]
    cache_key = f"edit_{admin_id}"
    if cache_key not in admin_edit_cache:
        await callback.answer("❌ انتهت الجلسة!", show_alert=True)
        return
    data = admin_edit_cache[cache_key]
    new_perms = data["new_perms"]
    try:
        await app.promote_chat_member(
            chat_id=data["chat_id"],
            user_id=admin_id,
            privileges=ChatPrivileges(
                can_delete_messages=new_perms["del"],
                can_restrict_members=new_perms["ban"],
                can_pin_messages=new_perms["pin"],
                can_manage_video_chats=new_perms["call"],
                can_invite_users=new_perms["invite"],
                can_change_info=new_perms["info"],
                can_promote_members=new_perms["promo"]
            )
        )
        changes = []
        perm_display = {
            "del": "حذف الرسائل",
            "ban": "تقييد الأعضاء",
            "pin": "تثبيت الرسائل",
            "call": "إدارة المكالمات",
            "invite": "دعوة مستخدمين",
            "info": "تعديل المجموعة",
            "promo": "رفع مشرفين"
        }
        for perm, name in perm_display.items():
            current_value = getattr(data["current_perms"], f"can_{perm_map(perm)}", False)
            if new_perms[perm] != current_value:
                changes.append(f"◍ {name}: {'✅' if new_perms[perm] else '❌'}")
        admin_user = await client.get_users(admin_id)
        promoter_user = await client.get_users(data["promoter_id"])
        report_text = (
            f"🎯 **تقرير تعديل الصلاحيات**\n\n"
            f"👤 المشرف: {admin_user.mention}\n"
            f"👮‍♂️ المعدل: {promoter_user.mention}\n\n"
            f"📋 التغييرات:\n" + "\n".join(changes) + "\n\n"
            f"⏱️ {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        )
        await callback.message.reply_text(report_text)
        await callback.message.delete()
        del admin_edit_cache[cache_key]
        await callback.answer("✅ تم التحديث بنجاح!", show_alert=True)
    except Exception as e:
        error_msg = (
            "⚠️ **حدث خطأ**\n\n"
            "تعذر تحديث صلاحيات المشرف\n"
            f"السبب: {str(e)}\n\n"
            "يرجى التحقق من صلاحيات البوت والمحاولة مرة أخرى"
        )
        await callback.message.reply_text(error_msg)
        await callback.answer("❌ فشل في الحفظ!", show_alert=True)

async def is_admin(user_id, chat_id):
    try:
        user_status = await app.get_chat_member(chat_id, user_id)
        return user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except:
        return False

def perm_map(perm):
    mapping = {
        "del": "delete_messages",
        "ban": "restrict_members",
        "pin": "pin_messages",
        "call": "manage_video_chats",
        "invite": "invite_users",
        "info": "change_info",
        "promo": "promote_members"
    }
    return mapping.get(perm, "")


temp_storage = {}

@app.on_message(filters.command("رفع مشرف", "") & filters.group, group=1212474777777)
async def promote_admin(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ ليس لديك الصلاحية لتنفيذ هذا الأمر")
        return
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    permissions_keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🗑️ حذف الرسائل: ❌", callback_data=f"perm_delete_{user_id}"),
            InlineKeyboardButton("🔇 تقييد أعضاء: ❌", callback_data=f"perm_restrict_{user_id}")
        ],
        [
            InlineKeyboardButton("➕ دعوة مستخدمين: ❌", callback_data=f"perm_invite_{user_id}"),
            InlineKeyboardButton("📌 تثبيت رسائل: ❌", callback_data=f"perm_pin_{user_id}")
        ],
        [
            InlineKeyboardButton("📞 إدارة المكالمات: ❌", callback_data=f"perm_manage_{user_id}"),
            InlineKeyboardButton("✏️ تعديل المجموعة: ❌", callback_data=f"perm_change_{user_id}")
        ],
        [
            InlineKeyboardButton("🔼 رفع مشرفين: ❌", callback_data=f"perm_promote_{user_id}")
        ],
        [
            InlineKeyboardButton("✅ تأكيد الصلاحيات", callback_data=f"confirm_perms_{user_id}")
        ]
    ])
    temp_data = {
        "chat_id": message.chat.id,
        "user": user,
        "promoter": message.from_user,
        "permissions": {
            "delete": False,
            "restrict": False,
            "invite": False,
            "pin": False,
            "manage": False,
            "change": False,
            "promote": False
        }
    }
    temp_storage[f"perms_{user_id}"] = temp_data
    await message.reply_text(
        f"⚙️ **إعدادات صلاحيات المشرف:**\n"
        f"👤 المستخدم: {user.mention}\n"
        f"🔽 يرجى اختيار الصلاحيات المطلوبة:",
        reply_markup=permissions_keyboard
    )

@app.on_callback_query(filters.regex(r"^perm_(delete|restrict|invite|pin|manage|change|promote)_(\d+)$"))
async def handle_perm_buttons(client, callback):
    data = callback.data
    perm_type = callback.matches[0].group(1)
    user_id = callback.matches[0].group(2)
    temp_data = temp_storage.get(f"perms_{user_id}")
    if not temp_data:
        await callback.answer("❌ انتهت صلاحية الجلسة!", show_alert=True)
        return
    temp_data["permissions"][perm_type] = not temp_data["permissions"][perm_type]
    perm_names = {
        "delete": "🗑️ حذف الرسائل",
        "restrict": "🔇 تقييد أعضاء",
        "invite": "➕ دعوة مستخدمين",
        "pin": "📌 تثبيت رسائل",
        "manage": "📞 إدارة المكالمات",
        "change": "✏️ تعديل المجموعة",
        "promote": "🔼 رفع مشرفين"
    }
    buttons = []
    for perm, name in perm_names.items():
        state = "✅" if temp_data["permissions"][perm] else "❌"
        buttons.append(InlineKeyboardButton(
            f"{name}: {state}",
            callback_data=f"perm_{perm}_{user_id}"
        ))
    keyboard = [buttons[i:i+2] for i in range(0, len(buttons), 2)]
    keyboard.append([InlineKeyboardButton(
        "✅ تأكيد الصلاحيات",
        callback_data=f"confirm_perms_{user_id}"
    )])
    await callback.message.edit_reply_markup(
        InlineKeyboardMarkup(keyboard)
    )
    await callback.answer(f"تم تغيير صلاحية {perm_names[perm_type]}")

@app.on_callback_query(filters.regex(r"^confirm_perms_(\d+)$"))
async def handle_confirm_button(client, callback):
    user_id = callback.matches[0].group(1)
    temp_data = temp_storage.get(f"perms_{user_id}")
    
    if not temp_data:
        await callback.answer("❌ انتهت صلاحية الجلسة!", show_alert=True)
        return

    ask = await client.ask(
        temp_data["chat_id"],
        "📝 يرجى إرسال اللقب الجديد للمشرف:",
        filters=filters.user(data["from_id"]),
        timeout=300
    )
    title = ask.text
    await client.promote_chat_member(
        chat_id=temp_data["chat_id"],
        user_id=user_id,
        privileges=ChatPrivileges(
            can_delete_messages=temp_data["permissions"]["delete"],
            can_restrict_members=temp_data["permissions"]["restrict"],
            can_invite_users=temp_data["permissions"]["invite"],
            can_pin_messages=temp_data["permissions"]["pin"],
            can_manage_video_chats=temp_data["permissions"]["manage"],
            can_change_info=temp_data["permissions"]["change"],
            can_promote_members=temp_data["permissions"]["promote"]
        )
    )
    await client.set_administrator_title(
        temp_data["chat_id"],
        user_id,
        title
    )
    active_perms = []
    for perm, name in {
        "delete": "حذف الرسائل",
        "restrict": "تقييد الأعضاء", 
        "invite": "دعوة المستخدمين",
        "pin": "تثبيت الرسائل",
        "manage": "إدارة المكالمات",
        "change": "تعديل المجموعة",
        "promote": "رفع المشرفين"
    }.items():
        if temp_data["permissions"][perm]:
            active_perms.append(f"◍ {name}")
    await callback.message.reply_text(
        f"🎉 **تم رفع المشرف بنجاح**\n\n"
        f"👤 المشرف: {temp_data['user'].mention}\n"
        f"🏷️ اللقب: {title}\n"
        f"👮 تمت العملية بواسطة: {temp_data['promoter'].mention}\n\n"
        f"🔘 **الصلاحيات الممنوحة:**\n" +
        "\n".join(active_perms) + "\n\n"
        f"🕒 التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )
    await callback.message.delete()
    del temp_storage[f"perms_{user_id}"]
    await callback.answer("✅ تم رفع المشرف بنجاح!", show_alert=True)

@app.on_message(filters.command("رفع مشرف", "") & filters.channel,group=12878712474)
async def tasfaya(client, message):
    ask = await app.ask(message.chat.id, "ارسل ايدي الان", filters=filters.user(message.from_user.id), timeout=300)
    ZOMBIE = ask.text
    await app.promote_chat_member(
        chat_id=message.chat.id,
        user_id=ZOMBIE,
        privileges=ChatPrivileges(
            can_promote_members=False,
            can_manage_video_chats=True,
            can_post_messages=True,
            can_invite_users=True,
            can_edit_messages=True,
            can_delete_messages=True,
            can_change_info=False
        )
    )
    await message.reply("تم رفع العضو مشرف بنجاح")

@app.on_message(filters.command(["صلاحياتي"], ""),group=115354)
async def aarprivileges(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    cae = await client.get_chat_member(chat_id, user_id)
    status = cae.status if cae else None
    if status == ChatMemberStatus.OWNER:
        await message.reply_text("أنت مالك الجروب")
    elif status == ChatMemberStatus.MEMBER:
        await message.reply_text("أنت عضو حقير")
    else:
        privileges = cae.privileges if cae else None 
        can_promote_members = "✅" if (privileges and privileges.can_promote_members) else "❌"
        can_manage_video_chats = "✅" if (privileges and privileges.can_manage_video_chats) else "❌"
        can_pin_messages = "✅" if (privileges and privileges.can_pin_messages) else "❌"
        can_invite_users = "✅" if (privileges and privileges.can_invite_users) else "❌"
        can_restrict_members = "✅" if (privileges and privileges.can_restrict_members) else "❌"
        can_delete_messages = "✅" if (privileges and privileges.can_delete_messages) else "❌"
        can_change_info = "✅" if (privileges and privileges.can_change_info) else "❌"
        text = "صلاحياتك في الجروب:\n\n"
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton(f"ترقية الأعضاء: {can_promote_members}", callback_data="noop")],
            [InlineKeyboardButton(f"إدارة الدردشات الصوتية: {can_manage_video_chats}", callback_data="noop")],
            [InlineKeyboardButton(f"تثبيت الرسائل: {can_pin_messages}", callback_data="noop")],
            [InlineKeyboardButton(f"دعوة المستخدمين: {can_invite_users}", callback_data="noop")],
            [InlineKeyboardButton(f"تقييد الأعضاء: {can_restrict_members}", callback_data="noop")],
            [InlineKeyboardButton(f"حذف الرسائل: {can_delete_messages}", callback_data="noop")],
            [InlineKeyboardButton(f"تغيير معلومات الجروب: {can_change_info}", callback_data="noop")],
            [InlineKeyboardButton("🔄 إعادة الفحص", callback_data="refresh_privileges")]
        ])
    await message.reply_text(text, reply_markup=keyboard)

@app.on_message(filters.command(["لقبي"], ""), group=7272727866)
async def title(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    chat_id = message.chat.id
    user = await client.get_chat_member(chat_id, user_id)    
    if user.status in [ChatMemberStatus.OWNER]:
        await message.reply_text("مالك الجروب")
    elif user.status == ChatMemberStatus.MEMBER:
     await message.reply_text("عضو حقير")
    elif user.status == ChatMemberStatus.ADMINISTRATOR:
        title = user.custom_title if user.custom_title else "مشرف"
        await message.reply_text(f"{title}")

@app.on_message(filters.command(["لقبه"], ""), group=72727866)
async def title(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    user = await client.get_chat_member(chat_id, user_id)    
    if user.status in [ChatMemberStatus.OWNER]:
        await message.reply_text("مالك الجروب")
    elif user.status == ChatMemberStatus.MEMBER:
     await message.reply_text("عضو حقير")
    elif user.status == ChatMemberStatus.ADMINISTRATOR:
        title = user.custom_title if user.custom_title else "مشرف"
        await message.reply_text(f"{title}")
###################################################### رفع المشرف ####################################################

# ################################################### باقي القفل والفتح  ############################################################

LOCK_FILE = "chat_locks.json"

def load_locks():
    default_data = {
        "dardasha": {},
        "mutaharek": {},
        "channel_lock": {},
        "videoo": {},
        "tawgeh": {},
        "photo_lock": {},
        "link_lock": {},
        "mentionn": {},
        "swear_lock": {},
        "sticker_lock": {},
        "muted_users": {}
    }
    
    try:
        if os.path.exists(LOCK_FILE):
            with open(LOCK_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key in default_data:
                    if key not in data:
                        data[key] = default_data[key]
                return data
        else:
            with open(LOCK_FILE, 'w', encoding='utf-8') as f:
                json.dump(default_data, f, ensure_ascii=False, indent=4)
            return default_data
    except Exception as e:
        print(f"حدث خطأ أثناء تحميل الإعدادات: {e}")
        return default_data

def save_locks(data):
    try:
        with open(LOCK_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"حدث خطأ أثناء حفظ الإعدادات: {e}")

locks = load_locks()
dardasha = locks.get("dardasha", {})
mutaharek = locks.get("mutaharek", {})
videoo = locks.get("videoo", {})
mentionn = locks.get("mentionn", {})
tawgeh = locks.get("tawgeh", {})
channel_lock = locks.get("channel_lock", {})
link_lock = locks.get("link_lock", {})
photo_lock = locks.get("photo_lock", {})
sticker_lock = locks.get("sticker_lock", {})
swear_lock = locks.get("swear_lock", {})


muted_users = locks.get("muted_users", {})
# ################################################### الدردشه ############################################################
@app.on_message(filters.command(["قفل الدردشه","قفل الدردشة"], ""), group=1212474987878)
async def lock_chat(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return
    
    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and \
       message.from_user.id not in [*dev, OWNER_ID, sourse_dev]:
        return
    
    if chat_id in dardasha:
        current_settings = dardasha[chat_id]
        await message.reply_text(
            f"⚠️ الدردشة مقفولة بالفعل\n"
            f"◍ العقوبة: {current_settings.get('punishment', 'حذف الرسائل')}\n"
            f"◍ النطاق: {'الكل' if current_settings.get('scope', 'all') == 'all' else 'الأعضاء فقط'}"
        )
        return
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("حذف الرسائل", callback_data=f"chat_choose_delete_{message.from_user.id}")],
        [InlineKeyboardButton("كتم المرسل", callback_data=f"chat_choose_mute_{message.from_user.id}")]
    ])
    
    await message.reply_text(
        f"◍ اختر طريقة العقاب لقفل الدردشة ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex(r"^chat_choose_(delete|mute)_(\d+)$"))
async def chat_choose_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[3])
    
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return
    
    get = await client.get_chat_member(chat_id, user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and \
       callback_query.from_user.id not in [*dev, OWNER_ID, sourse_dev]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return
    
    action = callback_query.data.split('_')[2]
    
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"chat_confirm_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"chat_confirm_{action}_members_{user_id}")]
    ])
    
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع بما فيهم المشرفين\n"
        "- باستثناء المشرفين: تطبق على الأعضاء العاديين فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()

@app.on_callback_query(filters.regex(r"^chat_confirm_(delete|mute)_(all|members)_(\d+)$"))
async def chat_confirm_lock(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[4])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return
    
    get = await client.get_chat_member(int(chat_id), user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and \
       callback_query.from_user.id not in [*dev, OWNER_ID, sourse_dev]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return
    
    action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]
    
    dardasha[chat_id] = {
        "punishment": action,
        "scope": scope
    }
    locks["dardasha"] = dardasha
    save_locks(locks)
    
    await callback_query.message.edit_text(
        f"◍ تم قفل الدردشة بنجاح\n"
        f"◍ العقوبة: {'حذف الرسائل' if action == 'delete' else 'كتم المرسل'}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط (استثناء المشرفين)'}"
    )
    await callback_query.answer()

@app.on_message(filters.command(["فتح الدردشه","فتح الدردشة"], ""), group=1789212474)
async def unlock_chat(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return
    
    chat_id = str(message.chat.id)
    get = await client.get_chat_member(int(chat_id), message.from_user.id)
    
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and \
       message.from_user.id not in [*dev, OWNER_ID, sourse_dev]:
        return
    
    if chat_id not in dardasha:
        await message.reply_text("⚠️ الدردشة غير مقفولة بالفعل!")
        return
        
    del dardasha[chat_id]
    locks["dardasha"] = dardasha
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح الدردشة بواسطة ↤︎「 {message.from_user.mention} 」")

@app.on_message(filters.group, group=12897812474)
async def handle_chat_message(client, message):
    chat_id = str(message.chat.id)
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
    if chat_id not in dardasha:
        return
    
    if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id, *dev):
        return
    
    try:
        settings = dardasha[chat_id]
        punishment = settings.get("punishment", "delete")
        scope = settings.get("scope", "all")
        if scope == "members":
            user_status = await client.get_chat_member(message.chat.id, message.from_user.id)
            if user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return
        
        if punishment == "delete":
            await message.delete()
            await client.send_message(
                message.chat.id,
                f"◍ عذراً {message.from_user.mention}، الدردشة مقفولة حالياً"
            )
        elif punishment == "mute":
            await message.delete()
            if chat_id not in muted_users:
                muted_users[chat_id] = []
            
            if message.from_user.id not in muted_users[chat_id]:
                muted_users[chat_id].append(message.from_user.id)
                locks["muted_users"] = muted_users
                save_locks(locks)
                await message.reply_text(f"◍ تم كتم {message.from_user.mention} لإرسال رسالة في الدردشة المقفولة")
    except Exception as e:
        print(f"Error handling chat message: {e}")

#################################################### المتحركات ############################################################
@app.on_message(filters.regex("قفل المتحركات"), group=1289712474)
async def lock_gifs(client, message):
    is_subscribe = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribe:
        return
    
    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    
    if chat_id in mutaharek:
        current_punishment, current_scope = mutaharek[chat_id]
        await message.reply_text(
            f"⚠️ المتحركات مقفولة بالفعل\n"
            f"◍ العقوبة الحالية: {current_punishment}\n"
            f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كتم", callback_data=f"choose_mute_{message.from_user.id}")],
        [InlineKeyboardButton("تقييد", callback_data=f"choose_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("طرد", callback_data=f"choose_ban_{message.from_user.id}")]
    ])
    await message.reply_text(
        f"◍ اختر نوع العقوبة لقفل المتحركات ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex(r"^choose_(mute|restrict|ban)_(\d+)$"))
async def choose_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[2])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return
    
    get = await client.get_chat_member(chat_id, user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return
    
    action = callback_query.data.split('_')[1]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع بما فيهم المشرفين\n"
        "- باستثناء المشرفين: تطبق على الأعضاء العاديين فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()

@app.on_callback_query(filters.regex(r"^confirm_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_punishment(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[3])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return
    
    get = await client.get_chat_member(int(chat_id), user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return
    
    action, scope = callback_query.data.split('_')[1], callback_query.data.split('_')[2]
    
    mutaharek[chat_id] = [action, scope]
    locks["mutaharek"] = mutaharek
    save_locks(locks)
    
    await callback_query.message.edit_text(
        f"◍ تم قفل المتحركات بنجاح\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط (استثناء المشرفين)'}"
    )
    await callback_query.answer()

@app.on_message(filters.regex("فتح المتحركات"), group=1289712475)
async def unlock_gifs(client, message):
    is_subscribe = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribe:
        return
    
    chat_id = str(message.chat.id)
    get = await client.get_chat_member(int(chat_id), message.from_user.id)
    
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    
    
    
    if chat_id not in mutaharek:
        await message.reply_text("⚠️ المتحركات غير مقفولة بالفعل!")
        return
    
    del mutaharek[chat_id]
    locks["mutaharek"] = mutaharek
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح المتحركات بواسطة ↤︎「 {message.from_user.mention} 」")

@app.on_message(filters.animation, group=14782124)
async def handle_gif(client, message):
    chat_id = str(message.chat.id)
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
    if chat_id not in mutaharek:
        return
    
    if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id):
        return
    
    try:
        punishment, scope = mutaharek[chat_id]
        if scope == "members":
            user_status = await client.get_chat_member(message.chat.id, message.from_user.id)
            if user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return
        
        await message.delete()
        if punishment == "mute":
            if chat_id not in muted_users:
                muted_users[chat_id] = []
            
            if message.from_user.id not in muted_users[chat_id]:
                muted_users[chat_id].append(message.from_user.id)
                locks["muted_users"] = muted_users
                save_locks(locks)
                await message.reply_text(f"◍ تم كتم {message.from_user.mention} لإرسال متحركات")
        elif punishment == "restrict":
            await client.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=False,
                    can_send_other_messages=False
                ))
            await message.reply_text(f"◍ تم تقييد {message.from_user.mention} لإرسال متحركات")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ تم طرد {message.from_user.mention} لإرسال متحركات")
    
    except Exception as e:
        print(f"Error handling GIF: {e}")
# ################################################### المتحركات ############################################################
# ################################################### المينشن ############################################################
@app.on_message(filters.regex("قفل المنشن"), group=1212474000)
async def lock_mention(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    
    if chat_id in mentionn:
        current_punishment, current_scope = mentionn[chat_id]
        await message.reply_text(
            f"⚠️ المنشن مقفول بالفعل\n"
            f"◍ العقوبة الحالية: {current_punishment}\n"
            f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كتم", callback_data=f"mention_mute_{message.from_user.id}")],
        [InlineKeyboardButton("تقييد", callback_data=f"mention_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("طرد", callback_data=f"mention_ban_{message.from_user.id}")]
    ])
    await message.reply_text(
        f"◍ اختر نوع العقوبة لقفل المنشن ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex(r"^mention_(mute|restrict|ban)_(\d+)$"))
async def choose_mention_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[2])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(chat_id, user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action = callback_query.data.split('_')[1]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_mention_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_mention_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع بما فيهم المشرفين\n"
        "- باستثناء المشرفين: تطبق على الأعضاء العاديين فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()

@app.on_callback_query(filters.regex(r"^confirm_mention_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_mention_punishment(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[4])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(int(chat_id), user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]
    
    mentionn[chat_id] = [action, scope]
    locks["mentionn"] = mentionn
    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم قفل المنشن بنجاح\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط (استثناء المشرفين)'}"
    )
    await callback_query.answer()

@app.on_message(filters.regex("فتح المنشن"), group=1210002474)
async def unlock_mention(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    
    if chat_id not in mentionn:
        await message.reply_text("⚠️ المنشن غير مقفول بالفعل!")
        return

    del mentionn[chat_id]
    locks["mentionn"] = mentionn
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح المنشن بواسطة ↤︎「 {message.from_user.mention} 」")

@app.on_message(filters.text & filters.group, group=59)
async def handle_mention(client, message):
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
    chat_id = str(message.chat.id)
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
    if chat_id not in mentionn:
        return
    if "@" not in message.text:
        return
    if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id):
        return

    try:
        punishment, scope = mentionn[chat_id]
        if scope == "members":
            user_status = await client.get_chat_member(message.chat.id, message.from_user.id)
            if user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return

        await message.delete()
        if punishment == "mute":
            if chat_id not in muted_users:
                muted_users[chat_id] = []
            if message.from_user.id not in muted_users[chat_id]:
                muted_users[chat_id].append(message.from_user.id)
                locks["muted_users"] = muted_users
                save_locks(locks)
                await message.reply_text(f"◍ تم كتم {message.from_user.mention} لإرسال منشن ممنوع")
        elif punishment == "restrict":
            await client.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=False,
                    can_send_other_messages=False
                ))
            await message.reply_text(f"◍ تم تقييد {message.from_user.mention} لإرسال منشن ممنوع")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ تم طرد {message.from_user.mention} لإرسال منشن ممنوع")
    except Exception as e:
        print(f"Error handling mention: {e}")


# ################################################### المينشن ############################################################
# ################################################### الفيديو ############################################################
@app.on_message(filters.regex("قفل الفيديو"), group=1212474487878)
async def lock_video(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    
    if chat_id in videoo:
        current_punishment, current_scope = videoo[chat_id]
        await message.reply_text(
            f"⚠️ الفيديو مقفول بالفعل\n"
            f"◍ العقوبة الحالية: {current_punishment}\n"
            f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كتم", callback_data=f"video_mute_{message.from_user.id}")],
        [InlineKeyboardButton("تقييد", callback_data=f"video_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("طرد", callback_data=f"video_ban_{message.from_user.id}")]
    ])
    await message.reply_text(
        f"◍ اختر نوع العقوبة لقفل الفيديو ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex(r"^video_(mute|restrict|ban)_(\d+)$"))
async def choose_video_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[2])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(chat_id, user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action = callback_query.data.split('_')[1]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_video_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_video_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع\n"
        "- باستثناء المشرفين: تطبق على الأعضاء فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()

@app.on_callback_query(filters.regex(r"^confirm_video_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_video_punishment(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[4])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(int(chat_id), user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]
    
    videoo[chat_id] = [action, scope]
    locks["videoo"] = videoo
    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم قفل الفيديو بنجاح\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط'}"
    )
    await callback_query.answer()

@app.on_message(filters.regex("فتح الفيديو"), group=12231212474)
async def unlock_video(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    
    if chat_id not in videoo:
        await message.reply_text("⚠️ الفيديو غير مقفول!")
        return

    del videoo[chat_id]
    locks["videoo"] = videoo
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح الفيديو بواسطة ↤︎「 {message.from_user.mention} 」")

@app.on_message(filters.video, group=121247487994)
async def handle_video(client, message):
    chat_id = str(message.chat.id)
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
    if chat_id not in videoo:
        return
    if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id):
        return

    try:
        punishment, scope = videoo[chat_id]
        if scope == "members":
            user_status = await client.get_chat_member(message.chat.id, message.from_user.id)
            if user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return

        await message.delete()
        if punishment == "mute":
            if chat_id not in muted_users:
                muted_users[chat_id] = []
            if message.from_user.id not in muted_users[chat_id]:
                muted_users[chat_id].append(message.from_user.id)
                locks["muted_users"] = muted_users
                save_locks(locks)
                await message.reply_text(f"◍ {message.from_user.mention} تم كتمك بسبب إرسال فيديو محظور.")
        elif punishment == "restrict":
            await client.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=False,
                    can_send_other_messages=False
                ))
            await message.reply_text(f"◍ {message.from_user.mention} تم تقييدك بسبب إرسال فيديو محظور.")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب إرسال فيديو محظور.")
    except Exception as e:
        print(f"Error handling video: {e}")



# ################################################### الفيديو ############################################################
# ################################################### التوجيه ############################################################
@app.on_message(filters.regex("قفل التوجيه"), group=12124747988)
async def lock_forward(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    
    if chat_id in tawgeh:
        current_punishment, current_scope = tawgeh[chat_id]
        await message.reply_text(
            f"⚠️ التوجيه مقفول بالفعل\n"
            f"◍ العقوبة الحالية: {current_punishment}\n"
            f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كتم", callback_data=f"fw_mute_{message.from_user.id}")],
        [InlineKeyboardButton("تقييد", callback_data=f"fw_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("طرد", callback_data=f"fw_ban_{message.from_user.id}")]
    ])
    await message.reply_text(
        f"◍ اختر نوع العقوبة لقفل التوجيه ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex(r"^fw_(mute|restrict|ban)_(\d+)$"))
async def choose_forward_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[2])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(chat_id, user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action = callback_query.data.split('_')[1]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_fw_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_fw_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع\n"
        "- باستثناء المشرفين: تطبق على الأعضاء فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()


@app.on_callback_query(filters.regex(r"^confirm_fw_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_forward_lock(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[4])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(int(chat_id), user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]

    tawgeh[chat_id] = [action, scope]
    locks["tawgeh"] = tawgeh
    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم قفل التوجيه بنجاح\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط'}"
    )
    await callback_query.answer()


@app.on_message(filters.regex("فتح التوجيه"), group=12124743147)
async def unlock_forward(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    
    if chat_id not in tawgeh:
        await message.reply_text("⚠️ التوجيه غير مقفول!")
        return

    del tawgeh[chat_id]
    locks["tawgeh"] = tawgeh
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح التوجيه بواسطة ↤︎「 {message.from_user.mention} 」")


@app.on_message(filters.forwarded, group=1277712474)
async def handle_forwarded(client, message):
    chat_id = str(message.chat.id)
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
    if chat_id not in tawgeh:
        return
    if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id):
        return

    try:
        punishment, scope = tawgeh[chat_id]
        if scope == "members":
            user_status = await client.get_chat_member(message.chat.id, message.from_user.id)
            if user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return

        await message.delete()
        if punishment == "mute":
            if chat_id not in muted_users:
                muted_users[chat_id] = []
            if message.from_user.id not in muted_users[chat_id]:
                muted_users[chat_id].append(message.from_user.id)
                locks["muted_users"] = muted_users
                save_locks(locks)
                await message.reply_text(f"◍ {message.from_user.mention} تم كتمك بسبب إرسال توجيه محظور.")
        elif punishment == "restrict":
            await client.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=False,
                    can_send_other_messages=False
                ))
            await message.reply_text(f"◍ {message.from_user.mention} تم تقييدك بسبب إرسال توجيه محظور.")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب إرسال توجيه محظور.")
    except Exception as e:
        print(f"Error handling forwarded message: {e}")


# ################################################### التوجيه ############################################################
# ################################################### الملصقات ############################################################
@app.on_message(filters.regex("قفل الملصقات"), group=129797912474)
async def lock_stickers(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    
    if chat_id in sticker_lock:
        current_punishment, current_scope = sticker_lock[chat_id]
        await message.reply_text(
            f"⚠️ الملصقات مقفولة بالفعل\n"
            f"◍ العقوبة الحالية: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كتم", callback_data=f"st_mute_{message.from_user.id}")],
        [InlineKeyboardButton("تقييد", callback_data=f"st_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("طرد", callback_data=f"st_ban_{message.from_user.id}")]
    ])
    await message.reply_text(
        f"◍ اختر نوع العقوبة لقفل الملصقات ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex(r"^st_(mute|restrict|ban)_(\d+)$"))
async def choose_sticker_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[2])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(chat_id, user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action = callback_query.data.split('_')[1]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_st_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_st_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع\n"
        "- باستثناء المشرفين: تطبق على الأعضاء فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()


@app.on_callback_query(filters.regex(r"^confirm_st_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_sticker_lock(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[4])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(int(chat_id), user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]

    sticker_lock[chat_id] = [action, scope]
    locks["sticker_lock"] = sticker_lock
    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم قفل الملصقات بنجاح\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل' if scope == 'all' else 'الأعضاء فقط'}"
    )
    await callback_query.answer()


@app.on_message(filters.regex("فتح الملصقات"), group=12127989474)
async def unlock_stickers(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    
    if chat_id not in sticker_lock:
        await message.reply_text("⚠️ الملصقات غير مقفولة!")
        return

    del sticker_lock[chat_id]
    locks["sticker_lock"] = sticker_lock
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح الملصقات بواسطة ↤︎「 {message.from_user.mention} 」")


@app.on_message(filters.sticker, group=1211112474)
async def handle_sticker(client, message):
    chat_id = str(message.chat.id)
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
    if chat_id not in sticker_lock:
        return
    if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id):
        return

    try:
        punishment, scope = sticker_lock[chat_id]
        if scope == "members":
            user_status = await client.get_chat_member(message.chat.id, message.from_user.id)
            if user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return

        await message.delete()
        if punishment == "mute":
            if chat_id not in muted_users:
                muted_users[chat_id] = []
            if message.from_user.id not in muted_users[chat_id]:
                muted_users[chat_id].append(message.from_user.id)
                locks["muted_users"] = muted_users
                save_locks(locks)
                await message.reply_text(f"◍ {message.from_user.mention} تم كتمك بسبب إرسال ملصقات.")
        elif punishment == "restrict":
            await client.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=False,
                    can_send_other_messages=False,
                    can_send_stickers=False
                ))
            await message.reply_text(f"◍ {message.from_user.mention} تم تقييدك بسبب إرسال ملصقات.")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب إرسال ملصقات.")
    except Exception as e:
        print(f"Error handling sticker: {e}")

# ################################################### الملصقات ############################################################
# ################################################### الصور ############################################################
# قفل الصور
@app.on_message(filters.regex("قفل الصور"), group=1211472)
async def lock_photos(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return

    if chat_id in photo_lock:
        current_punishment, current_scope = photo_lock[chat_id]
        await message.reply_text(
            f"⚠️ الصور مقفولة بالفعل\n"
            f"◍ العقوبة: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كتم", callback_data=f"ph_mute_{message.from_user.id}")],
        [InlineKeyboardButton("تقييد", callback_data=f"ph_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("طرد", callback_data=f"ph_ban_{message.from_user.id}")]
    ])
    await message.reply_text(
        f"◍ اختر نوع العقوبة لقفل الصور ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )


# اختيار نطاق العقوبة
@app.on_callback_query(filters.regex(r"^ph_(mute|restrict|ban)_(\d+)$"))
async def choose_photo_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[2])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(chat_id, user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action = callback_query.data.split('_')[1]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_ph_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_ph_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع\n"
        "- باستثناء المشرفين: تطبق على الأعضاء فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()


# تأكيد القفل
@app.on_callback_query(filters.regex(r"^confirm_ph_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_photo_lock(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[4])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(int(chat_id), user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]

    photo_lock[chat_id] = [action, scope]
    locks["photo_lock"] = photo_lock
    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم قفل الصور بنجاح\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط'}"
    )
    await callback_query.answer()


# فتح الصور
@app.on_message(filters.regex("فتح الصور"), group=1212474777)
async def unlock_photos(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return

    if chat_id not in photo_lock:
        await message.reply_text("⚠️ الصور غير مقفولة!")
        return

    del photo_lock[chat_id]
    locks["photo_lock"] = photo_lock
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح الصور بواسطة ↤︎「 {message.from_user.mention} 」")


# تنفيذ العقوبة
@app.on_message(filters.photo, group=121452474)
async def handle_photo_violation(client, message):
    chat_id = str(message.chat.id)
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
    if chat_id not in photo_lock:
        return

    if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id):
        return

    try:
        punishment, scope = photo_lock[chat_id]
        if scope == "members":
            user_status = await client.get_chat_member(message.chat.id, message.from_user.id)
            if user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return

        await message.delete()
        if punishment == "mute":
            if chat_id not in muted_users:
                muted_users[chat_id] = []
            if message.from_user.id not in muted_users[chat_id]:
                muted_users[chat_id].append(message.from_user.id)
                locks["muted_users"] = muted_users
                save_locks(locks)
                await message.reply_text(f"◍ {message.from_user.mention} تم كتمك بسبب إرسال صورة محظورة.")
        elif punishment == "restrict":
            await client.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=False,
                    can_send_other_messages=False
                )
            )
            await message.reply_text(f"◍ {message.from_user.mention} تم تقييدك بسبب إرسال صورة محظورة.")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب إرسال صورة محظورة.")
    except Exception as e:
        print(f"Error handling photo violation: {e}")



# ################################################### الصور ############################################################
# قفل الروابط
@app.on_message(filters.regex("قفل الروابط"), group=110111)
async def lock_links(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return

    if chat_id in link_lock:
        current_punishment, current_scope = link_lock[chat_id]
        await message.reply_text(
            f"⚠️ الروابط مقفولة بالفعل\n"
            f"◍ العقوبة: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كتم", callback_data=f"ln_mute_{message.from_user.id}")],
        [InlineKeyboardButton("تقييد", callback_data=f"ln_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("طرد", callback_data=f"ln_ban_{message.from_user.id}")]
    ])
    await message.reply_text(
        f"◍ اختر نوع العقوبة لقفل الروابط ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )


# اختيار نطاق العقوبة
@app.on_callback_query(filters.regex(r"^ln_(mute|restrict|ban)_(\d+)$"))
async def choose_link_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[2])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(chat_id, user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action = callback_query.data.split('_')[1]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_ln_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_ln_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع\n"
        "- باستثناء المشرفين: تطبق على الأعضاء فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()


# تأكيد القفل
@app.on_callback_query(filters.regex(r"^confirm_ln_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_link_lock(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[4])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(int(chat_id), user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]

    link_lock[chat_id] = [action, scope]
    locks["link_lock"] = link_lock
    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم قفل الروابط بنجاح\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط'}"
    )
    await callback_query.answer()


# فتح الروابط
@app.on_message(filters.regex("فتح الروابط"), group=110222)
async def unlock_links(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return

    if chat_id not in link_lock:
        await message.reply_text("⚠️ الروابط غير مقفولة!")
        return

    del link_lock[chat_id]
    locks["link_lock"] = link_lock
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح الروابط بواسطة ↤︎「 {message.from_user.mention} 」")


# تنفيذ العقوبة على الروابط
@app.on_message(filters.text, group=110333)
async def handle_link_violation(client, message):
    chat_id = str(message.chat.id)
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
    if chat_id not in link_lock:
        return

    if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id):
        return

    if any(link in message.text.lower() for link in ["http://", "https://", "www.", ".com", ".net", ".org", "t.me", "telegram.me"]):
        try:
            punishment, scope = link_lock[chat_id]
            if scope == "members":
                user_status = await client.get_chat_member(message.chat.id, message.from_user.id)
                if user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                    return

            await message.delete()
            if punishment == "mute":
                if chat_id not in muted_users:
                    muted_users[chat_id] = []
                if message.from_user.id not in muted_users[chat_id]:
                    muted_users[chat_id].append(message.from_user.id)
                    locks["muted_users"] = muted_users
                    save_locks(locks)
                    await message.reply_text(f"◍ {message.from_user.mention} تم كتمك بسبب إرسال رابط محظور.")
            elif punishment == "restrict":
                await client.restrict_chat_member(
                    message.chat.id,
                    message.from_user.id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=False,
                        can_send_other_messages=False
                    )
                )
                await message.reply_text(f"◍ {message.from_user.mention} تم تقييدك بسبب إرسال رابط محظور.")
            elif punishment == "ban":
                await client.ban_chat_member(message.chat.id, message.from_user.id)
                await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب إرسال رابط محظور.")
        except Exception as e:
            print(f"Error handling link violation: {e}")


# ###################################################  الروابط  ############################################################

# ###################################################  الحمايه  ############################################################
@app.on_message(filters.command(["قفل الحمايه"], ""), group=18798)
async def lock_protection(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text(f"◍ فقط المالك لديه الصلاحية ↤︎「 {message.from_user.mention} 」")
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كتم", callback_data=f"pr_mute_{message.from_user.id}")],
        [InlineKeyboardButton("تقييد", callback_data=f"pr_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("طرد", callback_data=f"pr_ban_{message.from_user.id}")]
    ])
    await message.reply_text(
        f"◍ اختر نوع العقوبة لقفل الحماية الشاملة ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex(r"^pr_(mute|restrict|ban)_(\d+)$"))
async def choose_protection_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[2])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return
    
    action = callback_query.data.split('_')[1]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"full_pr_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"full_pr_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق الحماية الشاملة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع\n"
        "- باستثناء المشرفين: تطبق على الأعضاء فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()


@app.on_callback_query(filters.regex(r"^full_pr_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_full_protection(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[4])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]
        
    locks_to_update = {
        "dardasha": [action, scope],
        "mutaharek": [action, scope],
        "channel_lock": [action, scope],
        "photo_lock": [action, scope],
        "videoo": [action, scope],
        "link_lock": [action, scope],
        "sticker_lock": [action, scope],
        "swear_lock": [action, scope],
        "mentionn": [action, scope],
        "tawgeh": [action, scope]
    }

    for lock_name, lock_value in locks_to_update.items():
        locks[lock_name][chat_id] = lock_value

    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم تفعيل الحماية الشاملة بنجاح\n\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط'}\n\n"
        f"◍ أنواع المحتوى المقفولة:\n"
        f"- السب والشتائم\n"
        f"- الروابط\n"
        f"- الرسائل من القنوات\n"
        f"- الصور\n"
        f"- الفيديوهات\n"
        f"- الملصقات\n"
        f"- التاغ والمنشن\n"
        f"- التوجيهات"
    )
    await callback_query.answer("✓ تم تفعيل الحماية الشاملة", show_alert=True)


@app.on_message(filters.command(["فتح الحمايه"], ""), group=545177)
async def unlock_protection(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text(f"◍ فقط المالك لديه الصلاحية ↤︎「 {message.from_user.mention} 」")
        return

    locks_to_remove = [
        "dardasha", "mutaharek", "channel_lock",
        "photo_lock", "videoo", "sticker_lock",
        "link_lock", "swear_lock", "tawgeh",
        "mentionn"
    ]

    for lock_name in locks_to_remove:
        if chat_id in locks[lock_name]:
            try:
                del locks[lock_name][chat_id]
            except Exception as e:
                pass

    save_locks(locks)
    await message.reply_text(
        f"◍ تم فتح الحماية الشاملة بنجاح\n"
        f"◍ بواسطة ↤︎「 {message.from_user.mention} 」\n\n"
        f"◍ أنواع المحتوى المفتوحة الآن:\n"
        f"- السب والشتائم\n"
        f"- الروابط\n"
        f"- الرسائل من القنوات\n"
        f"- الصور\n"
        f"- الفيديوهات\n"
        f"- الملصقات\n"
        f"- التاغ والمنشن\n"
        f"- التوجيهات"
    )
# ###################################################  الحمايه  ############################################################

# ###################################################  السب  ############################################################
swear_words = [
    "كسمك", "متناك", "احا", "متناكه", "شرموطه", "شمال", 
    "زب", "خول", "قحبه", "عرص", "معرص", "نيك", "متناك",
    "خخخ", "خخ", "خخخخ", "كس", "عير", "كحبه", "منيوك"
]

@app.on_message(filters.regex("قفل السب"), group=15989789)
async def lock_swearing(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return

    if chat_id in swear_lock:
        current_punishment, current_scope = swear_lock[chat_id]
        await message.reply_text(
            f"⚠️ السب مقفل بالفعل\n"
            f"◍ العقوبة: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كتم", callback_data=f"sw_mute_{message.from_user.id}")],
        [InlineKeyboardButton("تقييد", callback_data=f"sw_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("طرد", callback_data=f"sw_ban_{message.from_user.id}")]
    ])
    await message.reply_text(
        f"◍ اختر نوع العقوبة لقفل السب ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex(r"^sw_(mute|restrict|ban)_(\d+)$"))
async def choose_swear_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[2])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(chat_id, user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action = callback_query.data.split('_')[1]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_sw_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_sw_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع\n"
        "- باستثناء المشرفين: تطبق على الأعضاء فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()


@app.on_callback_query(filters.regex(r"^confirm_sw_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_swear_lock(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[4])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(int(chat_id), user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]

    swear_lock[chat_id] = [action, scope]
    locks["swear_lock"] = swear_lock
    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم قفل السب بنجاح\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط'}"
    )
    await callback_query.answer()


@app.on_message(filters.regex("فتح السب"), group=1212474)
async def unlock_swearing(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return

    if chat_id not in swear_lock:
        await message.reply_text("⚠️ السب غير مقفل!")
        return

    del swear_lock[chat_id]
    locks["swear_lock"] = swear_lock
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح السب بواسطة ↤︎「 {message.from_user.mention} 」")


@app.on_message(filters.text, group=56)
async def handle_swear_violation(client, message):
    chat_id = str(message.chat.id)
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
    if chat_id not in swear_lock:
        return
        
    if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id):
        return
    
    message_text = message.text.lower()
    if any(swear_word in message_text for swear_word in swear_words):
        try:
            punishment, scope = swear_lock[chat_id]
            if scope == "members":
                user_status = await client.get_chat_member(message.chat.id, message.from_user.id)
                if user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                    return

            await message.delete()
            if punishment == "mute":
                if chat_id not in muted_users:
                    muted_users[chat_id] = []
                if message.from_user.id not in muted_users[chat_id]:
                    muted_users[chat_id].append(message.from_user.id)
                    locks["muted_users"] = muted_users
                    save_locks(locks)
                    await message.reply_text(f"◍ {message.from_user.mention} تم كتمك بسبب السب!")
            elif punishment == "restrict":
                await client.restrict_chat_member(
                    message.chat.id,
                    message.from_user.id,
                    ChatPermissions(
                        can_send_messages=True,
                        can_send_media_messages=False,
                        can_send_other_messages=False
                    )
                )
                await message.reply_text(f"◍ {message.from_user.mention} تم تقييدك بسبب السب!")
            elif punishment == "ban":
                await client.ban_chat_member(message.chat.id, message.from_user.id)
                await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب السب!")
        except Exception as e:
            print(f"Error handling swear violation: {e}")


# ###################################################  السب  ###################################################
# ###################################################  الفنوات  ###################################################
@app.on_message(filters.regex("قفل القنوات"), group=1578878)
async def lock_channels(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return

    if chat_id in channel_lock:
        current_punishment, current_scope = channel_lock[chat_id]
        await message.reply_text(
            f"⚠️ القنوات مقفولة بالفعل\n"
            f"◍ العقوبة: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كتم", callback_data=f"ch_mute_{message.from_user.id}")],
        [InlineKeyboardButton("تقييد", callback_data=f"ch_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("طرد", callback_data=f"ch_ban_{message.from_user.id}")]
    ])
    await message.reply_text(
        f"◍ اختر نوع العقوبة لقفل القنوات ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex(r"^ch_(mute|restrict|ban)_(\d+)$"))
async def choose_channel_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[2])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(chat_id, user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action = callback_query.data.split('_')[1]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_ch_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_ch_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع\n"
        "- باستثناء المشرفين: تطبق على الأعضاء فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()


@app.on_callback_query(filters.regex(r"^confirm_ch_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_channel_lock(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[4])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    get = await client.get_chat_member(int(chat_id), user_id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        await callback_query.answer("لم تعد لديك الصلاحية!", show_alert=True)
        return

    action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]

    channel_lock[chat_id] = [action, scope]
    locks["channel_lock"] = channel_lock
    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم قفل القنوات بنجاح\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط'}"
    )
    await callback_query.answer()


@app.on_message(filters.regex("فتح القنوات"), group=87874)
async def unlock_channels(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return

    if chat_id not in channel_lock:
        await message.reply_text("⚠️ القنوات غير مقفولة!")
        return

    del channel_lock[chat_id]
    locks["channel_lock"] = channel_lock
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح القنوات بواسطة ↤︎「 {message.from_user.mention} 」")


@app.on_message(filters.text, group=5621175)
async def handle_channel_violation(client, message):
    chat_id = str(message.chat.id)
    
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
        
    if chat_id not in channel_lock:
        return

    if not message.sender_chat:
        return

    if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id):
        return

    try:
        punishment, scope = channel_lock[chat_id]
        if scope == "members":
            user_status = await client.get_chat_member(message.chat.id, message.from_user.id)
            if user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
                return

        await message.delete()
        if punishment == "mute":
            if chat_id not in muted_users:
                muted_users[chat_id] = []
            if message.from_user.id not in muted_users[chat_id]:
                muted_users[chat_id].append(message.from_user.id)
                locks["muted_users"] = muted_users
                save_locks(locks)
                await message.reply_text(f"◍ {message.sender_chat.title}، تم كتم القناة بسبب الإرسال هنا!")
        elif punishment == "restrict":
            await client.restrict_chat_member(
                message.chat.id,
                message.from_user.id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=False,
                    can_send_other_messages=False
                )
            )
            await message.reply_text(f"◍ {message.sender_chat.title}، تم تقييد القناة بسبب الإرسال هنا!")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ {message.sender_chat.title}، تم حظر القناة من المجموعة!")
    except Exception as e:
        print(f"Error handling channel violation: {e}")
####################################################  القنوات  ###################################################
@app.on_message(filters.command(["حماية", "الحمايه", "الحماية"], ""), group=5451)
async def protection_menu(client, message):
    global mid
    mid = message.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id not in [*dev, OWNER_ID, sourse_dev]:
        await message.reply_text(f"عذراً عزيزي {message.from_user.mention} \nليس لديك صلاحية")
        return

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("إعدادات الحماية", callback_data=f"hemm {message.from_user.id}")],
        [InlineKeyboardButton("إغلاق", callback_data=f"close {message.from_user.id}")],
    ])
    
    await message.reply_text(
        f"**الإعــدادات**\n\n"
        f"◍ المجموعة: {message.chat.title}\n"
        f"◍ ايدي المجموعة: `{message.chat.id}`\n"
        f"◍ معرف المجموعة: @{message.chat.username if message.chat.username else 'لا يوجد'}\n\n"
        f"اختر ما تريد من الخيارات أدناه:",
        reply_markup=keyboard
    )

@app.on_message(filters.command(["حماية", "الحمايه", "الحماية"], ""), group=5451)
async def protection_menu(client, message):
    try:
        global mid
        mid = message.id
        
        # التحقق من الاشتراك
        is_subscribed = await checkg_member_status(message.from_user.id, message, client)
        if not is_subscribed:
            return False
        
        # التحقق من الصلاحيات
        get = await client.get_chat_member(message.chat.id, message.from_user.id)
        allowed_users = [*dev, OWNER_ID, sourse_dev]
        if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id not in allowed_users:
            await message.reply_text(f"عذراً {message.from_user.mention}، ليس لديك الصلاحية")
            return

        # إنشاء لوحة المفاتيح
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("إعدادات الحماية", callback_data=f"hemm {message.from_user.id}")],
            [InlineKeyboardButton("إغلاق", callback_data=f"close {message.from_user.id}")]
        ])
        
        # إرسال رسالة القائمة الرئيسية
        chat_info = f"""
        **الإعــدادات**

        ◍ المجموعة: {message.chat.title}
        ◍ ايدي المجموعة: `{message.chat.id}`
        ◍ معرف المجموعة: @{message.chat.username if message.chat.username else 'لا يوجد'}

        اختر ما تريد من الخيارات أدناه:
        """
        await message.reply_text(chat_info, reply_markup=keyboard)
        
    except Exception as e:
        print(f"Error in protection_menu: {str(e)}")
        await message.reply_text("حدث خطأ أثناء تحميل القائمة، يرجى المحاولة لاحقاً")


# تعريف أسماء أنواع القفل
LOCK_NAMES = {
    'dardasha': 'الدارشة',
    'mutaharek': 'المتحركات',
    'videoo': 'الفيديو',
    'mentionn': 'المنشن',
    'tawgeh': 'التوجيه',
    'channel_lock': 'القنوات',
    'link_lock': 'الروابط',
    'photo_lock': 'الصور',
    'sticker_lock': 'الملصقات',
    'swear_lock': 'السب'
}

@app.on_callback_query(filters.regex("^hemm (\\d+)$"))
async def protection_settings(client, q: CallbackQuery):
    try:
        user_id = int(q.matches[0].group(1))
        if user_id != q.from_user.id:
            return await q.answer("⚠️ ليس لديك الصلاحية!", show_alert=True)
        
        # إنشاء أزرار لأنواع الحماية
        buttons = []
        for lock_id, lock_name in LOCK_NAMES.items():
            lock_var = globals().get(lock_id, {})
            chat_id = str(q.message.chat.id)
            status = "✓" if chat_id in lock_var else "✗"
            
            if chat_id in lock_var:
                punishment, scope = lock_var[chat_id]
                btn_text = f"{lock_name} ({punishment}) {status}"
                callback_data = f"unlock_{lock_id}_{user_id}"
            else:
                btn_text = f"{lock_name} {status}"
                callback_data = f"lock_{lock_id}_{user_id}"
            
            buttons.append([InlineKeyboardButton(btn_text, callback_data=callback_data)])
        
        # إضافة زر الرجوع
        buttons.append([InlineKeyboardButton("↩️ رجوع", callback_data=f"back_main_{user_id}")])
        
        # تحرير الرسالة مع الأزرار الجديدة
        await q.message.edit_text(
            "**إعدادات الحماية:**\n\n"
            "◍ ✓ تعني أن الحماية مفعلة\n"
            "◍ ✗ تعني أن الحماية غير مفعلة\n\n"
            "اختر نوع الحماية الذي تريد تعديله:",
            reply_markup=InlineKeyboardMarkup(buttons)
        )
            
    except Exception as e:
        print(f"Error in protection_settings: {str(e)}")
        await q.answer("حدث خطأ أثناء تحميل الإعدادات", show_alert=True)


@app.on_callback_query(filters.regex("^lock_(\\w+)_(\\d+)$"))
async def lock_item_menu(client, q: CallbackQuery):
    try:
        lock_id = q.matches[0].group(1)
        user_id = int(q.matches[0].group(2))
        
        if user_id != q.from_user.id:
            return await q.answer("⚠️ ليس لديك الصلاحية!", show_alert=True)
            
        lock_name = LOCK_NAMES.get(lock_id, lock_id)
        
        # إنشاء أزرار خيارات العقوبة (كلها تدعم النطاق في هذا الإصدار)
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("كتم", callback_data=f"set_mute_{lock_id}_{user_id}")],
            [InlineKeyboardButton("تقييد", callback_data=f"set_restrict_{lock_id}_{user_id}")],
            [InlineKeyboardButton("طرد", callback_data=f"set_ban_{lock_id}_{user_id}")],
            [InlineKeyboardButton("↩️ رجوع", callback_data=f"hemm {user_id}")]
        ])
        
        # تحرير الرسالة مع خيارات العقوبة
        await q.message.edit_text(
            f"**إعدادات قفل {lock_name}:**\n\n"
            "اختر طريقة العقاب المطلوبة:",
            reply_markup=keyboard
        )
        
    except Exception as e:
        print(f"Error in lock_item_menu: {str(e)}")
        await q.answer("حدث خطأ أثناء تحميل الخيارات", show_alert=True)


@app.on_callback_query(filters.regex("^unlock_(\\w+)_(\\d+)$"))
async def unlock_item(client, q: CallbackQuery):
    try:
        lock_id = q.matches[0].group(1)
        user_id = int(q.matches[0].group(2))
        chat_id = str(q.message.chat.id)
        
        if user_id != q.from_user.id:
            return await q.answer("⚠️ ليس لديك الصلاحية!", show_alert=True)
            
        lock_var = globals().get(lock_id)
        if lock_var is None:
            return await q.answer("⚠️ نوع الحماية غير معروف!", show_alert=True)
            
        # إزالة القفل إذا كان موجوداً
        if chat_id in lock_var:
            del lock_var[chat_id]
            save_locks(locks)  # حفظ التغييرات
            
        await q.answer(f"✓ تم فتح {LOCK_NAMES.get(lock_id, lock_id)}", show_alert=True)
        await protection_settings(client, q)
        
    except Exception as e:
        print(f"Error in unlock_item: {str(e)}")
        await q.answer("حدث خطأ أثناء فتح الحماية", show_alert=True)


@app.on_callback_query(filters.regex("^set_(mute|restrict|ban)_(\\w+)_(\\d+)$"))
async def set_punishment(client, q: CallbackQuery):
    try:
        punishment = q.matches[0].group(1)
        lock_id = q.matches[0].group(2)
        user_id = int(q.matches[0].group(3))
        
        if user_id != q.from_user.id:
            return await q.answer("⚠️ ليس لديك الصلاحية!", show_alert=True)
            
        lock_var = globals().get(lock_id)
        if lock_var is None:
            return await q.answer("⚠️ نوع الحماية غير معروف!", show_alert=True)
        
        # عرض خيارات النطاق
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("الكل (بما فيهم المشرفين)", callback_data=f"confirm_{lock_id}_{punishment}_all_{user_id}")],
            [InlineKeyboardButton("الأعضاء فقط", callback_data=f"confirm_{lock_id}_{punishment}_members_{user_id}")],
            [InlineKeyboardButton("↩️ رجوع", callback_data=f"lock_{lock_id}_{user_id}")]
        ])
        
        await q.message.edit_text(
            f"**اختر نطاق تطبيق العقوبة:**\n\n"
            f"◍ العقوبة: {punishment}\n"
            f"◍ النوع: {LOCK_NAMES.get(lock_id, lock_id)}\n\n"
            "اختر نطاق العقوبة:",
            reply_markup=keyboard
        )
            
    except Exception as e:
        print(f"Error in set_punishment: {str(e)}")
        await q.answer("حدث خطأ أثناء تعيين العقوبة", show_alert=True)


@app.on_callback_query(filters.regex("^confirm_(\\w+)_(mute|restrict|ban)_(all|members)_(\\d+)$"))
async def confirm_lock_settings(client, q: CallbackQuery):
    try:
        lock_id = q.matches[0].group(1)
        punishment = q.matches[0].group(2)
        scope = q.matches[0].group(3)
        user_id = int(q.matches[0].group(4))
        chat_id = str(q.message.chat.id)
        
        if user_id != q.from_user.id:
            return await q.answer("⚠️ ليس لديك الصلاحية!", show_alert=True)
            
        lock_var = globals().get(lock_id)
        if lock_var is None:
            return await q.answer("⚠️ نوع الحماية غير معروف!", show_alert=True)
        
        # تطبيق الإعدادات
        lock_var[chat_id] = [punishment, scope]
        save_locks(locks)  # حفظ التغييرات
        
        # إرسال تأكيد للمستخدم
        await q.answer(
            f"✓ تم تفعيل {LOCK_NAMES.get(lock_id, lock_id)}\n"
            f"◍ العقوبة: {punishment}\n"
            f"◍ النطاق: {'الكل' if scope == 'all' else 'الأعضاء فقط'}",
            show_alert=True
        )
        
        # العودة إلى قائمة الإعدادات
        await protection_settings(client, q)
        
    except Exception as e:
        print(f"Error in confirm_lock_settings: {str(e)}")
        await q.answer("حدث خطأ أثناء تأكيد الإعدادات", show_alert=True)

# القائمة الرئيسية
@app.on_callback_query(filters.regex("^back_main_(\\d+)$"))
async def back_to_main(client, q: CallbackQuery):
    try:
        user_id = int(q.matches[0].group(1))
        if user_id != q.from_user.id:
            return await q.answer("⚠️ ليس لديك الصلاحية!", show_alert=True)
            
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton("إعدادات الحماية", callback_data=f"hemm {user_id}")],
            [InlineKeyboardButton("إغلاق", callback_data=f"close {user_id}")],
        ])
        
        await q.message.edit_text(
            f"**الإعــدادات**\n\n"
            f"◍ المجموعة: {q.message.chat.title}\n"
            f"◍ ايدي المجموعة: `{q.message.chat.id}`\n"
            f"◍ معرف المجموعة: @{q.message.chat.username if q.message.chat.username else 'لا يوجد'}\n\n"
            f"اختر ما تريد من الخيارات أدناه:",
            reply_markup=keyboard
        )
    except Exception as e:
        print(f"Error in back_to_main: {e}")
        await q.answer("حدث خطأ أثناء العودة للقائمة", show_alert=True)


# إغلاق القائمة
@app.on_callback_query(filters.regex("^close_(\\d+)$"))
async def close_menu(client, q: CallbackQuery):
    try:
        user_id = int(q.matches[0].group(1))
        if user_id == q.from_user.id:
            await q.message.delete()
    except Exception as e:
        print(f"Error in close_menu: {e}")
###################################### القفل والفتح ################################################

@app.on_message(filters.command(["مين ضافني"], ""), group=725458)
@app.on_message(filters.new_chat_members)
async def get_invited_by(client, message):
    try:
        invited_users = message.new_chat_members
        for user in invited_users:
            inviter = user.invited_by
            if inviter is None:
                continue
            inviter_name = f"{inviter.first_name}" if inviter.last_name else inviter.first_name
            await message.reply_text(f"الشخص الذي قام بدعوتك هو: {inviter_name}")
    except Exception as e:
        pass

@app.on_message(filters.command(["وقت الانضمام"], ""), group=727272786667)
async def jointime(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    chat_id = message.chat.id
    user = await client.get_chat_member(chat_id, user_id)
    join_date = user.joined_date.timestamp()
    join_time = datetime.utcfromtimestamp(join_date).strftime('%Y-%m-%d %H:%M:%S')
    await message.reply_text(f"الوقت الذي انضممت فيه للمجموعة: {join_time}")

@app.on_message(filters.command(["مين رفعني"], ""), group=75452)
async def get_promoted_by(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    member = await client.get_chat_member(chat_id, user_id)  
    if member.promoted_by:
        promoted_by = member.promoted_by.first_name
        await message.reply_text(f"تم رفعك مشرف بواسطة : {promoted_by}")
    else:
        await message.reply_text("مفيش حد رفعك مشرف للاسف ✨♥")
     


@app.on_message(filters.regex(r'تغير الاسم'), group=713000)
async def set_namde(client, message):     
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == OWNER_ID or message.from_user.id == 6473057664:
        ask = await app.ask(message.chat.id, "حسنا قوم بارسال الاسم الجديد", filters=filters.user(message.from_user.id), timeout=300)
        text = ask.text
        try:
            await client.set_chat_title(message.chat.id, text)
            await message.reply_text("تم تغيير اسم الجروب بنجاح ")   
        except Exception as e:
            await message.reply_text(f"حدث خطأ في تغيير الاسم: {str(e)}")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص مالك الجروب فقط ✨♥")
      
        
@app.on_message(filters.regex(r'تغير الاسم') & filters.channel, group=7798897130)
async def set_namde(client, message):   
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False   
    ask = await app.ask(message.chat.id, "حسنا قوم بارسال الاسم الجديد", filters=filters.user(message.from_user.id), timeout=300)
    text = ask.text
    try:
        await client.set_chat_title(message.chat.id, text)
        await message.reply_text("تم تغيير اسم القناة بنجاح ")   
    except Exception as e:
        await message.reply_text(f"خطا في تغيير الاسم: {str(e)}")
        
        
@app.on_message(filters.regex(r'تغير البايو') & filters.group, group=712312330)
async def set_nme(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == OWNER_ID or message.from_user.id == 6473057664:
        ask = await app.ask(message.chat.id, "حسنا قوم بارسال البايو الجديد", filters=filters.user(message.from_user.id), timeout=300)
        text = ask.text
        try:
            await client.set_chat_description(message.chat.id, text)
            await message.reply_text("تم تغيير بايو الجروب بنجاح!")
        except Exception as e:
            await message.reply_text(f"حدث خطأ في تغيير الاسم: {str(e)}")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص مالك الجروب فقط ✨♥")

@app.on_message(filters.regex(r'تغير الصوره') & filters.group, group=74654130)
async def set_nme(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER] or message.from_user.id == OWNER_ID or message.from_user.id == 6473057664:
        ask = await app.ask(message.chat.id, "حسنًا، قم بإرسال الصورة", filters=filters.user(message.from_user.id), timeout=300)
        photo = ask.photo
        photo = await client.download_media(photo)
        try:
            await client.set_chat_photo(message.chat.id, photo=photo)
            await message.reply_text("تم تغيير صورة الجروب بنجاح")
        except Exception as e:
            await message.reply_text(f"حدث خطأ في تغيير الصورة: {str(e)}")
    else:
        return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر يخص مالك الجروب فقط ✨♥")


@app.on_message(filters.regex(r'تغير البايو') & filters.channel, group=779977130)
async def set_nahme(client, message):  
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    ask = await app.ask(message.chat.id, "حسنا قوم بارسال البايو الجديد", filters=filters.user(message.from_user.id), timeout=300)
    text = ask.text
    try:
        await client.set_chat_description(message.chat.id, text)
        await message.reply_text("تم تغيير بايو القناة بنجاح!")
    except Exception as e:
        await message.reply_text(f"خطا في تغيير الاسم: {str(e)}")

@app.on_message(filters.new_chat_photo)
async def source_devvarphoto(client, message):
    chat_id = message.chat.id
    photo = await client.download_media(message.chat.photo.big_file_id)
    await client.send_photo(chat_id=chat_id, photo=photo, caption=f"حلوه صوره الجروب الجديده \n الشخص الي غيرها ده : {message.from_user.mention}")
    
@app.on_message(filters.new_chat_title)
async def source_devvarphoto(client, message):
    await client.send_message(message.chat.id, f"حلو اسم جروب الجديد \n\n الشخص الي غيره ده :\n[{message.from_user.mention}] \n الاسم الجديد للجروب :\n[{message.chat.title}]  ") 
    
@app.on_message(filters.regex(r'تغير الصوره') & filters.channel, group=71889789730)
async def set_nme(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    ask = await app.ask(message.chat.id, "حسنًا، قم بإرسال الصورة", filters=filters.user(message.from_user.id), timeout=300)
    photo = ask.photo
    photo = await client.download_media(photo)
    try:
        await client.set_chat_photo(message.chat.id, photo=photo)
        await message.reply_text("تم تغيير صورة القناه بنجاح")
    except Exception as e:
        await message.reply_text(f"حدث خطأ في تغيير الصورة: {str(e)}")
        
@app.on_message(filters.command(["معلوماته","كشف"], ""), group=1025554)
async def kashf(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user = await client.get_users(message.reply_to_message.from_user.id)
    name = user.first_name
    user_id = message.reply_to_message.from_user.id
    chat_idd = message.chat.id
    chat_username = f"@{message.chat.username}" 
    chat_name = message.chat.title
    username = f"@{message.reply_to_message.from_user.username}"
    CASER = await client.get_chat(message.reply_to_message.from_user.id)
    bioo = CASER.bio
    source_devvar = await client.get_chat(message.reply_to_message.from_user.id)
    photo = source_devvar.photo.big_file_id
    photo = await client.download_media(photo)
    await message.reply_photo( 
    photo=photo,
    caption=f"❤ ¦ ɴᴀᴍᴇ : {message.reply_to_message.from_user.mention}\n🥰 ¦ ᴜѕᴇ : {username}\n🔥 ¦ ɪᴅ : {user_id}\n♥¦ ɪᴅ ᥇𝓲ꪮꪮ : {bioo}\n😎 ¦ ɪᴅ ᴄʜᴀᴛ : {chat_idd}\n☠️ ¦ ᴄʜᴀᴛ : {chat_name}\n💕 ¦ ɢʀᴏᴜᴘ : {chat_username}\n",
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(name, url=f"https://t.me/{message.reply_to_message.from_user.username}")]]))


@app.on_message(filters.group & filters.regex(r"^مسح(?:\s(\d+))?$"), group=71300212878)
async def delete_message(client: Client, message: Message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return
    
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and message.from_user.id not in [OWNER_ID, 6473057664]:
        await message.reply_text(f"عذرًا {message.from_user.mention}, هذا الأمر للمشرفين فقط.")
        return
    try:
        match = message.matches[0]
        count = int(match.group(1)) if match.group(1) else 1
        messages_to_delete = []

        if message.reply_to_message:
            await message.delete()
            await app.delete_messages(message.chat.id, [message.reply_to_message.id, message.id])
            await message.reply_text(f"تم حذف رسالة هذا الشخص {message.from_user.mention} بنجاح ✨✅")
        else:
            if count == 1:
                await message.reply_text("يجب الرد على رسالة لحذفها.")
                return
            async for msg in user.get_chat_history(message.chat.id, limit=count):
                messages_to_delete.append(msg.id)
        messages_to_delete.append(message.id)
        await client.delete_messages(message.chat.id, messages_to_delete)
        if count == 1 and message.reply_to_message:
            await client.send_message(message.chat.id, "✓ تم حذف الرسالة المحددة.")
        else:
            await client.send_message(message.chat.id, f"✓ تم حذف {len(messages_to_delete) - 1} رسالة.")
    except Exception as e:
        pass
    

@app.on_message(filters.command(["طرد البوتات"], "") & filters.group, group=50789787)
async def ban_bots(client: Client, message: Message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and message.from_user.id != 6473057664:
        return
    
    count = 0
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
        if member.user.is_bot:
            try:
                await client.ban_chat_member(message.chat.id, member.user.id)
                count += 1
            except Exception as e:
                print(f"Error banning bot: {e}")
    
    if count > 0:
        await message.reply_text(f"تم طرد {count} بوت بنجاح✅♥")
    else:
        await message.reply_text("لا توجد بوتات لطردها.")

@app.on_message(filters.command(["البوتات"], "") & filters.group, group=644585)
async def list_bots(client: Client, message: Message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    bot_usernames = []
    count = 0 
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
        if member.user.is_bot:
            bot_usernames.append("@" + member.user.username)
            count += 1

    if count > 0:
        bot_list = "\n".join(bot_usernames)
        await message.reply_text(f"عدد البوتات في المجموعة: {count} \n يوزرات البوتات: {bot_list}")
    else:
        await message.reply_text("لا يوجد بوتات في المجموعة.")
  
@app.on_message(filters.command(["المشرفين"], "") & filters.group, group=5454)
async def list_administrators(client: Client, message: Message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.chat.id
    admin_usernames = []
    count = 0
    async for member in client.get_chat_members(message.chat.id):
        if member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            if member.user.username:
                admin_usernames.append("@" + member.user.username)
            else:
                admin_usernames.append(member.user.first_name)
            count += 1

    if count > 0:
        admin_list = "\n".join(filter(None, admin_usernames))
        await message.reply_text(f"عدد المشرفين في المجموعة: {count} \n يوزرات المشرفين: {admin_list}")
    else:
        await message.reply_text("لا يوجد مشرفين في المجموعة.")
  
@app.on_message(filters.command(["الحسابات المحذوفه"], "") & filters.group, group=5)
async def list_bots(client: Client, message: Message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
        return
    count = 0 
    async for member in client.get_chat_members(message.chat.id):
        if member.user.is_deleted:
            count += 1

    if count > 0:
        await message.reply_text(f"عدد الأعضاء الذين لديهم حسابات محذوفة في المجموعة: {count}")
    else:
        await message.reply_text("لا يوجد أعضاء لديهم حسابات محذوفة في المجموعة.")

@app.on_message(filters.command(["الغاء تثبيت","غ ث"], ""), group=77723) 
async def unpin_message(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6473057664:
        chat_id = message.chat.id
        reply_msg_id = message.reply_to_message_id  
        try:
            await client.unpin_chat_message(chat_id, message_id=reply_msg_id) 
            await message.reply_text("تم إلغاء تثبيت الرسالة بنجاح✅♥")
        except Exception as e:
            print(e)
            await message.reply_text("حدث خطأ أثناء إلغاء تثبيت الرسالة")
    else:
        await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(filters.command(["تثبيت", "ث"], ""), group=733) 
async def pin_message(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == 6473057664:
        chat_id = message.chat.id
        reply_msg_id = message.reply_to_message_id
        try:
            await client.pin_chat_message(chat_id, reply_msg_id)
            await message.reply_text("تم تثبيت الرسالة بنجاح✅♥")
        except Exception as e:
            print(e)
            await message.reply_text("حدث خطأ أثناء تثبيت الرسالة.")
    else:
        await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")


@app.on_message(filters.command(["اطردني"], ""), group=222668)
async def fire_user(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton("نعم", callback_data="confirm_kick"), InlineKeyboardButton("لا", callback_data="cancel_kick")],])
    await message.reply_text("هل أنت متأكد أنك تريد أن أقوم بطردك من الدردشة؟", reply_markup=keyboard)

@app.on_callback_query(filters.regex("^cancel_kick"))
async def handle_cancel_kick(client, callback_query):
    await callback_query.message.edit_text("تم إلغاء طلب الطرد. سعداء بأنك ستبقى معنا!")

@app.on_callback_query(filters.regex("^confirm_kick"))
async def handle_confirm_kick(client, callback_query):
    await client.ban_chat_member(callback_query.message.chat.id, callback_query.from_user.id)
    await callback_query.message.edit_text("تم طردك بنجاح. إذا كنت بحاجة للبقاء، فأهلاً بك دائمًا!")


ahmed = {}
tom_max = 3
@app.on_message(filters.command("انذار", ""), group=586873) 
async def tom(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
    usr = await client.get_users(message.reply_to_message.from_user.id)
    name = usr.first_name 
    username = f"@{message.reply_to_message.from_user.username}"
    me = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id
    if chat_id not in ahmed:
        ahmed[chat_id] = {}
    if user_id not in ahmed[chat_id]:
        ahmed[chat_id][user_id] = 1
    else:
        ahmed[chat_id][user_id] += 1
    await message.reply_text(f"◍ المستخدم ←{username} \n※ تم اعطاءه {ahmed[chat_id][user_id]} انذار من اصل 3")
    if ahmed[chat_id][user_id] >= tom_max:
        try:
         del ahmed[chat_id][user_id]
         await client.ban_chat_member(chat_id, user_id)
         await message.reply("تم طرد العضو")    
        except:
         await message.reply("مش عارف اطردو")    
#################################################### الدردشه ############################################################
#################################################### كتم وحظر وتقييد ############################################################

@app.on_message(filters.command(["كتم"], ""), group=394578)
async def mute_user_name(client, message):
    global muted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    chat_member = await client.get_chat_member(chat_id, message.from_user.id)
    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == zombie_id:
        if not message.reply_to_message and not message.text:
            await message.reply_text("قم بإرسال الأمر مع اسم المستخدم الذي ترغب في كتمه.")
            return
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            user_mention = message.reply_to_message.from_user.mention
        else:
            username = message.text.split(" ", 1)[1]
            user = await client.get_users(username)
            user_id = user.id 
            user_mention = user.mention()
        if user_id == zombie_id:
            await message.reply_text(f"عيب اقدع ده المبرمج محمد صالح 🥷")
            return
        if user_id == OWNER_ID:
            await message.reply_text("◍ عذرآ لا تستطيع استخدام الأمر على مطور البوت")
            return 
        target_member = await client.get_chat_member(chat_id, user_id)

        if target_member.status == ChatMemberStatus.OWNER:
            await message.reply_text("**مالك الجروب يجدع مقدرش عيب 🚧**")
            return
        
        if target_member.status == ChatMemberStatus.ADMINISTRATOR:
            await message.reply_text("**الادمن يجدع مقدرش عيب 👮‍♂️**")
            return
        
        chat_id = str(message.chat.id)
        if chat_id not in muted_users:
            muted_users[chat_id] = []    
        if user_id not in muted_users[chat_id]:
            muted_users[chat_id].append(user_id)
            locks["muted_users"] = muted_users
            save_locks(locks)
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ الغاء الكتم", callback_data=f"unbanrep {message.from_user.id} {user_id}")]
            ])
            await message.reply_animation("https://t.me/uu_u_e/6", caption=f"تم كتم العضو {user_mention} بنجاح.", reply_markup=keyboard)
        else:
            await message.reply_text("المستخدم مكتوم بالفعل.")
    else:
        await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**.")        

@app.on_callback_query(filters.regex("^unbanrep (\\d+) (\\d+)$"))
async def unmute_user(client: Client, callback_query: CallbackQuery):
    data = callback_query.data.split(" ")
    admin_id = int(data[1])
    user_id = int(data[2])
    if callback_query.from_user.id != admin_id:
        await callback_query.answer("صاحب الأمر هو فقط من يستطيع الضغط على الزر 🥷", show_alert=True)
        return

    chat_id = str(callback_query.message.chat.id)
    if chat_id in muted_users and user_id in muted_users[chat_id]:
        muted_users[chat_id].remove(user_id)
        await callback_query.message.edit_text("✅ تم إلغاء الكتم بنجاح.")


@app.on_message(filters.command(["الغاء الكتم", "الغاء كتم"], ""), group=62)
async def unmute_user(client, message):
    global muted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    chat_member = await client.get_chat_member(chat_id, message.from_user.id)
    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == zombie_id:
        chat_id = str(message.chat.id)
        if chat_id not in muted_users:
            muted_users[chat_id] = []
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            user_mention = message.reply_to_message.from_user.mention
        else:
            username = message.text.split(" ", 2)[2]
            user = await client.get_users(username)
            user_id = user.id
            user_mention = user.mention()
        if user_id in muted_users[chat_id]:
            muted_users[chat_id].remove(user_id)
            if user_mention:
                await message.reply_text(f"تم الغاء كتم المستخدم {user_mention}")
        else:
            await message.reply_text("المستخدم غير مكتوم.")
    else:
        await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**.")  

@app.on_message(filters.text, group=1548578)
async def handle_mssage(client, message):
    global muted_users
    if message.from_user.id in {OWNER_ID, sourse_dev, zombie_id}:
        return
    chat_id = str(message.chat.id)
    if chat_id in muted_users and message.from_user.id in muted_users[chat_id]:
        await client.delete_messages(chat_id=chat_id, message_ids=message.id)

@app.on_message(filters.command(["المكتومين"], ""), group=137)
async def get_rmuted_users(client, message):
    global muted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = str(message.chat.id)
    if chat_id in muted_users:
        count = len(muted_users[chat_id])
        user_mentions = [str(user) for user in muted_users[chat_id]]
        response = f"⌔ قائمة المكتومين وعددهم : {count}\n"
        response += "\n".join(user_mentions)
        await message.reply_text(response)



######################################################## حظر عام ####################################################
from datetime import datetime

collection_global_ban = db[f"global_bans_{BOT_USERNAME}"]

def ban_user_globally(admin_id, user_id):
    if not collection_global_ban.find_one({"user_id": user_id}):
        collection_global_ban.insert_one({
            "user_id": user_id,
            "banned_by": admin_id,
            "timestamp": datetime.now()
        })

def unban_user_globally(user_id):
    collection_global_ban.delete_one({"user_id": user_id})

def is_user_banned(user_id):
    return collection_global_ban.find_one({"user_id": user_id})

def get_banned_users():
    return [
        {
            "user_id": doc["user_id"],
            "banned_by": doc.get("banned_by"),
            "timestamp": doc.get("timestamp")
        }
        for doc in collection_global_ban.find()
    ]

def clear_banned_users():
    collection_global_ban.delete_many({})

@app.on_message(filters.regex(r"^مسح المحظورين عام$"), group=41084451312)
async def clear_banned_list(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return

    clear_banned_users()    
    await message.reply("✅ تم مسح جميع المحظورين عام بنجاح.")

@app.on_message(filters.regex(r"^(حظر عام 📛|حظر عام)$"), group=48451315782)
async def global_ban(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return

    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        ask = await client.ask(message.chat.id, "**📝 أرسل الآن يوزر أو آيدي المستخدم الذي تريد حظره**", filters=filters.user(message.from_user.id), timeout=60)
        try:
            user_input = ask.text.strip().replace("@", "")
            target_user = await client.get_users(user_input)
        except Exception:
            return await ask.reply("❌ لم أتمكن من العثور على المستخدم. تأكد من صحة اليوزر أو الآيدي.")
    
    confirm_buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ تأكيد الحظر", callback_data=f"confirm_ban_{target_user.id}"),
            InlineKeyboardButton("❌ إلغاء", callback_data="cancel_ban")
        ]
    ])
    await message.reply(
        f"⚠️ هل أنت متأكد من حظر {target_user.mention} عام؟",
        reply_markup=confirm_buttons
    )

@app.on_callback_query(filters.regex("^confirm_ban_"))
async def confirm_ban(client, callback):
    user_id = int(callback.data.split("_")[2])
    ban_user_globally(callback.from_user.id, user_id)
    await callback.message.edit_text(
        f"**◍ تم حظر المستخدم عام\n√**"
    )

@app.on_callback_query(filters.regex("^cancel_ban$"))
async def cancel_ban(client, callback):
    await callback.message.edit_text("✅ تم إلغاء عملية الحظر.")

@app.on_message(filters.regex(r"^(الغاء حظر عام 🛑|الغاء حظر عام)$"), group=145918312)
async def global_unban(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        ask = await client.ask(message.chat.id, "**📝 أرسل الآن يوزر أو آيدي المستخدم الذي تريد حظره**", filters=filters.user(message.from_user.id), timeout=60)
        try:
            user_input = ask.text.strip().replace("@", "")
            target_user = await client.get_users(user_input)
        except Exception:
            return await ask.reply("❌ لم أتمكن من العثور على المستخدم. تأكد من صحة اليوزر أو الآيدي.")
    if not is_user_banned(target_user.id):
        return await message.reply("ℹ️ هذا المستخدم غير محظور عام.")
    unban_user_globally(target_user.id)
    await message.reply(f"**◍ تم الغاء حظر المستخدم عام\n√**")

@app.on_message(filters.regex(r"^(المحظورين عام|المحظورين عام 🙅🏻‍♂️)$"), group=41084451312)
async def banned_list(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return
    
    bans = get_banned_users()
    if not bans:
        return await message.reply("ℹ️ لا يوجد مستخدمين محظورين حالياً.")
    
    text = "📋 قائمة المحظورين عام:\n\n"
    
    for ban in bans:
        user_id = ban["user_id"]
        banned_by = ban["banned_by"]
        timestamp = ban["timestamp"]
        
        try:
            banned_user = await client.get_users(user_id)
            banned_username = f"@{banned_user.username}" if banned_user.username else "لا يوجد يوزر"
            admin_user = await client.get_users(banned_by)
            admin_username = f"@{admin_user.username}" if admin_user.username else str(admin_user.id)
            text += (
                f"👤 المستخدم: {banned_username} (ID: {user_id})\n"
                f"👮 تم الحظر بواسطة: {admin_username}\n"
                f"📅 التاريخ: {timestamp.strftime('%Y-%m-%d %H:%M') if isinstance(timestamp, datetime) else 'غير معروف'}\n"
                "━━━━━━━━━━━━━━\n"
            )
        except Exception as e:
            text += (
                f"👤 المستخدم: ID: {user_id} (لم يتم العثور على معلوماته)\n"
                f"👮 تم الحظر بواسطة: {banned_by}\n"
                f"📅 التاريخ: {timestamp.strftime('%Y-%m-%d %H:%M') if isinstance(timestamp, datetime) else 'غير معروف'}\n"
                "━━━━━━━━━━━━━━\n"
            )
    await message.reply(text)

######################################################## حظر عام ####################################################
######################################################## كتم عام ####################################################
######################################################## كتم عام ####################################################
collection_global_mute = db[f"global_mutes_{BOT_USERNAME}"]

def mute_user_globally(admin_id, user_id):
    if not collection_global_mute.find_one({"user_id": user_id}):
        collection_global_mute.insert_one({
            "user_id": user_id,
            "muted_by": admin_id,
            "timestamp": datetime.now()
        })

def unmute_user_globally(user_id):
    collection_global_mute.delete_one({"user_id": user_id})

def is_user_muted(user_id):
    return collection_global_mute.find_one({"user_id": user_id})

def get_muted_users():
    return [
        {
            "user_id": doc["user_id"],
            "muted_by": doc.get("muted_by"),
            "timestamp": doc.get("timestamp")
        }
        for doc in collection_global_mute.find()
    ]

def clear_muted_users():
    collection_global_mute.delete_many({})

@app.on_message(filters.regex(r"^مسح المكتومين عام$"), group=6981312)
async def clear_muted_list(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return

    clear_muted_users()    
    await message.reply("✅ تم مسح جميع المكتومين عام بنجاح.")

@app.on_message(filters.regex(r"^كتم عام 🔕$") & filters.private, group=411315782)
async def global_mute(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return

    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        ask = await client.ask(message.chat.id, "📝 أرسل الآن يوزر أو آيدي المستخدم الذي تريد كتمه:", filters=filters.user(message.from_user.id), timeout=60)
        try:
            user_input = ask.text.strip().replace("@", "")
            target_user = await client.get_users(user_input)
        except Exception:
            return await ask.reply("❌ لم أتمكن من العثور على المستخدم. تأكد من صحة اليوزر أو الآيدي.")
    
    confirm_buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ تأكيد الكتم", callback_data=f"confirm_mute_{target_user.id}"),
            InlineKeyboardButton("❌ إلغاء", callback_data="cancel_mute")
        ]
    ])
    await message.reply(
        f"⚠️ هل أنت متأكد من كتم {target_user.mention} عام؟",
        reply_markup=confirm_buttons
    )

@app.on_callback_query(filters.regex("^confirm_mute_"))
async def confirm_mute(client, callback):
    user_id = int(callback.data.split("_")[2])
    mute_user_globally(callback.from_user.id, user_id)
    await callback.message.edit_text(
        f"**◍ تم كتم المستخدم عام\n√**"
    )

@app.on_callback_query(filters.regex("^cancel_mute$"))
async def cancel_mute(client, callback):
    await callback.message.edit_text("✅ تم إلغاء عملية الكتم.")

@app.on_message(filters.regex(r"^الغاء كتم عام 🔔$"), group=140084312)
async def global_unmute(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        ask = await client.ask(message.chat.id, "📝 أرسل الآن يوزر أو آيدي المستخدم الذي تريد إلغاء كتمه:", filters=filters.user(message.from_user.id), timeout=60)
        try:
            user_input = ask.text.strip().replace("@", "")
            target_user = await client.get_users(user_input)
        except Exception:
            return await ask.reply("❌ لم أتمكن من العثور على المستخدم. تأكد من صحة اليوزر أو الآيدي.")
    if not is_user_muted(target_user.id):
        return await message.reply("ℹ️ هذا المستخدم غير مكتوم عام.")
    unmute_user_globally(target_user.id)
    await message.reply(f"**◍ تم الغاء كتم المستخدم عام\n√**")

@app.on_message(filters.regex(r"^(المكتومين عام|المكتومين عام 🤐)$"), group=41084451312)
async def muted_list(client, message):
    if message.from_user.id not in [OWNER_ID, sourse_dev] and message.from_user.id not in dev:
        return
    mutes = get_muted_users()
    if not mutes:
        return await message.reply("ℹ️ لا يوجد مستخدمين مكتومين حالياً.")
    text = "📋 قائمة المكتومين عام:\n\n"
    for mute in mutes:
        user_id = mute["user_id"]
        muted_by = mute["muted_by"]
        timestamp = mute["timestamp"]
        try:
            user = await client.get_users(user_id)
            username = f"@{user.username}" if user.username else "لا يوجد يوزر"            
            admin = await client.get_users(muted_by)
            admin_username = f"@{admin.username}" if admin.username else str(admin.id)
            text += (
                f"👤 المستخدم: {username} (ID: {user_id})\n"
                f"👥 تم الكتم بواسطة: {admin_username}\n"
                f"📅 التاريخ: {timestamp.strftime('%Y-%m-%d %H:%M') if timestamp else 'غير معروف'}\n"
                "━━━━━━━━━━━━━━\n"
            )
        except Exception as e:
            print(f"Error getting user info: {e}")
            text += (
                f"👤 المستخدم: ID: {user_id} (لم يتم العثور على معلوماته)\n"
                f"👥 تم الكتم بواسطة: {muted_by}\n"
                f"📅 التاريخ: {timestamp.strftime('%Y-%m-%d %H:%M') if timestamp else 'غير معروف'}\n"
                "━━━━━━━━━━━━━━\n"
            )
    await message.reply(text)

######################################################## كتم عام ####################################################
######################################################## كتم عام ####################################################


@app.on_message(filters.command(["مسح المكتومين"], ""), group=1354456)
async def unmute_all(client, message):
    global muted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    chat_member = await client.get_chat_member(chat_id, message.from_user.id)
    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == zombie_id:
        chat_id = str(message.chat.id)
        if chat_id in muted_users:
            count = len(muted_users[chat_id])
            failed_count = 0        
            for member in muted_users[chat_id].copy():
                user_id = member
                try:
                    muted_users[chat_id].remove(member)
                except Exception:
                    failed_count += 1
            successful_count = count - failed_count
            if successful_count > 0:
                await message.reply_text(f"↢ تم مسح {successful_count} من المكتومين")
            else:
                await message.reply_text("↢ لا يوجد مستخدمين مكتومين ليتم مسحهم")
            if failed_count > 0:
                await message.reply_text(f"↢ فشل في مسح {failed_count} من المكتومين")
    else:
        await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**.")  
  

@app.on_message(filters.command(["كتمه"], ""), group=345569)
async def temp_mute_user(client, message):
    global muted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    if chat_id not in muted_users:
        muted_users[chat_id] = []
    chat_member = await client.get_chat_member(chat_id, message.from_user.id)
    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID or message.from_user.id == zombie_id: 
        if not message.reply_to_message:
            await message.reply_text("خطأ، لكتم شخص يرجى الرد على رسالته ثم كتابة الأمر بشكل صحيح مثل 'كتمه 10'")
            return
        user = message.reply_to_message.from_user
        if user.id == zombie_id:  
            await message.reply_text(f"**عيب اقدع ده المبرمج محمد صالح 🥷**")
            return
        parts = message.text.split()
        if len(parts) != 2 or not parts[1].isdigit():
            await message.reply_text("خطأ، لكتم شخص يرجى كتابة الأمر بشكل صحيح مثل 'كتمه 10'")
            return
        time = int(parts[1])
        muted_users[chat_id].append(user.id)
        await message.reply_text(f"العضو {user.mention} تم كتمه بنجاح لمدة {time} ثانية.")
        await asyncio.sleep(time)
        muted_users[chat_id].remove(user.id)
    else:
        await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**.")  

banned_users = []
@app.on_message(filters.regex(r"^(طرد|حظر)$"), group=726262728656)
async def ban_uhhser(client, message):
    global banned_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name
    dd = str(message.from_user.id)

    if chat_member.status in [ChatMemberStatus.OWNER] or message.from_user.id == OWNER_ID or message.from_user.id == zombie_id:
        if user_id == str(message.from_user.id):
            await message.reply_text("لا يمكنك حظر نفسك!")
            return

        if user_id == f"{zombie_id}":
            await message.reply_text("عيب اقدع ده المبرمج محمد صالح 🥷")
            return
        
        if user_id == f"{OWNER_ID}":
            await message.reply_text("لا يمكنك حظر مالك البوت")
            return

        member = await message.chat.get_member(user_id)
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("لا يمكنك حظر المالك الأصلي!")

        member = await message.chat.get_member(user_id)
        if member.status in [ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("لا يمكنك حظر المشرف!")

        if user_id not in banned_users:
            try:
                banned_users.append(user_id)
                await client.ban_chat_member(message.chat.id, int(user_id))
                user = await client.get_users(int(user_id))
            except Exception as e:
                 await message.reply_text(f"العضو {user.mention} غير موجود في الجروب")
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ إلغاء الحظر", callback_data=f"unban {message.from_user.id} {user_id}")]
            ])

            await message.reply_text(f"✅ تم حظر المستخدم {user.mention} بنجاح.", reply_markup=keyboard)
        else:
            user = await client.get_users(int(user_id))
            await message.reply_text(f"⚠️ المستخدم {user.mention} محظور بالفعل.")
    else:
        await message.reply_text("⚠️ هذا الأمر مخصص للمشرفين فقط.")


@app.on_message(filters.command(["الغاء حظر"], ""), group=72626256)
async def unban_uhhser(client, message):
    global banned_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status in [ChatMemberStatus.OWNER] or message.from_user.id == OWNER_ID or message.from_user.id == zombie_id:
        if user_id in banned_users:
            banned_users.remove(user_id)
            await client.unban_chat_member(message.chat.id, int(user_id))
            user = await client.get_users(int(user_id))
            await message.reply_text(f"✅ تم الغاء حظر المستخدم {user.mention} بنجاح.")
        else:
            user = await client.get_users(int(user_id))
            await message.reply_text(f"⚠️ المستخدم {user.mention} مش محظور اصلا.")
    else:
        await message.reply_text("⚠️ هذا الأمر مخصص للمشرفين فقط.")

@app.on_callback_query(filters.regex("^unban (\\d+) (\\d+)$"))
async def unban_Suser(client: Client, callback_query):
    data = callback_query.data.split(" ")
    admin_id = int(data[1])
    user_id = int(data[2])
    if callback_query.from_user.id != admin_id:
        await callback_query.answer("❌ لا يمكنك استخدام هذا الزر، فقط المسؤول عن الحظر يستطيع ذلك!", show_alert=True)
        return
    chat_id = callback_query.message.chat.id
    if user_id in banned_users:
        banned_users.remove(str(user_id))
        await client.unban_chat_member(chat_id, user_id)
        await callback_query.answer("✅ تم إلغاء الحظر بنجاح.", show_alert=True)
    else:
        await callback_query.answer("❌ المستخدم غير محظور!", show_alert=True)


restricted_users = []
@app.on_message(filters.command(["تقيد"], ""), group=62)
async def mullte(client: Client, message: Message):
    global restricted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return

    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name

    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == zombie_id or message.from_user.id == OWNER_ID or message.from_user.id == sourse_dev:
        if user_id == str(message.from_user.id):
            await message.reply_text("لا يمكنك تقيد نفسك!")
            return

        if user_id == zombie_id:
            await message.reply_text("عيب اقدع ده المبرمج محمد صالح 🥷")
            return
        
        if user_id == f"{OWNER_ID}":
            await message.reply_text("لا يمكنك تقييد مالك البوت")
            return
        
        if user_id == f"{sourse_dev}":
            await message.reply_text("لا يمكنك تقييد مبرمج السورس")
            return
        
        member = await message.chat.get_member(user_id)
        if member.status in [ChatMemberStatus.OWNER]:
            return await message.reply("لا يمكنك تقيد المالك الأصلي!")

        member = await message.chat.get_member(user_id)
        if member.status in [ChatMemberStatus.ADMINISTRATOR]:
            return await message.reply("لا يمكنك تقيد المشرف!")
        if user_id not in restricted_users:
            mute_permission = ChatPermissions(can_send_messages=False)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=user_id,
                permissions=mute_permission,
            )
            restricted_users.append(user_id)
            await message.reply_text(f"✅ ¦ تـم التقييد بـنجـاح\n {user.mention} ")
        else:
            user = await client.get_users(int(user_id))
            await message.reply_text(f"المستخدم {user.mention} مقيد بالفعل.")
    else:
        await message.reply_text("هذا الأمر مخصص للمشرفين فقط.")

@app.on_message(filters.command(["مسح المقيدين"], ""), group=40)
async def unmute(client: Client, message: Message):
    global restricted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == zombie_id or message.from_user.id == OWNER_ID or message.from_user.id == sourse_dev:
        count = len(restricted_users)
        for user in restricted_users:
            await client.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=user,
                permissions=unmute_permissions,
            )
            restricted_users.remove(user)
        await message.reply_text(f"↢ تم مسح {count} من المقيديد")
    else:
        await message.reply("ليس لديك صلاحية لتنفيذ هذا الأمر")


@app.on_message(filters.command(["الغاء تقيد","الغاء التقيد"], ""), group=94) 
async def uban_user(client, message):
    global restricted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم\n༄")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم\n༄")
            return
    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    name = chat_member.user.first_name
    
    if chat_member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == zombie_id or message.from_user.id == OWNER_ID or message.from_user.id == sourse_dev:  
        
        if user_id not in banned_users:
            user = await client.get_users(int(user_id))
            await message.reply_text(f"「 {user.mention} 」\nولك مو مقيد\n༄")
        else:
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=user_id,
                permissions=unmute_permissions,
            )
            restricted_users.remove(user_id)
            await message.reply_text(f"✅ ¦ تـم الغاء التقييد بـنجـاح\n {user_id} ")
    else:
        await message.reply_text("هذا الأمر مخصص للمشرفين فقط\n༄")

@app.on_message(filters.command(["تنزيل مشرف","ت م"], "")) 
async def m54ute(client, message):
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == OWNER_ID:  
        try:	   	
            await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=unmute_permissions)
            await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=unmute_permissions)
        except:
            await message.reply_text(f"لم استطع تنزيله")
        await message.reply_text(f"تم تنزيل المشرف بنجاح ✨♥")
    else:
        await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**")

@app.on_message(filters.command(["المقيدين"], ""), group=137762627)
async def banned_urss(client, message):
    global restricted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or (message.from_user.id != zombie_id or message.from_user.id != OWNER_ID or message.from_user.id != sourse_dev):
        await message.reply_text("هذا الامر يخص ❪ الادمن وفوق ❫ بس\n༄")
        return

    count = len(restricted_users)
    user_mentions = [await client.get_chat_member(message.chat.id, user_id) for user_id in restricted_users]
    response = f"<u>قائمة المقيدين وعددهم:</u> {count}\n"
    response += "...\n"
    for i, user in enumerate(user_mentions, start=1):
        mention = user.user.mention()
        response += f"{i}- {mention}\n"
    await message.reply_text(response, parse_mode=enums.ParseMode.HTML)

import wget
# ################################################### باقي القفل والفتح  ############################################################
# ################################################### باقي القفل والفتح  ############################################################
yoro = ["Xnxx", "سكس","اباحيه","جنس","اباحي","زب","كسمك","كس","شرمطه","نيك","لبوه","فشخ","مهبل","نيك خلفى","بتتناك","مساج","كس ملبن","نيك جماعى","نيك جماعي","نيك بنات","رقص","قلع","خلع ملابس","بنات من غير هدوم","بنات ملط","نيك طيز","نيك من ورا","نيك في الكس","ارهاب","موت","حرب","سياسه","سياسي","سكسي","قحبه","شواز","ممويز","نياكه","xnxx","sex","xxx","Sex","Born","borno","Sesso","احا","خخخ","ميتينك","تناك","يلعن","كسك","كسمك","عرص","خول","علق","كسم","انيك","انيكك","اركبك","زبي","نيك","شرموط","فحل","ديوث","سالب","مقاطع","ورعان","هايج","مشتهي","زوبري","طيز","كسي","كسى","ساحق","سحق","لبوه","اريحها","مقاتع","لانجيري","سحاق","مقطع","مقتع","نودز","ندز","ملط","لانجرى","لانجري","لانجيرى","مولااااعه"]
    

Downla_Locked = False 

@app.on_message(filters.command(["قفل التنزيل", "تعطيل التنزيل 🛠"], ""), group=1254798)
async def l_music(client, message):
    global Downla_Locked
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("◍ هذا الأمر يخص المطور فقط.")
    
    Downla_Locked = True
    await message.reply_text(f"◍ تم قفل التنزيل في جميع المجموعات بواسطة ↤︎「 {message.from_user.mention} 」")

@app.on_message(filters.command(["فتح التنزيل", "تفعيل التنزيل ⚙️"], ""), group=545889177)
async def unlo_music(client, message):
    global Downla_Locked
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("◍ هذا الأمر يخص المطور فقط.")
    
    Downla_Locked = False
    await message.reply_text(f"◍ تم فتح التنزيل في جميع المجموعات بواسطة ↤︎「 {message.from_user.mention} 」")


@app.on_message(filters.text & filters.regex(r"^(تنزيل|تحميل)$"), group=71328934)
async def gigshgxvkdnnj(client, message):
    bot_username = client.me.username
    global Music_Locked
    if Music_Locked:
        user = await client.get_chat(chat_id=f"{OWNER_ID}")
        nasme = user.mention
        return await message.reply_text(f"**◍ عذراً التنزيل معطل حالياً\n◍ تواصل مع مطور البوت لتفعيله\n◍ مطور البوت : `{nasme}`\n√**")
    keybord = InlineKeyboardMarkup([[InlineKeyboardButton("تحميل صوت ⚡", callback_data=f"hidhkdhj"),InlineKeyboardButton("تحميل فديو ⚡", callback_data=f"voic5854e1")], [InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣 ⤶", url=f"https://t.me/{bot_username}?startgroup=True")]])
    chat_idd = message.chat.id
    await message.reply_text(f"اختر الان بالاسفل ماذا تريد تحميله ✨♥", reply_markup=keybord)
    
@app.on_callback_query(filters.regex("voic5854e1"))
async def h24dgfgbie(client: Client, CallbackQuery):
    bot_username = client.me.username

    name = await client.ask(CallbackQuery.message.chat.id, text="ارسل الان ما تريد تحميله ✨♥", filters=filters.user(CallbackQuery.from_user.id), timeout=200)
    text = name.text
    if text in yoro:
        return await CallbackQuery.message.reply_text("لا يمكن تنزيل هذا")  
    else:
        print("احم")
    h = await CallbackQuery.message.reply_text(f"**جاري البحث عن {text} 🔍**")
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    url = mo
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quiet": True,
        "cookiefile": "/root/zombie/zombie.txt"
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
            video_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        print(f"{e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    await h.delete()
    try:
        await client.send_video(CallbackQuery.message.chat.id, video=video_file, duration=int(ytdl_data["duration"]), file_name=str(ytdl_data["title"]), thumb=sedlyf, supports_streaming=True, caption=capy)
        os.remove(video_file)
        os.remove(sedlyf)
    except Exception as e:
        print(f"\n{e}")

@app.on_callback_query(filters.regex("hidhkdhj"))
async def h24dg54hfbie(client: Client, CallbackQuery):
    bot_username = client.me.username
    name = await client.ask(CallbackQuery.message.chat.id, text="**ارسل الان ما تريد تحميله ✨♥**", filters=filters.user(CallbackQuery.from_user.id), timeout=200)
    text = name.text
    if text in yoro:
      return await CallbackQuery.message.reply_text("**لا يمكن تنزيل هذا**")  
    else:      
     print("احم")    
    h = await CallbackQuery.message.reply_text(f"**جاري البحث عن {text} 🔍**")
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    mio = mi["search_result"]
    mo = mio[0]["link"]
    mio[0]["duration"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    mio[0]["channel"]
    kekme = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    sedlyf = wget.download(kekme)
    opts = {'format': 'bestaudio[ext=m4a]', 'keepvideo': False, "cookiefile": "/root/zombie/zombie.txt", 'prefer_ffmpeg': False, 'geo_bypass': True, 'outtmpl': '%(title)s.%(ext)s', 'quite': True}
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(mo, download=True)
            audio_file = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        print(f"   : {e}")
        return
    c_time = time.time()
    capy = f"[{thum}]({mo})"
    file_stark = f"{ytdl_data['id']}.mp3"
    await h.delete()
    try:
        await client.send_audio(CallbackQuery.message.chat.id, audio=audio_file, duration=int(ytdl_data["duration"]), title=str(ytdl_data["title"]), performer=str(ytdl_data["uploader"]), file_name=str(ytdl_data["title"]), thumb=sedlyf,caption=capy)
        os.remove(audio_file)
        os.remove(sedlyf)
    except Exception as e:
        print(f" \n{e}")


################################################### الادمن ######################################
group_admins_collection = db[f"group_admins_{BOT_USERNAME}"]

def add_group_admin(group_id, admin_id):
    if not group_admins_collection.find_one({"group_id": group_id, "admin_id": admin_id}):
        group_admins_collection.insert_one({
            "group_id": group_id,
            "admin_id": admin_id,
            "date_added": datetime.now()
        })

def remove_group_admin(group_id, admin_id):
    group_admins_collection.delete_one({
        "group_id": group_id,
        "admin_id": admin_id
    })

def get_group_admins(group_id):
    admins = [doc["admin_id"] for doc in group_admins_collection.find({"group_id": group_id})]
    return admins

def is_group_admin(group_id, user_id):
    return bool(group_admins_collection.find_one({
        "group_id": group_id,
        "admin_id": user_id
    }))

@app.on_message(filters.command(["رفع ادمن"], "") & filters.group, group=1519957)
async def promote_admin(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ ليس لديك الصلاحية لتنفيذ هذا الأمر")
        return
    
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    
    add_group_admin(message.chat.id, user_id)
    await message.reply(f"**◍ تم رفع العضو {user.mention} ادمن بنجاح🛡\n√**")

@app.on_message(filters.command(["تنزيل ادمن"], "") & filters.group, group=15153457)
async def demote_admin(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ ليس لديك الصلاحية لتنفيذ هذا الأمر")
        return
    
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return

    remove_group_admin(message.chat.id, user_id)
    await message.reply(f"**◍ تم تنزيل العضو {user.mention} من الادمنية بنجاح🛡\n√**")

@app.on_message(filters.command(["الادمنيه", "الادمنية"], "") & filters.group, group=4566153457)
async def list_admins(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ ليس لديك الصلاحية لتنفيذ هذا الأمر")
        return
    
    chat_id = message.chat.id
    admins = get_group_admins(chat_id)
    
    if not admins:
        await message.reply("❌ لا يوجد أدمنية للبوت في هذه المجموعة!")
        return
    
    text = "🛡 قائمة أدمنية البوت في هذه المجموعة:\n\n"
    for admin_id in admins:
        try:
            user = await client.get_users(admin_id)
            text += f"- {user.mention} (ID: {admin_id})\n"
        except:
            text += f"- ID: {admin_id}\n"
    await message.reply(text)

@app.on_message(filters.command(["تنزيل الادمنية", "مسح الادمنية"], "") & filters.group, group=4444445)
async def confirm_delete_all_admins(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ فقط مالك الجروب يمكنه حذف الأدمنية!")
        return

    admins = get_group_admins(message.chat.id)
    if not admins:
        await message.reply("❌ لا يوجد أدمنية لحذفهم!")
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ نعم", callback_data=f"confirm_delete_admins:{message.chat.id}:{message.from_user.id}"),
         InlineKeyboardButton("❌ لا", callback_data="cancel_delete_admins")]
    ])
    await message.reply("⚠️ هل أنت متأكد أنك تريد حذف جميع أدمنية البوت من المجموعة؟", reply_markup=keyboard)

@app.on_callback_query(filters.regex("^confirm_delete_admins:(.+):(.+)$"))
async def delete_admins_callback(client, callback_query):
    chat_id, user_id = callback_query.data.split(":")[1:]

    if int(callback_query.from_user.id) != int(user_id):
        await callback_query.answer("❌ هذا الخيار ليس لك.", show_alert=True)
        return

    result = group_admins_collection.delete_many({"group_id": int(chat_id)})

    if result.deleted_count > 0:
        await callback_query.message.edit(f"✅ تم حذف جميع أدمنية البوت في هذه المجموعة ({result.deleted_count} أدمن)!")
    else:
        await callback_query.message.edit("⚠️ لم يتم العثور على أدمنية لحذفهم!")

@app.on_callback_query(filters.regex("^cancel_delete_admins$"))
async def cancel_delete_admins(client, callback_query):
    await callback_query.message.edit("❌ تم إلغاء عملية حذف الأدمنية.")

################################################### الادمن ######################################

################################################### المنشئ ######################################
group_creators_collection = db[f"group_creators_{BOT_USERNAME}"]

def add_group_creator(group_id, creator_id):
    if not group_creators_collection.find_one({"group_id": group_id, "creator_id": creator_id}):
        group_creators_collection.insert_one({
            "group_id": group_id,
            "creator_id": creator_id,
            "date_added": datetime.now()
        })
        return True
    return False

def remove_group_creator(group_id, creator_id):
    result = group_creators_collection.delete_one({
        "group_id": group_id,
        "creator_id": creator_id
    })
    return result.deleted_count > 0

def get_group_creators(group_id):
    creators = [doc["creator_id"] for doc in group_creators_collection.find({"group_id": group_id})]
    return creators

def is_group_creator(group_id, user_id):
    return bool(group_creators_collection.find_one({
        "group_id": group_id,
        "creator_id": user_id
    }))

@app.on_message(filters.command(["رفع منشئ"], "") & filters.group, group=1519958)
async def promote_creator(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    
    if get.status != ChatMemberStatus.OWNER and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ فقط مالك الجروب يمكنه رفع المنشئين!")
        return
    
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    
    if add_group_creator(message.chat.id, user_id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} منشئ بنجاح 🛠/n√**")
    else:
        await message.reply(f"⚠️ {user.mention} هو بالفعل منشئ في هذه المجموعة!")

@app.on_message(filters.command(["تنزيل منشئ"], "") & filters.group, group=15153458)
async def demote_creator(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    
    if get.status != ChatMemberStatus.OWNER and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ فقط مالك الجروب يمكنه تنزيل المنشئين!")
        return
    
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    
    if remove_group_creator(message.chat.id, user_id):
        await message.reply(f"**◍ تم تنزيل العضو {user.mention} من المنشئين بنجاح 🛠/n√**")
    else:
        await message.reply(f"⚠️ {user.mention} ليس منشئاً في هذه المجموعة!")

@app.on_message(filters.command(["المنشئين", "المشئين"], "") & filters.group, group=4566153458)
async def list_creators(client, message):
    chat_id = message.chat.id
    creators = get_group_creators(chat_id)
    if not creators:
        await message.reply("❌ لا يوجد منشئين للبوت في هذه المجموعة!")
        return
    
    text = "🛠 قائمة منشئي البوت في هذه المجموعة:\n\n"
    for creator_id in creators:
        try:
            user = await client.get_users(creator_id)
            text += f"- {user.mention}\n"
        except:
            text += f"- {creator_id}\n"
    await message.reply(text)

@app.on_message(filters.command(["مسح المنشئين", "حذف المنشئين"], "") & filters.group, group=8888888)
async def confirm_delete_all_creators(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status != ChatMemberStatus.OWNER and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ فقط مالك الجروب يمكنه حذف المنشئين!")
        return

    creators = get_group_creators(message.chat.id)
    if not creators:
        await message.reply("❌ لا يوجد منشئين لحذفهم!")
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ نعم", callback_data=f"confirm_delete_creators:{message.chat.id}:{message.from_user.id}"),
         InlineKeyboardButton("❌ لا", callback_data="cancel_delete_creators")]
    ])
    await message.reply("⚠️ هل أنت متأكد أنك تريد حذف جميع المنشئين من المجموعة؟", reply_markup=keyboard)



@app.on_callback_query(filters.regex("^confirm_delete_creators:(.+):(.+)$"))
async def delete_creators_callback(client, callback_query):
    chat_id, user_id = callback_query.data.split(":")[1:]
    
    if int(callback_query.from_user.id) != int(user_id):
        await callback_query.answer("❌ هذا الخيار ليس لك.", show_alert=True)
        return

    result = group_creators_collection.delete_many({"group_id": int(chat_id)})

    if result.deleted_count > 0:
        await callback_query.message.edit(f"✅ تم حذف جميع منشئي البوت في هذه المجموعة ({result.deleted_count} منشئ)!")
    else:
        await callback_query.message.edit("⚠️ لم يتم العثور على منشئين لحذفهم!")

@app.on_callback_query(filters.regex("^cancel_delete_creators$"))
async def cancel_delete_creators(client, callback_query):
    await callback_query.message.edit("❌ تم إلغاء عملية الحذف.")

################################################### المنشئ ######################################
################################################### المالك ######################################

group_owners_collection = db[f"group_owners_{BOT_USERNAME}"]

def add_group_owner(group_id, owner_id):
    if not group_owners_collection.find_one({"group_id": group_id, "owner_id": owner_id}):
        group_owners_collection.insert_one({
            "group_id": group_id,
            "owner_id": owner_id,
            "date_added": datetime.now()
        })
        return True
    return False

def remove_group_owner(group_id, owner_id):
    result = group_owners_collection.delete_one({
        "group_id": group_id,
        "owner_id": owner_id
    })
    return result.deleted_count > 0

def get_group_owners(group_id):
    owners = [doc["owner_id"] for doc in group_owners_collection.find({"group_id": group_id})]
    return owners

def is_group_owner(group_id, user_id):
    return bool(group_owners_collection.find_one({
        "group_id": group_id,
        "owner_id": user_id
    }))

@app.on_message(filters.command(["رفع مالك"], "") & filters.group, group=1111111)
async def promote_owner(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status != ChatMemberStatus.OWNER and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ فقط مالك الجروب يمكنه رفع مالك!")
        return

    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return

    if add_group_owner(message.chat.id, user_id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} مالك بنجاح 👑/n√**")
    else:
        await message.reply(f"⚠️ {user.mention} هو بالفعل مالك في هذه المجموعة!")

@app.on_message(filters.command(["تنزيل مالك"], "") & filters.group, group=2222222)
async def demote_owner(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status != ChatMemberStatus.OWNER and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ فقط مالك الجروب يمكنه تنزيل مالك!")
        return

    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return

    if remove_group_owner(message.chat.id, user_id):
        await message.reply(f"**◍ تم تنزيل العضو {user.mention} من المالكين بنجاح 👑/n√**")
    else:
        await message.reply(f"⚠️ {user.mention} ليس مالكاً في هذه المجموعة!")

@app.on_message(filters.command(["المالكين", "الملاك"], "") & filters.group, group=3333333)
async def list_owners(client, message):
    chat_id = message.chat.id
    owners = get_group_owners(chat_id)
    if not owners:
        await message.reply("❌ لا يوجد ملاك للبوت في هذه المجموعة!")
        return
    text = "👑 قائمة المالكين في هذه المجموعة:\n\n"
    for owner_id in owners:
        try:
            user = await client.get_users(owner_id)
            text += f"- {user.mention}\n"
        except:
            text += f"- {owner_id}\n"
    await message.reply(text)

@app.on_message(filters.command(["تنزيل المالكين", "مسح المالكين"], "") & filters.group, group=4444444)
async def confirm_delete_all_owners(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status != ChatMemberStatus.OWNER and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ فقط مالك الجروب يمكنه حذف المالكين!")
        return

    owners = get_group_owners(message.chat.id)
    if not owners:
        await message.reply("❌ لا يوجد مالكين لحذفهم!")
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ نعم", callback_data=f"confirm_delete_owners:{message.chat.id}:{message.from_user.id}"),
         InlineKeyboardButton("❌ لا", callback_data="cancel_delete_owners")]
    ])
    await message.reply("⚠️ هل أنت متأكد أنك تريد حذف جميع مالكين البوت من المجموعة؟", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^confirm_delete_owners:(.+):(.+)$"))
async def delete_owners_callback(client, callback_query):
    chat_id, user_id = callback_query.data.split(":")[1:]
    if int(callback_query.from_user.id) != int(user_id):
        await callback_query.answer("❌ هذا الخيار ليس لك.", show_alert=True)
        return

    result = group_owners_collection.delete_many({"group_id": int(chat_id)})
    if result.deleted_count > 0:
        await callback_query.message.edit(f"✅ تم حذف جميع مالكين البوت في هذه المجموعة ({result.deleted_count} مالك)!")
    else:
        await callback_query.message.edit("⚠️ لم يتم العثور على مالكين لحذفهم!")

@app.on_callback_query(filters.regex("^cancel_delete_owners$"))
async def cancel_delete_owners(client, callback_query):
    await callback_query.message.edit("❌ تم إلغاء عملية حذف المالكين.")

################################################### المالك ######################################
################################################### المميزين ######################################

group_vips_collection = db[f"group_vips_{BOT_USERNAME}"]

def add_group_vip(group_id, user_id):
    if not group_vips_collection.find_one({"group_id": group_id, "user_id": user_id}):
        group_vips_collection.insert_one({
            "group_id": group_id,
            "user_id": user_id
        })
        return True
    return False

def remove_group_vip(group_id, user_id):
    result = group_vips_collection.delete_one({
        "group_id": group_id,
        "user_id": user_id
    })
    return result.deleted_count > 0

def get_group_vips(group_id):
    return [doc["user_id"] for doc in group_vips_collection.find({"group_id": group_id})]

def is_group_vip(group_id, user_id):
    return bool(group_vips_collection.find_one({"group_id": group_id, "user_id": user_id}))

@app.on_message(filters.command(["رفع مميز"], "") & filters.group, group=5555555)
async def promote_vip(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status != ChatMemberStatus.OWNER and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ فقط مالك الجروب يمكنه رفع مميز!")
        return

    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return

    if add_group_vip(message.chat.id, user_id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} مميز بنجاح 🌟/n√**")
    else:
        await message.reply(f"⚠️ {user.mention} هو بالفعل مميز في هذه المجموعة!")

@app.on_message(filters.command(["تنزيل مميز"], "") & filters.group, group=66616666)
async def demote_vip(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status != ChatMemberStatus.OWNER and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ فقط مالك الجروب يمكنه تنزيل مميز!")
        return

    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
        
    if remove_group_vip(message.chat.id, user_id):
        await message.reply(f"**◍ تم تنزيل العضو {user.mention} من المميزين بنجاح 🌟/n√**")
    else:
        await message.reply(f"⚠️ {user.mention} ليس مميزاً في هذه المجموعة!")

@app.on_message(filters.command(["المميزين"], "") & filters.group, group=77777077)
async def list_vips(client, message):
    chat_id = message.chat.id
    vips = get_group_vips(chat_id)
    if not vips:
        await message.reply("❌ لا يوجد مميزين في هذه المجموعة!")
        return
    text = "🌟 قائمة المميزين في هذه المجموعة:\n\n"
    for vip_id in vips:
        try:
            user = await client.get_users(vip_id)
            text += f"- {user.mention}\n"
        except:
            text += f"- {vip_id}\n"
    await message.reply(text)

@app.on_message(filters.command(["مسح المميزين", "تنزيل المميزين"], "") & filters.group, group=88888818)
async def confirm_delete_all_vips(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status != ChatMemberStatus.OWNER and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ فقط مالك الجروب يمكنه حذف المميزين!")
        return

    vips = get_group_vips(message.chat.id)
    if not vips:
        await message.reply("❌ لا يوجد مميزين لحذفهم!")
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ نعم", callback_data=f"confirm_delete_vips:{message.chat.id}:{message.from_user.id}"),
         InlineKeyboardButton("❌ لا", callback_data="cancel_delete_vips")]
    ])
    await message.reply("⚠️ هل أنت متأكد أنك تريد حذف جميع المميزين من المجموعة؟", reply_markup=keyboard)

@app.on_callback_query(filters.regex("^confirm_delete_vips:(.+):(.+)$"))
async def delete_vips_callback(client, callback_query):
    chat_id, user_id = callback_query.data.split(":")[1:]
    if int(callback_query.from_user.id) != int(user_id):
        await callback_query.answer("❌ هذا الخيار ليس لك.", show_alert=True)
        return

    result = group_vips_collection.delete_many({"group_id": int(chat_id)})
    if result.deleted_count > 0:
        await callback_query.message.edit(f"✅ تم حذف جميع المميزين من المجموعة ({result.deleted_count} مستخدم)!")
    else:
        await callback_query.message.edit("⚠️ لم يتم العثور على مميزين لحذفهم!")

@app.on_callback_query(filters.regex("^cancel_delete_vips$"))
async def cancel_delete_vips(client, callback_query):
    await callback_query.message.edit("❌ تم إلغاء عملية حذف المميزين.")

################################################### المميزين ######################################
################################################### المطور الأساسي ######################################
main_devs_collection = db[f"main_developers_{BOT_USERNAME}"]

def add_main_developer(user_id):
    if not main_devs_collection.find_one({"user_id": user_id}):
        main_devs_collection.insert_one({"user_id": user_id})
        return True
    return False

def remove_main_developer(user_id):
    result = main_devs_collection.delete_one({"user_id": user_id})
    return result.deleted_count > 0

def get_main_developers():
    return [doc["user_id"] for doc in main_devs_collection.find()]

def is_main_developer(user_id):
    return bool(main_devs_collection.find_one({"user_id": user_id}))


@app.on_message(filters.command(["رفع مطور"], "") & filters.group, group=8888818)
async def promote_main_dev(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if add_main_developer(user.id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} مطور اساسي بنجاح 👨🏻‍💻/n√**")
    else:
        await message.reply(f"⚠️ {user.mention} مطور أساسي بالفعل.")


@app.on_message(filters.command(["تنزيل مطور"], "") & filters.group, group=8818)
async def demote_main_dev(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if remove_main_developer(user.id):
        await message.reply(f"**◍ تم تنزيل العضو {user.mention} من المطورين الاساسين بنجاح 👨🏻‍💻/n√**")
    else:
        await message.reply(f"⚠️ {user.mention} ليس مطورًا أساسيًا.")


@app.on_message(filters.command(["المطورين", "المطورين 🕵🏻‍♂️"], ""), group=8814818)
async def list_main_devs(client, message):
    devs = get_main_developers()
    if not devs:
        return await message.reply("**❌ لا يوجد مطورين أساسيين**")
    text = "**👨🏻‍💻 قائمة المطورين الأساسيين:**\n\n"
    for uid in devs:
        try:
            user = await client.get_users(uid)
            text += f"- {user.mention}\n"
        except:
            text += f"- `{uid}`\n"
    await message.reply(text)
################################################### المطور الأساسي ######################################
################################################### المطور الثانوي ######################################
sub_devs_collection = db[f"sub_developers_{BOT_USERNAME}"]

def add_sub_developer(user_id):
    if not sub_devs_collection.find_one({"user_id": user_id}):
        sub_devs_collection.insert_one({"user_id": user_id})
        return True
    return False

def remove_sub_developer(user_id):
    result = sub_devs_collection.delete_one({"user_id": user_id})
    return result.deleted_count > 0

def get_sub_developers():
    return [doc["user_id"] for doc in sub_devs_collection.find()]

def is_sub_developer(user_id):
    return bool(sub_devs_collection.find_one({"user_id": user_id}))


@app.on_message(filters.command(["رفع مطور ثانوي"], "") & filters.group, group=8898718)
async def promote_sub_dev(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if add_sub_developer(user.id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} مطور ثانوي بنجاح 🕵🏻‍♂️/n√**")
    else:
        await message.reply(f"⚠️ {user.mention} مطور ثانوي بالفعل.")


@app.on_message(filters.command(["تنزيل مطور ثانوي"], "") & filters.group, group=108818)
async def demote_sub_dev(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = str(user.id)
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = str(user.id)
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask = await app.ask(message.chat.id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
            user_id = ask.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if remove_sub_developer(user.id):
        await message.reply(f"◍ تم تنزيل العضو {user.mention} من المطورين الثانويين بنجاح 🕵🏻‍♂️/n√")
    else:
        await message.reply(f"⚠️ {user.mention} ليس مطورًا ثانويًا.")


@app.on_message(filters.command(["المطورين الثانويين", "المطورين الثانويين 🧑🏻‍💻"], ""), group=888854818)
async def list_sub_devs(client, message):
    devs = get_sub_developers()
    if not devs:
        return await message.reply("**❌ لا يوجد مطورين ثانويين**")
    text = "**🕵🏻‍♂️ قائمة المطورين الثانويين:**\n\n"
    for uid in devs:
        try:
            user = await client.get_users(uid)
            text += f"- {user.mention}\n"
        except:
            text += f"- `{uid}`\n"
    await message.reply(text)
################################################### المطور الثانوي ######################################
################################################### إدارة المدراء حسب الجروب ######################################
managers_collection = db[f"managers_{BOT_USERNAME}"]

def add_manager(user_id, group_id):
    if not managers_collection.find_one({"user_id": user_id, "group_id": group_id}):
        managers_collection.insert_one({"user_id": user_id, "group_id": group_id})
        return True
    return False

def remove_manager(user_id, group_id):
    result = managers_collection.delete_one({"user_id": user_id, "group_id": group_id})
    return result.deleted_count > 0

def get_managers(group_id):
    return [doc["user_id"] for doc in managers_collection.find({"group_id": group_id})]

def is_manager(user_id, group_id):
    return bool(managers_collection.find_one({"user_id": user_id, "group_id": group_id}))


@app.on_message(filters.command(["رفع مدير"], "") & filters.group, group=9999918)
async def promote_manager(client, message):
    group_id = message.chat.id

    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
            except Exception:
                return await message.reply_text("❌ لا يمكن العثور على المستخدم")
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
            except Exception:
                return await message.reply_text("❌ رقم ID غير صحيح")
        else:
            return await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
    else:
        ask = await app.ask(group_id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
        except Exception:
            return await message.reply_text("❌ رقم ID غير صحيح")

    if add_manager(user.id, group_id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} من المدراء بنجاح 📋/n√**")
    else:
        await message.reply(f"⚠️ {user.mention} مدير بالفعل في هذا الجروب.")


@app.on_message(filters.command(["تنزيل مدير"], "") & filters.group, group=9918)
async def demote_manager(client, message):
    group_id = message.chat.id

    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
            except Exception:
                return await message.reply_text("❌ لا يمكن العثور على المستخدم")
        elif target.isdigit():
            try:
                user = await client.get_users(int(target))
            except Exception:
                return await message.reply_text("❌ رقم ID غير صحيح")
        else:
            return await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
    else:
        ask = await app.ask(group_id, "📩 يرجى إرسال ايدي المستخدم:", filters=filters.user(message.from_user.id), timeout=300)
        try:
            user = await client.get_users(int(ask.text))
        except Exception:
            return await message.reply_text("❌ رقم ID غير صحيح")

    if remove_manager(user.id, group_id):
        await message.reply(f"**◍ تم تنزيل العضو {user.mention} من المدراء بنجاح 📋/n√**")
    else:
        await message.reply(f"⚠️ {user.mention} ليس مديرًا في هذا الجروب.")


@app.on_message(filters.command(["المدراء"], "") & filters.group, group=9984818)
async def list_managers(client, message):
    group_id = message.chat.id
    managers = get_managers(group_id)

    if not managers:
        return await message.reply("❌ لا يوجد مدراء في هذا الجروب.")
    
    text = "📋 قائمة المدراء في هذا الجروب:\n\n"
    for uid in managers:
        try:
            user = await client.get_users(uid)
            text += f"- {user.mention}\n"
        except:
            text += f"- `{uid}`\n"
    await message.reply(text)
################################################### إدارة المدراء حسب الجروب ######################################



#............................................ اكس او ...........................................................................    
board = ["⬜️"] * 9
players = []
current_player = 0
fanish_game = None  

def create_board():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(board[0], callback_data="10"), InlineKeyboardButton(board[1], callback_data="11"), InlineKeyboardButton(board[2], callback_data="12")],
        [InlineKeyboardButton(board[3], callback_data="13"), InlineKeyboardButton(board[4], callback_data="14"), InlineKeyboardButton(board[5], callback_data="15")],
        [InlineKeyboardButton(board[6], callback_data="16"), InlineKeyboardButton(board[7], callback_data="17"), InlineKeyboardButton(board[8], callback_data="18")],
    ])

@app.on_message(filters.command(["اكس او","اكس","xo","ox"], ""), group=76468513) 
async def sta54t_game(client, message):
    global players, board, fanish_game, current_player
    current_player = 0
    fanish_game = False
    players = [message.from_user.id]
    board = ["⬜️"] * 9
    await message.reply_text("""
انقر على الزر أدناه لبدء 👇🏻""", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("بدء اللعب 🎮", callback_data="join_game")]
    ]))

@app.on_callback_query(filters.regex("join_game"))
async def join_game(client, call):
    global players, current_player
    current_player = 0
    if call.from_user.id not in players:
        players.append(call.from_user.id)
        await client.edit_message_text(
            call.message.chat.id, call.message.id,
            f"دور الاعب الاول : ❌",
            reply_markup=create_board())

def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != "⬜️":
            return board[combo[0]] 
    return None

def is_draw():
    return all(cell != "⬜️" for cell in board)

@app.on_callback_query(
    filters.regex("10") | filters.regex("11") | filters.regex("12") |
    filters.regex("13") | filters.regex("14") | filters.regex("15") |
    filters.regex("16") | filters.regex("17") | filters.regex("18"))
async def handle_button(client, call):
    global current_player, players, fanish_game
    if fanish_game == True:
        await call.answer("اللعبة انتهت ⚡️", show_alert=True)
        return
    if call.from_user.id not in players:
        await call.answer("✋", show_alert=True)
        return
    if call.from_user.id != players[current_player]:
        await call.answer("ليس دورك", show_alert=True)
        return
    index = int(call.data) - 10
    if board[index] == "⬜️":
        board[index] = "❌" if current_player == 0 else "⭕️"
        current_player = 1 if current_player == 0 else 0
        user = await client.get_users(players[current_player])
        user_mention = user.mention()
        emo_xo = "❌" if current_player == 0 else "⭕️"
        await call.message.edit(
            f"دور الاعب : {emo_xo}\n{user_mention}",
            reply_markup=create_board())
        
        winner = check_winner()
        if winner:
            winner_mention =(await client.get_users(players[0 if winner == "❌" else 1])).mention
            await call.message.edit(
                f"الفائز 🎉: {winner_mention}")
            fanish_game = True 
            board[:] = ["⬜️"] * 9
        elif is_draw():
            await call.message.edit(
                "التعادل! 🤝")
            fanish_game = True
            board[:] = ["⬜️"] * 9
        if fanish_game==True:
            return
#............................................ اكس او ...........................................................................    
#............................................ حجرة........................................................................... 
game_state = {}

options = ["حجرة", "ورقة", "مقص"]

def get_winner(chat_id):
    player1_choice = game_state[chat_id]["player1"]["choice"]
    player2_choice = game_state[chat_id]["player2"]["choice"]
    player1_name = game_state[chat_id]["player1"]["name"]
    player2_name = game_state[chat_id]["player2"]["name"]
    
    if player1_choice == player2_choice:
        return "تعادل"
    elif (player1_choice == "حجرة" and player2_choice == "مقص") or (player1_choice == "ورقة" and player2_choice == "حجرة") or (player1_choice == "مقص" and player2_choice == "ورقة"):
        game_state[chat_id]["player1"]["score"] += 1
        return f"{player1_name}"
    else:
        game_state[chat_id]["player2"]["score"] += 1
        return f"{player2_name}"

@app.on_message(filters.command(["حجرة"], ""), group=589)
async def stahxrt(client, message):
    if message.chat.id not in game_state:
        game_state[message.chat.id] = {
            "player1": {
                "name": message.from_user.first_name,
                "choice": None,
                "score": 0
            },
            "player2": {
                "name": None,
                "choice": None,
                "score": 0
            }
        }
        await message.reply(
            f"{game_state[message.chat.id]['player1']['name']} بدأ لعبة حجرة ورقة مقص.\n\nانتظر اللاعب الثاني...",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("اضغط للعب", callback_data="join")],
                    [InlineKeyboardButton("ᏚᎾᏌᎡᏟᎬ mhmad saleh", url="https://t.me/uu_u_e")]
                ]
            )
        )
    else:
        await message.reply_text("هناك لعبة جارية بالفعل في هذه الدردشة. انتظر حتى تنتهي.")
        
@app.on_callback_query(filters.regex("join"), group=58957)
async def joinhf(client, callback_query):
    if callback_query.message.chat.id in game_state:
        if callback_query.from_user.first_name != game_state[callback_query.message.chat.id]["player1"]["name"]:
            game_state[callback_query.message.chat.id]["player2"]["name"] = callback_query.from_user.first_name
            await callback_query.message.edit(
                f"{game_state[callback_query.message.chat.id]['player1']['name']} و {game_state[callback_query.message.chat.id]['player2']['name']} يلعبان حجرة ورقة مقص.\n\n👨‍💼 دور اللاعب: {game_state[callback_query.message.chat.id]['player1']['name']}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("حجرة", callback_data="حجرة"),
                         InlineKeyboardButton("ورقة", callback_data="ورقة"),
                         InlineKeyboardButton("مقص", callback_data="مقص")],[
                         InlineKeyboardButton("ᏚᎾᏌᎡᏟᎬ mhmad saleh", url="https://t.me/uu_u_e")
                         ]
                    ]
                )
            )
        else:
            await callback_query.answer("انت منضم للعبه بالفعل", show_alert=True)
    else:
        await callback_query.answer("لا توجد لعبة جارية في هذه الدردشة.", show_alert=True)

@app.on_callback_query(filters.regex("^(حجرة|ورقة|مقص)$"), group=58965)
async def choovcse(client, callback_query):
    bot_username = client.me.username
    if callback_query.message.chat.id in game_state:
        user_choice = callback_query.data
        user_name = callback_query.from_user.first_name
        if user_name == game_state[callback_query.message.chat.id]["player1"]["name"]:
            game_state[callback_query.message.chat.id]["player1"]["choice"] = user_choice
            await callback_query.message.edit(
                f"👨‍💼 اللاعب الأول: {game_state[callback_query.message.chat.id]['player1']['name']} لقد لعب \n\n👨‍💼 اللاعب الثاني: {game_state[callback_query.message.chat.id]['player2']['name']} اختر الآن...",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("حجرة", callback_data="حجرة"),
                         InlineKeyboardButton("ورقة", callback_data="ورقة"),
                         InlineKeyboardButton("مقص", callback_data="مقص")],
                         [InlineKeyboardButton("ᏚᎾᏌᎡᏟᎬ mhmad saleh", url="https://t.me/uu_u_e")]
                    ]
                )
            )
        elif user_name == game_state[callback_query.message.chat.id]["player2"]["name"]:
            if game_state[callback_query.message.chat.id]["player1"]["choice"] is None:
                await callback_query.answer("لا يمكنك اللعب حتى يلعب اللاعب الأول.", show_alert=True)
            else:
                game_state[callback_query.message.chat.id]["player2"]["choice"] = user_choice
                winner = get_winner(callback_query.message.chat.id)
                name_player1 = game_state[callback_query.message.chat.id]['player1']['name']
                name_player2 = game_state[callback_query.message.chat.id]['player2']['name']
                choice_player1 = game_state[callback_query.message.chat.id]['player1']['choice']
                choice_player2 = game_state[callback_query.message.chat.id]['player2']['choice']
                player1_score = game_state[callback_query.message.chat.id]['player1']['score']
                player2_score = game_state[callback_query.message.chat.id]['player2']['score']
                await callback_query.message.edit(
                    f"⌯━─━─━─━──━─━─━─━─━─━─━──━⌯\n\n⚠️ الإسم : {name_player1}\n\n❓ الإختيار : {choice_player1}\n\n🛒 النقاط : {player1_score}\n\n⌯━─━─━─━──━─━─━─━─━─━─━──━⌯\n\n⚠️ الإسم : {name_player2}\n\n❓ الإختيار : {choice_player2}\n\n🛒 النقاط : {player2_score}\n\n⌯━─━─━─━──━─━─━─━─━─━─━──━⌯\n\n🕺 اللاعب الفائز هو ⤵️ \n\n{winner}\n\n⌯━─━─━─━──━─━─━─━─━─━─━──━⌯"
                )
                del game_state[callback_query.message.chat.id]
        else:
            await callback_query.answer("أنت لست جزء من هذه اللعبة.", show_alert=True)
    else:
        await callback_query.answer("لا توجد لعبة جارية في هذه الدردشة.", show_alert=True)          
#............................................ حجرة...........................................................................         
#............................................  لعبه البنك ...........................................................................    
def is_sudoer(_, __, message):
    return message.from_user.id == zombie_id

other_filters = filters.group &  ~filters.via_bot & ~filters.forwarded
other_filters2 = (
    filters.private &  ~filters.via_bot & ~filters.forwarded
)

def load_bank_data():
    try:
        with open('bank_data.json', 'r') as file:
            bank_data = json.load(file)
    except FileNotFoundError:
        bank_data = {}
    return bank_data
def save_bank_data(bank_data):
    with open('bank_data.json', 'w') as file:
        json.dump(bank_data, file)

cooldown_time = 12 * 60 * 60  

def check_cooldown(user_id):
    cooldown_data = load_cooldown_data()
    current_time = int(time.time())
    if str(user_id) in cooldown_data:
        last_use_time = cooldown_data[str(user_id)]
        time_passed = current_time - last_use_time
        remaining_time = cooldown_time - time_passed
        if time_passed < cooldown_time:
            hours = remaining_time // 3600
            minutes = (remaining_time % 3600) // 60
            response = f"عذرًا، يجب الانتظار {hours} ساعة و {minutes} دقيقة قبل استخدام الكنز مرة أخرى"
            return False, response
    cooldown_data[str(user_id)] = current_time
    save_cooldown_data(cooldown_data)
    return True, None
def load_cooldown_data():
    try:
        with open('cooldown_data.json', 'r') as file:
            cooldown_data = json.load(file)
    except FileNotFoundError:
        cooldown_data = {}
    return cooldown_data
def save_cooldown_data(cooldown_data):
    with open('cooldown_data.json', 'w') as file:
        json.dump(cooldown_data, file)
def get_remaining_time(user_id):
    cooldown_data = load_cooldown_data()
    current_time = int(time.time())
    if str(user_id) in cooldown_data:
        last_use_time = cooldown_data[str(user_id)]
        remaining_time = 20 * 60 - (current_time - last_use_time)
        if remaining_time < 0:
            remaining_time = 0
        return remaining_time
    return 0
##############££££££££££#############££££££££££#########££££#
LUCK_COOLDOWN = 1200  

last_luck_times = {}

def get_luck_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_luck_times:
        last_luck_time = last_luck_times[user_id]
        elapsed_time = current_time - last_luck_time
        remaining_time = LUCK_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_luck_time(user_id):
    last_luck_times[user_id] = int(time.time())
##############££££££££££#############££££££££££#########££££#
TRANSFER_COOLDOWN = 1200  


last_transfer_times = {}

def get_transfer_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_transfer_times:
        last_transfer_time = last_transfer_times[user_id]
        elapsed_time = current_time - last_transfer_time
        remaining_time = TRANSFER_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time

def update_transfer_time(user_id):
    last_transfer_times[user_id] = int(time.time())

@app.on_message(filters.command(["تحويل"], ""), group=53)
async def transfer(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_transfer_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    await message.reply_text(f'تم تحويل {amount} دولار بنجاح')
                    update_transfer_time(user_id)
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: تحويل + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["استثمار"], ""), group=53)
async def invest(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    # قم بتنفيذ الاستثمار وحساب العائد المحتمل
                    return_amount = amount * random.randint(50, 100) / 100
                    bank_data['accounts'][str(user_id)]['balance'] += return_amount
                    save_bank_data(bank_data)
                    cooldown_data = load_cooldown_data()
                    cooldown_data[str(user_id)] = int(time.time())
                    save_cooldown_data(cooldown_data)
                    await message.reply_text(f'تهانينا! لقد استثمرت {amount} دولار وحصلت على عائد بقيمة {return_amount} دولار')
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: استثمار + المبلغ')
        else:
            remaining_minutes = int(remaining_time / 60)
            remaining_seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {remaining_minutes} دقيقة و {remaining_seconds} ثانية بين كل عملية استثمار')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["حظ"], ""), group=53)
async def luck(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_luck_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    chance = random.randint(0, 1)
                    if chance == 1:
                        win_amount = amount * random.uniform(1, 3)
                        bank_data['accounts'][str(user_id)]['balance'] += win_amount
                        save_bank_data(bank_data)
                        await message.reply_text(f'تهانينا! لقد ربحت {win_amount} دولار')
                    else:
                        await message.reply_text('للأسف، لم تربح أي شيء')
                    update_luck_time(user_id)
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: حظ + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["اضف"], "") & filters.create(is_sudoer), group=46468)
async def add_mhzboney(client, message):
    reply_message = message.reply_to_message
    if reply_message is not None and reply_message.from_user is not None:
        user_id = reply_message.from_user.id
        args = message.text.split(" ")
        if len(args) == 2 and args[1].isdigit():
            amount = int(args[1])
            bank_data = load_bank_data()
            if 'accounts' not in bank_data:
                bank_data['accounts'] = {}
            if str(user_id) in bank_data['accounts']:
                bank_data['accounts'][str(user_id)]['balance'] += amount
            else:
                bank_data['accounts'][str(user_id)] = {'balance': amount}
            save_bank_data(bank_data)
            await message.reply_text(f'تمت إضافة {amount} فلوس للمستخدم {user_id}')
        else:
            await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: اضف + المبلغ')
##############££££££££££#############££££££££££#########££££
@app.on_message(filters.command(["حذف حسابه"], "") & filters.create(is_sudoer), group=5)
async def delete_account(client, message):
    reply_message = message.reply_to_message
    if reply_message is not None and reply_message.from_user is not None:
        user_id = reply_message.from_user.id
        bank_data = load_bank_data()
        if str(user_id) in bank_data['accounts']:
            del bank_data['accounts'][str(user_id)]
            save_bank_data(bank_data)
            await message.reply_text(f'تم حذف حساب المستخدم {user_id}')
        else:
            await message.reply_text('المستخدم المحدد لا يملك حساب بنكي')
    else:
        await message.reply_text('الرجاء الرد على شخص لحذف حسابه')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["حذف حسابي"], ""), group=6)
async def delete_my_account(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        del bank_data['accounts'][str(user_id)]
        save_bank_data(bank_data)
        await message.reply_text(f'تم حذف حسابك البنكي')
    else:
        await message.reply_text('لا تمتلك حسابًا بنكيًا')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["تصفير البنك"], "") & filters.create(is_sudoer), group=7)
async def reset_bank(client, message):
    bank_data = {'accounts': {}}
    save_bank_data(bank_data)
    await message.reply_text('تم مسح جميع حسابات البنك')  
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["فتح البنك"], "") & filters.create(is_sudoer), group=8)
async def enable_bank_game(client, message):
    chat_id = message.chat.id
    bank_data = load_bank_data()
    if 'game_enabled' in bank_data:
        await client.send_message(chat_id, 'لعبة البنك مفعلة بالفعل في المجموعة')
    else:
        bank_data['game_enabled'] = True
        save_bank_data(bank_data)
        await client.send_message(chat_id, 'تم تفعيل لعبة البنك في المجموعة')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["قفل البنك"], "") & filters.create(is_sudoer), group=9)
async def disable_bank_game(client, message):
    chat_id = message.chat.id
    bank_data = load_bank_data()
    if 'game_enabled' in bank_data:
        del bank_data['game_enabled']
        save_bank_data(bank_data)
        await client.send_message(chat_id, 'تم إيقاف لعبة البنك في المجموعة')
    else:
        await client.send_message(chat_id, 'لعبة البنك معطلة بالفعل في المجموعة')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["انشاء", "انشاء حساب بنكي"], ""), group=7536566)
async def create_account(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    bot_username = client.me.username
    username = message.from_user.username
    bank_data = load_bank_data()
    account_number = random.randint(100000000000000, 999999999999999)
    if 'accounts' not in bank_data:
        bank_data['accounts'] = {}
    if str(user_id) in bank_data['accounts']:
        await message.reply_text('لديك بالفعل حساب بنكي')
    else:
        bank_data['accounts'][str(user_id)] = {
            'username': username,
            'balance': 50,
            'account_number': account_number,
            'thief': 0
        }
        save_bank_data(bank_data)
        await message.reply_video(
            video=f"{video_path}",
            caption=f"↤︎ تم إنشاء حساب بنكي بنجاح\n↤︎ اكتب بنكي لترى حسابك 😇\n↤︎ نوع البنك : بنك مارلو\n↤︎ رقم حسابك {account_number}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "ᏚᎾᏌᎡᏟᎬ mhmad saleh",
                            url=f"https://t.me/uu_u_e"
                        ),
                    ],
                ]
            ),
        )
        
@app.on_message(filters.command(["فلوسي"], ""), group=11)
async def check_balance(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    accounts = bank_data.get('accounts', {})
    if str(user_id) in accounts:
        balance = accounts[str(user_id)]['balance']
        await message.reply_text(f'رصيدك الحالي هو: {balance} دولار')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["فلوسه"], ""), group=12)
async def check_user_balance(client, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        bank_data = load_bank_data()
        if str(user_id) in bank_data['accounts']:
            balance = bank_data['accounts'][str(user_id)]['balance']
            await message.reply_text(f'رصيد {reply.from_user.username} هو: {balance} دولار')
        else:
            await message.reply_text(f'المستخدم {reply.from_user.username} ليس لديه حساب بنكي')
    else:
        await message.reply_text('الرجاء الرد على رسالة المستخدم للحصول على معلومات الحساب')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["حسابي"], ""), group=13)
async def view_account(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        username = bank_data['accounts'][str(user_id)]['username']
        balance = bank_data['accounts'][str(user_id)]['balance']
        account_number = bank_data['accounts'][str(user_id)]['account_number']
        await message.reply_text(f'حسابك البنكي:\nالمستخدم: @{username}\nالرصيد: {balance} دولار\nرقم الحساب : {account_number}')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["بنكه"], ""), group=14)
async def view_user_account(client, message):
    reply = message.reply_to_message
    if reply:
        user_id = reply.from_user.id
        bank_data = load_bank_data()
        if str(user_id) in bank_data['accounts']:
            username = bank_data['accounts'][str(user_id)]['username']
            balance = bank_data['accounts'][str(user_id)]['balance']
            account_number = bank_data['accounts'][str(user_id)]['account_number']
            await message.reply_text(f'حساب {reply.from_user.username} البنكي:\nالمستخدم: {username}\nالرصيد: {balance} دولار\nرقم حسابه : {account_number}')
        else:
            await message.reply_text(f'المستخدم {reply.from_user.username} ليس لديه حساب بنكي')
    else:
        await message.reply_text('الرجاء الرد على رسالة المستخدم لعرض حسابه البنكي')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200  

last_operation_times = {}

def get_operation_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_operation_times:
        last_operation_time = last_operation_times[user_id]
        elapsed_time = current_time - last_operation_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_operation_time(user_id):
    last_operation_times[user_id] = int(time.time())

@app.on_message(filters.command(["مضاربه", "مضاربة"], ""), group=15) 
async def multiply(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_operation_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    save_bank_data(bank_data)
                    multiplier = random.randint(2, 5)
                    result_amount = amount * multiplier
                    bank_data['accounts'][str(user_id)]['balance'] += result_amount
                    save_bank_data(bank_data)
                    await message.reply_text(f'تهانينا! لقد قمت بالمضاعفة وحصلت على {result_amount} دولار')
                    update_operation_time(user_id)
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: مضاعفة + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200  

last_bribe_times = {}

def get_bribe_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_bribe_times:
        last_bribe_time = last_bribe_times[user_id]
        elapsed_time = current_time - last_bribe_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time

def update_bribe_time(user_id):
    last_bribe_times[user_id] = int(time.time())

@app.on_message(filters.command(["رشوة", "رشوه"], ""), group=16)
async def bribe_command(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_bribe_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 1:
                amount = random.randint(300, 4000)
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    if message.reply_to_message is None:
                        await message.reply_text('الرجاء الرد على رسالة لإرسال الرشوة')
                        return
                    receiver_id = message.reply_to_message.from_user.id
                    if receiver_id == user_id:
                        await message.reply_text('لا يمكنك إرسال رشوة لنفسك')
                        return
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    bank_data['accounts'][str(receiver_id)]['balance'] += amount
                    save_bank_data(bank_data)
                    await message.reply_text(f'تمت عملية الرشوة بنجاح! قمت بتحويل {amount} دولار إلى المستلم')
                    update_bribe_time(user_id)
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: رشوة')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200

last_wheel_times = {}

def get_wheel_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_wheel_times:
        last_wheel_time = last_wheel_times[user_id]
        elapsed_time = current_time - last_wheel_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_wheel_time(user_id):
    last_wheel_times[user_id] = int(time.time())

@app.on_message(filters.command(["عجلة الحظ", "عجله الحظ"], ""), group=17)
async def wheel_of_fortune(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_wheel_remaining_time(user_id)
        if remaining_time <= 0:
            win_amount = random.randint(100, 5000)
            bank_data['accounts'][str(user_id)]['balance'] += win_amount
            save_bank_data(bank_data)
            if win_amount > 0:
                await message.reply_text(f'تهانينا! لقد فزت بمبلغ {win_amount} دولار في عجلة الحظ')
            else:
                await message.reply_text('عذرًا، لم تفز بأي مبلغ في عجلة الحظ هذه المرة')
            update_wheel_time(user_id)
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
OPERATION_COOLDOWN = 1200  

last_tip_times = {}

def get_custom_tip_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_tip_times:
        last_tip_time = last_tip_times[user_id]
        elapsed_time = current_time - last_tip_time
        remaining_time = OPERATION_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
    
def update_custom_tip_time(user_id):
    last_tip_times[user_id] = int(time.time())

@app.on_message(filters.command(["بقشيش"], ""), group=18)
async def custom_tip_command(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_custom_tip_remaining_time(user_id)
        if remaining_time <= 0:
            args = message.text.split(' ')
            if len(args) == 2 and args[1].isdigit():
                amount = int(args[1])
                if amount <= bank_data['accounts'][str(user_id)]['balance']:
                    if message.reply_to_message is None:
                        await message.reply_text('الرجاء الرد على رسالة لإرسال البقشيش')
                        return
                    receiver_id = message.reply_to_message.from_user.id
                    if receiver_id == user_id:
                        await message.reply_text('لا يمكنك إرسال بقشيش لنفسك')
                        return
                    bank_data['accounts'][str(user_id)]['balance'] -= amount
                    bank_data['accounts'][str(receiver_id)]['balance'] += amount
                    save_bank_data(bank_data)
                    await message.reply_text(f'تمت عملية البقشيش بنجاح! قمت بتحويل {amount} دولار إلى المستلم')
                    update_custom_tip_time(user_id)
                else:
                    await message.reply_text('رصيدك الحالي غير كافي')
            else:
                await message.reply_text('الرجاء استخدام الأمر بالشكل الصحيح: بقشيش + المبلغ')
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
SALARY_COOLDOWN = 1200  

last_salary_times = {}

def get_salary_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_salary_times:
        last_salary_time = last_salary_times[user_id]
        elapsed_time = current_time - last_salary_time
        remaining_time = SALARY_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_salary_time(user_id):
    last_salary_times[user_id] = int(time.time())

@app.on_message(filters.command(["راتب"], ""), group=19)
async def salary(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_salary_remaining_time(user_id)
        if remaining_time <= 0:
            salary_amount = 3500
            bank_data['accounts'][str(user_id)]['balance'] += salary_amount
            save_bank_data(bank_data)
            await message.reply_text(f'تم صرف راتبك الشهري بمبلغ {salary_amount} دولار')
            update_salary_time(user_id)
        else:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            await message.reply_text(f'عذرًا، يجب الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام الأمر مرة أخرى')
    else:
        await message.reply_text('ليس لديك حساب بنكي')
##############££££££££££#############££££££££££#########££££#
STEAL_COOLDOWN = 1200  
POLICE_COOLDOWN = 1200  

last_steal_times = {}
last_police_times = {}
last_protection_times = {}

def get_steal_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_steal_times:
        last_steal_time = last_steal_times[user_id]
        elapsed_time = current_time - last_steal_time
        remaining_time = STEAL_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time

def get_police_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_police_times:
        last_police_time = last_police_times[user_id]
        elapsed_time = current_time - last_police_time
        remaining_time = POLICE_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def get_protection_remaining_time(user_id):
    current_time = int(time.time())
    if user_id in last_protection_times:
        last_protection_time = last_protection_times[user_id]
        elapsed_time = current_time - last_protection_time
        remaining_time = STEAL_COOLDOWN - elapsed_time
        if remaining_time < 0:
            remaining_time = 0
    else:
        remaining_time = 0
    return remaining_time
def update_steal_time(user_id):
    last_steal_times[user_id] = int(time.time())
def update_police_time(user_id):
    last_police_times[user_id] = int(time.time())
def update_protection_time(user_id):
    last_protection_times[user_id] = int(time.time())

@app.on_message(filters.command(["سرقة", "سرقه"], ""), group=20640)
async def steal_mo55ney(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_steal_remaining_time(user_id)
        if remaining_time > 0:
            await message.reply_text(f'يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى')
        else:
            target_id = message.reply_to_message.from_user.id
            if str(target_id) in bank_data['accounts']:
                if target_id == user_id:
                    await message.reply_text('لا يمكنك سرقة نفسك!')
                else:
                    stolen_amount = random.randint(10, 50)
                    if stolen_amount <= bank_data['accounts'][str(target_id)]['balance']:
                        bank_data['accounts'][str(user_id)]['balance'] += stolen_amount
                        bank_data['accounts'][str(target_id)]['balance'] -= stolen_amount
                        bank_data['accounts'][str(user_id)]['thief'] += stolen_amount
                        save_bank_data(bank_data)
                        update_steal_time(user_id)
                        await message.reply_text(f'تمت عملية السرقة بنجاح! تم سرقة {stolen_amount} دولار من المستخدم')
                    else:
                        await message.reply_text('لا يمكنك سرقته لانه فقير')
            else:
                await message.reply_text('المستخدم المحدد لا يملك حساب بنكي')
    else:
        await message.reply_text('ليس لديك حساب بنكي')

@app.on_message(filters.command(["شرطة", "شرطه"], ""), group=21)
async def police_usehcr(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_police_remaining_time(user_id)
        if remaining_time > 0:
            await message.reply_text(f'يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى')
        else:
            target_id = message.reply_to_message.from_user.id
            if str(target_id) in bank_data['accounts']:
                if target_id == user_id:
                    await message.reply_text('لا يمكنك استخدام الأمر على نفسك!')
                else:
                    stolen_amount = random.randint(10, 50)
                    if stolen_amount <= bank_data['accounts'][str(user_id)]['balance']:
                        bank_data['accounts'][str(user_id)]['balance'] -= stolen_amount
                        bank_data['accounts'][str(target_id)]['balance'] += stolen_amount
                        save_bank_data(bank_data)
                        update_police_time(user_id)
                        await message.reply_text(f'تمت عملية القبض على المستخدم! تم خصم {stolen_amount} دولار من حسابك')
                    else:
                        await message.reply_text('رصيدك الحالي غير كافي للقبض على المستخدم')
            else:
                await message.reply_text('المستخدم المحدد لا يملك حساب بنكي')
    else:
        await message.reply_text('ليس لديك حساب بنكي')

@app.on_message(filters.command(["حماية", "حمايه"], ""), group=22)
async def protect_money(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        remaining_time = get_protection_remaining_time(user_id)
        if remaining_time > 0:
            await message.reply_text(f'يجب عليك الانتظار لمدة {remaining_time} ثانية قبل استخدام الأمر مرة أخرى')
        else:
            protection_amount = random.randint(10, 50)
            if protection_amount <= bank_data['accounts'][str(user_id)]['balance']:
                bank_data['accounts'][str(user_id)]['balance'] -= protection_amount
                save_bank_data(bank_data)
                update_protection_time(user_id)
                await message.reply_text(f'تم تنفيذ عملية حماية الأموال بنجاح! تم خصم {protection_amount} دولار من حسابك')
            else:
                await message.reply_text('رصيدك الحالي غير كافي لحماية الأموال')
    else:
        await message.reply_text('ليس لديك حساب بنكي')

@app.on_message(filters.command(["توب الحراميه", "توب سرقه", "توب السرقة", "توب السرقه", "توب سرقة"], ""), group=22)
async def top_thieves(client, message):
    bank_data = load_bank_data()
    sorted_accounts = sorted(bank_data['accounts'], key=lambda x: bank_data['accounts'][x]['thief'], reverse=True)
    top_thieves = sorted_accounts[:5]  
    response = "أعلى الحرامية في البنك:\n\n"    
    for thief_id in top_thieves:
        thief_username = await client.get_chat(int(thief_id)).username
        thief_balance = bank_data['accounts'][thief_id]['thief']
        response += f"@{thief_username}: {thief_balance} دولار\n"
    await message.reply_text(response)
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["توب فلوس","توب الفلوس"], ""), group=20543)
async def top_m659oney(client, message):
    bank_data = load_bank_data()
    sorted_accounts = sorted(bank_data['accounts'], key=lambda x: bank_data['accounts'][x]['balance'], reverse=True)
    top_accounts = sorted_accounts[:5]  
    response = "أعلى الأموال في البنك:\n\n"
    for account_id in top_accounts:
        account_username = await client.get_chat(account_id).username
        account_balance = bank_data['accounts'][account_id]['balance']
        response += f"@{account_username}: {account_balance} دولار\n"
    
    await message.reply_text(response)
    
@app.on_message(filters.command(["البنك", "بنك"], ""), group=476785)
async def msmmezat(client, message):
    await message.reply_text(
        f"""**مرحبآ بك عزيزي » {message.from_user.mention}**في قسم لعبة بنك مارلو\n
🏦 اوامر لعبه البنك ⇊

👮‍♂️ « المطور » ⇊
⩹━★⊷⌯ᏚᎾᏌᎡᏟᎬ mhmad saleh⌯⊶★━⩺\n
➕╖ `اضف فلوس` + المبلغ «» ❬ بالرد علي الشخص المراد اضافه الفلوس له ❭
🗑╢ `حذف حسابه` «» ❬ بالرد علي الشخص المراد حذف حسابه ❭
❌╢ `حذف حساب` + اليوزر «» ❬ لحذف حساب الشخص ❭
😵╜ `تصفير البنك` «» ❬ لمسح كل الحسابات ❭

👨‍🦳 « الاعضاء » ⇊
⩹━★⊷⌯ᏚᎾᏌᎡᏟᎬ mhmad saleh⌯⊶★━⩺\n
📑╖ `انشاء` «» فتح حساب بنكي
🤑╢ `فلوسي` «» اموالي
💸╢ `فلوسه` «» امواله ❬ بالرد علي الشخص ❭
🏦╢ `بنكي` «» حسابي
💰╢ `بنكه` «» حسابه ❬ بالرد علي الشخص ❭
♻️╢ `تحويل` + المبلغ
☠️╢ `كنز`
🤖╢ `استثمار` + المبلغ
🍃╢ `حظ` + المبلغ
⏫╢ `مضاعفه` «» `مضاربه` + المبلغ
🎯╢ `عجله الحظ`
🤞╢ `رشوه`
🥺╢ `بقشيش`
⏳╢ `راتب`
📎╢ `سرقه` «» `اسرق` ❬ بالرد علي الشخص ❭
🚔╢ `شرطه` «» `شرطة` ❬ بالرد علي الشخص ❭
⭐️╢ `حمايه اموالي` «» ❬ لحمايه اموالك من السرقه ❭
👮╢ شرطه + اليوزر
💂‍♀️╢ `توب الحراميه` «» `توب السرقه`
⤴️╜ `توب الفلوس` «» `توب فلوس`

⩹━★⊷⌯ᏚᎾᏌᎡᏟᎬ mhmad saleh⌯⊶★━⩺""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ᏚᎾᏌᎡᏟᎬ mhmad saleh ⌝⚡", url="https://t.me/uu_u_e"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "close", callback_data="close"
                    ),
                ],
            ]
        ),
    )
#............................................ البنك ...........................................................................    
#............................................ الساعه ...........................................................................    
@app.on_message(filters.command(["الساعه","الوقت","ساعه", "التاريخ"], ""), group=76763)
async def hossaarwm(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    cairo_tz = pytz.timezone("Africa/Cairo")
    now = datetime.now(cairo_tz) 
    current_time = now.strftime("%I:%M:%S %p")
    current_date = now.strftime("%Y-%m-%d") 
    await message.reply_text(f"الساعة الحالية: {current_time}\nتاريخ اليوم: {current_date}")
#............................................ الساعه ...........................................................................   
#............................................ الردود ........................................................................... 
rododda = {}

@app.on_message(filters.text & filters.group & filters.regex(r"^الردود$"), group=321552)
async def show_all_replies(client, message):
    group_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    member = await client.get_chat_member(group_id, user_id)
    if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and user_id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply_text("🚫 | هذا الأمر مخصص للمشرفين فقط.")
    if group_id not in rododda or not rododda[group_id]:
        return await message.reply_text("ℹ️ | لا توجد ردود محفوظة في هذه المجموعة.")
    lines = []
    for i, (name, content) in enumerate(rododda[group_id].items(), 1):
        type_icon = {
            "text": "رسالة",
            "photo": "صورة",
            "video": "فيديو",
            "animation": "متحركة",
            "voice": "بصمة",
            "audio": "أغنية"
        }.get(content["type"], "وسيط")
        lines.append(f"{i} - ( {name} ) ࿓ ( {type_icon} )")
    text = "⇜ قائمة الردود  \n*⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆*\n" + "\n".join(lines)
    await message.reply_text(text)


@app.on_message(filters.regex("حذف جميع الردود") & filters.group, group=45852)
async def delete_all_replies(client, message):
    group_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    member = await client.get_chat_member(group_id, user_id)
    if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and user_id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply_text("🚫 | هذا الأمر مخصص للمشرفين فقط.")
    if group_id not in rododda or not rododda[group_id]:
        return await message.reply_text("ℹ️ | لا توجد ردود لحذفها.")
    try:
        ask = await client.ask(group_id, "⚠️ | هل أنت متأكد أنك تريد حذف جميع الردود في هذه المجموعة؟\nأرسل `نعم` للتأكيد أو `إلغاء` للإلغاء.", filters=filters.user(message.from_user.id), timeout=500)
        if ask.text.strip().lower() == "نعم":
            rododda[group_id].clear()
            await message.reply_text("✅ | تم حذف جميع الردود بنجاح.")
        else:
            await client.send_message(group_id, "❎ | تم إلغاء العملية.")
    except Exception:
        await client.send_message(group_id, "⚠️ | حدث خطأ. تأكد أنك بدأت البوت بالضغط على /start.")


@app.on_message(filters.regex("حذف رد") & filters.group, group=51245552)
async def delete_reply(client, message):
    group_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    check = await client.get_chat_member(group_id, user_id)
    if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and user_id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply_text("🚫 | هذا الأمر مخصص للمشرفين فقط.")
    try:
        ask = await client.ask(group_id, "🔹 أرسل *اسم الرد* الذي تريد حذفه:", filters=filters.user(message.from_user.id), timeout=500)
        reply_name = ask.text.strip()
        if group_id not in rododda:
            rododda[group_id] = {}
        if reply_name in rododda[group_id]:
            del rododda[group_id][reply_name]
            await message.reply_text(f"✅ | تم حذف الرد `{reply_name}` بنجاح.")
        else:
            await message.reply_text("❌ | هذا الرد غير موجود.")
    except Exception:
        await message.reply_text("❗ | تأكد أنك بدأت البوت بالضغط على /start ثم حاول مجددًا.")


@app.on_message(filters.regex("اضف رد") & filters.group, group=5587552)
async def add_reply(client, message):
    group_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    check = await client.get_chat_member(group_id, user_id)
    if check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and user_id not in [zombie_id, OWNER_ID, sourse_dev]:
        return await message.reply_text("🚫 | هذا الأمر مخصص للمشرفين فقط.")
    try:
        ask1 =await client.ask(group_id,
            "**⇜ حلو , الان ارسل اسم الرد\n**"
            "⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆", 
            filters=filters.user(message.from_user.id),
            timeout=300
        )
        reply_name = ask1.text.strip()
        ask2 = await client.ask(group_id,
            "⇜ حلو , الان ارسل جواب الرد\n"
            "⇜ ( نص, صوره, فيديو, متحركه, بصمه, اغنيه )\n"
            "⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n"
            "`{اليوزر}` ↬ يوزر المستخدم\n"
            "`{الاسم}` ↬ اسم المستخدم\n"
            "`{الايدي}` ↬ ايدي المستخدم\n"
            "`{الرتبه}` ↬ رتبة المستخدم", 
            filters=filters.user(message.from_user.id),
            timeout=300
        )
        if ask2.text:
            reply_data = {"type": "text", "data": ask2.text}
        elif ask2.photo:
            path = await client.download_media(ask2.photo)
            reply_data = {"type": "photo", "data": path, "caption": ask2.caption or ""}
        elif ask2.video:
            path = await client.download_media(ask2.video)
            reply_data = {"type": "video", "data": path, "caption": ask2.caption or ""}
        elif ask2.animation:
            path = await client.download_media(ask2.animation)
            reply_data = {"type": "animation", "data": path, "caption": ask2.caption or ""}
        elif ask2.voice:
            path = await client.download_media(ask2.voice)
            reply_data = {"type": "voice", "data": path}
        elif ask2.audio:
            path = await client.download_media(ask2.audio)
            reply_data = {"type": "audio", "data": path, "caption": ask2.caption or ""}
        else:
            return await client.send_message(group_id, "⚠️ | نوع الوسيط غير مدعوم، أرسل من الأنواع المذكورة.")
        if group_id not in rododda:
            rododda[group_id] = {}
        rododda[group_id][reply_name] = reply_data
        await client.send_message(group_id, f"✅ | تم حفظ الرد `{reply_name}` بنجاح.")
    except Exception as e:
        print(e)

@app.on_message(filters.text & filters.group, group=57854)
async def trigger_reply(client, message):
    group_id = message.chat.id
    if group_id not in rododda:
        return
    for reply_name in rododda[group_id]:
        if reply_name in message.text:
            reply_data = rododda[group_id][reply_name]

            reply_text = reply_data["data"]
            reply_text = reply_text.replace("{اليوزر}", f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name)
            reply_text = reply_text.replace("{الاسم}", message.from_user.first_name)
            reply_text = reply_text.replace("{الايدي}", str(message.from_user.id))
            user_id = message.from_user.id if message.from_user else "None"
            chat_member = await client.get_chat_member(group_id, user_id)
            user_status = chat_member.status
            if user_status == "administrator":
                rank = "مشرف"
            elif user_status == "owner":
                rank = "مالك"
            else:
                rank = "عضو"
            reply_text = reply_text.replace("{الرتبه}", rank)
            try:
                if reply_data["type"] == "video":
                    await message.reply_video(reply_data["data"])
                elif reply_data["type"] == "photo":
                    await message.reply_photo(reply_data["data"], caption=reply_text)
                elif reply_data["type"] == "animation":
                    await message.reply_animation(reply_data["data"], caption=reply_text)
                elif reply_data["type"] == "voice":
                    await message.reply_voice(reply_data["data"])
                elif reply_data["type"] == "audio":
                    await message.reply_audio(reply_data["data"], caption=reply_text)
                else:
                    await message.reply_text(reply_text)
            except Exception as e:
                await message.reply_text("❗ | حدث خطأ أثناء إرسال الرد.")
            break

#............................................ الردود ........................................................................... 


#............................................ الردود العام ........................................................................... 
global_replies = {}

@app.on_message(filters.regex("الردود العامة 📝"), group = 219723435)
async def show_all_global_replies(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    group_id = message.chat.id
    
    if user_id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply_text("🚫 | هذا الأمر مخصص للمشرفين فقط.")
    
    if not global_replies:
        return await message.reply_text("ℹ️ | لا توجد ردود عامة محفوظة.")
    
    lines = []
    for i, (name, content) in enumerate(global_replies.items(), 1):
        type_icon = {
            "text": "رسالة",
            "photo": "صورة",
            "video": "فيديو",
            "animation": "متحركة",
            "voice": "بصمة",
            "audio": "أغنية"
        }.get(content["type"], "وسيط")
        lines.append(f"{i} - ( {name} ) ࿓ ( {type_icon} )")
    
    text = "⇜ قائمة الردود العامة  \n*⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆*\n" + "\n".join(lines)
    await message.reply_text(text)


@app.on_message(filters.regex("حذف رد عام 🗑"), group = 2102398554)
async def delete_global_reply(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    group_id = message.chat.id    
    if user_id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply_text("🚫 | هذا الأمر مخصص للمشرفين فقط.")
    
    try:
        ask = await client.ask(message.chat.id, "**◍ ارسل اسم الرد العام اللذي تريد حذفه 📝\n√**", timeout=500)
        reply_name = ask.text.strip()
        
        if reply_name in global_replies:
            del global_replies[reply_name]
            await message.reply_text(f"**◍ تم حذف الرد العام بنجاح 🗑\n√**")
        else:
            await message.reply_text("**◍ عذرا هذا الرد غير موجود ❌\n√**")
    except Exception:
        await message.reply_text("❗ | حدث خطأ أثناء العملية.")


@app.on_message(filters.regex("اضف رد عام 💬"), group = 2148214)
async def add_global_reply(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    group_id = message.chat.id
    if user_id not in [OWNER_ID, zombie_id, sourse_dev]:
        return await message.reply_text("**🚫 | هذا الأمر مخصص للمشرفين فقط**")
    
    try:
        ask1 = await client.ask(message.chat.id, "**◍ ارسل اسم الرد العام 📝\n√**", timeout=300)
        reply_name = ask1.text.strip()
        
        ask2 = await client.send_message(message.chat.id, (
            "⇜ حلو , الحين ارسل جواب الرد العام\n"
            "⇜ ( نص, صوره, فيديو, متحركه, بصمه, اغنيه )\n"
            "⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n"
            "{اليوزر} ↬ يوزر المستخدم\n"
            "{الاسم} ↬ اسم المستخدم\n"
            "{الايدي} ↬ ايدي المستخدم\n"
            "{الرتبه} ↬ رتبة المستخدم"
        ))        
        if ask2.text:
            reply_data = {"type": "text", "data": ask2.text}
        elif ask2.photo:
            path = await client.download_media(ask2.photo)
            reply_data = {"type": "photo", "data": path, "caption": ask2.caption or ""}
        elif ask2.video:
            path = await client.download_media(ask2.video)
            reply_data = {"type": "video", "data": path, "caption": ask2.caption or ""}
        elif ask2.animation:
            path = await client.download_media(ask2.animation)
            reply_data = {"type": "animation", "data": path, "caption": ask2.caption or ""}
        elif ask2.voice:
            path = await client.download_media(ask2.voice)
            reply_data = {"type": "voice", "data": path}
        elif ask2.audio:
            path = await client.download_media(ask2.audio)
            reply_data = {"type": "audio", "data": path, "caption": ask2.caption or ""}
        else:
            return await client.send_message(user_id, "⚠️ | نوع الوسيط غير مدعوم، أرسل من الأنواع المذكورة.")
        
        global_replies[reply_name] = reply_data
        await client.send_message(user_id, f"**◍ تم تعيين الرد بنجاح ✅\n√**")
    except Exception as e:
        print(e)

@app.on_message(filters.text & filters.group)
async def trigger_global_reply(client, message):
    group_id = message.chat.id
    if not global_replies:
        return
    
    for reply_name in global_replies:
        if reply_name in message.text:
            reply_data = global_replies[reply_name]            
            reply_text = reply_data["data"]
            reply_text = reply_text.replace("{اليوزر}", f"@{message.from_user.username}" if message.from_user.username else message.from_user.first_name)
            reply_text = reply_text.replace("{الاسم}", message.from_user.first_name)
            reply_text = reply_text.replace("{الايدي}", str(message.from_user.id))            
            user_id = message.from_user.id if message.from_user else "None"
            chat_member = await client.get_chat_member(group_id, user_id)
            user_status = chat_member.status
            if user_status == "administrator":
                rank = "مشرف"
            elif user_status == "owner":
                rank = "مالك"
            else:
                rank = "عضو"
            reply_text = reply_text.replace("{الرتبه}", rank)
            try:
                if reply_data["type"] == "video":
                    await message.reply_video(reply_data["data"])
                elif reply_data["type"] == "photo":
                    await message.reply_photo(reply_data["data"], caption=reply_text)
                elif reply_data["type"] == "animation":
                    await message.reply_animation(reply_data["data"], caption=reply_text)
                elif reply_data["type"] == "voice":
                    await message.reply_voice(reply_data["data"])
                elif reply_data["type"] == "audio":
                    await message.reply_audio(reply_data["data"], caption=reply_text)
                else:
                    await message.reply_text(reply_text)
            except Exception as e:
                await message.reply_text("❗ | حدث خطأ أثناء إرسال الرد.")
            break


#............................................ الردود العام ........................................................................... 

#............................................ الردود العام ........................................................................... 
from datetime import datetime, date

GROUP_DATA_FILE = "group_data.json"

if not os.path.exists(GROUP_DATA_FILE):
    with open(GROUP_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump({"groups": {}}, f)

def load_group_data():
    try:
        with open('group_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"groups": {}}

def save_group_data(data):
    with open('group_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_day_name():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[date.today().weekday()]


@app.on_message(filters.group, group=5412234154)
async def track_message(client, message):
    if message.from_user and message.from_user.is_bot:
        return

    group_id = str(message.chat.id)
    user_id = str(message.from_user.id) if message.from_user else "unknown"
    data = load_group_data()
    now = datetime.utcnow()
    today_str = now.strftime("%Y-%m-%d")
    week_str = now.strftime("%Y-%U")
    month_str = now.strftime("%Y-%m")
    group = data.setdefault("groups", {}).setdefault(group_id, {
        "title": message.chat.title,
        "total_messages": 0,
        "total_text_messages": 0,
        "total_photos": 0,
        "total_videos": 0,
        "total_voices": 0,
        "total_stickers": 0,
        "total_links": 0,
        "last_activity": today_str,
        "members": {}
    })
    member = group["members"].setdefault(user_id, {
        "first_name": message.from_user.first_name if message.from_user else "مجهول",
        "username": message.from_user.username if message.from_user and hasattr(message.from_user, 'username') else None,
        "messages_count": 0,
        "text_messages_count": 0,
        "photos_count": 0,
        "videos_count": 0,
        "voices_count": 0,
        "stickers_count": 0,
        "links_count": 0,
        "last_message": today_str,
        "today_messages": 0,
        "weekly_messages": {},
        "monthly_messages": {},
        "active_days": {}
    })
    group["total_messages"] += 1
    member["messages_count"] += 1
    member["today_messages"] += 1
    member["weekly_messages"][week_str] = member["weekly_messages"].get(week_str, 0) + 1
    member["monthly_messages"][month_str] = member["monthly_messages"].get(month_str, 0) + 1
    member["active_days"][today_str] = member["active_days"].get(today_str, 0) + 1
    member["last_message"] = today_str
    group["last_activity"] = today_str
    if message.photo:
        group["total_photos"] += 1
        member["photos_count"] += 1
    elif message.video:
        group["total_videos"] += 1
        member["videos_count"] += 1
    elif message.voice:
        group["total_voices"] += 1
        member["voices_count"] += 1
    elif message.sticker:
        group["total_stickers"] += 1
        member["stickers_count"] += 1
    elif message.text:
        if "http://" in message.text or "https://" in message.text:
            group["total_links"] += 1
            member["links_count"] += 1
        else:
            group["total_text_messages"] += 1
            member["text_messages_count"] += 1
    save_group_data(data)

from pyrogram import enums
from urllib.parse import quote

@app.on_message(filters.command(["احصائيات الجروب", "الجروب", "جروب"], prefixes="") & filters.group, group=1121223)
async def group_stats(client, message):
    group_id = str(message.chat.id)
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    data = load_group_data()
    if group_id not in data.get("groups", {}):
        return await message.reply("❌ لا توجد بيانات محفوظة لهذه المجموعة بعد.")
    group = data["groups"][group_id]
    title = group.get("title", message.chat.title)
    try:
        chat = await client.get_chat(message.chat.id)
        if chat.username:
            group_link = f"https://t.me/{chat.username}"
        else:
            invite = await client.export_chat_invite_link(chat.id)
            group_link = invite
        members_count = await client.get_chat_members_count(chat.id)
        admins = [member async for member in client.get_chat_members(chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)]
        banned = [member async for member in client.get_chat_members(chat.id, filter=enums.ChatMembersFilter.BANNED)]
        restricted = [member async for member in client.get_chat_members(chat.id, filter=enums.ChatMembersFilter.RESTRICTED)]
        pinned_message = chat.pinned_message
        pinned_message_count = 1 if pinned_message else 0
        chat_id = str(message.chat.id)

        text = f"""<b>⇜ معلومات القروب :</b>
⋆┄─┄─┄─┄┄┄─┄┄─┄─┄─┄┄─┄──┄┄⋆
⇜ <b>اسم القروب :</b>  <a href="{group_link}">{title}</a>
⇜ <b>عدد الادمنيه :</b> {len(admins)}
⇜ <b>عدد المحظورين :</b> {len(banned)}
⇜ <b>عدد الاعضاء :</b> {members_count}
⇜ <b>عدد المقيديين :</b> {len(restricted)}
⇜ <b>عدد الرسائل المثبته :</b> {pinned_message_count}
⇜ <b>الايدي :</b> <code>{group_id}</code>
⋆┄─┄─┄─┄┄┄─┄┄─┄─┄─┄┄─┄──┄┄⋆
⇜ <b>تفاعل القروب :</b>
⋆┄─┄─┄─┄┄┄─┄┄─┄─┄─┄┄─┄──┄┄⋆
◍ 📝 <b>عدد الرسائل الكلي:</b> {group['total_messages']}
◍ ✉️ <b>الرسائل النصية:</b> {group.get('total_text_messages', 0)}
◍ 🖼️ <b>الصور:</b> {group['total_photos']}
◍ 🎥 <b>الفيديوهات:</b> {group['total_videos']}
◍ 🎙️ <b>الصوتيات:</b> {group['total_voices']}
◍ 🧩 <b>الملصقات:</b> {group['total_stickers']}
◍ 🔗 <b>الروابط:</b> {group['total_links']}
⋆┄─┄─┄─┄┄┄─┄┄─┄─┄─┄┄─┄──┄┄⋆
<b>⇜ صلاحيات القروب :</b>
⋆┄─┄─┄─┄┄┄─┄┄─┄─┄─┄┄─┄──┄┄⋆\n
"""
        for lock_id, lock_name in LOCK_NAMES.items():
            lock_var = globals().get(lock_id, {})
            status = "✓" if chat_id in lock_var else "✗"
    
            if chat_id in lock_var:
                punishment, scope = lock_var[chat_id]
                text += f"◍ {lock_name}: {status}\n"
            else:
                text += f"◍ {lock_name}: {status}\n"
        if chat.photo:
            photo = await client.download_media(message.chat.photo.big_file_id)
            await message.reply_photo(photo, caption=text, parse_mode=enums.ParseMode.HTML)
        else:
            await message.reply(text, parse_mode=enums.ParseMode.HTML)
    except Exception as e:
        print("خطأ:", e)
        await message.reply("❌ حصل خطأ أثناء جلب البيانات.")



@app.on_message(filters.command(["كشف"], prefixes="") & filters.group, group=145897774)
async def member_details(client, message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply("الرجاء الرد على رسالة العضو لرؤية تفاصيله")
    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    
    group_id = str(message.chat.id)
    user_id = str(message.reply_to_message.from_user.id)
    data = load_group_data()
    
    if group_id not in data["groups"] or user_id not in data["groups"][group_id]["members"]:
        return await message.reply("لا توجد بيانات عن هذا العضو")
    
    member_data = data["groups"][group_id]["members"][user_id]
    username = f"@{member_data['username']}" if member_data.get("username") else "لا يوجد"
    
    details_text = f"📌 تفاصيل العضو: {member_data['first_name']}\n"
    details_text += f"👤 المعرف: {username}\n"
    details_text += f"🆔 الايدي: {user_id}\n\n"
    details_text += f"📨 عدد الرسائل: {member_data['messages_count']}\n"
    details_text += f"✉️ الرسائل النصية: {member_data.get('text_messages_count', 0)}\n"
    details_text += f"🖼️ الصور: {member_data['photos_count']}\n"
    details_text += f"🎥 الفيديوهات: {member_data['videos_count']}\n"
    details_text += f"🎤 الصوتيات: {member_data['voices_count']}\n"
    details_text += f"📎 الروابط: {member_data['links_count']}\n"
    details_text += f"🖍️ الملصقات: {member_data['stickers_count']}\n\n"
    details_text += f"\n⏱️ آخر نشاط: {member_data['last_message']}"
    await message.reply(details_text)

@app.on_message(filters.command(["رسايلي", "إحصائياتي"], prefixes="") & filters.group, group=1454011)
async def my_stats(client, message):
    group_id = str(message.chat.id)
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = str(message.from_user.id)
    data = load_group_data()

    if group_id not in data["groups"] or user_id not in data["groups"][group_id]["members"]:
        return await message.reply("⚠️ لا توجد بيانات عنك في هذا الجروب")
    member_data = data["groups"][group_id]["members"][user_id]
    total = member_data["messages_count"]
    if total == 0:
        return await message.reply("📭 لم ترسل أي رسائل بعد في هذا الجروب")
    text_count = member_data.get("text_messages_count", 0)
    stats_text = f"📊 إحصائياتك في {data['groups'][group_id]['title']}\n\n"
    stats_text += f"🔢 عدد رسائلك الكلي: {total}\n\n"
    stats_text += "📈 توزيع الرسائل حسب النوع:\n"
    stats_text += f"📝 نصوص: {text_count}\n"
    stats_text += f"🖼 صور: {member_data['photos_count']}\n"
    stats_text += f"🎬 فيديوهات: {member_data['videos_count']}\n"
    stats_text += f"🎧 صوتيات: {member_data['voices_count']}\n"
    stats_text += f"📎 روابط: {member_data['links_count']}\n"
    stats_text += f"🖍 ملصقات: {member_data['stickers_count']}\n"
    await message.reply(stats_text)

@app.on_message(filters.command(["توب اليوم"], prefixes="") & filters.group, group=1878877)
async def top_today(client, message):
    group_id = str(message.chat.id)
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    data = load_group_data()
    if group_id not in data["groups"]:
        return await message.reply("❌ لا توجد بيانات محفوظة لهذه المجموعة بعد.")

    members = data["groups"][group_id].get("members", {})
    today_str = datetime.now().strftime("%Y-%m-%d")
    top_users = []
    for user_id, user_data in members.items():
        count_today = user_data.get("active_days", {}).get(today_str, 0)
        if count_today > 0:
            top_users.append((int(user_id), count_today))
    if not top_users:
        return await message.reply("📭 لا أحد أرسل رسائل اليوم في هذا الجروب.")
    top_users.sort(key=lambda x: x[1], reverse=True)
    result = f"🏆 <b>توب اليوم - {today_str}</b>\n\n"
    for i, (user_id, count) in enumerate(top_users[:10], start=1):
        try:
            user = await client.get_users(user_id)
            mention = f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"
        except:
            mention = f"<code>{user_id}</code>"
        result += f"{i}. {mention} - <b>{count}</b> رسالة\n"
    await message.reply(result, parse_mode="html")

@app.on_message(filters.text & filters.group & filters.regex(r"^توب$"), group=145897)
async def group_top(client, message):
    group_id = str(message.chat.id)
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    data = load_group_data()

    if group_id not in data["groups"]:
        return await message.reply("⚠️ لا توجد بيانات عن هذا الجروب")
    command_parts = message.text.split()

    top_type = "messages"
    if len(command_parts) > 1:
        arg = command_parts[1].lower()
        if arg in ["صور", "photos", "الصور"]:
            top_type = "photos"
        elif arg in ["فيديوهات", "videos", "الفيديوهات"]:
            top_type = "videos"
        elif arg in ["صوتيات", "voices", "الصوتيات"]:
            top_type = "voices"
        elif arg in ["ملصقات", "stickers", "الملصقات"]:
            top_type = "stickers"
        elif arg in ["روابط", "links", "الروابط"]:
            top_type = "links"
    top_stats = []
    for user_id, user_data in data["groups"][group_id]["members"].items():
        count = user_data[f"{top_type}_count"] if top_type != "messages" else user_data["messages_count"]
        top_stats.append({
            "user_id": user_id,
            "username": user_data["username"],
            "first_name": user_data["first_name"],
            "count": count
        })
    top_stats_sorted = sorted(top_stats, key=lambda x: x["count"], reverse=True)
    titles = {
        "messages": "🏆 توب الأعضاء حسب عدد الرسائل",
        "photos": "📸 توب الأعضاء حسب عدد الصور",
        "videos": "🎥 توب الأعضاء حسب عدد الفيديوهات",
        "voices": "🎙 توب الأعضاء حسب عدد الصوتيات",
        "stickers": "🖍 توب الأعضاء حسب عدد الملصقات",
        "links": "🔗 توب الأعضاء حسب عدد الروابط"
    }
    top_text = f"{titles[top_type]} في {data['groups'][group_id]['title']}\n\n"
    for i, user in enumerate(top_stats_sorted[:10], 1):
        medal = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else f"{i}."))
        top_text += f"{medal} {user['first_name']} (@{user['username']}) - {user['count']}\n"
    if not top_stats_sorted:
        top_text += "لا توجد بيانات بعد!"
    await message.reply(top_text)

@app.on_message(filters.command(["توب الاسبوع"], prefixes="") & filters.group, group=1454587)
async def top_week(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    group_id = str(message.chat.id)
    data = load_group_data()
    group = data["groups"].get(group_id)
    if not group:
        return await message.reply("❌ لا توجد بيانات محفوظة لهذه المجموعة.")
    current_week = datetime.utcnow().strftime("%Y-%U")
    members = group.get("members", {})
    sorted_week = sorted(
        members.items(),
        key=lambda x: x[1].get("weekly_messages", {}).get(current_week, 0),
        reverse=True
    )[:5]
    text = "📅 أكثر الأعضاء تفاعلًا هذا الأسبوع:\n\n"
    for i, (user_id, info) in enumerate(sorted_week, 1):
        name = info.get("first_name", "مجهول")
        count = info.get("weekly_messages", {}).get(current_week, 0)
        text += f"{i}. {name} - {count} رسالة\n"
    await message.reply(text)

@app.on_message(filters.command(["توب الشهر"], prefixes="") & filters.group, group=145458797)
async def top_month(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    group_id = str(message.chat.id)
    data = load_group_data()
    group = data["groups"].get(group_id)
    if not group:
        return await message.reply("❌ لا توجد بيانات محفوظة لهذه المجموعة.")

    current_month = datetime.utcnow().strftime("%Y-%m")
    members = group.get("members", {})
    sorted_month = sorted(
        members.items(),
        key=lambda x: x[1].get("monthly_messages", {}).get(current_month, 0),
        reverse=True
    )[:5]
    text = "📆 أكثر الأعضاء تفاعلًا هذا الشهر:\n\n"
    for i, (user_id, info) in enumerate(sorted_month, 1):
        name = info.get("first_name", "مجهول")
        count = info.get("monthly_messages", {}).get(current_month, 0)
        text += f"{i}. {name} - {count} رسالة\n"
    await message.reply(text)

#............................................ الردود العام ........................................................................... 

#............................................ الترحيب ........................................................................... 
WELCOME_DATA = {}

@app.on_message(filters.command("اضف ترحيب", prefixes="") & filters.group,group =511311143)
async def set_welcome_message(client: Client, message: Message):
    chat_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text(f"◍ فقط لديه الصلاحية ↤︎「 {message.from_user.mention} 」")
        return
    if WELCOME_DATA.get(chat_id, {}).get("text"):
        return await message.reply("⚠️ يوجد ترحيب مفعل بالفعل.\nيرجى استخدام `.حذف الترحيب` أولاً.")

    ask = await client.ask(
        chat_id,
        "✏️ أرسل الآن رسالة الترحيب التي تريدها.\n\n"
        "🌐 يمكنك استخدام المتغيرات التالية:\n"
        "◍ {mention} : منشن العضو\n"
        "◍ {username} : معرف المستخدم\n"
        "◍ {id} : ايدي العضو\n"
        "◍ {date} : تاريخ الانضمام\n"
        "◍ {time} : وقت الانضمام\n"
        "◍ {first_name} : الاسم الأول\n"
        "◍ {chat} : اسم المجموعة\n"
        "◍ {admin} : يوزر مالك الجروب\n"
        "◍ {members} : عدد الأعضاء\n\n"
        "📌 بعد إرسال الرسالة سيتم سؤالك عن نوع الصورة.",
        filters=filters.user(message.from_user.id),
        timeout=300
    )
    welcome_text = ask.text

    WELCOME_DATA[chat_id] = {
        "text": welcome_text,
        "photo": "none",
        "enabled": True,
        "setter_id": message.from_user.id
    }

    await message.reply(
        "✅ تم حفظ رسالة الترحيب!\n📌 اختر نوع صورة الترحيب:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📄 بدون صورة", callback_data="welcome_type:none")],
            [InlineKeyboardButton("👤 صورة العضو", callback_data="welcome_type:user")],
            [InlineKeyboardButton("👥 صورة الجروب", callback_data="welcome_type:chat")]
        ])
    )

@app.on_callback_query(filters.regex(r"^welcome_type:(none|user|chat)$"))
async def set_welcome_type(client: Client, callback_query):
    choice = callback_query.data.split(":")[1]
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id

    ahmed = WELCOME_DATA[chat_id]["setter_id"]
    if ahmed != user_id:
        return await callback_query.answer("❌ هذا الخيار متاح فقط لصاحب الأمر.", show_alert=True)
    
    if chat_id not in WELCOME_DATA:
        return await callback_query.answer("⚠️ لا يوجد ترحيب محفوظ.", show_alert=True)

    WELCOME_DATA[chat_id]["photo"] = choice
    types = {"none": "بدون صورة", "user": "صورة العضو", "chat": "صورة الجروب"}
    await callback_query.message.edit_text(f"✅ تم تعيين نوع صورة المغادرة إلى: {types[choice]}\nقم الان بارسال `تفعيل الترحيب`")


@app.on_message(filters.command("تفعيل الترحيب", prefixes="") & filters.group,group =51131873)
async def enable_welcome(client: Client, message: Message):
    chat_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text(f"◍ فقط لديه الصلاحية ↤︎「 {message.from_user.mention} 」")
        return
    if chat_id in WELCOME_DATA:
        WELCOME_DATA[chat_id]["enabled"] = True
        await message.reply("✅ تم تفعيل الترحيب.")
    else:
        await message.reply("⚠️ لا يوجد ترحيب محفوظ لتفعيله.")

@app.on_message(filters.command("تعطيل الترحيب", prefixes="") & filters.group,group =511313)
async def disable_welcome(client: Client, message: Message):
    chat_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text(f"◍ فقط لديه الصلاحية ↤︎「 {message.from_user.mention} 」")
        return
    if chat_id in WELCOME_DATA:
        WELCOME_DATA[chat_id]["enabled"] = False
        await message.reply("🛑 تم تعطيل الترحيب.")
    else:
        await message.reply("⚠️ لا يوجد ترحيب محفوظ لتعطيله.")

@app.on_message(filters.command("حذف الترحيب", prefixes="") & filters.group, group=252650)
async def delete_welcome(client: Client, message: Message):
    chat_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text(f"◍ فقط لديه الصلاحية ↤︎「 {message.from_user.mention} 」")
        return
    if chat_id in WELCOME_DATA:
        del WELCOME_DATA[chat_id]
        await message.reply("🗑️ تم حذف رسالة الترحيب بنجاح.")
    else:
        await message.reply("⚠️ لا يوجد ترحيب محفوظ.")

@app.on_message(filters.new_chat_members, group=71354650)
async def welcome(client: Client, message: Message):
    chat_id = message.chat.id
    welcome = WELCOME_DATA.get(chat_id)
    if not welcome or not welcome.get("enabled"):
        return

    now = datetime.now()
    members_count = await client.get_chat_members_count(chat_id)
    dd = "مشرف غير معروف"
    async for member in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            m = await client.get_chat(member.user.id)
            dd = f"@{m.username}" if m.username else m.first_name

    for user in message.new_chat_members:
        text = welcome["text"]
        replacements = {
            "{mention}": user.mention,
            "{username}": f"@{user.username}" if user.username else "لا يوجد",
            "{id}": str(user.id),
            "{date}": now.strftime("%Y-%m-%d"),
            "{time}": now.strftime("%H:%M:%S"),
            "{first_name}": user.first_name or "",
            "{chat}": message.chat.title,
            "{admin}": dd,
            "{members}": str(members_count)
        }
        for key, val in replacements.items():
            text = text.replace(key, val)

        photo_type = welcome.get("photo", "none")
        try:
            if photo_type == "user":
                async for photo in client.get_chat_photos(user.id, limit=1):
                    await client.send_photo(chat_id, photo.file_id, caption=text)
                    break
            elif photo_type == "chat":
                chat_info = await client.get_chat(chat_id)
                async for photo in client.get_chat_photos(chat_info.id, limit=1):
                    await client.send_photo(chat_id, photo.file_id, caption=text)
                    break
            else:
                await client.send_message(chat_id, text)
        except Exception as e:
            await client.send_message(chat_id, f"{text}\n⚠️ (حدث خطأ: {e})")
#............................................  الترحيب ........................................................................... 
# ............................................ المغادرة ........................................................................... 
LEAVE_DATA = {}

@app.on_message(filters.command("اضف مغادره", prefixes="") & filters.group, group=5119643)
async def set_leave_message(client: Client, message: Message):
    chat_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text(f"◍ فقط لديه الصلاحية ↤︎「 {message.from_user.mention} 」")
        return
    if LEAVE_DATA.get(chat_id, {}).get("text"):
        return await message.reply("⚠️ يوجد مغادره مفعل بالفعل.\nيرجى استخدام `.حذف مغادره` أولاً.")

    ask = await client.ask(
        chat_id,
        "✏️ أرسل الآن رسالة المغادرة التي تريدها.\n\n"
        "🌐 يمكنك استخدام المتغيرات التالية:\n"
        "◍ {mention} : منشن العضو\n"
        "◍ {username} : معرف المستخدم\n"
        "◍ {id} : ايدي العضو\n"
        "◍ {date} : تاريخ المغادرة\n"
        "◍ {time} : وقت المغادرة\n"
        "◍ {first_name} : الاسم الأول\n"
        "◍ {chat} : اسم المجموعة\n"
        "◍ {admin} : يوزر مالك الجروب\n"
        "◍ {members} : عدد الأعضاء\n\n"
        "📌 بعد إرسال الرسالة سيتم سؤالك عن نوع الصورة.",
        filters=filters.user(message.from_user.id),
        timeout=300
    )
    leave_text = ask.text

    LEAVE_DATA[chat_id] = {
        "text": leave_text,
        "photo": "none",
        "enabled": True,
        "setter_id": message.from_user.id
    }

    await message.reply(
        "✅ تم حفظ رسالة المغادرة!\n📌 اختر نوع صورة المغادرة:",
        reply_markup=InlineKeyboardMarkup([ 
            [InlineKeyboardButton("📄 بدون صورة", callback_data="leave_type:none")],
            [InlineKeyboardButton("👤 صورة العضو", callback_data="leave_type:user")],
            [InlineKeyboardButton("👥 صورة الجروب", callback_data="leave_type:chat")]
        ])
    )

@app.on_callback_query(filters.regex(r"^leave_type:(none|user|chat)$"))
async def set_leave_type(client: Client, callback_query):
    choice = callback_query.data.split(":")[1]
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id

    ahmed = LEAVE_DATA[chat_id]["setter_id"]
    if ahmed != user_id:
        return await callback_query.answer("❌ هذا الخيار متاح فقط لصاحب الأمر.", show_alert=True)
    
    if chat_id not in LEAVE_DATA:
        return await callback_query.answer("⚠️ لا يوجد مغادره محفوظ.", show_alert=True)

    LEAVE_DATA[chat_id]["photo"] = choice
    types = {"none": "بدون صورة", "user": "صورة العضو", "chat": "صورة الجروب"}
    await callback_query.message.edit_text(f"✅ تم تعيين نوع صورة المغادرة إلى: {types[choice]}\nقم الان بارسال `تفعيل المغادره`")

@app.on_message(filters.command("تفعيل المغادره", prefixes="") & filters.group, group=101873)
async def enable_leave(client: Client, message: Message):
    chat_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text(f"◍ فقط لديه الصلاحية ↤︎「 {message.from_user.mention} 」")
        return
    if chat_id in LEAVE_DATA:
        LEAVE_DATA[chat_id]["enabled"] = True
        await message.reply("✅ تم تفعيل المغادرة.")
    else:
        await message.reply("⚠️ لا يوجد مغادره محفوظ لتفعيله.")

@app.on_message(filters.command("تعطيل المغادره", prefixes="") & filters.group, group=5199213)
async def disable_leave(client: Client, message: Message):
    chat_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text(f"◍ فقط لديه الصلاحية ↤︎「 {message.from_user.mention} 」")
        return
    if chat_id in LEAVE_DATA:
        LEAVE_DATA[chat_id]["enabled"] = False
        await message.reply("🛑 تم تعطيل المغادرة.")
    else:
        await message.reply("⚠️ لا يوجد مغادره محفوظ لتعطيله.")

@app.on_message(filters.command("حذف المغادره", prefixes="") & filters.group, group=28354650)
async def delete_leave(client: Client, message: Message):
    chat_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_statuses = [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status not in allowed_statuses and message.from_user.id not in allowed_users:
        await message.reply_text(f"◍ فقط لديه الصلاحية ↤︎「 {message.from_user.mention} 」")
        return
    if chat_id in LEAVE_DATA:
        del LEAVE_DATA[chat_id]
        await message.reply("🗑️ تم حذف رسالة المغادرة بنجاح.")
    else:
        await message.reply("⚠️ لا يوجد مغادره محفوظ.")


@app.on_message(filters.left_chat_member, group=25354650)
async def leave(client: Client, message: Message):
    chat_id = message.chat.id
    leave = LEAVE_DATA.get(chat_id)
    if not leave or not leave.get("enabled"):
        return

    now = datetime.now()
    members_count = await client.get_chat_members_count(chat_id)
    dd = "مشرف غير معروف"
    async for member in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            m = await client.get_chat(member.user.id)
            dd = f"@{m.username}" if m.username else m.first_name

    # بدل من التكرار عبر 'message.left_chat_member'، يتم الوصول مباشرة إليه
    user = message.left_chat_member
    text = leave["text"]

    replacements = {
        "{mention}": user.mention,
        "{username}": f"@{user.username}" if user.username else "لا يوجد",
        "{id}": str(user.id),
        "{date}": now.strftime("%Y-%m-%d"),
        "{time}": now.strftime("%H:%M:%S"),
        "{first_name}": user.first_name or "",
        "{chat}": message.chat.title,
        "{admin}": dd,
        "{members}": str(members_count)
    }

    for key, val in replacements.items():
        text = text.replace(key, str(val) if val is not None else "")
        

    photo_type = leave.get("photo", "none")
    try:
        if photo_type == "user":
            async for photo in client.get_chat_photos(user.id, limit=1):
                await client.send_photo(chat_id, photo.file_id, caption=text)
                break
        elif photo_type == "chat":
            chat_info = await client.get_chat(chat_id)
            async for photo in client.get_chat_photos(chat_info.id, limit=1):
                await client.send_photo(chat_id, photo.file_id, caption=text)
                break
        else:
            await client.send_message(chat_id, text)
    except Exception as e:
        await client.send_message(chat_id, f"{text}\n⚠️ (حدث خطأ: {e})")

# ............................................ المغادرة ........................................................................... 
# ............................................ الالعاب ........................................................................... 

@app.on_message(filters.text & filters.group & filters.regex(r"^تخ$"), group=7168912870)
async def send_gif(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    user = await client.get_users(int(user_id))
    gif_url = "https://t.me/uu_u_e/9"
    caption = (
        f"╭◉ᚐ المجرم هو : {message.from_user.mention}\n"
        f"╰⬣ᚐ الضحية : {user.mention}"
    )
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("المرحوم", url=f"https://t.me/{user.username}")]]
    )
    
    await client.send_animation(
        message.chat.id, 
        gif_url,
        caption=caption,
        reply_markup=reply_markup
    )

@app.on_message(filters.text & filters.group & filters.regex(r"^تف$"), group=71122878)
async def send_gf(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    user = await client.get_users(int(user_id))
    gif_url = "https://t.me/uu_u_e/8"
    caption = (
        f"╭◉ᚐ الفاعل هو : {message.from_user.mention}\n"
        f"╰⬣ᚐ المعفن : {user.mention}"
    )
    
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("المعفن", url=f"https://t.me/{user.username}")]]
    )
    
    await client.send_animation(
        message.chat.id, 
        gif_url,
        caption=caption,
        reply_markup=reply_markup
    )

@app.on_message(filters.text & filters.group & filters.regex(r"^مح$"), group=7198878)
async def sed_gf(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif len(message.text.split()) > 2:
        target = message.text.split()[2]
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await client.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    user = await client.get_users(int(user_id))
    gif_url = "https://t.me/uu_u_e/10"
    caption = (
        f"╭◉ᚐ المتحرش هو : {message.from_user.mention}\n"
        f"╰⬣ᚐ الضحيه : {user.mention}"
    )
    
    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("الضحيه", url=f"https://t.me/{user.username}")]]
    )
    
    await client.send_animation(
        message.chat.id, 
        gif_url,
        caption=caption,
        reply_markup=reply_markup
    )


############################################# الالعاب ##################################################
src = []

@app.on_message(filters.command(["قفل التسليه","تعطيل التسليه"], ""), group=258073) 
async def fffcaesar(client, message):
    bot_username = client.me.username
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if message.chat.id in src:
         return await message.reply_text("تم معطل من قبل🔒")
       src.append(message.chat.id)
       return await message.reply_text("تم تعطيل التسليه بنجاح ✅🔒")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")

@app.on_message(filters.command(["فتح التسليه","تفعيل التسليه"], ""), group=7479003) 
async def caesarrf(client, message):
    bot_username = client.me.username
    group_id = message.chat.id
    chek = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not message.chat.id in src:
         return await message.reply_text("االتسليه مفعل من قبل ✅")
       src.remove(message.chat.id)
       return await message.reply_text("تم فتح التسليه بنجاح ✅🔓")
    else:
       return await message.reply_text(f"عزرا عزيزي{message.from_user.mention}\n هذا الامر لا يخصك✨♥")



#..........................................   اخ       ................................................................
akhoia = {}

@app.on_message(filters.command(["رفع اخ"], "") & filters.group, group=36)
async def rf3akhoia(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in akhoia:
        akhoia[user_id] = [] 
    akhoia[user_id].append(reply_name)    
    await message.reply_text(f"تم رفعه اخ🌚\n│ \n└ʙʏ : {reply_name}\n\nاخويه وحبيبي🫂")

@app.on_message(filters.command(["تنزيل اخ"], "") & filters.group, group=37)
async def tnzel_akhoia(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in akhoia and reply_name in akhoia[user_id]:
        akhoia[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيله اخ\n│ \n└ʙʏ : {reply_name}\n\n طلع نقص 😒🙂")
    else:
        await message.reply_text("مش مرفوع اخ اصلا")    

@app.on_message(filters.command(["اخواتي"], "") & filters.group, group=38)
async def akhoia_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in akhoia and akhoia[user_id]: 
        nq = "\n".join(akhoia[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد اخ اصلا")
#..........................................   اخ       ................................................................
#..........................................   جدع       ................................................................
algdan = {}

@app.on_message(filters.command(["رفع جدع"], "") & filters.group, group=105)
async def rf3aalgdan(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in algdan:
        algdan[user_id] = [] 
    algdan[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع جدع🙈\n│ \n└ʙʏ : {reply_name}\n\nابن امي الي مفيش منو اتنين🙈❤️")

@app.on_message(filters.command(["تنزيل جدع"], "") & filters.group, group=106)
async def tnzel_algdan(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in algdan and reply_name in algdan[user_id]:
        algdan[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل جدع😒\n│ \n└ʙʏ : {reply_name}\n\n انت وله ابن امي ولا اعرفك اتفو😒")
    else:
        await message.reply_text("مش مرفوع جدع اصلا")    

@app.on_message(filters.command(["الجدعان"], "") & filters.group, group=107)
async def algdan_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in algdan and algdan[user_id]: 
        nq = "\n".join(algdan[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد جدع اصلا")
#..........................................   جدع       ................................................................
#..........................................   اخت       ................................................................
o1kh1ty = {}

@app.on_message(filters.command(["رفع اخت"], "") & filters.group, group=39)
async def rf3o1kh1ty(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in o1kh1ty:
        o1kh1ty[user_id] = [] 
    o1kh1ty[user_id].append(reply_name)    
    await message.reply_text(f"تم رفعه اخت☺️\n│ \n└ʙʏ : {reply_name}\n\n قلب اختك🫂❤️")

@app.on_message(filters.command(["تنزيل اخت"], "") & filters.group, group=40)
async def tnzel_o1kh1ty(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in o1kh1ty and reply_name in o1kh1ty[user_id]:
        o1kh1ty[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيله اخت😌\n│ \n└ʙʏ : {reply_name}\n\nاخص مكنش العشم فيك😒")
    else:
        await message.reply_text("مش مرفوع اخت اصلا")    

@app.on_message(filters.command(["اخوتي"], "") & filters.group, group=41)
async def o1kh1ty_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in o1kh1ty and o1kh1ty[user_id]: 
        nq = "\n".join(o1kh1ty[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد اخت اصلا")
#..........................................   اخت       ................................................................
#..........................................   بنتي       ................................................................
ban1aty = {}

@app.on_message(filters.command(["رفع بنتي"], "") & filters.group, group=42)
async def rf3ban1aty(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    reply_name = message.reply_to_message.from_user.mention   
    if user_id not in ban1aty:
        ban1aty[user_id] = [] 
    ban1aty[user_id].append(reply_name)    
    await message.reply_text(f"تم رفعه بنتي😊\n│ \n└ʙʏ : {reply_name}\n\n قلب يبنتك كده كده💋😌")

@app.on_message(filters.command(["تنزيل بنتي"], "") & filters.group, group=43)
async def tnzel_ban1aty(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    reply_name = message.reply_to_message.from_user.mention   
    if user_id in ban1aty and reply_name in ban1aty[user_id]:
        ban1aty[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيله بنتي😌\n│ \n└ʙʏ : {reply_name}\n\n بنتك من لحمك ودمك تبعها كده اخص😔🥺")
    else:
        await message.reply_text("مش مرفوع بنتي اصلا")    

@app.on_message(filters.command(["بناتي"], "") & filters.group, group=44)
async def ban1aty_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in ban1aty and ban1aty[user_id]: 
        nq = "\n".join(ban1aty[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد بنتي اصلا")
#..........................................   بنتي       ................................................................
#..........................................   مراتي       ................................................................
mrataty = {}

@app.on_message(filters.command(["رفع مراتي"], "") & filters.group, group=45)
async def rf3mrataty(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in mrataty:
        mrataty[user_id] = [] 
    mrataty[user_id].append(reply_name)    
    await message.reply_text(f"تم رفعه زوجي😉\n│ \n└ʙʏ : {reply_name}\n\n حبيبي وقره عيني🫂😂")

@app.on_message(filters.command(["تنزيل مراتي"], "") & filters.group, group=46)
async def tnzel_mrataty(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in mrataty and reply_name in mrataty[user_id]:
        mrataty[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل مراتى😒\n│ \n└ʙʏ : {reply_name}\n\n طلعت طيزها حمره 😂🌚")
    else:
        await message.reply_text("مش مرفوع مراتي اصلا")    

@app.on_message(filters.command(["مراتاتي"], "") & filters.group, group=47)
async def mrataty_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in mrataty and mrataty[user_id]: 
        nq = "\n".join(mrataty[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد مراتي اصلا")
#..........................................   مراتي       ................................................................
#..........................................   زوجي       ................................................................
zogaty = {}

@app.on_message(filters.command(["رفع زوجي"], "") & filters.group, group=48)
async def rf3zogaty(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in zogaty:
        zogaty[user_id] = [] 
    zogaty[user_id].append(reply_name)    
    await message.reply_text(f"تم رفعه زوجي😉\n│ \n└ʙʏ : {reply_name}\n\n حبيبي وقره عيني🫂😂")

@app.on_message(filters.command(["تنزيل زوجي"], "") & filters.group, group=49)
async def tnzel_zogaty(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in zogaty and reply_name in zogaty[user_id]:
        zogaty[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل زوجي😒\n│ \n└ʙʏ : {reply_name}\n\n طلقتني ياخاين طب والي في بطني😂")
    else:
        await message.reply_text("مش مرفوع زوجي اصلا")    

@app.on_message(filters.command(["ازواجي"], "") & filters.group, group=50)
async def zogaty_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in zogaty and zogaty[user_id]: 
        nq = "\n".join(zogaty[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد زوجي اصلا")
#..........................................   زوجي       ................................................................
#..........................................   ابني       ................................................................
ab1nay = {}

@app.on_message(filters.command(["رفع ابني"], "") & filters.group, group=51)
async def rf3ab1nay(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in ab1nay:
        ab1nay[user_id] = [] 
    ab1nay[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع ابني☺️\n│ \n└ʙʏ : {reply_name}\n\n ابن وحبيبي وابن بطني😁")

@app.on_message(filters.command(["تنزيل ابني"], "") & filters.group, group=52)
async def tnzel_ab1nay(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in ab1nay and reply_name in ab1nay[user_id]:
        ab1nay[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل ابني😔\n│ \n└ʙʏ : {reply_name}\n\n يابني ميتين الكلب اتبريت مني اخص💔")
    else:
        await message.reply_text("مش مرفوع ابني اصلا")    

@app.on_message(filters.command(["ابنائي"], "") & filters.group, group=53)
async def ab1nay_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in ab1nay and ab1nay[user_id]: 
        nq = "\n".join(ab1nay[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد ابني اصلا")
#..........................................   ابني       ................................................................
#..........................................   غبي       ................................................................
agb1iaa = {}

@app.on_message(filters.command(["رفع غبي"], "") & filters.group, group=54)
async def rf3agb1iaa(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in agb1iaa:
        agb1iaa[user_id] = [] 
    agb1iaa[user_id].append(reply_name)    
    await message.reply_text(f"تم رفعه غبي😁\n│ \n└ʙʏ : {reply_name}\n\n وارث الغباء منك نيها نيها😂")

@app.on_message(filters.command(["تنزيل غبي"], "") & filters.group, group=55)
async def tnzel_agb1iaa(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in agb1iaa and reply_name in agb1iaa[user_id]:
        agb1iaa[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل غبي😁\n│ \n└ʙʏ : {reply_name}\n\nالحمدلله اكتشف اني مش غبي😂❤️")
    else:
        await message.reply_text("مش مرفوع غبي اصلا")    

@app.on_message(filters.command(["اغبياء"], "") & filters.group, group=56)
async def agb1iaa_list(client, message):
    user_id = message.from_user.id if message.from_user else "None" 
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in agb1iaa and agb1iaa[user_id]: 
        nq = "\n".join(agb1iaa[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد غبي اصلا")
#..........................................   غبي       ................................................................
#..........................................   اهبل       ................................................................
alh1obl = {}

@app.on_message(filters.command(["رفع اهبل"], "") & filters.group, group=57)
async def rf3alh1obl(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in alh1obl:
        alh1obl[user_id] = [] 
    alh1obl[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع اهبل😁\n│ \n└ʙʏ : {reply_name}\n\n رقم مستشفى المجنين بسرعه 😁")

@app.on_message(filters.command(["تنزيل اهبل"], "") & filters.group, group=58)
async def tnzel_alh1obl(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in alh1obl and reply_name in alh1obl[user_id]:
        alh1obl[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيله اهبل😁\n│ \n└ʙʏ : {reply_name}\n\n اتعلجت الحمدلله💃😁")
    else:
        await message.reply_text("مش مرفوع اهبل اصلا")    

@app.on_message(filters.command(["الهبل"], "") & filters.group, group=59)
async def alh1obl_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in alh1obl and alh1obl[user_id]: 
        nq = "\n".join(alh1obl[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد اهبل اصلا")
#..........................................   اهبل       ................................................................
#..........................................   نمله       ................................................................
nmla = {}

@app.on_message(filters.command(["رفع نمله"], "") & filters.group, group=60)
async def rf3nmla(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in nmla:
        nmla[user_id] = [] 
    nmla[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع نمله😁\n│ \n└ʙʏ : {reply_name}\n\n شوفت نمله عامله عمله😂😂")

@app.on_message(filters.command(["تنزيل نمله"], "") & filters.group, group=61)
async def tnzel_nmla(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in nmla and reply_name in nmla[user_id]:
        nmla[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل النمله\n│ \n└ʙʏ : {reply_name}\n\n الله يرحمه كانت عامله عمله😁")
    else:
        await message.reply_text("مش مرفوع نمله اصلا")    

@app.on_message(filters.command(["النمل"], "") & filters.group, group=62)
async def nmla_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"   
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in nmla and nmla[user_id]: 
        nq = "\n".join(nmla[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد نمله اصلا")
#..........................................   نمله       ................................................................
#..........................................   صرصار       ................................................................
sorsar = {}

@app.on_message(filters.command(["رفع صرصار"], "") & filters.group, group=63)
async def rf3sorsar(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in sorsar:
        sorsar[user_id] = [] 
    sorsar[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع صرصار🪳\n│ \n└ʙʏ : {reply_name}\n\n هاتو شبشب بسرعه 😂 😁")

@app.on_message(filters.command(["تنزيل صرصار"], "") & filters.group, group=64)
async def tnzel_sorsar(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in sorsar and reply_name in sorsar[user_id]:
        sorsar[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل صرصار\n│ \n└ʙʏ : {reply_name}\n\n مات كان طيب🪳🫣")
    else:
        await message.reply_text("مش مرفوع صرصار اصلا")    

@app.on_message(filters.command(["الصارصير"], "") & filters.group, group=65)
async def sorsar_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in sorsar and sorsar[user_id]: 
        nq = "\n".join(sorsar[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد صرصار اصلا")
#..........................................   صرصار       ................................................................
#..........................................   قرد       ................................................................
mon1key = {}

@app.on_message(filters.command(["رفع قرد"], "") & filters.group, group=66)
async def rf3mon1key(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in mon1key:
        mon1key[user_id] = [] 
    mon1key[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع قرد🌚\n│ \n└ʙʏ : {reply_name}\n\nابو طيز حمرا 🍑")

@app.on_message(filters.command(["تنزيل قرد"], "") & filters.group, group=67)
async def tnzel_mon1key(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    reply_name = message.reply_to_message.from_user.mention   
    if user_id in mon1key and reply_name in mon1key[user_id]:
        mon1key[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل القرد🙈\n│ \n└ʙʏ : {reply_name}\n\n يخصاره طلعت مش حمرا😂")
    else:
        await message.reply_text("مش مرفوع قرد اصلا")    

@app.on_message(filters.command(["القرود"], "") & filters.group, group=68)
async def mon1key_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in mon1key and mon1key[user_id]: 
        nq = "\n".join(mon1key[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد قرد اصلا")
#..........................................   قرد       ................................................................
#..........................................   حمار       ................................................................
alhamer = {}

@app.on_message(filters.command(["رفع حمار"], "") & filters.group, group=69)
async def rf3alhamer(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in alhamer:
        alhamer[user_id] = [] 
    alhamer[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع حمار\n│ \n└ʙʏ : {reply_name}\n\n هركبك تع😊")

@app.on_message(filters.command(["تنزيل حمار"], "") & filters.group, group=70)
async def tnzel_alhamer(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    reply_name = message.reply_to_message.from_user.mention   
    if user_id in alhamer and reply_name in alhamer[user_id]:
        alhamer[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل حمار\n│ \n└ʙʏ : {reply_name}\n\n طلعت مش حلو في الركبه😉😂")
    else:
        await message.reply_text("مش مرفوع حمار اصلا")    

@app.on_message(filters.command(["الحمير"], "") & filters.group, group=71)
async def alhamer_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"   
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if user_id in alhamer and alhamer[user_id]: 
        nq = "\n".join(alhamer[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد حمار اصلا")
#..........................................   حمار       ................................................................
#..........................................   خنزير       ................................................................
pi2356g = {}

@app.on_message(filters.command(["رفع خنزير"], "") & filters.group, group=72)
async def rf3pi2356g(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in pi2356g:
        pi2356g[user_id] = [] 
    pi2356g[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {reply_name}\n\n خنزير 😂♥️")

@app.on_message(filters.command(["تنزيل خنزير"], "") & filters.group, group=73)
async def tnzel_pi2356g(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    reply_name = message.reply_to_message.from_user.mention   
    if user_id in pi2356g and reply_name in pi2356g[user_id]:
        pi2356g[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {reply_name}\n\n خنزير 😂♥️")
    else:
        await message.reply_text("مش مرفوع خنزير اصلا")    

@app.on_message(filters.command(["الخنازير"], "") & filters.group, group=74)
async def pi2356g_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return    
    if user_id in pi2356g and pi2356g[user_id]: 
        nq = "\n".join(pi2356g[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد خنزير اصلا")
#..........................................   خنزير       ................................................................
#..........................................   عجل       ................................................................
hu368rry = {}

@app.on_message(filters.command(["رفع عجل"], "") & filters.group, group=75)
async def rf3hu368rry(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in hu368rry:
        hu368rry[user_id] = [] 
    hu368rry[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع عجل\n│ \n└ʙʏ : {reply_name}\n\nحضرو السككين😂")

@app.on_message(filters.command(["تنزيل عجل"], "") & filters.group, group=76)
async def tnzel_hu368rry(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in hu368rry and reply_name in hu368rry[user_id]:
        hu368rry[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل عجل\n│ \n└ʙʏ : {reply_name}\n\n هرب من السلاخانه🙈")
    else:
        await message.reply_text("مش مرفوع عجل اصلا")    

@app.on_message(filters.command(["العجول"], "") & filters.group, group=77)
async def hu368rry_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return    
    if user_id in hu368rry and hu368rry[user_id]: 
        nq = "\n".join(hu368rry[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد عجل اصلا")
#..........................................   عجل       ................................................................
#..........................................   كلب       ................................................................
do467g = {}

@app.on_message(filters.command(["رفع كلب"], "") & filters.group, group=78)
async def rf3do467g(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in do467g:
        do467g[user_id] = [] 
    do467g[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع كلب\n│ \n└ʙʏ : {reply_name}\n\n هوهو وانا اجبلك عضمه😂")

@app.on_message(filters.command(["تنزيل كلب"], "") & filters.group, group=79)
async def tnzel_do467g(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in do467g and reply_name in do467g[user_id]:
        do467g[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل كلب\n│ \n└ʙʏ : {reply_name}\n\n طلع غدار عض الايد الى اكلته😂🌚")
    else:
        await message.reply_text("مش مرفوع كلب اصلا")    

@app.on_message(filters.command(["الكلاب"], "") & filters.group, group=80)
async def do467g_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return  
    if user_id in do467g and do467g[user_id]: 
        nq = "\n".join(do467g[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد كلب اصلا")
#..........................................   كلب       ................................................................
#..........................................   خروف       ................................................................
she578ep = {}

@app.on_message(filters.command(["رفع خروف"], "") & filters.group, group=81)
async def rf3she578ep(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in she578ep:
        she578ep[user_id] = [] 
    she578ep[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع خروف\n│ \n└ʙʏ : {reply_name}\n\nسيب النعجه يا خروف😂")

@app.on_message(filters.command(["تنزيل خروف"], "") & filters.group, group=82)
async def tnzel_she578ep(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in she578ep and reply_name in she578ep[user_id]:
        she578ep[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل خروف😁\n│ \n└ʙʏ : {reply_name}\n\nالنعجه والخروف هربو😂🤦‍♀")
    else:
        await message.reply_text("مش مرفوع خروف اصلا")    

@app.on_message(filters.command(["الخرفان"], "") & filters.group, group=83)
async def she578ep_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return    
    if user_id in she578ep and she578ep[user_id]: 
        nq = "\n".join(she578ep[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد خروف اصلا")
#..........................................   خروف       ................................................................
#..........................................   جاموسه        ................................................................
buf689falo = {}

@app.on_message(filters.command(["رفع جاموسه"], "") & filters.group, group=84)
async def rf3buf689falo(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in buf689falo:
        buf689falo[user_id] = [] 
    buf689falo[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {reply_name}\n\n جاموسه  😂♥️")

@app.on_message(filters.command(["تنزيل جاموسه"], "") & filters.group, group=85)
async def tnzel_buf689falo(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in buf689falo and reply_name in buf689falo[user_id]:
        buf689falo[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {reply_name}\n\n جاموسه  😂♥️")
    else:
        await message.reply_text("مش مرفوع جاموسه  اصلا")    

@app.on_message(filters.command(["الجواميس"], "") & filters.group, group=86)
async def buf689falo_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return    
    if user_id in buf689falo and buf689falo[user_id]: 
        nq = "\n".join(buf689falo[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد جاموسه  اصلا")
#..........................................   جاموسه        ................................................................
#..........................................    خول        ................................................................
yuseaf = {}

@app.on_message(filters.command(["رفع خول"], "") & filters.group, group=87)
async def rf3yuseaf(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in yuseaf:
        yuseaf[user_id] = [] 
    yuseaf[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع خول\n│ \n└ʙʏ : {reply_name}\n\nرفعت الخول وهنيكو😂😂❤️")

@app.on_message(filters.command(["تنزيل خول"], "") & filters.group, group=88)
async def tnzel_yuseaf(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    reply_name = message.reply_to_message.from_user.mention   
    if user_id in yuseaf and reply_name in yuseaf[user_id]:
        yuseaf[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل خول\n│ \n└ʙʏ : {reply_name}\n\n ريحتو ونزلتو عشانك😂😂♥️")
    else:
        await message.reply_text("مش مرفوع  خول  اصلا")    

@app.on_message(filters.command(["الخولات"], "") & filters.group, group=89)
async def yuseaf_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return    
    if user_id in yuseaf and yuseaf[user_id]: 
        nq = "\n".join(yuseaf[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد  خول  اصلا")
#..........................................    خول        ................................................................
#..........................................    متناك        ................................................................
harfosh = {}

@app.on_message(filters.command(["رفع متناك"], "") & filters.group, group=90)
async def rf3harfosh(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in harfosh:
        harfosh[user_id] = [] 
    harfosh[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع متناك\n│ \n└ʙʏ : {reply_name}\n\n رفعتو عشان انيكو😂😂❤️")

@app.on_message(filters.command(["تنزيل متناك"], "") & filters.group, group=91)
async def tnzel_harfosh(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    reply_name = message.reply_to_message.from_user.mention   
    if user_id in harfosh and reply_name in harfosh[user_id]:
        harfosh[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل متناك\n│ \n└ʙʏ : {reply_name}\n\n نيكتو ونزلتو😂♥️")
    else:
        await message.reply_text("مش مرفوع  متناك  اصلا")    

@app.on_message(filters.command(["المتناكين"], "") & filters.group, group=92)
async def harfosh_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return 
    if user_id in harfosh and harfosh[user_id]: 
        nq = "\n".join(harfosh[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد  متناك  اصلا")
#..........................................    متناك        ................................................................
#..........................................    عرص        ................................................................
alhadedy = {}

@app.on_message(filters.command(["رفع عرص"], "") & filters.group, group=93)
async def rf3alhadedy(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    reply_name = message.reply_to_message.from_user.mention
    
    if user_id not in alhadedy:
        alhadedy[user_id] = [] 
    alhadedy[user_id].append(reply_name)
    
    await message.reply_text(f"تم رفع عرص\n│ \n└ʙʏ : {reply_name}\n\n رفعتو عشان يعرصلي😂😂♥️")

@app.on_message(filters.command(["تنزيل عرص"], "") & filters.group, group=94)
async def tnzel_alhadedy(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    reply_name = message.reply_to_message.from_user.mention   
    if user_id in alhadedy and reply_name in alhadedy[user_id]:
        alhadedy[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل عرص\n│ \n└ʙʏ : {reply_name}\n\n علشان بص عليا من خرم الباب😂😂♥️")
    else:
        await message.reply_text("مش مرفوع  عرص  اصلا")    

@app.on_message(filters.command(["المعرصين"], "") & filters.group, group=95)
async def alhadedy_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return   
    if user_id in alhadedy and alhadedy[user_id]: 
        nq = "\n".join(alhadedy[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد  عرص  اصلا")
#..........................................    عرص        ................................................................
#..........................................    نجس        ................................................................
almutamard = {}

@app.on_message(filters.command(["رفع نجس"], "") & filters.group, group=96)
async def rf3almutamard(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    reply_name = message.reply_to_message.from_user.mention   
    if user_id not in almutamard:
        almutamard[user_id] = [] 
    almutamard[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع العضو\n│ \n└ʙʏ : {reply_name}\n\n  نجس  😂♥️")

@app.on_message(filters.command(["تنزيل نجس"], "") & filters.group, group=97)
async def tnzel_almutamard(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    reply_name = message.reply_to_message.from_user.mention  
    if user_id in almutamard and reply_name in almutamard[user_id]:
        almutamard[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل العضو\n│ \n└ʙʏ : {reply_name}\n\n  نجس  😂♥️")
    else:
        await message.reply_text("مش مرفوع  نجس  اصلا")    

@app.on_message(filters.command(["النجسين"], "") & filters.group, group=98)
async def almutamard_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return    
    if user_id in almutamard and almutamard[user_id]: 
        nq = "\n".join(almutamard[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد  نجس  اصلا")
#..........................................    نجس        ................................................................
#..........................................    ديوث        ................................................................
aldayous = {}

@app.on_message(filters.command(["رفع ديوث"], "") & filters.group, group=99)
async def rf3aldayous(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in aldayous:
        aldayous[user_id] = [] 
    aldayous[user_id].append(reply_name)   
    await message.reply_text(f"تم رفع ديوث\n│ \n└ʙʏ : {reply_name}\n\n رفعتو عشان يجيب اختو😂😂♥️")

@app.on_message(filters.command(["تنزيل ديوث"], "") & filters.group, group=100)
async def tnzel_aldayous(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in aldayous and reply_name in aldayous[user_id]:
        aldayous[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل ديوث\n│ \n└ʙʏ : {reply_name}\n\n برا ي كسمك انتا واختك😂😂❤️")
    else:
        await message.reply_text("مش مرفوع  ديوث  اصلا")    

@app.on_message(filters.command(["الديوثين"], "") & filters.group, group=101)
async def aldayous_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return    
    if user_id in aldayous and aldayous[user_id]: 
        nq = "\n".join(aldayous[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد  ديوث  اصلا")
#..........................................    ديوث        ................................................................
#..........................................    شاذ        ................................................................
far1edaa = {}

@app.on_message(filters.command(["رفع شاذ"], "") & filters.group, group=102)
async def rf3far1edaa(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id not in far1edaa:
        far1edaa[user_id] = [] 
    far1edaa[user_id].append(reply_name)    
    await message.reply_text(f"تم رفع شاذ\n│ \n└ʙʏ : {reply_name}\n\nعشان طيزو كبيره😂😂♥️")

@app.on_message(filters.command(["تنزيل شاذ"], "") & filters.group, group=103)
async def tnzel_far1edaa(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return
    if message.reply_to_message.from_user.id == zombie_id:
       return await message.reply_text("**عيب اقدع ده المبرمج محمد صالح 🥷**")    
    reply_name = message.reply_to_message.from_user.mention    
    if user_id in far1edaa and reply_name in far1edaa[user_id]:
        far1edaa[user_id].remove(reply_name)
        await message.reply_text(f"تم تنزيل شاذ\n│ \n└ʙʏ : {reply_name}\n\nعلشان طلعت معفنه😂😂♥️")
    else:
        await message.reply_text("مش مرفوع  شاذ  اصلا")    

@app.on_message(filters.command(["الشاذين"], "") & filters.group, group=104)
async def far1edaa_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    if message.chat.id in src:
      return    
    if user_id in far1edaa and far1edaa[user_id]: 
        nq = "\n".join(far1edaa[user_id])
        await message.reply_text(nq)    
    else:
        await message.reply_text("انت مش رافع حد  شاذ  اصلا")
#..........................................    شاذ        ................................................................
############################################# الالعاب ##################################################

async def start_zombiebot():
    await app.start()
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_zombiebot())