import os
import re
from faker import Faker
from pymysql.cursors import DictCursor
from common.yaml_handler import read_yaml
from common.logger_handler import get_logger
from common.excel_handler import ExcelHandler
from common.db_handler import DBHandler
from config import path


# class MidDBHanlder(DBHandler):
#     def __init__(self,
#                  host=user_config['db']['host'],
#                  port=user_config['db']['port'],
#                  user=user_config['db']['user'],
#                  password=user_config['db']['password'],
#                  # 不要写成utf-8
#                  charset=user_config['db']['charset'],
#                  # 指定数据库
#                  database=user_config['db']['database'],
#                  cursorclass=DictCursor
#                  ):
#         super.__init__(host=host,
#                        port=port,
#                        user=user,
#                        password=password,
#                        charset=charset,
#                        database=database,
#                        cursorclass=cursorclass)

class MidDBHandler(DBHandler):
    def __init__(self):
        yaml_path = os.path.join(path.config_path, 'config.yaml')
        yaml_config = read_yaml(yaml_path)
        user_path = os.path.join(path.config_path, 'security.yaml')
        user_config = read_yaml(user_path)

        super().__init__(host=user_config['db']['host'],
                         port=user_config['db']['port'],
                         user=user_config['db']['user'],
                         password=user_config['db']['password'],
                         # 不要写成utf-8
                         charset=user_config['db']['charset'],
                         # 指定数据库
                         database=user_config['db']['database'],
                         cursorclass=DictCursor)



class YZHandler():
    """任务：中间层。 common 和 调用层。
    使用项目的配置数据，填充common模块
    """
    # 替换数据
    # 新手机号码
    new_phone = ''
    investor_user_id = ''
    investor_user_token = ''
    admin_user_id = ''
    admin_user_token = ''
    loan_user_id = ''
    loan_user_token = ''


    yaml_path = os.path.join(path.config_path, 'config.yaml')
    yaml_config = read_yaml(yaml_path)

    user_path = os.path.join(path.config_path, 'security.yaml')
    user_config = read_yaml(user_path)

    # logger
    logger_file = os.path.join(path.logs_path, yaml_config['logger']['file'])
    logger = get_logger(name=yaml_config['logger']['name'],
                        file=logger_file)

    # excel对象
    excel_file = os.path.join(path.data_path, 'cases.xlsx')
    excel = ExcelHandler(excel_file)

    # 辅助函数
    # help_funcs = helper

    # 数据库
    db_class = MidDBHandler

    # 需要动态替换#...# 的数据
    investor_phone = user_config['investor_user']['phone']
    investor_pwd = user_config['investor_user']['pwd']
    loan_phone = user_config['loan_user']['phone']
    loan_pwd = user_config['loan_user']['pwd']
    admin_phone = user_config['admin_user']['phone']
    admin_pwd = user_config['admin_user']['pwd']


    @classmethod
    def replace_data(cls, string, pattern='#(.*?)#'):
        """数据动态替换"""
        # pattern = '#(.*?)#'
        results = re.finditer(pattern=pattern, string=string)
        for result in results:
            # old= '#investor_phone#'
            old = result.group()
            # key = 'investor_phone'
            key = result.group(1)
            new = str(getattr(cls, key, ''))
            string = string.replace(old, new)
        return string


    @classmethod
    def generate_new_phone(cls):
        """自动生成手机号"""
        fk = Faker(locale='zh_CN')
        while True:
            phone = fk.phone_number()
            db = MidDBHandler()
            phone_in_db = db.query('SELECT * FROM member WHERE mobile_phone = {}'.format(phone))
            db.close()
            if not phone_in_db:
                cls.new_phone = phone
                return phone

    # db = DBHandler(host='8.129.91.152',
    #              port=3306,
    #              user='future',
    #              password='123456',
    #              # 不要写成utf-8
    #              charset='utf8',
    #              # 指定数据库
    #              database='futureloan',
    #              cursorclass=DictCursor)


# def generate_new_phone():
#     """自动生成手机号"""
#     fk = Faker(locale='zh_CN')
#     while True:
#         phone = fk.phone_number()
#         db = MidDBHandler()
#         phone_in_db = db.query('SELECT * FROM member WHERE mobile_phone = {}'.format(phone))
#         db.close()
#         if not phone_in_db:
#             return phone


db = MidDBHandler()

if __name__ == '__main__':
    string = '{"mobile_phone": "#investor_phone#", "pwd": "#investor_pwd#", "mobile_phone": "#loan_phone#", "pwd": "#loan_pwd#", "mobile_phone": "#admin_phone#", "pwd": "#admin_pwd#"}'
    a = YZHandler.replace_data(string)
    print(a)

