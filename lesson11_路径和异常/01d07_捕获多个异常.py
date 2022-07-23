a = 3
b = 0

try:
    #可能发生异常的代码
    lst = [1,2]
    lst[100]
    a/b
except ZeroDivisionError as E:
    print(E)
    print("记录")
except IndexError as B :
    print(B)
    print("赶紧联系开发")

print("无论如何都会执行")