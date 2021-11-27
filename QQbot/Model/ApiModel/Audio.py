from pydantic import BaseModel

from QQbot.config import BOT_TOKEN


class STATUS():
    START = 0  # 开始播放操作
    PAUSE = 1  # 暂停播放操作
    RESUME = 2  # 继续播放操作
    STOP = 3   # 停止播放操作


class AudioAction(BaseModel):
    guild_id: str  # 频道id
    channel_id: str  # 子频道id
    audio_url: str  # 音频数据的url status为0时传
    text: str  # 状态文本（比如：简单爱-周杰伦），可选，status为0时传，其他操作不传

class AudioControl(BaseModel):
    audio_url: str  # 音频数据的url status为0时传
    text: str  # 状态文本（比如：简单爱-周杰伦），可选，status为0时传，其他操作不传
    status: int # 播放状态，参考 STATUS