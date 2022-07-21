# import json
#
# b = min(1, 2, 3, 6)
# print(b)
#
# b = max(1, 1000)
# print(b)
#
# a = (1, 2, 3, 4)
# print(sum(a))
#
# # eval把字符串两边的引号去掉
# print("4+8")
# print(eval("4+8"))
#
# a = "{'name' :'随风'}"
# print(type(a))
# print(type(eval(a)))
#
# b = eval(a)
# print(b['name'])

title = ["case_id", "title", "url"]
data = [1, "登录","http://www.baidu.com"]

total = tuple(zip(title, data))
print(total)
