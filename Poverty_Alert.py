# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 19:59:40 2022

@author: He Zekai
"""
import streamlit as st
from streamlit_echarts import st_echarts
import streamlit.components.v1 as components
from pyecharts import options as opts
from pyecharts.charts import Radar
from pyecharts import options as opts
from pyecharts.charts import *
from pyecharts.charts import Bar
from pyecharts.faker import Faker
import streamlit_echarts
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts import options as opts
from pyecharts.charts import TreeMap
import pyecharts.options as opts
from pyecharts.charts import Radar

import pyecharts.options as opts
from pyecharts.charts import Radar

import pandas as pd
import streamlit as st
import numpy as np
from streamlit_echarts import st_echarts
import matplotlib.pyplot as plt
import matplotlib as mpl

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

class Alert():
    def __init__(self,dataframe):
        self.dataframe = dataframe
        
    def main(self):
        df = self.dataframe
        # st.set_page_config(layout="wide")
        
        st.header('贫困警示')
        
        def fenxiang(data):  #分箱
            if data==0:
                return '正常'
            elif data==1:
                return '较高'
            elif data>=2:
                return '高'
        
        def tufa(data):
            if data==0:
                return '正常'
            elif data==1:
                return '较高'
            elif data>=2:
                return '很高'
        
        def fuxiangguan(data): #负相关得分
            if data=='低':
                return 1
            elif data=='较低':
                return 0.8
            elif data=='正常':
                return 0.5
            elif data=='较高':
                return 0.3
            elif data=='高':
                return 0.1
        
        def zhengxiangguan(data): #正相关得分
            if data=='低':
                return 0.1
            elif data=='较低':
                return 0.3
            elif data=='正常':
                return 0.5
            elif data=='较高':
                return 0.8
            elif data=='高':
                return 1
        
        def pk_sorce(data): #计算贫困分数
            if data>=6*0.68 and data<6*0.75:
                return '一般贫困预警'
            elif data>=6*0.75 and data<6*0.8:
                return '中等贫困预警'
            elif data>=6*0.8 :
                return '特别贫困预警'
            else:
                return '无贫困预警'
        
        pk_a = []
        pk_alldata = []
        for i in df['姓名']:
            #校园卡消费--负相关,越高越不贫困
            # pd.qcut(df['校园卡消费总金额'].astype(float), 5, labels=['底', '较低', '正常', '较高', '高'])
            a = ''.join(list(pd.qcut(df['校园卡消费总金额'].astype(float), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
            #年收入--负相关,越高越不贫困
            # pd.qcut(df['家庭年收入'].astype(float), 5, labels=['底', '较低', '正常', '较高', '高'])
            b = ''.join(list(pd.qcut(df['家庭年收入'].astype(float), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
            #家庭受教育子女数--正相关,越高越贫困
            c = fenxiang(df['家庭受教育子女数'].astype(float)[df['姓名']==i].values)
            #经济损失--正相关,越高越贫困
            d = fenxiang(df[['家人重病','突发事故','自然灾害']].astype(float).sum(axis=1)[df['姓名']==i].values)
            #家庭劳动力占比--负相关
            e= ''.join(list(pd.qcut(df['家庭劳动力占比'].astype(float), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
            #家庭因素--正相关,越高越贫困
        
            f  = tufa(df[['是否烈士子女','是否孤儿','是否残疾','是否单亲家庭']].astype(float).sum(axis=1)[df['姓名']==i].values)
            pk_target =np.array([a,b,c,d,e,f]).reshape(1,6)
            index_target = ['校园卡消费-负相关','家庭年收入-负相关','家庭受教育子女数-正相关','经济损失-正相关','家庭劳动力占比-负相关','家庭条件因素-正相关']
            pk_data = pd.DataFrame(pk_target,columns=index_target,index=[i])
        
            pk_sum = sum([fuxiangguan(pk_data['校园卡消费-负相关'].values),
            fuxiangguan(pk_data['家庭年收入-负相关'].values),
            fuxiangguan(pk_data['家庭劳动力占比-负相关'].values),
            zhengxiangguan(pk_data['家庭受教育子女数-正相关'].values),
            zhengxiangguan(pk_data['经济损失-正相关'].values),
            zhengxiangguan(pk_data['家庭条件因素-正相关'].values)])
            pk_a.append([i,pk_sorce(pk_sum)])   #姓名+贫困等级
            
            pk_alldata.append([i,pk_sorce(pk_sum),[fuxiangguan(pk_data['校园卡消费-负相关'].values),   #全转为正相关进行可视化
            zhengxiangguan(pk_data['家庭年收入-负相关'].values),
            zhengxiangguan(pk_data['家庭劳动力占比-负相关'].values),
            zhengxiangguan(pk_data['家庭受教育子女数-正相关'].values),
            zhengxiangguan(pk_data['经济损失-正相关'].values),
            zhengxiangguan(pk_data['家庭条件因素-正相关'].values)]])  #姓名+贫困等级+得分
        #     print(pk_sorce(pk_sum))
        k_v_exchanged = {}
        for key, value in dict(pk_a).items():
            if value not in k_v_exchanged:
                k_v_exchanged[value] = [key]
            else:
                k_v_exchanged[value].append(key)
        
        leida_pk_data = []
        for i in range(len(pk_alldata)):
            if pk_alldata[i][0] in k_v_exchanged['中等贫困预警']:
                leida_pk_data.append(pk_alldata[i][2])
        
        
        st.subheader('中等贫困学生')
        st.text('以下学生是后台根据算法推断出家庭情况为中等贫困的学生,请相关老师留意他们的经济情况并给予帮助!')
        a = pd.DataFrame(k_v_exchanged['中等贫困预警']).T
        a.index = ['姓名']
        st.table(a)
        
        def render_basic_radar1():
            
            option = {
                "title": {"text": "中等贫困警示学生雷达图",
                    "top": "top",
                    "left": "center"},
                "legend": {
                    "data": k_v_exchanged['中等贫困预警'],
                    "bottom":10,
                    "left":'center',
                    
                    "type":'scroll'},
                "tooltip": {
                    "trigger": 'item'
                    },
                "radar": {
                    "indicator": [
                        {"name": "校园卡消费", "max": 1},
                        {"name": "家庭年收入", "max": 1},
                        {"name": "家庭劳动力占比", "max": 1},
                        {"name": "家庭受教育子女数", "max": 1},
                        {"name": "经济损失", "max": 1},
                        {"name": "家庭条件因素", "max": 1},
                        
                    ]
                },
                "series": [
                    {
                        #"name": "",
                        "type": "radar",
                        "data": [
                            {
                                "value": leida_pk_data[i] ,
                                "name":k_v_exchanged['中等贫困预警'][i] ,
                            },
                            
                        ],
                    }for i in range(len(k_v_exchanged['中等贫困预警']))
                ],
            }
            st_echarts(option, height="500px")
        
        
        ST_RADAR_DEMOS = {
            "Radar: Basic Radar": (
                render_basic_radar1(),
                "https://echarts.apache.org/examples/en/editor.html?c=radar",
            ),
        }
        
        
        st.subheader('一般贫困学生')
        st.text('以下学生是后台根据算法推断出家庭情况为一般贫困的学生,请相关老师留意他们的经济情况并给予帮助!')
        b = pd.DataFrame(k_v_exchanged['一般贫困预警']).T
        b.index = ['姓名']
        st.table(b)
        leida_pk_data = []
        for i in range(len(pk_alldata)):
            if pk_alldata[i][0] in k_v_exchanged['一般贫困预警']:
                leida_pk_data.append(pk_alldata[i][2])
        
        
        
        #14张一般贫困雷达图--小图
        col1, col2= st.columns(2)
        with col1:
            leida_pk_data1 = leida_pk_data[:int(len(leida_pk_data)/2)]
            for i in range(len(leida_pk_data1)):
                v1 = [leida_pk_data1[i]]
                c = (
                    Radar(init_opts=opts.InitOpts(width="500px", height="400px", bg_color="#fff"))
                    .add_schema(
                        schema=[
                            opts.RadarIndicatorItem(name="校园卡消费", max_=1),
                            opts.RadarIndicatorItem(name="家庭年收入", max_=1),
                            opts.RadarIndicatorItem(name="家庭劳动力占比", max_=1),
                            opts.RadarIndicatorItem(name="家庭受教育子女数", max_=1),
                            opts.RadarIndicatorItem(name="经济损失", max_=1),
                            opts.RadarIndicatorItem(name="家庭条件因素", max_=1),
                        ],
                        splitarea_opt=opts.SplitAreaOpts(
                            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                        ),
                        textstyle_opts=opts.TextStyleOpts(color="#000000"),
                    )
                    .add(
                        series_name=k_v_exchanged['一般贫困预警'][i],
                        data=v1,
                        linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
                    )    
                    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                    .set_global_opts(
                        title_opts=opts.TitleOpts(title="%s的贫困指标雷达图"%k_v_exchanged['一般贫困预警'][i]), legend_opts=opts.LegendOpts()
                       ).render_embed()
                       )
                components.html(c, width=1000, height=600)
        
        with col2:
            leida_pk_data2 = leida_pk_data[int(len(leida_pk_data)/2):]
            for i in range(len(leida_pk_data2)):
                v1 = [leida_pk_data1[-i-1]]
                c = (
                    Radar(init_opts=opts.InitOpts(width="500px", height="400px", bg_color="#fff"))
                    .add_schema(
                        schema=[
                            opts.RadarIndicatorItem(name="校园卡消费", max_=1),
                            opts.RadarIndicatorItem(name="家庭年收入", max_=1),
                            opts.RadarIndicatorItem(name="家庭劳动力占比", max_=1),
                            opts.RadarIndicatorItem(name="家庭受教育子女数", max_=1),
                            opts.RadarIndicatorItem(name="经济损失", max_=1),
                            opts.RadarIndicatorItem(name="家庭条件因素", max_=1),
                        ],
                        splitarea_opt=opts.SplitAreaOpts(
                            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                        ),
                        textstyle_opts=opts.TextStyleOpts(color="#000000"),
                    )
                    .add(
                        series_name=k_v_exchanged['一般贫困预警'][-i+-1],
                        data=v1,
                        linestyle_opts=opts.LineStyleOpts(color="#CD0000"),
                    )    
                    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                    .set_global_opts(
                        title_opts=opts.TitleOpts(title="%s的贫困指标雷达图"%k_v_exchanged['一般贫困预警'][-i-1]), legend_opts=opts.LegendOpts()
                       ).render_embed()
                       )
                components.html(c, width=1000, height=600)





