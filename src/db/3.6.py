import pandas as pd
from sqlalchemy import create_engine
import pymysql
import tb
import var

# 从tbmro中求每对主邻小区均值、标准差、PrbC2I9、PrbABS6，需要最少数据量
def select_SSectorandISectorInfo_from_tbmro(num):
    tb.table_create(8)
    tb.trigger_create(8)
    tb_Name = var.table_Name[7]
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
    # sql = "with Ans(ServingSector, InterferingSector, cnt, mean, std, PrbC2I9, PrbABS6) " \
    #       "as (select ServingSector, InterferingSector, count(*) as cnt, AVG(LteScRSRP-LteNcRSRP) as mean, " \
    #       "STDDEV(LteScRSRP-LteNcRSRP) as std, SUM(IF(LteScRSRP-LteNcRSRP< 9, 1, 0))/count(*) as PrbC2I9, " \
    #       "SUM(IF(ABS(LteScRSRP-LteNcRSRP) < 6, 1, 0))/count(*) as PrbABS6 " \
    #       "from tbmro group by ServingSector, InterferingSector having count(*) > " + str(num) + ") " \
    #       "select ServingSector, InterferingSector,count(*) as cnt from Ans group by ServingSector, InterferingSector having cnt > 1 "
    sql = "with Ans(ServingSector, InterferingSector, cnt, mean, std, PrbC2I9, PrbABS6) " \
          "as (select ServingSector, InterferingSector, count(*) as cnt, AVG(LteScRSRP-LteNcRSRP) as mean, " \
          "STDDEV(LteScRSRP-LteNcRSRP) as std, SUM(IF(LteScRSRP-LteNcRSRP< 9, 1, 0))/count(*) as PrbC2I9, " \
          "SUM(IF(ABS(LteScRSRP-LteNcRSRP) < 6, 1, 0))/count(*) as PrbABS6 " \
          "from tbmro group by ServingSector, InterferingSector having count(*) > " + str(num) + ") " \
          "select ServingSector, InterferingSector, mean, std, PrbC2I9, PrbABS6 from Ans "
    sql_ins = var.sql_insert[5] + sql + "on duplicate key update\nmean=values(mean),\nstd=values(std),\nPrbC2I9=values(PrbC2I9),\nPrbABS6=values(PrbABS6)"

    cur.execute(sql_ins)
    try:
        cur.execute(sql_ins)
        print("执行MySQL插入语句成功")
        # 执行结束后清空临时关系表
        cur.execute("delete from " + tb_Name + "_tmp")
    except Exception as err:
        print("执行MySQL: %s 时出错: \n%s" % (sql_ins, err))
    finally:
        cur.execute("delete from " + tb_Name + "_tmp")
        cur.close()
        conn.commit()
        conn.close()

#测试：
#           "with temp(TimeStamp, ServingSector, InterferingSector, LteScRSRP, LteNcRSRP, Difference, Nine, Six) as " \
#           "(select TimeStamp, ServingSector, InterferingSector, LteScRSRP, LteNcRSRP, (LteScRSRP-LteNcRSRP) as Difference, " \
#           "IF(LteScRSRP-LteNcRSRP< 9, 1, 0) as Nine, IF(ABS(LteScRSRP-LteNcRSRP) < 6, 1, 0) as Six from tbmro), "\
#           "Ans(ServingSector, InterferingSector, cnt, mean, std, PrbC2I9, PrbABS6, cntNine, cntSix)" \
#           "as (select ServingSector, InterferingSector, count(*) as cnt, AVG(LteScRSRP-LteNcRSRP) as mean, " \
#           "STDDEV(LteScRSRP-LteNcRSRP) as std, SUM(Nine)/count(*) as PrbC2I9, SUM(Six)/count(*) as PrbABS6, " \
#           "SUM(Nine) as cntNine, SUM(Six) as cntSix "\
#           "from temp group by ServingSector, InterferingSector having count(*) > "+str(num)+")" \
#           "select ServingSector, InterferingSector, mean, std, PrbC2I9, PrbABS6 from Ans"


select_SSectorandISectorInfo_from_tbmro(1000)
# print(a['ServingSector'])
# print(a['InterferingSector'])
# print(a['mean'])
# print(a['std'])
# print(a['PrbC2I9'])
# print(a['PrbABS6'])
# tb.trigger_create(8)
