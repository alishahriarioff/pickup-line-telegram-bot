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

def get_pickup_line():
    try:
        response = requests.get('https://rizzapi.vercel.app/random', timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get('text', 'Sorry, something went wrong. Try again!')
    except (requests.RequestException, ValueError, KeyError) as e:
        logger.error(f"Error fetching pickup line: {e}")
        return "Sorry, I couldn't get a pickup line right now. Try again later!"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "Hello! 👋 Welcome to the Pickup Line Bot!\n\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "Just type 'hit' to get a random pickup line!"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: message.text.lower() == 'hit')
def send_pickup_line(message):
    pickup_line = get_pickup_line()
    bot.reply_to(message, pickup_line)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "I don't understand. Type 'hit' for a random pickup line or /help for commands.")

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