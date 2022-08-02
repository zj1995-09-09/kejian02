import logging

import pytest

def add(a,b):
    '''开发人员写的函数'''
    return a + b

@pytest.mark.smoke
def test_add():
    '''
    封装起来的测试过程，自动化测试用例
    '''
    ret = add(3,4)
    expected = 8
    assert expected == ret

# 如果assert 不通过，AssertionError
#     try:
#         assert expected == ret
#     except AssertionError as e:
#         logging.ERROR('断言失败',e)
#         logging.error('断言失败哦'+ e)
#     assert expected == ret
#

def test_minus():
    print('第二个用例')
    assert  3 - 2 == -1

# if __name__ == '__main__':
#     test add()
#     test test_minus()