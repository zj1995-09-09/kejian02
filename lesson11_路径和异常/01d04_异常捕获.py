'''
捕获：防止程序中断，正常执行
'''
except:出行异常会执行的代码
try:
    a / b
except:
    pass

try:
    a / b
except:
    print("b不能为0")

print("无论如何都会执行")