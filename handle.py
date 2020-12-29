# -*- coding: utf-8 -*-#
# filename: handle.py

import hashlib
import reply
import receive
import web
from Semantic.weather_query import weather
class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print("Handle Post webdata is ", webData)
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = recMsg.Content.decode('utf8')
                # res = content + ", this is my first wechat dev!"
                res = weather.query(content)
                replyMsg = reply.TextMsg(toUser, fromUser, res)
                return replyMsg.send()
            elif isinstance(recMsg, receive.EMsg) and recMsg.MsgType == 'event':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                res = '测试中，目前只支持天气查询~\n比如：上海'
                replyMsg = reply.TextMsg(toUser, fromUser, res)
                return replyMsg.send()
            else:
                print("暂且不处理")
                return "success"
        except Exception as Argment:
            print(Argment)
            return Argment