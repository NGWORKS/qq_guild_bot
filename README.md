# 概述
本库是基于QQ频道机器人而开发的一个`初步封装`了api接口和ws接口，目前可以实现简单的事件监听与交互。
> 注意 本项目还在开发中 如果您只能在 /hegugu-ng/qq_gulid_bot 仓库看到完整项目时，说明这个项目 **还不能直接用于生产环境！**

**目前已知的问题：**
* 全部都用同步写的，没有异步，但多线程
* 对ws的断开原因没有分析，只会重连
* 因为懒，完全没有写音频方面
* 对于发消息因为没有申请ARK能力没有进行测试。
## 谁应该阅读这个文档

开发qq频道机器人的开发者，在阅读文档时应当对机器人的功能与接入方法有一定了解。

## 使用的前置条件

* 已经阅读完官方文档，并且对频道机器人的各项功能有明确的认识。
* 申请了开发者账号。
* 有一定python基础
* 安装了依赖
## 依赖
python 3.6 +

```shell
pip install pydantic
pip install requests
pip install websocket-client
```
## 使用
**填写自己的bot信息**
见 `/QQbot/config.py`
> 这个是临时方法，后续会进行破坏性更新

这是最快速跑起来的方法

```python
from  QQbot import BOT,SendMessage

bot = BOT()
bot.sendRequest()
bot.ListenerImport()
bot.run_ws()
bot.tasksDocter()
```
> 关于事件驱动的核心和注册事件的方法，可以参考 `/QQbot/EventCore`

## 使用api
**导包**
```python
from QQbot import (AudioControl, SendMessage, add_roles_members,
                       delete_roles, delete_roles_members, establish_roles,
                       get_channel, get_guild_info, get_guilds_all_channel,
                       get_memder, get_roles, getMe, getMeGuilds, getMessage,
                       getWss, modify_roles, shardsWss)
```
### 当前用户信息获取
这一类接口可以获取到用户Bot的信息，如botID、昵称，加入的频道、在频道中的身份等。

#### 查看当前登录的Bot信息
该接口可以获取当前bot的id、昵称、头像

```python
# 查看当前登录用户
BotInof = getMe()
print(BotInof)
```
> 返回一个pydantic 对象

id='11810040378067637410' username='禾咕咕-测试中' avatar='http://thirdqq.qlogo.cn/g?b=oidb&k=G4icjGB7udGG1TArrwKId1A&s=100&t=1637758329' bot=None union_openid=None union_user_account=None

## 更多例子？
所有api的参考均见 test.ipynb

直接运行 run.py
可以快速观察工作流程

