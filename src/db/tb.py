import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine
import time
from src.db import var
import os
'''
    建表函数:table_create
    table:int           数据表，取值1-4,5,6,7分别表示 tbCell、tbKPI、tbPRB 和 tbMRO,tbPRBNEW,tbAdminUSER,tbOrdUSER;
'''


def table_create(table):
    # 若为建tbPRB，则需要同时建表tbPRBNEW
    if table == 3:
        table_create(5)
    # 索引为table
    table = table - 1
    # 表名
    tb_Name = var.table_Name[table]
    # 连接数据库
    conn = pymysql.connect(host='localhost',
                           user='root',
                           passwd='123456',
                           db='ltedb',
                           port=3306,
                           charset='utf8')
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    # 如果表已经存在，使用execute() 删除表
    cur.execute("drop table if EXISTS " + tb_Name)
    cur.execute("drop table if EXISTS " + tb_Name + "_tmp")
    # sql语句
    sql1 = "create table " + tb_Name + var.sql_create[table]
    sql2 = "create table " + tb_Name + "_tmp" + var.sql_create[table]
    try:
        # 执行sql语句并commit
        cur.execute(sql1)
        cur.execute(sql2)
        conn.commit()
        print("建表" + tb_Name + "成功")
    except Exception as err:
        # 出错时回滚（Rollback in case there is any error）
        print("建表" + tb_Name + "时出错 {}".format(str(err)))
        conn.rollback()
    # 断开连接
    conn.close()


'''
    建触发器函数:trigger_create
    table:int           数据表，取值1-4,5,6分别表示 tbCell、tbKPI、tbPRB 和 tbMRO,tbPRBNEW,tbUSER;
'''


def trigger_create(table):
    # 若为表tbPRB建触发器，则需要同时为tbPRBNEW建触发器
    if table == 3:
        trigger_create(5)
    # 索引为table
    table = table - 1
    # 表名
    tb_Name = var.table_Name[table]
    # 连接数据库
    conn = pymysql.connect(host='localhost',
                           user='root',
                           passwd='123456',
                           db='ltedb',
                           port=3306,
                           charset='utf8')
    # 使用cursor()方法创建光标
    cur = conn.cursor()
    # 如果已存在该触发器则删除
    cur.execute("drop trigger if EXISTS TR_IMPORT_" + tb_Name)
    # sql语句
    sql_tr = var.sql_trigger[table]

    try:
        # 执行sql语句并commit
        cur.execute(sql_tr)
        conn.commit()
        print("建触发器TR_IMPORT_" + tb_Name + "成功")
    except Exception as err:
        # 出错时回滚（Rollback in case there is any error）
        print("建触发器TR_IMPORT_" + tb_Name + "时出错 {}".format(str(err)))
        conn.rollback()
    # 断开连接
    conn.close()


'''
    数据导入函数:data_bulkinsert
    table:int           数据表，取值1-4分别表示 tbCell、tbKPI、tbPRB 和 tbMRO;
    df:dataframe        清洗和切片后的数据

数据清洗在flask完成，代码如下！！！！！！！！！！    
# 判断每条数据的各个属性值是否符合数据类型要求、取值是否在合法范围，剔除掉来自于数据文件的不符合要求的输入数据。
# 并在导入日志（txt 文件）中记录被剔除的数据在输入文件的位置、编号
ef = df[(df["AZIMUTH"] < 100)]
# print(ef.values) # dataframe转numpy数组
# print(ef.index.values[1]) # 输出dafaframe索引

# 输出不符合规范的数据信息
fo = open("Log_Import_" + tableName + "-" + nowTime + ".txt", "a")
fo.write("本次插入不合法的数据为:\n所在行\t\t内容\n")
for i in range(len(ef)):
    fo.write("第"+str(ef.index.values[i])+"行\t\t" + str(ef.values[i])+"\n")
fo.close()
# 数据清洗
df.drop(index=list(ef.index), inplace=True)
'''


def data_bulkinsert(table, df):
    # 索引为table
    table = table - 1
    # 表名
    tb_Name = var.table_Name[table]
    # 将导入的nan转换为None,nan不能再MySQL中使用
    df = df.where(df.notnull(), None)
    # 连接数据库
    conn = pymysql.connect(host='localhost',
                           user='root',
                           passwd='123456',
                           db='ltedb',
                           port=3306,
                           charset='utf8')
    # 使用cursor()方法创建光标
    cur = conn.cursor()

    # sql语句
    sql_ins = var.sql_insert[table]

    # 导入数据
    # args是一个包含多个元组的列表
    args = df.values.tolist()
    for i in range(len(args)):
        args[i] = tuple(args[i])
    # print(args)
    try:
        cur.executemany(sql_ins, args)
        print("执行MySQL插入语句成功")
        # 执行结束后清空临时关系表
        cur.execute("delete from " + tb_Name + "_tmp")
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql_ins, err))
    finally:
        cur.close()
        conn.commit()
        conn.close()


'''
    数据导出函数:data_export
    table:int           数据表，取值1-4,5分别表示 tbCell、tbKPI、tbPRB 和 tbMRO,tbPRBNEW;
    type:string         文件格式，取指为"xlsx"或"csv"
'''


def data_export(table, type):
    # 索引为table
    table = table - 1
    # 表名
    tb_Name = var.table_Name[table]

    # 初始化数据库连接，使用pymysql模块
    # MySQL的用户：root, 密码:123456, 端口：3306,数据库：ltedb
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ltedb')

    # 查询语句，选出employee表中的所有数据
    sql = "select * from " + tb_Name + ";"

    # read_sql_query的两个参数: sql语句， 数据库连接
    df = pd.read_sql_query(sql, engine)

    # 获取当前时间并格式化，目的是产生文件名唯一的文件
    nowTime = time.strftime("%Y_%m_%d-%H_%M_%S", time.localtime())
    path = "download/"
    if not os.path.exists(path):
        os.mkdir(path)

    if type == 'xlsx':
        # 输出到excel文件
        df.to_excel(path + tb_Name + "-" + nowTime + ".xlsx")
        return tb_Name + "-" + nowTime + ".xlsx"
    elif type == 'csv':
        # 输出到txt文件
        df.to_csv(path + tb_Name + "-" + nowTime + ".txt", sep='|', index=False)
        return tb_Name + "-" + nowTime + ".txt"
    else:
        print("输出时选择了错误的类型")


# for i in range(1, 7):
#     table_create(i)
#     trigger_create(i)
