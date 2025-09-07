from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, timedelta 
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
logger = getenv("logger")
OWNER_ID = int(getenv("OWNER_ID"))
OWNEwqr_ID = getenv("OWNER_ID")
appusername = getenv("appusername")
BOT_USERNAME = getenv("appusername")
num_design = getenv("num_design")
session = getenv("STRING_SESSION")
user = Client("zdombie", API_ID, API_HASH, session_string=session)
app = Client("zombie", API_ID, API_HASH, bot_token=BOT_TOKEN)
zombiiee = PyTgCalls(user, cache_duration=100)

translator = Translator()

bot_id = BOT_TOKEN.split(":")[0]

with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

audio_bass = "/root/hamo/"
photo_bot = f"/root/photos/{appusername}.jpg"
BOT_NAME = "حمو"
co_dev_name = config['co_dev_name']
zombie_id = config['zombie_id']
photo_source = config['photo_source']
video_path = config['video_path']
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

###################################################### رفع تلقائي ####################################################
#####################################  المالك والتاك  ##################################################
custom_owners = {}
@app.on_message(filters.command(["تغير المالك", "تغير يوزر المالك", "تغير مالك الجروب"], "") & filters.group, group=11123135)
async def change_owner(client, message):
    try:
        user_id = message.from_user.id if message.from_user else "None"
        allowed = any([
            is_group_owner(message.chat.id, user_id),
            is_main_developer(user_id),
            is_sub_developer(user_id),
            user_id in [OWNER_ID, sourse_dev, zombie_id],
        ])
        if not allowed:
            return await message.reply_text("**◍ تحتاج إلى رتبة مالك على الأقل لإستخدام الأمر\n√**")

        new_owner_id = None
        if message.reply_to_message and message.reply_to_message.from_user:
            user = message.reply_to_message.from_user
            new_owner_id = user.id
        elif len(message.command) > 1:
            target = message.command[1]
            try:
                if target.startswith("@"):
                    user = await client.get_users(target.strip("@"))
                elif target.isdigit():
                    user = await client.get_users(int(target))
                else:
                    return await message.reply("⚠️ يرجى إرسال يوزر صحيح أو رقم ID.")
                new_owner_id = user.id
            except Exception:
                return await message.reply("❌ لا يمكن العثور على المستخدم.")
        else:
            try:
                ask1 = await zom_ask(client, message, "**◍ ارسل الآن يوزر المالك او الايدي الجديد\n√**")
                user = await client.get_users(ask1.text.strip())
                new_owner_id = user.id
            except asyncio.TimeoutError:
                return await message.reply("⏱️ انتهى الوقت. لم يتم التعيين.")
            except Exception:
                return await message.reply("❌ المستخدم غير موجود.")
        chat_id = str(message.chat.id)
        custom_owners[chat_id] = new_owner_id
        await message.reply(
            f"**◍ تم تعيين [{user.first_name}](tg://user?id={user.id}) كمالك جديد للجروب\n√**"
        )
    except Exception as e:
        return await message.reply(f"❌ حدث خطأ: {e}")

@app.on_message(filters.command(["المالك", "صاحب الخرابه"], "") & filters.group, group=25345351)
async def show_owner(client: Client, message: Message):
    chat_id = str(message.chat.id)
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    if chat_id in custom_owners:
        try:
            user_id = custom_owners[chat_id]
            user = await client.get_users(user_id)
            ussfser = await client.get_chat(user.id) 
            key = InlineKeyboardMarkup([[InlineKeyboardButton(user.first_name, user_id=user.id)]])
            if user.photo:
                photo = await client.download_media(user.photo.big_file_id)
                return await message.reply_photo(
                    photo,
                    caption=f"🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{user.first_name}\n"
                            f"🎯 ¦𝚄𝚂𝙴𝚁 :@{user.username or 'لا يوجد'}\n"
                            f"🎃 ¦𝙸𝙳 :`{user.id}`\n"
                            f"💌 ¦𝙱𝙸𝙾 :{ussfser.bio or 'لا يوجد'}\n"
                            f"✨ ¦𝙲𝙷𝙰𝚃 : {message.chat.title}\n"
                            f"♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :`{chat_id}`",
                    reply_markup=key
                )
            else:
                return await message.reply(f"◍ المالك الجديد: {user.mention}", reply_markup=key)
        except Exception as e:
            return await message.reply(f"❌ حدث خطأ أثناء جلب بيانات المالك الجديد {e}")
    async for member in client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.OWNER:
            user = member.user
            key = InlineKeyboardMarkup([[InlineKeyboardButton(user.first_name, user_id=user.id)]])
            try:
                m = await client.get_chat(user.id)
                if m.photo:
                    photo = await client.download_media(m.photo.big_file_id)
                    return await message.reply_photo(
                        photo,
                        caption=f"🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{user.first_name}\n"
                                f"🎯 ¦𝚄𝚂𝙴𝚁 :@{user.username or 'لا يوجد'}\n"
                                f"🎃 ¦𝙸𝙳 :`{user.id}`\n"
                                f"💌 ¦𝙱𝙸𝙾 :{m.bio or 'لا يوجد'}\n"
                                f"✨ ¦𝙲𝙷𝙰𝚃 : {message.chat.title}\n"
                                f"♻️ ¦𝙸𝙳.𝙲𝙷𝙰𝚃 :`{chat_id}`",
                        reply_markup=key
                    )
            except:
                print(e)

takk = []
@app.on_message(filters.command(["تعطيل التاك", "قفل التاك"], "")& filters.group,group=1214745770)
async def takklock(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)  
    if message.text.lower() in ["تعطيل التاك", "قفل التاك"]:
        if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            if message.chat.id in takk:
                return await message.reply_text("**◍ هذا الأمر معطل من قبل 🔐\n√**")
            takk.append(message.chat.id)
            return await message.reply_text("**◍تم تعطيل التاج بنجاح ⚡️\n√**")
        else:
            return await message.reply_text("**◍ ليس لديك الصلاحية لإستخدام هذا الأمر ⛔️\n√**")

@app.on_message(filters.command(["فتح التاك", "تفعيل التاك"], "")& filters.group,group=12755448)
async def takkopen(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.text.lower() in ["تفعيل التاك", "فتح التاك"]:
        if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
            if not message.chat.id in takk:
                return await message.reply_text("**◍ هذا الأمر مفعل من قبل ⚡️\n√**")
            takk.remove(message.chat.id)
            return await message.reply_text("**◍تم تفعيل التاج بنجاح ⚡️\n√**")
        else:
            return await message.reply_text("**◍ ليس لديك الصلاحية لإستخدام هذا الأمر ⛔️\n√**")
        
array = []
@app.on_message(filters.command(["@all", "تاك","تاك للكل"], ""), group=545489708)
async def nummmm(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    if message.chat.id in takk:
        return await message.reply_text("**◍ التاك معطل فى المجموعة قم بتفعيله ⚠️\n√**")

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة الادمن على الأقل لإستخدام الأمر\n√**")
    
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
        if i == 5:
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


@app.on_message(filters.command(["بس المنشن", "/cancel","بس منشن","ايقاف التاك"], ""), group=5454878)
async def stop(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
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
def get_dynamic_selections():
    return [
        f"اسمي {BOT_NAME} ياخي",
        f"قتلك اسمي {BOT_NAME}",
        f"نعم حبي اسمي {BOT_NAME}",
        f"قول يقلب {BOT_NAME}",
        f"يعم فكك مني",
        f"ركز اسمي {BOT_NAME} يمسلم",
        f"نديني {BOT_NAME}",
        f"مش هرد عليك علشان اسمي {BOT_NAME}",
        f"اسمي {BOT_NAME} المطرشم",
        f"انا {BOT_NAME} ابو جلابيه الي مبشوفش",
        f"ينحم اسمي {BOT_NAME}",
        f"هو {BOT_NAME} اسم شركه",
        f"هو اسم {BOT_NAME}",
        f" ولك يفضح عرضك شنو هاي",
        f"ولك يفضح عرضك يزلمه",
        f" انا {BOT_NAME} عجبك",
        f"انا {BOT_NAME} المطرشم",
        f" نديني {BOT_NAME} يحب",
        f"اسمي {BOT_NAME} يصحبي",
        f"سبحااااانه",
        f"رايح مش راجع في طريق كله مواجع"
    ]

async def get_bot_name():
    global BOT_NAME
    return BOT_NAME

@app.on_message(filters.group, group=54100054)
async def trmessage(client, message):
    global BOT_NAME
    if message.from_user and message.text:
        if BOT_NAME.lower() == message.text.lower():
            selections = get_dynamic_selections()
            bar = random.choice(selections)
            await message.reply(
                f'<a href="{channel_source}">{bar}</a>',
                disable_web_page_preview=True
            )

@app.on_message(filters.command(["ضع اسم للبوت 🤖", "تعين اسم البوت"], ""),group=5478789)
async def set_bot(client: Client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    ask1 = await zom_ask(client, message, "**◍ ارسل اسم البوت الجديد الأن 🤖\n√**")
    global BOT_NAME
    BOT_NAME = ask1.text
    await message.reply_text("**◍ تم تعيين اسم البوت بنجاح ✅\n√**")

#################################################### بوت  ###################################################
@app.on_message(filters.command(["بوت", "البوت"], ""), group=5487)
async def botzomnbie(client: Client, message: Message):
    selections = get_dynamic_selections()
    bar = random.choice(selections)
    try:
        chat = await client.get_chat(channel_source)
        channel_title = chat.title
    except Exception as e:
        channel_title = "قناة البوت"
    await message.reply(
        f'**<a href="https://t.me/{channel_source}">{bar}</a>**',
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text=f"{channel_title}", url=f"https://t.me/{channel_source}")]
            ]
        ),
        disable_web_page_preview=True
    )

####################################################  الكول  ###################################################
@app.on_message(filters.regex("مين في الكول"),group=548678)
async def strcall(client, message):
    try:
        await zombiiee.join_group_call(message.chat.id, AudioPiped(f"{audio_bass}audio/me.mp3"), stream_type=StreamType().pulse_stream)
        text="😎🥰 المجانين  المتواجدين في الكول :\n\n"
        participants = await zombiiee.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث 🗣"
            else:
                mut="ساكت 🔕"
            try:
                user = await client.get_users(participant.user_id)
            except Exception as e:
                pass
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
        await asyncio.sleep(4)
        await zombiiee.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"مجنون الكول مش مفتوح اصلااا\n😜")
    except TelegramServerError:
        await message.reply(f"ارسل الامر تاني في مشكله في سيرفر التلجرام\n😜")
    except AlreadyJoinedError:
        text="😎🥰 المجانين  المتواجدين في الكول:\n\n"
        participants = await zombiiee.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يتحدث 🗣"
            else:
                mut="ساكت 🔕"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")

from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall, EditGroupCallParticipant
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat, InputUserSelf, GroupCallParticipant
from typing import Optional


async def get_group_call(
    client: Client, message: Message, err_message: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (
                await client.invoke(GetFullChannel(channel=chat_peer))
            ).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.invoke(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await message.reply_text(f"{err_message}")
    return False

@app.on_message(filters.command("فتح الكول", ""),group=4589721121)
async def vc(c, message):
    hh = await message.reply_text("جاري فتح الكول")   
    if (group_call := await get_group_call(user, message, err_message="الكول مفتوح")):
     await message.reply_text("الكول مفتوح اصلا يليفه")
     return        
    try:
     await user.invoke(CreateGroupCall(peer=(await user.resolve_peer(message.chat.id)), random_id=randint(10000, 999999999)))
     await hh.edit_text("تم فتح الكول بنجاح.")           
    except Exception as e:
     await hh.edit_text(f"قم برفع الحساب المساعد مشرف في الجروب")
  
@app.on_message(filters.command("قفل الكول", ""),group=2312132132)
async def end_vc(c, message):
    hh = await message.reply_text("جاري قفل الكول")   
    if not (group_call := await get_group_call(user, message, err_message="الكول مقفول")):
     await hh.edit_text("الكول مقفول اصلا يليفه")
     return        
    try:
     await user.invoke(EditGroupCallParticipant(call=group_call))
     await hh.edit_text("تم قفل الكول بنجاح.")           
    except Exception as e:
     await hh.edit_text(f"قم برفع الحساب المساعد مشرف في الجروب")

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
                [[InlineKeyboardButton("اضغط هنا للاشتراك بالقناة 🚦", url=f"https://t.me/{channel}")]]
            )
            text = f"🚦 **عذرا عزيزي يجب عليك الاشتراك في القناة أولًا.**\n\n📌 **قناة البوت:**\n➜ [@{channel}](https://t.me/{channel})"
            await client.send_message(chat_id=message.chat.id, text=text, reply_markup=keyboard)
            return False
    return True

@app.on_message(filters.command(["اضف قناة الاشتراك الخاص 📢"], "") & filters.private,group=12124688756)
async def asads_sub(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    if get_premium_status():
        cancel_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
        ])
        ask1 = await zom_ask(client, message, "**◍ أرسل معرف القناة مثال: @ChannelName\n◍ وتأكد من رفع البوت مشرف فالقناة 👮🏻‍♂️\n√**")
        channel_username = ask1.text.strip().replace("@", "")
        add_bot_chanel(channel_username)
        await client.send_message(message.chat.id, f"**◍ تم اضافة القناة للبوت ✅\n√**")
    else:
        await message.reply_text(f"**◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√**")

@app.on_message(filters.command(["حذف قناة الاشتراك الخاص 🗑"], "") & filters.private,group=1982112456)
async def aaddel_sub(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    if get_premium_status():
        cancel_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
        ])
        ask1 = await zom_ask(client, message, "**◍ أرسل معرف القناة مثال: @ChannelName\n√**")
        channel_username = ask1.text.strip().replace("@", "")
        del_bot_chanel(channel_username)
        await client.send_message(message.chat.id, "**◍ تم حذف القناة ❌\n√**")
    else:
        await message.reply_text(f"**◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√**")

  
@app.on_message(filters.command(["قنوات الاشتراك الخاص 📩"], "") & filters.private,group=1531445465)
async def channells(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    if get_premium_status():
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
                [[InlineKeyboardButton("اضغط هنا للاشتراك بالقناة 🚦", url=f"https://t.me/{channel}")]]
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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    if get_premium_status():
        cancel_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
        ])
        ask1 = await zom_ask(client, message, "**◍ أرسل معرف القناة مثال: @ChannelName\n◍ وتأكد من رفع البوت مشرف فالقناة 👮🏻‍♂️\n√**")
        channel_username = ask1.text.strip().replace("@", "")
        add_bot_channel(channel_username)
        await client.send_message(message.chat.id, f"**◍ تم اضافة القناة للبوت ✅\n√**")
    else:
        await message.reply_text(f"**◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√**")

@app.on_message(filters.command("حذف قناة الاشتراك 🗑", "") & filters.private, group=544547)
async def remove_bot_subscription(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    if get_premium_status():
        cancel_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("إلغاء العملية ❌", callback_data="cancel_add")]
        ])
        ask1 = await zom_ask(client, message, "**◍ أرسل معرف القناة مثال: @ChannelName\n√**")
        channel_username = ask1.text.strip().replace("@", "")
        del_bot_channel(channel_username)
        await client.send_message(message.chat.id, f"**◍ تم حذف القناة ❌\n√**")
    else:
        await message.reply_text(f"**◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√**")

@app.on_message(filters.command("قنوات الاشتراك 📥", "") & filters.private, group=54454)
async def list_bot_subscriptions(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    if get_premium_status():
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
    
    ask1 = await zom_ask(client, message, "**◍ أرسل معرف القناة مثال: @ChannelName\n√**")
    channel_username = ask1.text.strip().replace("@", "")
    add_group_channel(message.chat.id, channel_username)
    await client.send_message(message.chat.id, f"✅ تم إضافة القناة @{channel_username} إلى قائمة الاشتراك الإجباري لهذه المجموعة.")

@app.on_message(filters.command("حذف قناه الاشتراك", prefixes="") & filters.group, group=10547)
async def remove_group_subscription(client, message):
    if not await i_group_admin(client, message.chat.id, message.from_user.id):
        return await message.reply("❌ يجب أن تكون مشرفًا في المجموعة لاستخدام هذا الأمر.")
    
    ask1 = await zom_ask(client, message, "**◍ أرسل معرف القناة مثال: @ChannelName\n√**")
    channel_username = ask1.text.strip().replace("@", "")
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
    try:
        if not await check_group_member_status(message.from_user.id, message, client, message.chat.id):
            return
    except Exception as e:
        pass
########################################### الاشتراك الاجباري ################################################
Keyboarddev = ReplyKeyboardMarkup(
  [
    ["🔻 قفل الكيبورد 🔻"],
    ["التفعيل والتعطيل 🔏", "قسم السورس 🚦"],
    ["الاحصائيات 📊"],
    ["قسم الاشتراك الاجباري 🎭", "قسم الاذاعة 🔊"],
    ["ضع اسم للبوت 🤖", "قسم المساعد 🕹"],
    ["المطورين الثانويين 🧑🏻‍💻", "المطورين 🕵🏻‍♂️"],
    ["قسم العام 🚧"],
    ["حذف رد عام 🗑", "اضف رد عام 💬"],
    ["الردود العامة 📝"],
    ["قسم الترويج 💥"],
    ["الاصدار ⚙️", "معلومات السيرفر ℹ️"],
    ["قسم النسخه الاحتياطيه 📥"],
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
    ["تعطيل الاستارت 🚫", "تفعيل الاستارت 🕸"],
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

dev_nbackd = ReplyKeyboardMarkup(
  [
    ["جلب نسخه تلقائي 📯"],
    ["جلب نسخه البنك 🏦", "رفع نسخه البنك 🏦"],
    ["جلب نسخه لايكات 📥", "رفع نسخه لايكات 📤"],
    ["جلب نسخه حمايه 📥", "رفع نسخه حمايه 📤"],
    ["جلب نسخه جروبات 📥", "رفع نسخه جروبات 📤"],
    ["رجوع 🔙"]
  ],
  resize_keyboard=True
)

dev_helper = ReplyKeyboardMarkup(
  [
    ["تغيير المساعد 👤"],
    ["تغيير الاسم ✏️", "تغيير بايو 📄"],
    ["تغيير اليوزر 💥"],
    ["اضافه صوره 🏞", "ازاله صوره 🚫"],
    ["مغادرة كل الجروبات 🛑"],
    ["تعطيل اسم وقتي 📍", "تفعيل اسم وقتي ⏱️"],
    ["تعطيل بايو وقتي 🔺", "تفعيل بايو وقتي 🕰"],
    ["رجوع 🔙"]
  ],
  resize_keyboard=True
)

@app.on_message(filters.regex(r"^مغادرة كل الجروبات 🛑$") & filters.private, group=5860550)
async def leve_all_groups(client: Client, message: Message):
    try:
        await message.reply_text("**◍ جارٍ البحث عن المجموعات والقنوات...\n√**")
        dialogs = []
        async for dialog in user.get_dialogs():
            dialogs.append(dialog)
        groups = [
            d for d in dialogs if d.chat.type in {ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL}
        ]
        total = len(groups)
        left = 0
        errors = 0
        progress = await message.reply_text(
            f"**◍ تم العثور على {total} (مجموعة|قناة)\n◍ جارٍ تنفيذ عملية المغادرة...\n√**"
        )
        for dialog in groups:
            try:
                await user.leave_chat(dialog.chat.id)
                left += 1
            except Exception:
                errors += 1
                continue
            if left % 5 == 0 or left == total:
                await progress.edit_text(
                    f"**◍ تم مغادرة {left}/{total}\n**"
                    f"**◍ عدد الأخطاء: {errors}\n**"
                    f"**√**"
                )
            await asyncio.sleep(1)
        await progress.edit_text(
            f"**◍ تمت المغادرة من جميع المجموعات والقنوات\n**"
            f"**📤 المجموع: {total}\n**"
            f"**✅ غادر: {left}\n**"
            f"**❌ أخطاء: {errors}**"
            f"**√**"
        )
    except Exception as e:
        await message.reply_text(f"❌ حدث خطأ:\n{e}")

@app.on_message(filters.regex(r"^تغيير الاسم ✏️$") & filters.private, group=58650)
async def changefisrt(client: Client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    try:
        ask1 = await zom_ask(client, message, "**◍ ارسل الان الاسم الجديد\n√**")
        name = ask1.text
        await user.update_profile(first_name=name)
        await message.reply_text("**◍ تم تغير اسم الحساب المساعد بنجاح\n√**")
    except Exception as es:
        await message.reply_text(f" حدث خطأ أثناء تغير الاسم \n {es}")

@app.on_message(filters.regex(r"^تغيير بايو 📄$") & filters.private, group=586505)
async def changebio(client: Client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    try:
        ask1 = await zom_ask(client, message, "**◍ ارسل الان البايو الجديد\n√**")
        name = ask1.text
        await user.update_profile(bio=name)
        await message.reply_text("**◍ تم تغير البايو بنجاح\n√**")
    except Exception as es:
        await message.reply_text(f" حدث خطأ أثناء تغير البايو \n {es}")

@app.on_message(filters.regex(r"^تغيير اليوزر 💥$") & filters.private, group=586502)
async def changeusername(client: Client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    try:
        ask1 = await zom_ask(client, message, "**◍ ارسل الان اسم المستخدم الجديد\n◍ مثال : `Hamo`\n√**")
        name = ask1.text
        await user.set_username(name)
        await message.reply_text("**◍ تم تغير اسم المستخدم بنجاح\n√**")
    except Exception as es:
        pass

@app.on_message(filters.regex(r"^اضافه صوره 🏞$") & filters.private, group=5865067)
async def changephoto(client: Client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    try:
        ask1 = await zom_ask(client, message, "**◍ قم بإرسال الصوره الجديده الان\n√**")
        photo = ask1.photo
        photo = await client.download_media(photo)
        await user.set_profile_photo(photo=photo)
        await message.reply_text("**◍ تم تغير صوره الحساب المساعد بنجاح\n√**") 
    except Exception as es:
        pass

@app.on_message(filters.regex(r"^ازاله صوره 🚫$") & filters.private, group=541133)
async def change_photo(client: Client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    try:
        ask1 = await zom_ask(client, message, "**◍ قم بإرسال رقم الصورة التي تريد حذفها الآن\n◍ مثال : `1`\n√**")
        number = int(ask1.text.strip())
        photos = []
        async for p in user.get_chat_photos("me"):
            photos.append(p)
        if number < 1 or number > len(photos):
            return await message.reply_text(f"**◍ لا توجد صورة بهذا الرقم عدد الصور: {len(photos)}\n√**")
        await user.delete_profile_photos(photos[number - 1].file_id)
        await message.reply_text(f"**◍ تم حذف الصورة رقم {number} بنجاح\n√**")
    except Exception as es:
        pass

@app.on_message(filters.regex(r"^قسم المساعد 🕹$") & filters.private)
async def iqwdofus(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي │⎋ اليك قسم التحكم في المساعد", reply_markup=dev_helper)

@app.on_message(filters.regex(r"^قسم العام 🚧$") & filters.private)
async def iqwsaawus(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي │⎋ اليك قسم التحكم في المساعد", reply_markup=glsobal_ban)

@app.on_message(filters.regex(r"^قسم السورس 🚦$") & filters.private)
async def iWQqws(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    await message.reply("**💌╖أهلا بك عزيزي في قسم السورس\n🔰╢ تقدر تغير حقوق بوتك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة السورس دوس هنا**", reply_markup=Dev_kSouoard)

@app.on_message(filters.regex(r"^قسم النسخه الاحتياطيه 📥$") & filters.private)
async def irqrwQqws(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    await message.reply("**💌╖أهلا بك عزيزي في قسم النسخ الاحتياطيه\n🔰╢ تقدر تجيب النسخ الاحتياطيه عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة السورس دوس هنا**", reply_markup=dev_nbackd)

@app.on_message(filters.regex(r"^التفعيل والتعطيل 🔏$") & filters.private)
async def iofrewus(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
    await message.reply("**💌╖أهلا بك في قسم التفعيل والتعطيل\n📲╢ تقدر تتحكم في مهام بوتك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة السورس دوس هنا**", reply_markup=enableaa)

@app.on_message(filters.regex(r"^قسم الاشتراك الاجباري 🎭$") & filters.private)
async def iqwofdus(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    await message.reply("╮⦿ اليك قسم الاشتراك الاجباري", reply_markup=mustjoin)

@app.on_message(filters.regex(r"^قسم الاذاعة 🔊$") & filters.private)
async def iofawus(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
    await message.reply("╮⦿ اليك قسم الاذاعة", reply_markup=prodcast)

@app.on_message(filters.regex(r"^قسم الترويج 💥$") & filters.private)
async def iofawqweus(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
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

@app.on_message(filters.regex(r"^معلومات السيرفر ℹ️$") & filters.private)
async def server_info(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
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

async def restart_assistant(session_string):
    global user, zombiiee

    try:
        await user.stop()
        await zombiiee.stop()
    except:
        pass
    for file in ["zdombie.session", "zdombie.session-journal", "zdombie.session-wal", "zdombie.session-shm"]:
        if os.path.exists(file):
            os.remove(file)

    user = Client("zdombie", session_string=session_string, api_id=API_ID, api_hash=API_HASH)
    await user.start()

    zombiiee = PyTgCalls(user, cache_duration=100)
    await zombiiee.start()
    print("✅ تم إعادة تشغيل الحساب المساعد")

@app.on_message(filters.command(["تغيير المساعد"], "") & filters.private, group=1500201676)
async def change_assistant(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور اساسي على الأقل لإستخدام الأمر\n√**")

    ask1 = await zom_ask(client, message, "**◍ أرسل الجلسة الجديدة الآن\n√**")
    session = ask1.text
    await restart_assistant(session)
    await message.reply("✅ تم تغيير الحساب المساعد وتشغيله بنجاح")


@app.on_message(filters.regex(r"^سرعة السيرفر 🚀$") & filters.private)
async def speed_test(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
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


@app.on_message(filters.regex(r"^الاصدار ⚙️$") & filters.private)
async def show_version(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
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

@app.on_message(filters.regex(r"^تحديث السورس 📥$") & filters.private)
async def update_source(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
    progress_msg = await message.reply("🔄 **جاري تحديث السورس...**")    
    for i in range(1, 4):
        await asyncio.sleep(1)
        await progress_msg.edit(f"🔄 **جاري تحديث السورس...** {i*25}%")
    await asyncio.sleep(1)
    await progress_msg.edit("✅ **تم التحديث بنجاح!**\n\n✨ تم تحديث السورس إلى أحدث إصدار")

@app.on_message(filters.regex(r"^رستر البوت ♻️$") & filters.private)
async def restart_bot(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
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

@app.on_message(filters.regex("يشسيشسيشسيشسيشيشس") & filters.private, group=7113)
async def set_bot_name(client, message):
    global source_devv
    if message.from_user.id in dev or message.from_user.id == OWNER_ID or message.from_user.id == sourse_dev:
        ask1 = await zom_ask(client, message, "**◍ ارسل يوزر مطور السورس بدون علامه@\n√**")
        source_devv = ask1.text
        await message.reply_text("تم تعيين يوزر مطور السورس",disable_web_page_preview=True)
    else:
        await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**",disable_web_page_preview=True)
       
@app.on_message(filters.regex("تعيين قناة السورس 📣") & filters.private, group=71113)
async def set_bot_channel_source(client, message):
    global channel_source
    if get_premium_status() and message.from_user.id == OWNER_ID or message.from_user.id in dev or message.from_user.id == sourse_dev:
        if message.from_user.id in dev or message.from_user.id == OWNER_ID or message.from_user.id == sourse_dev:
            ask1 = await zom_ask(client, message, "**◍ ارسل يوزر قناة السورس مثل [@Channal] 👥\n√**")
            channel_source = ask1.text.strip().replace("@", "")
            await message.reply_text("**◍ تم تعيين قناة السورس بنجاح ⚡️\n√**",disable_web_page_preview=True)
        else:
            await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**",disable_web_page_preview=True)
    else:
        await message.reply_text(f"****◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√****")

@app.on_message(filters.regex("تعيين جروب السورس 👥") & filters.private, group=71213)
async def set_bot_gr(client, message):
    global gr
    if get_premium_status() and message.from_user.id == OWNER_ID or message.from_user.id in dev or message.from_user.id == sourse_dev:
        if message.from_user.id in dev or message.from_user.id == OWNER_ID or message.from_user.id == sourse_dev:
            ask1 = await zom_ask(client, message, "**◍ ارسل يوزر جروب السورس مثل [@Channal] 👥\n√**")
            gr = ask1.text.strip().replace("@", "")
            await message.reply_text("**◍ تم تعيين جروب السورس بنجاح ⚡️\n√**",disable_web_page_preview=True)
        else:
            await message.reply_text("**◍ ليس لديك الصلاحية لفعل ذلك 🚦\n√**",disable_web_page_preview=True)
    else:
        await message.reply_text(f"****◍ عذرا عزيزي هذا الامر خاص بقسم المدفوع 🖱\n◍ تواصل مع مطور السورس للاشتراك 💸\n√****")

@app.on_message(filters.regex("بسششسيبسبس") & filters.private, group=712513)
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
        
        output_filename = f"start_{BOT_USERNAME}.png"
        if os.path.exists(output_filename):
            return output_filename

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
            font_large = ImageFont.truetype("font.ttf", 70)
            font_medium = ImageFont.truetype("font.ttf", 40)
            font_small = ImageFont.truetype("font2.ttf", 40)
            draw.text((600, 150), " Music Player BoT", fill="white", stroke_width=1, stroke_fill="white", font=font_large)
            draw.text((600, 280), " Playing Music & Video", fill="white", stroke_width=1, stroke_fill="white", font=font_medium)
            draw.text((600, 340), f" Dev : Dev ZoMbie", fill="white", stroke_width=1, stroke_fill="white", font=font_medium)
            background.save(output_filename)
            return output_filename
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


start_enabled = True

@app.on_message(filters.command(["تفعيل الاستارت 🕸"], "") & filters.private, group=874641314)
async def enable_start(client, message):
    global start_enabled
    user_id = message.from_user.id if message.from_user else "None"
    if message.from_user.id == OWNER_ID or is_main_developer(user_id):
        start_enabled = True
        await message.reply("**◍ تم تفعيل الاستارت بنجاح\n√**")
    else:
        await message.reply("**◍ تحتاج رتبه مطور اساسي علي الاقل\n√**")

@app.on_message(filters.command(["تعطيل الاستارت 🚫"], "") & filters.private, group=15947201676)
async def disable_start(client, message):
    global start_enabled
    user_id = message.from_user.id if message.from_user else "None"
    if message.from_user.id == OWNER_ID or is_main_developer(user_id):
        start_enabled = False
        await message.reply("**◍ تم تعطيل الاستارت بنجاح\n√**")
    else:
        await message.reply("**◍ تحتاج رتبه مطور اساسي علي الاقل\n√**")


@app.on_message(filters.command(["/start", "رجوع 🔙"], "") & filters.private, group=1201676)
async def for_users(app, message):
    global channel_source, photo_source, channel_userss, start_enabled
    bot_username = (await app.get_me()).username
    CASER = bot_username
    photo = await gen_ot(CASER, message)
    user_id = message.from_user.id if message.from_user else "None"
    try:
        if message.from_user.id in dev or message.from_user.id == sourse_dev:
            await message.reply_text(f"مرحبا بك مطور السورس {message.from_user.mention} اليك كيب التحكم بالبوت", reply_markup=Keyboarddev)
            return
        elif message.from_user.id == OWNER_ID or is_main_developer(user_id) or is_sub_developer(user_id):
            await message.reply_text(f'💌╖أهلا بك عزيزي المطور `{message.from_user.mention}`\n🕹╢ تقدر تتحكم في بوتك عن طريق\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\n🚪╜ للدخول لقناة السورس <a href="https://t.me/uu_u_e">دوس هنا</a>', reply_markup=Keyboarddev)
            return
        else:
            is_subscribed = await check_chat_member_status(message.from_user.id, message, app)
            if not is_subscribed:
                return False
            if not start_enabled:
                return
            await message.reply_photo(
                photo=photo,
                caption=f"""**
⍟ 𝗧𝗵𝗲 𝗕𝗲𝘀𝘁 𝗦𝗼𝘂𝗿𝗰𝗲 𝗢𝗻 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺
**""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("English 🇬🇧", callback_data="english"),
                            InlineKeyboardButton("عـــربـــي 🇪🇬", callback_data="arbk")
                        ],
                    ]
                )
            )
            kep = ReplyKeyboardMarkup([["السورس🚦"], ["المطور 👨🏻‍💻", "مطور السورس 🕵🏻‍♂️"], ["اقتباس 💬", "قران 🕋"], ["تويت 🕊", "صراحة 💭"], ["متحركه 🎬", "استوريهات 📱"], ["أعلام 🇪🇬", "ممثلين 🕺🏻"], ["مشاهير 🎩", "فزورة 🎭"], ["نكتة 😹", "المختلف 🧠"], ["لاعبين ⛹🏻‍♂️", "مغنين 👨‍🎤"], ["صور 🖼", "انمي 🪭"], ["صور بنات 🧚🏻‍♀️", "صور شباب 🧜🏻‍♂️"]], resize_keyboard=True)
            await message.reply_text("** صلي علي النبي محمد ❤️ **",reply_markup=kep)
    except Exception as e:
        pass

@app.on_callback_query(filters.regex(pattern=r"^(arbk|english)$"))
async def admin_r98hts(client: Client, CallbackQuery):
    bot = await client.get_me()
    bot_username = bot.username
    usr1 = await client.get_chat(OWNER_ID)
    wenru = usr1.username
    namew = usr1.first_name
    command = CallbackQuery.matches[0].group(1)
    if command == "arbk":
        buttons = [
            [InlineKeyboardButton("اضف البوت الى مجموعتك ✅", url=f"https://t.me/{bot_username}?startgroup=new")],
            [InlineKeyboardButton("القناة", url=f"https://t.me/{channel_source}"), InlineKeyboardButton("الجروب", url=f"https://t.me/{gr}")],
            [InlineKeyboardButton(f"{namew}", url=f"https://t.me/{wenru}")]
        ]
        await CallbackQuery.answer("مرحبا بك في قسم اللغة العربية 🎧", show_alert=True)
        await CallbackQuery.edit_message_text(
            f"""**- مرحباً عزيزي {CallbackQuery.from_user.mention} 💌
- أنا بوت أقوم بتشغيل الموسيقى وحماية المجموعات ⚡️
- قُم بإضافتي إلى مجموعتك أو قناتك ✅
- سيتم تفعيلي وسينضم المساعد تلقائياً 🚀
- وفي حال واجهتك مشكلة تواصل مع المطور 🕵🏻‍♂️
- استخدم الأزرار بالأسفل لمعرفة كيفية التشغيل 🚦**""",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    elif command == "english":
        buttons = [
            [InlineKeyboardButton("Add the bot to your group 🚦", url=f"https://t.me/{bot_username}?startgroup=true")],
            [InlineKeyboardButton("ᏟᎻᎪŃŃᎬᏞ", url=f"https://t.me/{channel_source}"), InlineKeyboardButton("ᏀᎡØႮᏢ", url=f"https://t.me/{gr}")],
            [InlineKeyboardButton(f"{namew}", url=f"https://t.me/{wenru}")]
        ]
        await CallbackQuery.answer("Welcome to the English section 🎧", show_alert=True)
        await CallbackQuery.edit_message_text(
            f"""**- Hello {CallbackQuery.from_user.mention} 💌
- I'm a music bot that plays audio & video in voice chats ⚡️
- Add me to your group or channel ✅
- I will activate automatically and the assistant will join 🚀
- If you face any issue, contact the developer 🕵🏻‍♂️
- Use the buttons below to see usage commands 🚦**""",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

#..................................................... تواصل ...........................................


twaseeel = False

@app.on_message(filters.command(["تفعيل التواصل ⚡️"], "") & filters.private, group=713877765578)
async def hable_twasell(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
    global twaseeel
    twaseeel = True
    await app.send_message(message.chat.id, f"**◍ تم تفعيل التواصل بنجاح 📱\n√**")
    
@app.on_message(filters.command(["تعطيل التواصل 🔰"], "") & filters.private, group=713977578)
async def yble_twasell(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
    global twaseeel
    twaseeel = False
    await app.send_message(message.chat.id, f"**◍ تم تعطيل التواصل بنجاح 📲\n√**")


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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
    ask1 = await zom_ask(client, message, "**◍ ارسل النص المراد اذاعته\n√**")
    text = ask1.text
    ask1 = await zom_ask(client, message, "**◍ اذا كنت تريد الاذاعة بالتثبيت ارسل `نعم`\n√**")
    pin_message = ask1.text.lower() == "نعم"
    users = users_collection.find({"_id": {"$ne": "bot_stats"}})
    sent_count = 0
    for user in users:
        user_id = user["user_id"]
        try:
            msg = await client.send_message(user_id, text)
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
            sent_count += 1
        except Exception as e:
            print(f"Error sending message to user {user_id}: {e}")
    await message.reply(
        f"**◍ تم إرسال الإذاعة بنجاح\n"
        f"**◍ عدد المستخدمين: {sent_count}**\n"
        f"**√**"
    )

@app.on_message(filters.command(["اذاعة بالتوجية للمستخدمين 〽️"], "") & filters.private, group=548178744544)
async def broadcast_mese_message(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
    ask1 = await zom_ask(client, message, "**◍ ارسل الرسالة الموجهة الآن\n√**")
    if not ask1:
        return await message.reply("❌ لم يتم إرسال أي رسالة.")
    users = users_collection.find({"_id": {"$ne": "bot_stats"}})
    for user in users:
        user_id = user["user_id"]
        try:
            await ask1.forward(user_id)
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

new_gr = []
@app.on_message(filters.new_chat_members, group=6998788854)
async def groasdsss_me(client, message):
    group_id = message.chat.id
    group_name = message.chat.title
    if group_id in new_gr:
        return
    lefSt_user = message.new_chat_members
    for user in message.new_chat_members:
        if user.id == (await client.get_me()).id:

            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("𝑪𝒉𝒂𝒏𝒏𝒆𝒍", url=f"https://t.me/{channel_source}"),
                        InlineKeyboardButton("𝑮𝒓𝒐𝒖𝒑", url=f"https://t.me/{gr}"),
                    ],
                    [
                        InlineKeyboardButton("اضف البوت الى مجموعتك ✅", url=f"https://t.me/{appusername}?startgroup=new"),
                    ],
                ]
            )
            bot_username = (await app.get_me()).username
            CASER = bot_username
            photo = await gen_ot(CASER, message)
            welcome_caption = f"""**
• استطيع تشغيل الاغاني فالكول
• واعمل علي حـمايه الجروبـات
• يمكنك اضافتي إلى قناتك أو مجموعتك
• اعمل بسرعه 100 Mbps في الثانية
• لدي الالعاب كثير (بنك. كت. تويت. رو)
• تحميل من اليوتيوب بالخاص أو المجموعة
**"""
            if not photo:
                return await message.reply("⚠️ تعذر توليد صورة الترحيب.")

            try:
                await client.send_photo(
                    chat_id=message.chat.id,
                    photo=photo,
                    caption=welcome_caption,
                    reply_markup=reply_markup
                )
            except Exception as e:
                await message.reply(f"❌ خطأ أثناء إرسال الصورة: {type(e).__name__} - {e}")

@app.on_message(filters.left_chat_member, group=25354650)
async def leavawwae(client: Client, message: Message):
    chat_id = message.chat.id
    left_user = message.left_chat_member
    if left_user.id == (await client.get_me()).id:
        if chat_id in new_gr:
            new_gr.remove(chat_id)
            new_group.remove(chat_id)

new_group = []
@app.on_message(filters.text & filters.group, group=69954788854)
async def gdsss_e(client, message):
    group_id = message.chat.id
    if group_id in new_group:
        return

    bot_user = await client.get_me()
    bot_member = await client.get_chat_member(group_id, bot_user.id)

    if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
        new_group.append(group_id)

        admin_count = 0
        owner_id = None

        async for member in client.get_chat_members(group_id, filter=ChatMembersFilter.ADMINISTRATORS):
            if member.status == ChatMemberStatus.ADMINISTRATOR:
                add_group_admin(group_id, member.user.id)
                admin_count += 1
            elif member.status == ChatMemberStatus.OWNER:
                add_group_owner(group_id, member.user.id)
                owner_id = member.user.id

        await message.reply_text(
            f"**◍ تم تفعيل الجروب\n**"
            f"**◍ تم رفع `{admin_count}` من الادمنيه فى البوت\n**"
            f"**{'◍ تم رفع المالك بنجاح' if owner_id else ''}\n**"
            f"**√**"
        )

@app.on_message(filters.group & filters.regex(r"^تفعيل$"), group=75412878)
async def gdsass_e(client, message):
    group_id = message.chat.id
    group_name = message.chat.title
    group_username = message.chat.username 
    if group_id in new_group:
        link = f"https://t.me/{group_username}" if group_username else ""
        await message.reply_text(
            f'**◍ المجموعه : <a href="{link}">{group_name}</a>\n**'
            f'**◍ تم تفعيلها مسبقا**\n'
            f'**√**'
        )
        return

    bot_user = await client.get_me()
    bot_member = await client.get_chat_member(group_id, bot_user.id)

    if bot_member.status == ChatMemberStatus.ADMINISTRATOR:
        new_group.append(group_id)

        admin_count = 0
        owner_id = None

        async for member in client.get_chat_members(group_id, filter=ChatMembersFilter.ADMINISTRATORS):
            if member.status == ChatMemberStatus.ADMINISTRATOR:
                add_group_admin(group_id, member.user.id)
                admin_count += 1
            elif member.status == ChatMemberStatus.OWNER:
                add_group_owner(group_id, member.user.id)
                owner_id = member.user.id

        await message.reply_text(
            f"**◍ تم تفعيل الجروب\n**"
            f"**◍ تم رفع `{admin_count}` من الادمنيه فى البوت\n**"
            f"**{'◍ تم رفع المالك بنجاح' if owner_id else ''}\n**"
            f"**√**"
        )


@app.on_message(filters.command(["رفع الادمنيه","رفع الادمنية"], "") & filters.group, group=51214544)
async def gdassqe(client, message):
    group_id = message.chat.id
    bot_user = await client.get_me()
    bot_member = await client.get_chat_member(group_id, bot_user.id)
    admin_count = 0
    owner_id = None
    async for member in client.get_chat_members(group_id, filter=ChatMembersFilter.ADMINISTRATORS):
        if member.status == ChatMemberStatus.ADMINISTRATOR:
            add_group_admin(group_id, member.user.id)
            admin_count += 1
    await message.reply_text(
        f"**◍ تم رفع `{admin_count}` من الادمنيه فى البوت\n**"
        f"**√**"
    )

@app.on_message(filters.command(["اذاعة للجروبات 👥"], "") & filters.private, group=512531544)
async def broadcast_groups_message(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")

    ask1 = await zom_ask(client, message, "**◍ ارسل النص المراد اذاعته\n√**")
    text = ask1.text
    ask1 = await zom_ask(client, message, "**◍ اذا كنت تريد الاذاعة بالتثبيت ارسل `نعم`\n√**")
    pin_message = ask1.text.lower() == "نعم"
    groups = groups_collection.find({"_id": {"$ne": "bot_stats"}})
    for group in groups:
        group_id = group["group_id"]
        try:
            msg = await client.send_message(group_id, text)
            if pin_message:
                await msg.pin(disable_notification=False, both_sides=True)
        except Exception as e:
            print(f"Error sending message to group {group_id}: {e}")
    await message.reply("**◍ تم إرسال الإذاعة لجميع الجروبات\n√**")

@app.on_message(filters.command(["اذاعة بالتوجية للجروبات 🔂"], "") & filters.private, group=5497828544)
async def broadcast_forward_groups(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")

    ask1 = await zom_ask(client, message, "**◍ ارسل الرسالة الموجهة الآن\n√**")
    if not ask1:
        return await message.reply("❌ لم يتم إرسال أي رسالة.")
    groups = groups_collection.find({"_id": {"$ne": "bot_stats"}})
    for group in groups:
        group_id = group["group_id"]
        try:
            await ask1.forward(group_id)
        except Exception as e:
            print(f"Error forwarding message to group {group_id}: {e}")
    await message.reply("**◍ تم إرسال الإذاعة لجميع الجروبات\n√**")
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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
    ask1 = await zom_ask(client, message, "**◍ ارسل النص المراد اذاعته\n√**")
    text = ask1.text
    ask1 = await zom_ask(client, message, "**◍ اذا كنت تريد الاذاعة بالتثبيت ارسل `نعم`\n√**")
    pin_message = ask1.text.lower() == "نعم"
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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
    ask1 = await zom_ask(client, message, "**◍ ارسل الرسالة الموجهة الآن\n√**")
    if not ask1:
        return await message.reply("❌ لم يتم إرسال أي رسالة.")
    channels = channels_collection.find({"_id": {"$ne": "bot_stats"}})
    for channel in channels:
        channel_id = channel["channel_id"]
        try:
            await ask1.forward(channel_id)
        except Exception as e:
            print(f"Error forwarding message to channel {channel_id}: {e}")
    await message.reply("✅ تم إرسال الإذاعة لجميع القنوات!")

@app.on_message(filters.command(["ترويج للميوزك 🎸", "ترويج الميوزك"], ""), group=1588024)
async def promote_music_bot(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
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
        [InlineKeyboardButton("أضف البوت إلى مجموعتك أو قناتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
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

@app.on_message(filters.command(["ترويج الحماية", "ترويج للحماية 🛡"], "") & filters.private, group=158024)
async def prom_music_bot(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
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
        [InlineKeyboardButton("أضف البوت إلى مجموعتك أو قناتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
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

@app.on_message(filters.command(["ترويج الاذان", "ترويج للاذان 🕌"], "") & filters.private, group=158023424)
async def p_music_bot(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
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
        [InlineKeyboardButton("أضف البوت إلى مجموعتك أو قناتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
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

@app.on_message(filters.command(["ترويج السماح بالتحدث", "ترويج السماح بالتحدث 🗣"], "")& filters.private, group=1893424)
async def psic_bot(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
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
        [InlineKeyboardButton("أضف البوت إلى مجموعتك أو قناتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")]
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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
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

@app.on_message(filters.command(["سورس","السورس","سورس ⚡️","السورس🚦"], "") & (filters.private | filters.group), group=54587)
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
        video="https://t.me/uu_u_e/29",
        caption="""⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("ᏟᎻᎪΝΝᎬᏞ", url=f"https://t.me/{channel_source}"),
                InlineKeyboardButton("ᏀᎡØႮᏢ", url=f"https://t.me/{gr}")
            ],
            [
                InlineKeyboardButton(f"محمد صالح�", url=f"https://t.me/R_9_9_0")
            ],
            [
                InlineKeyboardButton("اضف البوت الى مجموعتك ✅", url=f"https://t.me/{appusername}?startgroup=new")
            ],
        ]),
    )

collection_premium = db[f"premium_status_{BOT_USERNAME}"]

def set_premium_status(status: bool):
    collection_premium.update_one({}, {"$set": {"premium": status}}, upsert=True)

def get_premium_status():
    premium_data = collection_premium.find_one({})
    return premium_data.get("premium", False) if premium_data else False

        
@app.on_message(filters.command(["الاوامر","اوامر السورس","اوامر البوت"], "") & (filters.private | filters.group), group=73)
async def kggalid(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    bot_username = (await app.get_me()).username
    CASER = bot_username
    photo = await gen_ot(CASER, message)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("أوامر المطور 🕵🏻‍♂️", callback_data="m1 " + str(message.from_user.id))],
        [InlineKeyboardButton("أوامر الحماية 🛡", callback_data="m2 " + str(message.from_user.id))] +
        [InlineKeyboardButton("أوامر الميوزك 🎸", callback_data="m3 " + str(message.from_user.id))],
        [InlineKeyboardButton("أوامر الرتب 🚦", callback_data="m4 " + str(message.from_user.id))],
        [InlineKeyboardButton("أوامر الأعضاء 🔰", callback_data="m5 " + str(message.from_user.id))],
        [InlineKeyboardButton("أوامر التسلية 🎭", callback_data="m566 " + str(message.from_user.id))] +
        [InlineKeyboardButton("أوامر الألعاب 🎲", callback_data="m7 " + str(message.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await message.reply_photo(
        photo=photo,
        caption=f"""**
⁣💌- 𝗪𝗲𝗹𝗰𝗼𝗺𝗲  ⁽ {message.from_user.mention} ⁾
⁣⁣⁣⁣⤸ إليك قائمة الأوامر الخاصة بي 📚
┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅
⚡- 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 𝗕𝘆  ⁽ <a href="https://t.me/R_9_9_0">🪫محمد صالح🎫</a> ⁾
**""",
        reply_markup=keyboard
    )
   

@app.on_callback_query(filters.regex("^command (\\d+)$"))
async def command(c: Client, m: Message):
    global mid
    mid = m.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("أوامر المطور 🕵🏻‍♂️", callback_data="m1 " + str(m.from_user.id))],
        [InlineKeyboardButton("أوامر الحماية 🛡", callback_data="m2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أوامر الميوزك 🎸", callback_data="m3 " + str(m.from_user.id))],
        [InlineKeyboardButton("أوامر الرتب 🚦", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("أوامر الأعضاء 🔰", callback_data="m5 " + str(m.from_user.id))],
        [InlineKeyboardButton("أوامر التسلية 🎭", callback_data="m566 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أوامر الألعاب 🎲", callback_data="m7 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_caption(
        caption=f"""**
💌- 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 ⁽ {m.from_user.mention} ⁾
⤸ إليك قائمة الأوامر الخاصة بي 📚
┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅
⚡- 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 𝗕𝘆 ⁽ <a href="https://t.me/R_9_9_0">🪫محمد صالح🎫</a> ⁾
**""",
        reply_markup=keyboard
    )
    await m.answer()

@app.on_callback_query(filters.regex("^m7 (\\d+)$"))
async def m7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("🔙️", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
🎮╖ « أوامر الالعاب » ⇊
🎯╜ « الالعاب التقليديه » ⇊
═══════ ××× ═══════ٴ
⭕️╖ اكس او «» اكس
✊╢ حجره ورقه مقص «» حجره
💬╢ اسالني
✅╜ صح وغلط
═══════ ××× ═══════ٴ
🏦 « اوامر لعبه البنك » ⇊
═══════ ××× ═══════ٴ
👮‍♂️ « المطور » ⇊
➕╖ اضف فلوس + المبلغ «» ❬ بالرد علي الشخص المراد اضافه الفلوس له ❭
🗑╢ حذف حسابه «» ❬ بالرد علي الشخص المراد حذف حسابه ❭
❌╢ حذف حساب + اليوزر «» ❬ لحذف حساب الشخص ❭
😵╜ تصفير البنك «» ❬ لمسح كل الحسابات ❭

👨‍🦳 « الاعضاء » ⇊
═══════ ××× ═══════ٴ
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
═══════ ××× ═══════ٴ
    """, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^command2 (\\d+)$"))
async def command2(c: Client, m: CallbackQuery):
    mid = m.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("أوامر المطور 🕵🏻‍♂️", callback_data="m1 " + str(m.from_user.id))],
        [InlineKeyboardButton("أوامر الحماية 🛡", callback_data="m2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أوامر الميوزك 🎸", callback_data="m3 " + str(m.from_user.id))],
        [InlineKeyboardButton("أوامر الرتب 🚦", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("أوامر الأعضاء 🔰", callback_data="m5 " + str(m.from_user.id))],
        [InlineKeyboardButton("أوامر التسلية 🎭", callback_data="m566 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أوامر الألعاب 🎲", callback_data="m7 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_caption(
        caption=f"""**
💌- 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 ⁽ {m.from_user.mention} ⁾
⤸ إليك قائمة الأوامر الخاصة بي 📚
┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅
⚡- 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 𝗕𝘆 ⁽ <a href="https://t.me/R_9_9_0">🪫محمد صالح🎫</a> ⁾
**""",
        reply_markup=keyboard
    )
    await m.answer()


@app.on_callback_query(filters.regex("^m1 (\\d+)$"))
async def m1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("🔙", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
🎖╖ « أوامر المطورين » ⇊
👨🏻‍💻╜ « المطور الثانوي » ⇊
═══════ ××× ═══════ٴ
✅╖ التفعيل والتعطيل داخل البوت
📑╢ اضف «» حذف رد عام
🤴╢ رفع «» تنزيل ❬ الرتب الأقل منة ❭
💎╢ مسح ❬ المميزين ,,, المنشئين ❭
🗃╢ الردود العامه
📝╢ حذف الردود العامه
🔉╢ جميع أنواع الاذاعه
⏳╢ الاحصائيات
💥╢ الترويج
🕌╢ تفعيل / تعطيل ❬ الاذان ❭
📚╜ ❬ + ❭ جميع ماسبق
═══════ ××× ═══════ٴ
🕵🏻‍♂️ « المطور الأساسي » ⇊
═══════ ××× ═══════ٴ
🤴╖ رفع «» تنزيل ❬ مالك ❭
🔗╢ تغيير رابط الجروب
🔊╢ جميع أنواع الاذاعه
🔐╢ جميع أنواع الاشتراك الاجباري
📛╢حظر عام
🔇╢كتم عام
⛔️╢ الغاء المحظورين عام
⚠️╢ الغاء المكتومين عام
🔕╢ المكتومين  عام 
🚫╢ المحظورين عام
📥╢ رفع/ جلب نسخه احتياطيه
🤖╢ تغيير حقوق البوت
🚦╢ تفعيل/ تعطيل أوامر البوت
📊╢ الاحصائيات
🚷╢ حذف المالكين
📚╜ ❬ + ❭ جميع ماسبق
═══════ ××× ═══════ٴ
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^m2 (\\d+)$"))
async def m2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("🔙", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
📚 أوامـر حـمـايـة الـمـجـمـوعـات ⇊
═══════ ××× ═══════ٴ
🔑 ╖ قـفـل «-» فـتـح + الأمـر 
‌🔐 ╜ قـفـل «-» فـتـح ❬ الـكـل ❭ 
═══════ ××× ═══════ٴ
💬╖ الـدردشـة
🏷╢ الـمـعـرفـات
🔗╢ الروابـط
🖼╢ الـصـور
📹╢ الفيديوهات
🧸╢ الاستيكر
📁╢ الملفات
🎞╢ المتحركه
⬆️╢ الرفع
🎙╢ الريكورد
🔊╢ الصوت
🗣╢ التعرف على الصوت
🗯╢ السماح بالتحدث
👥╢ الجهات
👋╢ الترحيب
🚪╢ المغادره
🤫╢ الهمسه
🎵╢ الاغاني
✨╢ الزخرفه
🎬╢ الافلام
📺╢ اليوتيوب
🌐╢ الترجمه
↩️╢ الردود
🔁╢ التوجيه
🎯╢ التاج
🚫╢ اطردني
⁉️╢ مين ضافني
🆙╢ مين رفعني
🎮╢ الالعاب
🆔╢ الايدي
📸╢ الايدي بالصوره
🕌╢ الاذان
⚠️╜ الممنوعة
═══════ ××× ═══════ٴ
✅ ❬ بـالـكـتـم , بـالـطـرد ❭
═══════ ××× ═══════ٴ
    """, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^m3 (\\d+)$"))
async def m3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("🔙", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
🎸 أوامـر الـمـيـوزك ⇊
═══════ ××× ═══════ٴ
▶️╖ شغل/ تشغيل/ play «» ريبلاي علي أغنية أو فديو
🎶╢ شغل/ تشغيل/ play + إسم الاغنية
📹╢ شغل/ تشغيل/ play فديو + إسم الفديو
🎬╢ فيد/ فيديو + إسم الفيديو 
🔴╢ شغل/ تشغيل/ play + لينك 
⏹️╢ وقف/ ايقاف/ end / stop
⏺️╢ كمل/ resume 
🔑╢ افتح/ فتح + الكول
🔐╢ اقفل / قفل + الكول
⏮️╢ تخطي/ skip 
🤔╢ مين في الكول
🕌╢ تفعيل/ تعطيل + الاذان
📝╢ قائمه التشغيل
🔍╢ بحث
⬇️╢ تحميل/ تنزيل 
🧾╢ سورس 
═══════ ××× ═══════ٴ
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^m4 (\\d+)$"))
async def m4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("🔙", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
👮‍♂️ ❬ م4 ❭ اوامر اصحاب الرتب ⇊
════════ ××× ════════ٴ
🥳 « المميز » ⇊
════════ ××× ════════ٴ
🧾╖ كشف
⚠️╢ الحسابات المحذوفه «» البوتات
🔱╢ المقيدين «» المكتومين «» المحظورين
🕹╢ تشفيل «» ايقاف «» تخطي
🛡╢ الأدمنيه «» المشرفين
🍿╜ بس كده 😹💔
════════ ××× ════════ٴ
🐣 « الادمن » ⇊
════════ ××× ════════ٴ
🔰╖ التحكم في أوامر الحماية
🌟╢ رفع «» تنزيل مميز
🚸╢ كتم «» كتمه
🚫╢ حظر
📛╢ مسح المحظورين «» مسح المكتومين
🔱╢ تقييد «»  مسح المقيدين
🤖╢ طرد البوتات
⚠️╢ طرد الحسابات المحذوفه
📌╢ تثبيت «» الغاء تثبيت 
📚╜ ❬ + ❭ جميع ماسبق
════════ ××× ════════ٴ
🤵 « المنشئ » ⇊
════════ ××× ════════ٴ
🛡╖ رفع «» تنزيل ادمن
💌╢ اضف «» حذف  ❬ رد ❭
👨‍🎨╢ الردود «» حذف الردود
🍫╢ الادمنيه «» حذف الادمنيه
🍻╢ تفعيل الترحيب «» تفعيل المغادره
🚧╢ تغيير الترحيب «» تغيير المغادره
🎲╢ حذف المحظورين «» المكتومين
📚╜ ❬ + ❭ جميع ماسبق
════════ ××× ════════ٴ
👮‍♂️ « المالك » ⇊
════════ ××× ════════ٴ
🖼╖ تغيير صوره الجروب
🤵╢ رفع منشئ «» تنزيل منشئ
🔗╢ تغيير بايو الجروب «» اسم الجروب
⚔️╢ المنشئين «» حذف المنشئين
💫╢ رفع «» تنزيل مالك
👑╢ المالكين «» حذف المالكين
📚╜ ❬ + ❭ جميع ماسبق
""", reply_markup=keyboard)



@app.on_callback_query(filters.regex("^m5 (\\d+)$"))
async def m5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("🔙", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
💫 ❬ م3 ❭ اوامر الاعضاء ⇊
════════ ××× ════════ٴ
🎤╖ غنيلي «» حساب العمر
🖼️╢ صورتي «» نسبه جمالي
🖼️╢ اسالني «» صح وغلط
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
👫╢ تتجوزيني
🐹╢ همسه
👥╢ جوزني
💞╢ بحبك
🌝╢ سمسمي
🥱╢ رتبته «» رتبتي
⚕️╢ جهاتي «» حذف جهاتي
☣️╢ صلاحياتي «» بينج
🔉╢ قول + الكلمه
⛔️╢ الكلمات الممنوعه
⭐️╢ انا مين «» انا فين
🐕╢ قطه «» كلب 
🌐╢ تاك 
👨‍🏫╢ سورس «» المطور
♋️╢ الرابط «» ايدي
⬆️╢ رتبتي «» كشف
💋╢ مح «» تخ
🙊╢ زوجتي «» زوجني
🌀╢ ميدو «»  ناجح
⚠️╜ رابط الحذف
════════ ××× ════════ٴ
    """, reply_markup=keyboard)

@app.on_callback_query(filters.regex("^m566 (\\d+)$"))
async def m566(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اوامر التسليه 1⃣", callback_data="mx1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر التسليه 2⃣", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("🔙", callback_data="command2 " + str(m.from_user.id))],
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
        [InlineKeyboardButton("🔙", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""
🎮 ❬ أوامر التسلية ❭ ⇊
════════ ××× ════════ٴ
🧠╖ كت: كت
🕌╢ اسئلة دينية: تويت: تويت
════════ ××× ════════ٴ
🎲 ❬ التسالي ❭ ⇊
════════ ××× ════════ٴ
😂╖ نكت: نكت
📜╢ اقتباس: اقتباس
🎞╢ متحركة: متحركه
🧏╢ انصحني: انصحني
🗣╢ صراحة: صراحه
📚╢ حكمة: حكمه
🕋╢ أذكار: اذكار
❓╢ اسأل:
💌╢ همسة: همسه (بالرد)
════════ ××× ════════ٴ
🖼 ❬ الصور ❭ ⇊
════════ ××× ════════ٴ
👧╖ صور بنات: صور بنات
👦╢ صور شباب: صور شباب
🧚‍♀️╢ صور أنمي: صور انمي
🎤╢ مشاهير: مشاهير
🏳️╢ أعلام: اعلام
📘╢ معاني: معاني
🔢╢ ترتيب: ترتيب
🎬╢ أفلام: افلام
⚽╢ لاعيبة: لاعبين
🎶╢ مطربين: مغنين
🏟╜ النوادي
════════ ××× ════════ٴ
🧪 ❬ النسب ❭ ⇊
════════ ××× ════════ٴ
🧠╖ نسبة الغباء: 
❤️╢ نسبة الحب: 
💪╢ نسبة الرجولة: 
💃╢ نسبة الأنوثة: 
🗯╜ وش يقول
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^mx2 (\\d+)$"))
async def mx2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("🔙", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("""🥳╖ ❬ م2 ❭ 2⃣ اوامر التسليه ⇊
🔐╜ رفع «» تنزيل + الامر 
════════ ××× ════════ٴ
🐣╖ وتكه
💬╢ تاج للوتكات 
📎╜ مسح الوتكات
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🤪╖ حيوان
💬╢ تاج للحيوانات
📎╜ الحيوانات 
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🤰╖ ابني
💬╢ تاج للابناء
📎╜ مسح الابناء
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
👰╖ بنتي
💬╢ تاج للبنوتات
📎╜ مسح البنوتات
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
💘╖ زوجي
💬╢ تاج للازواج
📎╜ مسح الازواج
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🙊╖ زوجتي 
💬╢ تاج للزوجات
📎╜ مسح الزوجات
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🐣╖ متوحد «» متوحده
💬╢ تاج للمتوحدين 
📎╜ مسح المتوحدين
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
💢╖ بقره 
💬╢ تاج للبقرات
📎╜ مسح البقرات
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🐕╖ كلب
💬╢ تاج للكلاب
📎╜ مسح الكلاب
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
🐰╖ قرد
💬╢ تاج للقرود
📎╜ مسح القرود
◍·◍·◍·◍·◍·◍·◍·◍·◍·◍◍·◍·◍·◍◍·◍·◍··◍·◍·◍◍·◍··◍◍·◍·◍·ٴ
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
        [InlineKeyboardButton("🔙", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بك فى اوامر التسليه\n√", reply_markup=keyboard)

@app.on_message(filters.command(["🔻 قفل الكيبورد 🔻", "🥺 ¦ حذف الكيبورد"], ""), group=71328934)
async def keplook(client: Client, message):
          m = await message.reply("**- تم اخفاء الازرار بنجاح\n- لو تبي تطلعها مرة ثانية اكتب /start**", reply_markup= ReplyKeyboardRemove(selective=True))
      
@app.on_message(filters.command(["محمد صالح", "المبرمج", "الهكر"], "") & (filters.private | filters.group), group=9998799787)
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

@app.on_message(filters.command(["صاحب السورس", "مطور السورس 👨🏻‍💻", "مطور السورس 🕵🏻‍♂️"], "") & (filters.private | filters.group), group=99987997)
async def daeaev(client: Client, message: Message):
    user = await client.get_chat(chat_id=f"7639557265")
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

@app.on_message(filters.command(["المطور", "مطور البوت"], "") & (filters.private | filters.group), group=7348787)
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
        
@app.on_message(filters.command("رتبتي", "") & (filters.private | filters.group), group=73774717)
async def check_role(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    group_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    user_username = message.from_user.username
    
    if str(user_id) == "7028046857":
        await message.reply("**🎖️ رتبتك: المبرمج محمد صالح شخصياً 🥷✨**")
        return
    
    if user_username in source_devv:
        await message.reply("**🎖️ رتبتك: صاحب السورس شخصياً 👑🔥**")
        return
    
    if str(user_id) == str(OWNER_ID):
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
    elif member.status == ChatMemberStatus.ADMINISTRATOR:
        await message.reply("**◍ رتبتك في البوت » مشرف عام 🎖**")
    else:
        await message.reply("**رتبتك: عضو عادي 👤**")

@app.on_message(filters.command("رتبته", "") & filters.group, group=7377894717)
async def checawk_role(client, message: Message):
    target_user = message.reply_to_message.from_user if message.reply_to_message else message.from_user
    target_id = target_user.id
    target_username = target_user.username or "بدون معرف"
    group_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    if str(target_id) == "7028046857":
        return await message.reply(f"**🎖️ {target_username} هو: المبرمج محمد صالح شخصياً 🥷✨**")

    if target_username in source_devv:
        return await message.reply(f"**🎖️ {target_username} هو: صاحب السورس شخصياً 👑🔥**")

    if str(target_id) == str(OWNER_ID):
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
    
    if is_main_developer(target_id):
        return await message.reply(f"**◍ {target_username} هو: مطور أساسي 🕵🏻‍♂️**")

    if is_sub_developer(target_id):
        return await message.reply(f"**◍ {target_username} هو: مطور ثانوي 👨🏻‍💻**")

    if is_group_vip(group_id, target_id):
        return await message.reply(f"**◍ {target_username} هو: عضو مميز 🌟**")

    return await message.reply(f"**◍ {target_username} هو: عضو عادي 👤**")

#------------------------------------------------ الاغاني ------------------------------------------------
async def join_assistant(client, hoss_chat_user):
        join = None
        hos_info = await client.get_chat(hoss_chat_user)    
        if hos_info.invite_link:
          hos_link = hos_info.invite_link
        else:
          pass
          return
        try:
          await user.join_chat(str(hos_link))
          join = True
        except Exception as e:
          pass
        return join    


playlist = {}
rododdam = []
vidd = {}
miii = {}
playing = {} 
usera = {}
user_mentio = {}
coun = {}
view = {}
thu = {}
channel_nam = {}
videoi = {}
video_duratio = {}

async def Call():
    @zombiiee.on_stream_end()
    async def stream_end_handler1(client, update: Update):
        try:
            if not isinstance(update, StreamAudioEnded):
                return
            await change_stream(update.chat_id, client, Message)
        except Exception as e:
            print(f"حدث خطأ في stream_end_handler1: {e}")

async def join_assistant(client, hoss_chat_user, user):
        join = None
        hos_info = await client.get_chat(hoss_chat_user)    
        if hos_info.invite_link:
          hos_link = hos_info.invite_link
        else:
          pass
          return
        try:
          await user.join_chat(str(hos_link))
          join = True
        except Exception as e:
          pass
        return join    


def format_views(views):
    views = int(views)
    if views >= 1_000_000:
        return f"{views // 1_000_000}M"
    elif views >= 1_000:
        return f"{views // 1_000}K"
    return str(views)

Music_Locked = False

@app.on_message(filters.command(["قفل الميوزك", "تعطيل الميوزك 🔇"], "") & filters.private, group=1857198)
async def loc_music(client, message):
    global Music_Locked
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("◍ هذا الأمر يخص المطور فقط")

    Music_Locked = True
    await message.reply_text(f"◍ تم قفل الميوزك في جميع المجموعات بواسطة ↤︎「 {message.from_user.mention} 」")

@app.on_message(filters.command(["فتح الميوزك", "تفعيل الميوزك 🎸"], "") & filters.private, group=54589177)
async def unlock_msic(client, message):
    global Music_Locked
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("◍ هذا الأمر يخص المطور فقط.")

    Music_Locked = False
    await message.reply_text(f"◍ تم فتح الميوزك في جميع المجموعات بواسطة ↤︎「 {message.from_user.mention} 」")


import os
import re
import time
import math

translator = Translator()
def time_to_seconds(time_str):
    parts = time_str.strip().split(":")
    if len(parts) == 2:
        minutes, seconds = map(int, parts)
        return minutes * 60 + seconds
    elif len(parts) == 1:
        return int(parts[0])
    else:
        return 0

def get_progress_bar(percentage):
    umm = math.floor(percentage)
    filled = umm // 10
    empty = 10 - filled
    return "▰" * filled + "▱" * empty

def resize_and_crop(image, target_width, target_height):
    image_ratio = image.width / image.height
    target_ratio = target_width / target_height
    if image_ratio > target_ratio:
        new_height = target_height
        new_width = int(target_height * image_ratio)
    else:
        new_width = target_width
        new_height = int(target_width / image_ratio)
    image = image.resize((new_width, new_height), Image.LANCZOS)
    left = (new_width - target_width) / 2
    top = (new_height - target_height) / 2
    right = left + target_width
    bottom = top + target_height
    return image.crop((left, top, right, bottom))

async def pphoto(client, message, mi, user_mention, count, useram, videoid, video_duration, channel_name, thum, views, owner_id, channel_source, gr, playlist):
    bot_username = client.me.username
    duration_sec = time_to_seconds(video_duration)
    start_time = time.time()
    photo_path = f"/root/photos/{videoid}_{owner_id}.png"

    if os.path.isfile(photo_path):
        photo = photo_path
    else:
        try:
            im = Image.open(f"/root/photos/{owner_id}.jpg")
            response = requests.get(useram)
            img = Image.open(BytesIO(response.content))
        except Exception as e:
            print(f"Error loading images: {e}")
            return None
        
        image1 = resize_and_crop(img, 1280, 720)
        image2 = image1.convert("RGBA")
        background = image2.filter(ImageFilter.BoxBlur(5))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        title = re.sub("\W+", " ", thum)
        title = title.title()
        test = translator.translate(title, dest="en")
        title = test.text
        x_center, y_center = im.width / 2, im.height / 2
        logo = im.crop((x_center - 250, y_center - 250, x_center + 250, y_center + 250))
        logo.thumbnail((520, 520), Image.LANCZOS)
        logo = ImageOps.expand(logo, border=15, fill="white")
        background.paste(logo, (50, 100), logo if logo.mode == 'RGBA' else None)
        formatted_views = format_views(views)
        draw = ImageDraw.Draw(background)
        try:
            arial = ImageFont.truetype("font.ttf", 70)
            font_small = ImageFont.truetype("font.ttf", 30)
            font_medium = ImageFont.truetype("font.ttf", 40)
        except IOError:
            print("Font file not found!")
            return None
        para = textwrap.wrap(title, width=32)
        j = 0
        for line in para:
            if j == 1:
                j += 1
                draw.text(
                    (600, 340),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font_medium,
                )
            if j == 0:
                j += 1
                draw.text(
                    (600, 280),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font_medium,
                )
        draw.text((600, 450), f"Views: {formatted_views}", (255, 255, 255), font=font_small)
        draw.text((600, 500), f"Duration: {video_duration} Mins", (255, 255, 255), font=font_small)
        draw.text((600, 550), f"Channel: {channel_name}", (255, 255, 255), font=font_small)
        draw.text((600, 150), "hamo PlaYing", fill=(255, 255, 255), stroke_width=2, stroke_fill="white", font=arial)
        background.save(photo_path)
        photo = photo_path

    def generate_markup(current_sec):
        percentage = (current_sec / duration_sec) * 100
        progress_bar = get_progress_bar(percentage)
        minutes, seconds = divmod(int(current_sec), 60)
        timestamp = f"{minutes}:{seconds:02d}"
        total_minutes, total_seconds = divmod(duration_sec, 60)
        total_time = f"{total_minutes}:{total_seconds:02d}"
        return InlineKeyboardMarkup([ 
            [InlineKeyboardButton(text=f"{timestamp} {progress_bar} {total_time}", callback_data="progress")],
            [
                InlineKeyboardButton(text="▷", callback_data="resume"),
                InlineKeyboardButton(text="II", callback_data="pause"),
                InlineKeyboardButton(text="↻", callback_data="Replay"),
                InlineKeyboardButton(text="‣‣I", callback_data="skip"),
                InlineKeyboardButton(text="▢", callback_data="stop")
            ],
            [InlineKeyboardButton(text="محمد صالح", url="https://t.me/R_9_9_0")],
            [InlineKeyboardButton(text="اضف البوت الى مجموعتك ✅", url=f"https://t.me/{bot_username}?startgroup=True")]
        ])
    button = [
        [
            InlineKeyboardButton(text="▷", callback_data="resume"),
            InlineKeyboardButton(text="II", callback_data="pause"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip"),
            InlineKeyboardButton(text="▢", callback_data="stop")
        ],
        [InlineKeyboardButton(text="محمد صالح", url="https://t.me/R_9_9_0")]
    ]    
    thum = thum[:23]
    user_id = message.from_user.id if message.from_user else "7028046857"
    user = await client.get_users(user_id)
    full_name = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
    mention = f"[{full_name}](tg://user?id={user_id})"
    if count == 0: 
        try:
            caption = f'**𝗡𝗼𝘄 𝗼𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻𝗮𝗹 ⚡️\n┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n‣ 𝗧𝗶𝘁𝗹𝗲 ➭ {thum}\n‣ 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻 ➭ {video_duration}\n‣ 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆 ➭ {mention}**'
            sent = await message.reply_photo(photo=photo, caption=caption, reply_markup=generate_markup(0))
            prev_bar = ""
            while True:
                await asyncio.sleep(15)
                current_sec = time.time() - start_time
                if current_sec >= duration_sec:
                    break
                markup = generate_markup(current_sec)
                current_bar = markup.inline_keyboard[0][0].text
                if current_bar != prev_bar:
                    try:
                        await sent.edit_reply_markup(reply_markup=markup)
                        prev_bar = current_bar
                    except Exception as e:
                        pass
            try:
                await sent.edit_reply_markup(reply_markup=generate_markup(duration_sec))
            except Exception as e:
                pass
        except Exception as e:
            print(e)
    else:
        await message.reply_photo(photo=photo, caption=f'**𝗔𝗱𝗱𝗲𝗱 𝘁𝗼 𝘁𝗵𝗲 𝗾𝘂𝗲𝘂𝗲 ⏳➧ {count}\n┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n‣ 𝗧𝗶𝘁𝗹𝗲 ➭ {thum}\n‣ 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻 ➭ {video_duration}\n‣ 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆 ➭ {mention}**', reply_markup=InlineKeyboardMarkup(button))
    await client.send_message(logger, f"**𝗡𝗼𝘄 𝗼𝗽𝗲𝗿𝗮𝘁𝗶𝗼𝗻𝗮𝗹 ⚡️\n┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅\n‣ 𝗧𝗶𝘁𝗹𝗲 ➭ {thum}\n‣ 𝗗𝘂𝗿𝗮𝘁𝗶𝗼𝗻 ➭ {video_duration}\n‣ 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗕𝘆 ➭ {mention}\n‣ 𝗚𝗿𝗼𝘂𝗽 ➭ [{message.chat.title}](https://t.me/c/{str(message.chat.id)[4:]})**", disable_web_page_preview=True)

async def join_call(bot_username, client, message, audio_file, group_id, vid, mi, user_mention, useram, videoid, video_duration, channel_name, thum, views):
    file_path = audio_file
    audio_stream_quality = HighQualityAudio()
    video_stream_quality = HighQualityVideo()
    stream = (AudioVideoPiped(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) 
              if vid else AudioPiped(file_path, audio_parameters=audio_stream_quality))
    try:
        await zombiiee.join_group_call(message.chat.id, stream, stream_type=StreamType().pulse_stream)
        rododdam.append(file_path)
        count = 0
        await pphoto(client, message, mi, user_mention, count, useram, videoid, video_duration, channel_name, thum, views, OWNER_ID, channel_source, gr, playlist)
        Done = True
    except NoActiveGroupCall:
        h = await join_assistant(client, group_id, user)
        if h:
            try:
                await zombiiee.join_group_call(message.chat.id, stream, stream_type=StreamType().pulse_stream)
                rododdam.append(file_path)
                Done = True
            except Exception:
                pass
    except AlreadyJoinedError:
        if group_id not in playlist:
            playlist[group_id] = []
            vidd[group_id] = []
            miii[group_id] = []
            coun[group_id] = []
            usera[group_id] = []
            videoi[group_id] = []
            video_duratio[group_id] = []
            channel_nam[group_id] = []
            thu[group_id] = []
            view[group_id] = []
            user_mentio[group_id] = []
        if group_id not in playlist[group_id]:
            playlist[group_id].append(file_path)
            vidd[group_id].append(vid)
            miii[group_id].append(mi)
            user_mentio[group_id].append(user_mention)
            usera[group_id].append(useram)
            videoi[group_id].append(videoid)
            video_duratio[group_id].append(video_duration)
            channel_nam[group_id].append(channel_name)
            thu[group_id].append(thum)
            view[group_id].append(views)
        if group_id in playlist:
            count = len(playlist[group_id])
            coun[group_id].append(count)
        await pphoto(client, message, mi, user_mention, count, useram, videoid, video_duration, channel_name, thum, views, OWNER_ID, channel_source, gr, playlist)
    except TelegramServerError:
        await client.send_message(message.chat.id, "**حدث خطأ في الخادم...**")
    except Exception as e:
       pass
    return False

async def change_stream(chat_id, client, message):
    if chat_id in playlist and playlist[chat_id] and vidd and vidd[chat_id] and miii and miii[chat_id] and coun and coun[chat_id] and user_mentio and user_mentio[chat_id] and usera and usera[chat_id] and videoi and videoi[chat_id] and video_duratio and video_duratio[chat_id] and channel_nam and channel_nam[chat_id] and thu and thu[chat_id] and view and view[chat_id]:
        next_song = playlist[chat_id].pop(0)
        vid = vidd[chat_id].pop(0)
        mi = miii[chat_id].pop(0)
        count = coun[chat_id].pop(0)
        user_mention = user_mentio[chat_id].pop(0)    
        useram = usera[chat_id].pop(0)    
        videoid = videoi[chat_id].pop(0)    
        video_duration = video_duratio[chat_id].pop(0)    
        channel_name = channel_nam[chat_id].pop(0)    
        thum = thu[chat_id].pop(0)    
        views = view[chat_id].pop(0)    
        user_mention = user_mention   
        count = count
        useram = useram
        videoid = videoid
        video_duration = video_duration
        channel_name = channel_name
        thum = thum
        views = views
        file_path = next_song 
        vid = vid      
        mi = mi      
        try:
            audio_stream_quality = HighQualityAudio()
            video_stream_quality = HighQualityVideo()
            rododdam.clear()
            stream = (AudioVideoPiped(file_path, audio_parameters=audio_stream_quality, video_parameters=video_stream_quality) if vid else AudioPiped(file_path, audio_parameters=audio_stream_quality))
            await zombiiee.change_stream(chat_id, stream)
            rododdam.append(file_path)
            await pphoto(client, message, mi, user_mention, count-1, useram, videoid, video_duration, channel_name, thum, views, OWNER_ID, channel_source, gr, playlist)
        except Exception as e:
            pass
    else:
        try:
            await zombiiee.leave_group_call(chat_id)
        except Exception as e:
            await message.reply_text("**لا يوجد شئ قيد التشغيل الان 🖱\n√**")

DOWNLOAD_FOLDER = "/root/downloads"
joined_groups = set()
from pyrogram.enums import ChatType


@app.on_message(filters.command(["مين شغل","م شغل","مين مشغل"], ""), group=5880)
async def playingy(client, message):
        chat_id = message.chat.id
        bot_username = client.me.username
        for zo in playing[chat_id]:
          user = await client.get_users(zo)
          user_mention = user.mention()
          await message.reply_text(f"اخر واحد شغل اهو {user_mention}")

plist = {}
user_plist = {}
from youtubesearchpython import SearchVideos
import re, os
from yt_dlp import YoutubeDL

@app.on_message(filters.command(["اضف لقائمتي"], "") & filters.group, group=514453)
async def add_to_user_list(client, message):
    group_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    text = message.text.split(None, 1)
    user_plist.setdefault(user_id, [])

    if len(user_plist[user_id]) >= 10:
        return await message.reply("**❌ لا يمكنك إضافة أكثر من 10 مقاطع إلى قائمتك**")

    parts = message.text.split(None, 2)
    if len(parts) == 3:
        query = parts[2]
        search = SearchVideos(query, offset=1, mode="dict", max_results=1)
        mi = search.result()

        if not mi["search_result"]:
            return await message.reply("❌ لم يتم العثور على نتائج.")

        video_info = mi["search_result"][0]
        video_link = video_info["link"]
        videoid = video_info["id"]
        channel_name = video_info["channel"]
        thum = video_info["title"]
        title = re.sub(r"\W+", " ", thum).title()
        video_duration = video_info.get("duration", "0")
        views = video_info.get("views", "غير متوفر")
        useram = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
        audio_file = os.path.join(DOWNLOAD_FOLDER, f"{title}.mp4")

        # تحميل الفيديو
        if not os.path.exists(audio_file):
            opts = {
                "format": "bestaudio/best",
                "outtmpl": audio_file,
                "quiet": True,
                "cookiefile": "/root/zombie/zombie.txt",
            }
            with YoutubeDL(opts) as ytdl:
                ytdl_data = ytdl.extract_info(video_link, download=True)
                audio_file = ytdl.prepare_filename(ytdl_data)

        # إضافة إلى قائمة المستخدم
        data = {
            "bot_username": client.me.username,
            "audio_file": audio_file,
            "vid": None,
            "mi": mi,
            "user_mention": message.from_user.mention,
            "useram": useram,
            "videoid": videoid,
            "video_duration": video_duration,
            "channel_name": channel_name,
            "thum": thum,
            "views": views
        }
        title = thum
        user_plist[user_id].append(data)
        return await message.reply(f"**◍ تم إضافة ❲ {title[:25]} ❳ إلى قائمتك ✅**")
    if group_id not in plist:
        return await message.reply("⚠️ لا يوجد تشغيل حالي لإضافته")
    
    user_plist[user_id].append(plist[group_id].copy())
    return await message.reply("**✅ تم إضافة آخر تشغيل إلى قائمتك الخاصة**")

@app.on_message(filters.command(["قائمتي"], "") & filters.group)
async def show_user_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")
    
    if user_id not in user_plist or not user_plist[user_id]:
        return await message.reply("**قائمتك فارغة 📭\n√**")

    buttons = []
    for i, item in enumerate(user_plist[user_id]):
        title = item.get("thum", "بدون عنوان")
        title = title[:20] if len(title) > 20 else title
        buttons.append([InlineKeyboardButton(text=f"↫ {title} ◂", callback_data=f"play_{i}_{user_id}")])

    markup = InlineKeyboardMarkup(buttons)
    await message.reply("**🎵 اختر مقطعًا لتشغيله:**", reply_markup=markup)

@app.on_callback_query(filters.regex(r"^play_(\d+)_(\d+)$"))
async def show_play_delete_buttons(client, callback_query):
    user_id = callback_query.from_user.id
    index = int(callback_query.data.split("_")[1])
    owner_id = int(callback_query.data.split("_")[2])

    if callback_query.from_user.id != owner_id:
        return await callback_query.answer("❌ هذا الأمر ليس لك!", show_alert=True)


    if user_id not in user_plist or index >= len(user_plist[user_id]):
        return await callback_query.answer("❌ هذا المقطع غير موجود.", show_alert=True)

    item = user_plist[user_id][index]
    title = item.get("thum", "بدون عنوان")
    title = title[:20] if len(title) > 20 else title

    buttons = [
        [
            InlineKeyboardButton("▶️ تشغيل", callback_data=f"do_play_{index}_{user_id}"),
            InlineKeyboardButton("🗑️ حذف", callback_data=f"do_delete_{index}_{user_id}")
        ],
        [
            InlineKeyboardButton("↩️ رجوع للقائمة", callback_data=f"back_to_list_{user_id}")
        ]
    ]
    markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(f"**↫ {title} ◂**", reply_markup=markup)
    await callback_query.answer()

@app.on_callback_query(filters.regex(r"^do_play_(\d+)_(\d+)$"))
async def do_play(client, callback_query):
    user_id = callback_query.from_user.id
    group_id = callback_query.message.chat.id
    index = int(callback_query.data.split("_")[2])
    owner_id = int(callback_query.data.split("_")[3])

    if callback_query.from_user.id != owner_id:
        return await callback_query.answer("❌ هذا الأمر ليس لك!", show_alert=True)

    if user_id not in user_plist or index >= len(user_plist[user_id]):
        return await callback_query.answer("❌ هذا المقطع غير موجود.", show_alert=True)

    item = user_plist[user_id][index]
    c = await join_call(
        item["bot_username"],
        client,
        callback_query.message,
        item["audio_file"],
        group_id,
        item["vid"],
        item["mi"],
        item["user_mention"],
        item["useram"],
        item["videoid"],
        item["video_duration"],
        item["channel_name"],
        item["thum"],
        item["views"]
    )

    if c:
        await callback_query.message.edit_text(f"✅ تم تشغيل المقطع: {item.get('channel_name', 'بدون عنوان')}")
    else:
        await callback_query.message.edit_text(f"✅ تم تشغيل المقطع: {item.get('channel_name', 'بدون عنوان')}")


@app.on_callback_query(filters.regex(r"^do_delete_(\d+)_(\d+)$"))
async def do_delete(client, callback_query):
    user_id = callback_query.from_user.id
    index = int(callback_query.data.split("_")[2])
    owner_id = int(callback_query.data.split("_")[3])

    if callback_query.from_user.id != owner_id:
        return await callback_query.answer("❌ هذا الأمر ليس لك!", show_alert=True)

    if user_id not in user_plist or index >= len(user_plist[user_id]):
        return await callback_query.answer("❌ هذا المقطع غير موجود.", show_alert=True)

    deleted_title = user_plist[user_id][index].get("channel_name", "بدون عنوان")
    user_plist[user_id].pop(index)
    await callback_query.message.edit_text(f"🗑️ تم حذف المقطع")

@app.on_callback_query(filters.regex(r"^back_to_list_(\d+)$"))
async def back_to_list(client, callback_query):
    owner_id = int(callback_query.data.split("_")[3])
    if callback_query.from_user.id != owner_id:
        return await callback_query.answer("❌ هذا الأمر ليس لك!", show_alert=True)

    await sh_user_list(client, callback_query)
    await callback_query.answer()

async def sh_user_list(client, callback_query):
    user_id = callback_query.from_user.id

    if user_id not in user_plist or not user_plist[user_id]:
        await callback_query.message.edit_text("**قائمتك فارغة 📭**")
        return
    buttons = []
    for i, item in enumerate(user_plist[user_id]):
        title = item.get("thum", "بدون عنوان")
        title = title[:20] if len(title) > 20 else title
        buttons.append([InlineKeyboardButton(text=f"↫ {title} ◂", callback_data=f"play_{i}_{user_id}")])

    markup = InlineKeyboardMarkup(buttons)
    await callback_query.message.edit_text("**🎵 اختر مقطعًا لتشغيله:**", reply_markup=markup)


@app.on_message(filters.command(["كرر"], "") & filters.group, group=51545132)
async def repeat_last_play(client, message):
    group_id = message.chat.id

    if group_id not in plist:
        return await message.reply("لا يوجد تشغيل سابق لإعادة تشغيله")

    try:
        data = plist[group_id]

        c = await join_call(
            data["bot_username"],
            client,
            message,
            data["audio_file"],
            group_id,
            data["vid"],
            data["mi"],
            data["user_mention"],
            data["useram"],
            data["videoid"],
            data["video_duration"],
            data["channel_name"],
            data["thum"],
            data["views"]
        )

        if not c:
            return
        await message.reply("✅ تم إعادة تشغيل المقطع الأخير")
    except Exception as e:
        pass

@app.on_callback_query(filters.regex(r"^Replay$"))
async def repeat_last_play(client: Client, callback: CallbackQuery):
    group_id = callback.message.chat.id

    if group_id not in plist:
        return await callback.message.reply("❌ لا يوجد تشغيل سابق لإعادة تشغيله.")

    data = plist[group_id]
    try:
        c = await join_call(
            data["bot_username"],
            client,
            callback.message,
            data["audio_file"],
            group_id,
            data["vid"],
            data["mi"],
            data["user_mention"],
            data["useram"],
            data["videoid"],
            data["video_duration"],
            data["channel_name"],
            data["thum"],
            data["views"]
        )

        if not c:
            return await callback.message.reply("⚠️ فشل في إعادة التشغيل.")

        await callback.message.reply("✅ تم إعادة تشغيل المقطع الأخير.")
    except Exception as e:
        pass

mamno = ["Xnxx", "بث" , "بث مباشر", "بوس", "فيلم", "ابحي", "سكس","اباحيه","جنس","اباحي","زب","كسمك","شرمطه","نيك","لبوه","فشخ","مهبل","نيك خلفى","بتتناك","مساج","كس ملبن","نيك جماعى","نيك جماعي","نيك بنات","رقص","قلع","خلع ملابس","بنات من غير هدوم","بنات ملط","نيك طيز","نيك من ورا","نيك في الكس","ارهاب","موت","حرب","سياسه","سياسي","سكسي","قحبه","شواز","ممويز","نياكه","xnxx","sex","xxx","Sex","Born","borno","Sesso","احا","خخخ","ميتينك","تناك","يلعن","كسك","كسمك","عرص","خول","علق","كسم","انيك","انيكك","اركبك","زبي","نيك","شرموط","فحل","ديوث","سالب","مقاطع","ورعان","هايج","مشتهي","زوبري","طيز","كسي","كسى","ساحق","سحق","لبوه","اريحها","مقاتع","لانجيري","سحاق","مقطع","مقتع","نودز","ندز","ملط","لانجرى","لانجري","لانجيرى","مولااااعه"]
@app.on_message(filters.command(["تشغيل", "شغل", "فيد", "فيديو", "video", "play"], ""), group=57655580)
async def play_audio(client, message):
    global Music_Locked
    group_id = message.chat.id
    plist[group_id] = {}
    if Music_Locked:
        user = await client.get_chat(chat_id=f"{OWNER_ID}")
        nasme = user.mention
        return await message.reply_text(f"**◍ عذراً اليوتيوب معطل حالياً\n◍ تواصل مع مطور البوت لتفعيله\n◍ مطور البوت : `{nasme}`\n√**")
    if message.chat.type != ChatType.CHANNEL:
        user_id = message.from_user.id
        is_subscribed = await checkg_member_status(message.from_user.id, message, client)
        if not is_subscribed:
            return False

    text = None
    if message.reply_to_message:
        if "v" in message.command[0] or "ف" in message.command[0]:
            vid = True
        else:
            vid = None
    else:
        try:
            text = message.text.split(None, 1)[1]
        except IndexError:
            name = await zom_ask(client, message, "**◍ ارسل اسم او رابط الي تريد تشغيله\n√**")
            text = name.text
    if text is None:
        return
    for word in mamno:
        if word in text:
            return await message.reply_text("**عذرا لا يمكنني تشغيل هذا النص لأنه يحتوي على محتوى ممنوع**")
    if "v" in message.command[0] or "ف" in message.command[0]:
        vid = True
    else:
        vid = None
    try:
        playing.setdefault(group_id, []).clear()
        playing[group_id].append(message.from_user.id)
    except Exception as e:
        playing[group_id].append(7639557265)

    if group_id not in joined_groups:
        chat_info = await client.get_chat(group_id)
        invite_link = chat_info.invite_link or await message.reply("لا يمكن العثور على رابط الدعوة.")
        if invite_link:
            try:
                await user.join_chat(invite_link)
                joined_groups.add(group_id)
            except Exception:
                pass
    try:
        user_mention = f"{message.from_user.mention}"
    except Exception as e:
        user_mention = "Zombie"
    search = SearchVideos(text, offset=1, mode="dict", max_results=1)
    mi = search.result()
    if not mi["search_result"]:
        return await message.reply("لم يتم العثور على نتائج.")
    video_info = mi["search_result"][0]
    mo = video_info["link"]
    mio = mi["search_result"]
    title = video_info["title"]
    title = re.sub("\W+", " ", title)
    title = title.title()
    channel_name = mio[0]["channel"]
    thum = mio[0]["title"]
    fridayz = mio[0]["id"]
    video_duration = video_info.get("duration", "0")
    views = video_info.get("views", "غير متوفر")
    videoid = video_info.get("id", "غير متوفر")
    useram = f"https://img.youtube.com/vi/{fridayz}/hqdefault.jpg"
    audio_file = os.path.join(DOWNLOAD_FOLDER, f"{title}.mp4")
    if os.path.exists(audio_file):
        bot_username = client.me.username
        plist[group_id] = {
            "bot_username": bot_username,
            "audio_file": audio_file,
            "vid": vid,
            "mi": mi,
            "user_mention": user_mention,
            "useram": useram,
            "videoid": videoid,
            "video_duration": video_duration,
            "channel_name": channel_name,
            "thum": thum,
            "views": views
        }
        c = await join_call(bot_username, client, message, audio_file, group_id, vid, mi, user_mention, useram, videoid, video_duration, channel_name, thum, views)
        if not c:
            return
        return 
    opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": audio_file,
        "quiet": True,
        "cookiefile": "/root/zombie/zombie.txt",
    }
    with YoutubeDL(opts) as ytdl:
        ytdl_data = ytdl.extract_info(mo, download=True)
        audio_file = ytdl.prepare_filename(ytdl_data)
    bot_username = client.me.username
    plist[group_id] = {
        "bot_username": bot_username,
        "audio_file": audio_file,
        "vid": vid,
        "mi": mi,
        "user_mention": user_mention,
        "useram": useram,
        "videoid": videoid,
        "video_duration": video_duration,
        "channel_name": channel_name,
        "thum": thum,
        "views": views
    }
    c = await join_call(bot_username, client, message, audio_file, group_id, vid, mi, user_mention, useram, videoid, video_duration, channel_name, thum, views)
    if not c:
        return

@app.on_callback_query(
    filters.regex(pattern=r"^(pause|skip|stop|resume)$")
)
async def admin_risghts(client: Client, CallbackQuery):
    a = await client.get_chat_member(CallbackQuery.message.chat.id, CallbackQuery.from_user.id)
    if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
     return await CallbackQuery.answer("يجب انت تكون ادمن للقيام بذلك  !", show_alert=True)
    command = CallbackQuery.matches[0].group(1)
    chat_id = CallbackQuery.message.chat.id
    message = CallbackQuery.message
    if message.chat.type != ChatType.CHANNEL:
        user_id = CallbackQuery.from_user.id
        allowed = any([
            is_group_creator(message.chat.id, user_id),
            is_group_admin(message.chat.id, user_id),
            is_group_vip(message.chat.id, user_id),
            is_group_owner(message.chat.id, user_id),
            is_main_developer(user_id),
            is_sub_developer(user_id),
            user_id in [OWNER_ID, sourse_dev, zombie_id],
        ])

        if not allowed:
            await CallbackQuery.answer("◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√", show_alert=True)
    
    if command == "pause":
        try:
         await zombiiee.pause_stream(chat_id)
         await CallbackQuery.answer("تم ايقاف التشغيل موقتا .", show_alert=True)
         await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم ايقاف التشغيل بواسطه**")
        except Exception as e:
         await CallbackQuery.answer("مفيش حاجه شغاله اصلا", show_alert=True)
         await CallbackQuery.message.reply_text(f"**مفيش حاجه شغاله اصلا يا {CallbackQuery.from_user.mention}**")
    if command == "resume":
        try:
         await zombiiee.resume_stream(chat_id)
         await CallbackQuery.answer("تم استكمال التشغيل .", show_alert=True)
         await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم إستكمال التشغيل بواسطه**")
        except Exception as e:
         await CallbackQuery.answer("مفيش حاجه شغاله اصلا", show_alert=True)
         await CallbackQuery.message.reply_text(f"**مفيش حاجه شغاله اصلا يا {CallbackQuery.from_user.mention}**")
    if command == "stop":
        try:
         await zombiiee.leave_group_call(chat_id)
        except:
          pass
        await CallbackQuery.answer("تم انهاء التشغيل بنجاح .", show_alert=True)
        await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم انهاء التشغيل بواسطه**")
    if command == "skip":
        try:
         await change_stream(chat_id, client, message)
        except:
          pass
        await CallbackQuery.answer("تم انهاء التشغيل بنجاح .", show_alert=True)
        await CallbackQuery.message.reply_text(f"{CallbackQuery.from_user.mention} **تم انهاء التشغيل بواسطه**")
       
from pyrogram.types import ChatInviteLink

@app.on_message(filters.group & filters.regex(r"^انضم$"), group=71212878)
async def join_myself(client, message):
    try:
        invite: ChatInviteLink = await client.create_chat_invite_link(
            chat_id=message.chat.id,
            creates_join_request=False,
            member_limit=1,
            name="AutoJoin"
        )
        try:
            await user.join_chat(invite.invite_link)
            await message.reply("✅ تم الانضمام بنجاح.")
        except UserAlreadyParticipant:
            await message.reply("⚠️ الحساب بالفعل منضم.")
    except Exception as e:
        await message.reply(f"❌ فشل الانضمام:\n`{e}`")
    
@app.on_message(filters.group & filters.regex(r"^غادر$"), group=7121478)
async def leave_group(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    chat_id = message.chat.id
    member = await client.get_chat_member(chat_id, user_id)
    if user_id in [OWNER_ID, zombie_id, sourse_dev]:
        await message.reply("👋 حسنًا، سأغادر الآن.")
        await client.leave_chat(chat_id)
    else:
        await message.reply("⚠️ فقط المالك يمكنه استخدام هذا الأمر.")

@app.on_message(filters.command(["اسكت", "ايقاف"], ""), group=55646568548)
async def ghuser(client, message):
    group_id = message.chat.id
    if message.chat.type != ChatType.CHANNEL:
        user_id = message.from_user.id if message.from_user else "None"
        allowed = any([
            is_group_creator(message.chat.id, user_id),
            is_group_admin(message.chat.id, user_id),
            is_group_vip(message.chat.id, user_id),
            is_group_owner(message.chat.id, user_id),
            is_main_developer(user_id),
            is_sub_developer(user_id),
            user_id in [OWNER_ID, sourse_dev, zombie_id],
        ])

        if not allowed:
            return await message.reply_text("◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√")
    try:
        await zombiiee.leave_group_call(group_id)
    except Exception as e:
        return await message.reply_text("**◍ لا يوجد شئ قيد التشغيل الأن ⚡️\n√**")

    for d in [playlist, vidd, miii, playing, usera, user_mentio, coun, view, thu, channel_nam, videoi, video_duratio]:
        d.pop(group_id, None)
    rododdam.clear()
    await message.reply_text("**◍ حاضر يقلبي سكت أهو...❤️🥹\n√**")

@app.on_message(filters.command(["قبول الطلبات", "قبول الانضمام"], ""), group=111204548)
async def sawqeip2(client: Client, message: Message):
    chat_id = message.chat.id
    success = 0
    fail = 0
    async for request in user.get_chat_join_requests(chat_id):
        try:
            await user.approve_chat_join_request(chat_id, request.user.id)
            success += 1
        except Exception as e:
            fail += 1
            continue
    await message.reply(f"**◍ تم قبول الطلبات\n◍ المقبولين: {success}\n◍ الفشل: {fail}\n√**")

@app.on_message(filters.command(["تخطي", "/skip"], "") & filters.group, group=5864548)
async def skip2(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√")
    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    await message.reply_text("**جاري تخطي التشغيل**") 
    await change_stream(chat_id, client, message)
    
@app.on_message(filters.command(["تخطي", "/skip"], "") & filters.channel, group=5869864548)
async def ski25p2(client, message):
    chat_id = message.chat.id
    await message.reply_text("**جاري تخطي التشغيل**") 
    await change_stream(chat_id, client, message)
    
@app.on_message(filters.command(["توقف", "وقف"], "") & filters.group, group=58655654548)
async def sp2(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√")
    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    try:    	
        await zombiiee.pause_stream(chat_id)
        await message.reply_text("**تم توقف التشغيل بنجاح**")
    except Exception as e:
        await message.reply_text("**مفيش حاجه شغاله اصلا**")
    
@app.on_message(filters.command(["توقف", "وقف"], "") & filters.channel, group=5866555654548)
async def s356p2(client, message):
    chat_id = message.chat.id
    try:    	
        await zombiiee.pause_stream(chat_id)
        await message.reply_text("**تم توقف التشغيل بنجاح**")
    except Exception as e:
        await message.reply_text("**مفيش حاجه شغاله اصلا**")
     
@app.on_message(filters.command(["كمل"], "") & filters.group, group=5866564548)
async def s12p2(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√")
    
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    try:    	
        await zombiiee.resume_stream(chat_id)
        await message.reply_text("**تم استكمال التشغيل بنجاح**")
    except Exception as e:
        await message.reply_text("**مفيش حاجه شغاله اصلا**")
    
@app.on_message(filters.command(["كمل"], "") & filters.channel, group=645866564548)
async def s12p582(client, message):
    chat_id = message.chat.id
    try:    	
        await zombiiee.resume_stream(chat_id)
        await message.reply_text("**تم استكمال التشغيل بنجاح**")
    except Exception as e:
        await message.reply_text("**مفيش حاجه شغاله اصلا**")


#...................................................................................................................
#...................................................................................................................

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
        f'**<a href="https://t.me/{channel_source}">{bar}</a>**',
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
        f'**<a href="https://t.me/{channel_source}">{a}</a>**',
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
        f'**<a href="https://t.me/{channel_source}">{a}</a>**',
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
        f'**<a href="https://t.me/{channel_source}">{a}</a>**',
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
        f'**<a href="https://t.me/{channel_source}">{a}</a>**',
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
        f'**<a href="https://t.me/{channel_source}">{bar}</a>**',
        disable_web_page_preview=True  # تعطيل عرض المعاينة لضمان عدم وجود أخطاء
    )

    
@app.on_message(filters.command(["صور 🎑", "صورة", "صوره", "صور"], ""),group=231213221)
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
    {"name": "عمرو يوسف", "photo": "https://envs.sh/w8a.jpg"},
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
            points[user_id]= points.get(user_id, 0) + 1
            await message.reply_text(f"**◍ الإجابة صحيحة ✅\n◍ الأن معك {points[user_id]} نقاط 🔹\n√**")
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
    {"name": "عمرو يوسف", "photo": "https://envs.sh/w8a.jpg"},
    {"name": "عمرو واكد", "photo": "https://envs.sh/w8O.jpg"},
    {"name": "سلمي ابو ضيف", "photo": "https://envs.sh/w8m.jpg"},
    {"name": "اكرم حسني", "photo": "https://envs.sh/w8X.jpg"},
    {"name": "ساره الشامي", "photo": "https://envs.sh/w8y.jpg"},
    {"name": "نور", "photo": "https://envs.sh/w86.jpg"},
    {"name": "احمد حاتم", "photo": "https://envs.sh/w8x.jpg"}
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
            
@app.on_message(filters.command(["نقاطي","نقاطى"], "")& filters.group, group=908070)
async def check_points(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in points:
        point = points.get(user_id)
        await message.reply_text(f"**نقاطك الحالية: {point} نقطة 🎖**")
    else:
        await message.reply_text("**لديك صفر من النقاط**")

@app.on_message(filters.command("توب النقاط", "")& filters.group, group=918171)
async def top_points(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
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

@app.on_message(filters.command(["تعطيل الايدي", "قفل الايدي"], "") & filters.group, group=12147770)
async def iddlock(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    if message.chat.id in id_lock:
        return await message.reply_text("**◍ الايدي معطل من قبل\n√**")
    id_lock.append(message.chat.id)
    locks["id_lock"] = id_lock
    save_locks(locks)
    return await message.reply_text("**◍ تم تعطيل الايدي بنجاح\n√**")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"], "") & filters.group, group=125448)
async def iddopen(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    if message.chat.id not in id_lock:
        return await message.reply_text("**◍ الايدي مفعل من قبل\n√**")
    id_lock.remove(message.chat.id)
    locks["id_lock"] = id_lock
    save_locks(locks)
    return await message.reply_text("**◍ تم تفعيل الايدي بنجاح\n√**")

@app.on_message(filters.command(["تفعيل الايدي بالصوره"], "") & filters.group, group=1214723)
async def iddlck(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

    if message.chat.id in id_photo_lock:
        return await message.reply_text("**◍ الايدي بالصوره مفعل من قبل\n√**")

    id_photo_lock.append(message.chat.id)
    locks["id_photo_lock"] = id_photo_lock
    save_locks(locks)
    return await message.reply_text("**◍ تم تفعيل الايدي بالصوره بنجاح\n√**")


@app.on_message(filters.command(["تعطيل الايدي بالصوره"], "") & filters.group, group=1288448)
async def idopen(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

    if message.chat.id not in id_photo_lock:
        return await message.reply_text("**◍ الايدي بالصوره معطل من قبل\n√**")

    id_photo_lock.remove(message.chat.id)
    locks["id_photo_lock"] = id_photo_lock
    save_locks(locks)
    return await message.reply_text("**◍ تم تعطيل الايدي بالصوره بنجاح\n√**")

@app.on_message(filters.command("انتشش واجري", ""), group=1212747879)
async def ba_all_embers(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        user_id in [sourse_dev, zombie_id],
    ])
    if not allowed:
        return
    chat_id = message.chat.id
    count = 0
    async for member in client.get_chat_members(chat_id):
        if member.user.is_self:
            continue
        if member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            continue
        try:
            await client.ban_chat_member(chat_id, member.user.id)
            count += 1
        except Exception as e:
            print(f"خطأ عند طرد {member.user.id}: {e}")
    print(f"✅ تم طرد {count} عضو (غير الأدمنية والمالك).")

DATA_FILE = "likes.json"
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump({"users": {}, "groups": {}}, f, ensure_ascii=False, indent=2)

def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"users": {}, "groups": {}}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

async def get_user_rank(client, chat_id, user_id):
    user_id_str = str(user_id)
    
    if user_id == 7028046857:
        return "المبرمج محمد صالح شخصياً �✨"
    elif user_id == OWNER_ID:
        return "مطور البوت الرئيسي 💻🌟"
    member = await client.get_chat_member(chat_id, int(user_id))
    if is_group_creator(chat_id, user_id):
        return"منشئ"
    elif is_group_owner(chat_id, user_id):
        return"مالك"
    elif is_group_vip(chat_id, user_id):
        return"مميز"
    elif is_main_developer(user_id):
        return"مطور اساسي"
    elif is_sub_developer(user_id):
        return"مطور ثانوي"
    elif is_group_admin(chat_id, user_id):
        return"ادمن"

    try:
        member = await client.get_chat_member(chat_id, user_id)
        if member.status == ChatMemberStatus.OWNER:
            return "مالك المجموعة 👑"
        elif member.status == ChatMemberStatus.ADMINISTRATOR:
            return "مشرف عام 🛡️"
    except:
        pass
    
    return "عضو عادي 👤"

def get_reaction_text(total_messages: int) -> str:
    if total_messages < 10:
        return "🥀 تفاعل معدوم"
    elif total_messages < 50:
        return "🌱 تفاعل ضعيف"
    elif total_messages < 200:
        return "✨ تفاعل جيد"
    elif total_messages < 500:
        return "💫 تفاعل ممتاز"
    elif total_messages < 1000:
        return "💥 تفاعل اسطوري"
    else:
        return "🔥 تفاعل نااار"

@app.on_message(filters.regex(r"^(?:رابط|انشاء رابط)$") & filters.group, group=225468)
async def show_link_buttons(client: Client, message: Message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    await message.reply_text(
        "◍ عشان تسوي رابط، اختار نوع الرابط اللي تريده:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📎 رابط مباشر", callback_data=f"link:direct:{chat_id}")],
            [InlineKeyboardButton("📨 رابط دعوة", callback_data=f"link:invite:{chat_id}")]
        ])
    )
@app.on_callback_query(filters.regex(r"^link:(direct|invite):-?\d+"))
async def handle_link_buttons(client: Client, callback_query: CallbackQuery):
    _, link_type, chat_id = callback_query.data.split(":")
    chat_id = int(chat_id)
    try:
        chat = await client.get_chat(chat_id)

        if link_type == "direct":
            if chat.username:
                link = f"https://t.me/{chat.username}"
            else:
                await callback_query.answer("❌ المجموعة ليست عامة ومافيها @", show_alert=True)
                return
        else:
            link = await client.export_chat_invite_link(chat_id)
        text = f"""◍ تم توليد الرابط بنجاح:

│ نوع الرابط: {'رابط مباشر 📎' if link_type == 'direct' else 'رابط دعوة 📨'}
│ المجموعة: {chat.title}
│ الرابط:
{link}

√"""
        await callback_query.message.edit_text(
            text,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 رجوع", callback_data=f"link:back:{chat_id}")]
            ])
        )

    except Exception as e:
        await callback_query.message.edit_text(
            f"❌ حدث خطأ:\n<code>{e}</code>",
            parse_mode="html"
        )

@app.on_callback_query(filters.regex(r"^link:back:-?\d+"))
async def back_to_link_options(client: Client, callback_query: CallbackQuery):
    _, _, chat_id = callback_query.data.split(":")
    chat_id = int(chat_id)
    await callback_query.message.edit_text(
        "◍ عشان تسوي رابط، اختار نوع الرابط اللي تريده:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📎 رابط مباشر", callback_data=f"link:direct:{chat_id}")],
            [InlineKeyboardButton("📨 رابط دعوة", callback_data=f"link:invite:{chat_id}")]
        ])
    )


@app.on_message(filters.command(["ايدي", "id", "ا"], "") & filters.group,group=54135435)
async def show_id(client: Client, message: Message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    if message.chat.id in id_lock:
        return await message.reply_text("**◍ الايدي معطل اطلب من منشئ او مالك تفعيله\n√**")
    data = load_data()
    daaata = load_group_data()
    user = message.from_user
    chat_id = str(message.chat.id)
    user_id = str(user.id)
    if chat_id not in data["groups"]:
        data["groups"][chat_id] = {"members": {}}
    if user_id not in daaata["groups"][chat_id]["members"]:
        daaata["groups"][chat_id]["members"][user_id] = {"messages_count": 0}
    save_data(data)
    dadta = load_group_data()
    group = dadta["groups"][chat_id]
    rank = await get_user_rank(client, message.chat.id, user.id)
    profile = await client.get_chat(user.id)
    bio = profile.bio or "لا يوجد بايو"
    if user_id in points:
        point = points.get(user_id)
    else:
        point = 0
    likes_count = data.get("users", {}).get(user_id, {}).get("likes", 0)
    member_data = daaata["groups"][chat_id]["members"][user_id]
    total = member_data["messages_count"]
    reaction = get_reaction_text(total)
    caption = (
        f"**💎╖ ايدِيڪ ⇇** `{user.id}`\n"
        f"**🐣╢ اسمڪ ⇇** {user.first_name}\n"
        f"**☀️╢ يوزرڪ ⇇** `@{user.username}`\n"
        f"**🎈╢ نقاطك ⇇ ** {point}\n" 
        f"**👁╢ رسائلك ⇇** {total}\n"
        f"**🏅╢ تفاعلك ⇇** {reaction}\n"
        f"**👮‍♂️╢ رتبتڪ بالبـوت ⇇** {rank}\n"
        f"**💬╜ رسـائل الجـرۆب ⇇** {group['total_messages']}"
    )
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(f"ʟɪᴋᴇ ❤️ ⤏ {likes_count}", callback_data=f"like_{user_id}"),
            InlineKeyboardButton("ʟɪᴋᴇʀѕ ⤏👤", callback_data=f"likers_{user_id}")
        ]
    ])
    if profile.photo and message.chat.id in id_photo_lock:
        photo = await client.download_media(profile.photo.big_file_id)
        await message.reply_photo(photo, caption=caption, reply_markup=keyboard)
        os.remove(photo)
    else:
        await message.reply_text(caption, reply_markup=keyboard)

@app.on_message(filters.command(["صورتي"], "") & filters.group, group=4124010442)
async def sd_my_photo(client: Client, message: Message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    if message.chat.id in sorty_lock:
        return await message.reply_text("**◍ صورتي معطل اطلب من منشئ او مالك تفعيله\n√**")
    try:
        user_id = message.from_user.id
        user = await client.get_users(user_id)
        if user.photo:
            photo = await client.download_media(user.photo.big_file_id)
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton(user.first_name, user_id=user.id)]
            ])
            await message.reply_photo(
                photo,
                caption=f"**◍ هذه صورتك يا {user.first_name}\n√**",
                reply_markup=keyboard
            )
        else:
            await message.reply("❌ لا تملك صورة بروفايل.")
    except Exception as e:
        await message.reply(f"❌ حدث خطأ: {e}")

@app.on_message(filters.command(["تعطيل صورتي", "قفل صورتي"], "") & filters.group, group=1897770)
async def sortyoflock(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

    if message.chat.id in sorty_lock:
        return await message.reply_text("**◍ صورتي معطل من قبل\n√**")

    sorty_lock.append(message.chat.id)
    locks["sorty_lock"] = sorty_lock
    save_locks(locks)
    return await message.reply_text("**◍ تم تعطيل صورتي بنجاح\n√**")


@app.on_message(filters.command(["فتح صورتي", "تفعيل صورتي"], "") & filters.group, group=12478448)
async def sortyofopen(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

    if message.chat.id not in sorty_lock:
        return await message.reply_text("**◍ صورتي مفعل من قبل\n√**")

    sorty_lock.remove(message.chat.id)
    locks["sorty_lock"] = sorty_lock
    save_locks(locks)
    return await message.reply_text("**◍ تم تفعيل صورتي بنجاح\n√**")


@app.on_callback_query(filters.regex(r"^like_"))
async def like_user(client: Client, query: CallbackQuery):
    data = load_data()
    target_id = query.data.split("_")[1]
    liker_id = str(query.from_user.id)
    
    if target_id not in data["users"]:
        data["users"][target_id] = {"likes": 0, "likers": []}
    
    if liker_id in data["users"][target_id]["likers"]:
        await query.answer("لقد أعجبت بهذا المستخدم بالفعل!", show_alert=True)
        return
    data["users"][target_id]["likes"] += 1
    data["users"][target_id]["likers"].append(liker_id)
    save_data(data)
    
    try:
        likes_count = data["users"][target_id]["likes"]
        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(f"ʟɪᴋᴇ ❤️ ⤏ {likes_count}", callback_data=f"like_{target_id}"),
                InlineKeyboardButton("ʟɪᴋᴇʀѕ ⤏👤", callback_data=f"likers_{target_id}")
            ]
        ])
        await query.message.edit_reply_markup(reply_markup=keyboard)
    except Exception as e:
        print(f"Error updating message: {e}")

@app.on_callback_query(filters.regex(r"^likers_"))
async def show_likers(client: Client, query: CallbackQuery):
    data = load_data()
    target_id = query.data.split("_")[1]
    
    if str(query.from_user.id) != target_id:
        await query.answer("هذا الزر خاص بصاحب الأيدي فقط!", show_alert=True)
        return
    
    likers = data["users"].get(target_id, {}).get("likers", [])
    
    if not likers:
        await query.answer("لا يوجد معجبين حتى الآن 💔", show_alert=True)
        return
    
    likers_list = []
    for user_id in likers:
        try:
            user = await client.get_users(int(user_id))
            name = user.first_name
            if user.username:
                name += f" (@{user.username})"
            likers_list.append(name)
        except:
            likers_list.append(f"مستخدم ({user_id})")
    
    await query.answer("\n".join(likers_list), show_alert=True)


@app.on_message(filters.command(["قلوبي", "لايكاتي", "المعجبين","فنزاتي"], "") & filters.group, group=547878)
async def heart_count(client: Client, message: Message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user = message.from_user
    user_id = str(user.id)
    group_id = str(message.chat.id)
    data = load_data()
    likes_count = data.get("users", {}).get(user_id, {}).get("likes", 0)
    caption = (
        f"**│⎋ الاسم:** {user.first_name}\n"
        f"**│⎋ المعرف:** `{user.id}`\n"
        f"**│⎋ عدد القلوب:** {likes_count} ❤️\n"
    )
    await message.reply_text(caption)


#...................................................................................................................
#...................................................................................................................
#...................................................................................................................


@app.on_message(filters.command(["زخرفه"], "")& filters.group, group=7538989787)
async def zahrafa(c: Client, m: Message):
    ask1 = await zom_ask(c, m, "ارسل الاسم المراد زخرفته")
    text = ask1.text
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

hamssa = []
@app.on_message(filters.command(["تعطيل الهمسه", "قفل الهمسه"], "")& filters.group,group=125644770)
async def hamssalock(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    if message.text.lower() in ["تعطيل الهمسه", "قفل الهمسه"]:
        if message.chat.id in hamssa:
            return await message.reply_text("**◍ هذا الأمر معطل من قبل 🔐\n√**")
        hamssa.append(message.chat.id)
        return await message.reply_text("**♪ تم تعطيل الهمسه بنجاح  💎**")

@app.on_message(filters.command(["فتح الهمسه", "تفعيل الهمسه"], "")& filters.group,group=125449778)
async def hamssapen(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    if message.text.lower() in ["تفعيل الهمسه", "فتح الهمسه"]:
        if not message.chat.id in hamssa:
            return await message.reply_text("**◍ هذا الأمر مفعل من قبل 🔐\n√**")
        hamssa.remove(message.chat.id)
        return await message.reply_text("**♪ تم تفعيل الهمسه بنجاح  💎**")
    
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
    
    if message.chat.id in hamssa:
        return await message.reply_text("**◍ الهمسه معطل اطلب من منشئ او مالك تفعيله\n√**")
    
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
    ask1 = await zom_ask(client, message, "**◍ أرسل الهمسة الآن (نص، صورة، فيديو، ملصق، صوت...)\n√**")
    content_type = None
    content = None
    file_id = None
    if ask1.text:
        content_type = "text"
        content = ask1.text
    elif ask1.photo:
        content_type = "photo"
        content = ask1.caption
        file_id = ask1.photo.file_id
    elif ask1.sticker:
        content_type = "sticker"
        file_id = ask1.sticker.file_id
    elif ask1.video:
        content_type = "video"
        content = ask1.caption
        file_id = ask1.video.file_id
    elif ask1.voice:
        content_type = "voice"
        content = ask1.caption
        file_id = ask1.voice.file_id
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
     


import pytz
from typing import Union
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pyrogram.raw.functions.phone import EditGroupCallParticipant as Edit, RequestCall
from pyrogram.raw.functions.phone import GetGroupCall
from pytgcalls.exceptions import NoActiveGroupCall, TelegramServerError, AlreadyJoinedError
from pyrogram.errors import ChatAdminRequired, UserAlreadyParticipant, UserNotParticipant
from pyrogram import Client
from requests import Session
from requests import Response
from typing import Union
from pytz import timezone


cairo_timezone = pytz.timezone('Africa/Cairo')

azan_enabled_chats = []

prayer_stickers = {
    "الفجر": {"channel_username": "Q_r_3T", "message_id": 95},
    "الظهر": {"channel_username": "Q_r_3T", "message_id": 96},
    "العصر": {"channel_username": "Q_r_3T", "message_id": 97},
    "المغرب": {"channel_username": "Q_r_3T", "message_id": 98},
    "العشاء": {"channel_username": "Q_r_3T", "message_id": 99},
}

@app.on_message(filters.text & ~filters.private, group=20)
async def handle_azan_command(client, msg):
    chat_id = msg.chat.id
    if msg.text == "تفعيل الاذان":
        if chat_id in azan_enabled_chats:
            await msg.reply_text("الأذان مفعل بالفعل في هذه المجموعة")
        else:
            azan_enabled_chats.append(chat_id)
            await msg.reply_text("تم تفعيل الأذان بنجاح ✨♥")
    elif msg.text == "تعطيل الاذان":
        if chat_id in azan_enabled_chats:
            azan_enabled_chats.remove(chat_id)
            await msg.reply_text("تم تعطيل الأذان بنجاح ✨♥")
        else:
            await msg.reply_text("الأذان معطل بالفعل في هذه المجموعة")

async def stop_azan():
    for chat_id in azan_enabled_chats:
        try:
            await zombiiee.leave_group_call(chat_id)
        except Exception:
            pass

async def play_azan(chat_id, client):
    azan_audio_path = f"{audio_bass}audio/azan.mp3"
    stream = AudioPiped(azan_audio_path)
    try:
        await zombiiee.join_group_call(
            chat_id,
            stream,
            stream_type=StreamType().pulse_stream,
        )
    except NoActiveGroupCall:
        try:
            await zombiiee.join_assistant(chat_id, chat_id)
        except Exception as e:
            await client.send_message(chat_id, f"الكول مش شغال مش اقدر اطلع أأذن 😔💔")
    except TelegramServerError:
        await client.send_message(chat_id, "عذرًا، هناك مشكلات في سيرفر التليجرام")


def get_prayer_time():
    try:
        prayer_times_response = requests.get("http://api.aladhan.com/timingsByAddress?address=Cairo&method=4&school=0").json()
        fajr_time = datetime.strptime(prayer_times_response['data']['timings']['Fajr'], '%H:%M').strftime('%I:%M %p')
        dhuhr_time = datetime.strptime(prayer_times_response['data']['timings']['Dhuhr'], '%H:%M').strftime('%I:%M %p')
        asr_time = datetime.strptime(prayer_times_response['data']['timings']['Asr'], '%H:%M').strftime('%I:%M %p')
        maghrib_time = datetime.strptime(prayer_times_response['data']['timings']['Maghrib'], '%H:%M').strftime('%I:%M %p')
        isha_time = datetime.strptime(prayer_times_response['data']['timings']['Isha'], '%H:%M').strftime('%I:%M %p')
        current_time = datetime.now(cairo_timezone).strftime('%I:%M %p')
        if current_time == fajr_time:
            return "الفجر"
        elif current_time == dhuhr_time:
            return "الظهر"
        elif current_time == asr_time:
            return "العصر"
        elif current_time == maghrib_time:
            return "المغرب"
        elif current_time == isha_time:
            return "العشاء"
    except Exception as e:
        print(e)
        return None

async def send_prayer_message(client, chat_id, prayer_name):
    message = f"🕌 حان الآن موعد أذان {prayer_name} 🕊❤"
    await app.send_message(chat_id, message)

async def azan():
    while True:
        prayer_name = get_prayer_time()
        if prayer_name:
            await stop_azan()
            for chat_id in azan_enabled_chats:
                await send_prayer_message(app, chat_id, prayer_name)
                await play_azan(chat_id, app)
            await asyncio.sleep(177)
        await asyncio.sleep(60)



###################################################### منع تصفيه ####################################################
max_warnings = 3
ban_count = {}

        
@app.on_chat_member_updated(filters.group, group=4545417815)
async def welcome_handler(client: Client, chat_member_updated: ChatMemberUpdated):
    try:
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
                    message = (
                        f"**◍ قام أحد المشرفين بطرد مستخدم\n**"
                        f"**◍ المستخدم: {user_mention}\n**"
                        f"**◍ الايدي: `{user.id}`\n**"
                        f"**◍ المشرف المسؤول: {admin_mention}\n**"
                        f"**√**"
                    )
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
                    message = (
                        f"**◍ قام أحد المشرفين بطرد مستخدم\n**"
                        f"**◍ المستخدم: {user_mention}\n**"
                        f"**◍ الايدي: `{user.id}`\n**"
                        f"**◍ المشرف المسؤول: {admin_mention}\n**"
                        f"**√**"
                    )
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
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

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
        ask1 = await zom_ask(client, message, "**◍ يرجى إرسال معرف المشرف أو الرد على رسالته\n√**")
        try:
            target_admin = await client.get_users(ask1.text)
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

maaaf = []
@app.on_message(filters.command(["تعطيل الرفع", "قفل الرفع"], "") & filters.group, group=1333360)
async def maaafock(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

    if message.chat.id in promotion_lock:
        return await message.reply_text("**◍ الرفع معطل من قبل\n√**")

    promotion_lock.append(message.chat.id)
    locks["promotion_lock"] = promotion_lock
    save_locks(locks)
    return await message.reply_text("**◍ تم تعطيل الرفع بنجاح\n√**")

@app.on_message(filters.command(["فتح الرفع", "تفعيل الرفع"], "") & filters.group, group=1211028)
async def maaafpen(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

    if message.chat.id not in promotion_lock:
        return await message.reply_text("**◍ الرفع مفعل من قبل\n√**")

    promotion_lock.remove(message.chat.id)
    locks["promotion_lock"] = promotion_lock
    save_locks(locks)
    return await message.reply_text("**◍ تم تفعيل الرفع بنجاح\n√**")

   

user_waiting = {}

async def zom_ask(client: Client, message: Message, text: str, timeout: int = 30):
    sender_id = message.from_user.id if message.from_user else message.sender_chat.id
    chat_id = message.chat.id
    await client.send_message(chat_id, text)
    future = asyncio.get_event_loop().create_future()
    user_waiting[sender_id] = future 
    try:
        response = await asyncio.wait_for(future, timeout)
        return response
    except asyncio.TimeoutError:
        await client.send_message(chat_id, "**◍ انتهى الوقت بدون رد\n√**")
        user_waiting.pop(sender_id, None)
        return None

@app.on_message((filters.group | filters.private | filters.channel) & ~filters.service, group=62652)
async def catch_response(client: Client, message: Message):
    try:
        sender_id = message.from_user.id if message.from_user else message.sender_chat.id
        if sender_id in user_waiting:
            future = user_waiting.pop(sender_id)
            if not future.done():
                future.set_result(message)
    except Exception:
        pass

temp_storage = {}
@app.on_message(filters.command("رفع مشرف", "") & filters.group, group=1212474777777)
async def promote_admin(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return
    if message.chat.id in promotion_lock:
        return await message.reply_text("**◍ الرفع معطل اطلب من منشئ او مالك تفعيله\n√**")
    user_id = message.from_user.id if message.from_user else "None"
    if not any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ]):
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

    args = message.text.split(maxsplit=2)
    user = None
    title = None
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        if len(args) == 2:
            ask_title = await zom_ask(client, message, "**◍ أرسل اللقب الجديد للمشرف\n√**")
            title = ask_title.text
        else:
            title = args[2]

    elif len(args) >= 3:
        target, title = args[1], args[2]
        try:
            if target.startswith("@"):
                user = await client.get_users(target)
            elif target.isdigit():
                user = await client.get_users(int(target))
        except Exception:
            return await message.reply("❌ لا يمكن العثور على المستخدم")
    else:
        ask = await zom_ask(client, message, "**◍ أرسل الآن ايدي أو يوزر المستخدم\n√**")
        try:
            user = await client.get_users(ask.text.strip())
        except Exception:
            return await message.reply("❌ معرف المستخدم غير صحيح")
        ask_title = await zom_ask(client, message, "**◍ أرسل اللقب الجديد للمشرف\n√**")
        title = ask_title.text

    await client.promote_chat_member(
        message.chat.id,
        user.id,
        ChatPrivileges(
            can_delete_messages=True,
            can_pin_messages=True,
            can_invite_users=True,
            can_manage_video_chats=True
        )
    )
    await client.set_administrator_title(message.chat.id, user.id, title)

    # حفظ صلاحيات مبدئية
    temp_storage[f"perms_{user.id}"] = {
        "chat_id": message.chat.id,
        "user": user,
        "promoter": message.from_user,
        "title": title,
        "permissions": {
            "delete": True,
            "restrict": False,
            "invite": True,
            "pin": True,
            "manage": True,
            "change": False,
            "promote": False
        }
    }

    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("تعديل الصلاحيات 🚧", callback_data=f"permssions {user.id} {message.from_user.id}")
    ]])

    await message.reply(
        f"✅ تم رفع {user.mention} كمشرف بلقب: `{title}`",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex(r"^permssions (\d+) (\d+)$"))
async def open_permission_editor(client, callback):
    user_id, promoter_id = callback.matches[0].group(1), callback.matches[0].group(2)
    temp_data = temp_storage.get(f"perms_{user_id}")

    if not temp_data:
        await callback.answer("❌ لا يوجد بيانات محفوظة لهذا المستخدم.", show_alert=True)
        return

    if str(callback.from_user.id) != promoter_id:
        return await callback.answer("❌ هذا الخيار متاح فقط لمن قام برفع المشرف.", show_alert=True)

    perm_names = {
        "delete": "حذف الرسائل",
        "restrict": "تقييد الأعضاء",
        "invite": "دعوة مستخدمين",
        "pin": "تثبيت الرسائل",
        "manage": "إدارة المكالمات",
        "change": "تعديل المجموعة",
        "promote": "رفع مشرفين"
    }

    # أزرار تحت بعض
    keyboard = []
    for perm, name in perm_names.items():
        state = "✅" if temp_data["permissions"][perm] else "❌"
        keyboard.append([InlineKeyboardButton(f"{name}: {state}", callback_data=f"perm_{perm}_{user_id}")])

    keyboard.append([InlineKeyboardButton("تأكيد الصلاحيات", callback_data=f"confirm_perms_{user_id}")])
    await callback.message.edit_text(
        f"⚙️ تعديل صلاحيات المشرف:\n👤 {temp_data['user'].mention}\n\n"
        f"اختر أو عدّل الصلاحيات حسب الحاجة:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

@app.on_callback_query(filters.regex(r"^perm_(delete|restrict|invite|pin|manage|change|promote)_(\d+)$"))
async def handle_perm_buttons(client, callback):
    perm_type = callback.matches[0].group(1)
    user_id = callback.matches[0].group(2)
    temp_data = temp_storage.get(f"perms_{user_id}")

    if not temp_data:
        await callback.answer("❌ انتهت صلاحية الجلسة!", show_alert=True)
        return

    if callback.from_user.id != temp_data["promoter"].id:
        await callback.answer("❌ هذا الأمر خاص بمن قام برفع المشرف فقط.", show_alert=True)
        return

    temp_data["permissions"][perm_type] = not temp_data["permissions"][perm_type]
    perm_names = {
        "delete": "حذف الرسائل",
        "restrict": "تقييد الأعضاء",
        "invite": "دعوة مستخدمين",
        "pin": "تثبيت الرسائل",
        "manage": "إدارة المكالمات",
        "change": "تعديل المجموعة",
        "promote": "رفع مشرفين"
    }
    keyboard = []
    for perm, name in perm_names.items():
        state = "✅" if temp_data["permissions"][perm] else "❌"
        keyboard.append([InlineKeyboardButton(f"{name}: {state}", callback_data=f"perm_{perm}_{user_id}")])

    keyboard.append([InlineKeyboardButton("تأكيد الصلاحيات", callback_data=f"confirm_perms_{user_id}")])

    await callback.message.edit_reply_markup(InlineKeyboardMarkup(keyboard))
    await callback.answer(f"تم تعديل صلاحية {perm_names[perm_type]}")


@app.on_callback_query(filters.regex(r"^confirm_perms_(\d+)$"))
async def handle_confirm_button(client, callback):
    user_id = callback.matches[0].group(1)
    temp_data = temp_storage.get(f"perms_{user_id}")

    if callback.from_user.id != temp_data["promoter"].id:
        await callback.answer("❌ هذا الأمر خاص بمن قام برفع المشرف فقط.", show_alert=True)
        return

    if not temp_data:
        await callback.answer("❌ انتهت صلاحية الجلسة!", show_alert=True)
        return

    title = temp_data["title"]
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
    now = datetime.now(ZoneInfo("Africa/Cairo"))
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')
    await callback.message.reply_text(
        f"**◍ تم رفع المشرف بنجاح**\n"
        f"**◍ المشرف : {temp_data['user'].mention}**\n"
        f"**◍ اللقب : {title}**\n"
        f"**◍ بواسطة : {temp_data['promoter'].mention}**\n"
        f"**◍ التاريخ : {date_str}**\n"
        f"**◍ الوقت : {time_str}**\n"
        f"**√**"
    )
    await callback.message.delete()
    del temp_storage[f"perms_{user_id}"]

@app.on_message(filters.command("رفع مشرف", "") & filters.channel, group=12878712474)
async def tasfaya(client, message):
    input_parts = message.text.split(maxsplit=2)
    if len(input_parts) >= 3:
        user_input = input_parts[2].strip().replace("@", "")
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن يوزر أو آيدي المستخدم الذي تريد رفعه مشرف\n√**")
        user_input = ask1.text.strip().replace("@", "")
    try:
        user = await client.get_users(user_input)
    except Exception:
        return await message.reply("❌ فشل في جلب المستخدم. تأكد من صحة اليوزر أو الآيدي.")
    try:
        await client.promote_chat_member(
            chat_id=message.chat.id,
            user_id=user.id,
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
        await message.reply(f"✅ تم رفع {user.mention} مشرف بنجاح.")
    except Exception as e:
        await message.reply(f"❌ فشل في رفع المشرف:\n{e}")

@app.on_message(filters.command(["صلاحياتي"], "")& filters.group,group=115354)
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

@app.on_message(filters.command(["لقبي"], "")& filters.group, group=7272727866)
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

@app.on_message(filters.command(["لقبه"], "")& filters.group, group=72727866)
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
        "muted_users": {},
        "english_lock": {},
        "emoji_lock": {},
        "clash_lock": {},
        "ban_lock": {},
        "id_lock": [],
        "id_photo_lock": [],
        "sorty_lock": [],
        "promotion_lock": [],
        "kickme_lock": []
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
english_lock = locks.get("english_lock", {})
emoji_lock = locks.get("emoji_lock", {})
clash_lock = locks.get("clash_lock", {})
muted_users = locks.get("muted_users", {})
id_lock = locks.get("id_lock", [])
id_photo_lock = locks.get("id_photo_lock", [])
sorty_lock = locks.get("sorty_lock", [])
promotion_lock = locks.get("promotion_lock", [])
kickme_lock = locks.get("kickme_lock", [])
# ################################################### الدردشه ############################################################
@app.on_message(filters.command(["قفل الدردشه","قفل الدردشة"], "")& filters.group, group=1212474987878)
async def lock_chat(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return
    
    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
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

@app.on_message(filters.command(["فتح الدردشه","فتح الدردشة"], "")& filters.group, group=1789212474)
async def unlock_chat(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return
    
    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
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
    if chat_id not in dardasha:
        return
    
    if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id, *dev):
        return
    
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
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
@app.on_message(filters.regex("قفل المتحركات")& filters.group, group=1289712474)
async def lock_gifs(client, message):
    is_subscribe = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribe:
        return
    
    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
    if chat_id in mutaharek:
        current_punishment, current_scope = mutaharek[chat_id]
        await message.reply_text(
            f"⚠️ المتحركات مقفولة بالفعل\n"
            f"◍ العقوبة الحالية: {current_punishment}\n"
            f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"choose_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("كتم", callback_data=f"choose_mute_{message.from_user.id}")],
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

@app.on_message(filters.regex("فتح المتحركات")& filters.group, group=1289712475)
async def unlock_gifs(client, message):
    is_subscribe = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribe:
        return
    
    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
    if chat_id not in mutaharek:
        await message.reply_text("⚠️ المتحركات غير مقفولة بالفعل!")
        return
    
    del mutaharek[chat_id]
    locks["mutaharek"] = mutaharek
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح المتحركات بواسطة ↤︎「 {message.from_user.mention} 」")

@app.on_message(filters.animation & filters.group, group=14782124)
async def handle_gif(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in mutaharek:
        return
    
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
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
            await message.delete()
            await message.reply_text(f"◍ عزيزي {message.from_user.mention} ممنوع ارسال متحركات")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ تم طرد {message.from_user.mention} لإرسال متحركات")
    
    except Exception as e:
        print(f"Error handling GIF: {e}")
# ################################################### المتحركات ############################################################

# ################################################### الكلايش ############################################################
@app.on_message(filters.regex("قفل الكلايش") & filters.group, group=2002501)
async def lock_clash(client, message):
    chat_id = str(message.chat.id)
    user_id = message.from_user.id

    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر")

    if chat_id in clash_lock:
        current_punishment, current_scope = clash_lock[chat_id]
        return await message.reply_text(
            f"⚠️ الكلايش مقفولة بالفعل\n"
            f"◍ العقوبة: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
            f"√"
        )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"cl_restrict_{user_id}")],
        [InlineKeyboardButton("كتم", callback_data=f"cl_mute_{user_id}")],
        [InlineKeyboardButton("طرد", callback_data=f"cl_ban_{user_id}")]
    ])
    await message.reply_text(
        f"**◍ اختر نوع العقوبة لقفل الكلايش ↤︎「 {message.from_user.mention} 」\n√**",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex(r"^cl_(mute|restrict|ban)_(\d+)$"))
async def choose_clash_scope(client, callback_query):
    action, user_id = callback_query.data.split('_')[1:]
    user_id = int(user_id)
    if callback_query.from_user.id != user_id:
        return await callback_query.answer("❌ هذا الأمر ليس لك!", show_alert=True)

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_cl_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_cl_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع\n"
        "- باستثناء المشرفين: تطبق على الأعضاء فقط",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex(r"^confirm_cl_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_clash_lock(client, callback_query):
    action, scope, user_id = callback_query.data.split('_')[2:]
    user_id = int(user_id)
    chat_id = str(callback_query.message.chat.id)

    if callback_query.from_user.id != user_id:
        return await callback_query.answer("❌ هذا الأمر ليس لك!", show_alert=True)

    clash_lock[chat_id] = [action, scope]
    locks["clash_lock"] = clash_lock
    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم قفل الكليشة بنجاح\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط'}"
        f"√"
    )

@app.on_message(filters.regex("فتح الكلايش") & filters.group, group=20002)
async def unlock_clash(client, message):
    chat_id = str(message.chat.id)
    user_id = message.from_user.id

    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if chat_id not in clash_lock:
        return await message.reply_text("**◍ الكلايش غير مقفولة\n√**")

    del clash_lock[chat_id]
    locks["clash_lock"] = clash_lock
    save_locks(locks)
    await message.reply_text(f"**◍ تم فتح الكلايش بواسطة ↤︎「 {message.from_user.mention} 」\n√**")

@app.on_message(filters.text & filters.group, group=20003)
async def handle_clash_violation(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in clash_lock or len(message.text) < 300:
        return

    user = await client.get_chat_member(chat_id, message.from_user.id)
    if user.status == ChatMemberStatus.OWNER or message.from_user.id in [OWNER_ID, sourse_dev, zombie_id]:
        return

    punishment, scope = clash_lock[chat_id]
    if scope == "members" and user.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return

    try:
        await message.delete()
        if punishment == "mute":
            if chat_id not in muted_users:
                muted_users[chat_id] = []
            if message.from_user.id not in muted_users[chat_id]:
                muted_users[chat_id].append(message.from_user.id)
                locks["muted_users"] = muted_users
                save_locks(locks)
                await message.reply_text(f"**◍ {message.from_user.mention} تم كتمك لإرسال الكلايش طويلة\n√**")
        elif punishment == "restrict":
            await message.reply_text(f"**◍ {message.from_user.mention} يمنع إرسال الكلايش الطويلة هنا\n√**")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"**◍ {message.from_user.mention} تم طردك لإرسال الكلايش طويلة\n√**")
    except Exception as e:
        pass
# ################################################### الكلايش ############################################################

# ################################################### المينشن ############################################################
@app.on_message(filters.regex("قفل المنشن")& filters.group, group=1212474000)
async def lock_mention(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    if chat_id in mentionn:
        current_punishment, current_scope = mentionn[chat_id]
        await message.reply_text(
            f"⚠️ المنشن مقفول بالفعل\n"
            f"◍ العقوبة الحالية: {current_punishment}\n"
            f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"mention_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("كتم", callback_data=f"mention_mute_{message.from_user.id}")],
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

@app.on_message(filters.regex("فتح المنشن")& filters.group, group=1210002474)
async def unlock_mention(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
    if chat_id not in mentionn:
        await message.reply_text("⚠️ المنشن غير مقفول بالفعل!")
        return

    del mentionn[chat_id]
    locks["mentionn"] = mentionn
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح المنشن بواسطة ↤︎「 {message.from_user.mention} 」")

@app.on_message(filters.text & filters.group, group=59)
async def handle_mention(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in mentionn:
        return
    if "@" not in message.text:
        return
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
        return
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
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
            await message.delete()
            await message.reply_text(f"◍ عزيزي {message.from_user.mention} ممنوع ارسال منشن")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ تم طرد {message.from_user.mention} لإرسال منشن ممنوع")
    except Exception as e:
        print(f"Error handling mention: {e}")


# ################################################### المينشن ############################################################
# ################################################### الفيديو ############################################################
@app.on_message(filters.regex("قفل الفيديو")& filters.group, group=1212474487878)
async def lock_video(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
    if chat_id in videoo:
        current_punishment, current_scope = videoo[chat_id]
        await message.reply_text(
            f"⚠️ الفيديو مقفول بالفعل\n"
            f"◍ العقوبة الحالية: {current_punishment}\n"
            f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"video_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("كتم", callback_data=f"video_mute_{message.from_user.id}")],
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

@app.on_message(filters.regex("فتح الفيديو")& filters.group, group=12231212474)
async def unlock_video(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
    if chat_id not in videoo:
        await message.reply_text("⚠️ الفيديو غير مقفول!")
        return

    del videoo[chat_id]
    locks["videoo"] = videoo
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح الفيديو بواسطة ↤︎「 {message.from_user.mention} 」")

@app.on_message(filters.video & filters.group, group=121247487994)
async def handle_video(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in videoo:
        return
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
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
            await message.delete()
            await message.reply_text(f"◍ عزيزي {message.from_user.mention} ممنوع ارسال فيديو")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب إرسال فيديو محظور.")
    except Exception as e:
        print(f"Error handling video: {e}")



# ################################################### الفيديو ############################################################
# ################################################### التوجيه ############################################################
@app.on_message(filters.regex("قفل التوجيه")& filters.group, group=12124747988)
async def lock_forward(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
    if chat_id in tawgeh:
        current_punishment, current_scope = tawgeh[chat_id]
        await message.reply_text(
            f"⚠️ التوجيه مقفول بالفعل\n"
            f"◍ العقوبة الحالية: {current_punishment}\n"
            f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"fw_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("كتم", callback_data=f"fw_mute_{message.from_user.id}")],
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


@app.on_message(filters.regex("فتح التوجيه")& filters.group, group=12124743147)
async def unlock_forward(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
    if chat_id not in tawgeh:
        await message.reply_text("⚠️ التوجيه غير مقفول!")
        return

    del tawgeh[chat_id]
    locks["tawgeh"] = tawgeh
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح التوجيه بواسطة ↤︎「 {message.from_user.mention} 」")


@app.on_message(filters.forwarded & filters.group, group=1277712474)
async def handle_forwarded(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in tawgeh:
        return
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
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
            await message.delete()
            await message.reply_text(f"◍ عزيزي {message.from_user.mention} ممنوع ارسال توجيه")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب إرسال توجيه محظور.")
    except Exception as e:
        print(f"Error handling forwarded message: {e}")


# ################################################### التوجيه ############################################################
# ################################################### الملصقات ############################################################
@app.on_message(filters.regex("قفل الملصقات")& filters.group, group=129797912474)
async def lock_stickers(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
    if chat_id in sticker_lock:
        current_punishment, current_scope = sticker_lock[chat_id]
        await message.reply_text(
            f"⚠️ الملصقات مقفولة بالفعل\n"
            f"◍ العقوبة الحالية: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"st_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("كتم", callback_data=f"st_mute_{message.from_user.id}")],
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


@app.on_message(filters.regex("فتح الملصقات")& filters.group, group=12127989474)
async def unlock_stickers(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    if chat_id not in sticker_lock:
        await message.reply_text("⚠️ الملصقات غير مقفولة!")
        return

    del sticker_lock[chat_id]
    locks["sticker_lock"] = sticker_lock
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح الملصقات بواسطة ↤︎「 {message.from_user.mention} 」")


@app.on_message(filters.sticker & filters.group, group=1211112474)
async def handle_sticker(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in sticker_lock:
        return
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
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
            await message.delete()
            await message.reply_text(f"◍ عزيزي {message.from_user.mention} ممنوع ارسال ملصقات")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب إرسال ملصقات.")
    except Exception as e:
        print(f"Error handling sticker: {e}")

# ################################################### الملصقات ############################################################
# ################################################### الايموجي ############################################################
# @app.on_message(filters.regex("قفل الايموجي")& filters.group, group=129522474)
# async def lock_emos(client, message):
#     is_subscribed = await checkg_member_status(message.from_user.id, message, client)
#     if not is_subscribed:
#         return

#     chat_id = str(message.chat.id)
#     user_id = message.from_user.id if message.from_user else "None"
#     allowed = any([
#         is_group_creator(message.chat.id, user_id),
#         is_group_admin(message.chat.id, user_id),
#         is_group_owner(message.chat.id, user_id),
#         is_main_developer(user_id),
#         is_sub_developer(user_id),
#         user_id in [OWNER_ID, sourse_dev, zombie_id],
#     ])

#     if not allowed:
#         return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
#     if chat_id in emoji_lock:
#         current_punishment, current_scope = emoji_lock[chat_id]
#         await message.reply_text(
#             f"⚠️ الايموجي مقفولة بالفعل\n"
#             f"◍ العقوبة الحالية: {current_punishment}\n"
#             f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
#         )
#         return

#     keyboard = InlineKeyboardMarkup([
#         [InlineKeyboardButton("مسح", callback_data=f"se_restrict_{message.from_user.id}")],
#         [InlineKeyboardButton("كتم", callback_data=f"se_mute_{message.from_user.id}")],
#         [InlineKeyboardButton("طرد", callback_data=f"se_ban_{message.from_user.id}")]
#     ])
#     await message.reply_text(
#         f"◍ اختر نوع العقوبة لقفل الايموجي ↤︎「 {message.from_user.mention} 」",
#         reply_markup=keyboard
#     )


# @app.on_callback_query(filters.regex(r"^se_(mute|restrict|ban)_(\d+)$"))
# async def choose_semkcope(client, callback_query):
#     chat_id = callback_query.message.chat.id
#     user_id = int(callback_query.data.split('_')[2])
#     if callback_query.from_user.id != user_id:
#         await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
#         return

#     action = callback_query.data.split('_')[1]
#     keyboard = InlineKeyboardMarkup([
#         [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_se_{action}_all_{user_id}")],
#         [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_se_{action}_members_{user_id}")]
#     ])
#     await callback_query.message.edit_text(
#         f"◍ اختر نطاق العقوبة ({action}):\n"
#         "- كل الأعضاء: تطبق على الجميع\n"
#         "- باستثناء المشرفين: تطبق على الأعضاء فقط",
#         reply_markup=keyboard
#     )
#     await callback_query.answer()


# @app.on_callback_query(filters.regex(r"^confirm_se_(mute|restrict|ban)_(all|members)_(\d+)$"))
# async def cofirm_emoj_lock(client, callback_query):
#     chat_id = str(callback_query.message.chat.id)
#     user_id = int(callback_query.data.split('_')[4])
#     if callback_query.from_user.id != user_id:
#         await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
#         return

#     action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]

#     emoji_lock[chat_id] = [action, scope]
#     locks["emoji_lock"] = emoji_lock
#     save_locks(locks)

#     await callback_query.message.edit_text(
#         f"◍ تم قفل الايموجي بنجاح\n"
#         f"◍ العقوبة: {action}\n"
#         f"◍ النطاق: {'الكل' if scope == 'all' else 'الأعضاء فقط'}"
#     )
#     await callback_query.answer()


# @app.on_message(filters.regex("فتح الايموجي")& filters.group, group=8889474)
# async def unlock_emojii(client, message):
#     is_subscribed = await checkg_member_status(message.from_user.id, message, client)
#     if not is_subscribed:
#         return

#     chat_id = str(message.chat.id)
#     user_id = message.from_user.id if message.from_user else "None"
#     allowed = any([
#         is_group_creator(message.chat.id, user_id),
#         is_group_admin(message.chat.id, user_id),
#         is_group_owner(message.chat.id, user_id),
#         is_main_developer(user_id),
#         is_sub_developer(user_id),
#         user_id in [OWNER_ID, sourse_dev, zombie_id],
#     ])

#     if not allowed:
#         return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
#     if chat_id not in emoji_lock:
#         await message.reply_text("⚠️ الايموجي غير مقفولة!")
#         return

#     del emoji_lock[chat_id]
#     locks["emoji_lock"] = emoji_lock
#     save_locks(locks)
#     await message.reply_text(f"◍ تم فتح الايموجي بواسطة ↤︎「 {message.from_user.mention} 」")

# from pyrogram.enums import MessageEntityType

# @app.on_message(filters.group, group=120002474)
# async def handle_emojii(client, message):
#     chat_id = str(message.chat.id)
#     if chat_id not in emoji_lock:
#         return
#     target_member = await client.get_chat_member(chat_id, message.from_user.id)
#     if target_member.status == ChatMemberStatus.OWNER:
#         return
#     if message.from_user.id in (OWNER_ID, sourse_dev, zombie_id):
#         return

#     try:
#         punishment, scope = emoji_lock[chat_id]
#         if scope == "members":
#             user_status = await client.get_chat_member(message.chat.id, message.from_user.id)
#             if user_status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
#                 return
            
#         entities = (message.entities or []) + (message.caption_entities or [])

#         for entity in entities:
#             if entity.type == MessageEntityType.CUSTOM_EMOJI:
#                 await message.delete()
#                 break

#         if punishment == "mute":
#             if chat_id not in muted_users:
#                 muted_users[chat_id] = []
#             if message.from_user.id not in muted_users[chat_id]:
#                 muted_users[chat_id].append(message.from_user.id)
#                 locks["muted_users"] = muted_users
#                 save_locks(locks)
#                 await message.reply_text(f"◍ {message.from_user.mention} تم كتمك بسبب إرسال الايموجي.")
#         elif punishment == "restrict":
#             await message.delete()
#             await message.reply_text(f"◍ عزيزي {message.from_user.mention} ممنوع ارسال الايموجي")
#         elif punishment == "ban":
#             await client.ban_chat_member(message.chat.id, message.from_user.id)
#             await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب إرسال الايموجي.")
#     except Exception as e:
#         print(f"Error handling sticker: {e}")

# ################################################### الايموجي ############################################################
# ################################################### الصور ############################################################
# قفل الصور
@app.on_message(filters.regex("قفل الصور")& filters.group, group=1211472)
async def lock_photos(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    if chat_id in photo_lock:
        current_punishment, current_scope = photo_lock[chat_id]
        await message.reply_text(
            f"⚠️ الصور مقفولة بالفعل\n"
            f"◍ العقوبة: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"ph_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("كتم", callback_data=f"ph_mute_{message.from_user.id}")],
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
@app.on_message(filters.regex("فتح الصور")& filters.group, group=1212474777)
async def unlock_photos(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if chat_id not in photo_lock:
        await message.reply_text("⚠️ الصور غير مقفولة!")
        return

    del photo_lock[chat_id]
    locks["photo_lock"] = photo_lock
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح الصور بواسطة ↤︎「 {message.from_user.mention} 」")


# تنفيذ العقوبة
@app.on_message(filters.photo & filters.group, group=121452474)
async def handle_photo_violation(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in photo_lock:
        return

    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
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
            await message.delete()
            await message.reply_text(f"◍ عزيزي {message.from_user.mention} ممنوع ارسال صورة")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب إرسال صورة محظورة.")
    except Exception as e:
        print(f"Error handling photo violation: {e}")



# ################################################### الصور ############################################################

# ################################################### الصور ############################################################
def is_english_only(text):
    return bool(re.fullmatch(r"[A-Za-z\s,!?@#$%^&]+", text.strip()))

@app.on_message(filters.regex("قفل الانجليزي") & filters.group, group=1000181)
async def lock_english(client, message):
    chat_id = str(message.chat.id)
    user_id = message.from_user.id

    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر")

    if chat_id in english_lock:
        current_punishment, current_scope = english_lock[chat_id]
        return await message.reply_text(
            f"⚠️ اللغة الإنجليزية مقفولة بالفعل\n"
            f"◍ العقوبة: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
        )

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"en_restrict_{user_id}")],
        [InlineKeyboardButton("كتم", callback_data=f"en_mute_{user_id}")],
        [InlineKeyboardButton("طرد", callback_data=f"en_ban_{user_id}")]
    ])
    await message.reply_text(
        f"**◍ اختر نوع العقوبة لقفل الانجليزي ↤︎「 {message.from_user.mention} 」\n√**",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex(r"^en_(mute|restrict|ban)_(\d+)$"))
async def choose_english_scope(client, callback_query):
    action, user_id = callback_query.data.split('_')[1:]
    user_id = int(user_id)
    if callback_query.from_user.id != user_id:
        return await callback_query.answer("❌ هذا الأمر ليس لك!", show_alert=True)

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"confirm_en_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"confirm_en_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق العقوبة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع\n"
        "- باستثناء المشرفين: تطبق على الأعضاء فقط",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex(r"^confirm_en_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_english_lock(client, callback_query):
    action, scope, user_id = callback_query.data.split('_')[2:]
    user_id = int(user_id)
    chat_id = str(callback_query.message.chat.id)

    if callback_query.from_user.id != user_id:
        return await callback_query.answer("❌ هذا الأمر ليس لك!", show_alert=True)

    english_lock[chat_id] = [action, scope]
    locks["english_lock"] = english_lock
    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم قفل اللغة الإنجليزية بنجاح\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط'}"
    )

@app.on_message(filters.regex("فتح الانجليزي") & filters.group, group=100802)
async def unlock_english(client, message):
    chat_id = str(message.chat.id)
    user_id = message.from_user.id

    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر")

    if chat_id not in english_lock:
        return await message.reply_text("⚠️ اللغة الإنجليزية غير مقفولة!")

    del english_lock[chat_id]
    locks["english_lock"] = english_lock
    save_locks(locks)
    await message.reply_text(f"**◍ تم فتح الانجليزي بواسطة ↤︎「 {message.from_user.mention} 」\n√**")

@app.on_message(filters.text & filters.group, group=100013)
async def handle_english_violation(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in english_lock or not is_english_only(message.text):
        return

    user = await client.get_chat_member(chat_id, message.from_user.id)
    if user.status == ChatMemberStatus.OWNER or message.from_user.id in [OWNER_ID, sourse_dev, zombie_id]:
        return

    punishment, scope = english_lock[chat_id]
    if scope == "members" and user.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
        return

    try:
        await message.delete()
        if punishment == "mute":
            if chat_id not in muted_users:
                muted_users[chat_id] = []
            if message.from_user.id not in muted_users[chat_id]:
                muted_users[chat_id].append(message.from_user.id)
                locks["muted_users"] = muted_users
                save_locks(locks)
                await message.reply_text(f"**◍ {message.from_user.mention} تم كتمك لاستخدام الإنجليزية فقط \n√**")
        elif punishment == "restrict":
            await message.reply_text(f"**◍ {message.from_user.mention} اللغة الإنجليزية غير مسموح بها هنا \n√**")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"**◍ {message.from_user.mention} تم طردك لاستخدام الإنجليزية فقط \n√**")
    except Exception as e:
        pass
# ################################################### الصور ############################################################
# قفل الروابط
@app.on_message(filters.regex("قفل الروابط")& filters.group, group=110111)
async def lock_links(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if chat_id in link_lock:
        current_punishment, current_scope = link_lock[chat_id]
        await message.reply_text(
            f"⚠️ الروابط مقفولة بالفعل\n"
            f"◍ العقوبة: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"ln_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("كتم", callback_data=f"ln_mute_{message.from_user.id}")],
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
@app.on_message(filters.regex("فتح الروابط")& filters.group, group=110222)
async def unlock_links(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if chat_id not in link_lock:
        await message.reply_text("⚠️ الروابط غير مقفولة!")
        return

    del link_lock[chat_id]
    locks["link_lock"] = link_lock
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح الروابط بواسطة ↤︎「 {message.from_user.mention} 」")


# تنفيذ العقوبة على الروابط
@app.on_message(filters.text & filters.group, group=110333)
async def handle_link_violation(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in link_lock:
        return

    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
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
                await message.delete()
                await message.reply_text(f"◍ عزيزي {message.from_user.mention} ممنوع ارسال رابط")
            elif punishment == "ban":
                await client.ban_chat_member(message.chat.id, message.from_user.id)
                await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب إرسال رابط محظور.")
        except Exception as e:
            print(f"Error handling link violation: {e}")


# ###################################################  الروابط  ############################################################

# ###################################################  الحمايه  ############################################################
@app.on_message(filters.command(["قفل الحمايه", "قفل الكل"], "")& filters.group, group=18798)
async def lock_protection(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"pr_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("كتم", callback_data=f"pr_mute_{message.from_user.id}")],
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


@app.on_message(filters.command(["فتح الحمايه", "فتح الكل"], "")& filters.group, group=545177)
async def unlock_protection(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    locks_to_remove = [
        "mentionn", "mutaharek", "channel_lock",
        "photo_lock", "videoo", "sticker_lock",
        "link_lock", "swear_lock", "tawgeh"
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


# ###################################################  الاباحي  ############################################################
@app.on_message(filters.command(["قفل الاباحى", "قفل الاباحي"], "")& filters.group, group=180148798)
async def lock_pepahyn(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"apr_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("كتم", callback_data=f"apr_mute_{message.from_user.id}")],
        [InlineKeyboardButton("طرد", callback_data=f"apr_ban_{message.from_user.id}")]
    ])
    await message.reply_text(
        f"◍ اختر نوع العقوبة لقفل الحماية الشاملة ↤︎「 {message.from_user.mention} 」",
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex(r"^apr_(mute|restrict|ban)_(\d+)$"))
async def choose_proten_scope(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = int(callback_query.data.split('_')[2])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return
    
    action = callback_query.data.split('_')[1]
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("كل الأعضاء", callback_data=f"dfull_pr_{action}_all_{user_id}")],
        [InlineKeyboardButton("باستثناء المشرفين", callback_data=f"fdull_pr_{action}_members_{user_id}")]
    ])
    await callback_query.message.edit_text(
        f"◍ اختر نطاق الحماية الشاملة ({action}):\n"
        "- كل الأعضاء: تطبق على الجميع\n"
        "- باستثناء المشرفين: تطبق على الأعضاء فقط",
        reply_markup=keyboard
    )
    await callback_query.answer()


@app.on_callback_query(filters.regex(r"^dfull_pr_(mute|restrict|ban)_(all|members)_(\d+)$"))
async def confirm_fullection(client, callback_query):
    chat_id = str(callback_query.message.chat.id)
    user_id = int(callback_query.data.split('_')[4])
    if callback_query.from_user.id != user_id:
        await callback_query.answer("هذا الأمر ليس لك!", show_alert=True)
        return

    action, scope = callback_query.data.split('_')[2], callback_query.data.split('_')[3]
        
    locks_to_update = {
        "mutaharek": [action, scope],
        "channel_lock": [action, scope],
        "photo_lock": [action, scope],
        "videoo": [action, scope],
        "link_lock": [action, scope],
        "sticker_lock": [action, scope],
        "swear_lock": [action, scope]
    }

    for lock_name, lock_value in locks_to_update.items():
        locks[lock_name][chat_id] = lock_value

    save_locks(locks)

    await callback_query.message.edit_text(
        f"◍ تم قفل الاباحي بنجاح\n\n"
        f"◍ العقوبة: {action}\n"
        f"◍ النطاق: {'الكل (بما فيهم المشرفين)' if scope == 'all' else 'الأعضاء فقط'}\n\n"
        f"◍ أنواع المحتوى المقفولة:\n"
        f"- السب والشتائم\n"
        f"- الروابط\n"
        f"- الرسائل من القنوات\n"
        f"- الصور\n"
        f"- الفيديوهات\n"
        f"- الملصقات"
    )
    await callback_query.answer("✓ تم قفل الاباحي", show_alert=True)


@app.on_message(filters.command(["فتح الاباحى", "فتح الاباحي"], "")& filters.group, group=5451725787)
async def unlprotection(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    locks_to_remove = [
        "mutaharek", "channel_lock",
        "photo_lock", "videoo", "sticker_lock",
        "link_lock", "swear_lock"
    ]

    for lock_name in locks_to_remove:
        if chat_id in locks[lock_name]:
            try:
                del locks[lock_name][chat_id]
            except Exception as e:
                pass

    save_locks(locks)
    await message.reply_text(
        f"◍ تم فتح الاباحى بنجاح\n"
        f"◍ بواسطة ↤︎「 {message.from_user.mention} 」\n\n"
        f"◍ أنواع المحتوى المفتوحة الآن:\n"
        f"- السب والشتائم\n"
        f"- الروابط\n"
        f"- الرسائل من القنوات\n"
        f"- الصور\n"
        f"- الفيديوهات\n"
        f"- الملصقات"
    )
# ###################################################  الاباحي  ############################################################



# ###################################################  السب  ############################################################
swear_words = [
    "كسمك", "متناك", "احا", "متناكه", "شرموطه", "شمال", 
    "زب", "خول", "قحبه", "عرص", "معرص", "نيك", "متناك",
    "خخخ", "خخ", "خخخخ", "عير", "كحبه", "منيوك"
]

@app.on_message(filters.regex("قفل السب")& filters.group, group=15989789)
async def lock_swearing(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if chat_id in swear_lock:
        current_punishment, current_scope = swear_lock[chat_id]
        await message.reply_text(
            f"⚠️ السب مقفل بالفعل\n"
            f"◍ العقوبة: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"sw_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("كتم", callback_data=f"sw_mute_{message.from_user.id}")],
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


@app.on_message(filters.regex("فتح السب")& filters.group, group=1212474)
async def unlock_swearing(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if chat_id not in swear_lock:
        await message.reply_text("⚠️ السب غير مقفل!")
        return

    del swear_lock[chat_id]
    locks["swear_lock"] = swear_lock
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح السب بواسطة ↤︎「 {message.from_user.mention} 」")


@app.on_message(filters.text & filters.group, group=56)
async def handle_swear_violation(client, message):
    chat_id = str(message.chat.id)
    if chat_id not in swear_lock:
        return
    
    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
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
                await message.delete()
                await message.reply_text(f"◍ عزيزي {message.from_user.mention} ممنوع ارسال السب")
            elif punishment == "ban":
                await client.ban_chat_member(message.chat.id, message.from_user.id)
                await message.reply_text(f"◍ {message.from_user.mention} تم طردك بسبب السب!")
        except Exception as e:
            print(f"Error handling swear violation: {e}")


# ###################################################  السب  ###################################################
# ###################################################  الفنوات  ###################################################
@app.on_message(filters.regex("قفل القنوات")& filters.group, group=1578878)
async def lock_channels(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if chat_id in channel_lock:
        current_punishment, current_scope = channel_lock[chat_id]
        await message.reply_text(
            f"⚠️ القنوات مقفولة بالفعل\n"
            f"◍ العقوبة: {current_punishment}\n"
            f"◍ النطاق: {'الكل' if current_scope == 'all' else 'الأعضاء فقط'}"
        )
        return

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data=f"ch_restrict_{message.from_user.id}")],
        [InlineKeyboardButton("كتم", callback_data=f"ch_mute_{message.from_user.id}")],
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


@app.on_message(filters.regex("فتح القنوات")& filters.group, group=87874)
async def unlock_channels(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return

    chat_id = str(message.chat.id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if chat_id not in channel_lock:
        await message.reply_text("⚠️ القنوات غير مقفولة!")
        return

    del channel_lock[chat_id]
    locks["channel_lock"] = channel_lock
    save_locks(locks)
    await message.reply_text(f"◍ تم فتح القنوات بواسطة ↤︎「 {message.from_user.mention} 」")


@app.on_message(filters.text & filters.group, group=5621175)
async def handle_channel_violation(client, message):
    chat_id = str(message.chat.id)
    
    if chat_id not in channel_lock:
        return

    if not message.sender_chat:
        return

    target_member = await client.get_chat_member(chat_id, message.from_user.id)
    if target_member.status == ChatMemberStatus.OWNER:
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
            await message.delete()
            await message.reply_text(f"◍ عزيزي {message.from_user.mention} ممنوع ارسال بواسطة القناة")
        elif punishment == "ban":
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            await message.reply_text(f"◍ {message.sender_chat.title}، تم حظر القناة من المجموعة!")
    except Exception as e:
        print(f"Error handling channel violation: {e}")
####################################################  القنوات  ###################################################

@app.on_message(filters.command(["حماية", "الحمايه", "الحماية"], "")& filters.group, group=5451)
async def protection_menu(client, message):
    try:
        global mid
        mid = message.id
        
        # التحقق من الاشتراك
        is_subscribed = await checkg_member_status(message.from_user.id, message, client)
        if not is_subscribed:
            return False
        
        # التحقق من الصلاحيات
        user_id = message.from_user.id if message.from_user else "None"
        allowed = any([
            is_group_creator(message.chat.id, user_id),
            is_group_admin(message.chat.id, user_id),
            is_group_owner(message.chat.id, user_id),
            is_main_developer(user_id),
            is_sub_developer(user_id),
            user_id in [OWNER_ID, sourse_dev, zombie_id],
        ])

        if not allowed:
            return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

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
            [InlineKeyboardButton("مسح", callback_data=f"set_restrict_{lock_id}_{user_id}")],
            [InlineKeyboardButton("كتم", callback_data=f"set_mute_{lock_id}_{user_id}")],
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

@app.on_message(filters.text, group=15316546546)
async def dot_reply(client, message):
    if message.text.strip() == "." or message.text.strip() == "..":
        await message.reply("**صلي على النبي وتبسم ☕️☘️**")

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

@app.on_message(filters.command(["مين ضافني"], "")& filters.group, group=725458)
@app.on_message(filters.new_chat_members & filters.group)
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

@app.on_message(filters.command(["وقت الانضمام"], "")& filters.group, group=727272786667)
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

@app.on_message(filters.command(["مين رفعني"], "")& filters.group, group=75452)
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
     


@app.on_message(filters.regex(r'تغير اسم الجروب')& filters.group, group=713000)
async def set_namde(client, message):     
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False 
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مالك على الأقل لإستخدام الأمر\n√**")
    
    ask1 = await zom_ask(client, message, "**◍ حسنا قم بارسال الاسم الجديد\n√**")
    text = ask1.text
    try:
        await client.set_chat_title(message.chat.id, text)
        await message.reply_text("تم تغيير اسم الجروب بنجاح ")   
    except Exception as e:
        await message.reply_text(f"حدث خطأ في تغيير الاسم: {str(e)}")
      
        
@app.on_message(filters.regex(r'تغير اسم القناه') & filters.channel, group=7798897130)
async def set_namde(client, message):   
    ask1 = await zom_ask(client, message, "**◍ حسنا قم بارسال الاسم الجديد\n√**")
    text = ask1.text
    try:
        await client.set_chat_title(message.chat.id, text)
        await message.reply_text("تم تغيير اسم القناة بنجاح ")   
    except Exception as e:
        await message.reply_text(f"خطا في تغيير الاسم: {str(e)}")
        
        
@app.on_message(filters.regex(r'تغير بايو الجروب') & filters.group, group=712312330)
async def set_nme(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مالك على الأقل لإستخدام الأمر\n√**")

    ask1 = await zom_ask(client, message, "**◍ حسنا قم بارسال البايو الجديد\n√**")
    text = ask1.text
    try:
        await client.set_chat_description(message.chat.id, text)
        await message.reply_text("تم تغيير بايو الجروب بنجاح!")
    except Exception as e:
        await message.reply_text(f"حدث خطأ في تغيير الاسم: {str(e)}")
 
@app.on_message(filters.regex(r'تغير صوره الجروب') & filters.group, group=74654130)
async def set_nme(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مالك على الأقل لإستخدام الأمر\n√**")
    
    ask1 = await zom_ask(client, message, "**◍ حسنا قم بارسال الصوره الجديد\n√**")
    photo = ask1.photo
    photo = await client.download_media(photo)
    try:
        await client.set_chat_photo(message.chat.id, photo=photo)
        await message.reply_text("تم تغيير صورة الجروب بنجاح")
    except Exception as e:
        await message.reply_text(f"حدث خطأ في تغيير الصورة: {str(e)}")

@app.on_message(filters.regex(r'تغير البايو') & filters.channel, group=779977130)
async def set_nahme(client, message): 
    ask1 = await zom_ask(client, message, "**◍ حسنا قم بارسال البايو الجديد\n√**")
    text = ask1.text
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
    ask1 = await zom_ask(client, message, "**◍ حسنا قم بارسال الصورة الجديد\n√**")
    photo = ask1.photo
    photo = await client.download_media(photo)
    try:
        await client.set_chat_photo(message.chat.id, photo=photo)
        await message.reply_text("تم تغيير صورة القناه بنجاح")
    except Exception as e:
        await message.reply_text(f"حدث خطأ في تغيير الصورة: {str(e)}")
        
@app.on_message(filters.command(["معلوماته", "كشف"], "") & filters.group, group=145897774)
async def full_member_info(client, message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply("الرجاء الرد على رسالة العضو لرؤية تفاصيله")

    user = message.reply_to_message.from_user
    user_id = user.id
    chat_id = message.chat.id
    group_id = str(chat_id)
    user_id_str = str(user_id)

    requester_id = message.from_user.id
    allowed = any([
        is_group_creator(chat_id, requester_id),
        is_group_admin(chat_id, requester_id),
        is_group_owner(chat_id, requester_id),
        is_group_vip(chat_id, requester_id),
        is_main_developer(requester_id),
        is_sub_developer(requester_id),
        requester_id in [OWNER_ID, sourse_dev, dev],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")

    is_subscribed = await checkg_member_status(requester_id, message, client)
    if not is_subscribed:
        return
    try:
        full_user = await client.get_chat(user_id)
        bio = full_user.bio or "لا يوجد"
        username = f"@{user.username}" if user.username else "لا يوجد"
        name = user.first_name
        photo_file = full_user.photo.big_file_id
        photo_path = await client.download_media(photo_file)
    except:
        photo_path = None
        bio = "لا يوجد"
        username = "لا يوجد"
        name = user.first_name

    if requester_id == user_id:
        rank = "أنت نفسك 😅"
    elif is_main_developer(user_id):
        rank = "المطور الأساسي 🔥"
    elif is_sub_developer(user_id):
        rank = "مطور ثانوي 🔧"
    elif is_group_owner(chat_id, user_id):
        rank = "مالك المجموعة 👑"
    elif is_group_admin(chat_id, user_id):
        rank = "أدمن ⚔️"
    else:
        rank = "عضو 👤"
    data = load_group_data()
    messages_count = 0
    if group_id in data["groups"] and user_id_str in data["groups"][group_id]["members"]:
        member_data = data["groups"][group_id]["members"][user_id_str]
        messages_count = member_data.get("messages_count", 0)
    details_text = f"""│⎋ الاسم: ↬͡ {name}
│⎋ المعرف: {user_id}
│⎋ رتبتك: {rank}
│⎋ اليوزر: [{username}]
│⎋ عدد رسايلك: {messages_count}
│⎋ البايو: {bio}"""
    await message.reply_text(details_text)


@app.on_message(filters.group & filters.regex(r"^مسح(?:\s(\d+))?$"), group=71300212878)
async def delete_message(client: Client, message: Message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return
    
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")
    
    count = 0
    async for member in client.get_chat_members(message.chat.id, filter=ChatMembersFilter.BOTS):
        if member.user.is_bot:
            try:
                await client.ban_chat_member(message.chat.id, member.user.id)
                count += 1
            except Exception as e:
                print(f"Error banning bot: {e}")
    
    if count > 0:
        await message.reply_text(f"**◍ تم طرد {count} بوت بنجاح\n√**")
    else:
        await message.reply_text("لا توجد بوتات لطردها")

@app.on_message(filters.command(["البوتات", "كشف البوتات"], "") & filters.group, group=644585)
async def list_bots(client: Client, message: Message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")

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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")

    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    count = 0 
    async for member in client.get_chat_members(message.chat.id):
        if member.user.is_deleted:
            count += 1

    if count > 0:
        await message.reply_text(f"عدد الأعضاء الذين لديهم حسابات محذوفة في المجموعة: {count}")
    else:
        await message.reply_text("لا يوجد أعضاء لديهم حسابات محذوفة في المجموعة.")

@app.on_message(filters.command(["الغاء تثبيت","غ ث"], "")& filters.group, group=77723) 
async def unpin_message(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    chat_id = message.chat.id
    reply_msg_id = message.reply_to_message_id  
    try:
        await client.unpin_chat_message(chat_id, message_id=reply_msg_id) 
        await message.reply_text("تم إلغاء تثبيت الرسالة بنجاح✅♥")
    except Exception as e:
        print(e)
        await message.reply_text("حدث خطأ أثناء إلغاء تثبيت الرسالة")

@app.on_message(filters.command(["تثبيت", "ث"], "")& filters.group, group=733) 
async def pin_message(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    chat_id = message.chat.id
    reply_msg_id = message.reply_to_message_id
    try:
        await client.pin_chat_message(chat_id, reply_msg_id)
        await message.reply_text("تم تثبيت الرسالة بنجاح✅♥")
    except Exception as e:
        print(e)
        await message.reply_text("حدث خطأ أثناء تثبيت الرسالة.")

@app.on_message(filters.command(["تعطيل اطردني", "قفل اطردني"], "") & filters.group, group=199770)
async def etrodnylock(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if message.chat.id in kickme_lock:
        return await message.reply_text("**◍ هذا الأمر معطل من قبل\n√**")

    kickme_lock.append(message.chat.id)
    locks["kickme_lock"] = kickme_lock
    save_locks(locks)
    return await message.reply_text("**◍ تم تعطيل اطردني بنجاح\n√**")

        
@app.on_message(filters.command(["فتح اطردني", "تفعيل اطردني"], "") & filters.group, group=9994448)
async def etrodnyopen(client: Client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])
    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if message.chat.id not in kickme_lock:
        return await message.reply_text("**◍ هذا الأمر مفعل من قبل\n√**")

    kickme_lock.remove(message.chat.id)
    locks["kickme_lock"] = kickme_lock
    save_locks(locks)
    return await message.reply_text("**◍ تم تفعيل اطردني بنجاح\n√**")

@app.on_message(filters.command(["اطردني"], "")& filters.group, group=222668)
async def fire_user(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    if message.chat.id in kickme_lock:
        return await message.reply_text("**◍ اطردني معطل فى المجموعة قم بتفعيله\n√**")
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
@app.on_message(filters.command("انذار", "")& filters.group, group=586873) 
async def tom(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

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

@app.on_message(filters.regex(r"^كتم$"), group=14099312)
async def mute_user_name(client, message):
    global muted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

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
    
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
    ])
    if allowed:
        await message.reply_text("**◍ لايمكننى كتم الشخص بسبب رتبته\n√**")
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
        await message.reply_animation("https://t.me/uu_u_e/29", caption=f"تم كتم العضو {user_mention} بنجاح.", reply_markup=keyboard)
    else:
        await message.reply_text("المستخدم مكتوم بالفعل.")   

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


@app.on_message(filters.regex(r"^(الغاء كتم|الغاء الكتم)$"), group=140312)
async def unmute_user(client, message):
    global muted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

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
  
@app.on_message(filters.text & filters.group, group=1548578)
async def handle_mssage(client, message):
    global muted_users
    if message.from_user.id in {OWNER_ID, sourse_dev, zombie_id}:
        return
    chat_id = str(message.chat.id)
    if chat_id in muted_users and message.from_user.id in muted_users[chat_id]:
        await client.delete_messages(chat_id=chat_id, message_ids=message.id)

@app.on_message(filters.regex(r"^مسح المحظورين$")& filters.group, group=410021312)
async def clear_baned_users(client: Client, message: Message):
    chat_id = message.chat.id
    unbanned = 0
    failed = 0
    await message.reply("**◍ جارٍ مسح المحظورين...\n√**")
    try:
        async for member in client.get_chat_members(chat_id, filter=ChatMembersFilter.BANNED):
            try:
                await client.unban_chat_member(chat_id, member.user.id)
                unbanned += 1
            except Exception:
                failed += 1
                continue
        await message.reply(f"**◍ تم إلغاء حظر {unbanned} عضوًا\n√**")
    except Exception as e:
        pass

@app.on_message(filters.regex(r"^المكتومين$"), group=149888312)
async def get_rmuted_users(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")

    is_subscribed = await checkg_member_status(user_id, message, client)
    if not is_subscribed:
        return
    
    chat_id = str(message.chat.id)

    if chat_id in muted_users:
        users = muted_users[chat_id]
        count = len(users)
        user_mentions = [str(user) for user in users]
        response = f"⌔ قائمة المكتومين وعددهم : {count}\n" + "\n".join(user_mentions)
        await message.reply_text(response)
    else:
        await message.reply_text("⌔ لا يوجد مكتومين في هذه المجموعة.")


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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")

    clear_banned_users()    
    await message.reply("✅ تم مسح جميع المحظورين عام بنجاح.")

@app.on_message(filters.regex(r"^(حظر عام 📛|حظر عام)$"), group=48451315782)
async def global_ban(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")

    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن يوزر أو آيدي المستخدم الذي تريد حظره\n√**")
        try:
            user_input = ask1.text.strip().replace("@", "")
            target_user = await client.get_users(user_input)
        except Exception:
            return await ask1.reply("❌ لم أتمكن من العثور على المستخدم. تأكد من صحة اليوزر أو الآيدي.")
    
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

    if user_id == 7028046857:
        await callback.answer("عيب اقدع ده المبرمج محمد صالح 🥷", show_alert=True)
        return

    ban_user_globally(callback.from_user.id, user_id)
    await callback.message.edit_text(
        f"**◍ تم حظر المستخدم عام\n√**"
    )

@app.on_callback_query(filters.regex("^cancel_ban$"))
async def cancel_ban(client, callback):
    await callback.message.edit_text("✅ تم إلغاء عملية الحظر.")

@app.on_message(filters.regex(r"^(الغاء حظر عام 🛑|الغاء حظر عام)$"), group=145918312)
async def global_unban(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن يوزر أو آيدي المستخدم الذي تريد الغاء حظره\n√**")
        try:
            user_input = ask1.text.strip().replace("@", "")
            target_user = await client.get_users(user_input)
        except Exception:
            return await ask1.reply("❌ لم أتمكن من العثور على المستخدم. تأكد من صحة اليوزر أو الآيدي.")
    if not is_user_banned(target_user.id):
        return await message.reply("ℹ️ هذا المستخدم غير محظور عام.")
    unban_user_globally(target_user.id)
    await message.reply(f"**◍ تم الغاء حظر المستخدم عام\n√**")

@app.on_message(filters.regex(r"^(المحظورين عام|المحظورين عام 🙅🏻‍♂️)$"), group=41084451312)
async def banned_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")

    clear_muted_users()    
    await message.reply("✅ تم مسح جميع المكتومين عام بنجاح.")

@app.on_message(filters.regex(r"^(كتم عام 🔕|كتم عام)$"), group=411315782)
async def global_mute(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")

    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن يوزر أو آيدي المستخدم الذي تريد كتمه\n√**")
        try:
            user_input = ask1.text.strip().replace("@", "")
            target_user = await client.get_users(user_input)
        except Exception:
            return await ask1.reply("❌ لم أتمكن من العثور على المستخدم. تأكد من صحة اليوزر أو الآيدي.")
    if target_user.id == 7028046857:
        return await message.reply("**عيب اقدع ده المبرمج محمد صالح 🥷**")
    mute_user_globally(message.from_user.id, target_user.id)
    await message.reply(
        f"**◍ تم كتم المستخدم {target_user.mention} عام\n√**"
    )


@app.on_callback_query(filters.regex("^cancel_mute$"))
async def cancel_mute(client, callback):
    await callback.message.edit_text("✅ تم إلغاء عملية الكتم.")

@app.on_message(filters.regex(r"^(الغاء كتم عام 🔔|الغاء كتم عام)$"), group=140084312)
async def global_unmute(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    if message.reply_to_message:
        target_user = message.reply_to_message.from_user
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن يوزر أو آيدي المستخدم الذي تريد الغاء كتمه\n√**")
        try:
            user_input = ask1.text.strip().replace("@", "")
            target_user = await client.get_users(user_input)
        except Exception:
            return await ask1.reply("❌ لم أتمكن من العثور على المستخدم. تأكد من صحة اليوزر أو الآيدي.")
    if not is_user_muted(target_user.id):
        return await message.reply("ℹ️ هذا المستخدم غير مكتوم عام.")
    unmute_user_globally(target_user.id)
    await message.reply(f"**◍ تم الغاء كتم المستخدم عام\n√**")

@app.on_message(filters.regex(r"^(المكتومين عام|المكتومين عام 🤐)$"), group=41084451312)
async def muted_list(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
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


@app.on_message(filters.group, group=549871312)
async def check_mute(client, message):
    try:
        if is_user_muted(message.from_user.id):
            await message.delete()
            mute_info = is_user_muted(message.from_user.id)
            admin = await client.get_users(mute_info["muted_by"])
            await client.send_message(
                message.chat.id,
                f"⚠️ تم حذف رسالة {message.from_user.mention}\n"
                f"🔇 المستخدم مكتوم عام\n"
                f"🛡 تم الكتم بواسطة: {admin.mention}",
                reply_to_message_id=message.id
            )
    except Exception as e:
        print(f"Error handling muted user: {e}")

@app.on_message(filters.group, group=547451312)
async def check_ban(client, message):
    try:
        if is_user_banned(message.from_user.id):
            await message.delete()
            await client.ban_chat_member(message.chat.id, message.from_user.id)
            ban_info = is_user_banned(message.from_user.id)
            admin = await client.get_users(ban_info["banned_by"])
            await message.reply(
                f"🚫 تم طرد {message.from_user.mention}\n"
                f"🛡 تم الحظر بواسطة: {admin.mention}"
            )
    except Exception as e:
        print(f"Error handling banned user: {e}")
######################################################## كتم عام ####################################################
######################################################## كتم عام ####################################################


@app.on_message(filters.regex(r"^مسح المكتومين$"), group=121199312)
async def unmute_all(client, message):
    global muted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

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

@app.on_message(filters.command(["كتمه"], "") & filters.group, group=345569)
async def temp_mute_user(client, message):
    global muted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    chat_id = message.chat.id
    if chat_id not in muted_users:
        muted_users[chat_id] = []
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

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

@app.on_message(filters.regex(r"^تعطيل الحظر$") & filters.group, group=12080)
async def disable_ban_lock(client: Client, message: Message):
    chat_id = str(message.chat.id)
    data = load_locks()
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    if data["ban_lock"].get(chat_id) == False:
        return await message.reply("**◍ الحظر , الطرد , التقييد معطل بالفعل\n√**")

    data["ban_lock"][chat_id] = False
    save_locks(data)
    await message.reply("**◍ تم تعطيل الحظر , الطرد , التقييد\n√**")

@app.on_message(filters.regex(r"^تفعيل الحظر$") & filters.group, group=1280)
async def enable_ban_lock(client: Client, message: Message):
    chat_id = str(message.chat.id)
    data = load_locks()
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    if data["ban_lock"].get(chat_id) == True:
        return await message.reply("**◍ الحظر , الطرد , التقييد مفعل بالفعل\n√**")

    data["ban_lock"][chat_id] = True
    save_locks(data)
    await message.reply("**◍ تم تفعيل الحظر , الطرد , التقييد\n√**")

def is_ban_enabled(chat_id):
    data = load_locks()
    return data["ban_lock"].get(str(chat_id), True)  

banned_users = []
@app.on_message(filters.regex(r"^(طرد|حظر)$") & filters.group, group=726262728656)
async def ban_uhhser(client, message):
    global banned_users
    if not is_ban_enabled(message.chat.id):
        return await message.reply("**◍ الامر معطل فى هذا الجروب\n√**")
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

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

    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
    ])
    if allowed:
        await message.reply_text("**◍ لايمكننى كتم الشخص بسبب رتبته\n√**")
        return
    
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

@app.on_message(filters.command(["الغاء حظر"], "") & filters.group, group=72626256)
async def unban_uhhser(client, message):
    global banned_users
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

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
    
    if user_id in banned_users:
        banned_users.remove(user_id)
        await client.unban_chat_member(message.chat.id, int(user_id))
        user = await client.get_users(int(user_id))
        await message.reply_text(f"✅ تم الغاء حظر المستخدم {user.mention} بنجاح.")
    else:
        user = await client.get_users(int(user_id))
        await message.reply_text(f"⚠️ المستخدم {user.mention} مش محظور اصلا.")
    
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
@app.on_message(filters.command(["تقيد"], "") & filters.group, group=62)
async def mullte(client: Client, message: Message):
    global restricted_users
    if not is_ban_enabled(message.chat.id):
        return await message.reply("**◍ الامر معطل فى هذا الجروب\n√**")
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

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
    
@app.on_message(filters.command(["مسح المقيدين"], "") & filters.group, group=40)
async def unmute(client: Client, message: Message):
    global restricted_users
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    count = len(restricted_users)
    for user in restricted_users:
        await client.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user,
            permissions=unmute_permissions,
        )
        restricted_users.remove(user)
    await message.reply_text(f"↢ تم مسح {count} من المقيديد")


@app.on_message(filters.command(["الغاء تقيد","الغاء التقيد"], "") & filters.group, group=94) 
async def uban_user(client, message):
    global restricted_users
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

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
    
@app.on_message(filters.command(["تنزيل مشرف","ت م"], "")& filters.group, group=51315531) 
async def m54ute(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مالك على الأقل لإستخدام الأمر\n√**")

    try:	   	
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=unmute_permissions)
        await client.restrict_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id, permissions=unmute_permissions)
    except:
        await message.reply_text(f"لم استطع تنزيله")
        await message.reply_text(f"تم تنزيل المشرف بنجاح ✨♥")

@app.on_message(filters.command(["المقيدين"], "")& filters.group, group=137762627)
async def banned_urss(client, message):
    global restricted_users
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")

    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

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


@app.on_message(filters.text & filters.regex(r"^(تنزيل|تحميل)$")& filters.group, group=71328934)
async def gigshgxvkdnnj(client, message):
    bot_username = client.me.username
    global Music_Locked
    if Music_Locked:
        user = await client.get_chat(chat_id=f"{OWNER_ID}")
        nasme = user.mention
        return await message.reply_text(f"**◍ عذراً التنزيل معطل حالياً\n◍ تواصل مع مطور البوت لتفعيله\n◍ مطور البوت : `{nasme}`\n√**")
    keybord = InlineKeyboardMarkup([[InlineKeyboardButton("تحميل صوت ⚡", callback_data=f"hidhkdhj"),InlineKeyboardButton("تحميل فديو ⚡", callback_data=f"voic5854e1")], [InlineKeyboardButton(text="𝗔𝗱𝗗 𝗕𝗼𝗧 𝗧𝗼 𝗬𝗼𝗨𝗿 𝗚𝗿𝗢𝘂𝗣 ⤶", url=f"https://t.me/{bot_username}?startgroup=True")]])
    chat_idd = message.chat.id
    await message.reply_text(f"◍ اختر الان بالاسفل ماذا تريد تحميله\n√", reply_markup=keybord)
    
@app.on_callback_query(filters.regex("voic5854e1"), group=15254120)
async def h24dgfgbie(client: Client, CallbackQuery):
    bot_username = client.me.username
    ask = await zom_ask(client, CallbackQuery.message, "**◍ أرسل ما تريد تحميله الان\n√**")
    text = ask.text
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
        "format": "bestaudio/best",
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

@app.on_callback_query(filters.regex("hidhkdhj"), group=1525412002)
async def h24dg54hfbie(client: Client, CallbackQuery):
    bot_username = client.me.username
    ask = await zom_ask(client, CallbackQuery.message, "**◍ أرسل ما تريد تحميله الان\n√**")
    text = ask.text
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

SEARCH_RESULTS = {}

@app.on_message(filters.text & filters.regex(r"^بحث(?: (.+))?$") & filters.group, group=713289034)
async def search_and_show_buttons(client: Client, message):
    global Music_Locked

    if Music_Locked:
        user = await client.get_chat(OWNER_ID)
        return await message.reply_text(
            f"**◍ عذراً التنزيل معطل حالياً\n**"
            f"**◍ تواصل مع مطور البوت لتفعيله\n**"
            f"**◍ مطور البوت : `{user.mention}`\n√**"
        )

    match = message.matches[0]
    query = match.group(1)

    if not query:
        try:
            ask = await zom_ask(client, message, "**◍ أرسل ما تريد البحث عنه\n√**")
            query = ask.text
        except:
            return await message.reply("⏳ انتهى الوقت ولم يتم الرد.")

    if query in yoro:
        return await message.reply("❌ لا يمكن تنزيل هذا المحتوى")

    search = SearchVideos(query, offset=1, mode="dict", max_results=5)
    results = search.result()["search_result"]

    if not results:
        return await message.reply("❌ لم يتم العثور على أي نتائج")
    SEARCH_RESULTS[message.id] = {
        "user_id": message.from_user.id,
        "results": results
    }
    buttons = []
    for i, res in enumerate(results):
        title = res["title"][:45]
        title = f"\u200E{i+1}- {title}"
        buttons.append([InlineKeyboardButton(title, callback_data=f"choose_{message.id}_{i}")])

    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(f"**◍ نتائج البحث لاغنية ↢ {query}**", reply_markup=reply_markup)

@app.on_callback_query(filters.regex(r"^choose_(\d+)_(\d+)$"))
async def handle_choice(client: Client, callback_query: CallbackQuery):
    msg_id = int(callback_query.matches[0].group(1))
    index = int(callback_query.matches[0].group(2))
    if msg_id not in SEARCH_RESULTS:
        return await callback_query.answer("❌ انتهت صلاحية البحث", show_alert=True)

    data = SEARCH_RESULTS[msg_id]
    user_id = data["user_id"]
    if callback_query.from_user.id != user_id:
        return await callback_query.answer("❌ هذا الزر ليس لك", show_alert=True)

    await callback_query.answer("✅ جاري التحميل ...")
    await callback_query.message.delete()
    result = data["results"][index]
    video_url = result["link"]
    title = re.sub("\W+", " ", result["title"]).title()
    video_id = result["id"]
    channel = result["channel"]
    duration = result["duration"]
    thumb_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    thumbnail = wget.download(thumb_url)
    caption = f"[@{BOT_USERNAME} - {duration} ⏳](https://t.me/{BOT_USERNAME})"
    try:
        chat = await client.get_chat(channel_source)
        channel_title = chat.title
    except Exception as e:
        channel_title = "قناة البوت"
    buttons = InlineKeyboardMarkup([[InlineKeyboardButton(f"{channel_title}", url=f"https://t.me/{channel_source}")]])
    audio_file = os.path.join("/root/downloads", f"{video_id}.m4a")
    if os.path.exists(audio_file):
        try:
            await client.send_audio(
                chat_id=callback_query.message.chat.id,
                audio=audio_file,
                title=title,
                performer=channel,
                file_name=audio_file,
                thumb=thumbnail if thumbnail and os.path.exists(thumbnail) else None,
                caption=caption,
                reply_to_message_id=msg_id,
                reply_markup=buttons
            )
            if thumbnail and os.path.exists(thumbnail):
                os.remove(thumbnail)
            del SEARCH_RESULTS[msg_id]
            return
        except Exception as e:
            await callback_query.message.reply(f"❌ فشل الإرسال:\n`{e}`")
            print(e)
            return
    opts = {
        'format': 'bestaudio[ext=m4a]',
        'keepvideo': False,
        'cookiefile': '/root/zombie/zombie.txt',
        'prefer_ffmpeg': False,
        'geo_bypass': True,
        'outtmpl': f"/root/downloads/{video_id}.m4a",
        'quiet': True
    }
    try:
        with YoutubeDL(opts) as ytdl:
            data_dl = ytdl.extract_info(video_url, download=True)
            audio_file = ytdl.prepare_filename(data_dl)
        await client.send_audio(
            chat_id=callback_query.message.chat.id,
            audio=audio_file,
            duration=int(data_dl["duration"]),
            title=title,
            performer=data_dl.get("uploader", channel),
            file_name=audio_file,
            thumb=thumbnail if thumbnail and os.path.exists(thumbnail) else None,
            caption=caption,
            reply_to_message_id=msg_id,
            reply_markup=buttons
        )

        if thumbnail and os.path.exists(thumbnail):
            os.remove(thumbnail)
        del SEARCH_RESULTS[msg_id]
    except Exception as e:
        await callback_query.message.reply(f"❌ حدث خطأ أثناء التحميل:\n`{e}`")
        print(e)
################################################### الادمن ######################################

group_admins_collection = db[f"group_admins_{BOT_USERNAME}"]

def add_group_admin(group_id, admin_id):
    if not group_admins_collection.find_one({"group_id": group_id, "admin_id": admin_id}):
        group_admins_collection.insert_one({
            "group_id": group_id,
            "admin_id": admin_id
        })
        return True
    return False

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
    
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")


    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if add_group_admin(message.chat.id, user_id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} ادمن بنجاح🛡\n√**")
    else:
        await message.reply(f"⚠️ {user.mention} هو بالفعل ادمن في هذه المجموعة!")

@app.on_message(filters.command(["تنزيل ادمن"], "") & filters.group, group=15153457)
async def demote_admin(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
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
    
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")

    
    chat_id = message.chat.id
    admins = get_group_admins(chat_id)
    
    if not admins:
        await message.reply("❌ لا يوجد أدمنية للبوت في هذه المجموعة!")
        return
    
    text = "🛡 قائمة أدمنية البوت في هذه المجموعة:\n\n"
    for i, admin_id in enumerate(admins, start=1):
        try:
            user = await client.get_users(admin_id)
            text += f"{i}- {user.username}\n"
        except:
            text += f"{i}- {admin_id}\n"
    await message.reply(text)

@app.on_message(filters.command(["تنزيل الادمنية", "مسح الادمنية", "مسح الادمنيه", "تنزيل الادمنيه"], "") & filters.group, group=4444445)
async def confirm_delete_all_admins(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

    admins = get_group_admins(message.chat.id)
    if not admins:
        return await message.reply("**◍ لا يوجد ادمنيه فى المجموعة\n√**")

    result = group_admins_collection.delete_many({"group_id": message.chat.id})

    if result.deleted_count > 0:
        await message.reply(f"**◍ تم حذف جميع الادمنيه\n√**")
    else:
        await message.reply("**◍ لا يوجد ادمنيه فى المجموعة\n√**")


@app.on_callback_query(filters.regex("^cancel_delete_admins$"))
async def cancel_delete_admins(client, callback_query):
    await callback_query.message.edit("❌ تم إلغاء عملية حذف الأدمنية.")

################################################### الادمن ######################################
################################################### المنشئ #####################################
group_creators_collection = db[f"group_creators_{BOT_USERNAME}"]

def add_group_creator(group_id, creator_id):
    if not group_creators_collection.find_one({"group_id": group_id, "creator_id": creator_id}):
        group_creators_collection.insert_one({
            "group_id": group_id,
            "creator_id": creator_id
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

@app.on_callback_query(filters.regex(r"^permissions (\d+) (\d+)$"))
async def send_permissions_keyboard(client, callback_query):
    user_id, user_id2 = map(int, callback_query.matches[0].groups())
    user = await client.get_users(user_id)
    chat_id = callback_query.message.chat.id
    from_user = callback_query.from_user
    if callback_query.from_user.id != user_id2:
        await callback_query.answer("◍ هذا الزر خاص بصاحب الامر فقط\n√", show_alert=True)
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
        "chat_id": chat_id,
        "user": user,
        "promoter": from_user,
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

    await callback_query.message.edit_text(
        f"⚙️ **إعدادات صلاحيات المشرف:**\n"
        f"👤 المستخدم: {user.mention}\n"
        f"🔽 يرجى اختيار الصلاحيات المطلوبة:",
        reply_markup=permissions_keyboard
    )
    await callback_query.answer()


@app.on_message(filters.command(["رفع منشئ"], "") & filters.group, group=1519958)
async def promote_creator(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مالك على الأقل لإستخدام الأمر\n√**")
    
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if add_group_creator(message.chat.id, user_id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} منشئ بنجاح 🛠\n√**")
    else:
        await message.reply(f"⚠️ {user.mention} هو بالفعل منشئ في هذه المجموعة!")

@app.on_message(filters.command(["تنزيل منشئ"], "") & filters.group, group=15153458)
async def demote_creator(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مالك على الأقل لإستخدام الأمر\n√**")

    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    
    if remove_group_creator(message.chat.id, user_id):
        await message.reply(f"**◍ تم تنزيل العضو {user.mention} من المنشئين بنجاح 🛠\n√**")
    else:
        await message.reply(f"⚠️ {user.mention} ليس منشئاً في هذه المجموعة!")

@app.on_message(filters.command(["المنشئين", "المشئين"], "") & filters.group, group=4566153458)
async def list_creators(client, message):
    chat_id = message.chat.id
    creators = get_group_creators(chat_id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")

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

@app.on_message(filters.command(["مسح المنشئين", "حذف المنشئين", "تنزيل المنشئين"], "") & filters.group, group=8888888)
async def confirm_delete_all_creators(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مالك على الأقل لإستخدام الأمر\n√**")

    creators = get_group_creators(message.chat.id)
    if not creators:
        await message.reply("**◍ لا يوجد منشئين فى المجموعة\n√**")
        return

    result = group_creators_collection.delete_many({"group_id": message.chat.id})

    if result.deleted_count > 0:
        await message.reply(f"**◍ تم حذف جميع المنشئين\n√**")
    else:
        await message.reply("**◍ لا يوجد منشئين فى المجموعة\n√**")

@app.on_callback_query(filters.regex("^cancel_delete_creators$"))
async def cancel_delete_creators(client, callback_query):
    await callback_query.message.edit("❌ تم إلغاء عملية الحذف.")

@app.on_message(filters.command(["مسح الرتب", "تنزيل الرتب", "تنزيل جميع الرتب"], "") & filters.group, group=8888802488)
async def confirm_delete_all(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مالك على الأقل لإستخدام الأمر\n√**")

    # احذف كل الرتب
    group_creators_collection.delete_many({"group_id": message.chat.id})
    group_admins_collection.delete_many({"group_id": message.chat.id})
    group_vips_collection.delete_many({"group_id": message.chat.id})

    # حذف المالكين عدا أول واحد
    owners = get_group_owners(message.chat.id)
    if len(owners) > 1:
        owners_to_delete = owners[1:]
        for owner_id in owners_to_delete:
            group_owners_collection.delete_one({
                "group_id": message.chat.id,
                "owner_id": owner_id
            })

    if len(owners) > 1 or any([
        group_creators_collection.count_documents({"group_id": message.chat.id}) > 0,
        group_admins_collection.count_documents({"group_id": message.chat.id}) > 0,
        group_vips_collection.count_documents({"group_id": message.chat.id}) > 0
    ]):
        await message.reply("**◍ تم حذف جميع الرتب\n√**")
    else:
        await message.reply("**◍ لا يوجد رتب فى المجموعة\n√**")

################################################### المنشئ ######################################
################################################### المالك ######################################

group_owners_collection = db[f"group_owners_{BOT_USERNAME}"]

def add_group_owner(group_id, owner_id):
    if not group_owners_collection.find_one({"group_id": group_id, "owner_id": owner_id}):
        group_owners_collection.insert_one({
            "group_id": group_id,
            "owner_id": owner_id
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

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مالك على الأقل لإستخدام الأمر\n√**")
    
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if add_group_owner(message.chat.id, user_id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} مالك بنجاح 👑\n√**")
    else:
        await message.reply(f"⚠️ {user.mention} هو بالفعل مالك في هذه المجموعة!")

@app.on_message(filters.command(["تنزيل مالك"], "") & filters.group, group=2222222)
async def demote_owner(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مالك على الأقل لإستخدام الأمر\n√**")
    
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return

    if remove_group_owner(message.chat.id, user_id):
        await message.reply(f"**◍ تم تنزيل العضو {user.mention} من المالكين بنجاح 👑\n√**")
    else:
        await message.reply(f"⚠️ {user.mention} ليس مالكاً في هذه المجموعة!")

@app.on_message(filters.command(["المالكين", "الملاك"], "") & filters.group, group=3333333)
async def list_owners(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")

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
        return

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    allowed_users = [*dev, OWNER_ID, sourse_dev]
    if get.status != ChatMemberStatus.OWNER and message.from_user.id not in allowed_users:
        await message.reply_text("⚠️ فقط مالك الجروب يمكنه حذف المالكين!")
        return

    owners = get_group_owners(message.chat.id)
    if len(owners) <= 1:
        return await message.reply("**◍ لا يوجد مالكين إضافيين للحذف\n√**")

    owners_to_delete = owners[1:]
    deleted_count = 0
    for owner_id in owners_to_delete:
        if remove_group_owner(message.chat.id, owner_id):
            deleted_count += 1
    await message.reply(f"**◍ تم حذف {deleted_count} من المالكين بنجاح\n√**")


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

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if add_group_vip(message.chat.id, user_id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} مميز بنجاح 🌟\n√**")
    else:
        await message.reply(f"⚠️ {user.mention} هو بالفعل مميز في هذه المجموعة!")

@app.on_message(filters.command(["تنزيل مميز"], "") & filters.group, group=66616666)
async def demote_vip(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
        
    if remove_group_vip(message.chat.id, user_id):
        await message.reply(f"**◍ تم تنزيل العضو {user.mention} من المميزين بنجاح 🌟\n√**")
    else:
        await message.reply(f"⚠️ {user.mention} ليس مميزاً في هذه المجموعة!")

@app.on_message(filters.command(["المميزين"], "") & filters.group, group=77777077)
async def list_vips(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")

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

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة ادمن على الأقل لإستخدام الأمر\n√**")

    vips = get_group_vips(message.chat.id)
    if not vips:
        await message.reply("**◍ لا يوجد مميزين فى المجموعة\n√**")
        return

    result = group_vips_collection.delete_many({"group_id": message.chat.id})
    if result.deleted_count > 0:
        await message.reply(f"**◍ تم حذف جميع المميزين\n√**")
    else:
        await message.reply("**◍ لا يوجد مميزين فى المجموعة\n√**")

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


@app.on_message(filters.command(["رفع مطور اساسي"], "") & filters.group, group=8888818)
async def promote_main_dev(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور فقط\n√**")
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if add_main_developer(user.id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} مطور اساسي بنجاح 👨🏻‍💻\n√**")
    else:
        await message.reply(f"⚠️ {user.mention} مطور أساسي بالفعل.")

@app.on_message(filters.command(["تنزيل مطور اساسي"], "") & filters.group, group=8818)
async def demote_main_dev(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور فقط\n√**")
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if remove_main_developer(user.id):
        await message.reply(f"**◍ تم تنزيل العضو {user.mention} من المطورين الاساسين بنجاح 👨🏻‍💻\n√**")
    else:
        await message.reply(f"⚠️ {user.mention} ليس مطورًا أساسيًا.")


@app.on_message(filters.command(["المطورين", "المطورين 🕵🏻‍♂️"], ""), group=8814818)
async def list_main_devs(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")

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


@app.on_message(filters.command(["مسح المطورين الاساسين", "تنزيل المطورين الاساسين"], "") & filters.group, group=88810818)
async def confirm_delete_ala(client, message):
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False

    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى مالك البوت على الأقل لإستخدام الأمر\n√**")

    devs = get_main_developers()
    if not devs:
        await message.reply("**◍ لا يوجد مطورين اساسين\n√**")
        return

    result = main_devs_collection.delete_many({})
    if result.deleted_count > 0:
        await message.reply(f"**◍ تم حذف جميع المطورين الاساسين\n√**")
    else:
        await message.reply("**◍ لا يوجد مطورين اساسين\n√**")

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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if add_sub_developer(user.id):
        await message.reply(f"**◍ تم رفع العضو {user.mention} مطور ثانوي بنجاح 🕵🏻‍♂️\n√**")
    else:
        await message.reply(f"⚠️ {user.mention} مطور ثانوي بالفعل.")


@app.on_message(filters.command(["تنزيل مطور ثانوي"], "") & filters.group, group=108818)
async def demote_sub_dev(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ هذا الامر خاص بالمطور والمطور الاساسى فقط\n√**")
    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        user_id = user.id
    elif len(message.text.split()) > 2:
        _, _, target = message.text.split(maxsplit=2)
        if target.startswith("@"):
            try:
                user = await client.get_users(target.strip("@"))
                user_id = user.id
            except Exception:
                await message.reply_text("❌ لا يمكن العثور على المستخدم")
                return
        elif target.isdigit():
            try:
                user = await client.get_users(target)
                user_id = target
            except Exception:
                await message.reply_text("❌ رقم ID غير صحيح")
                return
        else:
            await message.reply_text("⚠️ يرجى إرسال معرف المستخدم أو الرد على رسالته")
            return
    else:
        ask1 = await zom_ask(client, message, "**◍ أرسل الآن آيدي المستخدم\n√**")
        try:
            user = await client.get_users(ask1.text)
            user_id = ask1.text
        except Exception:
            await message.reply_text("❌ رقم ID غير صحيح")
            return
    if remove_sub_developer(user.id):
        await message.reply(f"◍ تم تنزيل العضو {user.mention} من المطورين الثانويين بنجاح 🕵🏻‍♂️\n√")
    else:
        await message.reply(f"⚠️ {user.mention} ليس مطورًا ثانويًا.")


@app.on_message(filters.command(["المطورين الثانويين", "المطورين الثانويين 🧑🏻‍💻"], ""), group=888854818)
async def list_sub_devs(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_admin(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_group_vip(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مميز على الأقل لإستخدام الأمر\n√**")

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

#............................................ اكس او ...........................................................................    
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

games = {}

def create_board(board):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(board[0], callback_data="10"), InlineKeyboardButton(board[1], callback_data="11"), InlineKeyboardButton(board[2], callback_data="12")],
        [InlineKeyboardButton(board[3], callback_data="13"), InlineKeyboardButton(board[4], callback_data="14"), InlineKeyboardButton(board[5], callback_data="15")],
        [InlineKeyboardButton(board[6], callback_data="16"), InlineKeyboardButton(board[7], callback_data="17"), InlineKeyboardButton(board[8], callback_data="18")],
    ])

@app.on_message(filters.command(["اكس", "xo", "ox", "اكس او"], ""), group=76468513)
async def start_game(client, message: Message):
    board = ["⬜️"] * 9
    players = [message.from_user.id]
    current_player = 0
    finished = False

    m = await message.reply_text(
        "**◍ انقر على الزر أدناه لبدء\n√**",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("بدء اللعب 🎮", callback_data="join_game")]
        ])
    )

    games[m.id] = {
        "board": board,
        "players": players,
        "current_player": current_player,
        "finished": finished
    }

@app.on_callback_query(filters.regex("join_game"))
async def join_game(client, call: CallbackQuery):
    game = games.get(call.message.id)
    if not game or game["finished"]:
        await call.answer("اللعبة غير صالحة", show_alert=True)
        return

    if call.from_user.id not in game["players"]:
        game["players"].append(call.from_user.id)

    if len(game["players"]) < 2:
        await call.answer("في انتظار لاعب آخر...", show_alert=True)
        return

    await call.message.edit_text(
        "دور اللاعب الأول: ❌",
        reply_markup=create_board(game["board"])
    )

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for i, j, k in wins:
        if board[i] == board[j] == board[k] and board[i] != "⬜️":
            return board[i]
    return None

def is_draw(board):
    return all(cell != "⬜️" for cell in board)

@app.on_callback_query(
    filters.regex("1[0-8]")  # 10 to 18
)
async def play_move(client, call: CallbackQuery):
    game = games.get(call.message.id)
    if not game or game["finished"]:
        await call.answer("اللعبة انتهت ⚡️", show_alert=True)
        return

    user_id = call.from_user.id
    if user_id not in game["players"]:
        await call.answer("✋ لست مشاركًا في هذه اللعبة", show_alert=True)
        return

    if user_id != game["players"][game["current_player"]]:
        await call.answer("❌ ليس دورك!", show_alert=True)
        return

    index = int(call.data) - 10
    board = game["board"]

    if board[index] != "⬜️":
        await call.answer("❗️هذه الخانة مستخدمة", show_alert=True)
        return

    board[index] = "❌" if game["current_player"] == 0 else "⭕️"
    game["current_player"] = 1 - game["current_player"]

    winner = check_winner(board)
    if winner:
        winner_id = game["players"][0 if winner == "❌" else 1]
        user = await client.get_users(winner_id)
        await call.message.edit_text(f"🎉 الفائز: {user.first_name} ({winner})")
        game["finished"] = True
        return

    if is_draw(board):
        await call.message.edit_text("🤝 تعادل!")
        game["finished"] = True
        return

    next_player_id = game["players"][game["current_player"]]
    user = await client.get_users(next_player_id)
    symbol = "❌" if game["current_player"] == 0 else "⭕️"
    await call.message.edit_text(
        f"دور اللاعب: {symbol}\n{user.first_name}",
        reply_markup=create_board(board)
    )
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

@app.on_message(filters.command(["حجرة"], "")& filters.group, group=589)
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

@app.on_callback_query(filters.regex("^(حجرة|ورقة|مقص)$") & filters.group, group=58965)
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

@app.on_message(filters.command(["تحويل"], "") & filters.group, group=53)
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
@app.on_message(filters.command(["استثمار"], "") & filters.group, group=53)
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

@app.on_message(filters.command(["جلب نسخه البنك 🏦"], "") & filters.private, group=2314651445)
async def send_bank_backup(client, message: Message):
    file_path = "bank_data.json"
    try:
        await message.reply_document(
            document=file_path,
            caption="📤 هذه هي النسخة الحالية من قاعدة بيانات البنك\n√**"
        )
    except FileNotFoundError:
        await message.reply_text("**◍ الملف bank_data.json غير موجود\n√**")

UPLOAD_PATH = "bank_data.json"
@app.on_message(filters.command(["رفع نسخه البنك 🏦"], "") & filters.private, group=2314651446)
async def ask_for_bank_file(client: Client, message: Message):
    ask1 = await zom_ask(client, message, "**◍ أرسل الآن النسخة الجديدة بصيغة JSON\n√**")    
    downloaded_file = await ask1.download(file_name="new_bank.json")
    try:
        shutil.move(downloaded_file, UPLOAD_PATH)
        await ask1.reply_text("**◍ تم رفع النسخة الجديدة للبنك بنجاح\n√**")
    except Exception as e:
        await ask1.reply_text(f"**◍ فشل في استبدال النسخة\n√**")

@app.on_message(filters.command(["جلب نسخه لايكات 📥"], "") & filters.private, group=100801)
async def get_likes_backup(client, message: Message):
    file_path = "likes.json"
    if not os.path.exists(file_path):
        return await message.reply_text("**◍ الملف likes.json غير موجود\n√**")
    await message.reply_document(file_path, caption="📤 هذه هي النسخة الحالية من اللايكات\n√**")

@app.on_message(filters.command(["رفع نسخه لايكات 📤"], "") & filters.private, group=100902)
async def upload_likes_backup(client, message: Message):
    ask1 = await zom_ask(client, message, "**◍ أرسل الآن النسخة الجديدة بصيغة JSON\n√**")    
    file_path = await ask1.download(file_name="likes.json")
    await ask1.reply_text("**◍ تم رفع نسخة اللايكات بنجاح\n√**")

@app.on_message(filters.command(["جلب نسخه حمايه 📥"], "") & filters.private, group=10003)
async def get_locks_backup(client, message: Message):
    file_path = "chat_locks.json"
    if not os.path.exists(file_path):
        return await message.reply_text("**◍ الملف chat_locks.json غير موجود\n√**")
    await message.reply_document(file_path, caption="📤 هذه هي النسخة الحالية من الحمايه\n√**")

@app.on_message(filters.command(["رفع نسخه حمايه 📤"], "") & filters.private, group=10004)
async def upload_locks_backup(client, message: Message):
    ask1 = await zom_ask(client, message, "**◍ أرسل الآن النسخة الجديدة بصيغة JSON\n√**")    
    file_path = await ask1.download(file_name="chat_locks.json")
    await ask1.reply_text("**◍ تم رفع نسخة الحمايه بنجاح\n√**")

@app.on_message(filters.command(["جلب نسخه جروبات 📥"], "") & filters.private, group=10005)
async def get_group_backup(client, message: Message):
    file_path = "group_data.json"
    if not os.path.exists(file_path):
        return await message.reply_text("**◍ الملف group_data.json غير موجود\n√**")
    await message.reply_document(file_path, caption="📤 هذه هي النسخة الحالية من بيانات المجموعات\n√**")

@app.on_message(filters.command(["رفع نسخه جروبات 📤"], "") & filters.private, group=10006)
async def upload_group_backup(client, message: Message):
    ask1 = await zom_ask(client, message, "**◍ أرسل الآن النسخة الجديدة بصيغة JSON\n√**")    
    file_path = await ask1.download(file_name="group_data.json")
    await ask1.reply_text("**◍ تم رفع نسخة المجموعات بنجاح\n√**")

FILES = [
    "bank_data.json",
    "likes.json",
    "chat_locks.json",
    "group_data.json"
]

async def auto_backup_task(app: Client):
    await app.send_message(logger, "**◍ بدأ النسخ الاحتياطي التلقائي كل 24 ساعة\n√**")
    while True:
        for file in FILES:
            if os.path.exists(file):
                try:
                    await app.send_document(
                        chat_id=logger,
                        document=file,
                        caption=f"**◍ نسخة تلقائية من {file}\n√**"
                    )
                except Exception as e:
                    pass
            else:
                await app.send_message(logger, f"**◍ الملف {file} غير موجود\n√**")
        await asyncio.sleep(86400)

@app.on_message(filters.command("جلب نسخه تلقائي 📯", "") & filters.private, group=44656546)
async def start_backup_command(client, message):
    await message.reply_text("**◍ تم تفعيل النسخ الاحتياطي التلقائي\n√**")
    asyncio.create_task(auto_backup_task(client))
    
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["حظ"], "") & filters.group, group=53)
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
@app.on_message(filters.command(["اضف"], "") & filters.create(is_sudoer) & filters.group, group=46468)
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
@app.on_message(filters.command(["حذف حسابه"], "") & filters.create(is_sudoer) & filters.group, group=5)
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
@app.on_message(filters.command(["حذف حسابي"], "") & filters.group, group=6)
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
@app.on_message(filters.command(["تصفير البنك"], "") & filters.create(is_sudoer) & filters.group, group=7)
async def reset_bank(client, message):
    bank_data = {'accounts': {}}
    save_bank_data(bank_data)
    await message.reply_text('تم مسح جميع حسابات البنك')  
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["فتح البنك"], "") & filters.create(is_sudoer) & filters.group, group=8)
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
@app.on_message(filters.command(["قفل البنك"], "") & filters.create(is_sudoer) & filters.group, group=9)
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
@app.on_message(filters.regex("^(انشاء|انشاء حساب بنكي)$") & filters.group, group=710120513)
async def create_account(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    is_subscribed = await checkg_member_status(user_id, message, client)
    if not is_subscribed:
        return

    bank_data = load_bank_data()
    if str(user_id) in bank_data.get("accounts", {}):
        await message.reply_text("**لديك بالفعل حساب بنكي**")
        return

    await message.reply_text(
        text="**◍ عشان تسوي حساب لازم تختار نوع البطاقة\n√**",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("فيزا", callback_data=f"createbank_normal_{user_id}"),
             InlineKeyboardButton("اكسبريس", callback_data=f"createbank_gold_{user_id}"),
             InlineKeyboardButton("ماستر", callback_data=f"createbank_platinum_{user_id}")],
            [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")]
        ])
    )

@app.on_callback_query(filters.regex(r"^createbank_(normal|gold|platinum)_(\d+)$"), group=125787)
async def select_character(client, callback_query):
    try:
        visa_key, user_id = callback_query.data.split("_")[1:]
        user_id = int(user_id)

        if user_id != callback_query.from_user.id:
            await callback_query.answer("❌ هذا الخيار ليس لك", show_alert=True)
            return
    
        await callback_query.answer()

        await callback_query.message.edit_text(
            text="**◍ اختر شخصيتك في اللعبة :\n√**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("😈 شريرة", callback_data=f"bank_{visa_key}_evil_{user_id}"),
                InlineKeyboardButton("😇 طيبة", callback_data=f"bank_{visa_key}_good_{user_id}")],
                [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")]
            ])
        )
    except Exception as e:
        print(e)

@app.on_callback_query(filters.regex(r"^bank_(normal|gold|platinum)_(evil|good)_(\d+)$"), group=125787747)
async def finalize_account(client, callback_query):
    visa_key, character_type, user_id = callback_query.data.split("_")[1:]
    user_id = int(user_id)
    user_id_str = str(user_id)

    if user_id != callback_query.from_user.id:
        await callback_query.answer("❌ هذا الخيار ليس لك!", show_alert=True)
        return
    
    await callback_query.answer()

    bank_data = load_bank_data()
    if bank_data.get("accounts", {}).get(user_id_str):
        await callback_query.answer("لديك حساب بالفعل.", show_alert=True)
        return

    visa_names = {
        "normal": "فيزا",
        "gold": "اكسبريس",
        "platinum": "ماستر"
    }

    character_emojis = {
        "evil": "😈 شريرة",
        "good": "😇 طيبة"
    }

    account_number = random.randint(100000000000000, 999999999999999)
    username = callback_query.from_user.username or "None"

    bank_data.setdefault("accounts", {})
    bank_data["accounts"][user_id_str] = {
        'username': username,
        'balance': 50,
        'account_number': account_number,
        'thief': 0,
        'visa_type': visa_names[visa_key],
        'character': character_emojis[character_type]
    }
    save_bank_data(bank_data)
    await client.send_message(
        chat_id=callback_query.message.chat.id,
        text=(
            "🏦╖ تم انشاء حساب لك في بنك `محمد صالح`\n"
            "💵╢ بما انك عميل مميز تم اعطائك `50` دولار هديه\n"
            f"🔢╢ رقم حسابك ↢ `{account_number}`\n"
            f"💳╢ نوع البطاقة ↢ `{visa_names[visa_key].replace('💳 ', '')} كارد`\n"
            f"💸╢ فلوسك ↢ `50` دولار\n"
            f"👨‍🦰╜ شخصيتك ↢ `{character_emojis[character_type]}`"
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{BOT_USERNAME}?startgroup=new")]
        ])
    )
    await callback_query.message.delete()



@app.on_message(filters.command(["فلوسي"], "") & filters.group, group=11)
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
@app.on_message(filters.command(["فلوسه"], "") & filters.group, group=12)
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
@app.on_message(filters.command(["حسابي"], "") & filters.group, group=13)
async def view_account(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    bank_data = load_bank_data()
    if str(user_id) in bank_data['accounts']:
        username = bank_data['accounts'][str(user_id)]['username']
        balance = bank_data['accounts'][str(user_id)]['balance']
        account_number = bank_data['accounts'][str(user_id)]['account_number']
        account = bank_data["accounts"][str(user_id)]

        info_text = (
            f"**🏦 معلومات حسابك البنكي:\n**"
            f"**👨‍🦳╖ اسمك ↢ @{account.get('username', 'غير متوفر')}\n**"
            f"**🔢╢ رقم حسابك ↢ `{account.get('account_number')}`\n**"
            f"**💳╢ نوع البطاقة ↢ {account.get('visa_type')}\n**"
            f"**💸╢ رصيدك ↢ {account.get('balance')} دولار\n**"
            f"**🕵️‍♂️╢ شخصيتك ↢ {account.get('character')}\n**"
            f"**👨‍🦰╜ المبلغ المسروق ↢ {account.get('thief', 0)}**"
        )
        await message.reply_text(f"{info_text}")
    else:
        await message.reply_text("↢ ماعندك حساب بنكي ارسل ↢ ( `انشاء حساب بنكي` )")
##############££££££££££#############££££££££££#########££££#
@app.on_message(filters.command(["بنكه"], "") & filters.group, group=14)
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

@app.on_message(filters.command(["مضاربه", "مضاربة"], "") & filters.group, group=15) 
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

@app.on_message(filters.command(["رشوة", "رشوه"], "") & filters.group, group=16)
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

@app.on_message(filters.command(["عجلة الحظ", "عجله الحظ"], "") & filters.group, group=17)
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

@app.on_message(filters.command(["بقشيش"], "") & filters.group, group=18)
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

@app.on_message(filters.command(["راتب"], "") & filters.group, group=19)
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

@app.on_message(filters.command(["سرقة", "سرقه"], "") & filters.group, group=20640)
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

@app.on_message(filters.command(["شرطة", "شرطه"], "") & filters.group, group=21)
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

@app.on_message(filters.command(["حماية", "حمايه"], "") & filters.group, group=22)
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

@app.on_message(filters.command(["توب الحراميه", "توب سرقه", "توب السرقة", "توب السرقه", "توب سرقة"], "") & filters.group, group=22)
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
@app.on_message(filters.command(["توب فلوس","توب الفلوس"], "") & filters.group, group=20543)
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
    
@app.on_message(filters.command(["البنك", "بنك"], "") & filters.group, group=476785)
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
@app.on_message(filters.command(["الساعه","الوقت","ساعه", "التاريخ"], "") & filters.group, group=76763)
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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

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


@app.on_message(filters.regex("حذف الردود") & filters.group, group=45852)
async def delete_all_replies(client, message):
    group_id = message.chat.id
    is_subscribed = await checkg_member_status(message.from_user.id, message, client)
    if not is_subscribed:
        return False
    user_id = message.from_user.id if message.from_user else "None"
    member = await client.get_chat_member(group_id, user_id)
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    if group_id not in rododda or not rododda[group_id]:
        return await message.reply_text("ℹ️ | لا توجد ردود لحذفها.")
    try:
        ask = await zom_ask(client, message, "**⚠️ | هل أنت متأكد أنك تريد حذف جميع الردود في هذه المجموعة؟\nأرسل `نعم` للتأكيد أو `إلغاء` للإلغاء.**")
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
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

    try:
        ask = await zom_ask(client, message, "🔹 أرسل *اسم الرد* الذي تريد حذفه:")
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
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")

    try:
        ask1 = await zom_ask(client, message, "**⇜ حلو , الان ارسل اسم الرد\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆**")
        reply_name = ask1.text.strip()

        await asyncio.sleep(1.5)

        ask2 = await zom_ask(client, message, "**⇜ حلو , الان ارسل جواب الرد\n⇜ ( نص, صوره, فيديو, متحركه, بصمه, اغنيه )\n⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆**")
        reply = ask2
        if ask2.text:
            reply_data = {"type": "text", "data": ask2.text, "caption": ask2.text}
        elif ask2.photo:
            reply_data = {
                "type": "photo",
                "data": ask2.photo.file_id,
                "caption": ask2.caption or ""
            }

        elif ask2.video:
            reply_data = {
                "type": "video",
                "data": ask2.video.file_id,
                "caption": ask2.caption or ""
            }

        elif ask2.animation:
            reply_data = {
                "type": "animation",
                "data": ask2.animation.file_id,
                "caption": ask2.caption or ""
            }

        elif ask2.voice:
            reply_data = {
                "type": "voice",
                "data": ask2.voice.file_id
            }
        elif ask2.audio:
            reply_data = {
                "type": "audio",
                "data": ask2.audio.file_id,
                "caption": ask2.caption or ""
            }
        else:
            return await message.reply_text("⚠️ نوع غير مدعوم.")
        if group_id not in rododda:
            rododda[group_id] = {}
        rododda[group_id][reply_name] = reply_data
        await client.send_message(group_id, f"**✅ | تم حفظ الرد {reply_name} بنجاح**")
        print(reply_data)
    except asyncio.TimeoutError:
        await message.reply_text("⏰ انتهى الوقت.")
    except Exception as e:
        await message.reply_text(f"❌ حدث خطأ: {e}")


@app.on_message(filters.text & filters.group, group=57854)
async def trigger_reply(client, message):
    group_id = message.chat.id
    if group_id not in rododda:
        return
    
    for reply_name in rododda[group_id]:
        if reply_name in message.text:
            reply_data = rododda[group_id][reply_name]

            try:
                reply_text = reply_data.get("caption", "")
                user_id = message.from_user.id
                chat_member = await client.get_chat_member(group_id, user_id)
                user_status = chat_member.status

                if user_status == "administrator":
                    rank = "مشرف"
                elif user_status == "owner":
                    rank = "مالك"
                else:
                    rank = "عضو"

                reply_text = reply_text.replace("{الرتبه}", rank)
                if reply_data["type"] == "video":
                    await message.reply_video(reply_data["data"], caption=reply_text)
                elif reply_data["type"] == "photo":
                    await message.reply_photo(reply_data["data"], caption=reply_text)
                elif reply_data["type"] == "animation":
                    await message.reply_animation(reply_data["data"], caption=reply_text)
                elif reply_data["type"] == "voice":
                    await message.reply_voice(reply_data["data"])
                elif reply_data["type"] == "audio":
                    await message.reply_audio(reply_data["data"], caption=reply_text)
                else:  # نص فقط
                    await message.reply_text(reply_text)
            except Exception as e:
                print(f"[❌] Error in trigger_reply: {e}")
                await message.reply_text("❗ | حدث خطأ أثناء إرسال الرد.")
            break  # أول رد مطابق فقط

#............................................ الردود ........................................................................... 


#............................................ الردود العام ........................................................................... 
global_replies = {}

@app.on_message(filters.regex("الردود العامة 📝") & filters.private, group = 219723435)
async def show_all_global_replies(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    group_id = message.chat.id
    
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
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


@app.on_message(filters.regex("حذف رد عام 🗑") & filters.private, group = 2102398554)
async def delete_global_reply(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    group_id = message.chat.id    
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
    
    try:
        ask1 = await zom_ask(client, message, "**◍ ارسل اسم الرد العام اللذي تريد حذفه 📝\n√**")
        reply_name = ask1.text.strip()
        
        if reply_name in global_replies:
            del global_replies[reply_name]
            await message.reply_text(f"**◍ تم حذف الرد العام بنجاح 🗑\n√**")
        else:
            await message.reply_text("**◍ عذرا هذا الرد غير موجود ❌\n√**")
    except Exception:
        await message.reply_text("❗ | حدث خطأ أثناء العملية.")


@app.on_message(filters.regex("اضف رد عام 💬") & filters.private, group = 2148214)
async def add_global_reply(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    group_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة مطور ثانوي على الأقل لإستخدام الأمر\n√**")
    
    
    try:
        ask1 = await zom_ask(client, message, "**◍ ارسل اسم الرد العام 📝\n√**")
        reply_name = ask1.text.strip()

        await asyncio.sleep(1.5)

        ask2 = await zom_ask(client, message, 
            "⇜ حلو , الحين ارسل جواب الرد العام\n"
            "⇜ ( نص, صوره, فيديو, متحركه, بصمه, اغنيه )\n"
            "⋆┄─┄─┄─┄┄─┄─┄─┄─┄┄⋆\n"
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
            try: 
                reply_data = global_replies[reply_name]        
                reply_text = reply_data["caption"]
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
            except Exception as e:
                pass
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

@app.on_message(filters.text & filters.group & filters.regex(r"^(ترند|توب|المتفاعلين)$"), group=145897)
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
    top_text = f"\u200E{titles[top_type]} في {data['groups'][group_id]['title']}\n\n"
    for i, user in enumerate(top_stats_sorted[:20], 1):
        emoji = "🥇" if i == 1 else ("🥈" if i == 2 else ("🥉" if i == 3 else ""))
        line = f"{i}) {emoji} {user['count']} | {user['first_name']}"
        top_text += f"\u200E{line}\n"
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
from datetime import datetime

# التخزين المؤقت
WELCOME_DATA = {}

DEFAULT_WELCOME = (
    "◍ نورتنا يا {mention} 🤍\n"
    "❬ ممنوع الالفاظ والبرايفت واللينكات ❭ ⚠️\n"
    "❬ غير كدة كلنا اخوات واصحاب ❭ ❤️ √"
)

# تغيير الترحيب
@app.on_message(filters.command("تغيير الترحيب", prefixes="") & filters.group,group=5454556)
async def change_welcome_message(client: Client, message: Message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    ask1 = await zom_ask(client, message, "**✏️ أرسل الآن رسالة الترحيب التي تريدها.\n\n🌐 يمكنك استخدام المتغيرات التالية:\n◍ {mention} : منشن العضو\n◍ {username} : معرف المستخدم\n◍ {id} : ايدي العضو\n◍ {date} : تاريخ الانضمام\n◍ {time} : وقت الانضمام\n◍ {first_name} : الاسم الأول\n◍ {chat} : اسم المجموعة\n◍ {admin} : يوزر مالك الجروب\n◍ {members} : عدد الأعضاء\n\n📌 بعد إرسال الرسالة سيتم سؤالك عن نوع الصورة\n√**")
    user_text = ask1.text

    WELCOME_DATA[chat_id] = {
        "enabled": True,
        "text": user_text,
        "photo": "none",
        "setter_id": user_id
    }

    await message.reply(
        "✅ تم حفظ رسالة الترحيب!\n📌 اختر نوع صورة الترحيب:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📄 بدون صورة", callback_data="welcome_type:none")],
            [InlineKeyboardButton("👤 صورة العضو", callback_data="welcome_type:user")],
            [InlineKeyboardButton("👥 صورة الجروب", callback_data="welcome_type:chat")]
        ])
    )


# زر نوع الصورة
@app.on_callback_query(filters.regex(r"^welcome_type:(none|user|chat)$"))
async def set_welcome_type(client: Client, callback_query):
    choice = callback_query.data.split(":")[1]
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id

    if chat_id not in WELCOME_DATA or WELCOME_DATA[chat_id]["setter_id"] != user_id:
        return await callback_query.answer("❌ غير مسموح لك.", show_alert=True)

    WELCOME_DATA[chat_id]["photo"] = choice
    types = {"none": "📄 بدون صورة", "user": "👤 صورة العضو", "chat": "👥 صورة الجروب"}
    await callback_query.message.edit_text(f"✅ تم اختيار نوع الصورة: {types[choice]}")

# عرض الترحيب
@app.on_message(filters.command(["عرض الترحيب", "الترحيب"], prefixes="") & filters.group, group=56489618500)
async def show_welcome(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    data = WELCOME_DATA.get(chat_id)
    text = data["text"] if data else DEFAULT_WELCOME
    enabled = data["enabled"] if data else True
    photo = data["photo"] if data else "none"
    types = {"none": "📄 بدون صورة", "user": "👤 صورة العضو", "chat": "👥 صورة الجروب"}

    await message.reply(
        f"**رسالة الترحيب:**\n{text}\n\n"
        f"**الحالة:** {'✅ مفعلة' if enabled else '🛑 معطلة'}\n"
        f"**نوع الصورة:** {types.get(photo, '❓')}"
    )

# تعطيل الترحيب
@app.on_message(filters.command("تعطيل الترحيب", prefixes="") & filters.group, group=9984896500)
async def disable_welcome(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    if chat_id not in WELCOME_DATA:
        WELCOME_DATA[chat_id] = {
            "enabled": False,
            "text": DEFAULT_WELCOME,
            "photo": "none",
            "setter_id": message.from_user.id
        }
    else:
        WELCOME_DATA[chat_id]["enabled"] = False
    await message.reply("🛑 تم تعطيل الترحيب.")

# تفعيل الترحيب
@app.on_message(filters.command("تفعيل الترحيب", prefixes="") & filters.group, group=50764896500)
async def enable_welcome(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    if chat_id not in WELCOME_DATA:
        WELCOME_DATA[chat_id] = {
            "enabled": True,
            "text": DEFAULT_WELCOME,
            "photo": "none",
            "setter_id": message.from_user.id
        }
    else:
        WELCOME_DATA[chat_id]["enabled"] = True
    await message.reply("✅ تم تفعيل الترحيب.")

from zoneinfo import ZoneInfo
from pyrogram import enums

@app.on_chat_member_updated(filters.group, group=569874896500)
async def welcome_user_updated(client: Client, chat_member_update: ChatMemberUpdated):
    try:
        if chat_member_update.new_chat_member.status == enums.ChatMemberStatus.MEMBER:
            chat_id = chat_member_update.chat.id                
            welcome = WELCOME_DATA.get(chat_id, {
                "enabled": True,
                "text": DEFAULT_WELCOME,
                "photo": "none"
            })

            if not welcome["enabled"]:
                return

            now = datetime.now(ZoneInfo("Africa/Cairo"))
            members_count = await client.get_chat_members_count(chat_id)
            user = chat_member_update.from_user
            text = welcome["text"]
            replacements = {
                "{mention}": chat_member_update.from_user.mention,
                "{username}": f"@{user.username}" if user.username else "لا يوجد",
                "{id}": str(user.id),
                "{date}": now.strftime("%Y-%m-%d"),
                "{time}": now.strftime("%H:%M:%S"),
                "{first_name}": user.first_name or "",
                "{chat}": chat_member_update.chat.title,
                "{members}": str(members_count)
            }
            for key, val in replacements.items():
                text = text.replace(key, val)
            try:
                if welcome["photo"] == "user":
                    photos = [p async for p in client.get_chat_photos(user.id, limit=1)]
                    if photos:
                        await client.send_photo(chat_id, photos[0].file_id, caption=f"**{text}**")
                    else:
                        await client.send_message(chat_id, f"**{text}**")
                elif welcome["photo"] == "chat":
                    if chat_member_update.chat.photo:
                        photo = await client.download_media(chat_member_update.chat.photo.big_file_id)
                        await client.send_photo(chat_id, photo, caption=f"**{text}**")
                    else:
                        await client.send_message(chat_id, f"**{text}**")
                else:
                    await client.send_message(chat_id, f"**{text}**")
            except Exception as e:
                await client.send_message(chat_id, f"{text}\n⚠️ حدث خطأ: {e}")
    except Exception as e:
        pass

#............................................  الترحيب ........................................................................... 
# ............................................ المغادرة ........................................................................... 
# التخزين المؤقت للمغادرة
LEAVE_DATA = {}

DEFAULT_LEAVE = (
    "◍ انت مش جدع يا {mention} 🥺\n"
    "❬ حد يكون فى روم زى ده ويخرج ❭ 🙄\n"
    "❬ ده حتى كلنا اخوات واصحاب ❭ 🥺\n"
    "❬ يلا بالسلامات ❭ ❤️😂"
)

# تغيير رسالة المغادرة
@app.on_message(filters.command("تغيير المغادره", prefixes="") & filters.group, group=1278456567)
async def change_leave_message(client: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "None"
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    ask = await zom_ask(
        client,
        message,
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
        "📌 بعد إرسال الرسالة سيتم سؤالك عن نوع الصورة"
    )
    user_text = ask.text

    LEAVE_DATA[chat_id] = {
        "enabled": True,
        "text": user_text,
        "photo": "none",
        "setter_id": user_id
    }

    await message.reply(
        "✅ تم حفظ رسالة المغادرة!\n📌 اختر نوع صورة المغادرة:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📄 بدون صورة", callback_data="leave_type:none")],
            [InlineKeyboardButton("👤 صورة العضو", callback_data="leave_type:user")],
            [InlineKeyboardButton("👥 صورة الجروب", callback_data="leave_type:chat")]
        ])
    )

# تحديد نوع الصورة للمغادرة
@app.on_callback_query(filters.regex(r"^leave_type:(none|user|chat)$"))
async def set_leave_type(client: Client, callback_query):
    choice = callback_query.data.split(":")[1]
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id

    if chat_id not in LEAVE_DATA or LEAVE_DATA[chat_id]["setter_id"] != user_id:
        return await callback_query.answer("❌ غير مسموح لك.", show_alert=True)

    LEAVE_DATA[chat_id]["photo"] = choice
    types = {"none": "📄 بدون صورة", "user": "👤 صورة العضو", "chat": "👥 صورة الجروب"}
    await callback_query.message.edit_text(f"✅ تم اختيار نوع الصورة: {types[choice]}")

# تفعيل المغادرة
@app.on_message(filters.command("تفعيل المغادره", prefixes="") & filters.group, group=12340014)
async def enable_leave(client: Client, message: Message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    chat_id = message.chat.id
    if chat_id not in LEAVE_DATA:
        LEAVE_DATA[chat_id] = {
            "enabled": True,
            "text": DEFAULT_LEAVE,
            "photo": "none",
            "setter_id": message.from_user.id
        }
    else:
        LEAVE_DATA[chat_id]["enabled"] = True
    await message.reply("✅ تم تفعيل المغادرة.")

# تعطيل المغادرة
@app.on_message(filters.command("تعطيل المغادره", prefixes="") & filters.group, group=18234569)
async def disable_leave(client: Client, message: Message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    chat_id = message.chat.id
    if chat_id not in LEAVE_DATA:
        LEAVE_DATA[chat_id] = {
            "enabled": False,
            "text": DEFAULT_LEAVE,
            "photo": "none",
            "setter_id": message.from_user.id
        }
    else:
        LEAVE_DATA[chat_id]["enabled"] = False
    await message.reply("🛑 تم تعطيل المغادرة.")

@app.on_chat_member_updated(filters.group, group=569879197500)
async def leave_usr_updated(client: Client, chat_member_update: ChatMemberUpdated):
    try:
        if chat_member_update.old_chat_member.status == ChatMemberStatus.MEMBER and \
           chat_member_update.new_chat_member.status == ChatMemberStatus.LEFT:

            chat_id = chat_member_update.chat.id
            user = chat_member_update.from_user
            leave = LEAVE_DATA.get(chat_id, {
                "enabled": True,
                "text": DEFAULT_LEAVE,
                "photo": "none"
            })

            if not leave["enabled"]:
                return

            now = datetime.now(ZoneInfo("Africa/Cairo"))
            members_count = await client.get_chat_members_count(chat_id)
            text = leave["text"]
            replacements = {
                "{mention}": user.mention,
                "{username}": f"@{user.username}" if user.username else "لا يوجد",
                "{id}": str(user.id),
                "{date}": now.strftime("%Y-%m-%d"),
                "{time}": now.strftime("%H:%M:%S"),
                "{first_name}": user.first_name or "",
                "{chat}": chat_member_update.chat.title,
                "{members}": str(members_count)
            }

            for key, val in replacements.items():
                text = text.replace(key, val)

            try:
                if leave["photo"] == "user":
                    photos = [p async for p in client.get_chat_photos(user.id, limit=1)]
                    if photos:
                        await client.send_photo(chat_id, photos[0].file_id, caption=f"**{text}**")
                    else:
                        await client.send_message(chat_id, f"**{text}**")
                elif leave["photo"] == "chat":
                    if chat_member_update.chat.photo:
                        photo = await client.download_media(chat_member_update.chat.photo.big_file_id)
                        await client.send_photo(chat_id, photo, caption=f"**{text}**")
                    else:
                        await client.send_message(chat_id, f"**{text}**")
                else:
                    await client.send_message(chat_id, f"**{text}**")
            except Exception as e:
                await client.send_message(chat_id, f"{text}\n⚠️ حدث خطأ: {e}")

    except Exception as ex:
        print(ex)
# ............................................ المغادرة ........................................................................... 
# ............................................ الالعاب ........................................................................... 

@app.on_message(filters.text & filters.group & filters.regex(r"^تخ$"), group=7028046857)
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
    gif_url = "https://t.me/uu_u_e/30"
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

# ............................................ الالعاب ........................................................................... 
from pyrogram.errors import FloodWait

TIME_STYLES = [
    ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    ["𝟎", "𝟏", "𝟐", "𝟑", "𝟒", "𝟓", "𝟔", "𝟕", "𝟖", "𝟗"],
    ["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
    ["⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"],
    ["⓿", "❶", "❷", "❸", "❹", "❺", "❻", "❼", "❽", "❾"],
    ["𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", "𝟞", "𝟟", "𝟠", "𝟡"],
    ["０", "１", "２", "３", "４", "５", "６", "７", "８", "９"],
    ["𝟶", "𝟷", "𝟸", "𝟹", "𝟺", "𝟻", "𝟼", "𝟽", "𝟾", "𝟿"]
]
time_running = False
chosen_style = 0
original_name = None

def zhrf_time(t: str, style_index: int) -> str:
    styled = ""
    for c in t:
        if c.isdigit():
            styled += TIME_STYLES[style_index][int(c)]
        else:
            styled += c
    return styled

@app.on_message(filters.command(["تفعيل اسم وقتي ⏱️"], "") & filters.private, group=45531354)
async def activate_time_name(client, message):
    global time_running
    if time_running:
        await message.reply("الاسم الوقتي مفعل بالفعل.")
        return
    buttons = [
        [InlineKeyboardButton("ستايل 1", callback_data="style_0"),
         InlineKeyboardButton("ستايل 2", callback_data="style_1")],
        [InlineKeyboardButton("ستايل 3", callback_data="style_2"),
         InlineKeyboardButton("ستايل 4", callback_data="style_3")],
        [InlineKeyboardButton("ستايل 5", callback_data="style_4"),
         InlineKeyboardButton("ستايل 6", callback_data="style_5")],
        [InlineKeyboardButton("ستايل 7", callback_data="style_6"),
         InlineKeyboardButton("ستايل 8", callback_data="style_7")]
    ]

    styles_list = """اختر ستايل الساعة التي تريدها لاسمك المؤقت:
📋 قائمة الخطوط المتاحة:

1: ₀₁₂₃₄₅₆₇₈₉  
2: 𝟎𝟏𝟐𝟑𝟒𝟓𝟖𝟕𝟖𝟗  
3: 𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵  
4: ⓪①②③④⑤⑥⑦⑧⑨  
5: ⓿❶❷❸❹❺❻❼❽❾  
6: 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡  
7: ０１２３４５６７８９  
8: 𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"""

    await message.reply(styles_list, reply_markup=InlineKeyboardMarkup(buttons))

old_name = ""

@app.on_message(filters.command(["تعطيل اسم وقتي 📍"], ""), group=45531354)
async def deactivate_time_name(client, message):
    global old_name
    if old_name:
        await user.update_profile(first_name=old_name)
        await message.reply("تم تعطيل الاسم الوقتي وإرجاع الاسم القديم.")
    else:
        await message.reply("لا يوجد اسم قديم لاسترجاعه.")


@app.on_callback_query(filters.regex(r"style_\d"))
async def style_chosen(client, callback_query):
    global chosen_style, time_running, original_name, old_name
    chosen_style = int(callback_query.data.split("_")[1])
    await callback_query.message.delete()
    user_info = await user.get_me()
    original_name = user_info.first_name
    old_name = original_name
    await callback_query.message.reply("تم اختيار ستايل الوقت ✅\nجارٍ تفعيل الاسم الوقتي...")
    if not time_running:
        time_running = True
        asyncio.create_task(update_name_loop(client))

async def update_name_loop(client):
    global time_running, original_name
    last_time = ""
    while time_running:
        try:
            time_str = datetime.now(pytz.timezone("Africa/Cairo")).strftime('%I:%M')
            if time_str != last_time:
                last_time = time_str
                styled_time = zhrf_time(time_str, chosen_style)
                new_name = f"{original_name} {styled_time}"
                await user.update_profile(first_name=new_name)
            await asyncio.sleep(20)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as e:
            print(f"[Error] أثناء تحديث الاسم: {e}")
            await asyncio.sleep(30)


TIME_FORMATS = [
    ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    ["𝟎", "𝟏", "𝟐", "𝟑", "𝟒", "𝟓", "𝟔", "𝟕", "𝟖", "𝟗"],
    ["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
    ["⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"],
    ["⓿", "❶", "❷", "❸", "❹", "❺", "❻", "❼", "❽", "❾"],
    ["𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", "𝟞", "𝟟", "𝟠", "𝟡"],
    ["０", "１", "２", "３", "４", "５", "６", "７", "８", "９"],
    ["𝟶", "𝟷", "𝟸", "𝟹", "𝟺", "𝟻", "𝟼", "𝟽", "𝟾", "𝟿"]
]

is_bio_active = False  
selected_style = 0  # تم تغيير المتغير
original_bio = None
old_bio = ""

def apply_time_format(t: str, format_index: int) -> str:
    formatted = ""
    for c in t:
        if c.isdigit():
            formatted += TIME_FORMATS[format_index][int(c)]
        else:
            formatted += c
    return formatted

@app.on_message(filters.command(["تفعيل بايو وقتي 🕰"], ""), group=45054)
async def activate_time_bio(client, message):
    global is_bio_active
    if is_bio_active:
        await message.reply("البايو الوقتى مفعل بالفعل.")
        return

    buttons = [
        [InlineKeyboardButton("ستايل 1", callback_data="stylee_0"),
         InlineKeyboardButton("ستايل 2", callback_data="stylee_1")],
        [InlineKeyboardButton("ستايل 3", callback_data="stylee_2"),
         InlineKeyboardButton("ستايل 4", callback_data="stylee_3")],
        [InlineKeyboardButton("ستايل 5", callback_data="stylee_4"),
         InlineKeyboardButton("ستايل 6", callback_data="stylee_5")],
        [InlineKeyboardButton("ستايل 7", callback_data="stylee_6"),
         InlineKeyboardButton("ستايل 8", callback_data="stylee_7")]
    ]

    styles_list = """اختر ستايل الساعة التي تريدها لبايوك المؤقت:
📋 قائمة الخطوط المتاحة:

1: ₀₁₂₃₄₅₆₇₈₉  
2: 𝟎𝟏𝟐𝟓  
3: 𝟬𝟭𝟮𝟮  
4: ⓪①②③④⑤⑥⑦⑧⑨  
5: ⓿❶❷❸❹❺❻❼❽❾  
6: 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡  
7: ０１２６７８９  
8: 𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"""

    await message.reply(styles_list, reply_markup=InlineKeyboardMarkup(buttons))

@app.on_message(filters.command(["تعطيل بايو وقتي 🔺"], ""), group=4559874)
async def deactivate_time_bio(client, message):
    global is_bio_active, old_bio
    if not is_bio_active:
        await message.reply("البايو الوقتى غير مفعل حاليًا.")
        return

    if old_bio:
        await user.update_profile(bio=old_bio)
        is_bio_active = False  # تعطيل البايو الوقتى
        await message.reply("تم تعطيل البايو الوقتى وإرجاع البايو القديم.")
    else:
        await message.reply("لا يوجد بايو قديم لاسترجاعه.")  # تأكد من أن البايو موجود

@app.on_callback_query(filters.regex(r"stylee_\d"))
async def stye_chosen(client, callback_query):
    global selected_style, is_bio_active, original_bio, old_bio
    selected_style = int(callback_query.data.split("_")[1])
    user_info = await user.get_me()
    try:
        original_bio = user_info.bio  # محاولة الحصول على البايو
    except AttributeError:
        original_bio = None
    old_bio = original_bio
    await callback_query.message.delete()
    await callback_query.message.reply("تم اختيار ستايل الوقت ✅\nجارٍ تفعيل البايو الوقتى...")
    
    if not is_bio_active:
        is_bio_active = True
        asyncio.create_task(updae_bio_loop(client))

async def updae_bio_loop(client):
    global is_bio_active, original_bio
    last_time = ""
    while is_bio_active:
        try:
            time_str = datetime.now(pytz.timezone("Africa/Cairo")).strftime('%I:%M')
            if time_str != last_time:
                last_time = time_str
                formatted_time = apply_time_format(time_str, selected_style)
                new_bio = f"{original_bio} {formatted_time}"
                await user.update_profile(bio=new_bio)
            await asyncio.sleep(20)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as e:
            print(f"[Error] أثناء تحديث البايو: {e}")
            await asyncio.sleep(30)




TIME_FRMATS = [
    ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    ["𝟎", "𝟏", "𝟐", "𝟑", "𝟒", "𝟓", "𝟔", "𝟕", "𝟖", "𝟗"],
    ["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
    ["⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"],
    ["⓿", "❶", "❷", "❸", "❹", "❺", "❻", "❼", "❽", "❾"],
    ["𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", "𝟞", "𝟟", "𝟠", "𝟡"],
    ["０", "１", "２", "３", "４", "５", "６", "７", "８", "９"],
    ["𝟶", "𝟷", "𝟸", "𝟹", "𝟺", "𝟻", "𝟼", "𝟽", "𝟾", "𝟿"]
]

# القاموس لتخزين بيانات الجروبات
groups_data = {}

chosen_styEEle = 0
original_group_name = None
is_group_time_active = False

def time_to_style(t: str, style_index: int) -> str:
    styled = ""
    for c in t:
        if c.isdigit():
            styled += TIME_FRMATS[style_index][int(c)]
        else:
            styled += c
    return styled

@app.on_message(filters.command(["تفعيل الجروب وقتي"], "") & filters.group, group=45354)
async def activate_group_time_name(client, message):
    global chosen_styEEle, is_group_time_active

    if message.chat.id in groups_data and groups_data[message.chat.id]["active"]:
        await message.reply("الاسم الوقتي مفعل بالفعل لهذا الجروب.")
        return

    buttons = [
        [InlineKeyboardButton("ستايل 1", callback_data="stWyle_0"),
         InlineKeyboardButton("ستايل 2", callback_data="stWyle_1")],
        [InlineKeyboardButton("ستايل 3", callback_data="stWyle_2"),
         InlineKeyboardButton("ستايل 4", callback_data="stWyle_3")],
        [InlineKeyboardButton("ستايل 5", callback_data="stWyle_4"),
         InlineKeyboardButton("ستايل 6", callback_data="stWyle_5")],
        [InlineKeyboardButton("ستايل 7", callback_data="stWyle_6"),
         InlineKeyboardButton("ستايل 8", callback_data="stWyle_7")]
    ]

    styles_list = """اختر ستايل الساعة التي تريدها لبايوك المؤقت:
📋 قائمة الخطوط المتاحة:

1: ₀₁₂₃₄₅₆₇₈₉  
2: 𝟎𝟏𝟐𝟓  
3: 𝟬𝟭𝟮𝟮
4: ⓪①②③④⑤⑥⑦⑧⑨  
5: ⓿❶❷❸❹❺❻❼❽❾  
6: 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡  
7: ０１２６７８９  
8: 𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"""

    await message.reply(styles_list, reply_markup=InlineKeyboardMarkup(buttons))


@app.on_callback_query(filters.regex(r"stWyle_\d"))
async def style_chosen(client, callback_query):
    global chosen_styEEle, original_group_name

    chosen_styEEle = int(callback_query.data.split("_")[1])

    chat_info = await client.get_chat(callback_query.message.chat.id)
    original_group_name = chat_info.title

    groups_data[callback_query.message.chat.id] = {
        "active": True,
        "style": chosen_styEEle
    }

    await callback_query.message.delete()
    await callback_query.message.reply("تم اختيار ستايل الوقت ✅\nجارٍ تفعيل الاسم الوقتي...")

    asyncio.create_task(update_group_name_loop(client, callback_query.message.chat.id))

async def update_group_name_loop(client, chat_id):
    last_time = ""
    while True:
        try:
            time_str = datetime.now(pytz.timezone("Africa/Cairo")).strftime('%I:%M')
            if time_str != last_time:
                last_time = time_str
                styled_time = time_to_style(time_str, groups_data[chat_id]["style"])
                new_group_name = f"{original_group_name} {styled_time}"
                await client.set_chat_title(chat_id, new_group_name)
            await asyncio.sleep(20)
        except Exception as e:
            print(f"[Error] أثناء تحديث الاسم: {e}")
            await asyncio.sleep(30)

@app.on_message(filters.command(["تعطيل الجروب وقتي"], "") & filters.group, group=48354)
async def deactivate_group_time_name(client, message):
    if message.chat.id in groups_data and groups_data[message.chat.id]["active"]:
        del groups_data[message.chat.id]
        await client.set_chat_title(message.chat.id, original_group_name)
        await message.reply("تم تعطيل الاسم الوقتي وإرجاع الاسم الأصلي.")
    else:
        await message.reply("الاسم الوقتي غير مفعل لهذا الجروب.")



TIME_FORMATS = [
    ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"],
    ["𝟎", "𝟏", "𝟐", "𝟑", "𝟒", "𝟓", "𝟖", "𝟘", "𝟙", "𝟚"],
    ["𝟬", "𝟭", "𝟮", "𝟯", "𝟰", "𝟱", "𝟲", "𝟳", "𝟴", "𝟵"],
    ["⓪", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"],
    ["⓿", "❶", "❷", "❸", "❹", "❺", "❻", "❼", "❽", "❾"],
    ["𝟘", "𝟙", "𝟚", "𝟛", "𝟜", "𝟝", "𝟞", "𝟟", "𝟠", "𝟡"],
    ["０", "１", "２", "３", "４", "５", "６", "７", "８", "９"],
    ["𝟶", "𝟷", "𝟸", "𝟹", "𝟺", "𝟻", "𝟼", "𝟽", "𝟾", "𝟿"]
]

# القاموس لتخزين بيانات الجروبات
group_data = {}

chosean_style = 0
originl_bio = None
is_bio_enabled = False

def formaat_time(time_str: str, style_idx: int) -> str:
    formatted = ""
    for char in time_str:
        if char.isdigit():
            formatted += TIME_FORMATS[style_idx][int(char)]
        else:
            formatted += char
    return formatted

@app.on_message(filters.command(["تفعيل بايو وقتي"], "") & filters.group, group=45354)
async def enable_group_bio_time(client, message):
    global chosean_style, is_bio_enabled
    if message.chat.id in group_data and group_data[message.chat.id]["bio_enabled"]:
        await message.reply("بايو الجروب الوقتي مفعل بالفعل.")
        return

    buttons = [
        [InlineKeyboardButton("ستايل 1", callback_data="styale_0"),
         InlineKeyboardButton("ستايل 2", callback_data="styale_1")],
        [InlineKeyboardButton("ستايل 3", callback_data="styale_2"),
         InlineKeyboardButton("ستايل 4", callback_data="styale_3")],
        [InlineKeyboardButton("ستايل 5", callback_data="styale_4"),
         InlineKeyboardButton("ستايل 6", callback_data="styale_5")],
        [InlineKeyboardButton("ستايل 7", callback_data="styale_6"),
         InlineKeyboardButton("ستايل 8", callback_data="styale_7")]
    ]

    styles_list = """اختر ستايل الوقت لبايو الجروب:
📋 قائمة الخطوط المتاحة:

1: ₀₁₂₃₄₅₆₇₈₉  
2: 𝟎𝟏𝟐𝟓  
3: 𝟬𝟭𝟮𝟲  
4: ⓪①②③④⑤⑥⑦⑧⑨  
5: ⓿❶❷❸❹❺❻❼❽❾  
6: 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡  
7: ０１２٦７٨９  
8: 𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"""

    await message.reply(styles_list, reply_markup=InlineKeyboardMarkup(buttons))


@app.on_callback_query(filters.regex(r"styale_\d"))
async def style_selected(client, callback_query):
    global chosean_style, originl_bio

    chosean_style = int(callback_query.data.split("_")[1])
    group_info = await client.get_chat(callback_query.message.chat.id)
    originl_bio = group_info.description
    group_data[callback_query.message.chat.id] = {
        "bio_enabled": True,
        "style": chosean_style
    }
    await callback_query.message.delete()
    await callback_query.message.reply("تم اختيار ستايل الوقت ✅\nجارٍ تفعيل بايو الجروب الوقتي...")
    asyncio.create_task(update_group_bio_loop(client, callback_query.message.chat.id))


async def update_group_bio_loop(client, chat_id):
    last_time = ""
    while True:
        try:
            time_str = datetime.now(pytz.timezone("Africa/Cairo")).strftime('%I:%M')
            if time_str != last_time:
                last_time = time_str
                formatted_time = formaat_time(time_str, group_data[chat_id]["style"])
                new_bio = f"{originl_bio} {formatted_time}"
                await client.set_chat_description(chat_id, new_bio)
            await asyncio.sleep(20)
        except Exception as e:
            print(f"[Error] أثناء تحديث البايو: {e}")
            await asyncio.sleep(30)


@app.on_message(filters.command(["تعطيل بايو وقتي"], "") & filters.group, group=1354)
async def disable_group_bio_time(client, message):
    if message.chat.id in group_data and group_data[message.chat.id]["bio_enabled"]:
        del group_data[message.chat.id]
        await client.set_chat_description(message.chat.id, originl_bio)
        await message.reply("تم تعطيل بايو الجروب الوقتي وإرجاع البايو الأصلي.")
    else:
        await message.reply("بايو الجروب الوقتي غير مفعل لهذا الجروب.")





############################################# الالعاب ##################################################
src = []

@app.on_message(filters.command(["قفل التسليه","تعطيل التسليه"], "") & filters.group, group=258073) 
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

@app.on_message(filters.command(["فتح التسليه","تفعيل التسليه"], "") & filters.group, group=7479003) 
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

with open("/root/hamo/questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

user_asked_questions = {}

@app.on_message(filters.command(["اسالني","اسالني","سؤال","اساله","اسألني"], "") & filters.group, group=565653)
async def ask_question(client, message):
    user_id = message.from_user.id if message.from_user else "None"

    if user_id not in user_asked_questions:
        user_asked_questions[user_id] = []

    remaining_questions = [q for q in questions if q["question"] not in user_asked_questions[user_id]]

    if not remaining_questions:
        await message.reply("لقد أجبت على جميع الأسئلة! 🎉")
        return

    question = random.choice(remaining_questions)
    user_asked_questions[user_id].append(question["question"])

    keyboard = []
    for i in range(0, len(question["options"]), 2):
        row = []
        if i < len(question["options"]):
            row.append(InlineKeyboardButton(question["options"][i], callback_data=f"ans_{i}_{user_id}"))
        if i + 1 < len(question["options"]):
            row.append(InlineKeyboardButton(question["options"][i + 1], callback_data=f"ans_{i+1}_{user_id}"))
        keyboard.append(row)

    await message.reply(
        f"**{question['question']}**",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

@app.on_callback_query(filters.regex(r"^ans_\d+_\d+$"))
async def handle_answer(client, callback_query: CallbackQuery):
    data = callback_query.data.split("_")
    answer_index = int(data[1])
    allowed_user_id = int(data[2])
    user_id = callback_query.from_user.id

    if user_id != allowed_user_id:
        await callback_query.answer("هذا السؤال ليس موجهًا لك 🚧", show_alert=True)
        return

    question_text = callback_query.message.text.strip()

    for q in questions:
        if q["question"] == question_text:
            correct_index = q["correct"]
            correct_answer = q["options"][correct_index]
            if answer_index == correct_index:
                points[user_id] = points.get(user_id, 0) + 5
                result = f"**◍ إجابة صحيحة ✅ \n◍ تم إضافة 5 نقاط🔹**"
            else:
                result = f"**◍ إجابة خاطئة ❌\n◍ الاجابة الصحيحة: {correct_answer} ✔️**"

            await callback_query.message.edit_text(result)
            await callback_query.answer()
            break

users_db = {}


@app.on_message(filters.command(["صفحه"], "") & filters.group, group=4565448)
async def send_qurane(client, message):
    try:
        match = re.search(r"صفحه?\s+(\d+)", message.text)
        if not match:
            return await message.reply("❌ أرسل الأمر بهذا الشكل:\n/صفحة 110")
        page_num = int(match.group(1))

        if 1 <= page_num <= 604:
            formatted_page = str(page_num).zfill(3)  # تحويل الرقم إلى ثلاث خانات
            image_url = f"https://e-quran.com/pic/p{formatted_page}.jpg"
            await message.reply_photo(
                photo=image_url,
                caption=f"📖 صفحة رقم {page_num} من المصحف الشريف"
            )
        else:
            await message.reply("❌ رقم الصفحة يجب أن يكون بين 1 و 604.")
    except Exception as e:
        await message.reply("❌ حدث خطأ أثناء جلب الصفحة.")

@app.on_message(filters.command(["صفحة"], "") & filters.group, group=45451548)
async def send_quran_page(client, message):
    try:
        match = re.search(r"صفحة?\s+(\d+)", message.text)
        if not match:
            return await message.reply("❌ أرسل الأمر بهذا الشكل:\n/صفحة 110")
        page_num = int(match.group(1))

        if 1 <= page_num <= 604:
            formatted_page = str(page_num).zfill(3)  # تحويل الرقم إلى ثلاث خانات
            image_url = f"https://e-quran.com/pic/p{formatted_page}.jpg"
            await message.reply_photo(
                photo=image_url,
                caption=f"📖 صفحة رقم {page_num} من المصحف الشريف"
            )
        else:
            await message.reply("❌ رقم الصفحة يجب أن يكون بين 1 و 604.")
    except Exception as e:
        await message.reply("❌ حدث خطأ أثناء جلب الصفحة.")
        print(e)



@app.on_message(filters.command(["زوجني", "ز"], "") & filters.group, group=534653435)
async def marriage_offer(client: Client, message: Message):
    proposer = message.from_user
    proposer_id = proposer.id

    if message.reply_to_message and message.reply_to_message.from_user:
        target_user = message.reply_to_message.from_user
    else:
        try:
            members = []
            async for member in client.get_chat_members(message.chat.id, limit=500):
                if not member.user.is_bot and member.user.id != proposer_id:
                    members.append(member.user)
            if not members:
                return await message.reply("**مافيش حد أزوّجك له في الجروب 😅**")
            target_user = random.choice(members)
        except Exception as e:
            return await message.reply("**حدث خطأ أثناء اختيار العريس/العروسة 😅**")
    target_id = target_user.id
    if proposer_id in users_db:
        spouse_id = users_db[proposer_id]
        spouse_user = await client.get_users(spouse_id)
        return await message.reply(f"**الحقي جوزك بيجوز عليكي {spouse_user.mention} 😅**")
    
    if target_id in users_db:
        spouse_id = users_db[target_id]
        spouse_user = await client.get_users(spouse_id)
        return await message.reply(f"**◍ الشخص الذي اخترته متزوج بالفعل\n◍ من {spouse_user.mention}!**")
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("قبول", callback_data=f"accept_{proposer_id}_{target_id}"),
            InlineKeyboardButton("رفض", callback_data=f"reject_{proposer_id}_{target_id}")
        ]
    ])

    await message.reply(
        f"**◍ لديك طلب زواج من {proposer.mention}\n◍ هل توافق {target_user.mention}؟**",
        reply_markup=keyboard
    )

@app.on_callback_query(filters.regex(r"^(accept|reject)_(\d+)_(\d+)$"))
async def marriage_response(client: Client, callback_query):
    action, proposer_id, target_id = callback_query.data.split("_")
    proposer_id = int(proposer_id)
    target_id = int(target_id)

    if callback_query.from_user.id != target_id:
        await callback_query.answer("لا يمكنك الرد على هذا الطلب.", show_alert=True)
        return

    if action == "accept":
        users_db[proposer_id] = target_id
        users_db[target_id] = proposer_id
        await callback_query.answer("تم قبول الزواج!")
        await callback_query.edit_message_text("تم قبول الزواج بنجاح ❤️")
    else:
        await callback_query.answer("تم رفض الزواج.")
        await callback_query.edit_message_text("تم رفض طلب الزواج.")

@app.on_message(filters.command(["طلاق"], "") & filters.group, group=18005655435)
async def divorce(client: Client, message: Message):
    user_id = message.from_user.id if message.from_user else "None"
    spouse_id = users_db.get(user_id)
    if not spouse_id:
        return await message.reply("**اتنيل انت سنجل اصلا**")
    del users_db[user_id]
    del users_db[spouse_id]
    await message.reply("**تم الطلاق بنجاح**")

@app.on_message(filters.command(["زوجتي"], "") & filters.group, group=18005054)
async def show_wife(client: Client, message: Message):
    user_id = message.from_user.id if message.from_user else "None"
    spouse_id = users_db.get(user_id)
    if spouse_id:
        spouse = await client.get_users(spouse_id)
        await message.reply(f"**◍ زوجتك القمر هي: {spouse.mention}**")
    else:
        await message.reply("**اتنيل انت سنجل اصلا**")

@app.on_message(filters.command(["زوجي"], "") & filters.group, group=180055764)
async def show_husband(client: Client, message: Message):
    user_id = message.from_user.id if message.from_user else "None"
    spouse_id = users_db.get(user_id)
    if spouse_id:
        spouse = await client.get_users(spouse_id)
        await message.reply(f"زوجك هو: {spouse.mention}")
    else:
        await message.reply("**اتنيلي انتي سنجل اصلا**")

@app.on_message(filters.command(["المتزوجين","المتجوزين","المرتبطين"], "") & filters.group, group=1234567890)
async def list_married(client: Client, message: Message):
    couples = set()
    checked = set()
    for user, spouse in users_db.items():
        if user in checked or spouse in checked:
            continue
        couple = tuple(sorted((user, spouse)))
        couples.add(couple)
        checked.add(user)
        checked.add(spouse)
    if not couples:
        return await message.reply("**مقيش حد مجوز كلهم سناجل**")
    text = "قائمة المتزوجين:\n"
    for u1, u2 in couples:
        user1 = await client.get_users(u1)
        user2 = await client.get_users(u2)
        text += f"- {user1.mention} ❤️ {user2.mention}\n"
    await message.reply(text)

with open("/root/hamo/words.json", "r", encoding="utf-8") as f:
        words_list = json.load(f)

current_word_game = {}
used_words = {}
waiting_for_answer = {}

@app.on_message(filters.text & filters.group, group=156451455)
async def check_word_answer(client: Client, message: Message):
    user_id = message.from_user.id if message.from_user else "None"
    if message.text.startswith(("/", "ركب", "تجميع", "حروف", "فكك")):
        return
    if user_id in current_word_game:
        if message.text.strip() == current_word_game[user_id]:
            points[user_id] = points.get(user_id, 0) + 5
            await message.reply(f"**◍ إجابة صحيحة ✅ \n◍ تم إضافة 5 نقاط🔹**")
            del current_word_game[user_id]
        else:
            await message.reply(f"**◍ إجابة خاطئة ❌\n◍ الاجابة الصحيحة: {current_word_game[user_id]} ✔️**")
            del current_word_game[user_id]

@app.on_message(filters.command(["فكك", "تجميع", "حروف","رتب"], "") & filters.group, group=55453146)
async def worssd_game(client: Client, message: Message):
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in current_word_game:
        del current_word_game[user_id]

    if user_id not in used_words:
        used_words[user_id] = []

    remaining_words = [w for w in words_list if w not in used_words[user_id]]
    if not remaining_words:
        await message.reply("**✅ لقد أكملت كل الكلمات! 🎉**")
        return
    
    word = random.choice(remaining_words)
    used_words[user_id].append(word)

    shuffled = ''.join(random.sample(word, len(word)))
    while shuffled == word:
        shuffled = ''.join(random.sample(word, len(word)))

    current_word_game[user_id] = word
    await message.reply(
        f"**🧩 رتب الحروف لتكوين الكلمة:\n↢ ( {' '.join(shuffled)} )\n\nأرسل الكلمة الآن 📩**",
        quote=True
    )

character_guess = {}
user_guess_stage = {}
used_characters = {}

with open("/root/hamo/characters.json", "r", encoding="utf-8") as f:
        characters = json.load(f)

# @app.on_message(filters.command(["شخصية", "شخصيه"], "") & filters.group, group=15314153)
# async def start_character_guess(client, message):
#     user_id = message.from_user.id if message.from_user else "None"

#     if user_id not in used_characters:
#         used_characters[user_id] = []

#     remaining = [c for c in characters if c["name"] not in used_characters[user_id]]
#     if not remaining:
#         await message.reply("**✅ لقد خمنت كل الشخصيات المتاحة! 🎉**")
#         return

#     ch = random.choice(remaining)
#     used_characters[user_id].append(ch["name"])
#     character_guess[user_id] = ch
#     user_guess_stage[user_id] = 0

#     hint = ch["hints"][0]
#     keyboard = InlineKeyboardMarkup(
#         [[InlineKeyboardButton("🔁 تلميح آخر", callback_data=f"hint_{user_id}")]]
#     )
#     msg = await message.reply(
#         f"**🕵️‍♂️ من هو الشخصية؟\n🔎 التلميح الأول: {hint}**",
#         reply_markup=keyboard
#     )
#     character_guess[user_id]["chat_id"] = msg.chat.id
#     character_guess[user_id]["message_id"] = msg.id


# @app.on_message(filters.text & filters.group, group=531352132)
# async def handle_character_guess(client, message):
#     user_id = message.from_user.id if message.from_user else "None"
#     if message.text.startswith(("شخصية", "شخصيه")):
#         return
#     if user_id in character_guess:
#         user_input = message.text.strip().lower().replace("ى", "ي")
#         answers = character_guess[user_id].get("answers", [character_guess[user_id]["name"]])
#         normalized_answers = [ans.strip().lower().replace("ى", "ي") for ans in answers]

#         if user_input in normalized_answers:
#             points[user_id] = points.get(user_id, 0) + 5
#             await message.reply("**◍ إجابة صحيحة ✅ \n◍ تم إضافة 5 نقاط🔹**")
#             del character_guess[user_id]
#             del user_guess_stage[user_id]
#         else:
#             await message.reply("**❌ خطأ. جرب مرة أخرى أو اضغط زر تلميح آخر**")


# @app.on_callback_query(filters.regex(r"^hint_(\d+)$"))
# async def send_next_hint(client, callback_query: CallbackQuery):
#     target_user_id = int(callback_query.data.split("_")[1])
#     user_id = callback_query.from_user.id

#     if user_id != target_user_id:
#         await callback_query.answer("❌ هذا التلميح ليس لك!", show_alert=True)
#         return

#     if user_id not in character_guess:
#         await callback_query.answer("❌ لا يوجد سؤال نشط لك.", show_alert=True)
#         return

#     stage = user_guess_stage[user_id]
#     hints = character_guess[user_id]["hints"]

#     if stage + 1 < len(hints):
#         user_guess_stage[user_id] += 1
#         next_hint = hints[stage + 1]
#         new_text = f"**🕵️‍♂️ من هو الشخصية؟\n🔎 التلميح {stage + 2}: {next_hint}**"
#         try:
#             await callback_query.message.edit_text(new_text, reply_markup=callback_query.message.reply_markup)
#         except:
#             pass
#         await callback_query.answer()
#     else:
#         answer = character_guess[user_id].get("name", "غير معروف")
#         try:
#             await callback_query.message.edit_text(f"**❌ انتهت التلميحات.\nالشخصية كانت: {answer}**")
#         except:
#             pass
#         del character_guess[user_id]
#         del user_guess_stage[user_id]
#         await callback_query.answer()

current_facts = {}
used_facts = {}
facts = [
    {"text": "عدد كواكب المجموعة الشمسية هو 8؟", "correct": True},
    {"text": "الفيل هو أسرع حيوان بري؟", "correct": False},
    {"text": "اللغة العربية تحتوي على 28 حرفًا؟", "correct": True},
    {"text": "نيويورك هي عاصمة الولايات المتحدة؟", "correct": False},
    {"text": "الصحراء الكبرى هي أكبر صحراء في العالم؟", "correct": True},
    {"text": "الأوكسجين هو أكثر العناصر وفرة في القشرة الأرضية؟", "correct": False},
    {"text": "طوكيو هي عاصمة اليابان؟", "correct": True},
    {"text": "الحوت الأزرق هو أكبر حيوان على الأرض؟", "correct": True},
    {"text": "النملة تستطيع حمل 50 ضعف وزنها؟", "correct": True},
    {"text": "القارة القطبية الجنوبية ليس بها أي دول؟", "correct": True},
    {"text": "الذهب هو أفضل موصل للكهرباء؟", "correct": False},
    {"text": "أستراليا هي أكبر جزيرة في العالم؟", "correct": False},
    {"text": "الخليفة عمر بن الخطاب هو أول من جمع القرآن؟", "correct": False},
    {"text": "الزهرة هو الكوكب الأقرب إلى الشمس؟", "correct": False},
    {"text": "الأسد يعتبر من فصيلة القطط؟", "correct": True},
    {"text": "نهر النيل هو أطول نهر في العالم؟", "correct": True},
    {"text": "الضوء ينتقل أسرع من الصوت؟", "correct": True},
    {"text": "الخلايا العصبية تتجدد في جسم الإنسان؟", "correct": False},
    {"text": "الفلبين تتكون من أكثر من 7000 جزيرة؟", "correct": True},
    {"text": "القهوة هي المشروب الأكثر استهلاكًا بعد الماء؟", "correct": False},
    {"text": "جبل كليمنجارو يقع في سويسرا؟", "correct": False},
    {"text": "التمساح يبكي عندما يأكل فريسته؟", "correct": True},
    {"text": "الإنترنت اخترع في القرن العشرين؟", "correct": True},
    {"text": "الخيار يعتبر من الفواكه علميًا؟", "correct": True},
    {"text": "ألبرت أينشتاين حصل على جائزة نوبل في الفيزياء؟", "correct": True},
    {"text": "القلب البشري يحتوي على 4 حجرات؟", "correct": True},
    {"text": "البرازيل هي أكبر منتج للبن في العالم؟", "correct": True},
    {"text": "الفراعنة اعتقدوا أن الأرض مسطحة؟", "correct": False},
    {"text": "الليمور يعيش فقط في مدغشقر؟", "correct": True},
    {"text": "الزجاج مصنوع من الرمال؟", "correct": True},
    {"text": "النسر هو أطول الطيور عمرًا؟", "correct": True},
    {"text": "الهند لديها أكبر عدد من سكان في العالم؟", "correct": False},
    {"text": "الدماغ البشري يستخدم 10% فقط من قدرته؟", "correct": False},
    {"text": "القهوة تحتوي على مادة الكافيين أكثر من الشاي؟", "correct": True},
    {"text": "القطط لديها 5 أصابع في الأقدام الأمامية؟", "correct": False},
    {"text": "أول رجل وصل إلى القمر كان نيل أرمسترونج؟", "correct": True},
    {"text": "الزرافة لديها نفس عدد الفقرات العنقية مثل الإنسان؟", "correct": True},
    {"text": "الزئبق هو المعدن السائل الوحيد في درجة حرارة الغرفة؟", "correct": True},
    {"text": "اللون الأحمر يزيد من عدوانية الثيران؟", "correct": False},
    {"text": "الخضراوات المجمدة تفقد قيمتها الغذائية؟", "correct": False},
    {"text": "الضوء الأزرق يساعد على النوم؟", "correct": False},
    {"text": "القرش الأبيض الكبير من الحيوانات المهددة بالانقراض؟", "correct": True},
    {"text": "الفراشات تتذوق بأرجلها؟", "correct": True},
    {"text": "الصين هي أقدم حضارة مستمرة في العالم؟", "correct": True},
    {"text": "الليمون يحتوي على فيتامين سي أكثر من البرتقال؟", "correct": True},
    {"text": "الخلايا الدهنية في جسم الإنسان لا تنقسم؟", "correct": False},
    {"text": "الأسماك تشعر بالعطش؟", "correct": False},
    {"text": "الذهب الأبيض هو خليط من الذهب والنيكل؟", "correct": True},
    {"text": "النساء يتنفسن أسرع من الرجال؟", "correct": True},
    {"text": "القطط لا تميز الألوان؟", "correct": False},
    {"text": "الخليفة أبو بكر الصديق هو أول من دون الحديث النبوي؟", "correct": False},
    {"text": "الضوضاء تسبب ارتفاع ضغط الدم؟", "correct": True},
    {"text": "القرش الحوت هو أكبر أنواع الأسماك؟", "correct": True},
    {"text": "البرق أشد حرارة من سطح الشمس؟", "correct": True},
    {"text": "الخنزير لا يستطيع النظر إلى السماء؟", "correct": True},
    {"text": "النسر الأصلع ليس أصلعًا في الحقيقة؟", "correct": True},
    {"text": "القهوة تسبب الجفاف للجسم؟", "correct": False},
    {"text": "الزهور تنمو أسرع عند سماع الموسيقى؟", "correct": False},
    {"text": "الخلايا السرطانية تموت في البيئة القلوية؟", "correct": False},
    {"text": "الذهب لا يصدأ؟", "correct": True},
    {"text": "النساء يرمشن أبطأ من الرجال؟", "correct": False},
    {"text": "القطط المنزلية تنحدر من النمر؟", "correct": False},
    {"text": "الخس يحتوي على نسبة عالية من البروتين؟", "correct": False},
    {"text": "الضوء الأزرق يجذب البعوض؟", "correct": True},
    {"text": "القرنبيط والبروكلي من نفس النوع النباتي؟", "correct": True},
    {"text": "النساء يرمشن بشكل أكثر دقة من الرجال؟", "correct": True},
    {"text": "القطط تتعرق من خلال كفوفها؟", "correct": True},
    {"text": "الخليفة عثمان بن عفان جمع القرآن في مصحف واحد؟", "correct": True},
    {"text": "الضوء الأخضر يساعد على التركيز؟", "correct": True},
    {"text": "القرش يستطيع شم رائحة الدم من مسافة بعيدة؟", "correct": True},
    {"text": "البرتقال كان لونه أخضر في الأصل؟", "correct": True},
    {"text": "الخلايا العصبية لا تتجدد؟", "correct": False},
    {"text": "الذهب يستخدم في علاج بعض الأمراض؟", "correct": True},
    {"text": "النساء يتعلمن اللغات أسرع من الرجال؟", "correct": True},
    {"text": "القطط تحب الحلويات؟", "correct": False},
    {"text": "الخضراوات الطازجة أفضل دائمًا من المجمدة؟", "correct": False},
    {"text": "الضوء الأصفر يقلل من حوادث السير؟", "correct": True},
    {"text": "القرش يموت إذا توقف عن الحركة؟", "correct": True},
    {"text": "البرق يضرب نفس المكان مرتين؟", "correct": True},
    {"text": "الخنزير من الحيوانات النظيفة؟", "correct": True},
    {"text": "النسر يعيش حتى 70 سنة؟", "correct": True},
    {"text": "القهوة تساعد على حرق الدهون؟", "correct": True},
    {"text": "الزهور البيضاء أكثرها عطرًا؟", "correct": True},
    {"text": "الخلايا السرطانية لا تستخدم الأكسجين؟", "correct": False},
    {"text": "الذهب عنصر نادر في الكون؟", "correct": True},
    {"text": "النساء أكثر عرضة لارتفاع ضغط الدم من الرجال؟", "correct": False},
    {"text": "القطط تستخدم شواربها للتوازن؟", "correct": True},
    {"text": "الخس مهدئ طبيعي؟", "correct": True},
    {"text": "الضوء الأحمر هو الأسرع انتشارًا؟", "correct": False},
    {"text": "القرنبيط يمكن أن يكون أرجوانيًا؟", "correct": True},
    {"text": "النساء أكثر عرضة للإصابة بمرض الزهايمر؟", "correct": True},
    {"text": "القطط ترى في الظلام التام؟", "correct": False},
    {"text": "الخليفة علي بن أبي طالب قتل بالسم؟", "correct": False},
    {"text": "الضوء الأزرق يقلل من إنتاج الميلاتونين؟", "correct": True},
    {"text": "القرش يلد أم يبيض؟", "correct": "يختلف حسب النوع"},
    {"text": "البرتقالي لون يحفز الشهية؟", "correct": True},
    {"text": "الخلايا الجذعية يمكنها علاج الأمراض؟", "correct": True},
    {"text": "الذهب يستخدم في أجهزة الكمبيوتر؟", "correct": True},
    {"text": "النساء أكثر عرضة للاكتئاب من الرجال؟", "correct": True},
    {"text": "القطط تكره الماء؟", "correct": False},
    {"text": "الخضراوات الورقية غنية بالحديد؟", "correct": True},
    {"text": "الضوء الأخضر مهدئ للأعصاب؟", "correct": True},
    {"text": "القرش لا يصاب بالسرطان؟", "correct": False},
    {"text": "البرق يمكن أن يحدث بدون رعد؟", "correct": True},
    {"text": "الخنزير من أذكى الحيوانات؟", "correct": True},
    {"text": "النسر يرى من مسافة بعيدة جدًا؟", "correct": True},
    {"text": "القهوة تسبب هشاشة العظام؟", "correct": False},
    {"text": "الزهور الحمراء ترمز للحب؟", "correct": True},
    {"text": "الخلايا السرطانية تنقسم بلا توقف؟", "correct": True},
    {"text": "الذهب لا يتفاعل مع الأحماض؟", "correct": False},
    {"text": "النساء أكثر عرضة لأمراض المناعة الذاتية؟", "correct": True},
    {"text": "القطط تحب النعناع؟", "correct": False},
    {"text": "الخس مفيد لصحة العيون؟", "correct": True},
    {"text": "الضوء الأزرق يضر بالعين؟", "correct": True},
    {"text": "القرنبيط يمكن أكله نيئًا؟", "correct": True},
    {"text": "النساء أكثر تحملاً للألم من الرجال؟", "correct": True},
    {"text": "القطط لا تحب الروائح القوية؟", "correct": True},
    {"text": "الخليفة عمر بن الخطاب أسس التقويم الهجري؟", "correct": True},
    {"text": "الضوء الأحمر يستخدم في غرف العمليات؟", "correct": True},
    {"text": "القرش يشم رائحة الخوف؟", "correct": False},
    {"text": "البرتقالي لون الطاقة؟", "correct": True},
    {"text": "الخلايا الجذعية تأتي من الأجنة فقط؟", "correct": False},
    {"text": "الذهب معدن ناعم؟", "correct": True},
    {"text": "النساء أكثر عرضة للسكتة الدماغية؟", "correct": False},
    {"text": "القطط تحب أن تدلل بطنها؟", "correct": False},
    {"text": "الخضراوات المجمدة تفقد الفيتامينات؟", "correct": False},
    {"text": "الضوء الأصفر مهدئ؟", "correct": False},
    {"text": "القرش لا ينام أبدًا؟", "correct": False},
    {"text": "البرق يضرب أكثر في المناطق الاستوائية؟", "correct": True},
    {"text": "الخنزير لا يتعرق؟", "correct": True},
    {"text": "النسر يبني أعشاشه في الأماكن المرتفعة؟", "correct": True},
    {"text": "القهوة تسبب القرحة؟", "correct": False},
    {"text": "الزهور الصفراء ترمز للصداقة؟", "correct": True},
    {"text": "الخلايا السرطانية تنتشر عبر الدم؟", "correct": True},
    {"text": "الذهب لا يسبب الحساسية؟", "correct": True},
    {"text": "النساء أكثر عرضة لهشاشة العظام؟", "correct": True},
    {"text": "القطط تكره الروائح الحمضية؟", "correct": True},
    {"text": "الخس يساعد على الهضم؟", "correct": True},
    {"text": "الضوء الأزرق يزيد من إنتاجية العمل؟", "correct": True},
    {"text": "القرنبيط غني بفيتامين سي؟", "correct": True},
    {"text": "النساء أكثر عرضة لاضطرابات الأكل؟", "correct": True},
    {"text": "القطط تحب اللعب بالخيوط؟", "correct": True},
    {"text": "الخليفة أبو بكر الصديق دفن بجوار الرسول؟", "correct": True},
    {"text": "الضوء الأحمر يزيد من التوتر؟", "correct": False},
    {"text": "القرش الأبيض الكبير مهدد بالانقراض؟", "correct": True},
    {"text": "البرتقالي لون الإبداع؟", "correct": True},
    {"text": "الخلايا الجذعية تعالج السكري؟", "correct": True},
    {"text": "الذهب يستخدم في علاج الروماتيزم؟", "correct": True},
    {"text": "النساء أكثر عرضة للصداع النصفي؟", "correct": True},
    {"text": "القطط تحب الصناديق؟", "correct": True},
    {"text": "الخضراوات الورقية تقوي الذاكرة؟", "correct": True},
    {"text": "الضوء الأخضر يساعد على الاسترخاء؟", "correct": True},
    {"text": "القرش يهاجم البشر عمدًا؟", "correct": False},
    {"text": "البرق ينتج الأوزون؟", "correct": True},
    {"text": "الخنزير من أسرع الحيوانات نموًا؟", "correct": True},
    {"text": "النسر يطير على ارتفاعات عالية؟", "correct": True},
    {"text": "القهوة تسبب الإدمان؟", "correct": False},
    {"text": "الزهور الزرقاء نادرة في الطبيعة؟", "correct": True},
    {"text": "الخلايا السرطانية تستهلك الكثير من الطاقة؟", "correct": True},
    {"text": "الذهب معدن موصل جيد للحرارة؟", "correct": True},
    {"text": "النساء أكثر عرضة لالتهاب المفاصل؟", "correct": True},
    {"text": "القطط تكره الموز؟", "correct": True},
    {"text": "الخس يساعد على النوم؟", "correct": True},
    {"text": "الضوء الأزرق يضر بالنوم؟", "correct": True},
    {"text": "القرنبيط يمكن أن يكون برتقاليًا؟", "correct": True},
    {"text": "النساء أكثر عرضة للتوتر؟", "correct": True},
    {"text": "القطط تحب الاختباء؟", "correct": True},
    {"text": "الخليفة عمر بن الخطاب قتل وهو يصلي؟", "correct": True},
    {"text": "الضوء الأحمر يستخدم في الإضاءة الليلية؟", "correct": True},
    {"text": "القرش الحوت يتغذى على العوالق؟", "correct": True},
    {"text": "البرتقالي لون الحماس؟", "correct": True},
    {"text": "الخلايا الجذعية تعالج أمراض القلب؟", "correct": True},
    {"text": "الذهب لا يتأثر بالماء؟", "correct": True},
    {"text": "النساء أكثر عرضة للقلق؟", "correct": True},
    {"text": "القطط تحب النعناع البري؟", "correct": True},
    {"text": "الخضراوات المجمدة تحتوي على مغذيات؟", "correct": True},
    {"text": "الضوء الأصفر مريح للعين؟", "correct": True},
    {"text": "القرش يهاجم عند الشعور بالخطر؟", "correct": True},
    {"text": "البرق يحدث في الشتاء؟", "correct": False},
    {"text": "الخنزير من الحيوانات الاجتماعية؟", "correct": True},
    {"text": "النسر يبني أعشاشه كل عام؟", "correct": False},
    {"text": "القهوة تسبب الأرق؟", "correct": False},
    {"text": "الزهور البيضاء ترمز للسلام؟", "correct": True},
    {"text": "الخلايا السرطانية تنتشر عبر الجهاز الليمفاوي؟", "correct": True},
    {"text": "الذهب لا يتفاعل مع الأكسجين؟", "correct": True},
    {"text": "النساء أكثر عرضة لاضطرابات النوم؟", "correct": True},
    {"text": "القطط تحب الارتفاعات؟", "correct": True},
    {"text": "الخس مفيد للبشرة؟", "correct": True},
    {"text": "الضوء الأزرق يقلل من إنتاج الميلاتونين؟", "correct": True},
    {"text": "القرنبيط غني بالألياف؟", "correct": True},
    {"text": "النساء أكثر عرضة للاضطرابات النفسية؟", "correct": True},
    {"text": "الخليفة عثمان بن عفان قتل وهو يقرأ القرآن؟", "correct": True},
    {"text": "الضوء الأحمر يساعد على النوم؟", "correct": True},
    {"text": "القرش يستطيع كشف المجال الكهربائي؟", "correct": True},
    {"text": "البرتقالي لون الإثارة؟", "correct": True},
    {"text": "الخلايا الجذعية تعالج الشلل؟", "correct": True},
    {"text": "الذهب يستخدم في علاج السرطان؟", "correct": True},
    {"text": "النساء أكثر عرضة للصداع؟", "correct": True},
    {"text": "القطط تحب الأسماك؟", "correct": True},
    {"text": "الخضراوات الطازجة تفقد مغذياتها بسرعة؟", "correct": True},
    {"text": "الضوء الأخضر يساعد على التركيز؟", "correct": True},
    {"text": "القرش يهاجم عند رؤية الحركة؟", "correct": True},
    {"text": "البرق يحدث في الصيف أكثر؟", "correct": True},
    {"text": "الخنزير من الحيوانات النظيفة؟", "correct": True},
    {"text": "النسر يطير بسرعة عالية؟", "correct": True},
    {"text": "القهوة تسبب الجفاف؟", "correct": False},
    {"text": "الزهور الأرجوانية ترمز للروحانية؟", "correct": True},
    {"text": "الخلايا السرطانية تنمو بسرعة؟", "correct": True},
    {"text": "الذهب لا يتآكل؟", "correct": True},
    {"text": "النساء أكثر عرضة لآلام الظهر؟", "correct": True},
    {"text": "الخس يساعد على خفض الوزن؟", "correct": True},
    {"text": "الضوء الأزرق يضر بالبشرة؟", "correct": True},
    {"text": "القرنبيط يساعد على الهضم؟", "correct": True},
    {"text": "النساء أكثر عرضة لالتهاب المثانة؟", "correct": True},
    {"text": "الخليفة علي بن أبي طالب أول من أسلم من الصبيان؟", "correct": True},
    {"text": "الضوء الأحمر يقلل من الصداع؟", "correct": True},
    {"text": "القرش الحوت لديه أسنان؟", "correct": True},
    {"text": "البرتقالي لون الإبداع؟", "correct": True},
    {"text": "الخلايا الجذعية تعالج الحروق؟", "correct": True},
    {"text": "الذهب يستخدم في الإلكترونيات؟", "correct": True},
    {"text": "النساء أكثر عرضة لالتهاب المفاصل الروماتويدي؟", "correct": True},
    {"text": "القطط تحب الصيد؟", "correct": True},
    {"text": "الخضراوات الورقية تقوي المناعة؟", "correct": True},
    {"text": "الضوء الأخضر مهدئ للأعصاب؟", "correct": True},
    {"text": "القرش يهاجم عند الشعور بالجوع؟", "correct": True},
    {"text": "البرق يحدث في العواصف الرعدية؟", "correct": True},
    {"text": "الخنزير من الحيوانات الذكية؟", "correct": True},
    {"text": "النسر يرى الأشعة فوق البنفسجية؟", "correct": True},
    {"text": "القهوة تسبب السرطان؟", "correct": False},
    {"text": "الزهور الحمراء ترمز للشجاعة؟", "correct": True},
    {"text": "الخلايا السرطانية تنتشر عبر العظام؟", "correct": True},
    {"text": "الذهب لا يتفاعل مع الماء؟", "correct": True},
    {"text": "النساء أكثر عرضة لأمراض الغدة الدرقية؟", "correct": True},
    {"text": "القطط تحب اللعب؟", "correct": True},
    {"text": "الخس مفيد للقلب؟", "correct": True},
    {"text": "الضوء الأزرق يسبب إجهاد العين؟", "correct": True},
    {"text": "القرنبيط يساعد على خفض الكوليسترول؟", "correct": True},
    {"text": "النساء أكثر عرضة للربو؟", "correct": True},
    {"text": "القطط تحب النوم؟", "correct": True},
    {"text": "الخليفة عمر بن الخطاب أسس الديوان؟", "correct": True},
    {"text": "الضوء الأحمر يستخدم في العلاج؟", "correct": True},
    {"text": "القرش يهاجم عند رؤية الدم؟", "correct": True},
    {"text": "البرتقالي لون السعادة؟", "correct": True},
    {"text": "الخلايا الجذعية تعالج أمراض العيون؟", "correct": True},
    {"text": "الذهب لا يتأثر بالهواء؟", "correct": True},
    {"text": "النساء أكثر عرضة للالتهابات؟", "correct": True},
    {"text": "القطط تحب الحرارة؟", "correct": True},
    {"text": "الخضراوات المجمدة تحتفظ بفيتامين سي؟", "correct": True},
    {"text": "الضوء الأصفر مريح؟", "correct": True},
    {"text": "القرش يهاجم عند الشعور بالتهديد؟", "correct": True},
    {"text": "البرق يحدث في المناطق الجبلية؟", "correct": True},
    {"text": "الخنزير من الحيوانات المرحة؟", "correct": True},
    {"text": "النسر يطير لمسافات طويلة؟", "correct": True},
    {"text": "القهوة تسبب ارتفاع ضغط الدم؟", "correct": False},
    {"text": "الزهور الصفراء ترمز للتفاؤل؟", "correct": True},
    {"text": "الخلايا السرطانية تنتشر عبر الأعصاب؟", "correct": True},
    {"text": "الذهب لا يتفاعل مع القلويات؟", "correct": True},
    {"text": "النساء أكثر عرضة لأمراض المناعة؟", "correct": True},
    {"text": "القطط تحب الأماكن الضيقة؟", "correct": True},
    {"text": "الخس مفيد للهضم؟", "correct": True},
    {"text": "الضوء الأزرق يضر بالعين؟", "correct": True},
    {"text": "القرنبيط يساعد على إزالة السموم؟", "correct": True},
    {"text": "النساء أكثر عرضة للالتهاب الرئوي؟", "correct": True},
    {"text": "القطط تحب الاستكشاف؟", "correct": True},
    {"text": "الخليفة أبو بكر الصديق أول الخلفاء؟", "correct": True},
    {"text": "الضوء الأحمر يساعد على الاسترخاء؟", "correct": True},
    {"text": "القرش يهاجم عند الشعور بالضعف؟", "correct": True},
    {"text": "البرتقالي لون الإثارة؟", "correct": True},
    {"text": "الخلايا الجذعية تعالج الشلل الرعاش؟", "correct": True},
    {"text": "الذهب يستخدم في طب الأسنان؟", "correct": True},
    {"text": "النساء أكثر عرضة لأمراض الكلى؟", "correct": True},
    {"text": "القطط تحب المرتفعات؟", "correct": True},
    {"text": "الخضراوات الورقية تقوي العظام؟", "correct": True},
    {"text": "الضوء الأخضر يساعد على الشفاء؟", "correct": True},
    {"text": "القرش يهاجم عند رؤية الفريسة؟", "correct": True},
    {"text": "البرق يحدث في المناطق الحارة؟", "correct": True},
    {"text": "الخنزير من الحيوانات الودودة؟", "correct": True},
    {"text": "النسر يرى في الظلام؟", "correct": True},
    {"text": "القهوة تسبب الجفاف للبشرة؟", "correct": False},
    {"text": "الزهور الزرقاء ترمز للهدوء؟", "correct": True},
    {"text": "الخلايا السرطانية تنتشر عبر العضلات؟", "correct": True},
    {"text": "الذهب لا يتفاعل مع النيتروجين؟", "correct": True},
    {"text": "النساء أكثر عرضة لأمراض الكبد؟", "correct": False},
    {"text": "الخس مفيد للشعر؟", "correct": True},
    {"text": "الضوء الأزرق يسبب الأرق؟", "correct": True},
    {"text": "القرنبيط يساعد على خفض ضغط الدم؟", "correct": True},
    {"text": "النساء أكثر عرضة للالتهاب الكبدي؟", "correct": False},
    {"text": "القطط تحب الاختباء في الأماكن المغلقة؟", "correct": True},
    {"text": "الخليفة عمر بن الخطاب لقب بالفاروق؟", "correct": True},
    {"text": "الضوء الأحمر يساعد على التئام الجروح؟", "correct": True},
    {"text": "القرش يهاجم عند الشعور بالخوف؟", "correct": True},
    {"text": "البرتقالي لون الإبداع؟", "correct": True},
    {"text": "الخلايا الجذعية تعالج التصلب المتعدد؟", "correct": True},
    {"text": "الذهب يستخدم في علاج التهاب المفاصل؟", "correct": True},
    {"text": "النساء أكثر عرضة لأمراض الرئة؟", "correct": False},
    {"text": "القطط تحب اللعب بالكرات؟", "correct": True},
    {"text": "الخضراوات المجمدة تحتفظ بالمغذيات؟", "correct": True},
    {"text": "الضوء الأصفر مهدئ للأعصاب؟", "correct": True},
    {"text": "القرش يهاجم عند رؤية الحركة المفاجئة؟", "correct": True},
    {"text": "البرق يحدث في المناطق الرطبة؟", "correct": True},
    {"text": "الخنزير من الحيوانات الاجتماعية؟", "correct": True},
    {"text": "النسر يطير في التيارات الهوائية؟", "correct": True},
    {"text": "القهوة تسبب تسوس الأسنان؟", "correct": False},
    {"text": "الزهور البيضاء ترمز للنقاء؟", "correct": True},
    {"text": "الخلايا السرطانية تنتشر عبر الجلد؟", "correct": True},
    {"text": "الذهب لا يتفاعل مع الكلور؟", "correct": True},
    {"text": "النساء أكثر عرضة لأمراض القلب؟", "correct": False},
    {"text": "القطط تحب اللعب بالريش؟", "correct": True},
    {"text": "الخس مفيد للعظام؟", "correct": True},
    {"text": "الضوء الأزرق يضر بالجلد؟", "correct": True},
    {"text": "القرنبيط يساعد على الوقاية من السرطان؟", "correct": True},
    {"text": "النساء أكثر عرضة للالتهاب الرئوي؟", "correct": True},
    {"text": "القطط تحب النوم في الأماكن الدافئة؟", "correct": True},
    {"text": "الخليفة عثمان بن عفان جمع القرآن؟", "correct": True},
    {"text": "الضوء الأحمر يساعد على النوم؟", "correct": True},
    {"text": "القرش يهاجم عند رؤية الألوان الزاهية؟", "correct": False},
    {"text": "البرتقالي لون الإثارة؟", "correct": True},
    {"text": "الخلايا الجذعية تعالج السكتة الدماغية؟", "correct": True},
    {"text": "الذهب يستخدم في علاج السرطان؟", "correct": True},
    {"text": "النساء أكثر عرضة لأمراض العيون؟", "correct": True},
    {"text": "القطط تحب اللعب بالألعاب؟", "correct": True},
    {"text": "الخضراوات الورقية تقوي النظر؟", "correct": True},
    {"text": "الضوء الأخضر يساعد على التركيز؟", "correct": True},
    {"text": "القرش يهاجم عند رؤية الفريسة الضعيفة؟", "correct": True},
    {"text": "البرق يحدث في المناطق المفتوحة؟", "correct": True},
    {"text": "الخنزير من الحيوانات النظيفة؟", "correct": True},
    {"text": "النسر يرى من مسافة بعيدة؟", "correct": True},
    {"text": "القهوة تسبب الإجهاض؟", "correct": False},
    {"text": "الزهور الأرجوانية ترمز للغموض؟", "correct": True},
    {"text": "الخلايا السرطانية تنتشر عبر الدماغ؟", "correct": True},
    {"text": "الذهب لا يتفاعل مع الكبريت؟", "correct": True},
    {"text": "النساء أكثر عرضة لأمراض الجهاز الهضمي؟", "correct": True},
    {"text": "القطط تحب اللعب بالخيوط؟", "correct": True},
    {"text": "الخس مفيد للبشرة؟", "correct": True},
    {"text": "الضوء الأزرق يسبب الصداع؟", "correct": True},
    {"text": "القرنبيط يساعد على الهضم؟", "correct": True},
    {"text": "النساء أكثر عرضة للالتهاب المفصلي؟", "correct": True},
    {"text": "القطط تحب النوم في الشمس؟", "correct": True},
    {"text": "الخليفة علي بن أبي طالب رابع الخلفاء؟", "correct": True},
    {"text": "الضوء الأحمر يساعد على الاسترخاء؟", "correct": True},
    {"text": "القرش يهاجم عند رؤية الحركة السريعة؟", "correct": True},
    {"text": "البرتقالي لون الإبداع؟", "correct": True},
    {"text": "الخلايا الجذعية تعالج الشلل النصفي؟", "correct": True}
]

@app.on_message(filters.command("صح وغلط", "") & filters.group, group=15541345)
async def true_false_game(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    if user_id not in used_facts:
        used_facts[user_id] = []

    available_facts = [fact for fact in facts if fact["text"] not in used_facts[user_id]]
    
    if not available_facts:
        await message.reply("**✅ لقد أكملت جميع الأسئلة 🎉**")
        return

    fact = random.choice(available_facts)
    used_facts[user_id].append(fact["text"])
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("صح ✅", callback_data=f"tf_{message.from_user.id}_true"),
            InlineKeyboardButton("خطأ ❌", callback_data=f"tf_{message.from_user.id}_false")]
        ]
    )
    sent = await message.reply(
        f"**{fact['text']}**",
        reply_markup=keyboard
    )
    current_facts[message.from_user.id] = {
        "correct": fact["correct"],
        "message_id": sent.id,
        "chat_id": sent.chat.id,
        "text": fact["text"] 
    }

@app.on_callback_query(filters.regex("^tf_"))
async def answer_tf(client, callback_query):
    data = callback_query.data.split("_")
    owner_id = int(data[1])
    user_id = callback_query.from_user.id

    if user_id != owner_id:
        await callback_query.answer("**❌ هذا السؤال مخصص لصاحب الأمر فقط**", show_alert=True)
        return

    if owner_id not in current_facts:
        await callback_query.answer("⏳ أعد إرسال الأمر أولاً", show_alert=True)
        return

    chosen = data[2] == "true"
    fact_data = current_facts[owner_id]
    correct = fact_data["correct"]
    chat_id = fact_data["chat_id"]
    msg_id = fact_data["message_id"]
    question_text = fact_data["text"]

    if chosen == correct:
        points[user_id] = points.get(user_id, 0) + 5
        result_text = "**◍ إجابة صحيحة ✅ \n◍ تم إضافة 5 نقاط🔹**"
    else:
        answer = "صح ✅" if correct else "خطأ ❌"
        result_text = f"**◍ إجابة خاطئة ❌\n◍ الاجابة الصحيحة: {answer} ✔️**"

    await client.edit_message_text(
        chat_id=chat_id,
        message_id=msg_id,
        text=f"{result_text}"
    )
    del current_facts[owner_id]



redod = []
@app.on_message(filters.command(["تعطيل الردود", "قفل الردود"], "")& filters.group,group=19647770)
async def redodlock(client: Client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    if message.text.lower() in ["تعطيل الردود", "قفل الردود"]:
        if message.chat.id in redod:
            return await message.reply_text("**◍ هذا الأمر معطل من قبل 🔐\n√**")
        redod.append(message.chat.id)
        return await message.reply_text("**♪ تم تعطيل الردود بنجاح **")

@app.on_message(filters.command(["فتح الردود", "تفعيل الردود"], "")& filters.group,group=12540148)
async def redodopen(client: Client, message):
    user_id = message.from_user.id if message.from_user else "None"
    allowed = any([
        is_group_creator(message.chat.id, user_id),
        is_group_owner(message.chat.id, user_id),
        is_main_developer(user_id),
        is_sub_developer(user_id),
        user_id in [OWNER_ID, sourse_dev, zombie_id],
    ])

    if not allowed:
        return await message.reply_text("**◍ تحتاج إلى رتبة منشئ على الأقل لإستخدام الأمر\n√**")
    if message.text.lower() in ["تفعيل الردود", "فتح الردود"]:
        if not message.chat.id in redod:
            return await message.reply_text("**♪ الردود مفعل من قبل**")
        redod.remove(message.chat.id)
        return await message.reply_text("**♪ تم تفعيل الردود بنجاح**")
   

@app.on_message(filters.text & filters.group, group=154465)
async def handle_all(c, m):
    if m.chat.id in redod:
        return
    await allreply_for_bot(c, m)


async def txt1(m: Message, trigger: str, responses: list):
    if trigger == m.text.lower():
        await m.reply(f"**{random.choice(responses)}**")


async def allreply_for_bot(c: Client, m: Message):
    await txt1(m, "عندك كام سنه", ["لا قول انت الاول 😂❤️", "خمنااشر وانت 🙄", "بتعرف تعد لحد كام 🙄😂"])
    await txt1(m, "حبك", ["حبككك اكترر ❤️", "مسمعكش تقولي كده تانى 🙂", "ياهلا بالخوازيق 🥺❤️", "بكرهههههك 🙂🙂"])
    await txt1(m, "حصلخير", ["حصلخير اي هيجي منين الخير وانت هنا. 🙂😂"])
    await txt1(m, "حه", ["اي يستا جيت ع الجرح 🙂😂", "عيييييييييييب 🙄", "متنرفزوناش بقا اللاه 🙄"])
    await txt1(m, "خدو مني الفون", ["كلميني ع الواتس يمزه 😂❤️"])
    await txt1(m, "بابا", ["😂❤️ مين حبيب بابا انا مين روح بابا انا نينينيني "])
    await txt1(m, "ماما", ["ست الحبايب ياحبيه ياحبيبه 😌😂"])
    await txt1(m, "شتمني", ["ولا حاجه يقلبي بكرا يتزنق ويجي حقك من غير متقل ادبك 😂❤️ مصيبه ده "])
    await txt1(m, "يبرو", ["اي يقلب البرو في حد مزعلك انا هقوم بالواجب 😂❤️"])
    await txt1(m, "يسطا", ["قابلتك ع البسطه 😂❤"])
    await txt1(m, "فرحان", ["❤️ ربنا يتمم افراحك "])
    await txt1(m, "عيب", ["سيب الواد يلعب 😂😂"])
    await txt1(m, "يحب", ["🥺❤️ اي ياكبد الحب "])
    await txt1(m, "عامل اي", ["احسن منك 😌😂👌", "الحمدلله وانت 🥺❤️", "بخير طول مانت بخير 🥺❤️"])
    await txt1(m, "بعشقك", ["وه وه قدام الناس كده عيب 🙈❤️", "راعو ان فى ناس سناجل 🥺❤️", "بشعشك بكل تفاصيلك ❤️😂"])
    await txt1(m, "انت نرم", ["الله يرحم ابوك كان بيشرب الشربه بخرطوم الغساله😂🙂"])
    await txt1(m, "خد", ["لا يعم نا ماشي سلام 🌝😂"])
    await txt1(m, "الزعامه", ["الزعامه فوق وكسكلياه ضالابواه 💔😹"])
    await txt1(m, "فين الادمن", ["ايش بتريد منه🤔"])
    await txt1(m, "هاي", ["هاى ماى جايز❤️😉"])
    await txt1(m, "هلو", ["هلو باللى سرق قلبى 🤗🌟"])
    await txt1(m, "ماشى", ["ماشى رايح فين ❤️🥺", "خد الباب وراك 😂😂", "المركب اللى تودي 🙂😂"])
    await txt1(m, "غلس", ["اهو انت💔🥺"])
    await txt1(m, "بف", ["خدوني معاكم بف..🙄💔"])
    await txt1(m, "تع بف", ["خدوني معاكم بف..🙄💔"])
    await txt1(m, "انت مين", [" بتسال لي💨🌝"])
    await txt1(m, "احبك", ["احبككك اكترر ❤️", "مسمعكش تقولي كده تانى 🙂", "ياهلا بالخوازيق 🥺❤️", "بكرهههههك 🙂🙂"])
    await txt1(m, "اوف", ["لمين هاي ؟🌚🌙"])
    await txt1(m, "في اي", ["مافيش حاجه🙄"])
    await txt1(m, "نايمين", ["انا سهران😿😹"])
    await txt1(m, "كفايه كلام", ["اسكت انت😼👊"])
    await txt1(m, "هيي", ["يالا ياض من هنا😂💔"])
    await txt1(m, "انت فين", ["بارض الله الواسعه 😽😂"])
    await txt1(m, "هه", ["ضحكه مش سالكه 😳😂"])
    await txt1(m, "البوت عطلان", ["بطلو كدب بقي 🙄🙂"])
    await txt1(m, "البوت واقف", ["لا تكذب حبي🌞"])
    await txt1(m, "المدرسه", ["اذا بتجيب اسمها بطردك🌞✨"])
    await txt1(m, "شوف", [" اشوف اي 🌝🌝"])
    await txt1(m, "🙂", ["هنكد بقا اهو 😕"])
    await txt1(m, "🚶💔", ["تعالي اشكيلي ايش فيك🙁💔"])
    await txt1(m, "🙁", [" اشكيلي هموك ليش متضايق🙁💔"])
    await txt1(m, "😳", ["اوميقد😐😹"])
    await txt1(m, "😒", ["ايش بيك ؟😟"])
    await txt1(m, "تحبني", ["اممم افكر🙁😹", "زى اختي 🙂", "ياهلا بالخوازيق 🥺❤️", "بكرهههههك 🙂🙂"])
    await txt1(m, "بتحبني", ["اممم افكر🙁😹", "زى اختي 🙂", "ياهلا بالخوازيق 🥺❤️", "وهو القمر ميتحبش ؟؟ ❤️😂"])
    await txt1(m, "باي", ["ع فين لوين رايح وسايبنى🙁💔", "بايباي 🙂", "في رعايه الله 🥺❤️", "فى ستين داهيه 🙂🙂"])
    await txt1(m, "تعالي خاص", ["لو بنت هاجي غير كدة لا 🙄😂"])
    await txt1(m, "فرخه", ["خليها تبيض😂😂😂"])
    await txt1(m, "حاضر", ["حضرلك الخير ياارب ❤️", "شطووور 🙂", "اى الاحترام ده 🙄"])
    await txt1(m, "😐", ["مالك ي حبيبي 😔"])
    await txt1(m, "ار يو ريدى", ["بكوى القميص وجهزت اهو 🔥🥺😂"])
    await txt1(m, "وات", ["ازغط بط 😳😂"])
    await txt1(m, "ملكش دعوة", ["خدو واستعوى ❤️😂"])
    await txt1(m, "ملكش دعوه", ["خدو واستعوى ❤️😂"])
    await txt1(m, "انت مالك", ["مالى فى جيبى هه ❤️😂"])
    await txt1(m, "احسن", ["جتك لحسه 😂💃"])
    await txt1(m, "نعم", ["نعم الله عليك🙂"])
    await txt1(m, "نرتبط", ["مرتبط مع نفسي واحزاني ❤️😢"])
    await txt1(m, "بلوك", ["لما اللي منك يجرحك😢"])
    await txt1(m, "انا بكرهك", ["حبني بلييز 🥺"])
    await txt1(m, "بيبى", ["قلبى ياناس قلباااااى 😂❤️"])
    await txt1(m, "ها", ["هاا ياروحي"])
    await txt1(m, "فديت", ["فدااك ♥️"])
    await txt1(m, "محدش بيسال عليا", ["بنسأل عليك ياحلووو 🖤🔍"])
    await txt1(m, "شلونكم", ["تمام وانت يكيوت ؟ 💕"])
    await txt1(m, "كداب", ["انت اللى كدااب يحليتها ❤️😹"])
    await txt1(m, "عادي", ["فى المعادى هه😂😂"])
    await txt1(m, "عجبتك", ["اكييد اكتيير 😎"])
    await txt1(m, "حبيبي", ["اوه ياه 🌝😂"])
    await txt1(m, "بت", ["ليا اسم ياض يعره يمهزء نينينينني😹😎🏃🏻‍♀"])
    await txt1(m, "روحي", ["خلصتت روحكك يبعيد😹🚶🏻‍♀💔"])
    await txt1(m, "بوتي", ["قلب بوتكك من جواا 🥺♥️"])
    await txt1(m, "مش هتيجي", ["مش هرووووح 😹🏃🏻‍♀🏃🏻‍♀"])
    await txt1(m, "تف", ["اصفخص عليك منتن ءتفووووو😹👅"])
    await txt1(m, "وه", ["بسيفلاح يعره مسمعش صوتكك😹🤸🏻‍♀🙊"])
    await txt1(m, "وهه", ["بسيفلاح يعره مسمعش صوتكك😹🤸🏻‍♀🙊"])
    await txt1(m, "اي", ["جتك اوهه م سامع ولا ايي😹👻"])
    await txt1(m, "ايي", ["جتك اوهه م سامع ولا ايي😹👻"])
    await txt1(m, "طيب", ["فرح خالتك قريب😹💋💃🏻"])
    await txt1(m, "تيب", ["فرح خالتك قريب😹💋💃🏻"])
    await txt1(m, "خلاص", ["خلصتت روحكك يبعيد😹🚶🏻‍♀💔"])
    await txt1(m, "حصل", ["حصل حصوله 😹💜"])

############################################# الالعاب ##################################################
async def start_zombiebot():
    try:
        await app.start()
        await user.start()
        await zombiiee.start()
        await Call()
        asyncio.create_task(azan())
        await idle()
    except Exception as e:
        pass

loop = asyncio.get_event_loop()
loop.run_until_complete(start_zombiebot())