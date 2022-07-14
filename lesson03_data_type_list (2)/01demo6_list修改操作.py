songs =["千里之外","2022",'那一夜']
#添加一个元素
songs.append('hello')
print(songs)

#一次添加多个元素，列表合并
songs.extend(['歌曲1','歌曲2'])
print(songs)

#可以选择添加的位置，insert
songs.insert(1,2)
print(songs)

#删除操作，删除所有的元素
# 清空列表当中的元素
songs.remove('千里之外')
print(songs)

#根据索引删除
songs.pop(1)
print(songs)

del songs[0]
print(songs)


#修改索引为0的元素
songs[0] =1
print(songs)

#查，索引，切片
print(songs.count('hello'))
#获取索引
print(songs.index(1))



#字符串当中find 和 index 区别，找不到index报错，find -1


#排序
songs =[3,6,4.5]
songs.sort()
print(songs)

#反序
songs.reverse()
print(songs)








