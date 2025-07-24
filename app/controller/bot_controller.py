from pydoc import text
from app.controller.send_telegram_requirments import build_keyboard, send_message
from app.models.bot_user_model import User
from app.models.save_user_data import get_content_by_subject, save_user_data
from app.utils.factory import get_entity_by_id


async def handle_update(update: dict):
    message = update.get("message")
    if not message : return
    chat_id = update['chat']['id']
    user_message = update['text'] 
    user = await get_entity_by_id(User , chat_id)
    
    #& Step 1: Year Selected
    if user_message == '/start' or not user : 
        await save_user_data(chat_id, {"step": "year"} )
        buttons = [["1st Year", "2nd Year", "3rd Year", "4th Year"]]
        await send_message(chat_id, 'Welcome! Choose your year', build_keyboard(buttons) )
        return
    
    #& Step 2: Year Selected
    if user.step == "year":
        await save_user_data(chat_id, {"year": user_message, "step": "subject"})
        subject_buttons = [["Math", "Physics"], ["Programming", "Electronics"]]  # Customize per year
        await send_message(chat_id, f" You selected <b>{user_message}</b>.\nNow pick your subject:", build_keyboard(subject_buttons))
        return

    #& Step 3: Subject Selected
    if user.step == "subject":
        await save_user_data(chat_id, {"subject": user_message, "step": "done"})
        content_links = await get_content_by_subject(user.year, user_message)
        
        if not content_links:
            await send_message(chat_id, " No content available yet.")
        else:
            await send_message(chat_id, f" Here are your course videos for <b>{user_message}</b>:\n\n" + "\n".join(content_links))

        await send_message(chat_id, " You can type /start again to restart.")
