from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

'''Кнопки ниже окна ввода сообщения
Один список один ряд - каждая кнопка в списке который в основном списке
resize_keyboard - уменьшить клавиатуру
input_placeholder - подсказка в окне сообщений'''

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Catalog')],
#     [KeyboardButton(text='Basket'), KeyboardButton(text='Contacts'),]
# ], resize_keyboard=True, input_field_placeholder='main menu')


'''inline клавиатура с калбэком при нажатии на кнопку ничего не отправляется в чат
поэтому здесь используются callback для обработки сообщений'''
main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Catalog', callback_data='catalog')],
    [InlineKeyboardButton(text='Basket', callback_data='basket'),
     InlineKeyboardButton(text='Contacts', callback_data='contacts')]
])


'''Кнопки выше окна сообщений
Один список один ряд - каждая кнопка в списке который в основном списке
Нельзя оставить только текст'''
settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Youtube', url='https://youtube.com')]
])

cars = ['Vag', 'Mers', 'Bmw']


async def reply_cars():
    '''Достает данные из бд или списка и приводит к клавиатуре внизу'''
    keyboard = ReplyKeyboardBuilder()
    for car in cars:
        keyboard.add(KeyboardButton(text=car))
    return keyboard.adjust(2).as_markup() # Сколько кнопок в одном ряду


async def inline_cars():
    '''Достает данные из бд или списка и приводит к клавиатуре к кнопке вверху
    inline не можкт быть только текс'''
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url='https://youtube.com'))
    return keyboard.adjust(2).as_markup() # Сколько кнопок в одном ряду


async def inline_cars_2():
    '''Достает данные из бд или списка и приводит к клавиатуре к кнопке вверху
        inline не может быть только текс'''
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, callback_data=f'car_{car}'))
        return keyboard.adjust(2).as_markup()