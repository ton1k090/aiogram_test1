import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router

bot = Bot(token=TOKEN)
dp = Dispatcher() # Обработчик входящих обновлений


async def main():
    dp.include_router(router) # Сообщить о существовании роутера
    await dp.start_polling(bot) # Отправлять запрос и ждать ответ


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO) # Добавить логирование
    try:
        asyncio.run(main())
    except KeyboardInterrupt: # ошибка при отключении бота
        print('exit')