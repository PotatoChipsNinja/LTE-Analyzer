import pandas as pd
from sqlalchemy import create_engine
from scipy.stats import norm
import var
import tb

# 从tbmro中求每对主邻小区均值、标准差、PrbC2I9、PrbABS6，需要最少数据量
def select_SSectorandISectorInfo_from_tbmro(num):
    engine = create_engine(var.engine_creation)
    sql = "with Ans(ServingSector, InterferingSector, cnt, mean, std) " \
          "as (select ServingSector, InterferingSector, count(*) as cnt, AVG(LteScRSRP-LteNcRSRP) as mean, " \
          "STDDEV(LteScRSRP-LteNcRSRP) as std "\
          "from tbmro group by ServingSector, InterferingSector having count(*) > "+str(num)+") " \
          "select ServingSector, InterferingSector, mean, std from Ans"
    dfData = pd.read_sql_query(sql, engine)
    dfData['PrbC2I9'] = norm.cdf(9, loc=dfData['mean'], scale=dfData['std'])
    dfData['PrbABS6'] = norm.cdf(6, loc=dfData['mean'], scale=dfData['std']) - norm.cdf(-6, loc=dfData['mean'], scale=dfData['std'])
    return dfData

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


# 选取tbC2INEW中所有数据，供前端展示
def select_all_from_tbC2inew():
    engine = create_engine(var.engine_creation)
    sql = "select * from tbc2inew"
    dfData = pd.read_sql_query(sql, engine)
    return dfData


# tb.table_create(8)
# tb.trigger_create(8)
a = select_SSectorandISectorInfo_from_tbmro(000)
print(a)
tb.data_bulkinsert(8, a)


