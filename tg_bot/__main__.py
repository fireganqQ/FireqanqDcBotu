import importlib, re
from typing import Optional, List

from telegram import Message, Chat, Update, Bot, User
from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
from telegram.ext.dispatcher import run_async, DispatcherHandlerStop
from telegram.utils.helpers import escape_markdown

from tg_bot import dispatcher, updater, TOKEN, WEBHOOK, OWNER_ID, PORT, URL, LOGGER, ALLOW_EXCL

# modülleri dinamik olarak yüklemek için gerekli
# NOT: Modül sırası garanti edilmez, bunu yapılandırma dosyasında belirtin!
from tg_bot.modules.helper_funcs.chat_status import is_user_admin
from tg_bot.modules.helpers_funcs.misc import paginate_modules
#========================KURULUM BİTİM===============================

PM_START_TEXT = """
Merhaba {} Benim Adım {}! Beni Nasıl Kullanacağınıza Dair Soruların Varsa /help \
Komutunu Kullan!

Herhangi Bir Sorunuz Varsa Yada Hata Bildirmek İcin Lütden [Sahibim'e](t.me/fireganqq) Bildirmekden Cekinme!
Ayrıca Yeni Özellikler, Kesinti Süresi Vb. için [Duyuru Kanalıma](t.me/fireqanQBotlari) Baka Bilirsin!!
"""

HELP_TEXT1 = """
Selam! Benim ismim *{}*.

*Komutlar:*
 - /start: `Botu Başlatır`
 - /help: `Botu Nasıl Kullanacağınıza Dair Bilgi Verir`
 - /ss: `Sectiğiniz Bir Tane Doğruluk Veya Cesaret Sorusu Sorar`
 """

@run_async
def start(bot: Bot, update: Update):
    update.effective_message.reply_text(PM_START_TEXT)

@run_async
def help(bot: Bot, update: Update):
    update.effective_message.reply_text(HELP_TEXT1)
