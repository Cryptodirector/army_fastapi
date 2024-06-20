import asyncio
import logging
from aiogram import Bot, Dispatcher


logging.basicConfig(level=logging.INFO)

bot = Bot(token="7208425920:AAGqdNb93u9Q-E0MA-qz6TFJlCcPlxkbxqg")

dp = Dispatcher()


async def send_msg(value: str):
    await bot.send_message(
        text=value,
        chat_id='847449845'
    )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
