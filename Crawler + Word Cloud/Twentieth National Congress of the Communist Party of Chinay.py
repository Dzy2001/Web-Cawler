import requests
import jieba
from lxml import etree
import wordcloud
from matplotlib.pyplot import imread

#Here you need to download feasible images on your own, preferably a few with distinctly different colors.
#At the same time, you must understand the more basic knowledge of crawlers.

class Drawing(object):

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get_html(self):
        response = requests.get(self.url, self.headers)
        response.encoding = 'utf-8'
        return response.text

    def parse_data(self, data):
        html = etree.HTML(data)
        p_list = html.xpath('//*[@id="UCAP-CONTENT"]/p[@style="text-indent: 2em; font-family: 宋体; font-size: 12pt;"]')
        section1 = html.xpath('//*[@id="UCAP-CONTENT"]/p[5]/text()')[0]
        #print(section1)
        text = section1
        for p in p_list:
            if p.xpath('./text()'):
                section = p.xpath('./text()')[0]
                #print(section)
            else:
                section = p.xpath('./span/text()')[0]
                #print(section)
            text += section
        #print(text)
        return text

    def run(self):
        data = self.get_html()
        text = self.parse_data(data)
        ls = jieba.lcut(text)
        word_f_c = " ".join(ls)
        print(word_f_c)
        mask = imread('China.jpg')
        exclude = {'的', '和', '对', '以', '了', '中', '各', '把', '新', '不', '谋', '上',\
                   '化', '好', '守', '史', '还', '性', '其', '是', '为', '同', '到', '大',\
                   '最', '宽', '行', '时', '分', '做', '开', '六', '举', '再', '离', '住',\
                   '来', '七', '看', '促', '地', '正', '同', '也', '更', '给', '兴', '在',\
                   '水', '等', '用', '天', '女', '多', '边', '四', '是', '为', '上', '总',
                   '从'}
        w = wordcloud.WordCloud(font_path='msyh.ttc', mask=mask, max_words=2000,
                                max_font_size=90,  width=1000, height=700,
                                background_color='white', stopwords=exclude)
        w.generate(word_f_c)
        w.to_file("Twentieth National Congress of the Communist Party of China.png")

if __name__ == "__main__":
    url = 'http://www.gov.cn/xinwen/2022-10/25/content_5721685.htm'
    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    drawing = Drawing(url, headers)
    drawing.run()
