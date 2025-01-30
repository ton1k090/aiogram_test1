from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext # для управления состояниями

router = Router() # Выполняет роль диспетчера


class Reg(StatesGroup):
    '''Класс для присвоения этих состояний пользователю'''
    name = State()
    number = State()




@router.message(CommandStart()) # Диспетчер ждет именно сообщение ( команду старт )
async def cmd_start(message: Message):
    '''Обработчик команды старо'''
    await message.reply(f'Hello \n{message.from_user.id} \n{message.from_user.first_name}',
                        reply_markup=kb.main) # Отвечать этому же пользователю и отпр клавиатуру


@router.message(Command('help')) # Диспетчер ждет именно /help
async def get_help(message: Message):
    '''Обработчик команды help'''
    await message.reply('This is command help', reply_markup=kb.settings) # Отвечать и отправлять клавиатуру к сообщению


@router.message(F.text == 'How car') # Диспетчер ждет именно - How are you
async def how_are_you(message: Message):
    '''Обработчик сообщения от пользолвателя'''
    await message.reply('OK', reply_markup=await kb.inline_cars()) # Отвечает ОК и добавляет клавиатуру


@router.message(F.photo) # Диспетчер ждет именно фото
async def get_photo(message: Message):
    '''Обработчик фото'''
    await message.answer(f'ID photo: {message.photo[-1].file_id}') # Вернет фото id (-1 это качество)


@router.callback_query(F.data == 'catalog') # Если пришло слово с калбэка каталог
async def catalog(callback: CallbackQuery): # Принимаем калбэк
    '''Функция обрабатывающая калбэк с инлайн кнопки каталог и
    выводящая новую инлайн клавиатуру'''
    await callback.answer('') # Чтобы кнопка перестала гореть после нажатия
    await callback.message.edit_text('This is catalog', reply_markup=await kb.inline_cars()) # Отвечаем сообщением при нажатии кнопки каталог


'''                    FSM машина состояний                 '''
@router.message(Command('reg')) # отлавливаем команду reg
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name) # переходим к другому состоянию
    await message.answer('Input you name')


@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text) # присваиваем имя name
    await state.set_state(Reg.number) # переходим к другому состоянию
    await message.answer('Input you number')


@router.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text) # присваиваем номер number
    data = await state.get_data() # получить введенные данные
    await message.answer(f'Success!!!\nName: {data["name"]}\nNumber: {data["number"]}') # выводим сообщение
    await state.clear() # Очищаем