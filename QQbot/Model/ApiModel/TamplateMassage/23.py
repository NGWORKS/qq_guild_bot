# 23 链接+文本列表模板

from pydantic import BaseModel
from enum import Enum

class desc(Enum):
    pass

class Tamplate23(BaseModel):
    app: str
    app: str
    view: str
    ver: str
    desc: str
    prompt: str
    # meta: {
    #     detail: {
    #         list:#LIST#
    #     }
    # }
