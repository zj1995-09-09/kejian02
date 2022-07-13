# def run(func):
#     print("hello")
#     return func
#
#
# ret = run(max)
# print(ret)
#
# print(max(3,4,5))
# print(ret(3,4,5))
import time




# 装饰器
def log_time(func):

    def wrapper():
        print(time.time())
        func()
        return

    return wrapper


# @log_time()
def run():
    print("正在运行")

# print(log_time(run)())

run()
# @classmethod
# @pytest.mark
# @pytest.fixture

# python基础
# selenium 的库