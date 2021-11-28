from pydantic import BaseModel
from typing import Optional
from .User import User
from .Member import Member


class MessageEmbedField(BaseModel):

    name: str  # 字段名
    value: str  # 字段值


class MessageEmbed(BaseModel):
    title: str  # 标题
    description: str  # 描述
    prompt: str  # 消息弹窗内容
    timestamp: str  # iISO8601 timestamp	消息创建时间
    fields: list[MessageEmbedField]  # 对象数组	消息创建时间


class MessageAttachment(BaseModel):
    url: str  # 下载地址


class MessageArkObjKv(BaseModel):
    key: str  # key
    value: str  # value


class MessageArkObj(BaseModel):
    obj_kv: list[MessageArkObjKv]  # objkv类型的数组	ark objkv列表


class MessageArkKv(BaseModel):
    key: str  # key
    value: str  # value
    obj: list[MessageArkObj]  # arkobj类型的数组	ark obj类型的列表


class MessageArk(BaseModel):
    template_id: int  # ark模板id（需要先申请）
    kv: list[MessageArkKv]  # arkkv数组	kv值列表


class Message(BaseModel):
    id: str  # 消息 id -
    channel_id: str  # 子频道 id -
    guild_id: str  # 频道 id - 
    content: Optional[str]  # 消息内容 -
    timestamp:  str  # ISO8601 timestamp	消息创建时间 -
    edited_timestamp: Optional[str]  # ISO8601 timestamp	消息编辑时间
    mention_everyone: Optional[bool]  # 是否是@全员消息
    author: User  # 对象	消息创建者 -
    attachments: Optional[list[MessageAttachment]]  # 对象数组	附件
    embeds: Optional[list[MessageEmbed]]  # 对象数组	embed

    mentions: Optional[list[User]]  # 对象数组	消息中@的人 - 

    member: Optional[Member]  # 对象	消息创建者的member信息 -
    ark: Optional[MessageArk]  # ark消息对象	ark消息


data = {
    'author': {
        'avatar': 'http://thirdqq.qlogo.cn/g?b=oidb&k=HCORhra15uJp2jDAhvOy5A&s=100&t=1599799492',
        'bot': False,
        'id': '9802601117268679552',
        'username': 'sk什么时候更新啊'
    },
    'channel_id': '1555076',
    'content': '<@!11810040378067637410> message',
    'guild_id': '4930494858376070938',
    'id': '08d2d7d296b6c5b85d1084f55e1a133938303236303131313732363836373935353220801e280030f79bde83043815401548eaa9848d065800',
    'member': {
        'joined_at': '2021-11-24T20:45:06+08:00',
        'roles': ['2']
    },
    'mentions': [
        {'avatar': 'http://thirdqq.qlogo.cn/g?b=oidb&k=G4icjGB7udGG1TArrwKId1A&s=100&t=1637758329',
         'bot': True,
         'id': '11810040378067637410',
         'username': '禾咕咕-测试中'}
    ],
    'timestamp': '2021-11-27T01:10:02+08:00'
}
