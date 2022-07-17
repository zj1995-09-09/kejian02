age = 17
driver = False
work_hour = 9

if age >= 18:
    print("我可以喝酒")
    if driver:
        print("不能喝酒")
    else:
        if work_hour > 9:
            print("最好不要喝")
        elif 9 >= work_hour > 6:
            print("可以喝酒")
        else:
            print("钱不够")
else:
    print("满18周未成年")