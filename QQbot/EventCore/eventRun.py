"""
这个程序文件实现了启动相关线程、注册监听器、自我修复的功能
>> 启动各项功能
>> 注册相应的事件监听器
>> 提供系统状态监测、各线程工作状态监测
"""

from threading import Thread,Event
import time


from .eventManager import EventManager
from .linstener import (ChannelListener, GuildListener, MemberListener,
                        MessageListener)
from ..log import logger
from ..config import BOT_APPID, BOT_TOKEN
from ..Ws.ws import wsc

from ..Api import getMe, getMeGuilds, shardsWss


token = f'Bot {BOT_APPID}.{BOT_TOKEN}'


class BOT:
    """
    BOT初始化
    -----------
    这个类实现了启动Bot各项功能，并且初始化事件监听器以及对于其他线程的监控。
    """

    def __init__(self) -> None:
        self.eventManager = EventManager()
        self.tasksDocter__active = True
        self._run_ws = []
        self.wsc = wsc

    def sendRequest(self):
        """
        发送初始化请求
        -------------
        发送初始化请求，查询Bot信息
        """
        logger.info(f"正在验证BOT信息")
        self.BotInfo = getMe()
        MeGuilds = getMeGuilds()
        guild = len(MeGuilds)
        logger.info(f"BOT:{self.BotInfo.username}（{self.BotInfo.id}）加入了频道{guild}个")
        sharddata = shardsWss()
        self.url = sharddata.url
        self.shard = sharddata.shards
        logger.info(
            f"消息地址：{sharddata.url}，推荐分片数：{sharddata.shards}，当前还可以链接{sharddata.session_start_limit.remaining}次")
        logger.info(f"Bot将在5秒后启动")
        time.sleep(5)

    def ListenerImport(self):
        """
        初始化监听器
        -----------
        这个方法实现了初始化监听器
        """
        logger.info("初始化监听器")
        guildlistener = GuildListener()
        self.eventManager.AddEventListener(
            "GUILD_CREATE", guildlistener.GUILD_CREATE)
        self.eventManager.AddEventListener(
            "GUILD_UPDATE", guildlistener.GUILD_UPDATE)
        self.eventManager.AddEventListener(
            "GUILD_DELETE", guildlistener.GUILD_DELETE)

        channellistener = ChannelListener()
        self.eventManager.AddEventListener(
            "CHANNEL_CREATE", channellistener.CHANNEL_CREATE)
        self.eventManager.AddEventListener(
            "CHANNEL_UPDATE", channellistener.CHANNEL_UPDATE)
        self.eventManager.AddEventListener(
            "CHANNEL_DELETE", channellistener.CHANNEL_DELETE)

        memberlistener = MemberListener()
        self.eventManager.AddEventListener(
            "GUILD_MEMBER_ADD", memberlistener.GUILD_MEMBER_ADD)
        self.eventManager.AddEventListener("GUILD_MEMBER_UPDATE",memberlistener.GUILD_MEMBER_UPDATE)
        self.eventManager.AddEventListener(
            "GUILD_MEMBER_REMOVE", memberlistener.GUILD_MEMBER_REMOVE)

        messagelistener = MessageListener()
        self.eventManager.AddEventListener(
            "AT_MESSAGE_CREATE", messagelistener.AT_MESSAGE_CREATE)

        self.eventManager.Start()
    
    def __taskDr(self):
        import time
        logger.info("正在初始化任务线程监控模块")
        event = Event()
        while not event.wait(5) and self.tasksDocter__active == True:
            for ws in self._run_ws:
                if not ws['ws'].is_alive():
                    logger.warning(f"ws- {ws['count']} 线程挂了,重开")
                    count = ws['count']
                    wsclient = wsc(self.url, token, self.eventManager, shard=[
                                   count, self.shard], s=ws['obj'].s, session=ws['obj'].session)
                    websocket = Thread(target=wsclient.run, name=f"WS-{count}")
                    websocket.setDaemon = True
                    websocket.start()
                    self._run_ws.remove(ws)
                    self._run_ws.append(
                        {"count": count, "ws": websocket, "obj": wsclient})

    def tasksDocter(self):
        """
        任务状态监控
        -----------
        在使用中难免出现错误导致线程退出，这个模块旨在监测退出的线程并且重启它们。
        """
        tsd = Thread(target=self.__taskDr, name=f"tasksDocter")
        tsd.setDaemon = True
        tsd.start()

    """
    功能模块初始化
    -------------
    这个方法对于Bot的一些常用功能进行初始化
    * wsgo 是保持维护一组 WebSocket链接 接受QQ的各项事件信息 
    * 它运行在一组个名为 `WS` 的线程
    """

    def run_ws(self):
        """
        开启ws分片
        -------
        根据api返回的分片数进行分片
        """
        logger.info("正在开启ws线程")
        for count in range(self.shard):
            logger.info(f'正在创建分片为{count}的ws线程')
            wsclient = wsc(self.url, token, self.eventManager,
                           shard=[count, self.shard])
            websocket = Thread(target=wsclient.run, name=f"WS-{count}")
            websocket.setDaemon = True
            self._run_ws.append(
                {"count": count, "ws": websocket, "obj": wsclient})
            websocket.start()
            logger.info(f'创建成功！线程名为 WS-{count}')
