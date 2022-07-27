import logging


def get_logger(name='root',
               logger_level='DEBUG',
               stream_handler_level='DEBUG',
               file=None,
               file_handler_levl='INFO',
               fmt_str="time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s--%(lineno)s"
               ):
    logger = logging.getLogger(name)
    logger.setLevel(logger_level)
    fmt = logging.Formatter(fmt_str)

    # 日志处理器
    handler = logging.StreamHandler()
    handler.setLevel(stream_handler_level)
    handler.setFormatter(fmt)
    logger.addHandler(handler)

    if file:
        file_handler = logging.FileHandler(file, encoding='utf-8')
        file_handler.setLevel(file_handler_levl)
        file_handler.setFormatter(fmt)
        logger.addHandler(file_handler)

    return logger


if __name__ == '__main__':
    logger = get_logger(file='python36.log')
    logger.info('没事退下吧')

print(__file__)
print(__name__)
