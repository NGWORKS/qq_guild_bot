from typing import Text
from ..request import get
from ..Model.ApiModel import Member

def get_memder(guild_id:Text,user_id:Text) -> Member:
    """
    获得成员信息
    -----------
    获取`指定频道`中的`指定成员`信息。
    """
    member = get(f"/guilds/{guild_id}/members/{user_id}")
    member_info = Member(**member)
    return member_info