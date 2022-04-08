"""
优惠券
"""
from Okmarts_test_front.Common.Comm import Common
from Okmarts_test_front.mode.Post_mode import post
from Okmarts_test_front.mode.get_mode import get
from Okmarts_test_front.parameter.parameter import Parameters_cls


class Discounts:
    def __init__(self):
        info = Common().get_sess()
        self.sess = info[0]
        self.token = info[1]

    def discount(self, Parameters):
        casename = Parameters['casename']
        print(f'当前执行用例为{casename}')
        url = Parameters['url']
        data = Parameters['data']
        content_type = Parameters["content_type"]
        result = Parameters['result']
        assert_way = Parameters['assert_way']
        mode = Parameters['mode']

        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}', 'Content-Type': f'{content_type}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}

        get(self.sess, casename, url, data, header, result, assert_way)

    def exchange_discounts(self, Parameters):
        casename = Parameters['casename']
        print(f'当前执行用例为{casename}')
        url = Parameters['url']
        data = Parameters['data']
        content_type = Parameters["content_type"]
        result = Parameters['result']
        assert_way = Parameters['assert_way']
        mode = Parameters['mode']

        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '28',
                  'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.74Safari/537.36Edg/99.0.1150.55',
                  'Content-Type': f'{content_type};charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}

        if '"id":' in data:
            Parameters_cls().id(casename, data, mode)

        post(self.sess, casename, url, data, header, result, assert_way, content_type)
