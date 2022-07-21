cases =[
    ["http://example.com/login","get","yuz"],
    ["http://example.com/register","put","yw"],
    ["http://example.com/info","delete","wen"],
    ["http://example.com/project","option","achool"],
    ["http://example.com/interface","head","orange"]
]


for case in cases:
    print("case:",case)
    for data in case:
        print("data:",data)