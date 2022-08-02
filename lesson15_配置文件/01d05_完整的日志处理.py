'''
日志收集器logger
级别
处理器准备handler
处理器级别设置
设置日志格式format
添加日志处理器
NOSET 等于没写 废话
debug 调试
info 主体功能
warining 警告
error 犯错
critical 极其严重
'''

import logging
# 日志收集器
logger = logging.getLogger()
logger.setLevel('WARNING')

# 日志处理器
handler = logging.StreamHandler()
handler .setLevel('INFO')

# 文件处理器
file_handler = logging.FileHandler('python36.log',encoding='utf-8')
file_handler.setLevel('INFO')

# 处理器添加到收集器
logger.addHandler(handler)
logger.addHandler(file_handler)

# 设置格式
fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
handler.setFormatter(fmt)
file_handler.setFormatter(fmt)

logger.info('正常执行的逻辑')
logger.error('错误啦')
logger.debug('调试信息')

# 封装成函数，返回值logger
# 封装成类