import os
import telebot
import time
import random
from telebot.types import ReactionTypeEmoji
from flask import Flask
from threading import Thread

# --- Render Free Web Service ko 24/7 chalu rakhne ke liye ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Reaction Army is Running 24/7!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()
# ------------------------------------------------------------

CHANNEL_ID = '-1003174608918'
ADMIN_ID = 8293930284

BOT_TOKENS = [
    '8772027820:AAHES2wr9xSAZU78dPgK_wHwyVwLxX-MY1I',
    '8800784513:AAE3ZyO-ecy5dMrhjlB8IkVgcS5YzT-Ce_A',
    '8950271478:AAHJ7ZgBP9jc7R8Sn_nlgZEibgPJPftUty4',
    '8868879654:AAEjpizvcyfR_zo9c0iLJ8nkqB710RAP2oA',
    '8607252483:AAHMBHn40RhI9aDROUwowEThZxaX23C9ZAU',
    '8924370337:AAG0VnWFb6KcEUnJMvGnSvSh2_H100ObVOI',
    '7979826205:AAHL14yHoDn7WZJYY4QShRRVHGAyX45Ihx8',
    '8716331470:AAHJdTMRJtdDpPcsTnWcOOEhfDSv4HIOdgA',
    '8896375341:AAFIARE3vowPT_UNyjsetgwvHelVtIfLdvI',
    '8234506410:AAGaZGoEsyPIVv4gtwmz4C9CRrHc1FWy1Xk',
    '8677522558:AAGHjtsQEjsM1sEaVjxrEvarKrKxDYI4LUo',
    '8993001188:AAFsCpchMKV-EXe35lYatl3MpYwo_p2s49s',
    '8510697506:AAFW1rKpTKvFYn9XsAeukt18w--2uv9VEYU',
    '8710269433:AAGEUgLcaxkX-ZwAKcClCVGdCdv7hrueGHc',
    '8686914219:AAHpeiwM2d9Ji27B2p1T8U0CzZCWrSo873U',
    '8453995922:AAHGjphoD1T4twZLpWYTcJY19jZalt162TQ',
    '8820512662:AAE_ivO6VspDTGZhqJ4k62UQBYLcFd2cKF4',
    '8603163010:AAErswz4PB4FKe2oOgLfYWZG1TpsZMZkAc0',
    '8768157460:AAEZd5RPokoMNwWHV2GwV7MY604Z5P6kwNg',
    '8889978482:AAFCpylNV6kaNEcMKbBh7LCmZzx-EquLBd8',
    '8710015496:AAH5qGnFlAjmwVZC8RNxsztJeZTYTzBIF28',
    '8953737905:AAEdkOSsIQD2OCutiafJaP3bzCqTmlJpYIM',
    '8841302750:AAGvgMctXpt75cyvvAb4ZSp5-de0DlaPUMA',
    '8631961254:AAGXuetTUEY1gHttduY9_sbTHmYdTsn8s-A',
    '8968876865:AAGADiYVwmT5URhHLCrFofBfS4-9rgmpmMU',
    '8621590313:AAEmhDBUghE3sL5M25oGybr8Daj_u3mYQQY',
    '8695106142:AAFvi4L398aT7YF0GHlbiO5HlPL1VtTWv78',
    '8867534170:AAEIBMlEVUOSBsn-YdJesTAm9LWO3w4i4FY',
    '8955662087:AAERs7ZcnKhr7glXrkbxIuiQEWXTjpelboo',
    '8929417976:AAHY82ulaE6bU6HYbldkIP3aHCVnFdlWR0o'
]

listener_bot = telebot.TeleBot(BOT_TOKENS[0])
processed_albums = set()

def send_reactions(message_id):
    emojis = ['⭐', '❤️', '👍', '🔥', '🥰', '😱', '👏', '💯', '⚡', '🏆', '😘', '🍾', '🙏', '🆒', '🎉']
    for index, token in enumerate(BOT_TOKENS):
        try:
            temp_bot = telebot.TeleBot(token.strip())
            reaction = ReactionTypeEmoji(random.choice(emojis))
            temp_bot.set_message_reaction(CHANNEL_ID, message_id, [reaction])
            time.sleep(1.5)
        except Exception as e:
            pass

# Text, Single Photo, 2+ Photos + Text (Album), Video sab par kaam karega
@listener_bot.channel_post_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'voice', 'animation', 'sticker'])
def auto_react(message):
    if str(message.chat.id) != str(CHANNEL_ID):
        return

    # Agar 2 ya zyada photo ek sath text laga kar bheji hain, toh us par ekdum sahi react karega
    if message.media_group_id:
        if message.media_group_id in processed_albums:
            return
        processed_albums.add(message.media_group_id)

    Thread(target=send_reactions, args=(message.message_id,)).start()

if __name__ == "__main__":
    keep_alive()
    listener_bot.remove_webhook()
    time.sleep(3)
    print("🚀 Reaction Army (Text + Photo + Video + Album) Chalu Ho Gayi Hai...")
    while True:
        try:
            listener_bot.infinity_polling(allowed_updates=['channel_post'], skip_pending=True)
        except Exception:
            time.sleep(5)
