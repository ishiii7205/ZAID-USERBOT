import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "314582")) #optional
API_HASH = getenv("API_HASH", "b97e01ff95ec622ef8fadb7f5a4459cc") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5881100695").split()))
OWNER_ID = int(getenv("OWNER_ID","5846001897"))
MONGO_URL = getenv("MONGO_URL","mongodb+srv://Devarora0987:#Dev12345@cluster0.razivtc.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5814096427:AAFOXMOfUggS4ZXh0TVGzGRbgyiMwrCDuGI")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ishiii7205/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "1BVtsOLUBuyI5WMljGNQGY18ykGsWErRLSHxR1lg3yflGJF9swlWLDVblDHCYFV3EozpQtULh2f5e3xSVumSZQqm7vDCRoIW8R6Ks_CxzAyqTOwHj_Uy0JY9efVPHOPhucUdHOumPGndEKuPXnv6JLlufXXCUsiIvNM67IN0pXaHxQRHIuGdpZ_noRHYuAWB8AaxJA1yjxdrSpN4Jebdk3PHNoQCk3vScfcJV7Krql7PY9Aar-njfJm-9oVvURtR-PmmFosoaR042GPr5J7UFOjhBPRQRVXs4g-Ix-iIadeKcKPaahzdg4sBEmaknFGgw281W9hlvVWI1kA7CPKLSLJ9RkQ6MxPI=")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
