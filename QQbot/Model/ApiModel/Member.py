"""
成员对象(Member)
--------------
成员对象是一个频道成员应该有的数据结构，主要是由 ``Member`` 组成
"""
from typing import Optional

from pydantic import BaseModel

from .User import User


class Member(BaseModel):
    """
    成员对象
    -------
    成员对象是一个频道成员应该有的的数据结构::
    * ``user``	``User``	``用户基础信息``
    * ``nick``	``string``	``用户在频道内的昵称``
    * ``roles``	``string 数组``	``用户在频道内的身份组ID, 默认值可参考DefaultRoles``
    * ``joined_at``	``iISO8601 timestamp``	``用户加入频道的时间``

    """
    user: Optional[User]
    nick: Optional[str]
    roles: list[str]
    joined_at: str


class MemberWithGuildID(BaseModel):
    """
    带有频道id成员对象
    ----------------
    成员对象是一个频道成员应该有的的数据结构:
    * ``guild_id`` ``str``    ``频道id``
    * ``user``	``User``	``用户基础信息``
    * ``nick``	``string``	``用户在频道内的昵称``
    * ``roles``	``string 数组``	``用户在频道内的身份组ID, 默认值可参考DefaultRoles``
    * ``joined_at``	``iISO8601 timestamp``	``用户加入频道的时间``
    """
    guild_id: str
    user: User
    nick: str
    roles: list[str]
    joined_at: str
