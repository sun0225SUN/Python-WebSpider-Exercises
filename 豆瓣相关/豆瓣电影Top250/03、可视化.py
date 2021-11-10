"""
-*- coding: utf-8 -*-
@Time : 2021/11/10 下午 4:25
@Author : SunGuoqi
@Website : https://sunguoqi.com
@Github: https://github.com/sun0225SUN
"""

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar


def getzoombar(data):
    year_counts = data['上映年份'].value_counts()
    year_counts.columns = ['上映年份', '数量']
    year_counts = year_counts.sort_index()
    c = (
        Bar()
            .add_xaxis(list(year_counts.index))
            .add_yaxis('上映数量', year_counts.values.tolist())
            .set_global_opts(
            title_opts=opts.TitleOpts(title='各年份上映电影数量'),
            yaxis_opts=opts.AxisOpts(name='上映数量'),
            xaxis_opts=opts.AxisOpts(name='上映年份'),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_='inside')], )
            .render('各年份上映电影数量.html')
    )


def getcountrybar(data):
    country_counts = data['国家/地区'].value_counts()
    country_counts.columns = ['国家/地区', '数量']
    country_counts = country_counts.sort_values(ascending=True)
    c = (
        Bar()
            .add_xaxis(list(country_counts.index)[-10:])
            .add_yaxis('地区上映数量', country_counts.values.tolist()[-10:])
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title='地区上映电影数量'),
            yaxis_opts=opts.AxisOpts(name='国家/地区'),
            xaxis_opts=opts.AxisOpts(name='上映数量'),
        )
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .render('各地区上映电影数量前十.html')
    )


def getscorebar(data):
    df = data.sort_values(by='评价人数', ascending=True)
    c = (
        Bar()
            .add_xaxis(df['片名'].values.tolist()[-20:])
            .add_yaxis('评价人数', df['评价人数'].values.tolist()[-20:])
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title='电影评价人数'),
            yaxis_opts=opts.AxisOpts(name='片名'),
            xaxis_opts=opts.AxisOpts(name='人数'),
            datazoom_opts=opts.DataZoomOpts(type_='inside'),
        )
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .render('电影评价人数前二十.html')
    )


if __name__ == '__main__':
    data = pd.read_csv('top250.csv')
    getzoombar(data)
    getcountrybar(data)
    getscorebar(data)
