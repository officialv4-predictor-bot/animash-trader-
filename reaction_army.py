import telebot
import time
import random
from telebot.types import ReactionTypeEmoji

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
# Yeh ek safety step hai taaki bot restart hote hi phasse nahi
listener_bot.remove_webhook()
time.sleep(1)

@listener_bot.channel_post_handler(func=lambda message: str(message.chat.id) == CHANNEL_ID)
def auto_react(message):
    
    emojis = ['⭐', '❤️', '👍', '🔥', '🥰', '😱', '👏', '💯', '⚡', '🏆', '😘', '🍾', '🙏', '🆒', '🎉']

    for index, token in enumerate(BOT_TOKENS):
        try:
            temp_bot = telebot.TeleBot(token.strip())
            reaction = ReactionTypeEmoji(random.choice(emojis))
            temp_bot.set_message_reaction(CHANNEL_ID, message.message_id, [reaction])
            time.sleep(2) 
        except Exception as e:
            error_msg = f"❌ Bot Number {index + 1} fail ho gaya!\nWajah: {e}"
            try:
                listener_bot.send_message(ADMIN_ID, error_msg)
            except:
                pass

print("🚀 Error Tracker Wali Army Chalu Ho Gayi Hai...")

while True:
    try:
        # YAHAN THI SABSE BADI GALTI - Ise kabhi mat hatana
        listener_bot.infinity_polling(allowed_updates=['channel_post'])
    except Exception as e:
        time.sleep(5)
