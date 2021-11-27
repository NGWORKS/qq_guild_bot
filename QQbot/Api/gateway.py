from ..request import get
from ..Model.ApiModel.gateway import Shards


def getWss() -> str:
    """获取通用WSS接入点"""
    res = get("/gateway")
    return res['url']

def shardsWss() -> Shards:
    """获取带分片 WSS 接入点"""
    res = get("/gateway/bot")
    return Shards(**res)