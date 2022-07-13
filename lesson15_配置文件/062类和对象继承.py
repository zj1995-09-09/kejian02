class Logger:
    def __int__(self):
        print("正在初始化收集器")

        self.name = name

    def info(self, msg):
        print("正在记录：今天周二来自习")


class MyLogger(Logger):
    def __init__(self, name, fmt, level):
        super().__init__()

        self.fmt = fmt
        self.level = level


log = MyLogger("hello", 'debug', "fow")
log.info(1111)
