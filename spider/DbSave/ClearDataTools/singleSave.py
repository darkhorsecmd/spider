import os
import torndb
from xmlUnit.ReadXML import ReadXml
from tools.Mylog import Mylog

log = Mylog("class_save")


class singleSave():
    ConfigXML_Path = os.path.abspath(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "\\xmlUnit\\config.xml"
    readxml = ReadXml(ConfigXML_Path)

    def init(self, max_conns=30):
        self.host = singleSave.readxml.get_ItemValue("mysql_host")
        self.database = singleSave.readxml.get_ItemValue("mysql_dbName")
        self.user = singleSave.readxml.get_ItemValue("mysql_user")
        self.pwd = singleSave.readxml.get_ItemValue("mysql_pass")

    def query(self, sentense):
        self.host = singleSave.readxml.get_ItemValue("mysql_host")
        self.database = singleSave.readxml.get_ItemValue("mysql_dbName")
        self.user = singleSave.readxml.get_ItemValue("mysql_user")
        self.pwd = singleSave.readxml.get_ItemValue("mysql_pass")
        self.conns = torndb.Connection(self.host, self.database, self.user, self.pwd)
        return self.conns.get(sentense)

    def insert_data(self, info_dict, table_dict):
        self.host = singleSave.readxml.get_ItemValue("mysql_host")
        self.database = singleSave.readxml.get_ItemValue("mysql_dbName")
        self.user = singleSave.readxml.get_ItemValue("mysql_user")
        self.pwd = singleSave.readxml.get_ItemValue("mysql_pass")
        for key in table_dict:
            table = key
            field_list = []
            field_list = table_dict[key]
            # 下面一行稍微复杂一点，field_list[i]意思是 字段，info_dict[field_list[i]]意思是每个字段表示的意思
            ls = [(field_list[i], info_dict[field_list[i]]) for i in range(len(field_list)) if info_dict[field_list[i]]]
            sentence = r'INSERT INTO %s (' % table + ','.join([i[0] for i in ls]) + \
                       ') VALUES (' + ','.join(['%r' % i[1] for i in ls]) + ');'
            # 这里应该将dict转化为一个合格的插入语句
            try:
                self.conns = torndb.Connection(self.host, self.database, self.user, self.pwd)
                print(self.conns.insert(sentence))
            except Exception as e:
                log.error("class=save :" + '{'+sentence+'}'+str(e))


if __name__ == '__main__':
    # 配置数据库
    # ConfigXML_Path = os.path.abspath(
    #     os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "\\xmlUnit\\config.xml"
    # readxml = ReadXml(ConfigXML_Path)
    # print("\n" + readxml.get_ItemValue("mysql_host"))
    #
    # path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))  # E:\19年文件\毕设爬虫\spider\spider
    # detail_path = path + "\\xmlUnit+\\linkList_detail"
    # print(detail_path)
    #
    # # 测试 Tornado 数据库连接
    # # https://www.itread01.com/content/1541881449.html  python3.7 需要改一下文件，参考前面url
    # db = torndb.Connection("127.0.0.1", "hhdx", "root", "xqweXQWE")
    # print(db.get('select * from  swszy where url_object_id="0214bcdc8ac01216943733d880b490c9"'))
    # db.close()

    # 下面具体测试
    info_dict = {'NameZH': '刘友华', 'ProfessionalTitle': '职称:教授', 'Email': '邮箱:liuyh@nju.edu.cn', 'Tel': '办公电话:',
                 'MobilePhone': '手机号码:', 'Address': '办公室:A325',
                 'IntegratedInformation': '刘友华)))))))))))))))))职称:教授)))))))))))))))))职位:)))))))))))))))))系别:信息管理科学系)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))办公室:A325)))))))))))))))))邮箱:liuyh@nju.edu.cn)))))))))))))))))办公电话:)))))))))))))))))手机号码:))))))))))))))))))))))))))))))))))开放咨询时间:2017.03.01-2017.07.15)每周一上午9:00-11:30'}
    table_dict = {'Researcherbasicinfo': ['NameZH', 'ProfessionalTitle', 'Email', 'Tel', 'MobilePhone', 'Address',
                                          'IntegratedInformation']}
    data_save = singleSave()
    # print(data_save.query('select * from  swszy where url_object_id="0214bcdc8ac01216943733d880b490c9"'))
    data_save.insert_data(info_dict, table_dict)
