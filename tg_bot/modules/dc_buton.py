import importlib
import re
from typing import Optional, List

from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown

from tg_bot import dispatcher, updater, TOKEN, WEBHOOK, OWNER_ID, DONATION_LINK, CERT_PATH, PORT, URL, LOGGER, \
    ALLOW_EXCL
# modülleri dinamik olarak yüklemek için gerekli
# NOT: Modül sırası garanti edilmez, bunu yapılandırma dosyasında belirtin!
from tg_bot.modules import ALL_MODULES
from tg_bot.modules.helper_funcs.chat_status import is_user_admin
from tg_bot.modules.helper_funcs.misc import paginate_modules



def ss(bot: Bot, update: Update):
    update.effective_message.reply_text("Lüfen Cevaplamak İstediğiniz Soru Tipini Seçiniz!",
                                        reply_markup=InlineKeyboardMarkup(
                                            [[InlineKeyboardButton(text="Doğruluk",
                                                                   update.effective_message.send_massage("selam"))]]))




def asad(bot: Bot, update: Update):
    MARKDOWN = bot.send_massage("selamm")
    update.effective_message.reply_text("Lüfen Cevaplamak İstediğiniz Soru Tipini Seçiniz!",
                                        reply_markup=InlineKeyboardMarkup(
                                            [[InlineKeyboardButton(text="Doğruluk",
                                                                   parse_mode=ParseMode.MARKDOWN]]))





ss_handler = CommandHandler("ss", ss)
asad = CommandHandler("asad", asad)

dispatcher.add_handler(ss_handler)
dispatcher.add_handler(asad)
