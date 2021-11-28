from typing import Text
from ..request import get
from ..Model.ApiModel import Channel
from pydantic import BaseModel

class all_channel(BaseModel):
    ch:list[Channel]

def get_channel(channel_id:Text) -> Channel:
    """获取子频道信息"""
    channel = get(f"/channels/{channel_id}")
    channel_info = Channel(**channel)
    return channel_info

def get_guilds_all_channel(guild_id:Text) -> list[Channel]:
    """获取频道下的子频道列表"""
    channel = get(f"/guilds/{guild_id}/channels")
    channel_info = all_channel(**{"ch":channel})
    return channel_info.ch