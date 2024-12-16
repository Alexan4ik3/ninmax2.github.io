import aiogram
import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router1


async def main():
    bot = Bot(token='8096334704:AAFIYoy9yQ0YJF6QTvGRXpDt7BBi_yNehws')
    dp = Dispatcher()
    dp.include_router(router1)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye Bye')