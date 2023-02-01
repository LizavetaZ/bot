# import aiohttp
import time
import logging
from aiogram import Bot, Dispatcher, executor, types

# async def hi_command(update: Update, context: ContextTypes) -> None:
#     await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

# 'UTF-8-sig'
logging.basicConfig(level=logging.INFO, filename="bot_log.csv", filemode="w",
                    format="%(asctime)s: %(levelname)s %(funcName)s-%(lineno)d %(message)s")


MSG = "{}, choose an action:"

bot = Bot("5873069701:AAHypQc7tY8K5--o6yHe3BddYs5FsZdeyhI")
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    user_bot = message.from_user.is_bot
    user_message = message.text
    logging.info(f'{user_id=} {user_bot=} {user_message=}')
    await message.reply(f"Hi, {user_full_name}!")
    time.sleep(1)
    btns = types.ReplyKeyboardMarkup(row_width=2)
    # btn_calc = types.KeyboardButton('/calculator')
    # btn_notes = types.KeyboardButton('/notes')
    btn_image = types.KeyboardButton('/send_image')
    btn_out = types.KeyboardButton('/quit')
    btns.add(btn_image, btn_out)
    await bot.send_message(user_id, MSG.format(user_name), reply_markup=btns)

@dp.message_handler(commands=['quit'])
async def quit_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Goodbye! See you...',
                           reply_markup=types.ReplyKeyboardRemove())

# @dp.message_handler(commands=['notes'])
# async def quit_handler(message: types.Message):
#     await bot.send_message(message.from_user.id, 'This is notes!',
#                            reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['send_image'])
async def cmd_send_image(message):
    with open("cat.jpg", "rb") as f:
        await bot.send_photo(message.chat.id, photo=f)


if __name__ == '__main__':
    executor.start_polling(dp)