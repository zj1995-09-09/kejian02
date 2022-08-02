'''
get
post
'''
import requests

# 发送get请求
# 接口地址
# 本地http: // host: port / user / login
# 写代码之前先用postaman手工测试一把

url = 'http://httpbin.org/get'
headers = {'xyz': 'name'}
data = {'username': 'yuz', 'password': '123'}
resp = requests.get(url, params=data, headers=headers)
print(resp.json())

# html xml
# XML与HTML的区别在于XML是被用来传输和存储数据，其重点在于数据的内容
# HTML是用来显示数据，其重点是数据的外观。
# 怎么从网页中获取数据，简单来说就是通过URL来获取HTML文档。HTTP（超文本传输协议）构建与TCP/IP
# 协议之上，是网络浏览器和网络服务器之间的应用层协议，是一种通用的，无状态的，面向对象的协议

print(resp.text)
print(resp.content)

# content通常是用来获取图片的二进制字节码的
#
# text是用来获取字符串的，通常是某网页源代码字符串。
#
# json()通常是用来获取对象的ISON格式数据的，
