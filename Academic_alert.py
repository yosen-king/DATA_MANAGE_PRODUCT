# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:26:30 2022

@author: YHH---TEAM
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

import pandas as pd
import numpy as np


class academic():
    def __init__(self,dataframe):
        self.dataframe = dataframe
        
    def main(self):
        df = self.dataframe
        df = df[df["是否学业警示"]=='1']
        dfxm = df.loc[1:,["姓名",]]
        #dfjs = df.loc[1:,["是否学业警示",]].values
        dfgk = df.loc[1:,["挂科科目总学分","挂科数目","去图书馆次数","惩罚","参加社团数目"]]
        # dfyxxf = df.loc[1:,["应修学分",]].iloc[:1].values[0][0]
        
        dn=dfxm["姓名"].values.tolist() 
        
        
        st.header('学业警示')
        st.text('预计接下来会收到学业警示同学的名单如下,请老师务必多加关注以下同学的学业情况!')
        # a = list(dfxm.T.values)
        st.table(dfxm.T)
        
        dd=dfgk.values.tolist()
        
        
        def render_basic_radar():
            
            option = {
                "title": {"text": "学业警示学生雷达图",
                    "top": "top",
                    "left": "center"},
                "legend": {
                    "data": dn,
                    "bottom":10,
                    "left":'center',
                    
                    "type":'scroll'},
                "tooltip": {
                    "trigger": 'item'
                    },
                "radar": {
                    "indicator": [
                        {"name": "未修学分", "max": 28},
                        {"name": "挂科数目", "max": 10},
                        {"name": "去图书馆次数", "max": 100},
                        {"name": "惩罚", "max": 5},
                        {"name": "参加社团数目", "max": 5},
                        
                    ]
                },
                "series": [
                    {
                        #"name": "",
                        "type": "radar",
                        "data": [
                            {
                                "value": dd[i] ,
                                "name":dn[i] ,
                            },
                            
                        ],
                    }for i in range(len(dn))
                ],
            }
            st_echarts(option, height="500px")
        
        
        ST_RADAR_DEMOS = {
            "Radar: Basic Radar": (
                render_basic_radar(),
                "https://echarts.apache.org/examples/en/editor.html?c=radar",
            ),
        }







