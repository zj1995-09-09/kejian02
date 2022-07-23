a = 3
b = 0
try:
    a / b
except Exception as E:
    print(E)
    print("b不能为0")

print("无论如何都会执行")