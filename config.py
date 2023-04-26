from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "9514755"))
API_HASH = getenv("API_HASH", "40e7041d06ea7b6ee1cf39b3188b3452")
BOT_TOKEN = getenv("BOT_TOKEN", "6057670247:AAHjlWk0looQHIlLlArrEBIwLWViXvRRU7E")
SESSION_NAME = getenv("SESSION_NAME", "AgBhcataC10vlEailv-arbss4S9BWv4zMbr-R5PSS2hQ0ZCUX0dwOJe1q3K7zhByOt1KjVAufNnaxcEMsktb6D7idGmyR9NCfbPgOJTIr-aHlGJCwSQnzQkdhVpJCSnRC3SPbm-1EhX2seu6ECiG8VcVMJH-37KKMfugencCuBxibLr6McCIjNGpjcIT0ZS52F8s_ZZevTrWvR1mjYFWBKmTHgK-xXARqU1qs4QYGry_Ziw-oiERfvZZ3bn4tQZVe1wQqjWuE21LAZuz_agi60ZZiHc8IhVe8nVK1roLLSsGaLhi1KwXm99gp4g2VJ2HOUc_hE4Y4UWZqb6JROkS4yM-AAAAAXdqi1AA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "ccc_ac")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "Allsh_4bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ccc_ac")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "C3IUI")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
