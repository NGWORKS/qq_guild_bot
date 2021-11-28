from typing import List
from pydantic import BaseModel

class User(BaseModel):
    id:str
    username:str
    bot:bool

class Ready(BaseModel):
    version:str
    session_id:str
    user: User
    shard:list[int]