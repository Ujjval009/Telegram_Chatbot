import logging
import asyncio
from aiogram import Bot, Dispatcher , types ,  executor
from aiogram.utils import executor
from dotenv import load_dotenv
import os
import sys

from llm.mistral import generate_response

# Add the parent directory to sys.path to import main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Load environment variables
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
#print(TELEGRAM_BOT_TOKEN)

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    await message.answer(
        f"Hello, {message.from_user.full_name}!\n"
        "I'm Echo Bot!\n"
        "Send me any message."
    )
    
@dp.message_handler()
async def echo_handler(message: types.Message):
    #this will return echo
    await message.answer("Thinking... ⏳")
    reply = generate_response(message.text)
    await message.answer(reply)

    
if __name__ == "__main__":
    executor.start_polling(dp)