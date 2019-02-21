from xml.dom.minidom import parse
import xml.dom.minidom
import os
from tools.zhengze import zhengze

zhengze = zhengze()
class ReadDetailXML:
    def __init__(self):
        self.path = ""
        self.name=''
        self.detail_dict = {}
        self.keyList = []
        pass
    def getself(self):
        return self
    def setFilePath(self, file_path, flag):
        self.path = file_path
        self.detail_dict = ()
        self.keyList = []
        self._start_process(flag)
    def getname(self):
        return self.name
    def getwait_jobTitle(self):
        return self.wait_jobTitle
    def getwait_position(self):
        return self.wait_position
    def getwait_department(self):
        return self.wait_department
    def getwait_office(self):
        return self.wait_office
    def getwait_email(self):
        return self.wait_email
    def getwait_cellphoneNumber(self):
        return self.wait_cellphoneNumber
    def getwait_officePhone(self):
        return self.wait_officePhone
    def getwait_researchAreas(self):
        return self.wait_researchAreas
    def getwait_researchProject(self):
        return self.wait_researchProject

    def _start_process(self, flag):
        self.DOMTree = xml.dom.minidom.parse(self.path)
        self.root = self.DOMTree.documentElement
        if (flag == "东南大学_经济管理学院"):
            self.name=self.root.getElementsByTagName("item")[0].getElementsByTagName("name")[0].childNodes[0].data.strip().replace(' ','')
            self.wait_office=self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_office")[0].childNodes[0].data
            self.wait_officePhone =self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_officePhone")[0].childNodes[0].data
            self.wait_email = self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_email")[0].childNodes[0].data
        if (flag == "南京大学_信息管理学院"):
            self.name=self.root.getElementsByTagName("item")[0].getElementsByTagName("name")[0].childNodes[0].data.strip().replace(' ','')
            self.wait_jobTitle=self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_jobTitle")[0].childNodes[0].data.strip().replace(' ','')
            self.wait_position=self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_position")[0].childNodes[0].data.strip().replace(' ','')
            self.wait_department=self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_department")[0].childNodes[0].data.strip().replace(' ','')
            self.wait_office=self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_office")[0].childNodes[0].data.strip().replace(' ','')
            self.wait_email=self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_email")[0].childNodes[0].data.strip().replace(' ','')
            self.wait_cellphoneNumber=self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_cellphoneNumber")[0].childNodes[0].data.strip().replace(' ','')
            self.wait_officePhone=self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_officePhone")[0].childNodes[0].data.strip().replace(' ','')
            self.wait_researchAreas=self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_researchAreas")[0].childNodes[0].data.strip().replace(' ','')
            self.wait_researchProject=self.root.getElementsByTagName("item")[0].getElementsByTagName("wait_researchProject")[0].childNodes[0].data.strip().replace(' ','')

    def get_DetailDict(self):
        return self.detail_dict


if __name__ == '__main__':
    path = os.path.abspath(
        os.path.dirname(__file__)) + "\\linkList_detail\\南京大学_信息管理学院_detail0dced60c-35bc-11e9-bf4d-acd1b8a68732.xml"
    rd = ReadDetailXML()
    rd.setFilePath(path, "南京大学_信息管理学院")
    # print(rd.name)
    print(zhengze.getEmail(rd.wait_email))
    print(zhengze.getTitle(rd.getwait_jobTitle()))
    print(path)
