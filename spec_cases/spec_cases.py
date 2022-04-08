# -*- coding: UTF-8 -*-
"""
存放特殊用例
"""


class Spec_Cases:

    def spec_cases(self):
        spec_cases = {
            "spec_userAccount":['缺少userAccount参数请求失败','userAccount为空请求失败','userAccount参数错误请求失败','userAccount不包含@注册失败'
                ,'userAccount 存在中文注册失败','使用已注册的userAccount注册失败'],
            "spec_password": ['缺少password参数请求失败','password为空请求失败','password参数错误请求失败','password17位字符注册失败'
                ,'password5位字符注册失败','password6位字符注册成功','password等于16位字符注册成功','password包含中文注册失败'],
            "spec_count" : ['count参数为空新增失败','count参数丢失新增失败','count参数不为INT型新增失败','count参数为负数新增失败','count为非数字提交订单失败','count为空提交订单失败','缺少count提交订单失败','输入负数Count参数提交订单失败',
                            '参数count缺失编辑失败','参数count为空编辑失败','参数count为非数字编辑失败','参数count为0编辑失败','参数count为负数编辑失败'],
            "spec_goodsId" : ['goodsid参数为空新增失败','goodsid参数丢失新增失败','goodsid为非数字型新增失败','goodsid不存在新增失败',],
            "spec_firstname": ['参数First Name不填新增失败','参数First Name参数长度超过限制新增失败','缺少firstname修改地址失败','firstname为空修改地址失败'],
            "spec_lastname":['参数lastname不填新增失败','参数lastname参数长度超过限制新增失败','缺少lastname修改地址失败','lastname为空修改地址失败'],
            "spec_contactnumber":['参数contactnumber不填新增失败','参数contactnumber参数长度超过限制新增失败','缺少contactnumber修改地址失败','contactnumber为空修改地址失败'],
            "spec_ids":['ids为非数字删除失败','不存在ids删除失败'],
            "spec_addressid":['缺少addressid提交订单失败','addressid为空提交订单失败','addressid不存在提交订单失败'],
            "Spec_couponsid":['couponsid为不存在id提交订单失败','couponsid为空提交订单失败'],
            "spec_shopcartid":['shopCartId不存在提交订单失败','shopCartId为空提交订单失败'],
            "spec_orderId":['orderid参数为空发起订单支付失败','orderid参数不存在发起订单支付失败'],
            "spec_code":['code参数为空修改密码失败','code错误修改密码失败'],
            "spec_name":['参数缺失领取优惠券失败','参数name为空领取优惠券失败','未注册账户领取优惠券失败','已领取账户再次领取优惠券失败'],
            "spec_id":['无参数修改失败','参数ID缺失修改失败','参数ID不存在修改失败']
        }
        return spec_cases

