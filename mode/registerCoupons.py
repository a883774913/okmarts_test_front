"""
注册领取优惠券
"""
import requests

from Okmarts_test_front.Common.Comm import Common
from Okmarts_test_front.mode.get_mode import get
from Okmarts_test_front.spec_cases.spec_cases import Spec_Cases


class RegisterCoupons:
    def __init__(self):
        self.sess = requests.session()

    def registerCoupons(self, Parameters):
        casename = Parameters['casename']
        print(f'当前执行用例为{casename}')
        url = Parameters['url']
        data = Parameters['data']
        content_type = Parameters["content_type"]
        result = Parameters['result']
        assert_way = Parameters['assert_way']
        mode = Parameters['mode']

        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': 'null',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.74Safari/537.36Edg/99.0.1150.55',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Content-Type': f'{content_type}',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        spec_case = Spec_Cases().spec_cases()

        if casename in spec_case['spec_name']:
            print('特殊用例，不修改name参数')
        else:
            old_name = data.split('=')[-1]
            new_name = Common().random_account()[0]
            data = data.replace(f'{old_name}', f'{new_name}')
            print(f'修改old_name {old_name} 为 {new_name} ')

        print(data)

        get(self.sess, casename, url, data, header, result, assert_way)
