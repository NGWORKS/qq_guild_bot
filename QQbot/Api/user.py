from typing import Any, Text

from ..Model.ApiModel import User, Guild
from ..request import get
from pydantic import BaseModel

class Guildlist(BaseModel):
    hs:list[Guild]


def getMe() -> User:
    """
    获取当前用户信息
    --------------
    
    """
    res = get("/users/@me")
    return User(**res)


def getMeGuilds() -> list[Guild]:
    """获取当前用户加入的频道列表"""
    res = get("/users/@me/guilds")
    data = Guildlist(**{"hs":res})
    return data.hs
