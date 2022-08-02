class logger:
    def __init__(self, name):
        print('正在初始化收集器')
        self.name = name

    def info(self, msg):
        print('正在记录'+ str(msg))


class MyLogger(logger):
    def __init__(self, name, fmt, level):
        super().__init__(name)

        self.fmt =fmt
        self.level =level

log = MyLogger('hello','debug','fow')
log.info(15)
