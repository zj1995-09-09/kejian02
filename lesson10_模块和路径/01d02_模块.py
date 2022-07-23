'''
一个py的文件就叫模块。
包含__init__.py的文件夹叫做包
'''

# 模块和包是组织代码的

# 按照功能分类存储，函数会存到不同的模块当中。
# 不同用途的模块又被存到包里

# 模块：内置模块和第三方模块。
# 如果想使用其他模块的代码，就需要导入，import


# import time
# print(time.time())
# import  lesson10_模块和路径.d01_open
# a =lesson10_模块和路径.d01_open.add(3,4)
# print(a)
#
# 直接导入函数
# from lesson10_模块和路径.d01_open import add as module_add
#
# b =module_add(3,4)
# print(b)

# print(d01_open.add(3,4))

# 导入所有
# from lesson10_模块和路径.d01_open import *
# from ... import ... 主要用在自定义模块
# 既可以导入模块，还可以导入函数
#
# from ...import ...as ...重命名
# from ...import * 强烈建议不要用


import time

# print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y-%m-%d %H:%M:%S'))
