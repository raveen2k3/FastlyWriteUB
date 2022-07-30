from os import getenv, path

from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SESSION_NAME = getenv("SESSION_NAME")
if CHATS := getenv("AUTHORIZED_CHATS", None):
    CHATS = CHATS.split(" ")