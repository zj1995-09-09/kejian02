import pytest


@pytest.fixture(scope='function', autouse=True)
def function_before():
    '''
    用例前置条件
    '''

    print('测试用例执行前')
    yield 'chrome'  # 生成器函数
    print('测试用例执行之后')

# #斐波那契（Fibonacci）數列是一个非常简单的递归数列，除第一个和第二个数外，任意一个数都可由前两个数相加得到
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
# fab(5)
