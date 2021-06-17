import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
import time

from src.db import var
'''
    用户登录函数:用户发出注册请求时使用
    参数:
        userName: string 用户名
        passWord: password 密码
        idType: int 身份类型 ，值为1代表"admin",2代表"ordinary"
    返回值：boolean，成功返回True,不成功返回False
'''


def user_signin(userName, passWord, idType):
    # 根据用户类型确定用户表
    if idType == 1:
        tb_Name = "tbAdminUSER"
    elif idType == 2:
        tb_Name = "tbOrdUSER"
    # 初始化数据库连接，使用pymysql模块
    # MySQL的用户：root, 密码:123456, 端口：3306,数据库：ltedb
    engine = create_engine(var.engine_creation)
    sql = "select count(userName) from " + tb_Name + " where userName = \'" + userName + "\' and passWord = \'" + passWord + "\';"
    # print(sql)
    count = pd.read_sql_query(sql, engine)
    cnt = int(count.values)
    if cnt == 0:
        #print("用户名或密码错误，登录失败")
        return False
    else:
        #print("登录成功")
        return True


'''
    新增用户函数:用户发出注册请求或更改密码时使用
	参数:
    userName: string 用户名
    	passWord: string 密码
    	idType: int 身份类型 ，值为1代表"admin",2代表"ordinary"
'''


def user_add(userName, passWord, idType):
    # 根据用户类型确定用户表
    if idType == 1:
        tb_Name = "tbAdminUSER"
    elif idType == 2:
        tb_Name = "tbOrdUSER"
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()

    # 获取当前时间并格式化，的到regTime
    regTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    regTime = pd.to_datetime(regTime)
    # sql语句
    sql = "insert into " + tb_Name + "_tmp(userName,passWord,regTime) values(%s,%s,%s);"
    arg = (userName, passWord, regTime)
    try:
        cur.execute(sql, arg)
        if idType == 1:
            print("新增管理员用户" + userName + "成功")
        elif idType == 2:
            print("新增普通用户" + userName + "成功")
        # 执行结束后清空临时关系表
        cur.execute("delete from " + tb_Name + "_tmp")
        flag = True
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql, err))
        flag = False
    finally:
        cur.close()
        conn.commit()
        conn.close()

    return flag


'''
    删除用户函数:删除用户时使用
    参数:
        userName: string 用户名,确保用户名存在，用户名不存在对数据库无影响，也不报错
        idType: int 身份类型 ，值为1代表"admin",2代表"ordinary"
'''


def user_delete(userName, idType):
    # 根据用户类型确定用户表
    if idType == 1:
        tb_Name = "tbAdminUSER"
    elif idType == 2:
        tb_Name = "tbOrdUSER"
    # 连接数据库
    conn = var.pymysql_connect()
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    # sql语句
    sql = "delete from " + tb_Name + " where userName=" + "\'" + userName + "\';"
    try:
        cur.execute(sql)
        if idType == 1:
            print("删除管理员用户" + userName + "成功")
        elif idType == 2:
            print("删除普通用户" + userName + "成功")
        flag = True
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql, err))
        flag = False
    finally:
        cur.close()
        conn.commit()
        conn.close()

    return flag


'''
    修改用户密码函数:修改用户密码
    参数:
        userName: string 用户名,确保用户名存在，用户名不存在对数据库无影响，也不报错
        oldPsaawd: string 旧密码
        newPasswd: string 新密码
        idType: int 身份类型 ，值为1代表"admin",2代表"ordinary"
'''


def user_change_passwd(userName, oldPsaawd, newPasswd, idType):
    if user_signin(userName, oldPsaawd, idType):
        # 根据用户类型确定用户表
        if idType == 1:
            tb_Name = "tbAdminUSER"
        elif idType == 2:
            tb_Name = "tbOrdUSER"
        # 连接数据库
        conn = var.pymysql_connect()
        # 使用cursor()方法创建光标
        cur = conn.cursor()
        # sql语句
        sql = "update " + tb_Name + " set passWord=\'" + newPasswd + '\''
        sql = sql + " where userName=\'" + userName + "\';"
        try:
            cur.execute(sql)
            print("用户" + userName + "密码修改成功")
        except Exception as err:
            print("执行MySQL: %s 时出错: \n%s" % (sql, err))
        finally:
            cur.close()
            conn.commit()
            conn.close()
        return True
    else:
        print("用户名或密码错误，修改密码失败")
        return False


'''
    获取用户列表函数:获取用户列表时使用
    参数:
        idType: int 身份类型 ，值为1代表"admin",2代表"ordinary"
'''


def user_get_list(idType):
    # 根据用户类型确定用户表
    if idType == 1:
        tb_Name = "tbAdminUSER"
    elif idType == 2:
        tb_Name = "tbOrdUSER"
    # 初始化数据库连接，使用pymysql模块
    # MySQL的用户：root, 密码:123456, 端口：3306,数据库：ltedb
    engine = create_engine(var.engine_creation)
    sql = "select userName,regTime from " + tb_Name + ";"
    # print(sql)
    result = pd.read_sql_query(sql, engine)
    # print(result.values.tolist())
    return result.values.tolist()


if __name__ == "__main__":
    user_add("admin", "admin", 1)
# user_add("shiyuhui","123456",1)
# user_add("zhangxinyang","654321",1)
# user_signin("shiyuhui","123456",1)
# user_signin("shiyuhui","123",1)
# user_signin("shiyuhui","123456",2)
# user_change_passwd("shiyuhui","@@@@123","123456",1)
# print(user_get_list(1))
