"""
购买事件 登录-随机选择一个商品-立即购买- 打包订单 - 支付
"""
import json
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Okmarts_test_front.Common.Comm import Common


class story_shoping:

    def __init__(self):
        info = Common().get_sess()
        self.sess = info[0]
        self.token = info[1]

    # 搜索商品
    def search_goods(self):
        url = 'http://18.118.13.94:8080/jeecg-boot/sys/api/goods/fuzzyquery_byname_list?fuzzyQueryName=1&pageNo=1&pageSize=11&brands=&type=&origins=&sortType=1'
        header = {'Connection': 'keep-alive',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
        res = self.sess.get(url=url, headers=header)
        total_page = res.json()['result']['pages']
        random_page = random.randint(1, total_page)
        url1 = url.replace('pageNo=1', f'pageNo={random_page}')
        res1 = self.sess.get(url=url1, headers=header)
        try:
            assert res1.json()['success'] is True
        except AssertionError:
            print('搜索商品失败')
        return res1.json()

    # 获取id信息
    def get_id(self):
        try:
            infos = self.search_goods()['result']['records']
            random_id = random.choice(infos)['id']
        except:
            print('获取ID失败')
            random_id = None
        return random_id

    # 通过ID查询商品
    def select_goodsbyID(self, id):
        url = f'http://18.118.13.94:8080/jeecg-boot/sys/api/homePage/queryGoodsById?id={id}'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/100.0.4896.60Safari/537.36Edg/100.0.1185.29',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        res = self.sess.get(url=url, headers=header)
        try:
            assert res.json()['success'] is True
            goodsinfo = res.json()['result']
        except:
            print('通过ID查询商品失败')
            goodsinfo = None
        print(f'商品信息为{goodsinfo}')
        return goodsinfo

    # 获取运费
    def get_freight(self, id):
        url = f'http://18.118.13.94:8080/jeecg-boot/sys/api//homePage/getFreight?ids={id},&type=2'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/100.0.4896.60Safari/537.36Edg/100.0.1185.29',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        res = self.sess.get(url=url, headers=header)
        try:
            assert res.json()['success'] is True
            freight = res.json()['result']
        except AssertionError:
            print('获取运费出错啦！')
            freight = None
        print(f'运费为{freight}')
        return freight

    # 订单结算页获取可用优惠券
    def get_coupons(self):
        url = 'http://18.118.13.94:8080/jeecg-boot/sys/api/homePage/getMyDiscountsList?pageNo=1&pageSize=10&type=1'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/100.0.4896.60Safari/537.36Edg/100.0.1185.29',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        res = self.sess.get(url=url, headers=header)
        try:
            assert res.json()['success'] is True
            coupons_infos = res.json()['result']['records']
            print(f'存在{len(coupons_infos)}条可用优惠券')
            if not coupons_infos:
                coupons_info = {'id': 0, 'couponsAmount': 0}
            else:
                coupons_info = random.choice(coupons_infos)
        except AssertionError:
            print('获取优惠券失败')
            coupons_info = None
        print(f'优惠券信息为{coupons_info}')
        return coupons_info

    # 获取地址信息
    def get_address(self):
        url = 'http://18.118.13.94:8080/jeecg-boot/sys/api/homePage/getAddressList?pageNo=1&pageSize=100'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/100.0.4896.60Safari/537.36Edg/100.0.1185.29',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        res = self.sess.get(url=url, headers=header)
        try:
            assert res.json()['success'] is True
            if not res.json()['result']:
                print('地址栏为空，正在新增地址')
                self.add_address()
                self.get_address()
            else:
                address_infos = res.json()['result']
        except AssertionError:
            print('获取地址信息出错啦')
        return address_infos

    def add_address(self):
        url = 'http://18.118.13.94:8080/jeecg-boot/sys/api/homePage/addAddress'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '157',
                  'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/100.0.4896.60Safari/537.36Edg/100.0.1185.29',
                  'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        data = {"firstname": f"{Common().first_name()}", "lastname": f"{Common().last_name()}",
                "contactnumber": f"{Common().random_phone()}", "area1": "1", "area2": "11", "area3": "C2",
                "postalCode": "123",
                "addressLine": "123", "countryCode": "CN"}
        data = json.dumps(data)
        res = self.sess.post(url=url, headers=header, data=data)
        try:
            res.json()['success'] is True
        except AssertionError:
            print('新增地址失败')

    # 提交订单
    def submitOrder(self, addressID, couponsid, count: int, goodsid, freight: int, saleprice: float, discount: float,
                    couponsAmount: int):
        """
        立即购买提交订单
        :param addressID: 地址ID
        :param couponsid:优惠券ID
        :param count:商品数量
        :param goodsid:商品ID
        :param freight:运费
        :param saleprice:商品销售价格
        :param discount:优惠金额
        :param couponsAmount:优惠券优惠金额
        :return:
        """

        url = 'http://18.118.13.94:8080/jeecg-boot/my/shoppingCart/submitOrder'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '157',
                  'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/100.0.4896.60Safari/537.36Edg/100.0.1185.29',
                  'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        data = {"addressId": f"{addressID}", "couponsid": f"{couponsid}",
                "list": [{"count": count, "goodsId": f"{goodsid}"}],
                "estPrice": f"{(count * saleprice) * discount + freight - couponsAmount}", "freightPrice": freight}
        data = json.dumps(data)
        res = self.sess.post(url=url, headers=header, data=data)
        print(res.json())
        try:
            assert res.json()['success'] is True
            order_info = res.json()['result']
        except AssertionError:
            print('打包订单失败')
            order_info = None
        return order_info

    # 获取用户等级
    def get_userinfo(self):
        url = 'http://18.118.13.94:8080/jeecg-boot/sys/api/homePage/getUserInfo'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/100.0.4896.60Safari/537.36Edg/100.0.1185.29',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        res = self.sess.get(url=url, headers=header)
        try:
            assert res.json()['success'] is True
            lv = res.json()['result']['memberlevel']
            discount = self.Get_discount(lv)
        except AssertionError:
            print('获取会员等级失败')
            discount = None
        return discount

    def Get_discount(self, lv):
        if int(lv) == 0:
            print('等级为非会员')
            discount = 1
        elif int(lv) == 1:
            print('会员等级为 1')
            discount = 0.98
        elif int(lv) == 2:
            print('会员等级为 2')
            discount = 0.9
        elif int(lv) == 3:
            print('会员等级为3')
            discount = 0.88
        elif int(lv) == 4:
            print('会员等级为 4')
            discount = 0.8
        else:
            print('会员等级为 5')
            discount = 0.7
        return discount

    def random_count(self, goodsinfo):
        amount = goodsinfo['amount']
        if amount >= 10:
            count = random.randint(1, 10)
        else:
            count = random.randint(1, amount)  # 获取1-库存值的随机值
        return count

    # 执行支付
    def dopay(self, orderId):
        url = 'http://18.118.13.94:8080/jeecg-boot/sys/pay/doPay'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '157',
                  'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/100.0.4896.60Safari/537.36Edg/100.0.1185.29',
                  'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        data = {"orderId": f"{orderId}", "successUrl": "http://18.118.13.94:81/pay/payment?token=paypal",
                "cancelUrl": "http://18.118.13.94:81/pay/payment?token=paypal"}
        data = json.dumps(data)
        res = self.sess.post(url=url, headers=header, data=data)
        try:
            assert res.json()['success'] is True
            payinfo = res.json()['result']
        except AssertionError:
            print('支付失败')
            payinfo = None
        print(payinfo)
        return payinfo

    def get_result(self, orderId):
        url = f'http://18.118.13.94:8080/jeecg-boot/sys/pay/success?orderId={orderId}'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/100.0.4896.60Safari/537.36Edg/100.0.1185.29',
                  'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
        res = self.sess.get(url=url, headers=header)
        print(res.json())


    def pay(self,url):
        global dr
        dr = webdriver.Edge()
        dr.get(url)
        dr.maximize_window()
        time.sleep(2)
        dr.find_element(by=By.NAME,value='login_email').send_keys('sb-g4721a9160024@personal.example.com')
        dr.find_element(by=By.NAME,value='btnNext').click()
        time.sleep(2)
        dr.find_element(by=By.NAME,value='login_password').send_keys('qwe3541118')
        dr.find_element(by=By.ID,value='btnLogin').click()
        time.sleep(2)

        time.sleep(2)


    def main(self):
        self.search_goods()  # 查询商品
        random_id = self.get_id()  # 随机获取商品ID
        goodsinfo = self.select_goodsbyID(id=random_id)  # 通过ID查询商品详情
        address_info = random.choice(self.get_address())  # 随机获取一条地址信息
        freight = self.get_freight(id=random_id)  # 获取运费信息
        coupons_info = self.get_coupons()  # 获取优惠券信息

        discount = self.get_userinfo()  # 获取会员折扣
        count = self.random_count(goodsinfo)  # 获取随机数量
        orderinfo = self.submitOrder(addressID=address_info['id'], couponsid=coupons_info['id'], count=count,
                                     goodsid=goodsinfo['id'], freight=freight,
                                     saleprice=goodsinfo['saleprice'], discount=discount,
                                     couponsAmount=coupons_info['couponsAmount'])  # 提交订单获取订单信息
        payinfo = self.dopay(orderId=orderinfo['id'])
        url = payinfo['url']
        self.pay(url)
        self.get_result(orderId=orderinfo['id'])


if __name__ == '__main__':
    a = story_shoping()
    # a.get_coupons()
    a.main()
