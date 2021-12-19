from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.screenshotbot import ScreenShotBot
from bot.config import Config


BUTTONS = [[
    InlineKeyboardButton('𝖧𝗈𝗆𝖾 🏡', callback_data='home'),
    InlineKeyboardButton('𝖧𝖾𝗅𝗉 ⁉️', callback_data='help')
    ],[
    InlineKeyboardButton('𝖢𝗅𝗈𝗌𝖾 📛', callback_data='close')
]]


ABOUT_TEXT = """**Mʏ Dᴇᴛᴀɪʟs:**

**🤖 Bᴏᴛ:** {bot_name}
    
**✒️ Lᴀɴɢᴜᴀɢᴇ:** [Python 3](https://www.python.org)

**📔 Lɪʙʀᴀʀʏ:** [Pyrogram](https://docs.pyrogram.org)

**📡 Sᴇʀᴠᴇʀ:** [DigitalOcean](https://digitalocean.com)

**👤 Dᴇᴠᴇʟᴏᴘᴇʀ:** [Jerin](tg://user?id=1329457821)
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




