import asyncio

from Spotify_Music import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["repo"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/9e853d2314c00932163cf.mp4",
        caption=f"❖ ʜᴇʏ {message.from_user.mention} \n\n❖ ᴛᴇʀɪ ᴍᴀ ᴋɪ ᴄʜᴜᴛ",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="ɢʀᴏᴜᴘ", url=f"https://t.me/+Ckzm2ypQyIIzZTll"
            ),
            
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/All_SANATANI_BOT"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "• ᴄʟᴏsᴇ •", callback_data="close"
                    )
                ],
            ]
        )
    )
  
