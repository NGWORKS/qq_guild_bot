from typing import Optional
from pydantic import BaseModel, Field


class Properties(BaseModel):
    """
    设备信息
    -------
    告知服务端你的Bot系统、实现、设备
    """
    os: int = Field(alias='$os')
    browser: str = Field(alias='$browser')
    device: str = Field(alias='$device')

class Authorization(BaseModel):
    """
    鉴权信息
    -------
    包含token的鉴权信息
    """
    token: str
    intents: int
    shard: list[int]
    properties: Optional[Properties]

class Resumed(BaseModel):
    """
    重连鉴权
    -------
    进行重连鉴权
    """
    token: str
    session_id: str
    seq: int

