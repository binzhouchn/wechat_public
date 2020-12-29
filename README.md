# 本地服务与微信公众号联动

本文档是在已申请个人公众号（免费）的情况下，描述如何将本地的服务与微信公众号联动，比如提供用户天气查询、机器人问答、图像识别服务等等

[官方指南](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Getting_Started_Guide.html)<br>

总体流程：
 - 搭建本地服务，暴露80端口(用##3中的两个文件先启动服务)
 - 内网映射，我用的NATAPP(也可以用其他的)
 - 微信公众号/基本配置（服务器配置启用token）
 - 运行main.py启动最终本地服务
 - 其他补充

## 1.搭建本地服务

```shell
# 根据##3，新建main_test.py和handle_test.py然后运行本地python服务
python main_test.py 80
```

## 2. 内网映射（如果已有或者有云服务器可忽略）

- 申请NATAPP(https://natapp.cn/下载软件)
- 购买隧道，我买的是VIP_1型
- 购买二级域名，绑定我的VIP_1型隧道
- 修改隧道配置：本地地址：127.0.0.1；本地端口：80（配置完成后会有一个公网域名映射到本地127.0.0.1:80）

```shell
# cd到下载的natapp客户端
# 启动natapp服务(我的是mac)
./natapp -authtoken=xxxxx
```

## 3. 公众号配置

详情可参考[微信公众号入门指引](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Getting_Started_Guide.html)<br>

新建main_test.py<br>
```python
# -*- coding: utf-8 -*-
# filename: main_test.py
import web
from handle_test import Handle
urls = (
    '/wx', 'Handle',
)
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
```
新建handle_test.py<br>
```python
# -*- coding: utf-8 -*-
# filename: handle_test.py
import hashlib
import web
class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "bxxxxxxx1" #请按照公众平台官网\基本配置中信息填写
            list = [token, timestamp, nonce]
            list.sort()
            hashcode = hashlib.sha1(bytes(''.join(list),"utf-8")).hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception as Argument:
            return Argument
```

3.1 在公众号网页端基本配置/服务器配置中输入服务器地址(URL)，比如http://公网域名/wx<br>
3.2 令牌(Token)和上面代码中的"bxxxxxxx1"对应<br>
3.3 消息加解密密钥无所谓，消息加解密方式用明文模式即可

重新启动成功后（python main.py 80），点击提交按钮。若提示”token验证失败”, 请认真检查代码或网络链接等。若token验证成功，会自动返回基本配置的主页面，点击启动按钮<br>
公众号/基本配置/服务器配置(已启用) 


## 4. 运行main.py启动最终本地服务

```shell
# 可删除main_test.py和handle_test.py
# 启动main
python main.py 80
```

关注公众号会有event触发并提示用户，进入公众号输入框输入也会有本地python服务的返回！

## 5. 其他不定时补充

5.1 如果想输入文字然后回复图片（以临时素材为例）<br>
[素材管理](https://developers.weixin.qq.com/doc/offiaccount/Asset_Management/New_temporary_materials.html)
```md
(1)http请求方式: GET
https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET
会返回如下json
{
"access_token": "40_xxxxxxxQM",
"expires_in": 7200
}
(2)cd到需要上传的图片的文件夹下，然后
curl -F media=@xiaobai.jpeg "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=40_xxxxxxxQM&type=image"
会返回如下json
{"type":"image","media_id":"-jAxxxxxxK7A","created_at":1609251287,"item":[]}
(3)得到的media_id就可以写传入ImageMsg初始化中mediaId参数
```

5.2 xxx<br>





---

注：本地服务为天气查询，[参考](https://github.com/aichibazhang/python-weather-api)<br>

