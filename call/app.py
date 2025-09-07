import json
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime, time, timedelta
from pyromod import listen 
from pyrogram.types import Message
import random 
import pyrogram
import asyncio
from pyrogram import Client, filters, idle
import re
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
import os
from pyrogram.types import Message
from pyrogram.types import CallbackQuery
from pyromod import listen
import os
import pyrogram
import asyncio
from pyrogram import Client as app
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
    UserAlreadyParticipant
)
from pyrogram import Client, filters
from pyrogram import Client as app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message
import asyncio
import random
import re
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls import PyTgCalls, StreamType
from pytgcalls import PyTgCalls


app = Client(
    "mbhfho",
    api_id=int("27960337"),
    api_hash="22f8e42e48422f83c9aabebba937d0f4",
    bot_token="8219473262:AAH2OV5azUDRcHVMKQBlsWtXWIsr6QyaquU", 
    )

API_ID = int("27960337")
API_HASH = "22f8e42e48422f83c9aabebba937d0f4"
DEVS = ["R_9_9_0"]

@app.on_message(filters.command(["/start"], "") & filters.private)
async def kep(client, message):
    if message.from_user.username not in DEVS:
        return

    kep = InlineKeyboardMarkup([
        [InlineKeyboardButton("اضف حساب 🎯", callback_data="add_account"),
         InlineKeyboardButton("حذف حساب 🗑️", callback_data="remove_account")],

        [InlineKeyboardButton("تنظيف الحسابات 🧹", callback_data="safe_clean_scan")],

        [InlineKeyboardButton("انضمام للكول 🎸", callback_data="invite_call"),
         InlineKeyboardButton("مغادره الكول 🚫", callback_data="leave_call")],

        [InlineKeyboardButton("رشق تفاعلات 👍", callback_data="likes_accs"),
         InlineKeyboardButton("رشق تفاعلات 👎", callback_data="dis_like")],
        
        [InlineKeyboardButton("رشق استفتاء 📊", callback_data="vote_poll"),
         InlineKeyboardButton("رشق تفاعل محدد 🙈", callback_data="spisifc_reaction")],

        [InlineKeyboardButton("انضمام للجروب ➕", callback_data="invite_accounts"),
         InlineKeyboardButton("مغادرة جروب 👋", callback_data="leave_accounts")],

        [InlineKeyboardButton("مغادره كل الجروبات 👋", callback_data="leave_all")],

        [InlineKeyboardButton("رفع مطور 🧑‍💻", callback_data="add_dev"),
         InlineKeyboardButton("تنزيل مطور ❌", callback_data="remove_dev")],

        [InlineKeyboardButton("رفع نسخة الجلسات 📤", callback_data="upload_sessions"),
         InlineKeyboardButton("جلب نسخة الجلسات 📂", callback_data="get_sessions")]
    ])
    await message.reply_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي │⎋ اليك كيب التحكم بالبوت", reply_markup=kep)



@app.on_callback_query(filters.regex("^leave_all$"))
async def leave_all_handler(client, callback_query):
    try:
        accounts = await load_accounts()
        if not accounts:
            await callback_query.message.edit_text("❌ لا توجد حسابات مسجلة!")
            return

        buttons = []
        for acc in accounts:
            acc_name = acc.get('name', 'غير معروف')
            acc_phone = acc.get('phone', 'غير معروف')
            btn_text = f"{acc_name} ({acc_phone})"
            buttons.append([InlineKeyboardButton(btn_text, callback_data=f"select_acc:{acc['phone']}")])

        buttons.append([InlineKeyboardButton('✅ كل الحسابات', callback_data="select_acc:all")])
        buttons.append([InlineKeyboardButton('❌ إلغاء', callback_data="cancel_leave")])

        await callback_query.message.edit_text(
            '⚠️ **اختر الحسابات التي تريد مغادرة المجموعات منها:**\n'
            'سيتم مغادرة جميع المجموعات والقنوات للحساب المحدد!',
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        await callback_query.answer()
    except Exception as e:
        await callback_query.answer(f"حدث خطأ: {e}", show_alert=True)

@app.on_callback_query(filters.regex(r"^select_acc:(.*)$"))
async def select_account(client, callback_query):
    try:
        selected_phone = callback_query.data.split(":")[1]
        accounts = await load_accounts()

        if selected_phone == "all":
            buttons = [
                [InlineKeyboardButton('✅ تأكيد مغادرة الكل', callback_data="confirm_leave:all")],
                [InlineKeyboardButton('❌ إلغاء', callback_data="cancel_leave")]
            ]
            await callback_query.message.edit_text(
                '⚠️ **هل أنت متأكد من مغادرة جميع المجموعات لكل الحسابات؟**\n'
                'هذه العملية لا يمكن التراجع عنها!',
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        else:
            selected_acc = next((acc for acc in accounts if acc['phone'] == selected_phone), None)
            if not selected_acc:
                await callback_query.message.edit_text("❌ الحساب المحدد غير موجود!")
                return
            buttons = [
                [InlineKeyboardButton(f'✅ تأكيد مغادرة {selected_acc["name"]}', callback_data=f'confirm_leave:{selected_phone}')],
                [InlineKeyboardButton('❌ إلغاء', callback_data="cancel_leave")]
            ]
            await callback_query.message.edit_text(
                f'⚠️ **هل أنت متأكد من مغادرة جميع المجموعات لحساب {selected_acc["name"]}؟**\n'
                'هذه العملية لا يمكن التراجع عنها!',
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        await callback_query.answer()
    except Exception as e:
        await callback_query.answer(f"حدث خطأ: {e}", show_alert=True)

from pyrogram.enums import ChatType

@app.on_callback_query(filters.regex(r"^confirm_leave:(.*)$"))
async def confirm_leave(client, callback_query):
    try:
        target_phone = callback_query.data.split(":")[1]
        accounts = await load_accounts()
        await callback_query.message.edit_text('⏳ جاري معالجة الطلب...')
        
        accounts_to_process = []
        if target_phone == 'all':
            accounts_to_process = accounts
        else:
            selected_acc = next((acc for acc in accounts if acc['phone'] == target_phone), None)
            if selected_acc:
                accounts_to_process = [selected_acc]

        if not accounts_to_process:
            await callback_query.message.edit_text("❌ لم يتم العثور على الحسابات المطلوبة!")
            return
        
        total_left = 0
        total_errors = 0
        account_results = []

        for account in accounts_to_process:
            acc_name = account.get('name', 'غير معروف')
            session_str = account.get('session', '')

            if not session_str:
                account_results.append(f'• حساب {acc_name}: لا توجد جلسة صالحة')
                continue

            try:
                # إنشاء عميل Pyrogram جديد لكل حساب باستخدام StringSession
                user_client = Client(
                    "::memory::",
                    api_id=API_ID,
                    api_hash=API_HASH,
                    session_string=session_str,
                    no_updates=True
                )
                await user_client.start()

                dialogs = []
                async for dialog in user_client.get_dialogs():
                    dialogs.append(dialog)

                groups = [d for d in dialogs if d.chat.type in {ChatType.GROUP, ChatType.SUPERGROUP, ChatType.CHANNEL}]
                total = len(groups)
                left_count = 0
                errors = 0

                progress_msg = await callback_query.message.reply_text(f'🔍 حساب {acc_name}: تم العثور على {total} مجموعة/قناة\n⏳ جاري المغادرة...')

                for dialog in groups:
                    try:
                        await user_client.leave_chat(dialog.chat.id)
                        left_count += 1
                        if left_count % 5 == 0 or left_count == total:
                            await progress_msg.edit_text(
                                f'⏳ حساب {acc_name}: جاري المغادرة...\n'
                                f'✅ تم مغادرة: {left_count}/{total}\n'
                                f'❌ فشل في: {errors}'
                            )
                        await asyncio.sleep(1)
                    except Exception:
                        errors += 1
                        continue

                account_results.append(f'• حساب {acc_name}: تم {left_count} | فشل {errors} | إجمالي {total}')
                total_left += left_count
                total_errors += errors
                await user_client.stop()
            except Exception as e:
                account_results.append(f'• حساب {acc_name}: خطأ - {str(e)}')
                continue

        result_text = '✅ **تم الانتهاء!**\n\n' + '\n'.join(account_results)
        result_text += f'\n\nالإجمالي: تم {total_left} | فشل {total_errors}'
        await callback_query.message.edit_text(result_text)
        await callback_query.answer()
    except Exception as e:
        await callback_query.answer(f"حدث خطأ أثناء التنفيذ: {e}", show_alert=True)

@app.on_callback_query(filters.regex("^cancel_leave$"))
async def cancel_leave(client, callback_query):
    await callback_query.message.edit_text('❌ تم إلغاء العملية.', reply_markup=None)
    await callback_query.answer()



async def validate_session(session_str):
    temp_client = None
    try:
        temp_client = Client(
            "::memory::",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session_str,
            no_updates=True
        )
        await temp_client.start()
        me = await temp_client.get_me()
        if not me:
            return "invalid"
        return "valid"
    except Exception as e:
        error_msg = str(e)
        if "This session is expired" in error_msg:
            return "invalid: expired"
        elif "AUTH_KEY_DUPLICATED" in error_msg:
            return "invalid: duplicated"
        elif "TimeoutError" in error_msg:
            return "timeout"
        elif "Cannot connect to host" in error_msg:
            return "error: connection failed"
        else:
            return f"error: {error_msg}"
    finally:
        if temp_client:
            try:
                await temp_client.stop()
            except:
                pass

invalid_accounts_cache = []

@app.on_callback_query(filters.regex("safe_clean_scan"))
async def clean_accounts_safely(client, callback_query: CallbackQuery):
    try:
        global invalid_accounts_cache
        accounts = await load_accounts()
        valid_accounts = []
        invalid_accounts = []

        progress_msg = await callback_query.message.reply("🔄 بدء الفحص الآمن للجلسات...")

        invalid_accounts_cache = []  # تهيئة الكاش

        for index, account in enumerate(accounts):
            try:
                status = await asyncio.wait_for(
                    validate_session(account['session']),
                    timeout=15
                )
                if status == "valid":
                    valid_accounts.append(account)
                else:
                    invalid_accounts.append(account)
                    invalid_accounts_cache.append(account)
            except:
                invalid_accounts.append(account)
                invalid_accounts_cache.append(account)

            if index % 10 == 0 or index == len(accounts) - 1:
                await progress_msg.edit_text(
                    f"🔍 جاري الفحص ({index+1}/{len(accounts)})\n"
                    f"✅ الصالحة: {len(valid_accounts)}\n"
                    f"❌ غير الصالحة: {len(invalid_accounts)}"
                )
            await asyncio.sleep(0.5)
        result_text = (
            f"📊 **نتائج الفحص**\n\n"
            f"• الحسابات المفحوصة: {len(accounts)}\n"
            f"• الحسابات الصالحة: {len(valid_accounts)}\n"
            f"• الحسابات غير الصالحة: {len(invalid_accounts)}\n\n"
        )
        if invalid_accounts:
            sample = "\n".join([f"• {acc.get('phone', 'Unknown')} ({acc.get('session_name', 'No name')})"
                                for acc in invalid_accounts[:5]])
            result_text += f"**عينة من الحسابات غير الصالحة:**\n{sample}\n"
            if len(invalid_accounts) > 5:
                result_text += f"و {len(invalid_accounts) - 5} أخرى...\n\n"
            result_text += "هل تريد حذف الحسابات غير الصالحة؟"
            buttons = [
                [InlineKeyboardButton("🗑️ حذف غير الصالحة", callback_data="confirm_delete_invalid")],
                [InlineKeyboardButton("🔙 الاحتفاظ بها", callback_data="back_to_main")]
            ]
        else:
            result_text += "لا توجد حسابات غير صالحة للحذف"
            buttons = [[InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="back_to_main")]]

        await progress_msg.edit_text(
            result_text,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    except Exception as e:
        await callback_query.message.reply(
            f"⚠️ حدث خطأ في العملية الرئيسية\n{str(e)}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")]])
        )

@app.on_callback_query(filters.regex("confirm_delete_invalid"))
async def delete_invalid_accounts(client, callback_query: CallbackQuery):
    global invalid_accounts_cache
    try:
        accounts = await load_accounts()
        valid_accounts = [acc for acc in accounts if acc not in invalid_accounts_cache]
        await save_accounts(valid_accounts)

        deleted_list = "\n".join([
            f"• {acc.get('phone', 'Unknown')} ({acc.get('session_name', 'No name')})"
            for acc in invalid_accounts_cache
        ])

        result_text = (
            f"🧹 **تم حذف الحسابات غير الصالحة**\n\n"
            f"• الحسابات المفحوصة: {len(accounts)}\n"
            f"• الحسابات الصالحة: {len(valid_accounts)}\n"
            f"• الحسابات المحذوفة: {len(invalid_accounts_cache)}\n\n"
            f"**قائمة الحسابات المحذوفة:**\n"
            f"{deleted_list}"
        )

        await callback_query.message.edit_text(
            result_text,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="back_to_main")]])
        )

    except Exception as e:
        await callback_query.message.edit_text(
            f"❌ فشل الحذف: {str(e)}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")]])
        )


@app.on_callback_query(filters.regex(r"^confirm_del_(.+)"))
async def execute_delete(client, callback_query):
    try:
        phone_to_delete = callback_query.data.split("_", 2)[2]
        accounts = await load_accounts()
        new_accounts = [acc for acc in accounts if acc['phone'] != phone_to_delete]

        if len(new_accounts) == len(accounts):
            await callback_query.answer("❌ الحساب غير موجود!", show_alert=True)
            return

        if await save_accounts(new_accounts):
            await callback_query.message.edit(
                "✅ **تم حذف الحساب بنجاح!**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")]
                ])
            )
        else:
            await callback_query.message.edit(
                "❌ فشل في حذف الحساب!",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")]
                ])
            )
    except Exception as e:
        await callback_query.message.edit(
            f"❌ حدث خطأ أثناء حذف الحساب:\n{e}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")]
            ])
        )


@app.on_callback_query(filters.regex("add_dev"))
async def add_dev_callback(client: Client, callback_query: CallbackQuery):
    user = callback_query.from_user
    if user.username not in DEVS:
        return await callback_query.answer("❌ هذا الزر للمطورين فقط.", show_alert=True)
    try:
        response = await client.ask(
            chat_id=user.id,
            text="📨 في انتظار إرسال يوزر المطور...",
            filters=filters.user(user.id),
            timeout=60
        )
        username = response.text.strip().lstrip("@")
        target_user = await client.get_users(username)
        if target_user.username in DEVS:
            return await response.reply("⚠️ هذا المستخدم مضاف مسبقًا كمطور.")
        DEVS.append(target_user.username)
        await response.reply(f"✅ تم رفع [{target_user.first_name}](tg://user?id={target_user.id}) كمطور بنجاح.")
    except asyncio.TimeoutError:
        await client.send_message(user.id, "❌ انتهى الوقت ولم يتم إرسال يوزر.")
    except Exception as e:
        await client.send_message(user.id, f"❌ حدث خطأ أثناء رفع المطور:\n{e}")

@app.on_callback_query(filters.regex("remove_dev"))
async def remove_dev_callback(client: Client, callback_query: CallbackQuery):
    user = callback_query.from_user
    if user.username not in DEVS:
        return await callback_query.answer("❌ هذا الزر للمطورين فقط.", show_alert=True)
    try:
        response = await client.ask(
            chat_id=user.id,
            text="📨 في انتظار إرسال يوزر المطور...",
            filters=filters.user(user.id),
            timeout=60
        )
        username = response.text.strip().lstrip("@")
        if username not in DEVS:
            return await response.reply("⚠️ هذا المستخدم ليس مضافًا كمطور.")
        DEVS.remove(username)
        await response.reply(f"✅ تم **تنزيل** @{username} من المطورين بنجاح.")
    except asyncio.TimeoutError:
        await client.send_message(user.id, "❌ انتهى الوقت ولم يتم إرسال يوزر.")
    except Exception as e:
        await client.send_message(user.id, f"❌ حدث خطأ أثناء تنزيل المطور:\n{e}")


@app.on_callback_query(filters.regex("vote_poll"))
async def vote_poll(client, callback_query: CallbackQuery):
    sessions = await load_sessions()
    ask_link = await client.ask(callback_query.message.chat.id, "📨 أرسل الآن رابط الاستفتاء (poll) من قناة أو مجموعة عامة:")
    link = ask_link.text.strip()

    if not link.startswith("https://t.me/") or "/" not in link:
        await ask_link.reply("❌ الرابط غير صحيح. يجب أن يكون بصيغة https://t.me/username/message_id أو t.me/c/...")
        return

   
    parts = link.replace("https://t.me/", "").split("/")
    chat_username = parts[0]
    msg_id = int(parts[1])
    ask_option = await client.ask(callback_query.message.chat.id, "🗳️ أرسل رقم الخيار الذي تريد التصويت له (مثلاً: 0 = أول خيار):")
    try:
        option_index = int(ask_option.text.strip())
    except:
        await ask_option.reply("❌ يجب إرسال رقم صحيح للخيار.")
        return

    await ask_option.reply(f"📡 جاري التصويت للخيار رقم {option_index} من الحسابات...")

    count = 0
    for session in sessions:
        user = Client(f"session_{session}", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            await user.vote_poll(chat_username, msg_id, [option_index])
            count += 1
            await asyncio.sleep(2)
        except Exception as e:
            pass
        finally:
            await user.stop()

    await callback_query.message.reply_text(
        f"✅ تم التصويت للخيار رقم {option_index} بنجاح من {count} حساب.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 عودة", callback_data="back_to_main")]
        ])
    )


@app.on_callback_query(filters.regex("spisifc_reaction"))
async def specific_reaction(client, callback_query: CallbackQuery):
    if callback_query.from_user.username not in DEVS:
        await callback_query.answer("❌ ليس لديك صلاحيات.", show_alert=True)
        return

    sessions = await load_sessions()

    ask_emoji = await client.ask(callback_query.message.chat.id, "**🎯 أرسل الآن التفاعل (إيموجي) الذي تريد رشه على الرسالة:**")
    reaction = ask_emoji.text.strip()

    if not reaction:
        await ask_emoji.reply("❌ لم يتم إرسال تفاعل صحيح.")
        return

    ask_link = await client.ask(callback_query.message.chat.id, "📨 أرسل الآن رابط الرسالة (من قناة أو مجموعة عامة):")
    link = ask_link.text.strip()

    if not link.startswith("https://t.me/") or "/" not in link:
        await ask_link.reply("❌ الرابط غير صحيح. يجب أن يكون بصيغة https://t.me/username/message_id أو t.me/c/...")
        return

    
    parts = link.replace("https://t.me/", "").split("/")
    chat_username = parts[0]
    msg_id = int(parts[1])
    await ask_link.reply(f"📡 جاري رشق التفاعل {reaction} من الحسابات...")

    count = 0
    for session in sessions:
        user = Client(f"session_{session}", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            await user.send_reaction(chat_username, msg_id, reaction)
            count += 1
            await asyncio.sleep(2)
        except Exception as e:
            pass
        finally:
            await user.stop()

    await callback_query.message.reply_text(
        f"✅ تم رشق التفاعل {reaction} بنجاح من {count} حساب.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 عودة", callback_data="back_to_main")]
        ])
    )


@app.on_callback_query(filters.regex("likes_accs"))
async def likes_accounts(client, callback_query: CallbackQuery):
    sessions = await load_sessions()
    msg = await client.ask(callback_query.message.chat.id, "**📨 أرسل الآن رابط الرسالة (من قناة أو مجموعة عامة):**")
    link = msg.text.strip()
    if not link.startswith("https://t.me/") or "/" not in link:
        await msg.reply("❌ الرابط غير صحيح. يجب أن يكون بصيغة https://t.me/username/message_id")
        return
    try:
        parts = link.replace("https://t.me/", "").split("/")
        chat_username = parts[0]
        msg_id = int(parts[1])
    except:
        await msg.reply("❌ تأكد من الرابط، يجب أن يحتوي على اسم المستخدم ورقم الرسالة.")
        return

    await msg.reply("**📡 جاري رشق التفاعلات من الحسابات...**")
    reactions = ["👍", "❤️", "🔥", "💘", "👏","🕊","💯","⚡️","🏆"]
    count = 0
    for session in sessions:
        user = Client(f"session_{session}", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            emoji = random.choice(reactions)
            await user.send_reaction(chat_username, msg_id, emoji)
            count += 1
            await asyncio.sleep(2)
        except Exception as e:
            pass
        finally:
            await user.stop()
    await callback_query.message.reply_text(f"✅ تم رشق التفاعلات بنجاح من {count} حساب.",
                                            reply_markup=InlineKeyboardMarkup([
                                                [InlineKeyboardButton("عودة", callback_data="back_to_main")]
                                            ]))
    
@app.on_callback_query(filters.regex("dis_like"))
async def dis_like(client, callback_query: CallbackQuery):
    sessions = await load_sessions()
    msg = await client.ask(callback_query.message.chat.id, "**📨 أرسل الآن رابط الرسالة (من قناة أو مجموعة عامة):**")
    link = msg.text.strip()
    if not link.startswith("https://t.me/") or "/" not in link:
        await msg.reply("❌ الرابط غير صحيح. يجب أن يكون بصيغة https://t.me/username/message_id")
        return
    try:
        parts = link.replace("https://t.me/", "").split("/")
        chat_username = parts[0]
        msg_id = int(parts[1])
    except:
        await msg.reply("❌ تأكد من الرابط، يجب أن يحتوي على اسم المستخدم ورقم الرسالة.")
        return

    await msg.reply("**📡 جاري رشق التفاعلات من الحسابات...**")
    reactions = ["👎", "💩", "😂","🍌","👎", "💩", "🤮", "😡", "🤬"]
    count = 0
    for session in sessions:
        user = Client(f"session_{session}", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            emoji = random.choice(reactions)
            await user.send_reaction(chat_username, msg_id, emoji)
            count += 1
            await asyncio.sleep(2)
        except Exception as e:
            pass
        finally:
            await user.stop()
    await callback_query.message.reply_text(f"✅ تم رشق التفاعلات بنجاح من {count} حساب.",
                                            reply_markup=InlineKeyboardMarkup([
                                                [InlineKeyboardButton("عودة", callback_data="back_to_main")]
                                            ]))

ACCOUNTS_FILE = "accounts.json"

async def load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return []
    try:
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

async def save_accounts(accounts):
    try:
        with open(ACCOUNTS_FILE, "w", encoding="utf-8") as f:
            json.dump(accounts, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error saving accounts: {e}")
        return False
    
async def load_sessions():
    try:
        if not os.path.exists("accounts.json"):
            return []
        with open("accounts.json", "r", encoding='utf-8') as f:
            data = json.load(f)
            return [account["session"] for account in data if "session" in account]
    except Exception as e:
        print(f"Error loading sessions: {e}")
        return None

@app.on_callback_query(filters.regex("add_account"))
async def add_account(client, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    chat_id = callback_query.message.chat.id
    if not callback_query.from_user.username in DEVS:
        return
    
    ask = await client.ask(
        callback_query.message.chat.id,
        "📝 **إضافة حساب جديد**\n\n"
        "يرجى إرسال جلسة الحساب (كود الجلسة)\n\n"
        "▪ تأكد من صحة الجلسة\n"
        "▪ لا تشارك هذا الكود مع أحد\n"
        "▪ للإلغاء اكتب /cancel\n\n"
        "⏳ لديك 5 دقائق لإتمام العملية",
        timeout=300
    )
    session = ask.text.strip()
    accounts = await load_accounts()
    if any(acc['session'] == session for acc in accounts):
        await client.send_message(chat_id, "⚠️ هذه الجلسة مضافة مسبقاً!")
        return
    user = Client("::memory::", api_id=API_ID, api_hash=API_HASH, session_string=session,no_updates=True)
    try:
        await user.start()
        me = await user.get_me()
        account_info = {
            "name": f"{me.first_name or ''} {me.last_name or ''}".strip(),
            "username": me.username or "",
            "phone": me.phone_number or "",
            "session": session
        }
        accounts.append(account_info)
        if await save_accounts(accounts):
            await client.send_message(
                chat_id,
                f"✅ **تمت إضافة الحساب بنجاح!**\n\n"
                f"👤 الاسم: {account_info['name']}\n"
                f"📞 الهاتف: {account_info['phone']}\n"
                f"🔗 اليوزر: @{account_info['username']}\n\n"
                "تم حفظ الجلسة وتفعيلها بنجاح"
            )
    except Exception as e:
        await client.send_message(callback_query.message.chat.id, f"⚠️ فشل تشغيل الجلسة:\n{e}")
        return
    finally:
        await user.stop()
    await client.send_message(callback_query.message.chat.id, "تم إضافة الحساب بنجاح")


@app.on_callback_query(filters.regex("remove_account"))
async def remove_account(client, callback_query):
    try:
        accounts = await load_accounts()
        if not accounts:
            await callback_query.message.edit("❌ لا توجد حسابات مسجلة لحذفها!")
            return

        buttons = []
        for acc in accounts:
            acc_name = acc.get('name', 'غير معروف')
            acc_phone = acc.get('phone', 'غير معروف')
            btn_text = f"{acc_name} ({acc_phone})"
            buttons.append([
                InlineKeyboardButton(btn_text, callback_data=f"del_acc_{acc_phone}")
            ])
        buttons.append([InlineKeyboardButton("❌ إلغاء", callback_data="back_to_main")])

        await callback_query.message.edit(
            "🗑️ **اختر الحساب الذي تريد حذفه:**",
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    except Exception as e:
        await callback_query.message.edit(f"❌ حدث خطأ أثناء تحضير قائمة الحسابات:\n{e}")


@app.on_callback_query(filters.regex(r"^del_acc_(.+)"))
async def confirm_delete(client, callback_query):
    try:
        phone_to_delete = callback_query.data.split("_", 2)[2]
        accounts = await load_accounts()
        account_to_delete = next((acc for acc in accounts if acc['phone'] == phone_to_delete), None)

        if not account_to_delete:
            await callback_query.answer("❌ الحساب غير موجود!", show_alert=True)
            return

        await callback_query.message.edit(
            f"⚠️ **تأكيد الحذف**\n\n"
            f"هل أنت متأكد من حذف الحساب التالي؟\n\n"
            f"👤 الاسم: {account_to_delete.get('name', 'غير معروف')}\n"
            f"📞 الهاتف: {account_to_delete.get('phone', 'غير معروف')}\n"
            f"🔗 اليوزر: @{account_to_delete.get('username', 'غير معروف')}\n\n"
            "❗ لا يمكن التراجع عن هذه العملية.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✅ نعم، احذف", callback_data=f"confirm_del_{phone_to_delete}")],
                [InlineKeyboardButton("❌ لا، إلغاء", callback_data="remove_account")]
            ])
        )
    except Exception as e:
        await callback_query.message.edit(f"❌ حدث خطأ أثناء تحضير تأكيد الحذف:\n{e}")


@app.on_callback_query(filters.regex(r"^confirm_del_(.+)"))
async def execute_delete(client, callback_query):
    try:
        phone_to_delete = callback_query.data.split("_", 2)[2]
        accounts = await load_accounts()
        new_accounts = [acc for acc in accounts if acc['phone'] != phone_to_delete]

        if len(new_accounts) == len(accounts):
            await callback_query.answer("❌ الحساب غير موجود!", show_alert=True)
            return

        if await save_accounts(new_accounts):
            await callback_query.message.edit(
                "✅ **تم حذف الحساب بنجاح!**",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")]
                ])
            )
        else:
            await callback_query.message.edit(
                "❌ فشل في حذف الحساب!",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")]
                ])
            )
    except Exception as e:
        await callback_query.message.edit(
            f"❌ حدث خطأ أثناء حذف الحساب:\n{e}",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 العودة", callback_data="back_to_main")]
            ])
        )

@app.on_callback_query(filters.regex("upload_sessions"))
async def upload_sessions_handler(client, callback_query: CallbackQuery):
    if callback_query.from_user.username not in DEVS:
        await callback_query.answer("⚠️ أنت غير مخول لاستخدام هذا الأمر.", show_alert=True)
        return

    await callback_query.message.reply("📤 يرجى إرسال ملف الجلسات (accounts.json)")
    try:
        file_msg = await client.listen(callback_query.message.chat.id, filters=filters.document, timeout=300)
        
        if file_msg.document:
            file_path = await file_msg.download(file_name=os.path.join(os.getcwd(), "accounts.json"))
            await callback_query.answer("✅ تم تحديث الجلسات بنجاح")
        else:
            await callback_query.answer("❌ لم يتم إرسال ملف صحيح", show_alert=True)
    except asyncio.TimeoutError:
        await callback_query.answer("⌛️ انتهى الوقت المحدد للإرسال.", show_alert=True)
    except Exception as e:
        await callback_query.answer(f"❌ خطأ في التحديث: {str(e)}", show_alert=True)

@app.on_callback_query(filters.regex("get_sessions"))
async def get_sessions(client, callback_query: CallbackQuery):
    if not callback_query.from_user.username in DEVS:
        return
    with open("accounts.json", "rb") as file:
        await callback_query.message.reply_document(document=file)

@app.on_callback_query(filters.regex("invite_accounts"))
async def invite_accounts(client, callback_query: CallbackQuery):
    if callback_query.from_user.username not in DEVS:
        await callback_query.message.edit_text("ليس لديك صلاحيات لتنفيذ هذا الأمر.")
        return

    sessions = await load_sessions()
    
    name = await client.ask(callback_query.message.chat.id, "أرسل الآن الرابط")
    name = name.text
    if "https" in name:
        if not "+" in name:
            name = name.replace("https://t.me/", "")
    await callback_query.message.edit_text("انتظر قليلاً، جاري دعوة الحسابات للجروب...")

    for session in sessions:
        user = Client(f"session_{session}", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            await user.join_chat(name)
        except Exception as e:
            pass
        await user.stop()

    await callback_query.message.reply_text("تم انضمام الحسابات بنجاح للجروب.",
                                           reply_markup=InlineKeyboardMarkup([
                                               [InlineKeyboardButton("عودة", callback_data="back_to_main")]
                                           ]))

@app.on_callback_query(filters.regex("leave_call"))
async def leave_call(client, callback_query: CallbackQuery):
    if callback_query.from_user.username not in DEVS:
        await callback_query.message.edit_text("❌ ليس لديك صلاحيات لتنفيذ هذا الأمر.")
        return

    name = await client.ask(callback_query.message.chat.id, "📩 أرسل الآن رابط المجموعة")
    name = name.text
    if "https" in name:
        if "+" not in name:
            name = name.replace("https://t.me/", "")

    await callback_query.message.edit_text("⏳ جاري مغادرة جميع الحسابات من المكالمة الصوتية...")
    sessions = await load_sessions()
    for session in sessions:
        try:
            user = Client(f"session_{session}", api_id=API_ID, api_hash=API_HASH, session_string=session)
            await user.start()
            zombiiee = pytgcalls_instances.get(session)
            chat_info = await user.get_chat(name)
            await zombiiee.leave_group_call(chat_info.id)
            await user.stop()
        except Exception as e:
            print(f"❌ خطأ أثناء مغادرة المكالمة: {e}")
    await callback_query.message.edit_text("✅ تم مغادرة جميع الحسابات من المكالمة الصوتية.")

pytgcalls_instances = {}

@app.on_callback_query(filters.regex("invite_call"))
async def invite_call(client, callback_query: CallbackQuery):
    if callback_query.from_user.username not in DEVS:
        await callback_query.message.edit_text("❌ ليس لديك صلاحيات لتنفيذ هذا الأمر.")
        return

    sessions = await load_sessions()
    name = await client.ask(callback_query.message.chat.id, f"**📩 أرسل الآن رابط المجموعة**")
    name = name.text
    if "https" in name:
        if "+" not in name:
            name = name.replace("https://t.me/", "")

    count_msg = await client.ask(callback_query.message.chat.id, f"**📦 أرسل عدد الحسابات التي تريد استخدامها**")
    try:
        count = int(count_msg.text.strip())
    except ValueError:
        await callback_query.message.edit_text("❌ يرجى إرسال رقم صحيح.")
        return
    selected_sessions = sessions[:count]
    for session in selected_sessions:
        user = Client(f"session_{session}", api_id=API_ID, api_hash=API_HASH, session_string=session)
        await user.start()
        try:
            await user.join_chat(name)  
            zombiiee = PyTgCalls(user)
            await zombiiee.start()
            pytgcalls_instances[session] = zombiiee
            chat_info = await user.get_chat(name)
            await zombiiee.join_group_call(chat_info.id, AudioPiped(f"rr.mp3"), stream_type=StreamType().pulse_stream)
        except Exception as e:
            print(f"Error inviting user: {e}")
    await callback_query.message.reply_text(
        "✅ تم انضمام الحسابات بنجاح إلى المكالمة الصوتية.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 عودة", callback_data="back_to_main")]
        ])
    )

@app.on_callback_query(filters.regex("leave_accounts"))
async def leave_accounts(client, callback_query: CallbackQuery):
    if callback_query.from_user.username not in DEVS:
        await callback_query.message.edit_text("ليس لديك صلاحيات لتنفيذ هذا الأمر.")
        return

    sessions = await load_sessions()
    name = await client.ask(callback_query.message.chat.id, "أرسل الآن الرابط")
    name = name.text
    if "https" in name:
        if not "+" in name:
            name = name.replace("https://t.me/", "")
    await callback_query.message.edit_text("انتظر قليلاً، جاري مغادرة الحسابات من الجروب...")
    for session in sessions:
        async with Client(":memory:", api_id=API_ID, api_hash=API_HASH, session_string=session) as user:
            try:
                await user.leave_chat(name)
            except Exception as e:
                print(f"Error leaving chat: {e}")
    await callback_query.message.reply_text("تم مغادرة الحسابات بنجاح من الجروب.",
                                           reply_markup=InlineKeyboardMarkup([
                                               [InlineKeyboardButton("عودة", callback_data="back_to_main")]
                                           ]))

@app.on_callback_query(filters.regex("back_to_main"))
async def back_to_main(client, callback_query: CallbackQuery):
    kep = InlineKeyboardMarkup([
        [InlineKeyboardButton("اضف حساب 🎯", callback_data="add_account"),
         InlineKeyboardButton("حذف حساب 🗑️", callback_data="remove_account")],

        [InlineKeyboardButton("تنظيف الحسابات 🧹", callback_data="safe_clean_scan")],

        [InlineKeyboardButton("انضمام للكول 🎸", callback_data="invite_call"),
         InlineKeyboardButton("مغادره الكول 🚫", callback_data="leave_call")],

        [InlineKeyboardButton("رشق تفاعلات 👍", callback_data="likes_accs"),
         InlineKeyboardButton("رشق تفاعلات 👎", callback_data="dis_like")],
        
        [InlineKeyboardButton("رشق استفتاء 📊", callback_data="vote_poll"),
         InlineKeyboardButton("رشق تفاعل محدد 🙈", callback_data="spisifc_reaction")],

        [InlineKeyboardButton("انضمام للجروب ➕", callback_data="invite_accounts"),
         InlineKeyboardButton("مغادرة جروب 👋", callback_data="leave_accounts")],

        [InlineKeyboardButton("مغادره كل الجروبات 👋", callback_data="leave_all")],

        [InlineKeyboardButton("رفع مطور 🧑‍💻", callback_data="add_dev"),
         InlineKeyboardButton("تنزيل مطور ❌", callback_data="remove_dev")],

        [InlineKeyboardButton("رفع نسخة الجلسات 📤", callback_data="upload_sessions"),
         InlineKeyboardButton("جلب نسخة الجلسات 📂", callback_data="get_sessions")]
    ])
    await callback_query.message.edit_text("╮⦿ اهـلا بڪ عزيـزي المطـور الاساسـي │⎋ اليك كيب التحكم بالبوت", reply_markup=kep)

async def start_zombiebot():
    await app.start()
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_zombiebot())