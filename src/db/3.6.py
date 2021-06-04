import pandas as pd
from sqlalchemy import create_engine
import tb

# 从tbmro中求每对主邻小区均值、标准差、PrbC2I9、PrbABS6，需要最少数据量
def select_SSectorandISectorInfo_from_tbmro(num):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ltedb')
    # sql语句
    sql = "with Ans(ServingSector, InterferingSector, cnt, mean, std, PrbC2I9, PrbABS6) " \
          "as (select ServingSector, InterferingSector, count(*) as cnt, AVG(LteScRSRP-LteNcRSRP) as mean, " \
          "STDDEV(LteScRSRP-LteNcRSRP) as std, SUM(IF(LteScRSRP-LteNcRSRP< 9, 1, 0))/count(*) as PrbC2I9, " \
          "SUM(IF(ABS(LteScRSRP-LteNcRSRP) < 6, 1, 0))/count(*) as PrbABS6 " \
          "from tbmro group by ServingSector, InterferingSector having count(*) > " + str(num) + ") " \
          "select ServingSector, InterferingSector, mean, std, PrbC2I9, PrbABS6 from Ans "
          # "select * from Ans where ServingSector=\'5641-129\' and InterferingSector=\'15513-128\'"
          # "select ServingSector, InterferingSector,count(*) as cnt from Ans group by ServingSector, InterferingSector having cnt > 1 "
    dfData = pd.read_sql_query(sql, engine)
    return dfData  # 返回dict（属性:值）

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


a = select_SSectorandISectorInfo_from_tbmro(1000)
print(a)
tb.data_bulkinsert(8, a)


