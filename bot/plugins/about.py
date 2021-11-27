from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.screenshotbot import ScreenShotBot
from bot.config import Config




ABOUT_TEXT = """**𝖬𝗒 𝖣𝖾𝗍𝖺𝗂𝗅𝗌 :**

** My Name:** {bot_name}
    
** Language:** [Python 3](https://www.python.org/)

** FrameWork:** [Pyrogram](https://github.com/pyrogram/pyrogram)

** Server:** [DigitalOcean(https://digitalocean.com)

** Developer:** {bot_owner}
"""


@ScreenShotBot.on_message(filters.command("about") & filters.private & filters.incoming)
async def about(c, m, cb=True):
    me = await c.get_me()
    owner = await c.get_users(Config.AUTH_USERS)

    button = [[
        InlineKeyboardButton('Hᴏᴍᴇ 🏡', callback_data='home'),
        InlineKeyboardButton('Hᴇʟᴘ ⁉️', callback_data='help')
        ],[
        InlineKeyboardButton('Cʟᴏsᴇ 📛', callback_data="close")
    ]]
    reply_markup = InlineKeyboardMarkup(button)
    if cb:
        await m.message.edit(
            text=ABOUT_TEXT.format(bot_name=me.mention(style='md'), bot_owner=owner.mention(style="md")),
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
    else:
        await m.reply_text(
            text=ABOUT_TEXT.format(bot_name=me.mention(style='md'), bot_owner=owner.mention(style="md")),
            disable_web_page_preview=True,
            reply_markup=reply_markup,
            quote=True
        )
