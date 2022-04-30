# -*- coding: utf-8 -*-
"""
@author:  YHH---TEAM


the ensemble and main progress
"""

import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components
from Personal import personal_graph   #个人画像主页
import pandas as pd
from class_basic import Basic_imf
from Poverty_Alert import Alert
from Academic_alert import academic
st.set_page_config(layout="wide")
# design the Structure of sidebar

# 数据图区
def read_data():
    data = pd.read_csv('data.csv')
    data = data.drop([0])
    return data

df = read_data()

# 数理学院logo图片解析
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# 管理员权限页面构造与功能实现
def manager():
    choise_manager = st.sidebar.select_slider('请选择一种验证方式',['人脸识别','0','账号密码输入'],value = '0',
                                              help='通过验证后方才进入系统内部进行数据更改，拖动滑块选择一种验证方式')
    if choise_manager == '账号密码输入':
        accout = st.sidebar.text_input(label='管理员账号',help='请输入你的管理员账号密码信息',placeholder='ID')
        password = st.sidebar.text_input(label='管理员密码',placeholder='PASSWORD')
        confirm = st.sidebar.button('登录')
        
        if confirm:
            if accout == 'root' and password == 'root':
                st.sidebar.markdown('<right>`登录成功，请继续操作`<right>',unsafe_allow_html=True)
                return None
            else:
                st.sidebar.markdown('<right>`账号或密码错误，请重新输入`<right>',unsafe_allow_html=True)
                return None
    if choise_manager == '人脸识别':
        st.sidebar.camera_input("请对准摄像头",help='人脸识别验证方式需要您允许网页端使用当前设备摄像头')
        return None
        
def sidebar():
    st.sidebar.markdown('''[ <p style="text-align: center;"> <img src='data:image/png;base64,{}' class='img-fluid' width=300 height=72>](http://shuli.xy.bitzh.edu.cn/slxy/)'''.format(img_to_bytes("LOGO.png")), unsafe_allow_html=True)
    st.sidebar.markdown('**<center>学生画像系统<center>**',unsafe_allow_html=True)
    help_text = '学生画像系统包括包括三个部分。整体画像：对象是整个学院；个人画像：对象是学生个人与特定群体如贫户、学业警示等；管理员权限：对数据库内容进行增删改查'
    choise = st.sidebar.radio('功能选择',['整体画像','个人画像','管理员权限'],index = 0,help=help_text)
    if choise == '个人画像':
        ano_choise = st.sidebar.select_slider('请选择一种分析模式', ['学生概况','学业警示','贫困预警'],value = '学业警示',help = '分为3种模式，拖动滑块到对应的左、中、右三处')
        
        if ano_choise=='学生概况':
            name = st.sidebar.selectbox('请选择一位学生', df['姓名'].tolist(),help='每次只能选择一名学生')
            st.progress(100)
            st.spinner()
            with st.spinner(text='词云图头像制作正在进行中'):
                 personal_graph(name, df).main()   
                 
            
                 
        if ano_choise == '贫困预警':
            st.progress(100)
            st.spinner()
            with st.spinner(text='贫困生信息处理正在进行中'):
                 Alert(df).main()  
        
        if ano_choise == '学业警示':
            st.progress(100)
            st.spinner()
            with st.spinner(text='学业警示类学生正在提取中'):
                 academic(df).main()             
            
        return None
    
    if choise == '管理员权限':
        manager()
            
                
        return None
    
    if choise == '整体画像':
        st.progress(100)
        st.spinner()
        with st.spinner(text='班级信息正在进行中'):
             Basic_imf(df).main()  
        
    
    
    # with st.form(key='my_form'):
    #     text_input = st.text_input(label='Enter some text')
    #     submit_button = st.form_submit_button(label='Submit')
        
        # st.sidebar.button('Hit me')
        # # st.sidebar.download_button('On the dl', data)
        # st.sidebar.checkbox('Check me out')
        # st.sidebar.radio('Radio', [1,2,3])
        # st.sidebar.selectbox('Select', [1,2,3])
        # st.sidebar.multiselect('Multiselect', [1,2,3])
        # st.sidebar.slider('Slide me', min_value=0, max_value=10)
        # st.sidebar.select_slider('Slide to select', options=[1,'2'])
        # st.sidebar.text_input('Enter some text')
        # st.sidebar.number_input('Enter a number')
        # st.sidebar.text_area('Area for textual entry')
        # st.sidebar.date_input('Date input')
        # st.sidebar.time_input('Time entry')
        # st.sidebar.file_uploader('File uploader')
        # st.sidebar.camera_input("一二三,茄子!")
        # st.sidebar.color_picker('Pick a color')



def main():
    sidebar()
    return None


if __name__ == '__main__':
    main()



