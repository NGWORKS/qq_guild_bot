# 概述
本库是基于QQ频道机器人而开发的一个`初步封装`了api接口和ws接口，目前可以实现简单的事件监听与交互。
> 注意 本项目还在开发中 如果您只能在 `/hegugu-ng/qq_gulid_bot` 仓库看到完整项目时，说明这个项目 **还不能直接用于生产环境！**

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
BotInof = getMe()
print(BotInof)
```
> 返回未经特殊说明均为 `pydantic` 对象

**返回：**
```
id='11810040378067637410' username='禾咕咕-测试中' avatar='http://thirdqq.qlogo.cn/g?b=oidb&k=G4icjGB7udGG1TArrwKId1A&s=100&t=1637758329' bot=None union_openid=None union_user_account=None
```
#### 查看当前登录BOT加入的频道
```python
MeGuilds = getMeGuilds()
print("加入了频道",len(MeGuilds),"个")
print(MeGuilds)
```
**返回：**
```
id='11810040378067637410' username='禾咕咕-测试中' avatar='http://thirdqq.qlogo.cn/g?b=oidb&k=G4icjGB7udGG1TArrwKId1A&s=100&t=1637758329' bot=None union_openid=None union_user_account=None
```
### 频道相关
对频道进行操作

#### 获取指定频道信息
```python
guild_info = get_guild_info(4930494858376070938)
print(guild_info)
```
**返回：**

```
id='4930494858376070938' name='机器人禾咕咕' icon=None owner_id='9802601117268679552' owner=False op_user_id=None member_count=24 max_members=1200 description='ng' joined_at=None union_world_id=None union_org_id=None
```
> 百看不如一试，剩下的api你可以在 `test.ipynb` 中交互性的体验！

![在笔记本中交互体验所有api](/img/ex_3.png)


## 更多例子？
`所有的API` 参考均见 `test.ipynb`

> 直接运行 `run.py`，可以快速观察工作流程

![效果图](/img/ex_1.jpg)

如果你正确配置机器人并且启动程序，那么恭喜你，你将获得一个笨蛋机器人

> 注意：**发出这段话需要联系qq官方，关闭语料验证**

## 醒目的输出

当然，本项目也有醒目的日志输出，你可以一目了然的观察到目前的状态！

![效果图](/img/ex_2.png)

