from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.screenshotbot import ScreenShotBot
from bot.config import Config


BUTTONS = [[
    InlineKeyboardButton('π§πππΎ π‘', callback_data='home'),
    InlineKeyboardButton('π§πΎππ βοΈ', callback_data='help')
    ],[
    InlineKeyboardButton('π’ππππΎ π', callback_data='close')
]]


ABOUT_TEXT = """**MΚ Dα΄α΄α΄ΙͺΚs:**

**π€ Bα΄α΄:** {bot_name}
    
**βοΈ Lα΄Ι΄Ι’α΄α΄Ι’α΄:** [Python 3](https://www.python.org)

**π LΙͺΚΚα΄ΚΚ:** [Pyrogram](https://docs.pyrogram.org)

**π‘ Sα΄Κα΄ α΄Κ:** [DigitalOcean](https://digitalocean.com)

**π€ Dα΄α΄ α΄Κα΄α΄α΄Κ:** [Jerin](tg://user?id=1329457821)
"""

@ScreenShotBot.on_message(filters.private & filters.command("about"))
async def about_(c, m):
    me = await c.get_me()

    await m.reply_text(
        text=ABOUT_TEXT.format(
            bot_name=me.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(BUTTONS),
            quote=True,
    )


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("about"))
)
async def about_cb(c, m):
    me = await c.get_me()

    await m.answer()
    await m.message.edit(
        text=ABOUT_TEXT.format(
            bot_name=me.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(BUTTONS),
    )




