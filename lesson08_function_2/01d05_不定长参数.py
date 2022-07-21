'''
*b 表示不定长参数：长度不固定，剩下的我全要，垃圾桶
接受所有剩下的位置参数
多个数据放到一个变量元组

**kw,接受关键字参数 kw得到的是字典
不定长是函数定义的时候接受多个值
'''

# def add(a, *b, c, **kw):
#     print("a:", a)
#     print("b:", b)
#     print("kw:", kw)
#
# add(4,5,6,7,8, c=9, d="hello")


# name ="yuz"
# # 拆包
# dalao =["zaizai","achool"]
# add(name,*dalao)

def minus(a,**kw):
    print(a)
    print(kw)

name ="yuz"
info ={"age":18,"gender":"男"}
minus(name,**info)

#不定长参数。*args  **kwargs keyword_args

