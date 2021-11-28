from typing import Any, Text

from ..request import post


class AudioControl:
    """
    音频控制
    -------
    仅限音频类机器人才能使用，后续会根据机器人类型自动开通接口权限，现如需调用，需联系平台申请权限；

    """
    def __init__(self, channel_id: str, audio_url: str, text: str | None = "邀您共赏音乐") -> None:
        self.channel_id = channel_id
        self.audio_url = audio_url
        self.text = text

    def __request(self,data:Any):
        res = post(f"/channels/{self.channel_id}/audio",json=data)
        return res
    
    def start(self):
        """
        开始播放
        -------
        开始播放音乐
        """
        data = {"audio_url":self.audio_url,"text":self.text,"status":0}
        return self.__request(data)

    def pause(self):
        """
        暂停播放
        -------
        暂停播放音乐
        """
        data = {"status":1}
        return self.__request(data)
    
    def resume(self):
        """
        继续播放
        -------
        继续播放音乐
        """
        data = {"status":2}
        return self.__request(data)
    
    def stop(self):
        """
        停止播放
        -------
        停止播放音乐
        """
        data = {"status":3}
        return self.__request(data)
