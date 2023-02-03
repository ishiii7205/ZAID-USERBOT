import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = int(getenv("OWNER_ID"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BVtsOJYBuyVG7YYeap9mRZfv5xzj9LG3o0uA2A6WvFegzaotR_OEb4h7WupJPIX3YCQpk6vaZ2cZg9UwkvxyDvRHw74HhkgZQ9HJAOaVwU3Br_uiRH8nGQPpKroh7W2E-6r4AoDNIuiNOWuCD6k4Fd5MPHNohwWfuLDXhux99AzdrBJry9oY2FANaCkcRVeXrRsvchG5btOBbHLSpAOTTa22JXC_tV9wFzZsQsjZZMgb8lhgpUkFsXeuOGK2KsGz9Il0n-JOOJ6664CJESeuqOQQHGoCrBpGK8zkq1U2fUA56O1b5hpBib04n932ASazdcFY6u1VDXK0QagmfcSXHQXUFbyG0wc=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
