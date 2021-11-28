from pydantic import BaseModel

class SessionStartLimit(BaseModel):
    total:int            #每 24 小时可创建 Session 数
    remaining:int        #目前还可以创建的 Session 数
    reset_after:int      #重置计数的剩余时间(ms)
    max_concurrency:int  #每 5s 可以创建的 Session 数


class Shards(BaseModel):
    url:str      # WebSocket 的连接地址
    shards: int  # 建议的 shard 数
    session_start_limit:SessionStartLimit #创建Session限制信息