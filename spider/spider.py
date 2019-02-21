from xmlUnit import ReadLinksXML
from csvUnit import startReadCSV
from urllib import parse
from webCon import webCon
from tools.MoveFIle import MoveFile
from tools.zhengze import zhengze
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
    file_name = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\linkList_detail\\" + rule + str(
        uuid.uuid1()) + ".xml"
    open(file_name, "wb").write(pageDetail)
    print(url + "写入完毕")


def Myparse(url, key):  # list页面的url可以作为前缀拼凑成完整的网页链接
    PageDetailRule = key + "_detail"  # 每一个教师信息的解析规则，同时也是esdb的doc_type
    # 开始取出 每一个教师的link规则
    linkListPath = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\linkList"
    readXmlTree = ReadLinksXML.ReadTreeXml(linkListPath)
    urlLinkList = readXmlTree.getUrlList()  # linkList 文件夹下的所有文件当中的link 大列表
    for urlIndex in range(len(urlLinkList)):
        detailPageUrl = parse.urljoin(url, urlLinkList[urlIndex])
        parseDetail(detailPageUrl, PageDetailRule)


# 此函数用于处理 一个学院的所有的链接写入文件,同时存入linkList文件夹下面
def parse_addLink(url, key):
    linksParseRule = key  # 教师list的url 的解析规则，同时也是 esdb的index
    pageResult = web.con_ThenGetContent(url, linksParseRule)  # 获取此url下的所有教师个人链接
    xpathCss_selector_Xml_Content = web.getextra().getXslt()  # 截取的xpath的xml规则文件
    # 写入文件，查看一下
    if pageResult is not None:
        id = uuid.uuid1()
        file_name = os.path.abspath(os.path.dirname(__file__)) + "\\xmlUnit\\linkList\\" + key + str(
            uuid.uuid1()) + ".xml"
        open(file_name, "wb").write(pageResult)


if __name__ == '__main__':
    # 配置csv文件路径
    csvFilePath = os.path.dirname(__file__) + "/csvUnit"
    # csv 实例化
    readcsv = startReadCSV.startReadCSV(csvFilePath)
    # csv 开始读，对象可返回 tuple（key） 和 dict  这里就直接读了csvlist文件夹下的所有大学 分别存了一个list
    readcsv.startReadUrlList()
    # 实例化一个正则对象
    zz = zhengze()

    # 实例化一个存储到elasticsearch 对象
    # dataUnit = DataUnit()
    #########################################以上为必须要执行的预备动作
    for fileNameIndex in range(len(readcsv.getKeyFileName())):
        keyname = readcsv.getKeyFileName()[fileNameIndex]  # keyname为"学校名_学院名"
        scholl_name = zz.getSchollName(keyname)  # 获取学校名字 前缀
        academy_name = zz.getAcademy(keyname)  # 获取学院名字 后缀
        listlinks = readcsv.getdic()[keyname]
        qianzhui = ""
        for linkIndex in range(len(listlinks)):
            link = listlinks[linkIndex][0]
            qianzhui = link  # 这个前缀只是为了下面的Myparse里面的url做拼接用
            parse_addLink(link, keyname)  # 一下子就存储了一个学院的linklist 通过xml方式
        Myparse(qianzhui, keyname)  # 准备解析 linklist下面的所有链接
        moveFile.move_linkListTo_Last(scholl_name,academy_name)  # 解析完了，就将linklist下面的所有文件移到 linkList_Last文件夹下面
        moveFile.move_csvlistTo_Last(scholl_name,academy_name)  # 解析完了csvlist里面的链接，应该也要移动一下才对！
        print("ok")
    # 退出浏览器
    webCon.chrome.quit()
