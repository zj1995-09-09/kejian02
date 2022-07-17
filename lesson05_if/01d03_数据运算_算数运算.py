#to:进行高精度不能用float,转化成Decimal,里面的是字符串类型

from decimal import Decimal
print(Decimal(str(2.1))+Decimal(str(0.2)) ==Decimal(str(2.3)))
# print(Decimal(str(2.1)) + Decimal(str(0.2)) == Decimal(str(2.3)))

print(7/3)
print(7 %3)

# **次方，幂运算
print(3 **3)
