# 导入信息放在模块的最上面
import logging

def get_logger(name="root",
               logger_level="DEBUG",
               straam_handler_level="DEBUG",
               file=None,
               flie_handler_level="INFO",
               fmt_str="time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s--%(lineno)s"
):
    # logger封装
    # 获取日志收集器logger
    logger =logging.getLogger(name)
    logger.setLevel(logger_level)

    #"time:%(asctime)s--%level_name)s--%(name)s:%(message)s--%(filename)s--%(lineno)s"
    fmt =logging.Formatter(fmt_str)

    #日志处理器
    handler = logging.StreamHandler()
    handler.setLevel(straam_handler_level)
    handler.setFormatter(fmt)
    logger.addHandler(handler)
    #文件处理器
    if file:
        file_handler = logging.FileHandler(file,encoding="utf-8")
        file_handler.setLevel(flie_handler_level)
        file_handler.setFormatter(fmt)
        logger.addHandler(file_handler)
    return logger


if __name__ =="__main__":
    logger = get_logger(file="python36.log")
    logger.warning("可以退下了")


