"""
查询断言模块
"""
import requests


def get(sess,casename,url,data,header,result,assert_way):
    if 'POST' in casename:
        res = sess.post(url=url + '?' + data, headers=header)
        print('入口1')
        print(res.json())
        print(f'预期结果为 {result}')
        print(f'实际结果为 {res.json()[assert_way]}')
        assert result in res.json()[assert_way]
    elif 'DELETE' in casename:
        res = sess.delete(url=url + '?' + data, headers=header)
        print('入口2')
        print(res.json())
        print(f'预期结果为 {result}')
        print(f'实际结果为 {res.json()[assert_way]}')
        assert result in res.json()[assert_way]
    elif 'PUT' in casename:
        res = sess.put(url=url + '?' + data, headers=header)
        print('入口3')
        print(res.json())
        print(f'预期结果为 {result}')
        print(f'实际结果为 {res.json()[assert_way]}')
        assert result in res.json()[assert_way]
    elif '未登录' in casename:
        res = requests.get(url=url + '?' + data)
        print('入口4')
        print(res.json())
        print(f'预期结果为 {result}')
        print(f'实际结果为 {res.json()[assert_way]}')
        assert result in res.json()[assert_way]
    else:
        res = sess.get(url=url + '?' + data, headers=header)
        print('入口0')
        print(res.json())
        print(f'预期结果为 {result}')
        print(f'实际结果为 {res.json()[assert_way]}')
        print(res.url)
        assert result in res.json()[assert_way]