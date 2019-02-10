from xmlUnit import ReadXML
from xmlUnit import ReadTreeXML
from csvUnit import startReadCSV
from urllib import parse
from webCon import webCon
from tools.MoveFIle import MoveFile
from tools.DataUnit import DataUnit
import os
import uuid

APPKEY = ""
web = webCon()  # 实例化一个 webCon对象，下面所有的获取数据都从里面的方法得到
moveFile = MoveFile()  # 移动 csvUnit/csvlist下所有文件 到 csvUnit/csv_Last ；移动 xmlUnit/linklist下所有文件 到 xmlUnit/linkList_Last


def parseDetail(url, rule):
    pageDetail = web.con_ThenGetContent(url, rule)
    xpathCss_selector_Xml_Content = web.getextra().getXslt()  # 截取的xpath的xml规则文件，后面会保存到数据库，这里先不处理

    # 写入文件，查看一下
    id = uuid.uuid1()
    file_name = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\linkList_detail\\" + str(uuid.uuid1()) + ".xml"
    open(file_name, "wb").write(pageDetail)
    print(url+"写入完毕")


def Myparse(url, key):  # url可以作为前缀拼凑成完整的网页链接
    linksParseRule = key  # 教师list的url 的解析规则
    PageDetailRule = key + "_detail"  # 每一个教师信息的解析规则
    # 访问并读取网页内容

    pageResult = web.con_ThenGetContent(url, linksParseRule)  # 获取教师页所有链接
    print(type(pageResult))
    pass
    xpathCss_selector_Xml_Content = web.getextra().getXslt()  # 截取的xpath的xml规则文件
    # 写入文件，查看一下
    id = uuid.uuid1()
    file_name = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\linkList\\" + str(uuid.uuid1()) + ".xml"
    open(file_name, "wb").write(pageResult)

    # 开始取出 每一个教师的link规则
    linkListPath = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\linkList"
    readXmlTree = ReadTreeXML.ReadTreeXml(linkListPath)
    urlLinkList = readXmlTree.getUrlList()
    # print(urlLinkList)
    for urlIndex in range(len(urlLinkList)):
        detailPageUrl = parse.urljoin(url, urlLinkList[urlIndex])
        parseDetail(detailPageUrl, PageDetailRule)


if __name__ == '__main__':
    # 配置文件路径
    configFileName = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\config.xml"
    # configFileName = os.path.abspath(os.path.dirname(__file__))
    csvFilePath = os.path.dirname(__file__) + "/csvUnit"

    # xml 和csv 实例化
    readxml = ReadXML.ReadXml(configFileName)
    readcsv = startReadCSV.startReadCSV(csvFilePath)

    # csv 开始读，对象可返回 tuple（key） 和 dict
    readcsv.startReadUrlList()
    # 给全局变量APPKEY 赋值
    APPKEY = readxml.get_RootAttribute("appkey")

    # 配置连接属性
    web.setAppkey(APPKEY)


    #实例化一个存储到elasticsearch 对象
    dataUnit = DataUnit()
    #########################################以上为必须要执行的预备动作
    #

    for fileNameIndex in range(len(readcsv.getKeyFileName())):
        keyname = readcsv.getKeyFileName()[fileNameIndex]  #keyname为"学校名_学院名"
        listlinks = readcsv.getdic()[keyname]
        for linkIndex in range(len(listlinks)):
            link = listlinks[linkIndex][0]
            Myparse(link, keyname)
    moveFile.move_csvlistTo_Last()
    moveFile.move_linkListTo_Last()
