# Telegram Pickup Line Bot 🎯

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A Telegram bot that delivers random pickup lines with style. Categories include funny, romantic, and cheesy lines to brighten your day or break the ice.

## Features 🌟

- Random pickup line generation
- Category-based responses
- Interactive keyboard interface
- Emoji support
- Error handling and logging
- Environment variable configuration

## Installation 🛠️

1. Clone the repository and move to the directory
```bash
git clone https://github.com/yourusername/telegram-pickup-bot.git
cd telegram-pickup-bot
```
2. Create virtual environment and activate it
```bash
python -m venv .venv
.venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Configure environment variables
```bash
copy .env.example .env
# Edit .env with your Telegram Bot Token
```

## Usage 💡

1.Start the bot
```bash
python server.py
```
2.Available Commands
* ``/start`` - Initialize the bot
* ``💘 Give me a Pickup Line!`` - Get a random pickup line
* ``📖 Show Instructions`` - Display help
* ``🎯 About this Bot`` - Show bot information

## API Reference 📚

The bot uses the [Rizz](https://rizzapi-doc.vercel.app/) API for pickup line generation.

## Dependencies 📦

* python-telegram-bot
* python-dotenv
* requests

## Contributing 🤝

1. Fork the repository
2. Create feature branch (``git checkout -b feature/AmazingFeature``)
3. Commit changes (``git commit -m 'Add AmazingFeature'``)
4. Push to branch (``git push origin feature/AmazingFeature``)
5. Open a Pull Request

## License 📄

Distributed under the MIT License. See ``LICENSE`` for more information.

## Contact 📧

Ali Shahriari - ``@alishahriarioff`` - on every platform.

Project Link:
```bash
https://github.com/alishahriarioff/telegram-pickup-bot
```
