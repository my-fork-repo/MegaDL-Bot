# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os

class Config:
    API_ID = 3704772
    API_HASH = os.environ.get("API_HASH", "b8e50a035abb851c0dd424e14cac4c06")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1064540465:AAFTgEC_xtVSiu3RdoESorVfy_cAwZ5K0Qw")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = 500774612
    LOG_CHANNEL = -1001884618152
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)


class TEXT:
  ABOUT = """
🤖 **Name:** {bot_name}

📝 **Language:** [Python](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted On:** [Heroku](https://heroku.com)

🧑‍💻 **Developer:** [Safone](https://t.me/ImSafone)

👥 **Support Group:** [AsmSupport](https://t.me/AsmSupport)

📢 **Updates Channel:** [Ｓ１ ＢＯＴＳ](https://t.me/AsmSafone)
"""

  HELP_USER = """
This is **{bot_name}**

This Bot Can Download Files & Videos From Mega Links & Upload To Telegram. Just Send Any Mega.nz Link & See The Magic. You Can Also Add or Change Caption: Just Select An Uploaded File/ Video or Forward Me Any Telegram File & Then Write The Text You Want To Be Caption On The File As A Reply To That File & The Text You Wrote Will Be Attached As Caption 😁! 

**Made With ❤️ By @AsmSafone! 👑**
"""

  START_TEXT = """
👋🏻 **Hi** {user_mention},

I'm **{bot_name}**
I Can Download Files & Videos From Mega.nz Links & Upload To Telegram. Please Check Help To Learn More 😉!

**Maintained By: {bot_owner}**❤️!
"""
