'''
字符串格式化
'''

name ='周建'
money =10000000
money_chinese ='一千万'

ticket ='''
今收到{}
交来的{}
人民币{}
'''.format(name,money,money_chinese)
print(ticket)
