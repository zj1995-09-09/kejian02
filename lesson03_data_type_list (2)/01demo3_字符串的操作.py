# name ="yuze wang"
# print(name.count('e'))
# print(name.count(" "))
#
# #多个字符串一定要放到列表或者元组当中
# new_name ="".join(["雨泽","遇着","最闪亮"])
# print(new_name)
#
# print("雨泽"+ "/"+"遇着"+"最闪亮")
#
# # replace替换字符串
# name ="遇着遇着最闪亮"
# name =name.replace("闪亮","最好")
# print(name)

# split字符串切割 和join对应
name =' 遇着遇着/最闪亮 '
print(name.split('着'))

#把字符串左右两边的字符去掉，默认是空格默认是strip
print(name.strip())