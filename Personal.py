# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 17:32:04 2022

@author: YHH---TEAM
"""

import pandas as pd
import streamlit as st
import numpy as np


import streamlit.components.v1 as components
from word_cloud import wordcloud

from pyecharts import options as opts
from pyecharts.charts import Radar
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
        
import pyecharts.options as opts
from pyecharts.charts import Grid, Boxplot, Scatter

import pyecharts.options as opts
from pyecharts.charts import Grid, Boxplot, Scatter
        
import pyecharts.options as opts
from pyecharts.charts import Grid, Boxplot, Scatter



# df = pd.read_csv('data.csv')
# df = df.drop([0])


class personal_graph():
    def __init__(self,name,dataframe):
        self.name = name
        self.dataframe = dataframe
        
    def main(self):
        name = self.name
        df = self.dataframe
        # 词云图包调用与调出构建好的ehcarts文件，后续调用
        wc = wordcloud(df, name)
        c = wc.main()
        
        
        # 字典映射，将数据表中的编码解码为实际意义
        gender_dict = {'1':'男','2':'女'}
        
        face = {'1':'党员','2':'预备党员','3':'入党','4':'团员','5':'群众'}
        
        major = {'1':'应用统计学','2':'数据科学与大数据技术','3':'土木工程','4':'应用物理','5':'测控技术与仪器'}
        
        
        # display table and wordcloud
        
        # from pyecharts.globals import ThemeType
        # # st_pyecharts(c)
        # components.html(c,width=1000, height=1000)
        
        # 基本信息表格+头像词云图
        display_word = components.html(
            f"""
            <center>
                {c}
            </center>
            """,height = 460)
            
        if st.button('头像不显示请点击',help='如不显示，请多次点击'):
            display_word

            
        display_word 
            
        components.html(
            f"""
            <html>
            <head>
                <title>{name}的个人介绍</title>
                <meta charset="utf-8">
            </head>
            <body>
            <!-- 这是一个表格标签 -->

            <table width="100%" height="10%" cellpadding="5px" cellspacing="0" border="1" align="center">
            
             
                <tr align="center">
                    <th colspan="7" bgcolor="lightgray">基本信息</th>
                </tr>
                    
                <tr align="center">
                    <td width="100" align="center">姓名</td>
                    <td width="100" align="center">{name}</td>
                    <td width="100" align="center">性别</td>
                    <td width="100" align="center">{gender_dict[df.loc[df['姓名']==name]['性别'].values[0]]}</td>
                    <td width="100" align="center">联系电话</td>
                    <td width="100" align="center"><i>{df.loc[df['姓名']==name,'联系电话'].values[0]}</i></td>
        
                    </td>
                </tr>
                <tr>
                    <td width="100" align="center">民族</td>
                    <td width="100" align="center">{df.loc[df['姓名']==name,'民族'].values[0]}</td>
                    <td width="100" align="center">爱好</td>
                    <td width="100" align="center">{df.loc[df['姓名']==name,'爱好'].values[0]}</td>
                    <td width="100" align="center">政治面貌</td>
                    <td width="100" align="center">{face[df.loc[df['姓名']==name,'政治面貌'].values[0]]}</td>
                </tr>
                <tr>
                    <td width="100" align="center">籍贯</td>
                    <td width="100" align="center">{df.loc[df['姓名']==name,'籍贯'].values[0]}</td>
                    <td width="100" align="center">平均绩点</td>
                    <td width="100" align="center">{df.loc[df['姓名']==name,'平均绩点'].values[0]}</td>
                    <td width="100" align="center">总排名</td>
                    <td width="100" align="center">{df.loc[df['姓名']==name,'总排名'].values[0]}</td>
                </tr>
                <tr>
                    <td width="100" align="center">毕业院校</td>
                    <td width="100" colspan="2" align="center">北京理工大学珠海学院</td>
                    <td width="100" align="center">所学专业</td>
                    <td width="100" colspan="2" align="center">{major[df.loc[df['姓名']==name,'专业'].values[0]]}</td>
                </tr>
                <tr>
                    <td width="100" align="center">高考成绩</td>
                    <td width="100" colspan="2" align="center">{df.loc[df['姓名']==name,'高考成绩'].values[0]}</td>
                    <td width="100" align="center">电子邮箱</td>
                    <td width="100" colspan="3" align="center">{df.loc[df['姓名']==name,'邮箱'].values[0]}</td>
                </tr>
                <tr>
                    <td width="100" align="center">在职行业</td>
                    <td width="100" colspan="3" align="center">{df.loc[df['姓名']==name,'工作行业'].values[0]}</td>
                    
                    <td width="100" align="center">工作地点</td>
                    <td width="100" colspan="3" align="center">{df.loc[df['姓名']==name,'工作地点'].values[0]}</td>
                
                </tr>
            
             
            </table>
            </body>
            </html>
            """,
            height=300,
        )

        
        # <u>217272829</u>@qq.com
        
        #个人信息页
        # i = '林丹'  #名字索引,按键返i回值
        df.set_index('挂科数目')
        X = df.loc[:, df.columns != '挂科数目']
        # df[df['姓名']==i]
        
        def gender(label):  #字符转标签
            label = int(label)
            if label==1:
                xb = '男'
            elif label==2:
                xb = '女'
            return xb
        
        def zhuanye(label): #专业数字转标签
            label = int(label)
            if label==1:
                zy = '应用统计学'
            elif label==2:
                zy = '数据科学与大数据'
            elif label==3:
                zy = '土木工程'   
            elif label==4:
                zy = '应用物理'   
            elif label==5:
                zy = '测控技术与仪器'   
            return zy
        
        def zzmm(label): #政治面貌数字转标签
            label = int(label)
            if label==1:
                zzmm = '党员'
            elif label==2:
                zzmm = '预备党员'
            elif label==3:
                zzmm = '入党积极分子'   
            elif label==4:
                zzmm = '团员'   
            elif label==5:
                zzmm = '群众'   
            return zzmm
        i = name
        index_ = [
            '姓名', '性别', '民族', '学院', '专业', '班级', '学号', '生源地', '联系电话', '政治面貌', '邮箱',
            '寝室地址'
        ]
        list1 = np.array([
            ''.join(df.loc[df['姓名'] == i]['姓名'].tolist()),
            gender(df[df['姓名'] == i]['性别']),
            ''.join(df.loc[df['姓名'] == i]['民族'].tolist()), '数理与土木工程学院',
            zhuanye(df[df['姓名'] == i]['专业']),
            ''.join(df.loc[df['姓名'] == i]['班级'].tolist()),
            ''.join(df.loc[df['姓名'] == i]['学号'].tolist()),
            ''.join(df.loc[df['姓名'] == i]['生源地'].tolist()),
            ''.join(df.loc[df['姓名'] == i]['联系电话'].tolist()),
            zzmm(df[df['姓名'] == i]['政治面貌']),
            ''.join(df.loc[df['姓名'] == i]['邮箱'].tolist()),
            ''.join(df.loc[df['姓名'] == i]['寝室地址'].tolist())
        ]).reshape(1, 12)
        
        # st.write('姓名:',i,' '*10,'性别:',list1[0][2] )
        # col1, col2 = st.columns(2)
        
        # with col1:
        #     st.write('姓名:',''.join(df.loc[df['姓名'] == i]['姓名'].tolist()))
        #     st.write('性别:',gender(df[df['姓名'] == i]['性别']))
        #     st.write('民族:',''.join(df.loc[df['姓名'] == i]['民族'].tolist()))
        #     st.write('学院:','数理与土木工程学院')
        #     st.write('专业:',zhuanye(df[df['姓名'] == i]['专业']))
        #     st.write('班级:',''.join(df.loc[df['姓名'] == i]['班级'].tolist())+'班')
        
        # with col2:
        #     # st.write('姓名:',i,' '*10,'性别:',list1[0][2] )
        #     # st.write('姓名:',i,' '*10,'性别:',list1[0][2] )
        #     # st.write('姓名:',i,' '*10,'性别:',list1[0][2] )
        #     # st.write('姓名:',i,' '*10,'性别:',list1[0][2] )
        #     # st.write('姓名:',i,' '*10,'性别:',list1[0][2] )
        #     st.write('姓名:',i,' '*10,'性别:',list1[0][2] )
        #     st.write('姓名:',i,' '*10,'性别:',list1[0][2] )
        #     st.markdown("<style>{好好}</style>", unsafe_allow_html=True)
            
        
        #学生画像标签--入学水平,学习成果,课外拓展能力,在校表现
        #入学水平--高考成绩
        #高考成绩
        g = ''.join(list(pd.qcut(df['高考成绩'].astype(float), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
        
        #学习成果--绩点,已修学分,技能证书
        #绩点
        x = ''.join(list(pd.qcut(df['平均绩点'].astype(float), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
        #已修学分
        x1 = ''.join(list(pd.qcut(df['已修学分'].astype(float).rank(method='first'), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
        #技能证书
        def jineng(data):
            if data==0:
                return '一般'
            elif data==1:
                return '正常'
            elif data==2:
                return '较高'
            elif data==3:
                return '高'
        x2 = jineng(df[['四级通过','六级通过','计算机二级通过']].astype(float).sum(axis=1)[df['姓名']==i].values)
        
        
        #课外拓展能力--讲座,素质拓展学分
        #讲座
        k = ''.join(list(pd.qcut(df['参加讲座次数'].astype(float), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
        #素质拓展学分
        k1 = ''.join(list(pd.qcut(df['素质拓展学分'].astype(float).rank(method='first'), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
        
        
        #在校表现--参加竞赛,参加社团,去图书馆次数,食堂三餐次数
        #参加竞赛
        z = ''.join(list(pd.qcut(df['参加竞赛数目'].astype(float).rank(method='first'), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
        #参加社团数目
        z1 = ''.join(list(pd.qcut(df['参加社团数目'].astype(float).rank(method='first'), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
        #去图书馆次数
        z2 = ''.join(list(pd.qcut(df['去图书馆次数'].astype(float).rank(method='first'), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
        #食堂吃早饭的次数
        z3 = ''.join(list(pd.qcut(df['食堂吃早饭的次数'].astype(float).rank(method='first'), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
        #食堂吃午饭的次数
        z4 = ''.join(list(pd.qcut(df['食堂吃晚饭的次数'].astype(float).rank(method='first'), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
        #食堂吃晚饭的次数
        z5 = ''.join(list(pd.qcut(df['食堂吃晚饭的次数'].astype(float).rank(method='first'), 5, labels=['低', '较低', '正常', '较高', '高'])[df['姓名']==i].values))
        # 求出综合等级,然后计算平均成绩,确定该类型的等级
        def dj_fen(data):  #等级转分数
            if data == '低':
                return 0.2
            elif data =='较低':
                return 0.3
            elif data =='正常':
                return 0.6
            elif data =='较高':
                return 0.8
            elif data=='高':
                return 1
        
        def fen_dj(data):   #分数转等级
            if 0<data<=0.2:
                return '低'
            elif 0.2<data<=0.4 =='较低':
                return '较低'
            elif 0.4<data<=0.6:
                return '正常'
            elif 0.6<data<=0.8:
                return '较高'
            elif 0.8<data<=1:
                return '高'
        
        kk = fen_dj(np.mean([dj_fen(k),dj_fen(k1)]))
        xx = fen_dj(np.mean([dj_fen(x),dj_fen(x1),dj_fen(x2)]))
        zz = fen_dj(np.mean([dj_fen(z),dj_fen(z1),dj_fen(z2),dj_fen(z3),dj_fen(z4),dj_fen(z5)]))
        sum_ = fen_dj(np.mean([dj_fen(k),dj_fen(k),dj_fen(k1),dj_fen(x),dj_fen(x1),dj_fen(x2),dj_fen(z),dj_fen(z1),dj_fen(z2),dj_fen(z3),dj_fen(z4),dj_fen(z5)]))
        
        def youxiu(data):  #学生分类结果
            if data=='高':
                return '优秀'
            elif data=='较高':
                return '良好'
            elif data=='正常':
                return '中等'
            else:
                return '及格'
            
        gr_target =np.array([g,kk,xx,zz,youxiu(sum_)]).reshape(1,5)
        gr_index_target = ['入学水平','学习成果','课外拓展能力','在校表现','学生评级']
        gr_data = pd.DataFrame(gr_target,columns=gr_index_target,index=[i])
        st.markdown('###### <center>学生在校综合表现<center>',unsafe_allow_html=True)
        st.table(gr_data)

        
        
        
        #个人评级雷达图

        
        
        v1 = [[dj_fen(g),np.mean([dj_fen(x),dj_fen(x1),dj_fen(x2)]),np.mean([dj_fen(k),dj_fen(k1)]),np.mean([dj_fen(k),dj_fen(k),dj_fen(k1),dj_fen(x),dj_fen(x1),dj_fen(x2),dj_fen(z),dj_fen(z1),dj_fen(z2),dj_fen(z3),dj_fen(z4),dj_fen(z5)]),dj_fen(sum_)]]
        c = (
            Radar(init_opts=opts.InitOpts(width="1000px", height="1000px"))
            .add_schema(
                schema=[
                    opts.RadarIndicatorItem(name="入学水平", max_=1.1),
                    opts.RadarIndicatorItem(name="学习成果", max_=1.1),
                    opts.RadarIndicatorItem(name="课外拓展能力	", max_=1.1),
                    opts.RadarIndicatorItem(name="在校表现	", max_=1.1),
                    opts.RadarIndicatorItem(name="学生评级", max_=1.1),
                ]
            )
            .add('', v1)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                legend_opts=opts.LegendOpts(selected_mode="single"),
                title_opts=opts.TitleOpts(title="%s的个人雷达图"%i),
            )
        )
        c.render_notebook()
        streamlit_echarts.st_pyecharts(c)
        
        
        def li_fl(data):#列表中元素转浮点,方便画箱线图
            float_lst = []
            for item in data:
                float_lst.append(float(item))
            return float_lst
        
        
        #学生画像标签--高考成绩,已修学分
        
        y_data = [
            df['高考成绩'].astype(float),
            df['已修学分'].astype(float),
        
        ]
        scatter_data = [float(''.join(df.loc[df['姓名']==i]['高考成绩'].values)),float(''.join(df.loc[df['姓名']==i]['已修学分'].values))]
        
        box_plot = Boxplot()
        
        box_plot = (
            box_plot.add_xaxis(xaxis_data=["", ""])
            .add_yaxis(series_name="", y_axis=box_plot.prepare_data(y_data))
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    pos_left="center", title=""
                ),
                tooltip_opts=opts.TooltipOpts(trigger="item", axis_pointer_type="shadow"),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    boundary_gap=True,
                    splitarea_opts=opts.SplitAreaOpts(is_show=False),
                    axislabel_opts=opts.LabelOpts(formatter=" {value}"),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
            )
            .set_series_opts(tooltip_opts=opts.TooltipOpts(formatter="{b}: {c}"))
        )
        scatter = (
            Scatter()
            .add_xaxis(xaxis_data=["高考成绩", "已修学分"])
            .add_yaxis(series_name="", y_axis=scatter_data)
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    pos_left="10%",
                    pos_top="90%",
                    title_textstyle_opts=opts.TextStyleOpts(
                        border_color="#666", border_width=1, font_size=14
                    ),
                ),
                yaxis_opts=opts.AxisOpts(
                    axislabel_opts=opts.LabelOpts(is_show=False),
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                ),
            )
        )
        grid = (
            Grid(init_opts=opts.InitOpts(width="1000px", height="1000px"))
            .add(
                box_plot,
                grid_opts=opts.GridOpts(pos_left="10%", pos_right="10%", pos_bottom="15%"),
            )
            .add(
                scatter,
                grid_opts=opts.GridOpts(pos_left="10%", pos_right="10%", pos_bottom="15%"),
            ) 
        )
        streamlit_echarts.st_pyecharts(grid)  # width="800px", height="600px"
        
        
        #学生画像标签--
        
        y_data = [
            df['平均绩点'].astype(float),
            df['参加竞赛数目'].astype(float),
            df['素质拓展学分'].astype(float),
        ]
        scatter_data = [float(''.join(df.loc[df['姓名']==i]['平均绩点'].values)),float(''.join(df.loc[df['姓名']==i]['参加竞赛数目'].values)),float(''.join(df.loc[df['姓名']==i]['素质拓展学分'].values))]
        
        box_plot = Boxplot()
        
        box_plot = (
            box_plot.add_xaxis(xaxis_data=["", "",""])
            .add_yaxis(series_name="", y_axis=box_plot.prepare_data(y_data))
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    pos_left="center", title=""
                ),
                tooltip_opts=opts.TooltipOpts(trigger="item", axis_pointer_type="shadow"),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    boundary_gap=True,
                    splitarea_opts=opts.SplitAreaOpts(is_show=False),
                    axislabel_opts=opts.LabelOpts(formatter=" {value}"),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
            )
            .set_series_opts(tooltip_opts=opts.TooltipOpts(formatter="{b}: {c}"))
        )
        
        scatter = (
            Scatter()
            .add_xaxis(xaxis_data=["平均绩点", "参加竞赛数目","素质拓展学分"])
            .add_yaxis(series_name="", y_axis=scatter_data)
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    pos_left="10%",
                    pos_top="90%",
                    title_textstyle_opts=opts.TextStyleOpts(
                        border_color="#666", border_width=1, font_size=14
                    ),
                ),
                yaxis_opts=opts.AxisOpts(
                    axislabel_opts=opts.LabelOpts(is_show=False),
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                ),
            )
        )
        grid = (
            Grid(init_opts=opts.InitOpts(width="1000px", height="1000px"))
            .add(
                box_plot,
                grid_opts=opts.GridOpts(pos_left="10%", pos_right="10%", pos_bottom="15%"),
            )
            .add(
                scatter,
                grid_opts=opts.GridOpts(pos_left="10%", pos_right="10%", pos_bottom="15%"),
            )
        )
        streamlit_echarts.st_pyecharts(grid)  #streamlit_echarts.st_pyecharts(c) 这个加了就没有弹性
        
        #学生画像标签--去 图书馆次数,三餐,讲座次数
        
        
        y_data = [
            df['去图书馆次数'].astype(float),
            df['食堂吃早饭的次数'].astype(float),
            df['食堂吃午饭的次数'].astype(float),
            df['食堂吃晚饭的次数'].astype(float),
            df['参加讲座次数'].astype(float),
        ]
        scatter_data = [float(''.join(df.loc[df['姓名']==i]['去图书馆次数'].values)),float(''.join(df.loc[df['姓名']==i]['食堂吃早饭的次数'].values)), float(''.join(df.loc[df['姓名']==i]['食堂吃午饭的次数'].values)), float(''.join(df.loc[df['姓名']==i]['食堂吃晚饭的次数'].values)),float(''.join(df.loc[df['姓名']==i]['参加讲座次数'].values))]
        
        box_plot = Boxplot()
        
        box_plot = (
            box_plot.add_xaxis(xaxis_data=["", "", "", "", ""])
            .add_yaxis(series_name="", y_axis=box_plot.prepare_data(y_data))
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    pos_left="center", title=""
                ),
                tooltip_opts=opts.TooltipOpts(trigger="item", axis_pointer_type="shadow"),
                xaxis_opts=opts.AxisOpts(
                    type_="category",
                    boundary_gap=True,
                    splitarea_opts=opts.SplitAreaOpts(is_show=False),
                    axislabel_opts=opts.LabelOpts(formatter=" {value}"),
                    splitline_opts=opts.SplitLineOpts(is_show=False),
                ),
                yaxis_opts=opts.AxisOpts(
                    type_="value",
                    splitarea_opts=opts.SplitAreaOpts(
                        is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                    ),
                ),
            )
            .set_series_opts(tooltip_opts=opts.TooltipOpts(formatter="{b}: {c}"))
        )
        
        scatter = (
            Scatter()
            .add_xaxis(xaxis_data=["去图书馆次数", "食堂吃早饭的次数", "食堂吃午饭的次数", "食堂吃晚饭的次数", "参加讲座次数"])
            .add_yaxis(series_name="", y_axis=scatter_data)
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    pos_left="10%",
                    pos_top="90%",
                    title_textstyle_opts=opts.TextStyleOpts(
                        border_color="#666", border_width=1, font_size=14
                    ),
                ),
                yaxis_opts=opts.AxisOpts(
                    axislabel_opts=opts.LabelOpts(is_show=False),
                    axistick_opts=opts.AxisTickOpts(is_show=False),
                ),
            )
        )
        
        grid = (
            Grid(init_opts=opts.InitOpts(width="1000px", height="1000px"))
            .add(
                box_plot,
                grid_opts=opts.GridOpts(pos_left="10%", pos_right="10%", pos_bottom="15%"),
            )
            .add(
                scatter,
                grid_opts=opts.GridOpts(pos_left="10%", pos_right="10%", pos_bottom="15%"),
            )
        )
        streamlit_echarts.st_pyecharts(grid) # ,width="800px", height="600px"







