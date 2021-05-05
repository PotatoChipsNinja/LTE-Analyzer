import pandas as pd
from sqlalchemy import create_engine
import time

# tbCell返回sectorId(1)/sectorName(2)/eNodeBId(3)/eNodeBName(4)/小区名称(5)/属性列表(6)/小区名(7)：需要类型和MySQL的引擎
def select_BasicData_From_tb(type):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ltedb')
    if type == 1:
        sql = "select SECTOR_ID from tbCell;"
        dfData = pd.read_sql_query(sql, engine)
    elif type == 2:
        sql = "select SECTOR_NAME from tbCell;"
        dfData = pd.read_sql_query(sql, engine)
    elif type == 3:
        sql = "select ENODEBID from tbCell;"
        dfData = pd.read_sql_query(sql, engine)
    elif type == 4:
        sql = "select ENODEB_NAME from tbCell;"
        dfData = pd.read_sql_query(sql, engine)
    elif type == 5:
        sql = "select 小区名称 from tbKPI;"
        dfData = pd.read_sql_query(sql, engine)
    elif type == 6:
        sql = "SELECT COLUMN_NAME  FROM information_schema.columns WHERE table_name='tbKPI';"
        dfData = pd.read_sql_query(sql, engine)
        for i in ['起始时间', '网元/基站名称', '小区', '小区名称']:
            del_index = dfData[dfData['COLUMN_NAME'] == i].index
            dfData = dfData.drop(del_index)
    elif type == 7:
        sql = "select 小区名称 from tbPRBnew;"
        dfData = pd.read_sql_query(sql, engine)
    return dfData.values.tolist()

#-------------------1-------------------
# 查询tbCell中小区信息：需要查询的sectorId以及MySQL的引擎
def select_SectorAllo_From_tbCell_SectorId(sectorId):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ltedb')
    sql = "select * from tbCell where SECTOR_ID = \'" + sectorId + "\';"
    dfData = pd.read_sql_query(sql, engine)
    # index = dfData.columns.tolist()
    # value = dfData.values.tolist()[0]
    # dataDict = dict(zip(index,value))
    dataDict = dfData.to_dict()
    return dataDict  # 返回dict（属性:值）


# 查询tbCell中小区信息：需要查询的sectorName以及MySQL的引擎
def select_SectorAllo_From_tbCell_SectorName(sectorName):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ltedb')
    sql = "select * from tbCell where SECTOR_NAME = \'" + sectorName + "\';"
    dfData = pd.read_sql_query(sql, engine)
    # index = dfData.columns.tolist()
    # value = dfData.values.tolist()[0]
    # dataDict = dict(zip(index,value))
    dataDict = dfData.to_dict()
    return dataDict  # 返回dict（属性:值）


#-------------------2-------------------
# 查询tbCell中小区信息：需要查询的eNodeBID以及MySQL的引擎
def select_SectorAllo_From_tbCell_eNodeBId(eNodeBId):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ltedb')
    sql = "select * from tbCell where ENODEBID = \'" + eNodeBId + "\';"
    dfData = pd.read_sql_query(sql, engine)
    # index = dfData.columns.tolist()
    # value = dfData.values.tolist()[0]
    # dataDict = dict(zip(index,value))
    dataDict = dfData.to_dict()
    return dataDict  # 返回dict（属性:值）


# 查询tbCell中小区信息：需要查询的eNodeBName以及MySQL的引擎
def select_SectorAllo_From_tbCell_eNodeBName(eNodeBName):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ltedb')
    sql = "select * from tbCell where ENODEB_NAME = \'" + eNodeBName + "\';"
    dfData = pd.read_sql_query(sql, engine)
    # index = dfData.columns.tolist()
    # value = dfData.values.tolist()[0]
    # dataDict = dict(zip(index,value))
    dataDict = dfData.to_dict()
    return dataDict  # 返回dict（属性:值）


#-------------------3-------------------
# 查询tbKPI中数据信息：需要查询的小区名称，数据，起始日期，终止日期以及MySQL的引擎
def select_Data_From_tbKPI_SectorName(sectorName, attribute, startDate, endDate):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ltedb')
    startDate = "2020-07-"+str(startDate)+" 00:00:00"
    endDate = "2020-07-"+str(endDate)+" 00:00:00"
    sql = "select " + attribute + " from tbKPI where 小区名称 = \'" + sectorName + "\' and 起始时间 between \'" + startDate + "\' and \'" + endDate + "\';"
    dfData = pd.read_sql_query(sql, engine)
    return dfData.values.tolist()

#-------------------4-------------------
# 查询tbPRBnew中数据信息：需要查询的小区名称，数据，起始日期，终止日期以及MySQL的引擎
def select_Data_From_tbPRBnew_SectorName(sectorName, attribute, startDate, endDate):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ltedb')
    attribute = "第"+str(attribute)+"个PRB上检测到的干扰噪声的平均值"
    startDate ="2020-07-"+startDate[0:2]+" "+startDate[3:5]+":00:00"
    endDate = "2020-07-"+endDate[0:2]+" "+endDate[3:5]+":00:00"
    sql = "select " + attribute + " from tbPRBnew where 小区名称 = \'" + sectorName + "\' and 起始时间 between \'" + startDate + "\' and \'" + endDate + "\';"
    dfData = pd.read_sql_query(sql, engine)
    return dfData.values.tolist()

# 查询tbPRB中数据信息：需要查询的小区名称，数据，起始日期，终止日期以及MySQL的引擎
def select_Data_From_tbPRB_SectorName(sectorName, attribute, startDate, endDate):
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ltedb')
    attribute = "第"+str(attribute)+"个PRB上检测到的干扰噪声的平均值"
    startDate ="2020-07-"+startDate[0:2]+" "+startDate[3:5]+":00:00"
    endDate = "2020-07-"+endDate[0:2]+" "+endDate[3:5]+":00:00"
    sql = "select " + attribute + " from tbPRB where 小区名称 = \'" + sectorName + "\' and 起始时间 between \'" + startDate + "\' and \'" + endDate + "\';"
    dfData = pd.read_sql_query(sql, engine)
    return dfData.values.tolist()

# 初始化数据库连接，使用pymysql模块
# MySQL的用户：root, 密码:123456, 端口：3306,数据库：ltedb

# print(select_Data_From_tbPRBnew_SectorName('B马高速入口-HLHF-2', 1, '17-00', '17-10', engine))
# print(select_BasicData_From_tb(1, engine))
# print(select_BasicData_From_tb(2, engine))
# print(select_BasicData_From_tb(3, engine))
# print(select_BasicData_From_tb(4, engine))
# print(select_BasicData_From_tb(5, engine))
# print(select_BasicData_From_tb(6, engine))
# print(select_BasicData_From_tb(7, engine))




# # 表名
# tableName = "tbCell"
# # 查询语句，选出employee表中的所有数据
# sql = "select * from tbCell where SECTOR_ID = sectorId;"
#
# # read_sql_query的两个参数: sql语句， 数据库连接
# df = pd.read_sql_query(sql, engine)
#
# # 输出employee表的查询结果
# # print(df)
#
# # 获取当前时间并格式化，目的是产生文件名唯一的文件
# nowTime = time.strftime("%Y_%m_%d-%H_%M_%S", time.localtime())
# # print(nowTime)
#
# # 输出到excel文件
# # df.to_excel(tableName+"-"+nowTime+".xlsx")
#
# # 输出到txt文件
# df.to_csv(tableName+"-"+nowTime+".txt", sep='|', index=False)



