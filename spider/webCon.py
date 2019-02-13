import requests
import os
from gooseeker import GsExtractor
from lxml import etree
from tools.RandomUserAgent import RandomUserAgent
from tools.IpAgency import IpAgency
from tools.chrome import chrome


class webCon:
    #chrome启动的慢，所以尽量少启动，作为静态最合适
    chrome = chrome()  # 只会实例化一次

    def __init__(self):
        # 集搜客提供的API
        self.extra = GsExtractor()

        # ip代理商提供的服务
        self.Ipagency = IpAgency()

    def con_ThenGetContent(self, url, rule):
        rd = RandomUserAgent()
        headers = {"User-Agent": rd.get_RanDomAgent()}
        try:
            #requests 代理方式采集数据
            data = requests.get(url=url, headers=headers, timeout=500, proxies=self.Ipagency.getIpProxy()).text
            # data = requests.get(url=url, headers=headers,timeout=500).text  #不用代理方式
            doc = etree.HTML(data)
            # doc = etree.HTML(conn.read())
            self.extra.setXsltFromAPI(theme=rule)  # 获取规则文件，并读取
            content = self.extra.extract(doc)  # 更具xslt 解析的内容，xml 字节格式
            return content
        except Exception as e:
            #最好加一个日志
            print("requests hava some problem:" + str(e) + "try selenium way")

            try:
                # chrome 浏览器方式采集数据
                data = webCon.chrome.get_html(url=url)
                doc = etree.HTML(data)
                self.extra.setXsltFromAPI(theme=rule)  # 获取规则文件，并读取
                content = self.extra.extract(doc)  # 更具xslt 解析的内容，xml 字节格式
                return content
            except Exception as e1:
                #这里最好加一个日志

                try:
                    # 阿布云代理IP出错 requests 本机IP采集数据
                    data = requests.get(url=url, headers=headers,timeout=500).text  #不用代理方式
                except Exception as e2:
                    #加一个日志操作，warning
                    return str.encode((str(url) + ":" + str(e1)))

    def getextra(self):
        return self.extra


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\config.xml"
    print(path)
