"""
购物车模块
"""

from Okmarts_test_front.Common.Comm import Common
from Okmarts_test_front.mode.Post_mode import post
from Okmarts_test_front.parameter.parameter import Parameters_cls
from Okmarts_test_front.spec_cases.spec_cases import Spec_Cases


class Shoping_car:
    def __init__(self):
        info = Common().get_sess()
        self.sess = info[0]
        self.token = info[1]

    def shoping_car(self, Parameters):
        casename = Parameters['casename']
        print(f'当前执行用例为{casename}')
        url = Parameters['url']
        data = Parameters['data']
        content_type = Parameters["content_type"]
        result = Parameters['result']
        assert_way = Parameters['assert_way']
        mode = Parameters['mode']

        spec_case = Spec_Cases().spec_cases()
        shopcar_info = Common().select_shopcar_goodsinfo()

        if '"id":' in data:
            data = Parameters_cls().id(casename, data, mode)
        if '"count":' in data:
            data = Parameters_cls().count(casename, data, spec_case['spec_count'], shopcar_info, mode)
        if '"goodsId":' in data:
            data = Parameters_cls().goodsId(casename, data, spec_case['spec_goodsId'], shopcar_info,mode)
        if '"ids":' in data:
            data = Parameters_cls().shop_ids(casename, data, spec_case['spec_ids'])

        print(f'修改后data为{data}')

        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '64',
                  'X-Access-Token': f'{self.token}',
                  'Accept': 'application/json,text/plain,*/*',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Content-Type': f'{content_type};charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/', 'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}

        post(sess=self.sess,casename=casename,url=url,data=data,header=header,result=result,assert_way=assert_way,content_type=content_type)

    def shoping_car_add(self,Parameters):
        casename = Parameters['casename']
        print(f'当前执行用例为{casename}')
        url = Parameters['url']
        data = Parameters['data']
        content_type = Parameters["content_type"]
        result = Parameters['result']
        assert_way = Parameters['assert_way']
        mode = Parameters['mode']

        spec_case = Spec_Cases().spec_cases()

        goodsinfo = Common().select_goodsinfo()
        print(goodsinfo)

        if '"count":' in data:
            data = Parameters_cls().count(casename, data, spec_case['spec_count'], goodsinfo, mode)
        if '"goodsId":' in data:
            data = Parameters_cls().goodsId(casename, data, spec_case['spec_goodsId'], goodsinfo,mode)

        print(f'修改后data为{data}')

        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '64',
                  'X-Access-Token': f'{self.token}',
                  'Accept': 'application/json,text/plain,*/*',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Content-Type': f'{content_type};charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/', 'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}

        post(sess=self.sess,casename=casename,url=url,data=data,header=header,result=result,assert_way=assert_way,content_type=content_type)
