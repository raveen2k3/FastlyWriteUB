from os import remove
from sys import version_info
from time import sleep

import pytesseract
from PIL import Image
from pyrogram import Client
from pyrogram import __version__ as pyro_version
from pyrogram import filters
from pyrogram.types import Message

from config import API_HASH, API_ID, CHATS, SESSION_NAME

fastly = Client(
    name="userbot",
    session_string=SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
)

python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"

BOT_VERSION = "0.1"
alive_msg = f"""
**fastlyWrite USERBOT is Alive & Running**\n
    **Python Version:** `{python_version}`
    **Pyrogram Version:** `{pyro_version}`
    **Bot Version:** `{BOT_VERSION}`
**\n\n HOST YOUR OWN AND CHEAT WEN ? **"""

prefixes = [".", "!"]


@fastly.on_message(
    filters.photo
    & filters.chat(CHATS)
    & filters.user(users=[1877720720, 1983714367, 5053950120])
)
async def ping(_, message: Message):
    path = await fastly.download_media(message, file_name="bot_img.jpg")
    print("Now working")
    sleep(1)
    slicer = pytesseract.image_to_string(Image.open("./downloads/bot_img.jpg"))
    word_to_send = slicer.replace("By @FastlyWriteBot", " ")
    await message.reply_text(word_to_send)
    remove(path)


@fastly.on_message(filters.command(["alive"], prefixes) & filters.me)
async def alive(_, message: Message):
    chat_id = message.chat.id
    await message.reply_text(alive_msg)
    await fastly.delete_messages(chat_id, message.id)


if __name__ == "__main__":
    fastly.run()
