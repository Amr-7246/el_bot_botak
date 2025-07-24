import uvicorn
import os
from dotenv import load_dotenv
from typing import Optional, List
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

load_dotenv()

# ~ Start DB Connection 
class MongoDB:
    client: Optional[AsyncIOMotorClient] = None
    database: Optional[AsyncIOMotorDatabase] = None

mongodb = MongoDB()

async def connect_mongoDB() :
    """Create database connection"""
    mongodb.client = AsyncIOMotorClient(os.getenv('MONGO_CONECTION_URL'))
    mongodb.database = mongodb.client[os.getenv("DATABASE_NAME")]  # type: ignore
    try : 
        await mongodb.client.admin.command('ping')
        print('MongoDB connection happend without any errors Amr . . . ')
    except Exception as e :
        print(f'There is MongoDB connection error Amr . . . {e} ' )
        raise
# ~ End DB Connection 
# ~ Servre initialization
if "__name__" == "__main__" :
    uvicorn.run(
        "app.app:app",       
        host="0.0.0.0",       # Support All req
        port=5000,     
        reload=True  
    )
# ~ Servre initialization