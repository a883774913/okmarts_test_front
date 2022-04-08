"""
数据预埋
"""
import json
import random

from Okmarts_test_front.Common.Comm import Common



class Embedded_data:
    def __init__(self):
        info = Common().get_sess()
        self.sess = info[0]
        token = info[1]
        self.header= {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '64',
                  'X-Access-Token':f'{token}',
                  'Accept': 'application/json,text/plain,*/*',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Content-Type':'application/json;charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/', 'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}

    def add_address(self,number):
        """
        :param number: 需要循环的次数
        :return: 无
        """
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/homePage/addAddress'
        n = 0
        for i in range(1,number):
            firstname = Common().first_name()
            lastname = Common().last_name()
            contactnumber = Common().random_phone()
            data = {"firstname": f"{firstname}", "lastname": f"{lastname}", "contactnumber": f"{contactnumber}",
                    "area1": "11", "area2": "11", "area3": "CN", "postalCode": "21", "addressLine": "12",
                    "countryCode": "CN"}
            data = json.dumps(data)
            res = self.sess.post(url=url,data=data,headers=self.header)
            try:
                assert res.json()['message'] == '成功'
            except AssertionError :
                n+=1
            finally:
                print(f'第 {i + 1}次 预埋地址数据完成，存在 {n} 次错误 ，还剩 {number-i-1} 次')

    #添加商品到购物车的
    def add_car(self,numbers):
        """
        :param numbers: 循环次数
        :return:
        """
        url = 'http://18.118.13.94:81/jeecg-boot/my/shoppingCart/add'
        n = 0
        for i in range(1,numbers):
            try:
                goodsinfo = Common().select_goodsinfo()
                count = goodsinfo['amount']
                if count > 10:
                    count = random.randint(2,10)
                goodsId = goodsinfo['id']
                data = {"count": random.randint(1,count), "goodsId": f"{goodsId}"}
                data = json.dumps(data)
                res = self.sess.post(url=url,data=data,headers=self.header)
                assert '操作成功' in res.json()['message']

            except AssertionError:
                n+=1
            finally:
                print(f'第 {i + 1}次 预埋地址数据完成，存在 {n} 次错误 ，还剩 {numbers - i - 1} 次')

    def add_favorites(self,numbers):
        """
        收藏栏商品数据预埋
        :param numbers: 需要预埋的商品量
        :return: 无
        """
        err = 0
        url = 'http://18.118.13.94:81/jeecg-boot/sys/api/usersAttentionGoods/add'
        for i in range(numbers):
            try:
                goodsid = Common().select_goodsinfo()["id"]
                data = {"goodsid": f"{goodsid}"}
                data = json.dumps(data)
                res = self.sess.post(url=url, headers=self.header, data=data)
                assert '操作成功' in res.json()['message']
            except:
                err+=1
            finally:
                print(f'第 {i + 1}次 预埋地址数据完成，存在 {err} 次错误 ，还剩 {numbers - i - 1} 次')




if __name__ == '__main__':
    a = Embedded_data()
    # a.add_address(5)
    # a.add_car(50)
    a.add_favorites(10)