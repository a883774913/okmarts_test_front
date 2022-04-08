"""
获取验证码接口
"""
import random

from Okmarts_test_front.Common.Comm import Common
from Okmarts_test_front.mode.get_mode import get
from pachong1.userAgent import UserAgent


class GET_Code:
    def __init__(self):
        info = Common().random_sess()
        self.sess = info[0]
        self.token = info[1]
        self.user_agent = random.choice(UserAgent().useragent_list())

    def get_code(self,Parameters):
        casename = Parameters['casename']
        print(f'当前执行用例为{casename}')
        url = Parameters['url']
        data = Parameters['data']
        content_type = Parameters["content_type"]
        result = Parameters['result']
        assert_way = Parameters['assert_way']

        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': f'{self.user_agent}',
                  'Content-Type': f'{content_type}',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/', 'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}

        get(sess=self.sess, casename=casename, url=url, data=data, header=header, result=result, assert_way=assert_way)