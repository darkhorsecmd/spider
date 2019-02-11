import requests
import os
from gooseeker import GsExtractor
from lxml import etree
from tools.RandomUserAgent import RandomUserAgent
from tools.IpAgency import IpAgency
import time

class webCon:
    def __init__(self):
        self.APPKEY = ""
        self.extra = GsExtractor()  # 生成xsltExtractor对象
        self.configpath = os.path.abspath(os.path.dirname(__file__))+"\\xmlUnit\\config.xml"
        self.Ipagency = IpAgency(configPath=self.configpath)

    def con_ThenGetContent(self, url, rule):
        # conn = request.urlopen(url)
        try:
            rd = RandomUserAgent()
            headers = {"User-Agent": rd.get_RanDomAgent()}
            #蛋疼的代理IP，等有机会自己搞一个，这里休眠一下，0.5秒 再请求应该是够的，错了再说！！！
            time.sleep(0.5)
            data = requests.get(url=url, headers=headers,timeout=500,proxies=self.Ipagency.getIpProxy()).text
            doc = etree.HTML(data)
            # doc = etree.HTML(conn.read())
            self.extra.setXsltFromAPI(APIKey=self.APPKEY, theme=rule)  # 获取规则文件，并读取
            content = self.extra.extract(doc)  # 更具xslt 解析的内容，xml 字节格式
            return content
        except BaseException:
            return b"conect error"

    def setAppkey(self, APPKEY):
        self.APPKEY = APPKEY

    def getextra(self):
        return self.extra
if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))+"\\xmlUnit\\config.xml"
    print(path)