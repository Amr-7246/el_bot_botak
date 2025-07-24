from fastapi import FastAPI, Request
from app.Routes.bot_router import router as bot_router
import httpx

from app.config import TELEGRAM_TOKEN, WEBHOOK_URL
from app.controller.bot_controller import handle_update
app = FastAPI()

app.include_router( bot_router , prefix='/bot')

@app.get("/")
def Start_app():
  print("Done Amr . . . Your app is running without any issues")
  return {"meesage" : "Done Amr . . . Your app is running without any issues" }

@app.post('/webhook')
async def telgrame_webhook(req: Request):
  update = await req.json()
  await handle_update(update)
  return {"ok" : True}

@app.on_event("startup") #! Fix the duprication
async def sen_your_app_url():
  telegram_url= f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook"
  Your_url = f"{WEBHOOK_URL}/webhook"
  async with httpx.AsyncClient() as clinet :
    await clinet.post(telegram_url , json={"url" : Your_url })