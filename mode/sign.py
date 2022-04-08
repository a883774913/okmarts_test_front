"""
签到
"""

from Okmarts_test_front.Common.Comm import Common
from Okmarts_test_front.mode.get_mode import get


class Sign:
    def __init__(self):
        self.info = Common().random_sess()

    def sign(self, Parameters):
        casename = Parameters['casename']
        print(f'当前执行用例为{casename}')
        url = Parameters['url']
        data = Parameters['data']
        result = Parameters['result']
        assert_way = Parameters['assert_way']
        content_type = Parameters['content_type']
        sess = self.info[0]
        token = self.info[1]

        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{token}', 'Content-Type': f'{content_type}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.74Safari/537.36Edg/99.0.1150.52',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}

        if casename == '重复签到签到失败':
            info = Common().get_sess()
            sess = info[0]
            token = info[1]
            header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive',
                      'Accept': 'application/json,text/plain,*/*',
                      'X-Access-Token': f'{token}',
                      'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.74Safari/537.36Edg/99.0.1150.52',
                      'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                      'Accept-Encoding': 'gzip,deflate',
                      'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
            get(sess, casename, url, data, header, result, assert_way)
        get(sess, casename, url, data, header, result, assert_way)
