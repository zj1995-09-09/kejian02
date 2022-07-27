# 导入信息放在模块的最上面
import logging


class MyLogger(logging.Logger):

    def __init__(self,
                 name='root',
                 logger_level='DEBUG',
                 stream_handler_level='DEBUG',
                 file=None,
                 file_handler_level='INFO',
                 fmt_str='time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s--%(lineno)s'
                 ):

    # 获取日志收集器
    logger
    super().__init__(name, logger_level)
    # self == 收集器
    # self.setLevel(logger_level)

    fmt = logging.Formatter(fmt_str)

    # 日志处理器
    handler =logging.Str