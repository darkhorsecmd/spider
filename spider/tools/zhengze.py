import re
#目前只有返回 "南京大学_信息管理学院" 前面的大学名字和 后面的学院名字
class zhengze():
    def getSchollName(self,s):
        pattern = '.*(?=_)'
        return re.search(pattern=pattern,string=s).group(0)
    def getAcademy(self,s):
        pattern = '(?<=_).*'
        return re.search(pattern=pattern,string=s).group(0)

    def getEmail(self, s):
        pattern = '[\w]+(\.[\w]+)*@[\w]+(\.[\w]+)+'
        return re.search(pattern=pattern, string=s).group(0)

    def getPhoneNum(self, s):
        phoneNumPattern = '[1][3,4,5,7,8][0-9]\\d{8}'
        return re.findall(phoneNumPattern, s)

    def getTelNum(self, s):  # (+\d{2,3}[\s-]?)
        telPattern = '(\+\d{2})?[\s-]?(\d{2,3})?[\s-]?\d{7,8}'
        return re.search(pattern=telPattern, string=s).group(0)

    def getTitle(self, s):
        pattern = '[(教授)(副教授)(讲师)]'
        return re.findall(pattern, s)

    def getresearchAreas(self,testSentence):
        result = re.findall("从事\w*研究。*", testSentence)
        # print(result)
        if len(result) == 0:
            result = re.findall("研究领域(主要)?涉及[:：]?\w*。*", testSentence)
            # print(result)
            if len(result) == 0:
                result = re.findall("研究[(方向)(领域)][:：为是]?[\w“”]*。?", testSentence)
                # print(result)
                if len(result) == 0:
                    result = re.findall("科研方向[:：为是]?\w*。?", testSentence)
                    # print(result)
                    if len(result) == 0:
                        result = re.findall("(研究[\w、]+[,，。])", testSentence)
                    # print(result)
        return result

if __name__ == '__main__':
    zz = zhengze()
    print(zz.getSchollName("南京大学_信息管理学院_test_hello"))
    print(zz.getAcademy("南京大学_信息管理学院"))
    print(zz.getSchollName("南京大学_信息管理学院_detail1b7f97fb-35bc-11e9-8cd9-acd1b8a68732.xml"))
    print(zz.getEmail('邮箱:  ligang@nju.edu.cn'))

    sentence = '''

     办公室:  潘琦楼A217

    邮箱:  ligang@nju.edu.cn

    办公电话:  +86 025 89681397

    手机号码:  13951671420

    职称:  副教授

    开放咨询时间:  周四 10 am.-12 am.'''

    print(zz.getPhoneNum(sentence)[0])
    print(zz.getTelNum(sentence))
    print(" ".join(zz.getTitle(sentence)))



