# movies =["画皮","蜡笔小新","上海堡垒","你的名字"]
# print(movies[2])
#
# movies ={}
# print(type(movies))
# print(len(movies))
#
# # 字典公式 {key:value,key1:value1,key2:value2}
#
# movies ={"favor":"画皮",
#         "first_with_gf":"蜡笔小新",
#         "second_with_gr":"上海堡垒",
#         "hate":"你的名字",
#         "cried":"心花怒放",
#         1:"大话西游",
#         "0":"情人"
# }
# print(movies)
#
# #通过key获取某个值（索引）
#
# print(movies['first_with_gf'])
# # print(movies[0])
#
# # 切片字典不行，没有同时获取多个的操作
movies = {"favor": "画皮",
         "first_with_gf": "蜡笔小新",
         "second_with_gf": "上海堡垒",
        "hate": "你的名字",
        {1:2}: "大话西游"
         }
print(movies[{1:2}])
