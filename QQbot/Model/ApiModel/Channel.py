from typing import Optional
from enum import Enum
from pydantic import BaseModel


class Channel(BaseModel):
    """子频道"""
    id:	str         # 子频道id
    guild_id: str   # 频道id
    name: str       # 子频道名
    type: int       # 子频道类型 ChannelType
    sub_type: int   # 子频道子类型 ChannelSubType
    position: int   # 排序，必填，而且不能够和其他子频道的值重复
    parent_id: str  # 分组 id
    owner_id: str   # 创建人 id


class ChannelType(str, Enum):
    """子频道类型枚举类"""
    text = 0	# 文字子频道
    voice = 2	# 语音子频道
    # 4	子频道分类
    live = 10005	#直播子频道

class ChannelSubType(str, Enum):
    """子频道子类型"""
    chat = 0	# 闲聊
    notice = 1	#公告
    introduction = 2	#攻略
    game = 3	# 开黑
