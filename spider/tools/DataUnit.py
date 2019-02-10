from elasticsearch import Elasticsearch
from xmlUnit import ReadXML
import os


class DataUnit:
    configFileName = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + "\\xmlUnit\\config.xml"
    read = ReadXML.ReadXml(configFileName)
    host = read.get_ItemValue("esdb_host")  # 配置静态esdb 数据库地址

    def __init__(self):
        self.es = Elasticsearch(hosts="127.0.0.1")
        self.index = ""
        self.doc_type = ""

    #需要显示调用此函数
    def createIndex(self,index):
        self.index=index
        result = self.es.indices.create(index=self.index)
        if result["acknowledged"] is not True:
            print("创建index失败，你可以尝试删除该index，然后再运行此处代码")
            exit(1)
    #需要显示调用
    def setDoctype(self, doc_type):
        # 插入数据时候用得到；说明下6x之后一个index对应一个type
        self.doc_type = doc_type
    #需要显示调用
    def insertData(self, data):
        if self.doc_type != "":
            self.es.index(index=self.index, doc_type=self.doc_type, body=data)
        else:
            print('Please ensure set "doc_type"')


if __name__ == '__main__':
    dataunit = DataUnit()
    dataunit.createIndex("测试")
    dataunit.setDoctype("news_report")
    datas = [
        {
            'title': '美国留给伊拉克的是个烂摊子吗',
            'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
            'date': '2011-12-16'
        },
        {
            'title': '公安部：各地校车将享最高路权',
            'url': 'http://www.chinanews.com/gn/2011/12-16/3536077.shtml',
            'date': '2011-12-16'
        },
        {
            'title': '中韩渔警冲突调查：韩警平均每天扣1艘中国渔船',
            'url': 'https://news.qq.com/a/20111216/001044.htm',
            'date': '2011-12-17'
        },
        {
            'title': '中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首',
            'url': 'http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml',
            'date': '2011-12-18'
        }
    ]
    for data in datas:
        dataunit.insertData(data=data)
