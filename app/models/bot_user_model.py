from pydantic import BaseModel #! Ask About BaseModel & data_model structuer
from beanie import Document

# class User(BaseModel) as Document : #! Ask About the defrance between BaseModel & Document
class User(Document) :
    chat_id: int 
    year: str | None = None
    subject: str | None = None
    step: str = "year"


# from beanie import Document, Indexed
# from pydantic import Field, BaseModel, validator
# from datetime import datetime
# from typing import Optional, List

# # Shared Input Schema: for create/update endpoints
# class CourseIn(BaseModel):
#     title: str = Field(..., min_length=3, max_length=100)
#     description: Optional[str] = Field(None, max_length=1000)
#     duration: int = Field(..., ge=1, description="Duration in hours")
#     price: float = Field(..., ge=0, description="Course price in USD")
#     instructor: str = Field(..., min_length=3)
#     tags: List[str] = Field(default_factory=list)

#     @validator("tags", each_item=True)
#     def non_empty_tags(cls, v):
#         assert v.strip(), "Tags must not be empty"
#         return v

# # Document model = maps to MongoDB collection
# class Course(Document):
#     title: Indexed(str)  # type: ignore # indexed for faster search
#     description: Optional[str]
#     duration: int
#     price: float
#     instructor: str
#     tags: List[str]
#     created_at: datetime = Field(default_factory=datetime.utcnow)
#     updated_at: datetime = Field(default_factory=datetime.utcnow)

#     class Settings:
#         name = "courses"

#     # Run automatically before saving
#     def update_timestamp(self):
#         self.updated_at = datetime.utcnow()

#     # Pydantic config
#     class Config: # type: ignore
#         schema_extra = {
#             "example": {
#                 "title": "Intro to FastAPI",
#                 "description": "Learn to build APIs with Python",
#                 "duration": 10,
#                 "price": 49.99,
#                 "instructor": "Jane Doe",
#                 "tags": ["python", "backend"]
#             }
#         }
