from gooseeker import GsExtractor
from urllib import request
from lxml import etree
import requests
from tools.RandomUserAgent import RandomUserAgent

class webCon:
    def __init__(self):
        self.APPKEY = ""
        self.extra = GsExtractor()  # 生成xsltExtractor对象

    def con_ThenGetContent(self, url, rule):
        # conn = request.urlopen(url)
        # conn  = requests.get(url=url,hea)
        rd  = RandomUserAgent()
        headers = {"User-Agent": rd.get_RanDomAgent()}
        data = requests.get(url=url,headers=headers).text
        conn = etree.HTML(data)
        doc = etree.HTML(conn.read())
        self.extra.setXsltFromAPI(APIKey=self.APPKEY, theme=rule)  # 获取规则文件，并读取
        content = self.extra.extract(doc)  # 获取教师url 解析到的xml文件
        return content

    def setAppkey(self, APPKEY):
        self.APPKEY = APPKEY

    def getextra(self):
        return self.extra
