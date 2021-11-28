from typing import Text
from ..request import get
from ..Model.ApiModel import Guild



def get_guild_info(guild_id:Text):
    """获取频道信息"""
    res = get(f"/guilds/{guild_id}")
    guild_info = Guild(**res)
    return guild_info