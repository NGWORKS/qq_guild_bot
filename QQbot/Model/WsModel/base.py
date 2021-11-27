from typing import Optional, Union

from pydantic import BaseModel

from ..ApiModel import AudioAction, Channel, Guild, MemberWithGuildID, Message
from .authorization import Authorization
from .ready import Ready


class hb(BaseModel):
    heartbeat_interval: int


class Load(BaseModel):
    """
    负载
    ----
    ws消息主体
    """
    op: int  # op 指的是opcode
    d: Optional[Union[int, str, Ready, hb, Authorization, Guild, Message,
                      Channel, MemberWithGuildID, AudioAction]]   # 事件内容
    s: Optional[int]   # 消息序列号，发送心跳时携带最新的
    t: Optional[str]   # 事件类型
