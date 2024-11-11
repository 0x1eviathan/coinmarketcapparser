from pydantic import BaseModel 


class Settings(BaseModel): 
    token: str 
    database_url: str
    
    
settings = Settings(
    token='7411751245:AAFMS-P66w5fnISa2NN_Ck9izXhuPrUQMwE',
    database_url='sqlite+aiosqlite:///src/api/database/database.db'
)
