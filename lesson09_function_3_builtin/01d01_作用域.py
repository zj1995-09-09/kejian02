# 变量，局部变量和全局变量
# 局部：在函数体或者代码块里面定义的变量
# 全局：文件里面定义的变量
#局部作用域能不能获取全局变量 可以

# a ="随风"
# def add():
#     b =a +"王"
#     print(b)
#     return None
#
# add()

# def add():
#     a =1
#     print(a)
#     return a
#
# print(a)

a ="随风"

def add():
    global a
    a =a+"王"
    print(a)
    return None

add()