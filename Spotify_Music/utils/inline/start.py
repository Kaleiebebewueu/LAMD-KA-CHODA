from pyrogram.types import InlineKeyboardButton

import config
from Spotify_Music import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ), 
        ],   
        [
            InlineKeyboardButton(text="• ʜᴇʟᴘ •", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="• sᴇᴛ •", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
             InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data="close"),
             ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="˹ʙᴏᴛ sᴛᴀᴛᴜs ᴀɴᴅ ᴍᴏʀᴇ ʙᴏᴛs˼", url=f"https://t.me/All_SANATANI_BOT/324"),
    ],
    ]
    return buttons
