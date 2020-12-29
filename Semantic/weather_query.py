# -*- coding: utf-8 -*-
# filename: sem.py 语义处理模块

import json
import re
import time
import requests
from bs4 import BeautifulSoup

class Weather:
	def __init__(self):
		with open('Semantic/citycode.txt', mode='r', encoding='utf-8') as r:
			self.citycode = r.readlines()
	def query(self, city_name):
		try:
			mill = int(round(time.time() * 1000))

			headers = {'Accept': '*/*',
					   'Accept-Encoding': 'gzip, deflate',
					   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
					   'Connection': 'keep-alive',
					   'Cookie': 'vjuids=-14768fb78.163f88bf07a.0.ee06aa72c6622; f_city=%E5%8C%85%E5%A4%B4%7C101080201%7C; UM_distinctid=166621631e8368-02bcbf8e9ce7fb-9393265-1fa400-166621631e9641; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1539706259,1539832348,1539832353,1539856676; vjlast=1528883311.1547965750.21; Wa_lvt_1=1547965750; Wa_lpvt_1=1547965761',
					   'Host': 'd1.weather.com.cn',
					   'Referer': 'http://www.weather.com.cn/weather1d/101010100.shtml',
					   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36}'}
			r = requests.get('http://d1.weather.com.cn/sk_2d/' + self.read_city(city_name) + '.html?_=' + str(mill),
							 headers=headers)
			r.encoding = 'utf-8'
			res = self.parse_html(r.text)
		except Exception as e:
			print(e)
			res = '【天气查询】\n城市输入有误，请重新输入'
		return res

	def parse_html(self, source):
		soup = BeautifulSoup(source, 'html5lib')
		text = soup.body.text
		return text.split('=')[1]

	def read_city(self, city_name):
		for line in self.citycode:
			if city_name in line:
				return re.split('=', line)[0]

weather = Weather()
