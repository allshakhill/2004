from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "6159822636"))
API_HASH = getenv("API_HASH", "40e7041d06ea7b6ee1cf39b3188b3452")
BOT_TOKEN = getenv("BOT_TOKEN", "6617823581:AAGYslekrMONNywxYEfEdRO2EnnEaL6DaGQ")
SESSION_NAME = getenv("SESSION_NAME", "AgCDx9n2Ddwc2AS3-2H02XDbuvV72PBKN-xRHXHxMZbLbVZBBrAcntgRcBXN6n0thLsbBsNmXmc8Ie0vW19SFeqq3LTYFOt71F7OjfSBn3Oj5Sv6QXOCqbUsw6aOMi4MCSo4QPERy0Lk0dTmO_ty-GkrdagNsegMvqxLTQrteo50nZc5QxQXuT7WML63gD8dxYDuSaJCwR-eAewbcypbIXIfkvFRTLyemqsBTHhcUmyG3LkGbyhjIVtTQ92HzIpMQncoaPiPSAcgAZUO6_p2iqbaZ7jMOFg5yPK3Q1DTrlb7utHh9myI1uBJTfh8X3s-zP2ZJr4iT9l4D86MiMnINDGCAAAAAW5NJEIA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "ccc_ac")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "Drive_lbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "EEIElO")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "EEIElO")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "6159822636").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6145516610").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
