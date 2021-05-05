import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
from win32com.client import Dispatch
import time
'''
    获取数据库信息函数:
    无参数
    用于返回数据库信息   
'''


def db_get_inf():
    return


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
    conn = pymysql.connect(host='localhost',
                           user='root',
                           passwd='123456',
                           db='ltedb',
                           port=3306,
                           charset='utf8')
    # 修改超时时间
    conn.query('SET GLOBAL have_query_cache="YES"')
    conn.query('SET GLOBAL query_cache_size=' + queryCacheSize)
    # 提交并关闭连接
    conn.commit()
    conn.close()
    return True


# db_change_timeout(28800,28800)
db_change_cache_size("10M")