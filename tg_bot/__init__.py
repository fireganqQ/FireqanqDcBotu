import logging, os, sys

import telegram.ext as tg

# günlük kaydı etkinleştir
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(massage)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

# sürüm <3.6 ise, botu durdurun.

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("En az 3.6 python sürümüne sahip olmalısınız! Birden çok özellik buna bağlıdır. Bot bırakma.")
    quit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", None)
    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", None))
    except ValueError:
        raise Exception("OWNER_ID env değişkeniniz geçerli bir tam sayı değil")

    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "") # Jeton içermez
    PORT = int(os.environ.get("PORT", 5000))
    WORKERS = int(os.environ.get('WORKERS', 8))
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
else:
    from tg_bot.config import Development as Config
    TOKEN = Config.API_KEY
    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("OWNER_ID değişkeniniz geçerli bir tam sayı değil")

    OWNER_USERNAME = Config.OWNER_USERNAME
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    WORKERS = Config.WORKERS
    ALLOW_EXCL = Config.ALLOW_EXCL
updater = tg.Updater("1461600900:AAFNecHk8ofiLpEGKj2nwsP0N-rTdnfGFyI", workers=WORKERS)
dispatcher = updater.dispatcher

# Önceki tüm değişkenlerin ayarlandığından emin olmak için sonuna yükleyin
from tg_bot.modules.helper_funcs.handlers import CustomCommandHandler, CustomRegexHandler

# normal ifade işleyicisinin fazladan anahtarlar alabileceğinden emin olun
tg.RegexHandler = CustomRegexHandler

if ALLOW_EXCL:
    tg.CommandHandler = CustomCommandHandler
