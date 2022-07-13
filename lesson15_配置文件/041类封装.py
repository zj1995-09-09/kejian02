# 导入信息放在模块的最上面
import logging


class MyLogger(logging.Logger):

    def __init__(self,
                 name="zhoujian",
                 logger_level="DEBUG",
                 stream_handler_level="DEBUG",
                 file=None,
                 file_handler_level="INFO",
                 fmt_str="time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s--%(lineno)s"
                 ):
        # 获取日志收集器logger
        super().__init__(name, logger_level)
        # self == 收集器
        # self.setLevel(logger_level)

        # "time:%(asctime)s--%(levelname)s:%(name)s:%(message)s--%(filename)s--%(linno)s"
        fmt = logging.Formatter(fmt_str)
        handler = logging.StreamHandler()
        handler.setLevel(stream_handler_level)
        handler.setFormatter(fmt)
        self.addHandler(handler)
        # 文件处理器
        if file:
            file_handler = logging.FileHandler(file, encoding="utf-8")
            file_handler.setLevel(file_handler_level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)


if __name__ == "__main__":
    pass
