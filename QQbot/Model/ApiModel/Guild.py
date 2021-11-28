# -*- coding: utf-8 -*-
"""
频道对象(Guild)
--------------
频道对象是一个频道应该有的的数据结构，主要是由 ``Guild`` 组成
"""
from typing import Optional

from pydantic import BaseModel


class Guild(BaseModel):
    """
    频道对象
    ======
    频道对象是一个频道应该有的的数据结构
    * 频道对象中所涉及的 ID 类数据，都仅在机器人场景流通，与真实的 ID 无关。请不要理解为真实的 ID

    参数::
    -----
    * ``id``    	    ``string``  ``频道ID``
    * ``name``      	``string``	``频道名称``
    * ``icon``  	    ``string``	``频道头像地址``
    * ``owner_id``  	``string``	``创建人用户ID``
    * ``owner``     	``bool``	``当前人是否是创建人``
    * ``member_count``	``int``	    ``成员数``
    * ``max_members``	``int``	    ``最大成员数``
    * ``description``	``string``	``描述``
    * ``joined_at``	    ``string``	``加入时间``
    * ``union_world_id`` ``string``	``游戏绑定公会区服ID，需要特殊申请并配置后才会返回``
    * ``union_org_id``	``string``	``游戏绑定公会/战队ID，需要特殊申请并配置后才会返回``

    """
    id: str
    name: str
    icon: Optional[str]
    owner_id: Optional[str]
    owner: Optional[bool]
    op_user_id: Optional[str]
    member_count: Optional[int]
    max_members: Optional[int]
    description: Optional[str]
    joined_at: Optional[str]
    union_world_id: Optional[str]
    union_org_id: Optional[str]
