import httpx
from app.config import TELEGRAM_TOKEN

telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
async def send_message(chat_id: int, text: str, reply_markup: dict | None = None ):
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "reply_markup": reply_markup,
    }
    await httpx.AsyncClient().post(f"${telegram_url}/sendMessage", json= payload)
    
def build_keyboard(buttons: list[list[str]]) -> dict:
    return {"keyboard": [[{"text": btn} for btn in row] for row in buttons], "resize_keyboard": True}










# async def send_btn_structure(btn : list[list[str]]) : #& [ ["1st Year", "2nd Year", "3rd Year", "4th Year"] , [] ... ]
#     final_object =  "reply_markup" :  "keyboard":  
#     return 

# #& object: 
# #&    object : [ [{text:1st Year} , {text:2nd Year}] ] 
# #&    object : Ture