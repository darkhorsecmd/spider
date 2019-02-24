from xml.dom.minidom import parse
import xml.dom.minidom
import os
from tools.zhengze import zhengze
from tools.Mylog import Mylog

mylog = Mylog("详细页面解析")


class ReadDetailXML:
    def __init__(self):
        self.path = ""
        self.detail_dict = {}
        # 获取 Mysql_field_config.xml 文件里面的数据库字段配置信息
        self.filed_dict = {}
        self.setFieldDict()  # 这个类方法给 filed_dict{}字典填充 Mysql_field_config.xml里面的内容

        self.table_dict = {}
        self.temp_list = []

    def gettable_dict(self):
        # return :{'Researcherbasicinfo': ['NameZH', 'ProfessionalTitle', 'Email', 'Tel', 'MobilePhone', 'Address', 'IntegratedInformation']}
        self.temp_list.clear()  # 首先要清楚一下上一次使用的内容
        # 先获取所有要用的table名字存入 temp_list 列表中
        for key in self.detail_dict:
            table = self.filed_dict[key]
            if table not in self.temp_list:
                self.temp_list.append(table)
        # 依次取出 table1
        for index in range(len(self.temp_list)):
            lists=[]  #预先准备好一个lists，存入属于这个table的字段
            for key in self.detail_dict:  # 遍历detail的key
                table = self.filed_dict[key]  # 取出detail里面的table2名字
                if table == self.temp_list[index]:  # 如果table2和table1名字一样
                    lists.append(key)  #这个字段是属于这个table的，则将他加入list
            self.table_dict[self.temp_list[index]] = lists  #detail里面遍历完毕，准备取出第二个table
        return  self.table_dict

    def setFilePath(self, file_path):
        self.path = file_path
        self.detail_dict.clear()
        self._start_process()

    def _start_process(self):
        self.DOMTree = xml.dom.minidom.parse(self.path)
        self.root = self.DOMTree.documentElement

        for key in self.filed_dict:
            # 获取传入的detail文件里面每一个可能存在的标签data
            # key 为字段名
            try:
                # 有可能获取不到，属于正常现象
                value = self.root.getElementsByTagName("item")[0].getElementsByTagName(key)[0].childNodes[
                    0].data.strip().replace(' ', ')')
                try:
                    # 有可能字段会在编程或在任意时间段误操作，捕获一下很必要
                    self.detail_dict[key] = "".join(value.split())
                except Exception as e:
                    mylog.error(self.path + "--" + key + ":" + str(e))
            except IndexError as d:
                # 缺少某个字段，在这里被捕获，但暂时不做任何处理，因为是正常现象
                # mylog.debug(str(d))
                pass

    def addDetailDict(self, key, value):
        self.detail_dict[key] = value

    def get_DetailDict(self):
        #return : {'NameZH': '刘友华', 'ProfessionalTitle': '职称:教授', 'Email': '邮箱:liuyh@nju.edu.cn'}
        return self.detail_dict

    def get_FieldDict(self):
        #return : {'Url': 'Spiderinfo', 'SpiderTime': 'Spiderinfo', 'NameZH': 'Researcherbasicinfo'}
        return self.filed_dict

    def setFieldDict(self):
        path = os.path.abspath(os.path.dirname(__file__)) + "\\Mysql_field_config.xml"
        DOMTree = xml.dom.minidom.parse(path)
        collection = DOMTree.documentElement
        # key 是数据表字段名
        # value是表名
        MysqlNodeList = collection.getElementsByTagName("filed")
        for node in MysqlNodeList:
            key = node.childNodes[0].data
            value = node.getAttribute("table")
            self.filed_dict[key] = value


if __name__ == '__main__':
    path = os.path.abspath(
        os.path.dirname(__file__)) + "\\linkList_detail\\南京大学_信息管理学院_detail1c36bd83-37f9-11e9-8893-acd1b8a68732.xml"
    rd = ReadDetailXML()
    rd.setFilePath(path)
    InfoDict = rd.get_DetailDict()
    if InfoDict.__len__() != 0:
        print(InfoDict)
    else:
        print("InfoDict Is None")
    print("ok")
    print(rd.gettable_dict())
    # print(rd.get_FieldDict())