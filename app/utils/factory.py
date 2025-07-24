from fastapi import HTTPException
from beanie import Document
from typing import Type
from pymongo import ReturnDocument

async def get_entity(Model: Type[Document]):
    data = await Model.find_all().to_list()
    return data

async def get_entity_by_id(Model: Type[Document], id: str):
    result = await Model.get(id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return result

async def create_entity(Model: Type[Document], payload: dict):
    item = Model(**payload)
    await item.insert()
    return item

async def delete_entity(Model: Type[Document], id: str):
    doc = await Model.get(id)
    if not doc:
        raise HTTPException(status_code=404, detail="Not found")
    await doc.delete()
    return {"message": "Deleted"}
