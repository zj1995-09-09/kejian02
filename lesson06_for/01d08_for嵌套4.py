keys =["url","method"]
cases =[
    ["login","get"],
    ["register","pos"],
    ["project","put"]
]
lst =[]
for case in cases:
    adict ={}
    # 同时获取列表的索引和值
    for index ,data in enumerate(case):
        adict[keys[index]] =data
    print(adict)
    lst.append(adict)
print(lst)