import re


# 目前有返回 "南京大学_信息管理学院" 前面的大学名字和 后面的学院名字
# 不需要实例化对象，直接用类方法就可以
class zhengze():
    @classmethod
    def getSchollName(cls, s):
        # demo:s=南京大学_信息管理学院_test_hello
        # return:南京大学_信息管理学院_test
        pattern = '.*(?=_)'
        return re.search(pattern=pattern, string=s).group(0)

    @classmethod
    def getAcademy(cls, s):
        # demo:s=南京大学_信息管理学院_test_hello
        # return:信息管理学院_test_hello
        pattern = '(?<=_).*'
        return re.search(pattern=pattern, string=s).group(0)

    @classmethod
    def getEmail(cls, s):
        # demo:s=邮箱: ligang @ nju.edu.cn
        # return:ligang@nju.edu.cn
        pattern = '[\w]+(\.[\w]+)*@[\w]+(\.[\w]+)+'
        return re.search(pattern=pattern, string=s).group(0)

    @classmethod
    def getPhoneNum(cls, s):
        # demo:s=手机号码:  13951671420  混乱字符
        # return: 13951671420
        phoneNumPattern = '[1][3,4,5,7,8][0-9]\\d{8}'
        return re.findall(phoneNumPattern, s)

    @classmethod
    def getTelNum(cls, s):  # (+\d{2,3}[\s-]?)
        # demo:s= 办公号码：+86 025 89681397 asdf
        # return:+86 025 89681397
        telPattern = '(\+\d{2})?[\s-]?(\d{2,3})?[\s-]?\d{7,8}'
        return re.search(pattern=telPattern, string=s).group(0)

    @classmethod
    def getTitle(cls, s):
        # demo:s=    职称:  副教授,讲师开放咨询时间
        # return: 副教授讲师
        pattern = '[(教授)(副教授)(讲师)]{0,1}'
        title = "".join(re.findall(pattern, s))
        return title

    @classmethod
    def getresearchAreas(cls, testSentence):
        #暂时没有深层次测试，后面会补充
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
    print(zhengze.getSchollName("南京大学_信息管理学院_test_hello"))
    print(zhengze.getAcademy("南京大学_信息管理学院_test_hello"))
    print(zhengze.getSchollName("南京大学_信息管理学院_detail1b7f97fb-35bc-11e9-8cd9-acd1b8a68732.xml"))
    print(zhengze.getEmail('邮箱:  ligang@nju.edu.cn'))
    sentence = '''

     办公室:  潘琦楼A217

    邮箱:  ligang@nju.edu.cn

    办公电话:  +86 025 89681397

    手机号码:  13951671420

    职称:  副教授,讲师

    开放咨询时间:  周四 10 am.-12 am.'''

    print(zhengze.getPhoneNum("asdf手机号码:  13951671420  混乱字符")[0])
    print(zhengze.getTelNum(sentence))
    print(zhengze.getTitle(sentence))
