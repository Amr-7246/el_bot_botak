from fastapi import APIRouter, Body
from app.controller.bot_controller import show_courses , create_course, show_single_course, delete_course

router = APIRouter()

@router.get("/")
async def get_all():
  return await show_courses()

@router.post("/")
async def create(payload: dict = Body(...)): #! Ask
  return await create_course(payload)

@router.get("/{id}")
async def get_one(id: str):
  return await show_single_course(id)

@router.delete("/{id}")
async def remove(id: str):
  return await delete_course(id)
