# 对象(object),实例
# 内存地址相同，表示的是同一个对象，数据
# 可以通过id(object)函数获取

class Car:
    pass

my_car =Car()
your_car =Car()
# print(my_car)
print(id(my_car))
print(id(your_car))
print(Car == Car)