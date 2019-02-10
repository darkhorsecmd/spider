from elasticsearch import Elasticsearch
import json

es = Elasticsearch()
def createEdb():
    mapping = {
        'properties': {
            'title': {
                'type': 'text',
                'analyzer': 'ik_max_word',
                'search_analyzer': 'ik_max_word'
            }
        }
    }
    es.indices.delete(index='news', ignore=[400, 404])
    es.indices.create(index='news', ignore=400)
    result = es.indices.put_mapping(index='news', doc_type='politics', body=mapping)
    print(result)

def insertEdb():
    datas = [
        {
            'title': '美国1留给伊拉克的是个烂摊子吗',
            'url': 'http://view.news.qq.com/zt2011/usa_iraq/index.htm',
            'date': '2011-12-16'
        },
        {
            'title': '公安部1：各地校车将享最高路权',
            'url': 'http://www.chinanews.com/gn/2011/12-16/3536077.shtml',
            'date': '2011-12-16'
        }
        # {
        #     'title': '中韩渔警冲突调查：韩警平均每天扣1艘中国渔船',
        #     'url': 'https://news.qq.com/a/20111216/001044.htm',
        #     'date': '2011-12-17'
        # },
        # {
        #     'title': '中国驻洛杉矶领事馆遭亚裔男子枪击 嫌犯已自首',
        #     'url': 'http://news.ifeng.com/world/detail_2011_12/16/11372558_0.shtml',
        #     'date': '2011-12-18'
        # }
    ]

    for data in datas:
        es.index(index='news', doc_type='politics', body=data)

def searchAllEdb():
    result = es.search(index='news', doc_type='politics')
    print(result)

def searchTitleEdb():
    dsl = {
        'query':{
            'match':{
                'title':'中国领事馆'
            }
        }
    }
    result = es.search(index='news',doc_type='politics',body=dsl)
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__ == '__main__':
    insertEdb()
    # searchAllEdb()
    # searchTitleEdb()