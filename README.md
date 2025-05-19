# Dalee Telegram Bot

Этот бот позволяет генерировать изображения высокого качества с помощью модели DALL-E 3 от OpenAI прямо в Telegram.

## Возможности
- Генерация изображений по текстовому описанию
- Простое взаимодействие через Telegram

## Быстрый старт

1. **Клонируйте репозиторий:**
   ```bash
   git clone <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
   cd <ИМЯ_ПАПКИ_РЕПОЗИТОРИЯ>
   ```
2. **Создайте и заполните файл `.env`:**
   ```env
   OPENAI_API_KEY=sk-ваш_ключ_от_OpenAI
   TELEGRAM_BOT_TOKEN=ваш_токен_бота_Telegram
   ```
3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Запустите бота:**
   ```bash
   python dalee_bot.py
   ```

## Переменные окружения
- `OPENAI_API_KEY` — ваш API-ключ OpenAI
- `TELEGRAM_BOT_TOKEN` — токен Telegram-бота

## Лицензия
MIT 