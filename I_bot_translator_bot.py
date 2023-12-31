from googletrans import Translator
import logging

from aiogram import Bot, Dispatcher, executor, types
API_TOKEN="6821676696:AAH00T4XDy3klCHkncCXeCbwdXlg1djJfvI"

# Configure logging
logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)
tarjima=Translator()

@dp.message_handler(commands=['start','help'])
async def echo(massage:types.Message):
    await massage.answer(f"Asslomalaykum 'I_bot_translator'ga xush kelibsiz \n Matningizni yuboring.")




@dp.message_handler()
async def get_data(massage:types.Message):
    matn=massage.text
    tarjimon=tarjima.translate(matn,dest='en')
    tarjima_qilindi=tarjimon.text
    await massage.reply(tarjima_qilindi)

if __name__== '__main__':
    executor.start_polling(dp,skip_updates=False)