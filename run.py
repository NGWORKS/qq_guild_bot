from  QQbot import BOT,SendMessage
from QQbot.Api import channel


bot = BOT()
bot.sendRequest()
bot.ListenerImport()
bot.run_ws()
bot.tasksDocter()

from functools import partial
 
def myfunc1(event):
    # print(event)
    msg = f"<@!{event.author.id}> \n超纲啦~超纲啦！我还不支持这些命令哦~"
    if event.content == f'<@!{bot.BotInfo.id}> ':
        msg = f"欸？发生了什么~？\n<@!{event.author.id}> 是不会使用吗？快试试对我发送 <@!{bot.BotInfo.id}> 帮助 看看~"

    m = SendMessage(channel_id=event.channel_id)
    m.send_text(content=msg,msg_id=event.id)
    
bot.eventManager.AddEventListener("AT_MESSAGE_CREATE",myfunc1)


