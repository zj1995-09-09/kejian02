'''
放在类里面的函数就叫方法 method
方法：代表类或实例的行为
方法怎么调用：__init__()
实例方法：就是一个对象（个体 ）特有的行为 实例属性
类方法：整个类具有的行为
普通方法：调用实例方法 obj.方法（）
带有self的是实例方法


类方法和实例方法：类方法会在方法上面加一个声明@classmethod
静态方法（static method）:在方法当中，不需要用到对象self,又不需要用类cls
当你需要吧一个普通的函数放在类下面的时候，方便管理
'''


def baoyang():
    '''
    和类，和对象没有关系
    她就不应该被定义成实例方法
    '''
    print('正在保养。。。')

class Car:
    fadongji = True
    wheel = True
    material =['塑料','橡胶']
    def __init__(self,logo,color):
        print('对象产生时进行的初始化工作')
        print('类里面的',id(self))
        self.brand =logo
        self.color =color

    def drive(self,distance =500):
        '''
        开车
        '''
        print("{}开起来非常快，而且可以续航{}公里".format(self,distance))

    @classmethod
    def fly(cls):
        '''
        飞
        '''
        print('{}正在飞'.format(cls))

    @classmethod
    def other_class_method(cls):
        print("other")

    @classmethod
    def baoyang(cls):
        '''
    和类，对象没有关系
    她就不应该被定义成实例方法
        '''
        print('正在保养。。。')

your_car =Car('h','heise')
print('品牌'+ your_car.brand)
print(your_car.color)
your_car.drive()
# 实例可以调用类方法
your_car.fly()
Car.fly()


# 静态方法怎么调用
Car.baoyang()
your_car.baoyang()
