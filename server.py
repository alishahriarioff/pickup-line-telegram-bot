import telebot
import requests

# Replace 'YOUR_BOT_TOKEN' with your actual token
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

def get_pickup_line():
    response = requests.get('https://rizzapi.vercel.app/random')
    data = response.json()
    return data['text']

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! 👋 Welcome to my bot. Type 'hit' for a random pickup line.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() == 'hit':
        pickup_line = get_pickup_line()
        bot.reply_to(message, pickup_line)
    else:
        bot.reply_to(message, "I don't understand. Type 'hit' for a random pickup line.")

bot.infinity_polling()