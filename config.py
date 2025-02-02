#(©)CodeXBotz
#By @Codeflix_Bots



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24371796"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "8121c78f4b8b31e88cc2623d1277338d")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002100796720"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1439890119"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://AnimeRavenBots:AnimeRavenBots@animeravenbots.huekk.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "kurumiX_Robot")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002038915478"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002034252225"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "-1002027984564"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>𝑯𝒆𝒚!! {mention} \n\nɪ 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝑻𝒐 𝑶𝒖𝒓 𝑵𝒆𝒙𝒖𝒔 𝑪𝒐𝒎𝒎𝒖𝒏𝒊𝒕𝒚, 𝑰𝒇 𝒚𝒐𝒖 𝒘𝒂𝒏𝒕 𝒕𝒐 𝒔𝒖𝒑𝒑𝒐𝒓𝒕 𝒐𝒖𝒓 𝒄𝒐𝒎𝒎𝒖𝒏𝒊𝒕𝒚, 𝒚𝒐𝒖 𝒄𝒂𝒏 𝒅𝒐 𝒔𝒐 𝒃𝒚 𝒔𝒖𝒃𝒔𝒄𝒓𝒊𝒃𝒊𝒏𝒈 𝒕𝒐 𝒐𝒖𝒓 𝒄𝒉𝒂𝒏𝒏𝒆𝒍, 𝑭𝒐𝒓 𝒎𝒐𝒓𝒆 𝒊𝒏𝒇𝒐𝒓𝒎𝒂𝒕𝒊𝒐𝒏 𝑱𝒐𝒊𝒏 𝒐𝒖𝒓 𝒄𝒉𝒂𝒏𝒏𝒆𝒍...!\nɪ » @AnimeNexusNetwork  𝑻𝒉𝒂𝒏𝒌𝒔 𝑭𝒐𝒓 𝒚𝒐𝒖𝒓 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 @Stelleron_Hunter</b>")
try:
    ADMINS=[1439890119]
    for x in (os.environ.get("ADMINS", "7827448605 5696112220").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b><blockquote>›› ʜᴇʏ {mention} ×,</blockquote>\n  ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>ʙᴀᴋᴋᴀ ! ᴅᴏɴᴛ ᴍᴇssᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @KaiXSen</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(7784698094)

LOG_FILE_NAME = "animeravenbots.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
