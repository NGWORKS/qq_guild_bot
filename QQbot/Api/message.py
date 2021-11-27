from typing import Any, Text

from ..Model.ApiModel.Massage import Message, MessageArk, MessageEmbed
from ..request import get, post


class SendMessage:
    """
    发送消息
    -------
    * 要求操作人在该子频道具有发送消息的权限。
    * 发送成功之后，会触发一个创建消息的事件。
    * `被动回复` 消息有效期为 `5 分钟`
    * `主动推送` 消息 每日每个子频道 `限 2 条`
    * 发送消息接口要求机器人需要链接到websocket gateway 上保持在线状态
    """

    def __init__(self, channel_id: Text) -> None:
        self.url = f"/channels/{channel_id}/messages"

    def __request(self, data: Any) -> Message:
        # print(self.url)
        res = post(self.url, json=data)
        # print(res)
        return Message(**res)

    def send_text(self, content: Text, msg_id: Text | None = None) -> Message:
        """
        发送文字
        -------
        文本内容，支持内嵌格式

        通过机器人向指定子频道发送一条文字消息。
        * 如果带了 `msg_id` 视为 `被动回复消息`，否则视为`主动推送消息`
        """
        data = {"content": content, "msg_id": msg_id}
        return self.__request(data)

    def send_embed(self, embed: MessageEmbed, msg_id: Text | None) -> Message:
        """
        发送 embed 消息
        -------
        embed 消息，一种特殊的 ark

        通过机器人向指定子频道发送一条embed消息。
        * 如果带了 `msg_id` 视为 `被动回复消息`，否则视为`主动推送消息`
        """
        data = {"embed": embed.dict(exclude_none=True), "msg_id": msg_id}
        return self.__request(data)

    def send_ark(self, ark: MessageArk, msg_id: Text | None) -> Message:
        """
        发送 ark(模板) 消息
        -------
        通过机器人向指定子频道发送一条ark 消息。
        * 如果带了 `msg_id` 视为 `被动回复消息`，否则视为`主动推送消息`
        """
        data = {"ark": ark.dict(exclude_none=True), "msg_id": msg_id}
        return self.__request(data)

    def send_image(self, image: Text, msg_id: Text | None) -> Message:
        """
        发送 图片消息
        -------
        通过机器人向指定子频道发送一个图片消息。
        * 如果带了 `msg_id` 视为 `被动回复消息`，否则视为`主动推送消息`
        """
        data = {"image": image, "msg_id": msg_id}
        return self.__request(data)

    def send_message(
        self,
        content: Text | None = None,
        embed: MessageEmbed | None = None,
        ark: MessageArk | None = None,
        image: Text | None = None,
        msg_id: Text | None = None
    ) -> Message:
        """
        发送复合类型消息
        ---------------
        发送一条可由`文字`、`embed`、`ark`、`图片` 组成的消息。
        * content, embed, ark, image 至少需要有一个字段，否则无法下发消息。
        * 如果带了 `msg_id` 视为 `被动回复消息`，否则视为`主动推送消息`
        """
        if content is None and embed is None and ark is None and image is None:
            ValueError("content, embed, ark, image 至少需要有一个字段")
        data = {"content": content, "embed": embed.dict(exclude_none=True),
                "ark": ark.dict(exclude_none=True), "image": image, "msg_id": msg_id}
        return self.__request(data)


def getMessage(channel_id: Text, message_id: Text) -> Message:
    """
    获取指定消息
    -----------
    查询`指定channel` 中一条`指定message_id`的信息
    """
    res = get(f"/channels/{channel_id}/messages/{message_id}")
    return Message(**res)
