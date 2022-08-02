'''
写一个登录函数，输入用户名和密码，如果用户名 = 'yuz',并且密码'123456'返回登录成功，否则返回登陆失败
编写测试用例函数，测试上面的登录函数 至少3个测试用例
使用pytest运行
'''

import pytest


def login(username, password):
    if username == 'yuz' and password == '123456':
        return '登陆成功'
    return '登陆失败'


data = [
    {'username': 'yuz', 'password': '123456', 'expected': '登陆成功'},
    {'username': '', 'password': '', 'expected': '登陆失败'},
    {'username': 'a', 'password': 'b', 'expected': '登陆失败'},
]


@pytest.mark.parametrize('info', data)
def test_login(info):
    # test_login1
    # test_login2
    # test_login3
    u = info['username']
    p = info['password']
    exp = info['expected']
    assert exp == login(u, p)
