from xml.dom.minidom import parse
import xml.dom.minidom
import os
from tools.zhengze import zhengze
from tools.Mylog import Mylog
import csv

zhengze = zhengze()
mylog = Mylog("教师信息")
erolog = Mylog("教师信息错误日志")


class ReadDetailXML:
    def __init__(self):
        self.path = ""
        self.detail_dict = {}
        self.keyList = []

    def getself(self):
        return self

    def setFilePath(self, file_path):
        self.path = file_path
        self.detail_dict = ()
        self.keyList = []
        self._start_process()

    def _start_process(self):
        self.DOMTree = xml.dom.minidom.parse(self.path)
        self.root = self.DOMTree.documentElement
        self.name = self.root.getElementsByTagName("item")[0].getElementsByTagName("name")[0].childNodes[0].data.strip().replace(' ', '')

    def get_DetailDict(self):
        return self.detail_dict


if __name__ == '__main__':
    rd = ReadDetailXML()
    detail_path = "E:\\19年文件\\毕设爬虫\\spider\spider\\xmlUnit\\linkList_detail"
    # 获取详情文件夹所有文件名
    ListFiles = os.listdir(detail_path)

    for index in range(len(ListFiles)):
        try:
            file_path = detail_path + "\\" + ListFiles[index]  # detail xml文件路径
            rd.setFilePath(file_path, "南京大学_信息管理学院")
            data = []
            name = rd.name
            data.append(name)
            mylog.info(name)
            office = rd.office
            data.append(office)
            mylog.info(office)
            department = rd.department
            data.append(department)
            mylog.info(department)
            position = rd.position
            data.append(position)
            mylog.info(position)
            jobTitle = rd.jobTitle
            data.append(jobTitle)
            mylog.info(jobTitle)
            email = rd.email
            data.append(email)
            mylog.info(email)
            OfficePhone = rd.officePhone
            data.append(OfficePhone)
            mylog.info(OfficePhone)
            cellPhone = rd.cellphoneNumber
            data.append(cellPhone)
            mylog.info(cellPhone)
            researchAreas = rd.researchAreas
            data.append(researchAreas)
            mylog.info(researchAreas)
            researchProject = rd.researchProject
            data.append(researchProject)
            mylog.info(researchProject)
            book = rd.book
            data.append(book)
            mylog.info(book)
            print("OK")
        except IndexError as e:
            erolog.error(str(e))
