# open 打开文件
# 文件的路径，如果没有路径，在当前目录查找文件
#
# 得到文件ASCII
# 声明文件的编码格式
f = open("demo.txt", encoding='utf-8')
# 读取文件数据

# print(f.read())
# # readlines

print(f.readlines())
f.close()


# 文件写入
# 打开文件的模式r,w
f =open("demo1.txt",encoding="utf-8",mode="w")
f.write("hello,zhoujian")
f.close()

文件的关闭
