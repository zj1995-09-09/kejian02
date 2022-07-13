#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# email: wagyu2016@163.com
# wechat: shoubian01
# author: 王雨泽
import pymysql
from pymysql.cursors import DictCursor


class MysqlHandler():
    def __init__(
            self,
            host="8.129.91.152",
            port=3306,
            user="future",
            password="123456",
            charset='utf8',
            cursorclass=DictCursor
    ):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset=charset,
            cursorclass=cursorclass
        )
        self.cursor = self.conn.cursor()

    def query(self, sql, one=True):
        self.cursor.execute(sql)
        if one:
            return self.cursor.fetchone()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    db = MysqlHandler(
        # host="8.129.91.152",
        # port=3306,
        # user="future",
        # password="123456",
        # charset='utf8',
        # cursorclass=DictCursor
    )

    data = db.query("SELECT * FROM futureloan.member LIMIT 10;")
    print(data)