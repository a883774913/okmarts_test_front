"""数据清理模块"""
import json
import random

from Okmarts_test_front.Common.Comm import Common
from Okmarts_test_front.mode.address_mode import Address_mode
from pachong1.userAgent import UserAgent


class Clean_testdata:

    def __init__(self):
        info = Common().get_sess()
        self.sess = info[0]
        self.token = info[1]
        self.User_Agent = random.choice(UserAgent().useragent_list())

    def claen_address(self,number):
        """
        :param number: 循环的次数
        :return:
        """
        err = 0
        for i in range(1,number):
            try:
                Address_mode().address_mode(Parameters={'casename': '输入正确参数删除地址成功', 'url': 'http://18.118.13.94:81/jeecg-boot/sys/api/homePage/updateAddress', 'data': '{"type":3,"id":"1506562052406251520"}', 'content_type': 'application/json', 'result': '成功', 'assert_way': 'message', 'mode': '删除地址'})
            except AssertionError:
                err += 1
            finally:
                print(f'正在执行第{i+1}次数据清理任务，出现了{err}次错误，还剩{number-i-1}次任务')

    def clean_shopingcar(self):
        url = 'http://18.118.13.94:8080/jeecg-boot/my/shoppingCart/batchDelShopCart'
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '149', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'User-Agent': f'{self.User_Agent}',
                  'Content-Type': 'application/json;charset=UTF-8', 'Origin': 'http://18.118.13.94:81', 'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}

        id_li = Common().select_shopcar_ids()       #获取购物车所有id列表集合
        data = {"ids":f"{Common().splicing_all_id(id_li)}"}
        data = json.dumps(data)
        res = self.sess.post(url=url,data=data,headers=header)
        assert '操作成功' in res.json()['message']

    def clean_favorites(self):
        url = 'http://18.118.13.94:8080/jeecg-boot/sys/api/usersAttentionGoods/deleteBatch'

        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Accept': 'application/json,text/plain,*/*',
                  'X-Access-Token': f'{self.token}',
                  'Content-Type': 'application/x-wwwform-urlencoded',
                  'User-Agent': f'{self.User_Agent}', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/',
                  'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        id_li = Common().get_favorites_ids()    #获取所有收藏商品列表
        data = f"ids={Common().splicing_all_id(id_li)}"
        res = self.sess.delete(url=url+'?'+ data,headers=header)
        assert '操作成功' in res.json()['message']






if __name__ == '__main__':
    a = Clean_testdata()
    a.claen_address(10)
    # a.clean_shopingcar()
    # a.clean_favorites()