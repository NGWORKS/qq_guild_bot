import json
from typing import List, Optional, Text

from pydantic import BaseModel
from QQbot.request.request import delete, patch, post, put

from ..Model.ApiModel import Channel, RoleRequest
from ..Model.ApiModel.Roles import DefaultRoles, Filter, Info
from ..request import get


class role_id(BaseModel):
    role_id: str


class role_and_guild_id(BaseModel):
    guild_id: str
    role_id: str


def get_roles(guild_id: Text) -> RoleRequest:
    """
    获取频道身份组列表信息
    --------------------

    需要使用的token对应的用户具备删除身份组权限。如果是机器人，要求被添加为管理员。
    """
    res = get(f"/guilds/{guild_id}/roles")
    guild_info = RoleRequest(**res)
    return guild_info


def establish_roles(guild_id: Text, filter: Filter, info: Info) -> role_id:
    """
    创建一个频道身份组
    -----------------

    需要使用的token对应的用户具备删除身份组权限。如果是机器人，要求被添加为管理员。

    """
    data = {
        "filter": filter.dict(exclude_none=True),
        "info": info.dict(exclude_none=True)
    }
    res = post(f"/guilds/{guild_id}/roles", json=data)
    role_id_obj = role_id(**res)
    return role_id_obj


def modify_roles(guild_id: Text, role_id: Text, filter: Filter, info: Info) -> role_and_guild_id:
    """
    修改频道身份组
    -------------

    需要使用的token对应的用户具备删除身份组权限。如果是机器人，要求被添加为管理员。

    """
    data = {
        "filter": filter.dict(exclude_none=True),
        "info": info.dict(exclude_none=True)
    }
    res = patch(f"/guilds/{guild_id}/roles/{role_id}", json=data)
    res = res.json()
    role_and_guild_id_obj = role_and_guild_id(**res)
    return role_and_guild_id_obj


def delete_roles(guild_id: Text, role_id: Text) -> bool:
    """
    删除频道身份组
    -------------

    需要使用的token对应的用户具备删除身份组权限。如果是机器人，要求被添加为管理员。

    """
    res = delete(f"/guilds/{guild_id}/roles/{role_id}")
    if res.status_code != 204:
        return False
    return True


def add_roles_members(guild_id: Text, user_id: Text, role_id: int, channel: Channel | None = None) -> bool:
    """
    增加频道身份组成员
    ----------------

    需要使用的token对应的用户具备删除身份组权限。如果是机器人，要求被添加为管理员

    * 如果要增加的身份组ID是 `5-子频道管理员` 时，需要增加 `channel` 对象来指定具体是哪个子频道

    """
    data = None
    if role_id == DefaultRoles.channel_admin and channel is None:
        ValueError("When role_id is 5, you must provide a channel object")
    if role_id == DefaultRoles.channel_admin and channel is not None:
        data = {"channel": channel.dict(exclude_none=True)}
    res = put(
        f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}", json=data)
    if res.status_code != 204:
        return False
    return True


def delete_roles_members(guild_id: Text, user_id: Text, role_id: int, channel: Channel | None = None) -> bool:
    """
    删除频道身份组成员
    -----------------

    需要使用的token对应的用户具备删除身份组权限。如果是机器人，要求被添加为管理员

    * 如果要删除的身份组ID是 `5-子频道管理员` 时，需要增加 `channel` 对象来指定具体是哪个子频道

    """
    data = None
    if role_id == DefaultRoles.channel_admin and channel is None:
        ValueError("When role_id is 5, you must provide a channel object")
    if role_id == DefaultRoles.channel_admin and channel is not None:
        data = {"channel": channel.dict(exclude_none=True)}
    res = delete(
        f"/guilds/{guild_id}/members/{user_id}/roles/{role_id}", json=data)
    if res.status_code != 204:
        return False
    return True
