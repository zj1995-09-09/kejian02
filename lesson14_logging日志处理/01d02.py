'''
super 函数
子类的方法想调用父类的方法 。超继承
'''


class Dog():
    def __init__(self,color):
        self.color =color
        self.ke ='dog'

    def run(self):
        print('狗在跑')

# 获取某个属性 getattr()
# 设置某个属性 setattr()

my_dog =Dog('black')
print(my_dog.color)
