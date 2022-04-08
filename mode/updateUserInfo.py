"""修改用户信息"""
import re

from Okmarts_test_front.Common.Comm import Common
from Okmarts_test_front.mode.Post_mode import post
from Okmarts_test_front.spec_cases.spec_cases import Spec_Cases


class UpdateUserinfo:
    def __init__(self):
        info = Common().get_sess()
        self.sess = info[0]
        self.token = info[1]

    def update_userinfo(self, Parameters):
        casename = Parameters['casename']
        print(f'当前执行用例为{casename}')
        url = Parameters['url']
        data = Parameters['data']
        content_type = Parameters["content_type"]
        result = Parameters['result']
        assert_way = Parameters['assert_way']
        mode = Parameters['mode']

        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '356',
                  'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.74Safari/537.36Edg/99.0.1150.55',
                  'Content-Type': f'{content_type};charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}

        spec_cases = Spec_Cases().spec_cases()
        if casename in spec_cases['spec_id']:
            print('特殊用例，不修改参数')
        elif casename in ['参数subscribePromotional缺失修改失败','参数subscribeAccount缺失修改失败','参数subscribeCommodity缺失修改失败',
                          '参数subscribePromotional为非限定数字修改失败','参数subscribeAccount为非限定数字修改失败','参数subscribeCommodity为非限定数字修改失败']:
            print('特殊用例，不修改参数')
        else:
            old_id = re.findall('"id":"(.*?)"', string=data)[0]
            new_id = Common().select_userinfo()['id']
            print(new_id)
            data = data.replace(f'{old_id}', f'{new_id}')

        print(data)
        post(self.sess, casename, url, data, header, result, assert_way, content_type)
