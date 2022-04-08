"""
post 类型方法判断
"""

import requests


def post(sess,casename, url, data, header, result, assert_way, content_type):
    """
    :param sess: 会话
    :param casename: 用例名称
    :param url: 地址
    :param data: data数据
    :param header: 请求头
    :param result: 测试预期结果
    :param assert_way: 断言方式
    :param content_type: content-type
    :return:
    """

    if "GET" in casename:
        res = sess.get(url=url, data=data.encode('utf-8'), headers=header)
        print('入口 2')
        print(res.json())
        print(f'预期结果为 {result}')
        print(f'实际结果为 {res.json()[assert_way]}')
        assert result in res.json()[assert_way]
    elif "PUT" in casename:
        res = sess.put(url=url, data=data.encode('utf-8'), headers=header)
        print('入口 3')
        print(res.json())
        print(f'预期结果为 {result}')
        print(f'实际结果为 {res.json()[assert_way]}')
        assert result in res.json()[assert_way]
    elif "DELETE" in casename:
        res = sess.delete(url=url, data=data.encode('utf-8'), headers=header)
        print('入口 4')
        print(res.json())
        print(f'预期结果为 {result}')
        print(f'实际结果为 {res.json()[assert_way]}')
        assert result in res.json()[assert_way]
    elif '未登录' in casename:
        header = {'Host': '18.118.13.94:8080', 'Connection': 'keep-alive', 'Content-Length': '64',
                  'X-Access-Token': 'null',
                  'Accept': 'application/json,text/plain,*/*',
                  'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/99.0.4844.51Safari/537.36Edg/99.0.1150.39',
                  'Content-Type': f'{content_type};charset=UTF-8', 'Origin': 'http://18.118.13.94:81',
                  'Referer': 'http://18.118.13.94:81/', 'Accept-Encoding': 'gzip,deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6', 'sec-gpc': '1'}
        res = requests.post(url=url, headers=header, data=data.encode('utf-8'))
        print('入口 5')
        print(res.json())
        print(f'预期结果为 {result}')
        print(f'实际结果为 {res.json()[assert_way]}')
        assert result in res.json()[assert_way]
    else:
        res = sess.post(url=url, data=data.encode('utf-8'), headers=header)
        print('入口 0')
        print(res.json())
        print(f'预期结果为 {result}')
        print(f'实际结果为 {res.json()[assert_way]}')
        assert result in res.json()[assert_way]
