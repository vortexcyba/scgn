from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.utils import Utilities
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"**Hi there {m.from_user.mention}.\n\nI'm Screenshot Generator. I can provide screenshots from**"
        "your video files almost instantly without downloading the entire file. For more details check /help.**",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👤 Maintained By", url="https://t.me/imjerin"),
                    InlineKeyboardButton(
                        "⚙️ Settings", callback_data="set+settings")
                ]
            ]
         )
    )
