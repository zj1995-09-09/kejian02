# 导入信息放在模块的最上面
import logging


def get_logger(name='root',
               logger_level='DEBUG',
               stream_handler_level='DEBUG',
               file=None,
               file_handler_level='INFO',
               fmt_str="time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s---%(lineno)s"
               ):
    """logger封装"""

    # 获取日志收集器 logger
    logger = logging.getLogger(name)
    logger.setLevel(logger_level)
    # "time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s---%(lineno)s"
    fmt = logging.Formatter(fmt_str)
    # 日志处理器
    handler = logging.StreamHandler()
    handler.setLevel(stream_handler_level)
    logger.addHandler(handler)
    handler.setFormatter(fmt)
    # 文件处理器
    if file:
        file_handler = logging.FileHandler(file, encoding="utf-8")
        file_handler.setLevel(file_handler_level)
        logger.addHandler(file_handler)
        file_handler.setFormatter(fmt)
    return logger


if __name__ == '__main__':
    logger = get_logger(file="python36.log")
    # 不要调用两次 get_logger()
    logger.info("没事退下吧")