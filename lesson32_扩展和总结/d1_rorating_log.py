
import logging
import time
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

# logger = logging.getLogger("python36")
#
# # 初始化handler
# handler = RotatingFileHandler('py36.log',
#                              maxBytes=100,
#                              backupCount=3,
#                                 encoding='utf-8')
# logger.addHandler(handler)
#
# # 打印日志
# for i in range(100):
#     logger.warning("生成警告信息{}".format(time.time()))
#     time.sleep(0.1)


# 根据时间生成新文件
logger = logging.getLogger('python36')
handler = TimedRotatingFileHandler('timepy36.log',
                                   when='s',
                                   interval=2,
                                   backupCount=100,
                                   encoding='utf-8')

logger.addHandler(handler)

for i in range(10):
    logger.warning("生成警告信息{}".format(time.time()))
    time.sleep(0.3)

