from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    """用户"""
    id:str	        # 用户 id
    username:str     	#用户名
    avatar:Optional[str]	        #用户头像地址
    bot:Optional[bool]	         #是否是机器人
    union_openid:Optional[str]	#特殊关联应用的 openid，需要特殊申请并配置后才会返回。如需申请，请联系平台运营人员。
    union_user_account:Optional[str]	#机器人关联的互联应用的用户信息，与union_openid关联的应用是同一个。如需申请，请联系平台运营人员。
