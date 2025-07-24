from app.models.bot_user_model import User

async def save_user_data(chat_id , data):
    user = await User.find_one(User.chat_id == chat_id)
    
    if user:
        await user.set(data)
        return user
    else:
        new_user = User(chat_id=chat_id, **data)
        await new_user.insert()
        return new_user
    
    
async def get_content_by_subject(year: str, subject: str):
    # You can structure this however you'd like — static file, DB, CMS, etc.
    content_map = {
        "1st Year": {
            "Math": ["https://youtu.be/example1", "https://youtu.be/example2"],
            "Programming": ["https://youtu.be/prog1"]
        }
    }
    return content_map.get(year, {}).get(subject, [])
