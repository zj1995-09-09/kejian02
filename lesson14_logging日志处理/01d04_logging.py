'''
直接使用logging 有以下问题：
- info 信息没有产生
- 文件输出日志
- 时间，运行日志的位置

最好不要直接用logging.info 这样的操作

'''

import  logging

class Dog():
    def __init__(self,color):
        logging.info('正在初始化')
        self.color = color
        logging.info('获取属性 color')
        self .ke = 'dog'
        logging .warning('警告。。。')
        try:
            a =[]
            a[100]
        except IndexError:
            logging.error('超出异常错误，这里有错误')

    def run(self):
        print('狗在跑')

dog = Dog('黑色')
dog.run()





















