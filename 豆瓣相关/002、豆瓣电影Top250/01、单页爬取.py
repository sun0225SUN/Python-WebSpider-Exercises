"""
-*- coding: utf-8 -*-
@Time : 2021/11/10 下午 5:23
@Author : SunGuoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""

# 导入一些模块
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

# 首先确定URL
url = 'https://movie.douban.com/top250'
# UA伪装
headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
# 发起请求
response = requests.get(url, headers=headers)
# 获得响应文件文本
# print(response.text)
html = response.text
# 创建BeautifulSoup对象，方便解析
soup = BeautifulSoup(html, 'lxml')
# 找出所有的li标签
all_li = soup.find('ol', {'class': 'grid_view'}).find_all('li')
# 创建一个空列表，存放我们的数据。
datas = []
for item in all_li:
    # 提取影片名称（只提取了中文名称）
    name = item.find('span', {'class': 'title'}).text
    # 提取影片评分
    score = item.find('span', {'property': 'v:average'}).text
    # 提取影片经典语录
    quote = item.find('span', {'class': "inq"}).text
    # 下面提取影片信息部分
    info = item.find_all('p', {'class': ''})
    # print(info.text)
    # 返回的是一个列表，列表里是一个元组
    # print(info[0].text)
    info_contents = info[0].text
    # 分割影片信息，提取影片 导演 || 主演 || 上映年份 || 国家/地区 || 类型
    result = re.findall(
        '^.*?\u5bfc\u6f14:\s(.*?)\s.*?\u4e3b\u6f14:\s(.*?)\s.*?(\d{4})\s.*?([\u4e00-\u9fa5].*)\xa0.*?\u002f.*?([\u4e00-\u9fa5].*?)\s\s.*$',
        info_contents, re.S)
    # 把数据按找字典的格式存放到列表里
    datas.append({
        '片名': name,
        '年份': result[0][2],
        '评分': score,
        '导演': result[0][0],
        '主演': result[0][1],
        '类型': result[0][4],
        '国家/地区': result[0][3],
        '经典台词': quote
    })
print("爬取完成！！！")
# 写入到文件
df = pd.DataFrame(datas)
df.to_csv("豆瓣电影.csv", index=False, header=True, encoding='utf_8_sig')
print("已写入豆瓣.csv文件")
