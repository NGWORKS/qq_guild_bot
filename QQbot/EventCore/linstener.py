"""
监听器
>> 用于监听各种事件并响应
>> 用于消费ws传递的各种事件
"""

from ..log import logger

class GuildListener:
    """
    频道事件
    -------
    用于监听-响应频道发生变动时的三种事件：
    * GUILD_CREATE 机器人被加入到某个频道的时候
    * GUILD_UPDATE 频道信息变更
    * GUILD_DELETE 频道被解散 或 机器人被移除

    收到的事件信息应该是一个频道对象(Guild)
    """
    def GUILD_CREATE(self,event):
        """
        GUILD_CREATE 监听器
        ------------------
        用于监听并响应机器人被添加到某个频道的的事件信息。
        """
        logger.info(f"机器人被添加到了频道：{event.id}")
        # 做点什么 加入数据库 主动发送欢迎语料

    def GUILD_UPDATE(self,event):
        """
        GUILD_UPDATE 监听器
        ------------------
        用于监听并响应频道信息变更的事件信息。
        """
        logger.info(f"频道：{event.id} 信息发生变动")
        # 做点什么 静默更新数据库信息

    def GUILD_DELETE(self,event):
        """
        GUILD_DELETE 监听器
        ------------------
        用于监听并响应频道信息变更的事件信息。
        """
        logger.info(f"频道：{event.id} 移除了机器人或者频道被解散")
        # 做点什么 删数据


    
class ChannelListener:
    """
    子频道事件
    ----------
    用于监听-响应子频道发生变动时的三种事件：
    * CHANNEL_CREATE 子频道被创建
    * CHANNEL_UPDATE 子频道信息变更
    * CHANNEL_DELETE 子频道被删除

    收到的事件信息应该是一个子频道对象(Channel)
    """

    def CHANNEL_CREATE(self,event):
        """
        CHANNEL_CREATE 监听器
        ------------------
        用于监听并响应子频道被创建的事件信息。
        """
        logger.info(f"新的子频道：{event.id}被创建")
        # 做点什么 加入数据库
    
    def CHANNEL_UPDATE(self,event):
        """
        CHANNEL_UPDATE 监听器
        ------------------
        用于监听并响应子频道信息变更的事件信息。
        """
        logger.info(f"子频道：{event.id}被更新")
        # 做点什么 修改数据库
    
    def CHANNEL_DELETE(self,event):
        """
        CHANNEL_DELETE 监听器
        ------------------
        用于监听并响应子频道被删除的事件信息。
        """
        logger.info(f"子频道：{event.id}被删除")
        # 做点什么 修改数据库

class MemberListener:
    """
    频道成员事件
    -----------
    用于监听-响应频道成员的两种事件信息：
    * GUILD_MEMBER_ADD 新用户加入频道
    * GUILD_MEMBER_REMOVE 用户离开频道

    收到的事件信息应该是一个用户在频道中的信息(MemberWithGuildID)
    """
    def GUILD_MEMBER_ADD(self,event):
        """
        GUILD_MEMBER_ADD 监听器
        ------------------
        用于监听并响应新用户加入频道的事件信息。
        """
        logger.info(f"用户：{event.name}加入")
        # 做点什么 加入数据库 欢迎
    
    def GUILD_MEMBER_UPDATE(self,event):
        logger.info(f"用户：{event.name} 信息发生变动")
        # 做点什么 加入数据库 欢迎
    
    def GUILD_MEMBER_REMOVE(self,event):
        """
        GUILD_MEMBER_REMOVE 监听器
        ------------------
        用于监听并响应用户离开频道的事件信息。
        """
        logger.info(f"用户：{event.name} 退出")
        # 做点什么 删除数据库

class MessageListener:
    """
    消息事件
    -------
    用于监听-响应消息的一种事件信息：
    * AT_MESSAGE_CREATE 用户发送消息，并且@当前机器人

    收到的事件信息应该是一消息对象(Message)
    """
    def AT_MESSAGE_CREATE(self,event):
        """
        AT_MESSAGE_CREATE 监听器
        ------------------
        用于监听并响应用户发送消息，并且@当前机器人的事件信息。
        """
        logger.info(f"收到频道 {event.guild_id} 内 子频道 {event.channel_id} 用户 {event.author.username}（{event.author.id}）的消息 {event.content}")
        # 做点什么


# class AudioListener:
#     """
#     音频事件
#     -------
#     用于监听-响应音频的一种事件信息：
#     * AUDIO_START 音频开始播放时
#     * AUDIO_FINISH 音频播放结束时
#     * AUDIO_ON_MIC 机器人上麦时
#     * AUDIO_OFF_MIC 机器人下麦时

#     收到的事件信息应该是音频动态对象(AudioAction)
#     """
#     def __init__(self,ws) -> None:
#         self.ws = ws

#     def send(self,message):
#         try:
#             self.ws.send(json.dumps(message))
#         except:
#             logger.info('ws推送失败，请检查网络连接')

#     # 这个不做

    
    