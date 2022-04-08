# -*- coding: UTF-8 -*-
"""
将用例转换为字典形式
"""

import xlrd

class Get_Data:

    #data无回车可直接使用
    def case_list(self, dict, casename, URL, Parameters, content_type, result, assert_way, list_name,mode):
        dict["casename"] = casename
        dict["url"] = URL
        dict["data"] = Parameters
        dict["content_type"] = content_type
        dict["result"] = result
        dict["assert_way"] = assert_way
        dict["mode"] = mode
        list_name.append(dict)

    def get_exclinfo(self):
        wb = xlrd.open_workbook(r"C:\Users\admin\Desktop\okmarts\O&Kmark\前端接口测试用例.xls")  # 打开文件
        sh = wb.sheet_by_name('前端')  # 获取指定sheet
        General_table = {}

        login_list = []       #登录用例集合
        regist_list = []        #注册用例集合
        goodsType_list = []        #查询商品类型接口
        shop_car_list = []       #购物车表分页查询
        searchSystem_list = []      #查询系统相关接口
        getHomeBanner_list = []          #查询首页广告位数据
        getHomeGoods_list = []          #查询首页商品数据
        signQuery_list = []             #首页签到查询
        routeUrl_list = []              #查询路由信息
        fuzzyquery_byname_list = []     #模糊查询
        queryGoodsById = []             #通过商品id查询详情
        shoppingCart_add = []           #加入到购物车
        shoppingCart_edit = []          #购物车编辑
        getAddressList = []             #获取地址信息
        addAddress = []                 #新增地址
        address_delete = []             #删除地址
        batchDelShopCart = []           #批量删除购物车
        address_edit = []               #编辑地址
        submitOrder = []                #提交订单
        doPay = []                      #订单执行支付
        sign = []                       #签到
        usersAttentionGoods_add = []    #添加收藏
        usersAttentionGoods_delete = [] #删除收藏
        usersAttentionGoods_list = []   #收藏查询
        usersAttentionGoods_deleteBatch = [] #收藏批量删除
        getUserEmailCode = []           #获取验证码
        updateUserPassword = []         #修改密码
        change_address = []             #修改默认地址
        getMyDiscountsList = []         #获取我的优惠券列表
        queryDiscountsPageList = []     #获取积分商城优惠券信息
        exchangeDiscounts = []          #兑换优惠券
        registerCoupons = []           #注册优惠券
        getUserInfo = []                #获取用户信息
        updateUserInfo = []             #修改用户信息
        withdrawalCheckPassword = []     #检查密码
        addWithdrawal  = []             #积分兑换
        getMyOrderList = []             # 通知查询
        queryNoticePage = []            #通知消息列表
        news_list = []                  #新闻查询
        listFowHot = []                 #新闻热销商品
        newInformation_queryById = []   #通过商品ID查询新闻详情



        for i in range(sh.nrows):
            di = {}
            value = sh.row_values(i)
            caseNO = value[0]       #用例编号
            casename = value[1]        #用例标题
            mode = value[2]         #所属模块
            URL = "http://18.118.13.94:81"+value[3]          #接口地址
            URL = URL.replace(' ','')
            Parameters = value[6]                       #参数
            content_type = value[7]                 #请求参数类型
            result = value[8]                       #断言结果
            assert_way = value[9]                   #断言方式
            if mode == "登录":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,login_list,mode)
            if mode == "注册":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,regist_list,mode)
            if mode == "商品类型表":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,goodsType_list,mode)
            if mode == "购物车表-分页列表查询":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, shop_car_list, mode)
            if mode == "搜索系统":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, searchSystem_list, mode)
            if mode == "查询首页广告栏位数据":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, getHomeBanner_list, mode)
            if mode == "查询首页商品数据":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, getHomeGoods_list, mode)
            if mode == "签到查询":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, signQuery_list, mode)
            if mode == "查路由信息":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, routeUrl_list, mode)
            if mode == "根据商品名称模糊查询接口":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, fuzzyquery_byname_list, mode)
            if mode == "查询商品详情":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, queryGoodsById, mode)
            if mode == "购物车表-添加":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, shoppingCart_add, mode)
            if mode == "购物车表-编辑":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, shoppingCart_edit, mode)
            if mode == "获取地址列表":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, getAddressList, mode)
            if mode == "新增地址":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, addAddress, mode)
            if mode == "删除地址":
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, address_delete, mode)
            if mode == '购物车-批量删除' :
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, batchDelShopCart, mode)
            if mode == '修改地址' :
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, address_edit, mode)
            if mode == '购物车表-购买提交订单' :
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, submitOrder, mode)
            if mode == '订单发起支付':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, doPay, mode)
            if mode == '签到':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, sign, mode)
            if mode == '用户收藏商品表-添加':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, usersAttentionGoods_add, mode)
            if mode == '用户收藏商品表-通过id删除':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, usersAttentionGoods_delete,mode)
            if mode == '用户收藏商品表-分页列表查询':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way, usersAttentionGoods_list, mode)
            if mode == '用户收藏商品表-批量删除':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               usersAttentionGoods_deleteBatch, mode)
            if mode == '获取修改账号邮箱的验证码':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               getUserEmailCode, mode)
            if mode == '修改用户密码':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               updateUserPassword, mode)
            if mode == '切换默认地址':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               change_address, mode)
            if mode == '我的优惠券-查询':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               getMyDiscountsList, mode)
            if mode == '积分商城优惠券信息查询':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               queryDiscountsPageList, mode)
            if mode == '兑换优惠券':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               exchangeDiscounts, mode)
            if mode == '注册成功领取优惠券':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               registerCoupons, mode)
            if mode == '获取用户信息':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               getUserInfo, mode)
            if mode == '修改个人信息':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               updateUserInfo, mode)
            if mode == '积分提现_检查密码':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               withdrawalCheckPassword, mode)
            if mode == '积分兑换':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               addWithdrawal, mode)
            if mode == '查询订单信息':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               getMyOrderList, mode)
            if mode == '通知消息列表':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               queryNoticePage, mode)
            if mode == '新闻分页查询':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               news_list, mode)
            if mode == '新闻版块热销商品':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               listFowHot, mode)
            if mode == '查询新闻详情':
                self.case_list(di, casename, URL, Parameters, content_type, result, assert_way,
                               newInformation_queryById, mode)
            else :
                pass

        # print(login_list)
        General_table["登录"] = login_list
        General_table['注册'] = regist_list
        General_table['商品类型表'] = goodsType_list
        General_table['购物车表'] = shop_car_list
        General_table['搜索系统'] = searchSystem_list
        General_table['首页广告位'] = getHomeBanner_list
        General_table['首页商品数据'] = getHomeGoods_list
        General_table['签到查询'] = signQuery_list
        General_table['路由信息']=routeUrl_list
        General_table['模糊查询'] = fuzzyquery_byname_list
        General_table['查询商品详情'] = queryGoodsById
        General_table['添加购物车'] = shoppingCart_add
        General_table['购物车-编辑'] = shoppingCart_edit
        General_table['获取地址信息'] = getAddressList
        General_table['新增地址'] = addAddress
        General_table['删除地址'] = address_delete
        General_table['购物车-批量删除'] = batchDelShopCart
        General_table['修改地址'] = address_edit
        General_table['提交订单']=submitOrder
        General_table['执行支付'] = doPay
        General_table['签到'] = sign
        General_table['添加收藏'] = usersAttentionGoods_add
        General_table['删除收藏'] = usersAttentionGoods_delete
        General_table['收藏查询'] = usersAttentionGoods_list
        General_table['收藏批量删除'] = usersAttentionGoods_deleteBatch
        General_table['获取验证码'] = getUserEmailCode
        General_table['修改密码'] = updateUserPassword
        General_table['修改默认地址'] = change_address
        General_table['获取我的优惠券'] = getMyDiscountsList
        General_table['获取积分商城优惠券'] = queryDiscountsPageList
        General_table['兑换优惠券'] = exchangeDiscounts
        General_table['注册优惠券'] = registerCoupons
        General_table['获取用户信息'] = getUserInfo
        General_table['修改用户信息'] = updateUserInfo
        General_table['检查密码'] = withdrawalCheckPassword
        General_table['积分兑换'] = addWithdrawal
        General_table['订单查询'] = getMyOrderList
        General_table['通知消息列表'] = queryNoticePage
        General_table['新闻分页查询'] = news_list
        General_table['新闻版块热销商品'] = listFowHot
        General_table['新闻详情'] = newInformation_queryById
        return General_table

    #获取用例名称集合 用于ids显示用例名称
    def casename_list(self,mode):
        info = self.get_exclinfo()
        li = []
        for i in range(len(info[mode])):
            casename = info[mode][i]["casename"]
            li.append(casename)
        return li


if __name__ == '__main__':
    a = Get_Data()
    info = a.get_exclinfo()['登录']
    print(info)


