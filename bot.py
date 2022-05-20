import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

from handlers.chatbot import trainer, cb
from helpers.message_helpers import get_message_info, get_user_info, is_bot_mentioned

load_dotenv(".env")

API_TOKEN = os.environ.get("TG_API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    user_first_name, user_last_name, user_username, user_is_bot = get_user_info(message)
    message_text, message_type, _ = get_message_info(message)

    if not user_is_bot:
        if message_text == "/start":
            return await message.reply(f"Hi! {user_first_name} {user_last_name}. Pleasure speaking with you.")
        else:
            return await message.reply("Hi!\nI\"m EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    _, _, user_username, _ = get_user_info(message)

    is_mentioned = await is_bot_mentioned(message, dp)
    if is_mentioned:
        return await message.reply(f"I hate mentions @{user_username}")

    return await message.answer(f"{cb.get_response(message.text)}\n\n@{user_username}")


if __name__ == "__main__":
    trainer.train(
        "chatterbot.corpus.english"
    )
    executor.start_polling(dp, skip_updates=True)
