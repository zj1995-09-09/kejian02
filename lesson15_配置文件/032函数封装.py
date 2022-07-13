# 导入信息放在模块的最上面
import logging


def get_logger(name='root',
               logger_level='DEBUG',
               stream_hanlder_level='DEBUG',
               file=None,
               file_handler_level='INFO',
               fmt_str="time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s--%(lineno)s"
               ):
    '''logger封装'''

    # 获取日志收集器 logger
    logger = logging.getLogger(name)
    logger.setLevel(logger_level)
    # "time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s--%(lineno)s"
    fmt = logging.Formatter(fmt_str)
    # 日志处理器handler
    handler =logging.StreamHandler()
    handler.setLevel(stream_hanlder_level)
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    # 文件处理器file_handler
    if file:
        file_handler =logging.FileHandler(file,encoding="utf-8")
        file_handler.setLevel(file_handler_level)
        file_handler.setFormatter(fmt)
        logger.addHandler(file_handler)
    return logger


if __name__ == "__main__":
    logger = get_logger(file="python36.log")
    logger.warning("6点到了 快去吃饭吧")