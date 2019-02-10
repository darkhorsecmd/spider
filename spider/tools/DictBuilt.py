# 自定义构造字典
class EsDatadict():
    def __init__(self):
        self.dict = {}

    def addToDict(self, key, value):
        self.dict[key] = value

    def getDict(self):
        return self.dict


if __name__ == '__main__':
    esdata = EsDatadict()
    esdata.addToDict('sex', 'top')
    esdata.addToDict("hello", "word")
    print(esdata.getDict())
