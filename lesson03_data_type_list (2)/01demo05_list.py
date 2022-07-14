#列表里可以存储任意类型的数据
songs = ["千里之外",
         "那一夜",
         "惊雷",
         "告白气球",
         100,
         "钻石",
         True,
         (1,2),
         {"username":"yuz"},
         [1,2, ["a", "b"]]
         ]
print(songs)
print(type(songs))

#切片获取多个 列表的切片得到的数据类型，列表
print(songs[1:4])

