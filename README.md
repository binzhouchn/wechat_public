# 微信公众号搭建

本文档

[官方指南](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Getting_Started_Guide.html)<br>

总体流程：
 - 搭建本地服务，暴露80端口
 - 内网映射，我用的NATAPP(也可以用其他的)
 - 微信公众号/基本配置（服务器配置启用token）

## 1.搭建本地服务

```shell
# 运行本地python服务
python main.py 80
```

## 2. 内网映射（如果已有或者有云服务器可忽略）

- 申请NATAPP(下载软件)
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

新建main.py<br>
```python
# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
urls = (
    '/wx', 'Handle',
)
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
```
新建handle.py<br>
```python
# -*- coding: utf-8 -*-
# filename: handle.py
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

重新启动成功后（python main.py 80），点击提交按钮。若提示”token验证失败”, 请认真检查代码或网络链接等。若token验证成功，会自动返回基本配置的主页面，点击启动按钮<br>
公众号/基本配置/服务器配置(已启用) 


















注：本地服务为天气查询，[参考](https://github.com/aichibazhang/python-weather-api)<br>

