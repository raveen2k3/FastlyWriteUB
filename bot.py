from pyrogram import *
import pytesseract 
from PIL import Image
import os
from pyrogram.types import *
from time import sleep
from sys import version_info
from pyrogram import __version__ as pyro_version
from config import API_HASH, API_ID, SESSION_NAME

fastly = Client(name="userbot" ,
    session_string= SESSION_NAME,
    api_id= API_ID,
    api_hash=API_HASH)

python_version = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"

BOT_VERSION = "0.1"
alive_msg = f"""
**fastlyWrite USERBOT is Alive & Running**
    
    **Python Version:** `{python_version}`
    **Pyrogram Version:** `{pyro_version}`
    **Bot Version:** `{BOT_VERSION}`
**\n\n HOST YOUR OWN AND CHEAT WEN ? **"""

prefixes=["." , "!"]

#change the chats & the bot_id(users)
#i tried fix it but sadly i cant , maybe in future ill fix it 
@fastly.on_message(filters.photo & filters.chat(chats=[-1001266552555,-1001355881913,-1001577467953,-1001577467953,-1001384708196]) & filters.user(users=[ 1877720720 , 1983714367 , 5053950120]))
async def ping (Client:fastly , message:Message):    
    path = await fastly.download_media(message ,file_name='bot_img.jpg')
    print("not working")
    sleep(1)
    slicer = (pytesseract.image_to_string(Image.open(f'./downloads/bot_img.jpg')))
    word_to_send = slicer.replace("By @FastlyWriteBot" , " ")
    await fastly.send_message(message.chat.id , word_to_send)
    os.remove(path)
            



@fastly.on_message(filters.command(["alive"] , prefixes))
async def alive (Client:fastly , message:Message):
    user_id = message.from_user.id
    tester_id = [1871813121]
    if user_id in tester_id:
        chat_id = message.chat.id
        await fastly.delete_messages(chat_id , message.id)
        await fastly.send_message(chat_id ,text= alive_msg)


        
        
fastly.run()
