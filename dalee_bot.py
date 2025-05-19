import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import openai
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Установите ваш ключ API OpenAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
# Установите токен вашего Telegram-бота
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

# Инициализация логирования
logger = logging.getLogger(__name__)

# Установка ключа API OpenAI
openai.api_key = OPENAI_API_KEY

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("👋 Привет! Я готов генерировать изображения в высоком качестве. Просто отправь мне свой запрос.")

# Обработчик текстовых сообщений
@dp.message_handler(lambda message: message.text and not message.text.startswith(' '))
async def generate_image(message: types.Message):
    user_id = message.from_user.id
    prompt = f"Ты самый лучший генератор картинок в высоком качестве. {message.text}"

    # Отправляем сообщение "Ожидайте..."
    waiting_message = await message.reply("⏳ Ожидайте..")

    try:
        # Запрос к OpenAI для генерации изображения
        response = openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="hd",
            n=1,
        )

        # Получаем URL изображения из ответа OpenAI
        image_url = response.data[0].url

        # Отправляем изображение пользователю в Telegram
        await bot.send_photo(chat_id=user_id, photo=image_url)

    except Exception as e:
        # Обработка ошибок
        logger.error(f"Error generating image: {e}")
        await message.reply("Произошла ошибка при генерации изображения. Пожалуйста, попробуйте еще раз.")

    finally:
        # Удаляем сообщение "Ожидайте..."
        await bot.delete_message(chat_id=user_id, message_id=waiting_message.message_id)

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
