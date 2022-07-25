'''
super 函数
子类的方法想调用父类的方法，超继承
'''


class Animal:
    def __init__(self, ke, color):
        self.ke = ke
        self.color = color

    def run(self):
        print("动物正在跑。。。")

    def eating(self):
        print("正在吃食物")


class Dog(Animal):
    def __init__(self, dog_color, kind):
        # 调用父类的初始化函数，再定义自己的特征

        self.color = dog_color
        super().__init__('dog', dog_color)
        self.kind = kind
    def run(self):
        print("狗在跑")
        super().eating()


my_dog = Dog('white', 'pig')
my_dog.run()
# print(Dog.__mro__)

# 初始化animal
animal = Animal("dog",'black')
print(animal)
print(type(animal))

# <class '__main__.Animal'>
# 初始化dog
dog = Dog('white','xiaogou')
print(dog.kind)
print(dog.color)



