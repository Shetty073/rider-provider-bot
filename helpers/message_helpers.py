from aiogram import types, Dispatcher


def get_user_info(message: types.Message):
    user = message.from_user
    user_is_bot = user.is_bot
    user_first_name = user.first_name
    user_last_name = user.last_name
    user_username = user.username

    return user_first_name, user_last_name, user_username, user_is_bot


def get_message_info(message: types.Message):
    message_text = message.text
    message_type = None
    user_mentioned = None
    if len(message.entities) > 0:
        message_type = message.entities[0].type
        offset = message.entities[0].offset
        length = message.entities[0].length
        user_mentioned = message_text[offset:length]

    return message_text, message_type, user_mentioned


async def is_bot_mentioned(message: types.Message, dp: Dispatcher):
    message_text = message.text
    is_mentioned = False
    bot = await dp.bot.get_me()
    bot_username = f"@{bot.username[:-3]}"
    for entity in message.entities:
        if entity.type == "mention":
            user_mentioned = message_text[entity.offset:entity.length]
            if user_mentioned == bot_username:
                is_mentioned = True

    return is_mentioned
