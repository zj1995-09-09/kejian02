"""
此时d01 叫做主程序，
而 excel 叫子模块。

口诀：编写一个模块时，注意定格写的代码主要是以下：
- 定义变量
- 定义函数
- 定义类

调用函数，使用变量，尽量不要定格写。

"""

from lesson11_路径和异常 import excel


# def add():
#     print("add函数")

# print(__name__)

if __name__ == '__main__':
    excel.add()