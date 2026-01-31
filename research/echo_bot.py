import logging
import asyncio
from aiogram import Bot, Dispatcher , types 
from aiogram.utils import executor
from dotenv import load_dotenv
import os
import main


# Load environment variables
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
#print(TELEGRAM_BOT_TOKEN)

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(Commands=['start', 'help'])
async def command_start_handler(message:types.Message):
    """
    This handler receives messages with `/start` or  `/help` command
    """
    await message.answer(f"Hello,{message.from_user.full_name}!\nI'm Echo Bot!\nSend me any message, and I'll echo it back to you.")
    

if __name__ == "__main__":
    executor.start_polling(dp)