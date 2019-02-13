import re
#目前只有返回 "南京大学_信息管理学院" 前面的大学名字和 后面的学院名字
class zhengze():
    def getSchollName(self,s):
        pattern = '.*(?=_)'
        return re.search(pattern=pattern,string=s).group(0)
    def getAcademy(self,s):
        pattern = '(?<=_).*'
        return re.search(pattern=pattern,string=s).group(0)

if __name__ == '__main__':
    zz = zhengze()
    print(zz.getSchollName("南京大学_信息管理学院"))
    print(zz.getAcademy("南京大学_信息管理学院"))

