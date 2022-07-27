# 日志收集器logger
# 收集器级别 level
# 处理器准备 handler
# 处理器级别设置
# 设置日志格式 format()
# 日志收集器add 处理器
#
# NOSET 0
# DEBUG 10
# INFO 20
# Warning 30
# ERROR 40
# critical 50

import logging
# 获取日志收集器 logger
logger = logging.getLogger('python 36')
logger.setLevel('WARNING')

# 日志处理器
handler =logging.StreamHandler()
handler.setLevel('DEBUG')

# 文件处理器
file_handler =logging.FileHandler('python36.log',encoding='utf-8')
file_handler.setLevel('INFO')

# 处理器添加到收集器上
logger.addHandler(handler)
logger.addHandler(file_handler)

# 设置格式
fmt =logging.Formatter('time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s--%(lineno)s')
handler.setFormatter(fmt)
file_handler.setFormatter(fmt)


logger.info('正常执行的逻辑')
logger.error('错误')
logger.debug('调试信息')
