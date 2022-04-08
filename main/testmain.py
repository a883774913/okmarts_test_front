"""
前端接口测试入口
"""
import allure
import pytest

from Okmarts_test_front.data.get_data import Get_Data
from Okmarts_test_front.mode.Discounts import Discounts
from Okmarts_test_front.mode.Favorites import Favorites
from Okmarts_test_front.mode.Query import Query
from Okmarts_test_front.mode.address_mode import Address_mode
from Okmarts_test_front.mode.change_password import Change_Password
from Okmarts_test_front.mode.claen_testdata import Clean_testdata
from Okmarts_test_front.mode.Embedded_data import Embedded_data
from Okmarts_test_front.mode.do_pay import DoPay
from Okmarts_test_front.mode.get_code import GET_Code
from Okmarts_test_front.mode.login import Login
from Okmarts_test_front.mode.news import News
from Okmarts_test_front.mode.order import order
from Okmarts_test_front.mode.regist import Regist
from Okmarts_test_front.mode.registerCoupons import RegisterCoupons
from Okmarts_test_front.mode.shopingcar_mode import Shoping_car
from Okmarts_test_front.mode.sign import Sign
from Okmarts_test_front.mode.updateUserInfo import UpdateUserinfo
from Okmarts_test_front.mode.withdrawal import Withdrawal


@allure.epic("O&Kmarts 前端接口测试用例")
class TestMain:
    def setup_class(self):
        Embedded_data().add_address(4)
        Embedded_data().add_car(30)
        Embedded_data().add_favorites(15)

    def teardown_class(self):
        Clean_testdata().claen_address(10)
        Clean_testdata().clean_shopingcar()
        Clean_testdata().clean_favorites()

    login_cases = Get_Data().get_exclinfo()['登录']
    login_casename = Get_Data().casename_list('登录')

    @allure.feature("登录模块")
    @pytest.mark.parametrize("Parameters", login_cases, ids=login_casename)
    def test_login(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Login().login(Parameters)

    registe_cases = Get_Data().get_exclinfo()['注册']
    registe_casename = Get_Data().casename_list('注册')

    @allure.feature("注册模块")
    @pytest.mark.parametrize("Parameters", registe_cases, ids=registe_casename)
    def test_registe(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Regist().regist(Parameters)

    goodstype_list_cases = Get_Data().get_exclinfo()['商品类型表']
    goodstype_list_casename = Get_Data().casename_list('商品类型表')

    @allure.feature("首页查询")
    @allure.story("查询商品类型")
    @pytest.mark.parametrize("Parameters", goodstype_list_cases, ids=goodstype_list_casename)
    def test_goodstype_list(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    searchSystem_list_cases = Get_Data().get_exclinfo()['搜索系统']
    searchSystem_list_casename = Get_Data().casename_list('搜索系统')

    @allure.feature("首页查询")
    @allure.story("系统查询")
    @pytest.mark.parametrize("Parameters", searchSystem_list_cases, ids=searchSystem_list_casename)
    def test_searchSystem_list(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    getHomeBanner_list_cases = Get_Data().get_exclinfo()['首页广告位']
    getHomeBanner_list_casename = Get_Data().casename_list('首页广告位')

    @allure.feature("首页查询")
    @allure.story("首页广告位查询")
    @pytest.mark.parametrize("Parameters", getHomeBanner_list_cases, ids=getHomeBanner_list_casename)
    def test_getHomeBanner_list(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    getHomeGoods_list_cases = Get_Data().get_exclinfo()['首页商品数据']
    getHomeGoods_list_casename = Get_Data().casename_list('首页商品数据')

    @allure.feature("首页查询")
    @allure.story("首页商品数据")
    @pytest.mark.parametrize("Parameters", getHomeGoods_list_cases, ids=getHomeGoods_list_casename)
    def test_getHomeGoods_list(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    signQuery_list_cases = Get_Data().get_exclinfo()['签到查询']
    signQuery_list_casename = Get_Data().casename_list('签到查询')

    @allure.feature("签到")
    @allure.story("签到查询")
    @pytest.mark.parametrize("Parameters", signQuery_list_cases, ids=signQuery_list_casename)
    def test_signQuery_list(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    routeUrl_list_cases = Get_Data().get_exclinfo()['路由信息']
    routeUrl_list_casename = Get_Data().casename_list('路由信息')

    @allure.feature("首页查询")
    @allure.story("路由查询")
    @pytest.mark.parametrize("Parameters", routeUrl_list_cases, ids=routeUrl_list_casename)
    def test_routeUrl_list(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    fuzzyquery_byname_list_cases = Get_Data().get_exclinfo()['模糊查询']
    fuzzyquery_byname_list_casename = Get_Data().casename_list('模糊查询')

    @allure.feature("模糊查询")
    @pytest.mark.parametrize("Parameters", fuzzyquery_byname_list_cases, ids=fuzzyquery_byname_list_casename)
    def test_fuzzyquery_byname_list(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    queryGoodsById_cases = Get_Data().get_exclinfo()['查询商品详情']
    queryGoodsById_casename = Get_Data().casename_list('查询商品详情')

    @allure.feature("查询商品详情")
    @pytest.mark.parametrize("Parameters", queryGoodsById_cases, ids=queryGoodsById_casename)
    def test_queryGoodsById(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    shop_car_list_cases = Get_Data().get_exclinfo()['购物车表']
    shop_car_list_casename = Get_Data().casename_list('购物车表')

    @allure.feature("购物车")
    @allure.story("购物车表-分页查询")
    @pytest.mark.parametrize("Parameters", shop_car_list_cases, ids=shop_car_list_casename)
    def test_shop_car_list(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    shoppingCart_add_cases = Get_Data().get_exclinfo()['添加购物车']
    shoppingCart_add_casename = Get_Data().casename_list('添加购物车')

    @allure.feature("购物车")
    @allure.story("添加商品到购物车")
    @pytest.mark.parametrize("Parameters", shoppingCart_add_cases, ids=shoppingCart_add_casename)
    def test_shoppingCart_add(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Shoping_car().shoping_car_add(Parameters)

    shoppingCart_edit_cases = Get_Data().get_exclinfo()['购物车-编辑']
    shoppingCart_edit_casename = Get_Data().casename_list('购物车-编辑')

    @allure.feature("购物车")
    @allure.story("购物车-编辑")
    @pytest.mark.parametrize("Parameters", shoppingCart_edit_cases, ids=shoppingCart_edit_casename)
    def test_shoppingCart_edit(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Shoping_car().shoping_car(Parameters)

    batchDelShopCart_cases = Get_Data().get_exclinfo()['购物车-批量删除']
    batchDelShopCart_casename = Get_Data().casename_list('购物车-批量删除')

    @allure.feature("购物车")
    @allure.story("购物车-批量删除")
    @pytest.mark.parametrize("Parameters", batchDelShopCart_cases, ids=batchDelShopCart_casename)
    def test_batchDelShopCart(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Shoping_car().shoping_car(Parameters)

    getAddressList_cases = Get_Data().get_exclinfo()['获取地址信息']
    getAddressList_casename = Get_Data().casename_list('获取地址信息')

    @allure.feature("地址管理")
    @allure.story("获取地址信息")
    @pytest.mark.parametrize("Parameters", getAddressList_cases, ids=getAddressList_casename)
    def test_getAddressList(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    addAddress_cases = Get_Data().get_exclinfo()['新增地址']
    addAddress_casename = Get_Data().casename_list('新增地址')

    @allure.feature("地址管理")
    @allure.story("新增地址")
    @pytest.mark.parametrize("Parameters", addAddress_cases, ids=addAddress_casename)
    def test_addAddress(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Address_mode().address_mode(Parameters)

    address_edit_cases = Get_Data().get_exclinfo()['修改地址']
    address_edit_casename = Get_Data().casename_list('修改地址')

    @allure.feature("地址管理")
    @allure.story("修改地址")
    @pytest.mark.parametrize("Parameters", address_edit_cases, ids=address_edit_casename)
    def test_address_edit(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Address_mode().address_mode(Parameters)

    change_address_cases = Get_Data().get_exclinfo()['修改默认地址']
    change_address_casename = Get_Data().casename_list('修改默认地址')

    @allure.feature("地址管理")
    @allure.story("修改默认地址")
    @pytest.mark.parametrize("Parameters", change_address_cases, ids=change_address_casename)
    def test_change_address(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Address_mode().address_mode(Parameters)

    address_delete_cases = Get_Data().get_exclinfo()['删除地址']
    address_delete_casename = Get_Data().casename_list('删除地址')

    @allure.feature("地址管理")
    @allure.story("删除地址")
    @pytest.mark.parametrize("Parameters", address_delete_cases, ids=address_delete_casename)
    def test_address_delete(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Address_mode().address_mode(Parameters)

    submitOrder_cases = Get_Data().get_exclinfo()['提交订单']
    submitOrder_casename = Get_Data().casename_list('提交订单')

    @allure.feature("提交订单")
    @pytest.mark.parametrize("Parameters", submitOrder_cases, ids=submitOrder_casename)
    def test_submitOrder(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        order().order(Parameters)

    dopay_cases = Get_Data().get_exclinfo()['执行支付']
    dopay_casename = Get_Data().casename_list('执行支付')

    @allure.feature("执行支付")
    @pytest.mark.parametrize("Parameters", dopay_cases, ids=dopay_casename)
    def test_dopay(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        DoPay().dopay(Parameters)

    sign_list_cases = Get_Data().get_exclinfo()['签到']
    sign_list_casename = Get_Data().casename_list('签到')

    @allure.feature("签到")
    @allure.story("签到")
    @pytest.mark.parametrize("Parameters", sign_list_cases, ids=sign_list_casename)
    def test_sign(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Sign().sign(Parameters)

    usersAttentionGoods_add_cases = Get_Data().get_exclinfo()['添加收藏']
    usersAttentionGoods_add_casename = Get_Data().casename_list('添加收藏')

    @allure.feature("收藏")
    @allure.story("添加收藏")
    @pytest.mark.parametrize("Parameters", usersAttentionGoods_add_cases, ids=usersAttentionGoods_add_casename)
    def test_usersAttentionGoods_add(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Favorites().favorites(Parameters)

    usersAttentionGoods_delete_cases = Get_Data().get_exclinfo()['删除收藏']
    usersAttentionGoods_delete_casename = Get_Data().casename_list('删除收藏')

    @allure.feature("收藏")
    @allure.story("删除收藏")
    @pytest.mark.parametrize("Parameters", usersAttentionGoods_delete_cases, ids=usersAttentionGoods_delete_casename)
    def test_usersAttentionGoods_delete(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Favorites().favorites_delete(Parameters)

    usersAttentionGoods_list_cases = Get_Data().get_exclinfo()['收藏查询']
    usersAttentionGoods_list_casename = Get_Data().casename_list('收藏查询')

    @allure.feature("收藏")
    @allure.story("收藏查询")
    @pytest.mark.parametrize("Parameters", usersAttentionGoods_list_cases, ids=usersAttentionGoods_list_casename)
    def test_usersAttentionGoods_list(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    usersAttentionGoods_deleteBatch_cases = Get_Data().get_exclinfo()['收藏批量删除']
    usersAttentionGoods_deleteBatch_casename = Get_Data().casename_list('收藏批量删除')

    @allure.feature("收藏")
    @allure.story("批量删除收藏")
    @pytest.mark.parametrize("Parameters", usersAttentionGoods_deleteBatch_cases,
                             ids=usersAttentionGoods_deleteBatch_casename)
    def test_usersAttentionGoods_deleteBatch(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Favorites().favorites_delete(Parameters)

    getUserEmailCode_cases = Get_Data().get_exclinfo()['获取验证码']
    getUserEmailCode_casename = Get_Data().casename_list('获取验证码')

    @allure.feature("获取验证码")
    @pytest.mark.parametrize("Parameters", getUserEmailCode_cases, ids=getUserEmailCode_casename)
    def test_getUserEmailCode_casename(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        GET_Code().get_code(Parameters)

    updateUserPassword_cases = Get_Data().get_exclinfo()['修改密码']
    updateUserPassword_casename = Get_Data().casename_list('修改密码')

    @allure.feature("修改密码")
    @pytest.mark.parametrize("Parameters", updateUserPassword_cases, ids=updateUserPassword_casename)
    def test_updateUserPassword(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Change_Password().change_password(Parameters)

    getMyDiscountsList_cases = Get_Data().get_exclinfo()['获取我的优惠券']
    getMyDiscountsList_casename = Get_Data().casename_list('获取我的优惠券')

    @allure.feature("优惠券")
    @allure.story("获取我的优惠券")
    @pytest.mark.parametrize("Parameters", getMyDiscountsList_cases, ids=getMyDiscountsList_casename)
    def test_getMyDiscountsList(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Discounts().discount(Parameters)

    queryDiscountsPageList_cases = Get_Data().get_exclinfo()['获取积分商城优惠券']
    queryDiscountsPageList_casename = Get_Data().casename_list('获取积分商城优惠券')

    @allure.feature("优惠券")
    @allure.story("获取优惠券商城数据")
    @pytest.mark.parametrize("Parameters", queryDiscountsPageList_cases, ids=queryDiscountsPageList_casename)
    def test_queryDiscountsPageList(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    exchangeDiscounts_cases = Get_Data().get_exclinfo()['兑换优惠券']
    exchangeDiscounts_casename = Get_Data().casename_list('兑换优惠券')

    @allure.feature("优惠券")
    @allure.story("兑换优惠券")
    @pytest.mark.parametrize("Parameters", exchangeDiscounts_cases, ids=exchangeDiscounts_casename)
    def test_exchangeDiscounts(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Discounts().exchange_discounts(Parameters)

    registerCoupons_cases = Get_Data().get_exclinfo()['注册优惠券']
    registerCoupons_casename = Get_Data().casename_list('注册优惠券')

    @allure.feature("优惠券")
    @allure.story("注册优惠券")
    @pytest.mark.parametrize("Parameters", registerCoupons_cases, ids=registerCoupons_casename)
    def test_registerCoupons(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        RegisterCoupons().registerCoupons(Parameters)

    getUserInfo_cases = Get_Data().get_exclinfo()['获取用户信息']
    getUserInfo_casename = Get_Data().casename_list('获取用户信息')

    @allure.feature("获取用户信息")
    @pytest.mark.parametrize("Parameters", getUserInfo_cases, ids=getUserInfo_casename)
    def test_getUserInfo(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    updateUserInfo_cases = Get_Data().get_exclinfo()['修改用户信息']
    updateUserInfo_casename = Get_Data().casename_list('修改用户信息')

    @allure.feature("修改用户信息")
    @pytest.mark.parametrize("Parameters", updateUserInfo_cases, ids=updateUserInfo_casename)
    def test_updateUserInfo(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        UpdateUserinfo().update_userinfo(Parameters)


    withdrawalCheckPassword_cases = Get_Data().get_exclinfo()['检查密码']
    withdrawalCheckPassword_casename = Get_Data().casename_list('检查密码')

    @allure.feature("积分提现")
    @allure.story("积分提现_检查密码")
    @pytest.mark.parametrize("Parameters", withdrawalCheckPassword_cases, ids=withdrawalCheckPassword_casename)
    def test_withdrawalCheckPassword(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Withdrawal().Withdrawal(Parameters)

    addWithdrawal_cases = Get_Data().get_exclinfo()['积分兑换']
    addWithdrawal_casename = Get_Data().casename_list('积分兑换')

    @allure.feature("积分提现")
    @allure.story("积分兑换")
    @pytest.mark.parametrize("Parameters", addWithdrawal_cases, ids=addWithdrawal_casename)
    def test_addWithdrawal(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Withdrawal().Withdrawal(Parameters)

    getMyOrderList_cases = Get_Data().get_exclinfo()['订单查询']
    getMyOrderList_casename = Get_Data().casename_list('订单查询')

    @allure.feature("订单查询")
    @pytest.mark.parametrize("Parameters", getMyOrderList_cases, ids=getMyOrderList_casename)
    def test_getMyOrderList(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    queryNoticePage_cases = Get_Data().get_exclinfo()['通知消息列表']
    queryNoticePage_casename = Get_Data().casename_list('通知消息列表')

    @allure.feature("通知消息列表")
    @pytest.mark.parametrize("Parameters", queryNoticePage_cases, ids=queryNoticePage_casename)
    def test_queryNoticePage(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    news_list_cases = Get_Data().get_exclinfo()['新闻分页查询']
    news_list_casename = Get_Data().casename_list('新闻分页查询')

    @allure.feature("新闻")
    @allure.story("新闻分页查询")
    @pytest.mark.parametrize("Parameters", news_list_cases, ids=news_list_casename)
    def test_news_list(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)


    listFowHot_cases = Get_Data().get_exclinfo()['新闻版块热销商品']
    listFowHot_casename = Get_Data().casename_list('新闻版块热销商品')

    @allure.feature("新闻")
    @allure.story("新闻版块热销商品")
    @pytest.mark.parametrize("Parameters", listFowHot_cases, ids=listFowHot_casename)
    def test_listFowHot(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        Query().query(Parameters)

    newInformation_queryById_cases = Get_Data().get_exclinfo()['新闻详情']
    newInformation_queryById_casename = Get_Data().casename_list('新闻详情')

    @allure.feature("新闻")
    @allure.story("新闻详情")
    @pytest.mark.parametrize("Parameters", newInformation_queryById_cases, ids=newInformation_queryById_casename)
    def test_newInformation_queryById(self, Parameters):
        allure.dynamic.title(Parameters['casename'])  # 测试用例名称
        News().news(Parameters)


if __name__ == '__main__':
    pytest.main([__file__])
