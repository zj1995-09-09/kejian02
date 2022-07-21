def get_offer(name,money,food):
    '''获得offer'''
    print("{}拿到了一个{}k的offer".format(name,money))
    eat(name,food)


def eat(eat_name,eat_food):
    print("{}最喜欢吃{}".format(eat_name,eat_food))

get_offer("zhoujian",20,"龙虾")

import keyword
print(keyword.kwlist)




