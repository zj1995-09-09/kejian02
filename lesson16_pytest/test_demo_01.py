import pytest


def add():
    '''开发人员写的函数'''
    return a + b


@pytest.mark.smoke
def test_add():
    '''封装起来的测试过程，自动化测试用例
    test_开头的函数
    '''

    ret = add(3, 4)
    expected = 8
#     # if ret == expected
#     print("测试用例通过")
#
# else:
# print("测试用例不通过")
#
# # 断言
# # 如果assert通过，程序会正常执行。
# # assert 不通过，会报错，AssertionError
# try:
#     assert expected == ret
# except AssertionError as e:
#     logging.error("断言失败"，e)
#     assert expected == ret


def test_minus():
    print("第二个用例")
    assert 3 - 2 == -1
