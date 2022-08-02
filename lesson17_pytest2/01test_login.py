'''
写一个登陆函数，输入用户名和密码，如果用户名 ='yuz' 并且密码 =‘123456’ 返回'登陆成功‘，否则返回’登陆失败‘
编写测试用例函数，测试上面的登陆函数。至少3个测试用例
使用pytest运行登陆成功用例（可以把运行的命令作为注释写在模块中）
'''


def login(username, password):
    if username == 'yuz' and password == '123456':
        return '登陆成功'
    return '登陆失败'


def test_login1():
    # 第一个用例
    u = ''
    p = ''
    expected = '登陆失败'
    ret = login(u, p)
    assert ret == expected


def test_login2():
    # 第一个用例
    u = 'a'
    p = 'b'
    expected = '登陆失败'
    ret = login(u,p)
    assert ret  == expected

def test_login3():
    # 第一个用例
    u = 'yuz'
    p = '123456'
    expected = '登陆成功'
    ret = login(u,p)
    assert ret == expected

