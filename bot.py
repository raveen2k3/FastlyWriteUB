from pyrogram import *
import pytesseract 
from PIL import Image
import os
from pyrogram.types import *
from time import sleep


from config import API_HASH, API_ID, SESSION_NAME , chats_covered , BOT_ID

fastly = Client(name="userbot" ,
    session_string= SESSION_NAME,
    api_id= API_ID,
    api_hash=API_HASH)

@fastly.on_message(filters.photo & filters.chat(chats_covered) & filters.user(BOT_ID))
async def ping (Client:fastly , message:Message):  
            path = await fastly.download_media(message ,file_name='bot_img.jpg')
            sleep(1)
            slicer = (pytesseract.image_to_string(Image.open(f'./downloads/bot_img.jpg')))
            word_to_send = slicer.replace("By @FastlyWriteBot" , " ")
            await fastly.send_message(message.chat.id , word_to_send)
            os.remove(path)
fastly.run()
