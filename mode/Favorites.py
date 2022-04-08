"""
收藏模块
"""
import random
import re

import requests

from Okmarts_test_front.Common.Comm import Common
from Okmarts_test_front.mode.Post_mode import post
from Okmarts_test_front.parameter.parameter import Parameters_cls
from Okmarts_test_front.spec_cases.spec_cases import Spec_Cases
from pachong1.userAgent import UserAgent


class Favorites:

    def __init__(self):
        info = Common().get_sess()
        self.sess = info[0]
        self.token = info[1]
        self.User_Agent = random.choice(UserAgent().useragent_list())

    def favorites(self, Parameters):
        casename = Parameters['casename']
        print(f'当前执行用例为{casename}')
        url = Parameters['url']
        data = Parameters['data']
        content_type = Parameters["content_type"]
        result = Parameters['result']
        assert_way = Parameters['assert_way']
        mode = Parameters['mode']

        spec_case = Spec_Cases().spec_cases()

        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '33',
                  'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': f'{self.User_Agent}',
                  'Content-Type': f'{content_type};charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/', 'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}

        goodsinfo = Common().select_goodsinfo()

        if '"goodsid":' in data:
            data = Parameters_cls().goodsId(casename, data, spec_case['spec_goodsId'], goodsinfo, mode)

        print(f'修改后的data 为{data}')

        post(sess=self.sess, casename=casename, url=url, data=data, header=header, result=result, assert_way=assert_way,
             content_type=content_type)

    def favorites_delete(self, Parameters):
        casename = Parameters['casename']
        print(f'当前执行用例为{casename}')
        url = Parameters['url']
        data = Parameters['data']
        content_type = Parameters["content_type"]
        result = Parameters['result']
        assert_way = Parameters['assert_way']

        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'Content-Type': f'{content_type}',
                  'User-Agent': f'{self.User_Agent}', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}

        if 'id=' in data:
            print('参数中存在id')
            if 'id' in casename or 'ID' in casename or 'Id' in casename or 'iD' in casename:  # 如果id在用例中则跳过
                print('特殊用例不修改ID参数')
            else:
                old_id = re.findall(pattern='id=(\d+)', string=data)[0]
                print(old_id)
                new_id = random.choice(Common().get_favorites_infos())['id']
                data = data.replace(old_id, new_id)
                print(f'替换{old_id}为{new_id}')
        if 'ids=' in data:
            print('参数中存在ids')
            print(data)
            if casename in ['参数为空删除失败', '参数错误删除失败']:
                print('特殊用例，不执行修改操作')
            else:
                old_ids = data.split('=')[-1]
                print(old_ids)
                new_ids = Common().Splicing_id(2, Common().get_favorites_ids())
                data = data.replace(old_ids, new_ids)
                print(f'替换{old_ids}为{new_ids}')

        print(data)
        if 'POST' in casename:
            res = self.sess.post(url=url + '?' + data, headers=header)
            print('入口1')
            print(res.json())
            print(f'预期结果为 {result}')
            print(f'实际结果为 {res.json()[assert_way]}')
            assert result in res.json()[assert_way]
        elif 'GET' in casename:
            res = self.sess.get(url=url + '?' + data, headers=header)
            print('入口2')
            print(res.json())
            print(f'预期结果为 {result}')
            print(f'实际结果为 {res.json()[assert_way]}')
            assert result in res.json()[assert_way]
        elif 'PUT' in casename:
            res = self.sess.put(url=url + '?' + data, headers=header)
            print('入口3')
            print(res.json())
            print(f'预期结果为 {result}')
            print(f'实际结果为 {res.json()[assert_way]}')
            assert result in res.json()[assert_way]
        elif '未登录' in casename:
            res = requests.delete(url=url + '?' + data)
            print('入口4')
            print(res.json())
            print(f'预期结果为 {result}')
            print(f'实际结果为 {res.json()[assert_way]}')
            assert result in res.json()[assert_way]
        else:
            res = self.sess.delete(url=url + '?' + data, headers=header)
            print('入口0')
            print(res.json())
            print(f'预期结果为 {result}')
            print(f'实际结果为 {res.json()[assert_way]}')
            assert result in res.json()[assert_way]
