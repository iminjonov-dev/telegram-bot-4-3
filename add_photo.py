# from aiogram.dispatcher import FSMContext
# from loader import dp, db
# from aiogram import types
# from states.user_reg import RegisterState
# from keybords.default.buttons import user_main_menu
#
# @dp.message_handler(commands="Rasm Joylash")
# async def user_upload_phot(message: types.Message,  state: FSMContext):
#     photo = db.get_random_photo(message.chat.id)
#     if photo is False:
#         text = "Hamma rasmlarni korib bo'ldingz"
#         await message.answer(text=text)
#     else:
#         if photo:
#             await state.update_data(photo_id=photo[0])
#             likes, dislikes = db.get_photo_likes(photo_id=photo[0])
#             likes = likes[0][0]
#             dislikes = dislikes[0][0]
#             await message.answer_photo(photo=photo[2],reply_markup=await user_like_button_def(likes, dislikes, photo[0])
#         else:
#              text = "Aktiv rasm majud emas!"
#              await message.answer(text=text)


from aiogram.dispatcher import FSMContext


from keybords.default.buttons import user_main_menu
from loader import dp, db
from aiogram import types



@dp.message_handler(text="Rasm joylash")
async def user_upload_photo(message: types.Message, state: FSMContext):
    photo = db.get_user_photo_by_chat_id(chat_id=message.chat.id)
    if photo:
        text = f"""
        Rasm alaqachon joylangan"""
        await message.answer_photo(photo=photo[2])
    else:
        text = "Iltimos yoqtirgan rasmingizni yuboring"
    await state.set_state("user-upload-photo")
    await message.answer(text=text)



@dp.message_handler(state="user-upload-photo", content_types=types.ContentTypes.PHOTO)
async def get_upload_photo(message: types.Message, state: FSMContext):
    await state.update_data(photo_id=message.photo[-1].file_id, chat_id=message.chat.id)
    data = await state.get_data()

    if db.add_photo(data):
        text = f"Rasm qo'shildi"
    else:
        text = "Rasm qo'shilmadi"
    await message.answer(text=text)
    await state.finish()