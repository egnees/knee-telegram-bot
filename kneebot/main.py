from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from knee_bot_token import TOKEN

import random

knee_bot = Bot(token=TOKEN)
dispatcher = Dispatcher(knee_bot)

random_photos_links = [
    'https://mobimg.b-cdn.net/v3/fetch/62/62c4d2fbacf26142f5b81cdf7f683184.jpeg',
    'https://kartinkin.net/uploads/posts/2022-02/1645951415_6-kartinkin-net-p-prizrachnii-gonshchik-kartinki-7.jpg',
    'https://cdn.fishki.net/upload/post/201505/29/1549063/7_01.jpg',
    'https://avafka.ru/wp-content/uploads/2019/08/absoliutnyi-chieloviek-pauk.jpg',
    'https://sun9-22.userapi.com/impg/AuB7vMQmt6kqENLmi3GMfuuB_9lGA-0TVtwOfw/Y0c3i4aqEUU.jpg?size=604x593&quality=96&sign=f98a2899df51f6d2c978f5be279bca4f&type=album',
    'https://cdn.fishki.net/upload/post/2020/05/26/3326862/d4debe2a3dee56a55693a202be7c421c.png',
    'https://mobimg.b-cdn.net/v3/fetch/82/825248da236e6723ec300fbdd5cad5a5.jpeg',
    'https://i.pinimg.com/originals/0e/b3/0d/0eb30d7567da2432ad711a5bcf5f6a87.jpg',
    'https://i.ytimg.com/vi/T0XIRTdiLpQ/maxresdefault.jpg'
]

@dispatcher.message_handler(commands=['start'])
async def start_knee_bot(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name} {message.from_user.last_name}'
                         f'!. Я твой друг, KneeBot, меня создал @Egnees.')


@dispatcher.message_handler(commands=['help'])
async def help_knee_bot(message: types.Message):
    await message.answer('/start чтобы начать\n'
                         + '/help чтобы получить помощь\n'
                         + '/my_picture чтобы посмотреть свою аву\n'
                         + '/service чтобы увидеть все изнутри\n'
                         + '/random_picture чтобы посмотреть рандомную картинку\n')


@dispatcher.message_handler(commands=['service'])
async def service_knee_bot(message: types.Message):
    await message.answer(message)


@dispatcher.message_handler(commands=['my_picture'])
async def my_picture_knee_bot(message: types.Message):
    profile_pictures = await dispatcher.bot.get_user_profile_photos(message.from_user.id)
    await message.answer_photo(dict((profile_pictures.photos[0][0])).get("file_id"))


@dispatcher.message_handler(commands=['random_picture'])
async def random_picture_knee_bot(message: types.Message):
    i = random.randint(0, len(random_photos_links) - 1)
    print('sending photo ' + str(i))
    await message.answer_photo(random_photos_links[i])

if __name__ == '__main__':
    executor.start_polling(dispatcher)