# Тестирую здесь работу тех или иных материалов

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '7170884667:AAGbZf1WSIz4SqsC7Ejyt0ZCvovrmt7t6O4'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!\nЗдесь Вы можете заказать кальян')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Этот бот упрощает заказ кальяна в ГринСити\n'
        'Вот описание команд, которые Вы можете использовать:\n'
        '/booking   - ВЫ можете выполнить бронирование кальяна (рекомендуется сперва посмотреть календарь)\n'
        '/freely    - Вы можете посмотреть количество свободных кальянов на сегодняшний день\n'
        '/calendar  - Вы можете посмотреть свободные дни для заказа кальяна\n'
        '/support   - В случае некорректной работы бота Вы можете связаться с поддержкой\n'
    )


# Этот хэндлер будет срабатывать на команду "/booking"
@dp.message(Command(commands=["booking"]))
async def process_start_command(message: Message):
    await message.answer(
        'Эта команда пока не реализована в полном объеме.\n'
        'Напишите @Steave_Boll для уточнения бронирования')


# Этот хэндлер будет срабатывать на команду "/freely"
@dp.message(Command(commands=["freely"]))
async def process_start_command(message: Message):
    await message.answer(
        'Эта команда пока не реализована в полном объеме.\n'
        'Напишите @Steave_Boll для уточнения количества свободных кальянов')


# Этот хэндлер будет срабатывать на команду "/calendar"
@dp.message(Command(commands=["calendar"]))
async def process_start_command(message: Message):
    await message.answer(
        'Эта команда пока не реализована в полном объеме.\n'
        'Напишите @Steave_Boll для уточнения свободных дней для бронирования')


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(
            text = 'Данный тип апдейтов не поддерживается'
            'методом send_reply'
        )


if __name__ == '__main__':
    dp.run_polling(bot)