'''
-post
'''
import requests

# 发送get请求
# 接口地址 本地http://post:port/user/login
# 写代码前 用postman手工测一把

url = 'http://httpbin.org/post?username=yuz&password=123'
headers = {'xyz': 'name', 'content-type': 'application/json'}
data = {'age': 18}
# 如果想传递form-data ,data =a

# 传递json数据，content-type ='application/json',json = data
resp = requests.post(url, headers=headers, json=data)
print(resp.json())
# 二进制的数据，图片，视频，bytes
print(resp.content)
