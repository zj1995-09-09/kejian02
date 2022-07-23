'''
此时d01叫做主程序，
excel叫做子模块
'''

# 口诀：编写一个模块，注意顶格写的代码
# 定义变量
# 定义函数
# 定义类

# 调用函数，使用变量尽量不要顶格写

# from lesson10_模块和路径 import excel


if __name__ == '__main__':


    def add(a, b):
        print("add函数")
        return a + b


print(add(3, 5))
print(__name__)
