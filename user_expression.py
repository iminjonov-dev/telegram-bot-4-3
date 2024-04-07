from aiogram.dispatcher import FSMContext


from keybords.default.buttons import user_main_menu
from keybords.inline.user import user_like_button_def, user_like_data, user_dislike_data
from loader import dp, db
from aiogram import types



@dp.callback_query_handler(user_like_data.filter(act='like'))
async def user_like_handler(call: types.CallbackQuery, callback_data: dict):
    photo_id = callback_data.get('photo_id')
    if db.chek_user_like(chat_id=call.message.chat.id, photo_id=photo_id):
        db.user_delete_like(chat_id=call.message.chat.id, photo_id=photo_id)
    else:
        db.user_like(chat_id=call.message.chat.id, photo_id=photo_id, is_like=True)
    likes, dislikes = db.get_photo_likes(photo_id)
    likes = likes[0][0]
    dislikes = dislikes[0][0]
    await call.message.edit_reply_markup(reply_markup=await user_like_button_def(likes, dislikes, photo_id))




@dp.callback_query_handler(user_dislike_data.filter(act='dislike'))
async def user_dislike_handler(call: types.CallbackQuery, callback_data: dict):
    photo_id = callback_data.get('photo_id')

    db.user_like(chat_id=call.message.chat.id, photo_id=photo_id, is_like=False)
    likes, dislikes = db.get_photo_likes(photo_id)

    likes = likes[0][0]
    dislikes = dislikes[0][0]
    await call.message.edit_reply_markup(reply_markup=await user_like_button_def(likes, dislikes, photo_id))