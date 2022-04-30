# -*- coding: utf-8 -*-
"""
WordCloud display

@author: YHH --- TEAM
"""
import jieba
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

class wordcloud():

    def __init__(self,dataframe,name):
        self.dataframe = dataframe
        self.name = name

    def english_judge(self,df):
        if (df['四级通过'].values == '1') and (df['六级通过'].values == '1'):
            return '很好'
        if (df['四级通过'].values == '1') and (df['六级通过'].values == '0'):
            return '较好'
        if (df['四级通过'].values == '0') and (df['六级通过'].values == '0'):
            return '一般'
        
    def computer_judge(self,df):
        if df['计算机二级通过'].values == '1':
            return '拥有计算机二级证书'
        else:
            return ''
        
    def fail_judge(self,df):
        if df['挂科数目'].values == '0':
            return '通过全部科目'
        else:
            return '挂过科目'
    
    def cop_judge(self,df):
        if df['参加竞赛数目'].values != '0':
            return '参加过多场'
        else:
            return '没有参与'
    
    def main(self):
        name = self.name
        df = self.dataframe
        df_self = df.loc[df['姓名']==name]
        major = {'1':'应用统计学','2':'数据科学与大数据技术','3':'土木工程','4':'应用物理','5':'测控技术与仪器'}
        face = {'1':'党员','2':'预备党员','3':'入党','4':'团员','5':'群众'}
        df_self['专业'] = df_self['专业'].apply(lambda x:major[x])
        df_self['政治面貌'] = df_self['政治面貌'].apply(lambda x:face[x])
        
        text = '我来自{}，生源地是{}，是{}人。我的专业是{}。我在{}班生活的很好，政治面貌为{}的一份子。对于课外活动，我喜欢运动，例如{}，因此我参加了我们学校的{}。在大学里面，我的英语很{}。{},\
        我的学业总排名在第{}名，平均绩点为{}，{}。我的高考成绩是{}分。不仅如此，我还参加了{}场讲座。学科竞赛我{}。目前位置，拿过奖学金{}次。现在我在{}工作，从事{}行业。'.format(\
                                                                    df_self['籍贯'].values[0],
                                                                    df_self['生源地'].values[0],
                                                                    df_self['民族'].values[0],
                                                                    df_self['专业'].values[0],
                                                                    df_self['班级'].values[0],
                                                                    df_self['政治面貌'].values[0],
                                                                    df_self['爱好'].values[0],
                                                                    df_self['参加社团名称'].values[0],
                                                                    self.english_judge(df_self),
                                                                    self.computer_judge(df_self),
                                                                    df_self['总排名'].values[0],
                                                                    df_self['平均绩点'].values[0],
                                                                    self.fail_judge(df_self),
                                                                    df_self['高考成绩'].values[0],
                                                                    df_self['参加讲座次数'].values[0],
                                                                    self.cop_judge(df_self),
                                                                    df_self['奖学金次数'].values[0],
                                                                    df_self['工作地点'].values[0],
                                                                    df_self['工作行业'].values[0], )
    
        
        
        # 保存全局分词，用于词频统计
        segments = []
        words = jieba.cut(text)
        for word in words:
            segments.append(word)
        
        # 遍历 word_list ，对 word 出现的频率进行统计
        counts = {}
        for word in segments:
            counts[word] = counts.get(word, 0)+1
            
        # 构造列表包元组，进入词云表中
        items = list(counts.items())
        words = items
        
        
        # words = [
        #     (''.join(list(df['籍贯'][df['姓名']==i].values)), 1),
        #     (''.join(list(df['生源地'][df['姓名']==i].values)), 1),
        #     (''.join(list(df['民族'][df['姓名']==i].values)), 1),
        #     (''.join(list(df['爱好'][df['姓名']==i].values)), 2),
        #     (list(df['参加社团名称'][df['姓名']=='陈勋'].values), 1),
        #     (''.join(list(df['寝室地址'][df['姓名']==i].values)), 2),
        #     (''.join(list(df['参加竞赛名称'][df['姓名']==i].values)), 1),
        #     (''.join(list(df['姓名'][df['姓名']==i].values)), 4),
        #     (''.join(list(df['学号'][df['姓名']==i].values)), 1),
        #     (''.join(list(df['邮箱'][df['姓名']==i].values)), 1),
        #     (zzmm(df[df['姓名'] == i]['政治面貌']),2),
        #     (gender(df[df['姓名'] == i]['性别']),1),
        #     (zhuanye(df[df['姓名'] == i]['专业']),2),
        #     ('总排名:'+''.join(list(df['总排名'][df['姓名']==i].values)), 3),
        #     ('平均绩点:'+''.join(list(df['平均绩点'][df['姓名']==i].values)), 2),
        #     (''.join(list(df['工作地点'][df['姓名']==i].values)), 1),
        #     (''.join(list(df['工作行业'][df['姓名']==i].values)), 2),
        # ]
        c = (
            WordCloud(init_opts=opts.InitOpts(width="800px", height="500px"))
            .add("", words, word_size_range=[20, 50], mask_image = '词云图底色.png',shape=SymbolType.DIAMOND) #shape=SymbolType.DIAMOND  ,pos_top="middle"
            .set_global_opts(title_opts=opts.TitleOpts(name+'头像'), tooltip_opts=opts.TooltipOpts(is_show=True),
        )
            .render_embed()
        )
        
        return c






