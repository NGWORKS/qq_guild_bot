# 概述
本库是基于QQ频道机器人而开发的一个`初步封装`了api接口和ws接口，目前可以`实现简单的`事件监听与交互。

> **注意:** 本项目还在开发中 如果您只能在 `/hegugu-ng/qq_gulid_bot` 仓库看到完整项目时，说明这个项目 **还不能直接用于生产环境！**

**受限于本人非专业的编码能力，项目中会存在诸多不合理的地方甚至错误的地方，如果您有发现，还望多多指教**

**目前已知的问题：**
* 全部都用同步写的，没有异步，但多线程
* 对ws的断开原因没有分析，只会重连
* 因为懒，完全没有写音频方面
* 对于发消息因为没有申请ARK能力没有进行测试。
* 事件绑定的操作比较反人类，但是可以用
* 对于发送主动消息需要审核的时候依然按照返回massage对象看待，会触发数据结构不匹配的错误

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
pip install colorlog
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

## 小贴士
几乎所有函数与类都有代码文档和类型提示，你可以像下面一样使用
![演示视频](/img/ex.gif)


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
加入了频道 1 个
[Guild(id='4930494858376070938', name='机器人禾咕咕', icon='https://groupprohead-76292.picgzc.qpic.cn/52603021637757906/100?t=1637757908022', owner_id=None, owner=False, op_user_id=None, member_count=None, max_members=None, description=None, joined_at=None, union_world_id=None, union_org_id=None)]
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
#### 获取指定频道身份组
```python
roleslist = get_roles(4930494858376070938)
print(roleslist)
```
**返回：**
```
guild_id='4930494858376070938' roles=[Role(id='4', name='创建者', color=4294927682, hoist=1, number=1, member_limit=1), Role(id='2', name='管理员', color=4280276644, hoist=1, number=5, member_limit=50), Role(id='5', name='子频道管理员', color=4282814975, hoist=1, number=0, member_limit=50), Role(id='10030939', name='万能的bot', color=4285110493, hoist=0, number=1, member_limit=2000), Role(id='10037002', name='测试', color=4285110493, hoist=0, number=0, member_limit=2000), Role(id='1', name='普通成员', color=4286151052, hoist=0, number=0, member_limit=1000)] role_num_limit='30'
```
#### 获取一个频道下的所有子频道
```python
all_channel = get_guilds_all_channel(4930494858376070938)
print(all_channel)
```
**返回：**

```
[Channel(id='1592769', guild_id='4930494858376070938', name='bot试炼场', type=4, sub_type=0, position=5, parent_id='0', owner_id='0'), Channel(id='1592782', guild_id='4930494858376070938', name='新功能孵化器', type=4, sub_type=0, position=6, parent_id='0', owner_id='0'), Channel(id='1554677', guild_id='4930494858376070938', name='很高兴遇见你', type=4, sub_type=0, position=2, parent_id='0', owner_id='0'), Channel(id='1554678', guild_id='4930494858376070938', name='话题讨论', type=4, sub_type=0, position=3, parent_id='0', owner_id='0'), Channel(id='1554680', guild_id='4930494858376070938', name='频道管理', type=4, sub_type=0, position=4, parent_id='0', owner_id='0'), Channel(id='1554681', guild_id='4930494858376070938', name='', type=4, sub_type=0, position=1, parent_id='0', owner_id='0'), Channel(id='1587214', guild_id='4930494858376070938', name='botの奇妙发言', type=0, sub_type=0, position=2, parent_id='1592769', owner_id='0'), Channel(id='1592778', guild_id='4930494858376070938', name='功能更新日历', type=10006, sub_type=0, position=1, parent_id='1592782', owner_id='0'), Channel(id='1554672', guild_id='4930494858376070938', name='😃闲聊大厅', type=0, sub_type=0, position=2, parent_id='1554678', owner_id='0'), Channel(id='1554675', guild_id='4930494858376070938', name='🔒管理员议事厅', type=0, sub_type=0, position=1, parent_id='1554680', owner_id='0'), Channel(id='1555076', guild_id='4930494858376070938', name='机器人测试', type=0, sub_type=0, position=1, parent_id='1592769', owner_id='0'), Channel(id='1554676', guild_id='4930494858376070938', name='🚪小黑屋', type=0, sub_type=0, position=2, parent_id='1554680', owner_id='0'), Channel(id='1592779', guild_id='4930494858376070938', name='产品锦鲤大投票', type=10006, sub_type=0, position=2, parent_id='1592782', owner_id='0'), Channel(id='1592790', guild_id='4930494858376070938', name='建议', type=10007, sub_type=0, position=1, parent_id='1554681', owner_id='0'), Channel(id='1554668', guild_id='4930494858376070938', name='📝重要通知', type=0, sub_type=1, position=1, parent_id='1554677', owner_id='0'), Channel(id='1554670', guild_id='4930494858376070938', name='🧐今日大事', type=0, sub_type=2, position=2, parent_id='1554677', owner_id='0'), Channel(id='1554671', guild_id='4930494858376070938', name='🥳欢迎萌新', type=0, sub_type=0, position=1, parent_id='1554678', owner_id='0')]
```

#### 获取指定子频道信息
```python
channel_info = get_channel(1554668)
print(channel_info)
```
**返回：**
```
id='1554668' guild_id='4930494858376070938' name='📝重要通知' type=0 sub_type=1 position=2 parent_id='1554677' owner_id='0'
```
### 身份组相关
#### 新建身份组
身份组操作需要导入  `Filter` 与 `Info` 两个类，本示例只导入一次供参考，其余部分视为已经导入
```python
from QQbot import Filter,Info
filter = Filter(name=1,color=1,hoist=1)
info = Info(name="BOT钦定~",color=4285110493,hoist=1)
new_roles = establish_roles(guild_id=4930494858376070938,filter=filter,info=info)
new_roles_id = new_roles.role_id
print(new_roles)
```
**返回：**

```
role_id='10037579'
```

#### 修改身份组
```python
new_info = Info(name="BOT在修改~",color=4285110493,hoist=1)
modify_roles(guild_id=4930494858376070938,role_id=new_roles_id,filter=filter,info=new_info)
```
**返回：**

```
role_and_guild_id(guild_id='4930494858376070938', role_id='10037579')
```
#### 删除身份组
```python
delete_roles(guild_id=4930494858376070938,role_id=new_roles_id)
```

**返回：**
布尔值

```
True
```
#### 查询成员在频道中的身份组
```python
get_memder(guild_id=4930494858376070938,user_id=11810040378067637410)
```
**返回：**

```
Member(user=User(id='11810040378067637410', username='禾咕咕-测试中', avatar='http://thirdqq.qlogo.cn/g?b=oidb&k=G4icjGB7udGG1TArrwKId1A&s=100&t=1637758329', bot=True, union_openid=None, union_user_account=None), nick='', roles=['1'], joined_at='2021-11-24T20:56:18+08:00')
```
#### 将指定成员移动到指定身份组
```python
add_roles_members(guild_id=4930494858376070938,user_id=11810040378067637410,role_id=10030939)
```
**返回：**
布尔值

```
True
```
#### 将指定成员从指定身份组中移除
```python
delete_roles_members(guild_id=4930494858376070938,user_id=11810040378067637410,role_id=10030939)
```
**返回：**
布尔值

```
True
```
### ws网关相关
#### 获取ws地址时返回分片信息与限制信息
```python
shardsWss()
```
**返回：**
```
Shards(url='wss://api.sgroup.qq.com/websocket', shards=1, session_start_limit=SessionStartLimit(total=1000, remaining=993, reset_after=82975041, max_concurrency=1))
```
#### 获取ws地址
```python
getWss()
```
**返回：**
字符串
```
'wss://api.sgroup.qq.com/websocket'
```
### 发送消息
> **注意：** 本功能还在开发中，暂无文档支持，您可以先行参考 `test.ipynb`



## 交互式的调试api？

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

