from xmlUnit import ReadXML
from xmlUnit import ReadTreeXML
from csvUnit import startReadCSV
from urllib import request
from lxml import etree
from gooseeker import GsExtractor
from urllib import parse
from webCon import webCon
import os
import uuid
import time

APPKEY = ""
web = webCon()  # 实例化一个 webCon对象，下面所有的获取数据都从里面的方法得到


def parseDetail(url, rule):
    pageDetail = web.con_ThenGetContent(url, rule)
    xpathCss_selector_Xml_Content = web.getextra().getXslt()  # 截取的xpath的xml规则文件，后面会保存到数据库，这里先不处理

    # 写入文件，查看一下
    id = uuid.uuid1()
    file_name = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\linkList_detail\\" + str(uuid.uuid1()) + ".xml"
    open(file_name, "wb").write(pageDetail)

    # 待加入 代理池，这里先休眠
    time.sleep(2)

    pass


def Myparse(url, key):  # url可以作为前缀拼凑成完整的网页链接
    linksParseRule = key  # 教师list的url 的解析规则
    PageDetailRule = key + "_detail"  # 每一个教师信息的解析规则
    # 访问并读取网页内容

    pageResult = web.con_ThenGetContent(url, linksParseRule)  # 获取教师页所有链接
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
    #########################################以上为必须要执行的预备动作,读的配置文件
    #
    # print(readcsv.getdic())  #dict
    # print(readcsv.getKeyFileName())  ## key
    for fileNameIndex in range(len(readcsv.getKeyFileName())):
        keyname = readcsv.getKeyFileName()[fileNameIndex]
        listlinks = readcsv.getdic()[keyname]
        for linkIndex in range(len(listlinks)):
            # 每一个link 后面将作为平凑的前缀
            link = listlinks[linkIndex][0]
            Myparse(link, keyname)
