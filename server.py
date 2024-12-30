import telebot
import requests
import os
import logging
from dotenv import load_dotenv
import time

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    logger.error("No BOT_TOKEN found in .env file")
    raise ValueError("BOT_TOKEN environment variable is required")

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = [
        telebot.types.KeyboardButton('💘 Give me a Pickup Line!'),
        telebot.types.KeyboardButton('/start'),
        telebot.types.KeyboardButton('📖 Show Instructions'),
        telebot.types.KeyboardButton('🎯 About this Bot')
    ]
    keyboard.add(*buttons)
    return keyboard

def get_pickup_line():
    try:
        response = requests.get('https://rizzapi.vercel.app/random', timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            'text': data.get('text', 'Sorry, something went wrong. Try again!'),
            'category': data.get('category', 'unknown')
        }
    except (requests.RequestException, ValueError, KeyError) as e:
        logger.error(f"Error fetching pickup line: {e}")
        return {
            'text': "Sorry, I couldn't get a pickup line right now. Try again later!",
            'category': 'unknown'
        }

def get_category_emoji(category):
    category_emojis = {
        'romantic': '😍',
        'funny': '😂',
        'cheesy': '🧀',
        'flirty': '😉',
        'clever': '🤓',
        'complimentary': '🍭'
    }
    return category_emojis.get(category.lower(), '✨')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "✨ *Welcome to the Ultimate Pickup Line Bot!* ✨\n\n"
        "Press any button below to get started:\n\n"
        "• 💘 Get a creative pickup line\n"
        "• 📖 View instructions\n"
        "• 🎯 Learn about the bot"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', reply_markup=create_keyboard())

@bot.message_handler(func=lambda message: message.text and message.text.strip() in ['💘 Give me a Pickup Line!', 'hit', '/start'])
def send_pickup_line(message):
    if message.text.strip() == '/start':
        send_welcome(message)
    else:
        result = get_pickup_line()
        category = result['category']
        pickup_line = result['text']
        emoji = get_category_emoji(category)
        
        # Send header message with category
        header = f"🎯 *Here's your {category.title()} pickup line:* {emoji}"
        bot.send_message(message.chat.id, header, parse_mode='Markdown')
        
        # Send pickup line separately
        bot.send_message(message.chat.id, f"_{pickup_line}_", parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text and message.text.strip() == '📖 Show Instructions')
def show_instructions(message):
    instructions = (
        "*How to use this bot:*\n\n"
        "1. Click '💘 Give me a Pickup Line!' for a new pickup line\n"
        "2. Click '📖 Show Instructions' to see this message again\n"
        "3. Click '🎯 About this Bot' to learn more\n\n"
        "That's it! Simple and fun! 🌟"
    )
    bot.reply_to(message, instructions, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text and message.text.strip() == '🎯 About this Bot')
def about_bot(message):
    about_text = (
        "*About Pickup Line Bot*\n\n"
        "This bot provides fun and creative pickup lines to break the ice! "
        "Perfect for starting conversations or just having fun. "
        "All pickup lines are meant to be entertaining! 😊\n\n"
        "*Connect with the Developer:*\n"
        "• 📱 Telegram: @alishahriarioff\n"
        "• 📸 Instagram: @alishahriarioff\n"
        "• 🐦 X (Twitter): @alishahriarioff\n"
        "• 💼 LinkedIn: @alishahriarioff\n"
        "• 💻 GitHub: @alishahriarioff\n"
        "• 🎥 YouTube: @alishahriarioff\n\n"
        "Made with ❤️ for the fun of it!"
    )
    bot.reply_to(message, about_text, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Please use the buttons below! 👇", reply_markup=create_keyboard())

def main():
    logger.info("Bot started!")
    while True:
        try:
            bot.infinity_polling(timeout=60, long_polling_timeout=60)
        except Exception as e:
            logger.error(f"Bot error: {e}")
            logger.info("Attempting to restart bot in 10 seconds...")
            time.sleep(10)

if __name__ == "__main__":
    main()