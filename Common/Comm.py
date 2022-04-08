"""
公共层
"""
import json
import os
import random

import requests
import xlrd

from Okmarts_test_front.save_report_history.save_report_history import Get_History
from pachong1.userAgent import UserAgent


class Common:

    def get_sess(self):
        sess = requests.session()
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/usr/userLogin'
        data = {"userAccount": "979172251@qq.com", "password": "a123456", "type": 0}
        data = json.dumps(data)
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '64',
                  'Accept': 'application/json,text/plain,*/*', 'X-Access-Token': 'null',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/', 'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.post(url=url, data=data, headers=header)
        token = res.json()['result']['token']
        assert res.json()['message'] == '操作成功！'
        return sess, token

    # 快速将FIDDLER中的handers转化为相应的格式
    def get_header(self, data):
        """
        快速的将 fiddler 中获取的请求头数据 转换为请求需要的 json\dict 格式
        :param data:  从 fiddler 抓取下来的请求头元数据
        :return:
        """
        string = data.replace(" ", '')
        li = string.split('\n')
        dict = {}
        for i in range(len(li) - 1):
            info = li[i].split(":", 1)
            dict[info[0]] = info[-1]
        print(dict)

    # 从用户表中随机选取一个账户
    def random_account(self):
        book = xlrd.open_workbook(r"C:\Users\admin\Desktop\okmarts\O&Kmark\okmarts账户.xls")
        sh = book.sheet_by_name('Sheet1')
        nrows = sh.nrows  # 获取行数
        ncols = sh.ncols  # 获取列数
        random_row = random.randint(1, nrows - 1)  # 随机行数
        userAgent = sh.cell_value(rowx=random_row, colx=0)
        password = sh.cell_value(rowx=random_row, colx=1)
        return userAgent, password

    # 获取随机账户登录后的session
    def random_sess(self):
        sess = requests.session()
        userinfo = self.random_account()
        useraccount = userinfo[0]
        password = userinfo[1]
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/usr/userLogin'
        data = {"userAccount": f"{useraccount}", "password": f"{password}", "type": 0}
        data = json.dumps(data)
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '64',
                  'Accept': 'application/json,text/plain,*/*', 'X-Access-Token': 'null',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/', 'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.post(url=url, data=data, headers=header)
        token = res.json()['result']['token']
        assert res.json()['message'] == '操作成功！'
        return sess, token

    # 随机账户
    def random_userAccount(self):
        email_list = ['qq.com', '163.com', 'gmail.com', 'netzero.net', 'zamnet.zm', 'comcast.net', 'cs.com',
                      'verizon.net', 'aviso.ci', 'kalianet.to', 'caron.se', 'terra.es', 'eunet.at', 'iway.na']
        random_userAccount = 'test' + f'{random.randint(1, 999999)}' + '@' + f'{random.choice(email_list)}'
        return random_userAccount

    # 生成30或者31位账户
    def random_userAccount_30or31(self, len):
        if len == 31:
            userAccount = "test" + f'{random.randint(11111111111111111111, 99999999999999999999)}' + "@" + "qq.com"
        elif len == 30:
            userAccount = "test" + f'{random.randint(1111111111111111111, 9999999999999999999)}' + "@" + "qq.com"
        else:
            userAccount = None
        print(userAccount)
        return userAccount

    # 输出报告
    def get_report(self):
        # 1 、 生成json文件
        print("正在生成JSON文件".center(76, '-'))
        cmd = r"pytest C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\main\testmain.py " \
              r"--alluredir=C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\tmp  --clean-alluredir "
        os.system(cmd)

        print("正在复制配置信息文件".center(76, '-'))
        # 2、 复制配置文件到json文件中
        cmd1 = r'copy C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\alluer-environment\environment.properties.properties' \
               r' C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\tmp\environment.properties '
        os.system(cmd1)

        print("正在生成报告".center(76, '-'))
        # 3、生成报告
        cmd2 = r"allure generate C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\tmp -o " \
               r"C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\report --clean "
        os.system(cmd2)
        print("报告生成完毕！！！！".center(76, '-'))

        # 4、 替换历史记录文件
        print("正在生成历史趋势文件".center(76, '-'))
        Get_History().get_history()

        # 5、为报告开启端口，共享查看
        # print('正在开启端口，分享报告')
        # cmd3 = r'allure open -h 192.168.81.102 -p 8885 C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\report'
        # os.system(cmd3)

    # 查询首页商品ID
    def select_homegoods_id(self):
        info = self.get_sess()
        sess = info[0]
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/homePage/getHomeGoods'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{info[1]}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.get(url=url, headers=header)
        li = res.json()["result"]['specialOfTheMonth']
        ids = []
        for i in li:
            ids.append(i['id'])
        return ids

    # 随机获取一条商品数据
    def select_goodsinfo(self):
        info = self.get_sess()
        sess = info[0]
        user_agent = random.choice(UserAgent().useragent_list())
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/goods/fuzzyquery_byname_list?fuzzyQueryName=5&pageNo=1&pageSize=11&brands=&type=&origins=&sortType=1'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{info[1]}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': f'{user_agent}',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.get(url=url, headers=header)
        print(res.json())
        total_page = res.json()['result']['pages']
        ran_page = random.randint(1, total_page)
        url1 = url.replace('pageNo=1', f'pageNo={ran_page}')
        result = sess.get(url=url1, headers=header)
        infos = result.json()['result']['records']
        ran_info = random.choice(infos)
        return ran_info

    #将数据写入json文件中
    def get_goodsinfo(self):
        info = self.get_sess()
        sess = info[0]
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/goods/fuzzyquery_byname_list?fuzzyQueryName=5&pageNo=1&pageSize=11&brands=&type=&origins=&sortType=1'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{info[1]}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.get(url=url, headers=header)
        total_page = res.json()['result']['pages']
        li = []
        for i in range(1,100):
            res = sess.get(url = url.replace("pageNo=1",f"pageNo={i}"),headers=header)
            goodsinfo = res.json()['result']['records']
            for info in goodsinfo:
                print(info)
                li.append(info)
        with open(r"C:\Users\admin\PycharmProjects\pythonProject\sss.json", "w") as f:
            json.dump(li, f)

    # 查询购物车中的商品
    def select_shopcar_goodsinfo(self):
        info = self.get_sess()
        sess = info[0]
        url = 'http://18.118.13.94:81/jeecg-boot/my/shoppingCart/list?pageNo=1&pageSize=100'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{info[1]}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.get(url=url, headers=header)
        infos = res.json()['result']['records']
        shopcar_infos = []
        for info in infos:
            shopcar_dict = {}
            id = info['id']  # 购物车定位ID
            goodsname = info['goodsName']  # 商品名称
            goodsprince = info['goodsPrice']  # 商品价格
            goodsid = info['goodsid']  # 商品id
            goodsamount = info['goodsamount']  # 购物车商品数量
            stock = info['stock']  # 商品库存
            totalprice = info['totalprice']  # 商品总价
            shopcar_dict['id'] = id
            shopcar_dict['goodsname'] = goodsname
            shopcar_dict['goodsprince'] = goodsprince
            shopcar_dict['goodsid'] = goodsid
            shopcar_dict['goodsamount'] = goodsamount
            shopcar_dict['stock'] = stock
            shopcar_dict['totalprice'] = totalprice
            shopcar_infos.append(shopcar_dict)
        random_shopcar_info = random.choice(shopcar_infos)  # 随机选择一条购物车商品数据
        print(random_shopcar_info)
        return random_shopcar_info

    # 返回购物车商品 id 的列表
    def select_shopcar_ids(self):
        info = self.get_sess()
        sess = info[0]
        url = 'http://18.118.13.94:81/jeecg-boot/my/shoppingCart/list?pageNo=1&pageSize=100'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{info[1]}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.get(url=url, headers=header)
        infos = res.json()['result']['records']
        # print(infos)
        shopcar_infos = []
        for info in infos:
            id = info["id"]
            shopcar_infos.append(id)
        return shopcar_infos

    def select_address_info(self):
        info = self.get_sess()
        sess = info[0]
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/homePage/getAddressList?pageNo=1&pageSize=10'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{info[1]}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.get(url=url, headers=header)
        infos = res.json()['result']
        ids = []
        for info in infos:
            ids.append(info['id'])
        return ids

    # 拼接 多个id 为 “id1，id2，id3” 类型
    def Splicing_id(self, num, li):
        ids = random.sample(li, num)
        a = ''
        for id in ids:
            a += id + ','
        res = a[:-1]
        return res

    def splicing_all_id(self, li):
        """
        拼接一个列表中的所有id
        :param li: 传入一个列表
        :return: 返回用逗号链接的所有id
        """
        a = ''
        for id in li:
            a += id + ','
        res = a[:-1]
        return res

    def first_name(self):
        first_name = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤',
                      '许', '何', '吕', '施', '张',
                      '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章', '云', '苏', '潘',
                      '葛', '奚', '范', '彭', '郎',
                      '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳', '酆', '鲍', '史', '唐', '费', '廉', '岑',
                      '薛', '雷', '贺', '倪', '汤',
                      '滕', '殷', '罗', '毕', '郝', '邬', '安', '常', '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元',
                      '卜', '顾', '孟', '平', '黄',
                      '和', '穆', '萧', '尹', '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成',
                      '戴', '谈', '宋', '茅', '庞',
                      '熊', '纪', '舒', '屈', '项', '祝', '董', '梁', '杜', '阮', '蓝', '闵', '席', '季', '麻', '强', '贾', '路', '娄',
                      '危', '江', '童', '颜', '郭',
                      '梅', '盛', '林', '刁', '钟', '丘', '徐', '邱', '骆', '高', '夏', '蔡', '田', '樊', '胡', '凌', '霍', '虞', '万',
                      '支', '柯', '昝', '管', '卢',
                      '莫', '经', '房', '裘', '缪', '干', '解', '应', '宗', '丁', '宣', '贲', '邓', '单', '杭', '洪', '包', '诸', '左',
                      '石', '崔', '吉', '钮', '龚',
                      '程', '嵇', '邢', '滑', '裴', '陆', '荣', '翁', '荀', '羊', '於', '惠', '甄', '曲', '家', '封', '芮', '羿', '储',
                      '靳', '汲', '邴', '糜', '松',
                      '井', '段', '富', '巫', '乌', '焦', '巴', '弓', '牧', '隗', '山', '谷', '车', '侯', '宓', '蓬', '全', '郗', '班',
                      '仰', '秋', '仲', '伊', '宫',
                      '宁', '仇', '栾', '暴', '甘', '钭', '厉', '戎', '祖', '武', '符', '刘', '景', '詹', '束', '龙', '叶', '幸', '司',
                      '韶', '郜', '黎', '蓟', '薄',
                      '印', '宿', '白', '怀', '蒲', '台', '从', '鄂', '索', '咸', '籍', '赖', '卓', '蔺', '屠', '蒙', '池', '乔', '阴',
                      '郁', '胥', '能', '苍', '双',
                      '闻', '莘', '党', '翟', '谭', '贡', '劳', '逢', '逄', '姬', '申', '扶', '堵', '冉', '宰', '郦', '雍', '璩', '桑',
                      '桂', '濮', '牛', '寿', '通',
                      '边', '扈', '燕', '冀', '郏', '浦', '尚', '农', '温', '别', '庄', '晏', '柴', '瞿', '阎', '充', '慕', '连', '茹',
                      '习', '宦', '艾', '鱼', '容',
                      '向', '古', '易', '慎', '戈', '廖', '庚', '终', '暨', '居', '衡', '步', '都', '耿', '满', '弘', '匡', '国', '文',
                      '寇', '广', '禄', '阙', '东',
                      '欧', '殳', '沃', '利', '蔚', '越', '夔', '隆', '师', '巩', '厍', '聂', '晁', '勾', '敖', '融', '冷', '訾', '辛',
                      '阚', '那', '简', '饶', '空',
                      '曾', '毋', '沙', '乜', '养', '鞠', '须', '丰', '巢', '关', '蒯', '相', '查', '荆', '红', '游', '竺', '权', '逯',
                      '盖', '益', '桓', '公', '晋',
                      '楚', '阎', '法', '汝', '鄢', '涂', '钦', '归', '海', '岳', '帅', '缑', '亢', '况', '后', '有', '琴', '商', '牟',
                      '佘', '佴', '伯', '赏', '墨',
                      '哈', '谯', '笪', '年', '爱', '阳', '佟', '言', '福']
        random_firstname = random.choice(first_name)
        return random_firstname

    def last_name(self):
        second_name = ['瑾', '雨', '钰', '静', '云', '珺', '惠', '惠', '晴', '岚', '云', '晴', '怡', '裕', '涵', '惠', '涵', '雯', '寒',
                       '润', '秉', '晴', '淑', '珺', '云', '舒', '素', '花', '岚', '清', '寒', '涵', '岚', '欣', '熙', '岚', '寒', '茹',
                       '寒', '岚', '正', '琳', '淑', '惠', '寒', '涵', '晴', '妍', '榕', '寒', '云', '茵', '茵', '惠', '洁', '雨', '翔',
                       '淑', '晴', '珺', '清', '梓', '雯', '雯', '雯', '茜', '云', '清', '秀', '欣', '惠', '茜', '茜', '舒', '婷', '晓',
                       '芷', '欣', '曦', '婷', '莉', '东', '巧', '佳', '秀', '新', '依', '欣', '梦', '菁', '泽', '怡', '陈', '婧', '美',
                       '悦', '莹', '莉', '德', '燕', '瑛', '鹤', '蓉', '佳', '蔡', '婧', '斯', '恺', '珂', '小', '成', '倩', '优', '长',
                       '瑜', '姝', '春', '华', '妍', '娉', '燕', '妍', '静', '禾', '妍', '惋', '清', '茜', '涵', '惠', '茵', '岚', '茜',
                       '媛', '珺', '茹', '涵', '翔', '雨', '思', '寒', '茜', '茜', '涵', '淑', '辰', '贞', '舒', '清', '茵', '淑', '媛',
                       '琳', '君', '云', '寒', '云', '岚', '淑', '颜', '真', '雯', '晴', '雯', '雯', '清', '青', '妍', '芬', '恬', '芙',
                       '宸', '翾', '丽', '悦', '桐', '铭', '睿', '莉', '长', '丽', '夕', '琳', '燕', '善', '琴', '筱', '旭', '蝾', '怡',
                       '莉', '芹', '翔', '晴', '晴', '雅', '茹', '若', '娅', '翔', '惠', '云', '茹', '雯', '寒', '舒', '雅', '雯', '岚',
                       '雯', '茜', '寒', '涵', '晴', '茜', '云', '岚', '茵', '莉', '梦', '涵', '茵', '晴', '岚', '涵', '雯', '惠', '寒',
                       '淑', '岚', '婷', '梓', '秀', '瑶', '芝', '娅', '树', '小', '厦', '卷', '欣', '世', '艳', '丹', '玲', '卓', '杭',
                       '玲', '睿', '炜', '雨', '炜', '丽', '忠', '瑞', '婧', '惠', '炎', '秀', '翠', '爱', '艳', '龙', '嫣', '志', '芷',
                       '悦', '红', '焱', '婷', '惠', '于', '沁', '诺', '梓', '秀', '昊', '小', '悦', '秀', '欣', '晓', '午', '会', '龙',
                       '琳', '展', '羽', '艺', '月', '歌', '海', '晶', '尤', '仪', '玉', '钰', '雪', '卿', '晓', '家', '安', '湘', '丹',
                       '薏', '婷', '怡', '琳', '卓', '瓶', '爱', '桂', '石', '腊', '雅', '莉', '娟', '艳', '棠', '悦', '婉', '嘉', '彩',
                       '媛', '美', '莉', '燕', '昕', '倡', '紊', '子', '爱', '维', '思', '振', '鸾', '玲', '旦', '苏', '羽', '秋', '建',
                       '泓', '富', '倩', '诗', '承', '雪', '妍', '晓', '依', '瑾', '永', '翰', '婉', '景', '赛', '晓', '晋', '幸', '歆',
                       '曾', '国', '彩', '三', '雪', '义', '雪', '津', '琳', '燕', '纯', '素', '艳']
        three = ['萱', '嘉', '彤', '香', '舒', '睿', '雅', '睿', '茜', '嫦', '涵', '惠', '翎', '梅', '惠', '絮', '菡', '婷', '淑', '洁',
                 '文', '清', '涵', '涵', '华', '媛', '娅', '曼', '雅', '华', '菊', '茵', '菡', '琳', '玉', '菲', '云', '絮', '媛', '瑜',
                 '妍', '竣', '淑', '语', '华', '婷', '珺', '如', '嫣', '瑜', '嫦', '清', '嫣', '云', '玲', '蓉', '雯', '梦', '菡', '云',
                 '雅', '婧', '婧', '嘉', '舒', '菡', '嫣', '梦', '珊', '怡', '茜', '华', '茜', '菲', '雯', '悦', '秀', '瑶', '秀', '丽',
                 '娜', '玲', '娜', '艳', '秀', '颖', '娜', '瑶', '洁', '茹', '芳', '若', '红', '宁', '怡', '帆', '莹', '绫', '梅', '萍',
                 '蔓', '梅', '华', '莉', '琳', '妍', '玉', '玲', '妍', '莉', '美', '冰', '美', '丽', '文', '瑶', '颖', '琳', '婷', '娟',
                 '艳', '青', '美', '悦', '凌', '洁', '嘉', '媛', '茹', '晴', '惠', '雁', '菲', '菲', '绮', '菲', '嫣', '鸣', '花', '艳',
                 '岚', '嫦', '菊', '媛', '云', '蓉', '颖', '嫣', '云', '萍', '华', '语', '爰', '茹', '晴', '鸣', '清', '华', '惠', '英',
                 '文', '语', '茹', '晴', '睿', '茜', '蓉', '羽', '迎', '梨', '婕', '旋', '琳', '霞', '淇', '卿', '倩', '琳', '娉', '英',
                 '美', '文', '涵', '星', '玲', '子', '雪', '妍', '婷', '婷', '颖', '悦', '嘉', '岚', '翠', '舒', '语', '美', '清', '媛',
                 '嘉', '絮', '云', '翔', '睿', '玉', '淑', '嫣', '茹', '淑', '云', '嫣', '绮', '睿', '梦', '菡', '萍', '雅', '萍', '丽',
                 '菲', '茹', '茵', '婷', '语', '瑛', '淑', '雁', '雅', '舒', '雯', '悦', '娟', '华', '蓉', '庭', '艳', '霞', '洁', '玉',
                 '颖', '悦', '蓉', '洁', '娇', '妍', '英', '丽', '颖', '琳', '莹', '婷', '英', '燕', '芬', '文', '芳', '琳', '颖', '萍',
                 '茹', '霞', '艳', '钰', '芳', '茹', '颖', '英', '霞', '秀', '玲', '娜', '媛', '瑶', '燕', '君', '怡', '妍', '张', '芳',
                 '怡', '梅', '瑶', '霞', '梅', '敏', '文', '莹', '萍', '玲', '玲', '燕', '婧', '文', '琳', '娟', '洁', '娟', '蓉', '洁',
                 '颖', '茹', '媛', '梅', '冉', '昱', '可', '淼', '婷', '花', '萍', '燕', '英', '梅', '莉', '娅', '娣', '红', '莉', '驰',
                 '婷', '洁', '红', '雪', '芳', '轩', '齐', '妍', '文', '文', '婧', '琴', '娟', '娜', '文', '瑶', '丽', '娅', '娟', '洁',
                 '艳', '颖', '茹', '霞', '成', '茹', '文', '芬', '玲', '霞', '婷', '琳', '琴', '颖', '燕', '文', '玉', '玉', '玉', '瑶',
                 '琳', '燕', '政', '娟', '婷', '婧', '文', '萍', '文', '秀', '明', '洁', '莉', '玲']
        li = [random.choice(second_name), random.choice(three)]
        random_lastname = random.choice(li)
        return random_lastname

    # 随机电话号码
    def random_phone(self):
        # 第二位
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]

        # 第三位的值根据第二位来确定
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9)
        }[second]
        # 后8位随机抽取
        suffix = ''
        for x in range(8):
            suffix = suffix + str(random.randint(0, 9))
        # 拼接
        return "1{}{}{}".format(second, third, suffix)

    # 随机生成国家
    def random_country(self):
        li = ['Eritrea', "China", 'Republic of Korea', 'Japan', 'Mongolia',
              "Democratic Peoples Republic of Korea", 'Republic of Singapore', 'Republic of Indonesia',
              'Republic of the Philippines', 'Brunei Darussalam', 'Kingdom of Thailand', 'Malaysia',
              'Kingdom of Cambodia', 'Socialist Republic of Vietnam', "Lao Peoples Democratic Republic",
              'Republic of the Union of Myanmar', 'Kingdom of Bhutan', 'Democratic Republic of East Timor',
              'Kingdom of Nepal', "Peoples Republic of Bangladesh", 'Republic of India',
              'Democratic Socialist Republic of Sri Lanka', 'Islamic Republic of Pakistan', 'Republic of Maldives',
              'Islamic State of Afghanistan', 'Republic of Tajikistan', 'Kyrgyz Republic', 'Republic of Kazakhstan',
              'Republic of Uzbekistan', 'Republic of Turkmenistan', 'Islamic Republic of Iran', 'Republic of Iraq',
              'State of Kuwait', 'State of Qatarc', 'United Arab Emirates', 'Kingdom of Bahrain', 'Sultanate of Oman',
              'Republic of Yemen', 'Kingdom of Saudi Arabia', 'Hashemite Kingdom of Jordan', 'State of Palestine',
              'State of Israel', 'Syrian Arab Republic', 'Lebanese Republic', 'Republic of Cyprus',
              'Republic of Turkey', 'Republic of Azerbaijan', 'Georgia', 'Republic of Armenia',
              'Federal Republic of Germany', 'United kingdom of Great Britain and Northern Ireland', 'Ireland',
              'Kingdom of Norway', 'Republic of Iceland', 'Kingdom of Sweden', 'Republic of Finland',
              'Republic of Latvia', 'Republic of Estonia', 'Republic of Lithuania', 'Czech Republic', 'Slovak Republic',
              'Republic of Poland', 'Republic of Hungary', 'Kingdom of Denmark', 'Kingdom of the Netherlands',
              'Russian Federation', 'Republic of Belarus', 'Ukraine', 'Republic of Moldova', 'Principality of Monaco',
              'French Republic', 'Kingdom of Belgium', 'Grand Duchy of Luxembourg', 'Republic of Austria',
              'Swiss Confederation', 'Principality of Andorra', 'Principality of Liechtenstein', 'Kingdom of Spain',
              'Portuguese Republic', 'Italian Republic', 'Republic of Malta', 'Republic of San Marino',
              'Vatican City State', 'Republic of Slovenia', 'Republic of Croatia', 'Bosnia and Herzegovina',
              'Federal Republic of Yugoslavia', 'Republic of Albania', 'Republic of Bulgaria', 'Romania',
              'Hellenic Republic', 'The Republic of North Macedonia', 'United States of America', 'Canada',
              'United Mexican States', 'Belize', 'Republic of Guatemala', 'Republic of El Salvador',
              'Republic of Nicaragua', 'Republic of Panama', 'Republic of Cuba', 'Commonwealth of the Bahamas',
              'Republic of Haiti', 'Jamaica', 'Republic of Honduras', 'Republic of Costa Rica', 'Dominican Republic',
              'Federation of Saint Kitts and Nevis', 'Antigua and Barbuda', 'Saint Lucia',
              'Saint Vincent and the Grenadines', 'Commonwealth of Dominica', 'Grenada', 'Barbados',
              'Republic of Trinidad and Tobago', 'Co-operative Republic of Guyana', 'Republic of Colombia',
              'Republic of Ecuador', 'Bolivarian Republic of Venezuela', 'Republic of Suriname', 'Republic of Bolivia',
              'Republic of Chile', 'Republic of Peru', 'Republic of Paraguay', 'Federative Republic of Brazil',
              'Argentine Republic', 'Oriental Republic of Uruguay', 'Arab Republic of Egypt',
              "Democratic Peoples Republic of Algeria", 'Federal Democratic Republic of Ethiopia',
              'Republic of South Africa', 'State of Eritrea', 'Republic of Djibouti', 'Republic of the Sudan',
              'Republic of South Sudan', 'Somali Republic', "Socialist Peoples Libyan Arab Jamahiriya",
              'Republic of Tunisia', 'Kingdom of Morocco', 'Republic of Cape Verde', 'Republic of Mali',
              'Islamic Republic of Mauritania', 'Republic of Senegal', 'Republic of the Gambia',
              'Republic of Guinea-Bissau', 'Republic of Guinea', 'Republic of Liberia', "Republic of Cote d'Ivoire",
              'Republic of Sierra Leone', 'Burkina Faso', 'Republic of Chad', 'Republic of Niger',
              'Federal Republic of Nigeria', 'Republic of Ghana', 'Togolese Republic', 'Republic of Benin',
              'Gabonese Republic', 'Republic of Cameroon', 'Republic of Equatorial Guinea',
              'Democratic Republic of Sao Tome and Principe', 'Republic of the Congo',
              'Democratic Republic of the Congo', 'Central African Republic', 'Republic of Burundi',
              'Republic of Uganda', 'Republic of Rwanda', 'United Republic of Tanzania', 'Republic of Kenya',
              'Republic of Angola', 'Republic of Zambia', 'Republic of Malawi', 'Republic of Seychelles',
              'Republic of Mozambique', 'Republic of Madagascar', 'Union of the Comoros', 'Republic of Mauritius',
              'Republic of Zimbabwe', 'Republic of Botswana', 'Republic of Namibia', 'Kingdom of Swaziland',
              'Kingdom of Lesotho', 'Commonwealth of Australia', 'New Zealand', 'Republic of the Fiji Islands',
              'Independent State of Papua New Guinea', 'Republic of Vanuatu', 'Kingdom of Tonga', 'Republic of Nauru',
              'Republic of Kiribati', 'Independent State of Samoa', 'Tuvalu', 'Federated States of Micronesia',
              'Solomon Islands', 'Republic of the Marshall Islands', 'Republic of Palau', 'China', 'Mongolia',
              'South Korea', 'North Korea', 'Japan', 'Singapore', 'Malaysia', 'Thailand', 'Philippines', 'India',
              'Vietnam', 'Laos', 'Cambodia', 'Myanmar', 'Bhutan', 'Nepal', 'East Timor', 'Brunei', 'Indonesia',
              'Sikkim', 'Bangladesh', 'Sri Lanka', 'Maldives', 'Pakistan', 'Afghanistan', 'Iran', 'Kuwait',
              'Saudi Arabia', 'Bahrain', 'Qatar', 'List of rulers of Oman', 'Yemen', 'Iraq', 'Syria', 'Lebanon',
              'Jordan', 'State of Palestine', 'Israel', 'Turkey', 'Uzbekistan', 'Kazakhstan', 'Kyrgyzstan',
              'Tajikistan', 'Armenia', 'Turkmenistan', 'Azerbaijan', 'Iceland', 'Faroe Islands', 'Danish Realm',
              'Norway', 'Sweden', 'Finland', 'Russia', 'Ukraine', 'Belarus', 'Moldova', 'Lithuania', 'Estonia',
              'Latvia', 'Poland', 'Czech Republic', 'Hungary', 'Germany', 'Austria', 'Switzerland', 'Netherlands',
              'Belgium', 'Luxembourg', 'United Kingdom', 'Gibraltar', 'Republic of Ireland', 'Kingdom of France',
              'Monaco', 'Andorra', 'Spain', 'Portugal', 'Italy', 'Vatican City', 'San Marino', 'Malta', 'Slovakia',
              'North Macedonia (region)', 'Serbia', 'Romania', 'Bulgaria', 'Albania', 'Greece', 'Montenegro',
              'Australia', 'New Zealand', 'Solomon Islands', 'Vanuatu', 'New Caledonia', 'Fiji', 'Nauru',
              'Federated States of Micronesia', 'Marshall Islands', 'Guam', 'Tuvalu', 'Wallis and Futuna', 'Samoa',
              'American Samoa', 'Niue', 'Norfolk Island', 'Palau', 'Tokelau', 'Cook Islands', 'Pitcairn Islands',
              'Greenland', 'Canada', 'United States of America(USA)', 'Bermuda', 'Mexico', 'Guatemala', 'El Salvador',
              'Nicaragua', 'Costa Rica', 'Panama', 'The Bahamas', 'Cuba', 'Cayman Islands', 'Jamaica', 'Haiti',
              'Puerto Rico', 'United States Virgin Islands', 'British Virgin Islands', 'Anguilla', 'Montserrat',
              'Guadeloupe', 'Dominica', 'Martinique', 'Barbados', 'Grenada', 'Aruba', 'Egypt', 'Libya', 'Algeria',
              'Morocco', 'Western Sahara', 'Senegal', 'The Gambia', 'Mali', 'Cape Verde', 'Guinea-Bissau',
              'Sierra Leone', 'Liberia', 'Ghana', 'Togo', 'Benin', 'Niger', 'Nigeria', 'Cameroon', 'Equatorial Guinea',
              'Central African Republic', 'Sudan', 'Kenya', 'Uganda', 'Tanzania', 'Rwanda', 'Zaire',
              'Congo  Democratic Republicof the Congo', 'Angola', 'Zambia', 'Malawi', 'Mozambique', 'Comoros',
              'Madagascar', 'Mauritius', 'Réunion', 'Zimbabwe', 'Botswana', 'Namibia', 'South Africa', 'Lesotho',
              'Eritrea']
        random_country = random.choice(li)
        return random_country

    def get_coupons_info(self):
        info = self.get_sess()
        sess = info[0]
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/homePage/getMyDiscountsList?pageNo=1&pageSize=100&type=undefined'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{info[1]}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.get(url=url, headers=header)
        infos = res.json()['result']['records']
        #  目标 {'已使用':[{},{}],"未使用":[{},{}]}
        coupons_dict = {}
        coupons_unused_list = []  # 未使用优惠卷集合
        coupons_used_list = []  # 已使用优惠卷集合
        for i in infos:
            coupons_info = {}  # 存放优惠券信息的字典,放在循环内每次刷新
            coupons_status = i['whetherUse_dictText']  # 优惠券状态
            couponsid = i['couponsId']  # 兑换优惠券时定位的优惠券ID
            end_time = i['couponsEndTime']  # 优惠券结束时间
            id = i["id"]  # 优惠券 ID
            couponsAmount = i['couponsAmount']  # 优惠券优惠金额
            requiredPoints = i['requiredPoints']  # 兑换所需积分
            if coupons_status == '未使用':
                coupons_info['id'] = id
                coupons_info['coupons_status'] = coupons_status
                coupons_info['end_time'] = end_time
                coupons_info['couponsid'] = couponsid
                coupons_info['couponsAmount'] = couponsAmount
                coupons_info['requiredPoints'] = requiredPoints
                coupons_unused_list.append(coupons_info)
                coupons_dict['未使用'] = coupons_unused_list
            if coupons_status == '已使用':
                coupons_info['id'] = id
                coupons_info['coupons_status'] = coupons_status
                coupons_info['end_time'] = end_time
                coupons_info['couponsid'] = couponsid
                coupons_info['couponsAmount'] = couponsAmount
                coupons_info['requiredPoints'] = requiredPoints
                coupons_used_list.append(coupons_info)
                coupons_dict['已使用'] = coupons_used_list
        return coupons_dict

    # 返回低于商品总价的优惠券id集合
    def get_coupons_id_by_totalprice(self, total_price):
        """
        通过购物车商品总价来筛选符合条件的优惠券
        :param total_price: 传入的商品总价格
        :return: 低于总价的优惠券列表
        """
        coupons = self.get_coupons_info()
        unused_info = coupons['未使用']
        li = []
        for info in unused_info:
            coupon_price = info['couponsAmount']  # 优惠金额
            id = info['couponsid']
            if coupon_price < total_price:  # 如果优惠券优惠金额小于商品总金额
                li.append(id)  # 将id加入列表
        if not li:
            print('未找到相关优惠券！！')
        else:
            print(f'找到 {len(li)} 张符合要求的优惠券! ')
        return li

    # 通过购物车id查询商品信息
    def selecet_goodsinfo_by_shopcarid(self, shopCartId):
        """
        :param shopCartId : 传入购物车定位的商品id 或者 id列表
        :return: 返回一个列表 包含一条或者多条 商品名称、价格、id、数量、库存信息
        """
        info = self.get_sess()
        sess = info[0]
        url = 'http://18.118.13.94:81/jeecg-boot/my/shoppingCart/list?pageNo=1&pageSize=100'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{info[1]}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.get(url=url, headers=header)
        try:
            infos = res.json()['result']['records']
            li = []  # 用于储存匹配到的信息
            for info in infos:
                dict = {}
                id = info['id']  # 购物车定位ID
                goodsname = info['goodsName']  # 商品名称
                goodsprince = info['goodsPrice']  # 商品价格
                goodsid = info['goodsid']  # 商品id
                goodsamount = info['goodsamount']  # 购物车商品数量
                stock = info['stock']  # 商品库存
                totalprice = info['totalprice']
                if type(shopCartId) == list:
                    for car_id in shopCartId:
                        if int(car_id) == int(id):
                            dict["goodsname"] = goodsname
                            dict['goodsprince'] = goodsprince
                            dict['goodsid'] = goodsid
                            dict['goodsamount'] = goodsamount
                            dict['stock'] = stock
                            dict['totalprice'] = totalprice
                            li.append(dict)
                elif type(shopCartId) == str:
                    if int(shopCartId) == int(id):
                        dict["goodsname"] = goodsname
                        dict['goodsprince'] = goodsprince
                        dict['goodsid'] = goodsid
                        dict['goodsamount'] = goodsamount
                        dict['stock'] = stock
                        dict['totalprice'] = totalprice
                        li.append(dict)
            print(li)
            return li
        except:
            print('传入参数值有误，请传入纯数字id')

    # 获取orderid
    def get_orderid(self):
        """
        返回一个通过待支付、支付成功、已签收、其他整理后的订单id集合
        :return: {待支付：[list1,list2,list3],支付成功：[list1,list2,list3],已签收:[list1,list2,list3]}
        """

        info = self.get_sess()
        sess = info[0]
        url = 'http://18.118.13.94:8080/jeecg-boot/sys/api/homePage/getMyOrderList?pageNo=1&pageSize=10&sort=&goodsName=&sortMethod='
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{info[1]}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.get(url=url, headers=header)
        total_page = res.json()['result']['pages']  # 获取总页数
        Unpaid = []  # 存放未支付订单
        paid = []  # 存放已支付订单
        Signed = []  # 存放已签收订单
        other = []  # 其他
        order_ids = {}  # 存放未支付、已支付、已签收订单信息字典
        for i in range(1, total_page + 1):
            res = sess.get(url=url.replace('pageNo=1&', f'pageNo={i}&'), headers=header)
            infos = res.json()['result']['records']
            for info in infos:
                order_status = info['statusText']
                orderid = info['orderId']
                if order_status == '待支付':
                    Unpaid.append(orderid)
                elif order_status == '支付成功':
                    paid.append(orderid)
                elif order_status == '已签收':
                    Signed.append(orderid)
                else:
                    other.append(orderid)
        order_ids['待支付'] = Unpaid
        order_ids['支付成功'] = paid
        order_ids['已签收'] = Signed
        order_ids['其他'] = other
        return order_ids

    def get_order1(self):
        """
        通过提交订单获取订单ID
        :return: 订单ID
        """
        info = self.get_sess()
        sess = info[0]
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{info[1]}', 'Content-Type': 'application/json',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        url = 'http://18.118.13.94:8080/jeecg-boot/my/shoppingCart/submitOrder'
        addressId = random.choice(self.select_address_info())  # 获取地址
        shopCartId = random.choice(self.select_shopcar_ids())  # 获取购物车商品ID
        goodsinfo = self.selecet_goodsinfo_by_shopcarid(shopCartId)  # 通过购物车ID查询商品详情
        count = goodsinfo[0]['goodsamount']  # 获取数量
        totalprice = goodsinfo[0]['totalprice']
        coupons_id = random.choice(self.get_coupons_id_by_totalprice(totalprice))
        data = {"addressId": f"{addressId}", "couponsid": f"{coupons_id}",
                "list": [{"count": count, "shopCartId": f"{shopCartId}"}], "remark": ""}
        data = json.dumps(data)
        res = sess.post(url=url, data=data, headers=header)
        order_id = res.json()['result']['id']
        return order_id

    # 查询收藏列表信息
    def get_favorites_infos(self):
        """
        获取收藏夹中商品数据
        :return: 商品数据列表
        """
        info = self.get_sess()
        sess = info[0]
        token = info[1]
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.74Safari/537.36Edg/99.0.1150.52',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/usersAttentionGoods/list?pageNo=1&pageSize=10'
        res = sess.get(url=url, headers=header)
        total_pages = res.json()['result']['pages']  # 总页数
        li = []
        for page in range(1, total_pages + 1):
            res = sess.get(url=url.replace('pageNo=1', f'pageNo={page}'), headers=header)
            infos = res.json()['result']['records']
            for info in infos:
                li.append(info)
        return li


    # 查询收藏列表信息
    def get_favorites_ids(self):
        """
        获取收藏夹中商品id集合
        :return: 商品id列表
        """
        info = self.get_sess()
        sess = info[0]
        token = info[1]
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.74Safari/537.36Edg/99.0.1150.52',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/usersAttentionGoods/list?pageNo=1&pageSize=10'
        res = sess.get(url=url, headers=header)
        total_pages = res.json()['result']['pages']  # 总页数
        li = []
        for page in range(1, total_pages + 1):
            res = sess.get(url=url.replace('pageNo=1', f'pageNo={page}'), headers=header)
            infos = res.json()['result']['records']
            for info in infos:
                li.append(info['id'])
        return li

    #查询积分商城可兑换的优惠券信息
    def select_point_info(self):
        """
        查询积分商城优惠券信息
        :return: 返回一个JSon串，所有优惠券信息
        """
        info = self.get_sess()
        sess = info[0]
        token = info[1]
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/homePage/queryDiscountsPageList'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{token}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        data= 'pageNo=1&pageSize=8'
        res = sess.get(url=url+"?"+data,headers=header)
        info = res.json()['result']['records']
        return info

    #查询用户信息
    def select_userinfo(self):
        info = self.get_sess()
        sess = info[0]
        token = info[1]
        url = 'http://18.118.13.94:8080/jeecg-boot/sys/api/homePage/getUserInfo'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{token}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res=sess.get(url=url,headers=header)
        return res.json()['result']

    #获取新闻ID
    def get_news_ids(self):
        info = self.get_sess()
        sess = info[0]
        token = info[1]
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/homePage/news/list'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{token}', 'Content-Type': f'application/x-www-form-urlencoded',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = sess.get(url=url,headers=header)
        ids = []
        infos = res.json()['result']['records']     #新闻信息集合
        for info in infos:
            ids.append(info['id'])
        return ids


if __name__ == '__main__':
    a = Common()
    # a.select_userinfo()
    # a.get_report()
    # a.select_goodsinfo()
    # a.get_news_ids()
    a.get_header(
        data = """
Host: 18.118.13.94:8080
Connection: keep-alive
Accept: application/json, text/plain, */*
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NDkzMDc4NTMsInVzZXJuYW1lIjoiYTg4Mzc3NDkxOEAxNjMuY29tIn0.s7K8f9vuMIV27nNj8H9VHXKRTdriRRPA78grO3gXi9w
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29
Origin: http://18.118.13.94:81
Referer: http://18.118.13.94:81/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
""")