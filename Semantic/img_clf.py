# -*- coding: utf-8 -*-
## 用百度SDK（安装aip）
from aip import AipImageClassify
import requests
import urllib
from config import APP_ID, API_KEY, SECRET_KEY
# [SDK文档地址](https://cloud.baidu.com/doc/IMAGERECOGNITION/s/4k3bcxj1m)

class ImageCLF:
    def __init__(self):
        """ 你的 APPID AK SK """
        self.client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
        self.client.setConnectionTimeoutInMillis(8000)
        self.client.setSocketTimeoutInMillis(8000)
    def image_classif(self, wechat_img_url, baike_num=0):
        print('wechat_img_url: ', wechat_img_url)
        # # 图片save到本地
        # pic_name = 'z_' + wechat_img_url.replace('https://', '').replace('http://', '').replace('/', '').replace('.jpg','').replace(
        #     '.jpeg', '').replace('.png', '').replace('.', '')[-6:] + '.png'
        # save_path = '~/Downloads/{}'.format(pic_name)
        # urllib.request.urlretrieve(wechat_img_url, save_path)
        # image = self.get_file_content(save_path)

        # 图片不save本地，直接request.get成bytes
        image = requests.get(wechat_img_url).content
        """ 如果有可选参数 """
        options = {}
        options["baike_num"] = baike_num #百度百科数量，默认返回0
        """ 带参数调用通用物体识别 """
        res = self.client.advancedGeneral(image, options)
        return str(res)

    """ 读取图片(如果图片存本地该函数会用到) """
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

imageclf = ImageCLF()

## 不用百度SDK
# import requests
# import base64
# import urllib
# from config import ACCESS_TOKEN
#
# # 直接调用接口，所以暂时不写类了
# def image_classif(wechat_img_url):
#     # 需要调用的百度接口url
#     request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
#     print('wechat_img_url: ',wechat_img_url)
#     image = base64.b64encode(requests.get(wechat_img_url).content)
#     params = {"image": image}
#     access_token = ACCESS_TOKEN
#     request_url = request_url + "?access_token=" + access_token
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     response = requests.post(request_url, data=params, headers=headers)
#     return response.text
