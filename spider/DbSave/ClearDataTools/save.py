import os
import torndb
import threading
from xmlUnit.ReadXML import ReadXml
from queue import Queue

class save(object):
    ConfigXML_Path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "\\xmlUnit\\config.xml"
    readxml = ReadXml(ConfigXML_Path)

    def init(self, max_conns=30):
        self.host = save.readxml.get_ItemValue("mysql_host")
        self.database = save.readxml.get_ItemValue("mysql_dbName")
        self.user = save.readxml.get_ItemValue("mysql_user")
        self.pwd = save.readxml.get_ItemValue("mysql_pass")
        self.idle_conn = Queue()
        self.pool_size = 0
        self.max_conns = max_conns
        self.conn_params = (self.host, self.database, self.user, self.pwd)
        self.poll_size_mutex = threading.Lock()

    def _get_conn_from_pool(self):
        if self.idle_conn.empty() and self.pool_size < self.max_conns:
            conn = torndb.Connection(*self.conn_params, time_zone="+8:00")
            self.poll_size_mutex.acquire()
            self.pool_size += 1
            self.poll_size_mutex.release()
            return conn
        return self.idle_conn.get()

    def query(self, *args, **kwargs):
        conn = self._get_conn_from_pool()
        res = conn.query(*args, **kwargs)
        self.idle_conn.put(conn)
        return res


    def insert_data(self,Info_dict):
        #这里应该将dict转化为一个合格的插入语句，默认一下子是插入所有数据
        pass

if __name__ == '__main__':
    # 配置数据库
    ConfigXML_Path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "\\xmlUnit\\config.xml"
    readxml = ReadXml(ConfigXML_Path)
    print("\n" + readxml.get_ItemValue("mysql_host"))

    path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))  # E:\19年文件\毕设爬虫\spider\spider
    detail_path = path + "\\xmlUnit+\\linkList_detail"
    print(detail_path)


    #测试 Tornado 数据库连接
    #https://www.itread01.com/content/1541881449.html  python3.7 需要改一下文件，参考前面url
    db = torndb.Connection("127.0.0.1","hhdx","root","xqweXQWE")
    print(db.get('select * from  swszy where url_object_id="0214bcdc8ac01216943733d880b490c9"'))
    db.close()