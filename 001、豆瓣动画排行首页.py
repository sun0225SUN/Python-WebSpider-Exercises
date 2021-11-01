"""
-*- coding: utf-8 -*-
@Time : 2021/11/1 下午 10:22
@Author : SunGuoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""

# 豆瓣动画电影排行响应的是json数据，emmm比较简单！！！

# 引入requests模块
import requests
import json

# 指定URL
url = 'https://movie.douban.com/j/chart/top_list'
# 指定参数
pararms = {
    'type': '25',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}
# 指定请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}
# 请求
response = requests.get(url=url, params=pararms, headers=headers)
# 经过分析，返回的数据是json格式的字符串
# 把字符串打包成json数据，这样就可以用字典的方式提取数据了
content = response.json()
# 开始提取数据，并写入txt文件
with open('豆瓣电影动画排行榜首页.txt', 'w', encoding='utf-8') as file:
    for i in content:
        title = i['title']
        score = i['score']
        file.write(title + ' ' + score + '\n')
print("爬取完成！")
