"""
频道身份组对象(Role)
--------------
频道身份组对象是一个身份组应该有的的数据结构，主要是由 ``Role`` 组成
"""
from pydantic import BaseModel


class DefaultRoles:
    """
    默认身份组类型
    ------------
    身份组id应该是一个数字id，各不相同，有一些默认的id，如下::
    * ``All`` ``1`` ``全体成员``
    * ``Guild_host`` ``2``	``管理员``
    * ``host`` ``4`` ``群主/创建者``
    * ``channel_admin`` ``5`` ``子频道管理员``
    """
    All = 1
    Guild_host = 2
    host = 4
    channel_admin = 5


class Role(BaseModel):
    """
    频道身份组对象
    ------------
    身份组应当由以下元素构成::
    * ``id``	        ``string``	``身份组ID, 默认值可参考DefaultRoles``
    * ``name``      	``string``	``名称``
    * ``color``	        ``uint32``	``ARGB的HEX十六进制颜色值转换后的十进制数值``
    * ``hoist``	        ``uint32``	``是否在成员列表中单独展示: 0-否, 1-是``
    * ``number``	    ``uint32``	``人数``
    * ``member_limit``	``uint32``	``成员上限``
    """
    id: str
    name: str
    color: int
    hoist: int
    number: int
    member_limit: int


class RoleRequest(BaseModel):
    """
    频道身份组返回模型
    ----------------
    获取频道身份组列表 返回数据::
    * ``guild_id``       ``str``          ``频道 ID``
    * ``roles``          ``list[Role]``   ``Role 对象数组,一组频道身份组对象``
    * ``role_num_limit`` ``str``          ``默认分组上限``

    """
    guild_id: str
    roles: list[Role]
    role_num_limit: str


class Filter(BaseModel):
    """
    身份组选项
    ---------
    * ``name`` 是否`设置名称`: `0-否`  `1-是`
    * ``color`` 是否`设置颜色`: `0-否`  `1-是`
    * ``hoist`` 是否设置在成员列表中`单独展示`: `0-否`  `1-是`
    """
    name: int
    color: int
    hoist: int


class Info(BaseModel):
    """
    身份组信息配置
    ---------
    * ``name`` 名称 ->str
    * ``color`` ARGB的HEX十六进制颜色值转换后的十进制数值 -> int
    * ``hoist`` 在成员列表中单独展示: 0-否, 1-是
    """
    name: str
    color: int
    hoist: int
