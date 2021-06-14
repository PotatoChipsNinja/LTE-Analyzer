import pandas as pd
from sqlalchemy import create_engine
from scipy.stats import norm
import var
import tb
from pandas.core.frame import DataFrame
from collections import defaultdict

# 从tbc2inew中选取符合要求的ServingSector, InterferingSector
def select_triplet_from_tbc2inew(xValue):
    engine = create_engine(var.engine_creation)
    sql = "select ServingSector, InterferingSector from tbc2inew where PrbABS6 >= " + str(xValue)
    dfData = pd.read_sql_query(sql, engine)

    dict_sectors = defaultdict(set)
    for i, j in zip(dfData['ServingSector'].tolist(), dfData['InterferingSector'].tolist()):
        dict_sectors[i].add(j)
        dict_sectors[j].add(i)

    set_allTriplet = set()
    set_temp = set()
    for i in dict_sectors.keys():
        for j in dict_sectors[i]:
            for k in (dict_sectors[j].intersection(dict_sectors[i]) - set_temp):
                set_allTriplet.add(tuple(sorted([i, j, k])))
        set_temp.add(i)

    dfData = DataFrame(list(set_allTriplet), columns={0: 'a小区ID', 1: 'b小区ID', 2: 'c小区ID'})
    return dfData


# 测试：
#           "with temp(TimeStamp, ServingSector, InterferingSector, LteScRSRP, LteNcRSRP, Difference, Nine, Six) as " \
#           "(select TimeStamp, ServingSector, InterferingSector, LteScRSRP, LteNcRSRP, (LteScRSRP-LteNcRSRP) as Difference, " \
#           "IF(LteScRSRP-LteNcRSRP< 9, 1, 0) as Nine, IF(ABS(LteScRSRP-LteNcRSRP) < 6, 1, 0) as Six from tbmro), "\
#           "Ans(ServingSector, InterferingSector, cnt, mean, std, PrbC2I9, PrbABS6, cntNine, cntSix)" \
#           "as (select ServingSector, InterferingSector, count(*) as cnt, AVG(LteScRSRP-LteNcRSRP) as mean, " \
#           "STDDEV(LteScRSRP-LteNcRSRP) as std, SUM(Nine)/count(*) as PrbC2I9, SUM(Six)/count(*) as PrbABS6, " \
#           "SUM(Nine) as cntNine, SUM(Six) as cntSix "\
#           "from temp group by ServingSector, InterferingSector having count(*) > "+str(num)+")" \
#           "select ServingSector, InterferingSector, mean, std, PrbC2I9, PrbABS6 from Ans"

a = select_triplet_from_tbc2inew(0.002)


print(a)

# print(a['ServingSector'].tolist())
