class Logger:
    def __init__(self,name):
        print ("正在初始化收集器")
        self.name =name
    def info(self,a):
        print ("正在上课0711")



class MyLogger(Logger):
    def __init__(self,name,fmt,level):
        super().__init__(name)

        self.fmt = fmt
        self.level = level

log = MyLogger("HHH","NOSET","fow")
log.info("hello")