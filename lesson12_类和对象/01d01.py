'''
分组捕获
异常也可以分组
'''

try:
    lst = [1, 2]
    lst[100]
    a / b
except (ZeroDivisionError, IndexError) as err:
    print(err)
    print(type(err))
    print("记录")
except(KeyError, ValueError) as e:
    print("赶紧联系开发")

finally:
    print("无论如何都会执行的操作")

# with open("file") as f:
#     pass
