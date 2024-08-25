from pyrogram import Client, filters


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
