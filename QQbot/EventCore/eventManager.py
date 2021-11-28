# -*- coding: utf-8 -*-
"""
这个程序文件实现了事件驱动的基本功能，并且为事件驱动建立了基本的操作方法
"""
from os import name
from queue import Queue, Empty
from threading import *
class EventManager:
    def __init__(self):
        """初始化事件管理器"""
        # 事件对象列表
        self.__eventQueue = Queue()
        # 事件管理器开关
        self.__active = False
        # 事件处理线程
        self.__thread = Thread(target = self.__Run,name="EventManager")
        self.count = 0
        # 这里的__handlers是一个字典，用来保存对应的事件的响应函数
        # 其中每个键对应的值是一个列表，列表中保存了对该事件监听的响应函数，一对多
        self.__handlers = {}

    def __Run(self):
        """引擎运行"""
        while self.__active == True:
            try:
                # 获取事件的阻塞时间设为1秒
                event = self.__eventQueue.get(block = True, timeout = 1)  
                self.__EventProcess(event)
            except Empty:
                pass
            self.count += 1

    def __EventProcess(self, event):
        """处理事件"""
        # 检查是否存在对该事件进行监听的处理函数
        if event.type_ in self.__handlers:
            # 若存在，则按顺序将事件传递给处理函数执行
            for handler in self.__handlers[event.type_]:
                t = Thread(target=handler,args=(event.dict["artical"],),name=f"mi_{self.count}")
                t.start()
        self.count += 1

    def Start(self):
        """启动"""
        # 将事件管理器设为启动
        self.__active = True
        # 启动事件处理线程
        self.__thread.start()
        self.count += 1

    def Stop(self):
        """停止"""
        # 将事件管理器设为停止
        self.__active = False
        # 等待事件处理线程退出
        self.__thread.join()
        self.count += 1

    def AddEventListener(self, type_, handler):
        """绑定事件和监听器处理函数"""
        # 尝试获取该事件类型对应的处理函数列表，若无则创建
        try:
            handlerList = self.__handlers[type_]
        except KeyError:
            handlerList = []
            self.__handlers[type_] = handlerList
            
        if handler not in handlerList:
            handlerList.append(handler)
        # print(self.__handlers)
        self.count += 1
        
    def RemoveEventListener(self, type_, handler):
        """移除监听器的处理函数"""
        try:
            handlerList = self.handlers[type_]
            # 如果该函数存在于列表中，则移除
            if handler in handlerList:
                handlerList.remove(handler)
            # 如果函数列表为空，则从引擎中移除该事件类型
            if not handlerList:
                del self.handlers[type_]
        except KeyError:
            pass
        self.count += 1

    def SendEvent(self, event):
        """发送事件，向事件队列中存入事件"""
        self.__eventQueue.put(event)
        self.count += 1

class Event:
    def __init__(self, type_=None):
        self.type_ = type_      # 事件类型
        self.dict = {}          # 字典用于保存具体的事件数据