import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
import time
'''
    获取数据库信息函数:
    无参数
    用于返回数据库信息   
'''


def db_get_inf():
    return {
        "host": "127.0.0.1",
        "port": 3306,
        "db": "ltdb",
        "username": "root",
        "password": "123456",
        "interactiveTimeout": 0,  # TODO
        "waitTimeout": 0,         # TODO
        "partition": "",          # TODO  
        "queryCacheSize": ""      # TODO
    }


'''
    修改数据库连接函数:
    interactiveTimeout: int 交互式连接超时时间，对应数据库的 interactive_timeout 参数，单位：秒
    waitTimeout: int 非交互式连接超时时间，对应数据库的 wait_timeout 参数，单位：秒
    返回值:bool 是否成功
'''


def db_change_timeout(interactiveTimeout, waitTimeout):
    # 连接数据库
    conn = pymysql.connect(host='localhost',
                           user='root',
                           passwd='123456',
                           db='ltedb',
                           port=3306,
                           charset='utf8')
    # 修改超时时间
    conn.query('SET GLOBAL interactive_timeout=' + str(interactiveTimeout))
    conn.query('SET GLOBAL wait_timeout=' + str(waitTimeout))
    # 提交并关闭连接
    conn.commit()
    conn.close()
    return True


'''
    修改数据库缓冲区大小函数:
    queryCacheSize: string 数据库缓冲区大小，对应数据库的 query_cache_size 参数
    返回值:bool 是否成功
'''


def db_change_cache_size(queryCacheSize):
    # 连接数据库
    # conn = pymysql.connect(host='localhost',
    #                        user='root',
    #                        passwd='123456',
    #                        db='ltedb',
    #                        port=3306,
    #                        charset='utf8')
    # conn.query('SET GLOBAL have_query_cache="YES"')
    # conn.query('SET GLOBAL query_cache_size=' + queryCacheSize)
    # 提交并关闭连接
    # conn.commit()
    # conn.close()
    return True


# db_change_timeout(28800,28800)
db_change_cache_size("10M")


# Traceback (most recent call last):
#   File "C:\Users\sh1487561\Desktop\TLE-Analyzer\app.py", line 5, in <module>
#     from src.api.admin import admin
#   File "C:\Users\sh1487561\Desktop\TLE-Analyzer\src\api\admin.py", line 3, in <module>
#     from src.db.common import *
#   File "C:\Users\sh1487561\Desktop\TLE-Analyzer\src\db\common.py", line 77, in <module>
#     db_change_cache_size("10M")
#   File "C:\Users\sh1487561\Desktop\TLE-Analyzer\src\db\common.py", line 68, in db_change_cache_size
#     conn.query('SET GLOBAL have_query_cache="YES"')
#   File "C:\Python39\lib\site-packages\pymysql\connections.py", line 548, in query
#     self._affected_rows = self._read_query_result(unbuffered=unbuffered)
#   File "C:\Python39\lib\site-packages\pymysql\connections.py", line 775, in _read_query_result
#     result.read()
#   File "C:\Python39\lib\site-packages\pymysql\connections.py", line 1156, in read
#     first_packet = self.connection._read_packet()
#   File "C:\Python39\lib\site-packages\pymysql\connections.py", line 725, in _read_packet
#     packet.raise_for_error()
#   File "C:\Python39\lib\site-packages\pymysql\protocol.py", line 221, in raise_for_error
#     err.raise_mysql_exception(self._data)
#   File "C:\Python39\lib\site-packages\pymysql\err.py", line 143, in raise_mysql_exception
#     raise errorclass(errno, errval)
# pymysql.err.OperationalError: (1238, "Variable 'have_query_cache' is a read only variable")
