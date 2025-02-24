# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from config import Config
from pyrogram import filters
from pyrogram.errors import UserNotParticipant
from pyrogram import Client as Tech_VJ
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.dl_button import ddl_call_back
from translation import Translation
from plugins.forcesub import get_invite_link

@Tech_VJ.on_callback_query(filters.regex('^X0$'))
async def delt(bot, update):
          await update.message.delete(True)


@Tech_VJ.on_callback_query()
async def button(bot, update):
    if "|" in update.data:
        await youtube_dl_call_back(bot, update)
    elif "=" in update.data:
        await ddl_call_back(bot, update)

    elif update.data == "home":
        await update.message.edit(
            text=Translation.TECH_VJ_START_TEXT.format(update.from_user.mention),
            reply_markup=Translation.TECH_VJ_START_BUTTONS,
            # disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit(
            text=Translation.TECH_VJ_HELP_TEXT,
            reply_markup=Translation.TECH_VJ_HELP_BUTTONS,
            # disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit(
            text=Translation.TECH_VJ_ABOUT_TEXT,
            reply_markup=Translation.TECH_VJ_ABOUT_BUTTONS,
            # disable_web_page_preview=True
        )
    elif "close" in update.data:
        await update.message.delete(True)

    elif "refreshForceSub" in update.data:
        if Config.TECH_VJ_UPDATES_CHANNEL:
            if str(Config.TECH_VJ_UPDATES_CHANNEL).startswith("-100"):
                channel_chat_id = int(Config.TECH_VJ_UPDATES_CHANNEL)
            else:
                channel_chat_id = Config.TECH_VJ_UPDATES_CHANNEL
            try:
                user = await bot.get_chat_member(channel_chat_id, update.message.chat.id)
                if user.status == "kicked":
                    await update.message.edit(
                        text="عذرا لا تستطيع استخدام البوت تم حظرك لحل المشكلة تواصل مع الدعم [المطور ](https://t.me/X_XF8).",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                chat_id = channel_chat_id
                invite_link = await get_invite_link(bot, chat_id)
                await update.message.edit(
                    text="**Iيعجبني ذكائك ولكن لا تكن ذكيًا أكثر من اللازم! 😑**\n\n",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🤖 انضم لقناتي ! ", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton("🔄 تحديث 🔄", callback_data="refreshForceSub")
                            ]
                        ]
                    )
                )
                return
            except Exception:
                await update.message.edit(
                    text="حدث خطأ برجاء التوصل  مع  [المطور ](https://t.me/X_XF8).",
                    disable_web_page_preview=True
                )
                return
        await update.message.edit(
            text=Translation.TECH_VJ_START_TEXT.format(update.from_user.mention),
            reply_markup=Translation.TECH_VJ_START_BUTTONS,
            # disable_web_page_preview=True
        )
