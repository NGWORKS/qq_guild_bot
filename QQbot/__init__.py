# -*- coding: utf-8 -*-
"""
NGWORKS QQ频道机器人脚手架
-
现在还都不是异步，等摸明白了会改。
使用::
>>> import QQbot

>>> bot = QQbot.BOT()
>>> bot.sendRequest()
>>> bot.ListenerImport()
>>> bot.run_ws()
>>> bot.tasksDocter()
"""
from .Api import (AudioControl, SendMessage, add_roles_members, delete_roles,
                  delete_roles_members, establish_roles, get_channel,
                  get_guild_info, get_guilds_all_channel, get_memder,
                  get_roles, getMe, getMeGuilds, getMessage, getWss,
                  modify_roles, shardsWss)
from .Model.ApiModel.Roles import Filter,Info
from .log import logger
from .EventCore import BOT
