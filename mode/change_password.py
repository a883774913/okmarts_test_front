"""
修改密码
"""
import random
import time

from Okmarts_test_front.Common.Comm import Common
from Okmarts_test_front.mode.Post_mode import post
from Okmarts_test_front.parameter.parameter import Parameters_cls
from Okmarts_test_front.spec_cases.spec_cases import Spec_Cases
from pachong1.userAgent import UserAgent


class Change_Password:
    def __init__(self):
        info = Common().get_sess()
        self.sess = info[0]
        self.token = info[1]
        self.user_agent = random.choice(UserAgent().useragent_list())

    def change_password(self,Parameters):
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
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}

        #发送验证码
        url1 = 'http://18.118.13.94:81/jeecg-boot/sys/api/homePage/getUserEmailCode'
        data1 = "type=1"
        res1 = self.sess.get(url=url1+'?'+data1,headers=header)
        print(res1.json())
        time.sleep(5)

        spec_case = Spec_Cases().spec_cases()



        if '"code":' in data:
            data = Parameters_cls().code(casename,data,spec_case['spec_code'])

        print(data)
        post(self.sess,casename,url,data,header,result,assert_way,content_type)

