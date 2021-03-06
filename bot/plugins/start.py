from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config import Config
from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m, cb=False):
    owner_id = Config.AUTH_USERS[0]
    username = 'imjerin'
    mention = '[Jerin](https://t.me/imjerin)'
    try:
        owner = await c.get_users(owner_id)
        username = owner.username if owner.username else 'imjerin'
        mention = owner.mention(style="md")
    except Exception as e:
        print(e)

    BUTTONS = [[
        InlineKeyboardButton("π§πΎππ βοΈ", callback_data="help"),
        InlineKeyboardButton("π²πΎππππππ β", callback_data="set+settings")
        ],[
        InlineKeyboardButton("π π»πππ β", callback_data="about"),
        InlineKeyboardButton("π’ππππΎ π", callback_data="close")
    ]]

    TEXT = f"__π Hi {m.from_user.mention},\n\nI'm Screenshot Generator Bot. I can provide screenshots, sample video from__"
    TEXT += "__ your video files and also can trim them almost instantly without downloading the entire file. For more details check help.__\n\n"
    TEXT += f"**Maintained By:** {mention}"

    if cb:
        try:
            await m.message.edit(
                text=TEXT,
                reply_markup=InlineKeyboardMarkup(BUTTONS)
            )
        except:
            pass
    else:
        await m.reply_text(
            text=TEXT,
            quote=True,
            reply_markup=InlineKeyboardMarkup(BUTTONS)
        )


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("home"))
)
async def home_cb(c, m):
    await m.answer()
    await start(c, m, True)


@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("close"))
)
async def close_cb(c, m):
    try:
        await m.message.delete()
        await m.message.reply_to_message.delete()
    except:
        pass
