'''
测试注册功能
自动化测试用例
用例函数以test_
'''

import requests
import pytest
from common.logger_handler import logger
from common.excel_handler import ExcelHandler

import os
from config import path

# log_file = os.path.join(path.logs_path,'py36.log')
# logger = get_logger(file = log_file)

获取excel文件的路径
excel_file = os.path.json(path.data_path, 'py36.log')


@pytest.mark.parametrize('test_info', data)
def test_register_01(test_info):
    '''注册用例'''
    # 准备测试数据
    # actual_url = 'http://api.lemonban.com/futureloan/member/register'
    # actual_method ='post'
    # actual_json ={'mobile_phone':'','pwd':''}
    # actual_headers={"X-Lemonban-Media-Type":"lemonban.v2"}
    # expected = 2

    actual_url = test_info['url']
    actual_method = test_info['method']
    actual_json = test_info['json']
    actual_headers = test_info['headers']
    expected = test_info['expected']

    resp = requests.request(method=actual_method,
                            url=actual_url,
                            headers=eval(actual_headers),
                            json=eval(actual_json)
    )
    获取响应体：json
    resp_body = resp.json()

    try:
        assert resp_body['codee'] == expected
    except AssertionError as  e:
        logger.error("用例失败:{}".format(e))
        raise e
