from typing import Any, Text
from requests import Session
from ..config import BOT_APPID, BOT_TOKEN,Url
from .error import getError

s = Session()
header = {'Authorization': f'Bot {BOT_APPID}.{BOT_TOKEN}',
          'Content-Type': 'application/json'}
s.headers.update(header)

url1 = "https://api.sgroup.qq.com/users/@me/guilds"


def UrlSplicing(url: Text, params: Text) -> Text:
    return url + params[1:len(params)]


def get(url: Text, json: Any | None = None, data: Any | None = None, params: Any | None = None):
    url = UrlSplicing(Url, url)
    res = s.get(url=url, json=json, data=data, params=params)
    getError(res)
    return res.json()


def post(url: Text, json: Any | None = None, data: Any | None = None, params: Any | None = None):
    url = UrlSplicing(Url, url)
    res = s.post(url=url, json=json, data=data, params=params)
    getError(res)
    return res.json()


def delete(url: Text, json: Any | None = None, data: Any | None = None, params: Any | None = None):
    url = UrlSplicing(Url, url)
    res = s.delete(url=url, json=json, data=data, params=params)
    return res


def put(url: Text, json: Any | None = None, data: Any | None = None, params: Any | None = None):
    url = UrlSplicing(Url, url)
    res = s.put(url=url, json=json, data=data, params=params)
    return res


def patch(url: Text, json: Any | None = None, data: Any | None = None, params: Any | None = None):
    url = UrlSplicing(Url, url)
    res = s.patch(url=url, json=json, data=data, params=params)
    return res
