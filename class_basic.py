# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 16:16:41 2022

@author: He Zekai
"""

import pandas as pd
import streamlit as st
import numpy as np
from streamlit_echarts import st_echarts


from pyecharts.faker import Faker
from streamlit_echarts import st_echarts, JsCode
import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

import streamlit.components.v1 as components
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

from LAC import LAC

from pyecharts import options as opts
from pyecharts.charts import *
from pyecharts.charts import Bar
from pyecharts.faker import Faker
import streamlit_echarts
from pyecharts import options as opts
from pyecharts.globals import ThemeType
#就业情况--矩阵树状图
from pyecharts import options as opts
from pyecharts.charts import TreeMap




class Basic_imf():
    def __init__(self,dataframe):
        self.dataframe = dataframe
    
    def main(self):
        df = self.dataframe
        # 展示一级标题
        st.header('学院整体画像')
        
        st.subheader('学院基本信息情况')
        
        
        # df = pd.read_csv(r'data.csv') 
        # df = df.drop([0])
        
        data = [
            {"value":int(df['就业状态'].value_counts(sort=0)[1]), "name": "工作"},
            {"value":int(df['就业状态'].value_counts(sort=0)[2]), "name": "出国"},
            {"value":int(df['就业状态'].value_counts(sort=0)[2]), "name": "考研"},
            {"value":int(df['就业状态'].value_counts(sort=0)[2]), "name": "公务员"},
            {"value":int(df['就业状态'].value_counts(sort=0)[2]), "name": "未就业"}
        ]
        c = (
            TreeMap()
            .add("就业情况数据",data)
            .set_global_opts(title_opts=opts.TitleOpts(title="就业状况"))
        )
        
        streamlit_echarts.st_pyecharts(
              c
        )
        
        #生源地地图
        # 装载分词模型
        lac = LAC(mode='seg')
        shengfen = []
        for i in df['生源地']:
            a =  lac.run(i)
            shengfen.append(a[0])
        sf = []
        for i in  list(set(shengfen)):
            sf.append([i,shengfen.count(i)])
            
        c = (
            Map()
            .add("生源数", sf, "china")
            .set_global_opts(
                title_opts=opts.TitleOpts(title="生源数地图"),
                visualmap_opts=opts.VisualMapOpts(max_=50, is_piecewise=True),
            )    .render_embed()
        )
        components.html(c, width=1000, height=600)
        
        #四六级二级--堆积条形图
        x_index = ["英语四级", "英语六级", "计算机二级"]
        y_value1 = [int(df['四级通过'].value_counts()[0]), int(df['六级通过'].value_counts()[0]), int(df['计算机二级通过'].value_counts()[0])]
        y_value1plus = [int(df['四级通过'].value_counts()[1]), int(df['六级通过'].value_counts()[1]), int(df['计算机二级通过'].value_counts()[1])]
        
        bar = (
            Bar()
            .add_xaxis(x_index)
            .add_yaxis("通过", y_value1, stack = "stack1") # y轴设置
            .add_yaxis("未通过", y_value1plus, stack = "stack1") # y轴设置
            .set_global_opts(title_opts=opts.TitleOpts(title="技能考试通过情况"))
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False)) 
            )
        
        # bar.render_notebook()
        streamlit_echarts.st_pyecharts(bar)
        
        
        
        
        
        
        # def load_data():
        #     data = pd.read_csv("data.csv")
        #     return data
        
        
        
        # df = load_data()
        
        def getlistnum(li):#这个函数就是要对列表的每个元素进行计数
            li = list(li)
            set1 = set(li)
            dict1 = {}
            for item in set1:
                dict1.update({item:li.count(item)})
            return dict1
        
        dfhy = df.loc[:,["工作行业",]]
        dfhy["工作行业"] = dfhy["工作行业"].astype(str)
        
        hydic=getlistnum(dfhy['工作行业'])
        
        hydic['未知']=hydic.pop('nan')
        
        dfhydata=list(hydic.keys())
        
        
        col = ['value', 'name']
        
        hydataall=[{col[0]:hydic.get(dfhydata[p]),col[1]:dfhydata[p]
            } for p in range(len(dfhydata))]
        
        
        
        
        # for i in range(51):
        #     a=dict(zip(df['平均绩点'],df['姓名']))
        
        dfjd = df.loc[:,['平均绩点','姓名',]]
        dfjd["平均绩点"] = dfjd["平均绩点"].astype(float)  # 将销量列数据类型转换为float
        
        dfxf = df.loc[:,["校园卡消费总金额",]]
        dfxm = df.loc[:,["姓名",]]
        dfxf["校园卡消费总金额"] = dfxf["校园卡消费总金额"].astype(float)
        
        dfxfl = [np.array(dfxf).tolist()[i][0] for i in range(len(df))]
        dfxml = [np.array(dfxm).tolist()[i][0] for i in range(len(df))]
        
        dfjd.columns = ['value', 'name']
        user_info = [{col:dfjd[col].tolist()[i] for col in dfjd.columns} for i in range(len(df))]
        
        
        
        
        
        options = {
            "title": {
                "text": "校园卡消费金额"
            },
            "xAxis": {
                "type": "category",
                "data": dfxml  # 此处也可传入数组
            },
            "tooltip": {
                "formatter": JsCode("function (params) \
                    { return `${params.seriesName}<br />${params.name}：${params.value}` ;}").js_code
            },
            "yAxis": {
                "type": "value"
            },
            "series": [
                {
                    "name": "fakerSeries",
                    "data": dfxfl,  # 此处也可传入数组
                    "type": "line"
                }
            ],
        }
        
        events = {
            "click": "function(params) { alert(params.name) }"
        }
        
        st_echarts(options=options, events=events)
        
        
        option = {
            'title' : {
                'text': '工作行业分布',
                "top": "top",
                'x':'left'
            },
            'tooltip' : {
                'trigger': 'item',
                'formatter': "{a} <br/>{b} : {c} ({d}%)"
            },
            'legend': {
                'orient': 'vertical',
                'left': 'left',
                'bottom':10,
                'data': dfhydata
                
            },
            'series' : [
                {
                    'name': '行业分布',
                    'type': 'pie',
                    'radius' : '75%',
                    #'center': ['50%', '60%'],
                        'data':hydataall
                    #    [
                    #     {'value':335, 'name':'直接访问'},
                    #     {'value':310, 'name':'邮件营销'},
                    #     {'value':234, 'name':'联盟广告'},
                    #     {'value':135, 'name':'视频广告'},
                    #     {'value':1548, 'name':'搜索引擎'}
                    # ]
                    ,
                    'itemStyle': {
                        'emphasis': {
                            'shadowBlur': 10,
                            'shadowOffsetX': 0,
                            'shadowColor': 'rgba(0, 0, 0, 0.5)'
                        }
                    }
                }
            ]
        };
        st_echarts(options=option, height="500px")
        
        
        option = {
        "title": {
                "text": "平均绩点",
                "top": "top",
                "left": "left"
            },
        "legend": {
            "left": 'center',
            "bottom":10,
            "type":'scroll'
        },
        "toolbox": {
            "show": "true",
            "feature": {
                "mark": {"show": "true"},
                "dataView": {"show": "true", "readOnly": "false"},
                "restore": {"show": "true"},
                
            }
        },
        "series": [
            {
                "name": '平均绩点',
                "type": 'pie',
                "radius": ["10", "180"],
                #"center": ['50%', '30%'],
                "roseType": 'area',
                "itemStyle": {
                    "borderRadius": "8"
                },
                    "data": user_info
            }
        ],
        "tooltip": {
                        "show": "true"
                    },
        "label": {
            "show":"true"
        },
        };
        
        st_echarts(options=option, height="600px")
        
        
        
        
        
        # visualization = st.sidebar.selectbox('基本情况信息',('班级基本情况信息',"学生个人基本情况"))
        # state_select = st.sidebar.selectbox('选择学生', df['姓名'].unique())
        # status_select = st.sidebar.radio("预警系统", ('无','学业预警', '贫困预警'))











