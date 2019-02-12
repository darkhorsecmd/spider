# spider各大学校教师信息公共爬虫

* ## 配置文件
    * ***目录***：spider\spider\xmlUnit\config.xml
    * **详细说明**
        * *属性*：'appkey'
            * 在网址：https://www.gooseeker.com申请的免费key
            ，起源是在github上找到的一个开源项目https://github.com/FullerHua/gooseeker，
            用于快速生成规则xstl，很方便，推荐使用
        * *tag*：'proxyUser'和'proxyPass'
            * 在网址https://www.abuyun.com/ 当中服务HTTP隧道购买得到的
            证书和密钥
        * *tag*:'esdb_host'
            * 开源搜索框架 Elasticsearch ,写了一个笔记：http://note.youdao.com/noteshare?id=b710d96846eb8098dd2038a5e6170302
            这里的'esdb_host'表示的意思是esdb的地址，这里暂时为本地地址
---

* ## 启动爬虫之前
    * ***目录***：spider\spider\csvUnit\csvlist\
    * **详细说明**
        * *制作教师链接list*
             * *需要知道的一些信息*
                  1. 找到一所大学的所有院系链接，链接一般藏在： *院系部门-》院系设置*
                  2. 找到该大学任意学院的教师列表页面：链接一般藏在各学院：导航栏的*师资力量* 栏目下
             * *需要做的事*：  
                  1. 手动搜集每个学院的 包含教师链接集合的页面地址，以南京大学计算机信息管理学院为例：
                     + http://im.nju.edu.cn/teachers.do?type=1&mid=4&mmid=41
                     + http://im.nju.edu.cn/teachers.do?type=4&mid=4&mmid=5dcefb89-45a3-11e5-91a4-002454d0cc1b
                     + http://im.nju.edu.cn/teachers.do?type=2&mid=4&mmid=7ddbacf0-2a46-11e5-8e21-002454d0cc1b
                     + http://im.nju.edu.cn/teachers.do?type=3&mid=4&mmid=80ceed23-2a46-11e5-8e21-002454d0cc1b  
                     + .....（左侧每一个导航）  
                     + 将上面几个地址复制粘贴到csv文件中，依次存储在*第一列*，保存文件名为：学院名； 这里保存为：信息管理学院；学院名最好和之前在院系设置里面看到的链接名字一样
             * 将上面那个csv文件保存在文件夹中 ，文件夹命名为：学校名；这里是：南京大学
        * 下载集搜客软件，10分钟时间学习创建xstl规则  
            * 需要定义两个规则（xstl）
                1. 第一个规则是为了获取所有教师链接，这里任意打开一个 教师链接集合页面，假设，现在是http://im.nju.edu.cn/teachers.do?type=1&mid=4&mmid=41  
                 **主题名**为：*学校名_学院名*,这里是*南京大学_信息管理学院*  
                 箱名任意，标签名：*link* ，这里因为程序中获取所有教师链接，标签名写死了，所以不可以随意更改。在软件里面测试一下，获取的链接是否完整，保证链接程序能全部获取
                2. 第二个规则是为了获取教师详情页面，这里任意打开一个教师的页面：假设现在是 教授页面下的 陈雅 教授，http://im.nju.edu.cn/teacherinfo.do?mid=4&mmid=41&tid=96230ccb-cabb-11e4-af7e-005056a62f9a
                 ，**主题名写：学校_学院_detail**，这里的主题名为：南京大学_信息管理学院_detail，箱名随意，标签名 你自己看着取，后面这个每个标签名在获取到的xml文件中以tag存在
---
* ## 启动爬虫
    * ***目录***：spider\spider\spider.py
    * ***启动方式***: 右击运行该py文件就可以了
---    
* ## 爬取结束后
     * 程序会自动将 spider\spider\csvUnit\csvlist 文件夹下的所有文件夹移动到 spider\spider\csvUnit\csvlist_Last
     * 将spider\spider\xmlUnit\linkList 文件夹下的所有文件移到spider\spider\xmlUnit\linkList_Last
---
* ## 你要的结果
    * ***存放目录*** spider\spider\xmlUnit\linkList_detail     
    * ***存放形式*** xml文件形式，命名方式：学校名_学院名_detail+UUID.xml           
---
* ## 如果您觉得我写的项目对您有益，麻烦点一下页面顶端的 star按钮，或者您也可以fork我的这个开源项目，感谢！