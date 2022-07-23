'''
类属性：所有的成员都具备的特征
表示：在类定义的下面去定义变量
类属性 == 类变量
'''

class Car:
    fadongji =True
    wheel = True
    material =['塑料','橡胶']
    # 发动机 车轮 材料

print(Car.wheel)

# 类属性的修改
Car.wheel = False
print(Car.wheel)

# 对象能不能获取类属性
my_car = Car()
print(my_car.material)

# 对象修改属性不影响整个类
my_car.material =['金属']
print(my_car.material)
print(Car.material)