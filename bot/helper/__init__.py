from pyrogram import Client, filters

from decouple import config

api = 29452145
hash = "5a2784e571fe5043852d32396a34a13b"
bot = "7445547849:AAHfX4_8TQ57cg71Q_l9ABoa6RfgfPWHgsE"
owner = str("6169288210").split()
group = "-1002243837012"
block = "1 2 3"
try:
    api = config("api", cast=int)
    hash = config("hash")
    bot = config("bot")
    owner = str(config("owner", default="1 2")).split()
    group = config("group")

    block = str(config("Block", default="1 2")).split()
except:
    print("error config")
app = Client("bot", api_id=api, api_hash=hash, bot_token=bot)
download_dir = "download"
codec_dir = "codec"
