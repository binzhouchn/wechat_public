# -*- coding: utf-8 -*-#
# filename: handle.py

import hashlib
import reply
import receive
import web
from Semantic.weather_query import weather
from Semantic.img_clf import imageclf
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
                # 得到content，即用户公众号对话框中输入的文字
                content = recMsg.Content.decode('utf8')
                # res = content + ", this is my first wechat dev!"
                if content == '小白':
                    # 如果文字是小白，则返回一张小白（我家的一只法斗）的image（图片存在临时素材库中，方法详见readme）
                    replyMsg = reply.ImageMsg(toUser, fromUser, "-jAxxxxxxK7A")
                else:
                    # 如果是其他文字，则调用查询天气方法，返回text
                    res = weather.query(content)
                    replyMsg = reply.TextMsg(toUser, fromUser, res)
                return replyMsg.send()
            elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'image':
                # 用户输入图片，调用百度接口返回该图片所属种类text
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                res = imageclf.image_classif(recMsg.PicUrl, baike_num=2)
                replyMsg = reply.TextMsg(toUser, fromUser, res)
                return replyMsg.send()
            elif isinstance(recMsg, receive.EMsg) and recMsg.MsgType == 'event':
                # 如果触发event，比如关注了该公众号则返回text给到用户
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