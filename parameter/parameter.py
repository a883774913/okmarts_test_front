# -*- coding: UTF-8 -*-
"""
存放data处理中的参数
"""
import random
import re

from Okmarts_test_front.Common.Comm import Common
from 在邮箱中获取验证码 import Get_Code


class Parameters_cls:

    @classmethod
    def userAccount(cls, casename, data, spec_userAccount, mode):
        print('存在userAccount参数')
        # 修改name参数 商品名称
        if casename not in spec_userAccount:  # 如果不在特殊用例中则修改参数name
            old_userAccount = re.findall(pattern='"userAccount":"(.*?)"', string=data)[0]
            if mode == '登录':
                userAccount = Common().random_account()[0]
            else:
                if 'userAccount输入31个字符注册失败' == casename:
                    userAccount = Common().random_userAccount_30or31(31)
                elif 'userAccount输入30个字符注册成功' == casename:
                    userAccount = Common().random_userAccount_30or31(30)
                else:
                    userAccount = Common().random_userAccount()
            data = data.replace(f'"userAccount":"{old_userAccount}"', f'"userAccount":"{userAccount}"', 1)
            print(f'修改 userAccount 参数 {old_userAccount} 为 {userAccount} ')
        else:
            print('特殊用例不修改 userAccount 参数 ')
        return data

    @classmethod
    def password(cls, casename, data, spec_password):
        print('存在 password 参数')
        # 修改name参数 商品名称
        if casename not in spec_password:  # 如果不在特殊用例中则修改参数name
            old_password = re.findall(pattern='"password":"(.*?)"', string=data)[0]
            password = Common().random_account()[1]
            data = data.replace(f'"password":"{old_password}"', f'"password":"{password}"', 1)
            print(f'修改 password 参数 {old_password} 为 {password} ')
        else:
            print('特殊用例不修改 password 参数 ')
        return data

    @classmethod
    def id(cls, casename:str, data:str, mode:str):
        """
        替换ID参数方法
        :param casename: 用例名称
        :param data: data数据
        :param mode: 模块
        :return: data
        """
        print('data中存在id参数')
        try:
            if 'id' in casename or 'ID' in casename or 'Id' in casename or 'iD' in casename:  # 如果id在用例中则跳过
                print('特殊用例不执行修改操作')
            else:
                if mode == '购物车表-编辑':
                    old_id = re.findall(pattern='"id":"(.*?)"', string=data)[0]
                    id = Common().select_shopcar_goodsinfo()['id']
                elif mode == '删除地址' or mode == '修改地址' or mode == '切换默认地址':
                    old_id = re.findall(pattern='"id":"(.*?)"', string=data)[0]
                    id = random.choice(Common().select_address_info())
                elif mode == '兑换优惠券':
                    old_id = re.findall(pattern='"id":"(.*?)"',string=data)[0]
                    id = random.choice(Common().select_point_info())
                else:
                    old_id = data.replace('id=', '')
                    id = random.choice(Common().select_homegoods_id())
                data = data.replace(f'{old_id}', f"{id}")
                print(f'替换data参数中的ID {old_id} 为: {id}')
            return data
        except IndexError:
            print('未找到相关ID')
            return data

    @classmethod
    def count(cls, casename, data, spec_count, info, mode):
        print('存在 count 参数')
        if casename not in spec_count:  # 如果不在特殊用例中则修改参数name
            old_count = re.findall(pattern='"count":(\d+)', string=data)[0]
            if mode == '购物车表-编辑' or mode == '购物车表-购买提交订单':
                if casename == '参数count超过商品库存编辑失败' or casename == 'count超过商品最大库存提交订单失败':
                    count = info['stock'] + 1
                else:
                    count= info['goodsamount']
            else:
                if casename == 'count参数大于商品存在数量新增失败':
                    count = info['amount'] + 1
                else:
                    if info['amount'] > 10:
                        count = random.randint(1, 10)
                    else:
                        count = random.randint(1, info['stock'])
            data = data.replace(f'"count":{old_count}', f'"count":{count}', 1)
            print(f'修改 count 参数 {old_count} 为 {count} ')
        else:
            print('特殊用例不修改 count 参数 ')
        return data

    @classmethod
    def goodsId(cls, casename, data, spec_goodsId, goodsinfo, mode):
        print('存在 goodsId 参数')
        if casename not in spec_goodsId:  # 如果不在特殊用例中则修改参数name
            if mode == '购物车表-添加':
                old_goodsId = re.findall(pattern='"goodsId":"(.*?)"', string=data)[0]
                goodsId = goodsinfo['id']
                data = data.replace(f'"goodsId":"{old_goodsId}"', f'"goodsId":"{goodsId}"', 1)
            elif mode == '用户收藏商品表-添加':
                old_goodsId = re.findall(pattern='"goodsid":"(.*?)"', string=data)[0]
                if casename == '已收藏goodsid再次收藏收藏失败':
                    goodsId = random.choice(Common().get_favorites_infos())['goodsid']
                else:
                    goodsId = goodsinfo['id']
                data = data.replace(f'"goodsid":"{old_goodsId}"', f'"goodsid":"{goodsId}"', 1)
            else:
                old_goodsId = re.findall(pattern='"goodsId":"(.*?)"', string=data)[0]
                goodsId = goodsinfo['goodsid']
                data = data.replace(f'"goodsId":"{old_goodsId}"', f'"goodsId":"{goodsId}"', 1)
            print(f'修改 goodsId 参数 {old_goodsId} 为 {goodsId} ')
        else:
            print('特殊用例不修改 goodsId 参数 ')
        return data

    @classmethod
    def firstname(cls, casename, data, spec_firstname):
        print('存在 firstname 参数')
        if casename not in spec_firstname:  # 如果不在特殊用例中则修改参数name
            old_firstname = re.findall(pattern='"firstname":"(.*?)"', string=data)[0]
            firstname = Common().first_name()
            data = data.replace(f'"firstname":"{old_firstname}"', f'"firstname":"{firstname}"', 1)
            print(f'修改 firstname 参数 {old_firstname} 为 {firstname} ')
        else:
            print('特殊用例不修改 firstname 参数 ')
        return data

    @classmethod
    def lastname(cls, casename, data, spec_lastname):
        print('存在 lastname 参数')
        if casename not in spec_lastname:  # 如果不在特殊用例中则修改参数name
            old_lastname = re.findall(pattern='"lastname":"(.*?)"', string=data)[0]
            lastname = Common().last_name()
            data = data.replace(f'"lastname":"{old_lastname}"', f'"lastname":"{lastname}"', 1)
            print(f'修改 lastname 参数 {old_lastname} 为 {lastname} ')
        else:
            print('特殊用例不修改 lastname 参数 ')
        return data

    @classmethod
    def contactnumber(cls, casename, data, Spec_contactnumber):
        print('存在contactnumber参数')
        if casename not in Spec_contactnumber:
            try:
                old_contactnumber = re.findall(pattern='"contactnumber":"(.*?)"', string=data)[0]
                contactnumber = Common().random_phone()
                data = data.replace(f'"contactnumber":"{old_contactnumber}"',
                                    f'"contactnumber":"{contactnumber}"', 1)
                print(f'修改 contactnumber 参数: {old_contactnumber} 为: {contactnumber}')
            except:
                print('参数contactnumber的值未找到！！')
        return data

    @classmethod
    def shop_ids(cls, casename, data, spec_ids):
        print('存在 ids 参数')
        if casename not in spec_ids:
            try:
                old_ids = re.findall(pattern='"ids":"(.*?)"', string=data)[0]
                li = Common().select_shopcar_ids()  # 获取id列表
                if casename == '购物车存在一件商品批量删除成功':
                    ids = Common().Splicing_id(1, li) + ','
                elif casename == 'ids部分参数错误删除购物车失败':
                    ids = 'sss,' + Common().Splicing_id(1, li)
                else:
                    ids = Common().Splicing_id(2, li)  # 处理IO值为 id1,id2,id3样式
                data = data.replace(f'"ids":"{old_ids}"',
                                    f'"ids":"{ids}"')
                print(f'修改 ids 参数: {old_ids} 为: {ids}')
            except:
                print('出错啦！！！')
        else:
            print('特殊用例不修改ids参数')
        return data

    @classmethod
    def addressId(cls, casename, data, Spec_addressId):
        print('存在 addressId 参数')
        if casename not in Spec_addressId:
            try:
                old_addressId = re.findall(pattern='"addressId":"(.*?)"', string=data)[0]
                addressId = random.choice(Common().select_address_info())
                data = data.replace(f'"addressId":"{old_addressId}"',
                                    f'"addressId":"{addressId}"', 1)
                print(f'修改 addressId 参数: {old_addressId} 为: {addressId}')
            except:
                print('参数 addressId 的值未找到！！')
        return data

    # 优惠卷id
    @classmethod
    def couponsid(cls, casename: str, data: str, Spec_couponsid: str, shopcar_info: dict) -> str:
        """
        :param casename:  用例名称
        :param data:    data集合
        :param Spec_couponsid: 特殊用例
        :param shopcar_info: 购物车数据
        :return: 替换couponsid 后的 data
        """
        print('存在 couponsid 参数')
        if casename not in Spec_couponsid:
            try:
                old_couponsid = re.findall(pattern='"couponsid":"(.*?)"', string=data)[0]
                print(f'old_couponsid为 {old_couponsid}')
                if casename == '使用已使用couponsid提交订单失败':
                    print('正在寻找已使用优惠券')
                    couponsinfo = random.choice(Common().get_coupons_info()['已使用'])
                    couponsid = couponsinfo['id']
                    print(f'couponsid 为 {couponsid}')
                else:
                    couponsid = random.choice(
                        Common().get_coupons_id_by_totalprice(shopcar_info['totalprice']))  # 随机选取一个优惠券
                    print(f'couponsid 为 {couponsid}')
                data = data.replace(f'"couponsid":"{old_couponsid}"',
                                    f'"couponsid":"{couponsid}"', 1)
                print(f'修改 couponsid 参数: {old_couponsid} 为: {couponsid}')
            except:
                print('参数 couponsid 的值未找到！！')
        return data

    @classmethod
    def shopCartId(cls, casename, data, Spec_shopCartId, shopcar_info):
        print('存在 shopCartId 参数')
        if casename not in Spec_shopCartId:
            try:
                old_shopCartId = re.findall(pattern='"shopCartId":"(.*?)"', string=data)[0]
                shopCartId = shopcar_info['id']
                data = data.replace(f'"shopCartId":"{old_shopCartId}"',
                                    f'"shopCartId":"{shopCartId}"', 1)
                print(f'修改 shopCartId 参数: {old_shopCartId} 为: {shopCartId}')
            except:
                print('参数 shopCartId 的值未找到！！')
        return data

    @classmethod
    def orderId(cls, casename, data, Spec_orderId):
        print('存在 orderId 参数')
        if casename not in Spec_orderId:
            try:
                old_orderId = re.findall(pattern='"orderId":"(.*?)"', string=data)[0]
                if casename == '使用已支付订单发起支付失败':
                    orderId = random.choice(Common().get_orderid()['支付成功'])
                else :
                    orderId = Common().get_order1()
                data = data.replace(f'"orderId":"{old_orderId}"',
                                    f'"orderId":"{orderId}"', 1)
                print(f'修改 orderId 参数: {old_orderId} 为: {orderId}')
            except:
                print('参数 orderId 的值未找到！！')
        return data

    @classmethod
    def code(cls, casename, data, Spec_code):
        print('存在 code 参数')
        if casename not in Spec_code:
            try:
                old_code = re.findall(pattern='"code":"(.*?)"', string=data)[0]
                code = Get_Code().wangyi(username='a883774918',password='Qwe3541118.',name='hydraulic')[0]
                print(f'code为{code}')
                data = data.replace(f'"code":"{old_code}"',
                                    f'"code":"{code}"', 1)
                print(f'修改 code 参数: {old_code} 为: {code}')
            except:
                print('参数 code 的值未找到！！')
        return data


