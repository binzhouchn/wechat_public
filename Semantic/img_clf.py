# -*- coding: utf-8 -*-
from aip import AipImageClassify
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
        pic_name = 'z_' + wechat_img_url.replace('https://', '').replace('http://', '').replace('/', '').replace('.jpg','').replace(
            '.jpeg', '').replace('.png', '').replace('.', '')[-6:] + '.png'
        save_path = '~/Downloads/{}'.format(pic_name)
        urllib.request.urlretrieve(wechat_img_url, save_path)
        image = self.get_file_content(save_path)
        """ 如果有可选参数 """
        options = {}
        options["baike_num"] = baike_num #百度百科数量，默认返回0
        """ 带参数调用通用物体识别 """
        res = self.client.advancedGeneral(image, options)
        return str(res)

    """ 读取图片 """
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

imageclf = ImageCLF()


# import requests
# import base64
# import urllib
# from config import ACCESS_TOKEN
#
# # 直接调用接口，只需要提供access_token
# def image_classif(wechat_img_url):
#     pic_name = 'z_'+ wechat_img_url.replace('https://','').replace('http://','').replace('/','').replace('.jpg','').replace('.jpeg','').replace('.png','').replace('.','')[-6:]+ '.png'
#     save_path = '~/Downloads/{}'.format(pic_name)
#     urllib.request.urlretrieve(wechat_img_url, save_path)
#     request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
#     # 二进制方式打开图片文件
#     f = open(save_path, 'rb')
#     img = base64.b64encode(f.read())
#     params = {"image": img}
#     access_token = ACCESS_TOKEN
#     request_url = request_url + "?access_token=" + access_token
#     headers = {'content-type': 'application/x-www-form-urlencoded'}
#     response = requests.post(request_url, data=params, headers=headers)
#     return response.text
