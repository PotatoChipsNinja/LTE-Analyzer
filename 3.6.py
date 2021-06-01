import pandas as pd
from sqlalchemy import create_engine

# 从tbmro中求每对主邻小区均值、标准差、PrbC2I9、PrbABS6，需要最少数据量
def select_SSectorandISectorInfo_from_tbmro(num):
    engine = create_engine('mysql+pymysql://root:zhangjie1212@@@localhost:3306/ltedb')
    sql = "with Ans(ServingSector, InterferingSector, cnt, mean, std, PrbC2I9, PrbABS6) " \
          "as (select ServingSector, InterferingSector, count(*) as cnt, AVG(LteScRSRP-LteNcRSRP) as mean, " \
          "STDDEV(LteScRSRP-LteNcRSRP) as std, SUM(IF(LteScRSRP-LteNcRSRP< 9, 1, 0))/count(*) as PrbC2I9, " \
          "SUM(IF(ABS(LteScRSRP-LteNcRSRP) < 6, 1, 0))/count(*) as PrbABS6 " \
          "from tbmro group by ServingSector, InterferingSector having count(*) > "+str(num)+") " \
          "select ServingSector, InterferingSector, mean, std, PrbC2I9, PrbABS6 from Ans"
    dfData = pd.read_sql_query(sql, engine)
    dataDict = dfData.to_dict()
    return dataDict  # 返回dict（属性:值）

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
print(a['ServingSector'])
print(a['InterferingSector'])
print(a['mean'])
print(a['std'])
print(a['PrbC2I9'])
print(a['PrbABS6'])

