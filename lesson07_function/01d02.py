'''
函数都有返回值，在return后面
如果没有写，默认返回return None
'''

# def print_all_dalao():
#     """打印所有的大佬。 Docstring 文档字符串， 说明函数的作用"""
#     # 函数体：运行函数的时候会执行的代码
#     print("1级大佬旧梦")
#     print("2级大佬阿鸡")
#     print("3级大佬Niki")
#
# ret =print_all_dalao()
# print("return value:",ret)


# a =2
# def add():
#     b =a+3
#     return b
#
# print(add())





def add(a,b):
    c =a +b -1
    return c
    print("函数内部",c)

print("函数的返回值:",add(3,4))