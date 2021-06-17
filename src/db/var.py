import pymysql


def pymysql_connect():
    con = pymysql.connect(host='localhost',
                          user='root',
                          passwd='zhangjie1212@@',
                          db='ltedb',
                          port=3306,
                          charset='utf8')
    return con


engine_creation = 'mysql+pymysql://root:zhangjie1212@@@localhost:3306/ltedb'
table_Name = [
    "tbcell", "tbKPI", "tbPRB", "tbMRO", "tbPRBNEW", "tbAdminUSER", "tbOrdUSER", "tbC2INEW", "tbC2I3"
]
sql_create = [
        """ 
        (   
            CITY            VARCHAR (30) NULL,
            SECTOR_ID       VARCHAR (30) NOT NULL,
            SECTOR_NAME     VARCHAR (30) UNIQUE KEY,
            ENODEBID        INT NOT NULL,
            ENODEB_NAME     VARCHAR (30) NOT NULL,
            EARFCN          INT NULL,
            PCI             INT NULL,
            PSS             INT NULL,
            SSS             INT NULL,
            TAC             INT NULL,
            VENDOR          VARCHAR (30) NULL,
            LONGITUDE       FLOAT DEFAULT NULL,
            LATITUDE        FLOAT DEFAULT NULL,
            STYLE           VARCHAR (30) NULL,
            AZIMUTH         FLOAT NULL,
            HEIGHT          FLOAT NULL,
            ELECTTILT       FLOAT NULL,
            MECHTILT        FLOAT NULL,
            TOTLETILT       FLOAT NULL,
            PRIMARY KEY(SECTOR_ID)              
        );
        """,
        """
        (   
            起始时间                            DATETIME NOT NULL,
            网元或基站名称                        VARCHAR (64) NOT NULL,
            小区                                VARCHAR (256) NOT NULL,  
            小区名称                            VARCHAR (64) NOT NULL,
            RRC连接建立完成次数               INT NULL,
            RRC连接请求次数         INT NULL,
            RRC建立成功率qf                   FLOAT NULL,
            E_RAB建立成功总次数               INT NULL,
            E_RAB建立尝试总次数               INT NULL,
            E_RAB建立成功率2                  FLOAT NULL,
            eNodeB触发的E_RAB异常释放总次数     INT NULL,
            小区切换出E_RAB异常释放总次数        INT NULL,
            E_RAB掉线率                    FLOAT NULL,
            无线接通率ay                       FLOAT NULL,
            eNodeB发起的S1_RESET导致的UE_Context释放次数    INT NULL,
            UE_Context异常释放次数                         INT NULL,
            UE_Context建立成功总次数                        INT NULL,
            无线掉线率                 FLOAT NULL,
            eNodeB内异频切换出成功次数      INT NULL,
            eNodeB内异频切换出尝试次数      INT NULL,
            eNodeB内同频切换出成功次数      INT NULL,
            eNodeB内同频切换出尝试次数      INT NULL,
            eNodeB间异频切换出成功次数      INT NULL,
            eNodeB间异频切换出尝试次数      INT NULL,
            eNodeB间同频切换出成功次数      INT NULL,
            eNodeB间同频切换出尝试次数      INT NULL,
            eNB内切换成功率                FLOAT NULL,
            eNB间切换成功率                FLOAT NULL,       
            同频切换成功率zsp               FLOAT NULL,
            异频切换成功率zsp               FLOAT NULL,
            切换成功率                     FLOAT NULL,
            小区PDCP层所接收到的上行数据的总吞吐量          BIGINT NULL,
            小区PDCP层所发送的下行数据的总吞吐量            BIGINT NULL,
            RRC重建请求次数                            INT NULL,
            RRC连接重建比率                             FLOAT NULL,
            通过重建回源小区的eNodeB间同频切换出执行成功次数   INT NULL,
            通过重建回源小区的eNodeB间异频切换出执行成功次数   INT NULL,
            通过重建回源小区的eNodeB内同频切换出执行成功次数   INT NULL,
            通过重建回源小区的eNodeB内异频切换出执行成功次数   INT NULL,
            eNB内切换出成功次数                           INT NULL,
            eNB内切换出请求次数                           INT NULL,
            PRIMARY KEY(起始时间,网元或基站名称,小区,小区名称)   
        );      
        """,
        """
        (   
            起始时间                            DATETIME NOT NULL,
            网元或基站名称                        VARCHAR (64) NOT NULL,
            小区描述                            VARCHAR (256) NOT NULL,  
            小区名称                            VARCHAR (64) NOT NULL,
            第0个PRB上检测到的干扰噪声的平均值       INT NULL,
            第1个PRB上检测到的干扰噪声的平均值       INT NULL,
            第2个PRB上检测到的干扰噪声的平均值       INT NULL,
            第3个PRB上检测到的干扰噪声的平均值       INT NULL,
            第4个PRB上检测到的干扰噪声的平均值       INT NULL,
            第5个PRB上检测到的干扰噪声的平均值       INT NULL,
            第6个PRB上检测到的干扰噪声的平均值       INT NULL,
            第7个PRB上检测到的干扰噪声的平均值       INT NULL,
            第8个PRB上检测到的干扰噪声的平均值       INT NULL,
            第9个PRB上检测到的干扰噪声的平均值       INT NULL,
            第10个PRB上检测到的干扰噪声的平均值       INT NULL,
            第11个PRB上检测到的干扰噪声的平均值       INT NULL,
            第12个PRB上检测到的干扰噪声的平均值       INT NULL,
            第13个PRB上检测到的干扰噪声的平均值       INT NULL,
            第14个PRB上检测到的干扰噪声的平均值       INT NULL,
            第15个PRB上检测到的干扰噪声的平均值       INT NULL,
            第16个PRB上检测到的干扰噪声的平均值       INT NULL,
            第17个PRB上检测到的干扰噪声的平均值       INT NULL,
            第18个PRB上检测到的干扰噪声的平均值       INT NULL,
            第19个PRB上检测到的干扰噪声的平均值       INT NULL,
            第20个PRB上检测到的干扰噪声的平均值       INT NULL,
            第21个PRB上检测到的干扰噪声的平均值       INT NULL,
            第22个PRB上检测到的干扰噪声的平均值       INT NULL,
            第23个PRB上检测到的干扰噪声的平均值       INT NULL,
            第24个PRB上检测到的干扰噪声的平均值       INT NULL,
            第25个PRB上检测到的干扰噪声的平均值       INT NULL,
            第26个PRB上检测到的干扰噪声的平均值       INT NULL,
            第27个PRB上检测到的干扰噪声的平均值       INT NULL,
            第28个PRB上检测到的干扰噪声的平均值       INT NULL,
            第29个PRB上检测到的干扰噪声的平均值       INT NULL,
            第30个PRB上检测到的干扰噪声的平均值       INT NULL,
            第31个PRB上检测到的干扰噪声的平均值       INT NULL,
            第32个PRB上检测到的干扰噪声的平均值       INT NULL,
            第33个PRB上检测到的干扰噪声的平均值       INT NULL,
            第34个PRB上检测到的干扰噪声的平均值       INT NULL,
            第35个PRB上检测到的干扰噪声的平均值       INT NULL,
            第36个PRB上检测到的干扰噪声的平均值       INT NULL,
            第37个PRB上检测到的干扰噪声的平均值       INT NULL,
            第38个PRB上检测到的干扰噪声的平均值       INT NULL,
            第39个PRB上检测到的干扰噪声的平均值       INT NULL,
            第40个PRB上检测到的干扰噪声的平均值       INT NULL,
            第41个PRB上检测到的干扰噪声的平均值       INT NULL,
            第42个PRB上检测到的干扰噪声的平均值       INT NULL,
            第43个PRB上检测到的干扰噪声的平均值       INT NULL,
            第44个PRB上检测到的干扰噪声的平均值       INT NULL,
            第45个PRB上检测到的干扰噪声的平均值       INT NULL,
            第46个PRB上检测到的干扰噪声的平均值       INT NULL,
            第47个PRB上检测到的干扰噪声的平均值       INT NULL,
            第48个PRB上检测到的干扰噪声的平均值       INT NULL,
            第49个PRB上检测到的干扰噪声的平均值       INT NULL,
            第50个PRB上检测到的干扰噪声的平均值       INT NULL,
            第51个PRB上检测到的干扰噪声的平均值       INT NULL,
            第52个PRB上检测到的干扰噪声的平均值       INT NULL,
            第53个PRB上检测到的干扰噪声的平均值       INT NULL,
            第54个PRB上检测到的干扰噪声的平均值       INT NULL,
            第55个PRB上检测到的干扰噪声的平均值       INT NULL,
            第56个PRB上检测到的干扰噪声的平均值       INT NULL,
            第57个PRB上检测到的干扰噪声的平均值       INT NULL,
            第58个PRB上检测到的干扰噪声的平均值       INT NULL,
            第59个PRB上检测到的干扰噪声的平均值       INT NULL,
            第60个PRB上检测到的干扰噪声的平均值       INT NULL,
            第61个PRB上检测到的干扰噪声的平均值       INT NULL,
            第62个PRB上检测到的干扰噪声的平均值       INT NULL,
            第63个PRB上检测到的干扰噪声的平均值       INT NULL,
            第64个PRB上检测到的干扰噪声的平均值       INT NULL,
            第65个PRB上检测到的干扰噪声的平均值       INT NULL,
            第66个PRB上检测到的干扰噪声的平均值       INT NULL,
            第67个PRB上检测到的干扰噪声的平均值       INT NULL,
            第68个PRB上检测到的干扰噪声的平均值       INT NULL,
            第69个PRB上检测到的干扰噪声的平均值       INT NULL,
            第70个PRB上检测到的干扰噪声的平均值       INT NULL,
            第71个PRB上检测到的干扰噪声的平均值       INT NULL,
            第72个PRB上检测到的干扰噪声的平均值       INT NULL,
            第73个PRB上检测到的干扰噪声的平均值       INT NULL,
            第74个PRB上检测到的干扰噪声的平均值       INT NULL,
            第75个PRB上检测到的干扰噪声的平均值       INT NULL,
            第76个PRB上检测到的干扰噪声的平均值       INT NULL,
            第77个PRB上检测到的干扰噪声的平均值       INT NULL,
            第78个PRB上检测到的干扰噪声的平均值       INT NULL,
            第79个PRB上检测到的干扰噪声的平均值       INT NULL,
            第80个PRB上检测到的干扰噪声的平均值       INT NULL,
            第81个PRB上检测到的干扰噪声的平均值       INT NULL,
            第82个PRB上检测到的干扰噪声的平均值       INT NULL,
            第83个PRB上检测到的干扰噪声的平均值       INT NULL,
            第84个PRB上检测到的干扰噪声的平均值       INT NULL,
            第85个PRB上检测到的干扰噪声的平均值       INT NULL,
            第86个PRB上检测到的干扰噪声的平均值       INT NULL,
            第87个PRB上检测到的干扰噪声的平均值       INT NULL,
            第88个PRB上检测到的干扰噪声的平均值       INT NULL,
            第89个PRB上检测到的干扰噪声的平均值       INT NULL,
            第90个PRB上检测到的干扰噪声的平均值       INT NULL,
            第91个PRB上检测到的干扰噪声的平均值       INT NULL,
            第92个PRB上检测到的干扰噪声的平均值       INT NULL,
            第93个PRB上检测到的干扰噪声的平均值       INT NULL,
            第94个PRB上检测到的干扰噪声的平均值       INT NULL,
            第95个PRB上检测到的干扰噪声的平均值       INT NULL,
            第96个PRB上检测到的干扰噪声的平均值       INT NULL,
            第97个PRB上检测到的干扰噪声的平均值       INT NULL,
            第98个PRB上检测到的干扰噪声的平均值       INT NULL,
            第99个PRB上检测到的干扰噪声的平均值       INT NULL,            
            PRIMARY KEY(起始时间,网元或基站名称,小区描述,小区名称) 
        );      
        """,
        """
        (
            TimeStamp                           DATETIME NOT NULL,
            ServingSector                       VARCHAR (30) NOT NULL,
            InterferingSector                   VARCHAR (30) NOT NULL,  
            LteScRSRP                           INT NOT NULL,
            LteNcRSRP                           INT NOT NULL,
            LteNcEarfcn                         INT NULL,
            LteNcPci                            INT NULL,
            PRIMARY KEY(TimeStamp,ServingSector,InterferingSector,LteScRSRP,LteNcRSRP)
        );      
        """,
        """
        (   
            起始时间                            DATETIME NOT NULL,
            网元或基站名称                        VARCHAR (64) NOT NULL,
            小区描述                            VARCHAR (256) NOT NULL,  
            小区名称                            VARCHAR (64) NOT NULL,
            第0个PRB上检测到的干扰噪声的平均值       INT NULL,
            第1个PRB上检测到的干扰噪声的平均值       INT NULL,
            第2个PRB上检测到的干扰噪声的平均值       INT NULL,
            第3个PRB上检测到的干扰噪声的平均值       INT NULL,
            第4个PRB上检测到的干扰噪声的平均值       INT NULL,
            第5个PRB上检测到的干扰噪声的平均值       INT NULL,
            第6个PRB上检测到的干扰噪声的平均值       INT NULL,
            第7个PRB上检测到的干扰噪声的平均值       INT NULL,
            第8个PRB上检测到的干扰噪声的平均值       INT NULL,
            第9个PRB上检测到的干扰噪声的平均值       INT NULL,
            第10个PRB上检测到的干扰噪声的平均值       INT NULL,
            第11个PRB上检测到的干扰噪声的平均值       INT NULL,
            第12个PRB上检测到的干扰噪声的平均值       INT NULL,
            第13个PRB上检测到的干扰噪声的平均值       INT NULL,
            第14个PRB上检测到的干扰噪声的平均值       INT NULL,
            第15个PRB上检测到的干扰噪声的平均值       INT NULL,
            第16个PRB上检测到的干扰噪声的平均值       INT NULL,
            第17个PRB上检测到的干扰噪声的平均值       INT NULL,
            第18个PRB上检测到的干扰噪声的平均值       INT NULL,
            第19个PRB上检测到的干扰噪声的平均值       INT NULL,
            第20个PRB上检测到的干扰噪声的平均值       INT NULL,
            第21个PRB上检测到的干扰噪声的平均值       INT NULL,
            第22个PRB上检测到的干扰噪声的平均值       INT NULL,
            第23个PRB上检测到的干扰噪声的平均值       INT NULL,
            第24个PRB上检测到的干扰噪声的平均值       INT NULL,
            第25个PRB上检测到的干扰噪声的平均值       INT NULL,
            第26个PRB上检测到的干扰噪声的平均值       INT NULL,
            第27个PRB上检测到的干扰噪声的平均值       INT NULL,
            第28个PRB上检测到的干扰噪声的平均值       INT NULL,
            第29个PRB上检测到的干扰噪声的平均值       INT NULL,
            第30个PRB上检测到的干扰噪声的平均值       INT NULL,
            第31个PRB上检测到的干扰噪声的平均值       INT NULL,
            第32个PRB上检测到的干扰噪声的平均值       INT NULL,
            第33个PRB上检测到的干扰噪声的平均值       INT NULL,
            第34个PRB上检测到的干扰噪声的平均值       INT NULL,
            第35个PRB上检测到的干扰噪声的平均值       INT NULL,
            第36个PRB上检测到的干扰噪声的平均值       INT NULL,
            第37个PRB上检测到的干扰噪声的平均值       INT NULL,
            第38个PRB上检测到的干扰噪声的平均值       INT NULL,
            第39个PRB上检测到的干扰噪声的平均值       INT NULL,
            第40个PRB上检测到的干扰噪声的平均值       INT NULL,
            第41个PRB上检测到的干扰噪声的平均值       INT NULL,
            第42个PRB上检测到的干扰噪声的平均值       INT NULL,
            第43个PRB上检测到的干扰噪声的平均值       INT NULL,
            第44个PRB上检测到的干扰噪声的平均值       INT NULL,
            第45个PRB上检测到的干扰噪声的平均值       INT NULL,
            第46个PRB上检测到的干扰噪声的平均值       INT NULL,
            第47个PRB上检测到的干扰噪声的平均值       INT NULL,
            第48个PRB上检测到的干扰噪声的平均值       INT NULL,
            第49个PRB上检测到的干扰噪声的平均值       INT NULL,
            第50个PRB上检测到的干扰噪声的平均值       INT NULL,
            第51个PRB上检测到的干扰噪声的平均值       INT NULL,
            第52个PRB上检测到的干扰噪声的平均值       INT NULL,
            第53个PRB上检测到的干扰噪声的平均值       INT NULL,
            第54个PRB上检测到的干扰噪声的平均值       INT NULL,
            第55个PRB上检测到的干扰噪声的平均值       INT NULL,
            第56个PRB上检测到的干扰噪声的平均值       INT NULL,
            第57个PRB上检测到的干扰噪声的平均值       INT NULL,
            第58个PRB上检测到的干扰噪声的平均值       INT NULL,
            第59个PRB上检测到的干扰噪声的平均值       INT NULL,
            第60个PRB上检测到的干扰噪声的平均值       INT NULL,
            第61个PRB上检测到的干扰噪声的平均值       INT NULL,
            第62个PRB上检测到的干扰噪声的平均值       INT NULL,
            第63个PRB上检测到的干扰噪声的平均值       INT NULL,
            第64个PRB上检测到的干扰噪声的平均值       INT NULL,
            第65个PRB上检测到的干扰噪声的平均值       INT NULL,
            第66个PRB上检测到的干扰噪声的平均值       INT NULL,
            第67个PRB上检测到的干扰噪声的平均值       INT NULL,
            第68个PRB上检测到的干扰噪声的平均值       INT NULL,
            第69个PRB上检测到的干扰噪声的平均值       INT NULL,
            第70个PRB上检测到的干扰噪声的平均值       INT NULL,
            第71个PRB上检测到的干扰噪声的平均值       INT NULL,
            第72个PRB上检测到的干扰噪声的平均值       INT NULL,
            第73个PRB上检测到的干扰噪声的平均值       INT NULL,
            第74个PRB上检测到的干扰噪声的平均值       INT NULL,
            第75个PRB上检测到的干扰噪声的平均值       INT NULL,
            第76个PRB上检测到的干扰噪声的平均值       INT NULL,
            第77个PRB上检测到的干扰噪声的平均值       INT NULL,
            第78个PRB上检测到的干扰噪声的平均值       INT NULL,
            第79个PRB上检测到的干扰噪声的平均值       INT NULL,
            第80个PRB上检测到的干扰噪声的平均值       INT NULL,
            第81个PRB上检测到的干扰噪声的平均值       INT NULL,
            第82个PRB上检测到的干扰噪声的平均值       INT NULL,
            第83个PRB上检测到的干扰噪声的平均值       INT NULL,
            第84个PRB上检测到的干扰噪声的平均值       INT NULL,
            第85个PRB上检测到的干扰噪声的平均值       INT NULL,
            第86个PRB上检测到的干扰噪声的平均值       INT NULL,
            第87个PRB上检测到的干扰噪声的平均值       INT NULL,
            第88个PRB上检测到的干扰噪声的平均值       INT NULL,
            第89个PRB上检测到的干扰噪声的平均值       INT NULL,
            第90个PRB上检测到的干扰噪声的平均值       INT NULL,
            第91个PRB上检测到的干扰噪声的平均值       INT NULL,
            第92个PRB上检测到的干扰噪声的平均值       INT NULL,
            第93个PRB上检测到的干扰噪声的平均值       INT NULL,
            第94个PRB上检测到的干扰噪声的平均值       INT NULL,
            第95个PRB上检测到的干扰噪声的平均值       INT NULL,
            第96个PRB上检测到的干扰噪声的平均值       INT NULL,
            第97个PRB上检测到的干扰噪声的平均值       INT NULL,
            第98个PRB上检测到的干扰噪声的平均值       INT NULL,
            第99个PRB上检测到的干扰噪声的平均值       INT NULL,            
            PRIMARY KEY(起始时间,网元或基站名称,小区描述,小区名称) 
        );      
        """,
        """
        (
            userName    VARCHAR(256) NOT NULL,
            passWord    VARCHAR(256) NOT NULL,
            regTime     DATETIME NOT NULL,
            PRIMARY KEY(userName)
        );
        """,
        """
        (
            userName    VARCHAR(256) NOT NULL,
            passWord    VARCHAR(256) NOT NULL,
            regTime     DATETIME NOT NULL,
            PRIMARY KEY(userName)
        );
        """,
        """
        (
            ServingSector                       VARCHAR (30) NOT NULL,
            InterferingSector                   VARCHAR (30) NOT NULL,  
            mean                                FLOAT NULL,
            std                                 FLOAT NULL,
            PrbC2I9                             FLOAT NULL,
            PrbABS6                             FLOAT NULL,
            PRIMARY KEY(ServingSector,InterferingSector)
        );          
        """,
        """
        (
            SectorA     VARCHAR (30) NOT NULL,
            SectorB     VARCHAR (30) NOT NULL,  
            SectorC     VARCHAR (30) NOT NULL, 
            PRIMARY KEY(SectorA,SectorB,SectorC)
        ); 
        """
]
sql_trigger = [
        """
        before insert on tbCell_tmp for each row
        begin
            if exists(select tbCell.SECTOR_ID from tbCell where tbCell.SECTOR_ID=NEW.SECTOR_ID) then
                update tbCell set 
                CITY=NEW.CITY,ENODEBID=NEW.ENODEBID,ENODEB_NAME=NEW.ENODEB_NAME,EARFCN=NEW.EARFCN,
                PCI=NEW.PCI,PSS=NEW.PSS,SSS=NEW.PSS,TAC=NEW.TAC,VENDOR=NEW.VENDOR,LONGITUDE=NEW.LONGITUDE,LATITUDE=NEW.LATITUDE,
                STYLE=NEW.STYLE,AZIMUTH=NEW.AZIMUTH,HEIGHT=NEW.HEIGHT,ELECTTILT=NEW.ELECTTILT,MECHTILT=NEW.MECHTILT,TOTLETILT=NEW.TOTLETILT
                where SECTOR_ID=NEW.SECTOR_ID;
            else
                insert into tbCell(CITY,SECTOR_ID,SECTOR_NAME,ENODEBID,ENODEB_NAME,EARFCN,PCI,PSS,SSS,TAC,VENDOR,LONGITUDE,LATITUDE,STYLE,AZIMUTH,HEIGHT,ELECTTILT,MECHTILT,TOTLETILT)
                values(NEW.CITY,NEW.SECTOR_ID,NEW.SECTOR_NAME,NEW.ENODEBID,NEW.ENODEB_NAME,NEW.EARFCN,NEW.PCI,NEW.PSS,NEW.SSS,NEW.TAC,NEW.VENDOR,NEW.LONGITUDE,NEW.LATITUDE,NEW.STYLE,NEW.AZIMUTH,NEW.HEIGHT,NEW.ELECTTILT,NEW.MECHTILT,NEW.TOTLETILT); 
            end if;
        end
        """,
        """
        before insert on tbKPI_tmp for each row
        begin
            if exists(select tbKPI.小区 from tbKPI where tbKPI.起始时间=NEW.起始时间 and tbKPI.网元或基站名称=NEW.网元或基站名称 
                                                        and tbKPI.小区=NEW.小区 and tbKPI.小区名称=NEW.小区名称) then
                update tbKPI set
                RRC连接建立完成次数=NEW.RRC连接建立完成次数,RRC连接请求次数=NEW.RRC连接请求次数,RRC建立成功率qf=NEW.RRC建立成功率qf,
                E_RAB建立成功总次数=NEW.E_RAB建立成功总次数,E_RAB建立尝试总次数=NEW.E_RAB建立尝试总次数,E_RAB建立成功率2=NEW.E_RAB建立成功率2,
                eNodeB触发的E_RAB异常释放总次数=NEW.eNodeB触发的E_RAB异常释放总次数,小区切换出E_RAB异常释放总次数=NEW.小区切换出E_RAB异常释放总次数,
                E_RAB掉线率=NEW.E_RAB掉线率,无线接通率ay=NEW.无线接通率ay,eNodeB发起的S1_RESET导致的UE_Context释放次数=NEW.eNodeB发起的S1_RESET导致的UE_Context释放次数,
                UE_Context异常释放次数=NEW.UE_Context异常释放次数,UE_Context建立成功总次数=NEW.UE_Context建立成功总次数,
                无线掉线率=NEW.无线掉线率,eNodeB内异频切换出成功次数=NEW.eNodeB内异频切换出成功次数,eNodeB内异频切换出尝试次数=NEW.eNodeB内异频切换出尝试次数,
                eNodeB内同频切换出成功次数=NEW.eNodeB内同频切换出成功次数,eNodeB内同频切换出尝试次数=NEW.eNodeB内同频切换出尝试次数,
                eNodeB间异频切换出成功次数=NEW.eNodeB间异频切换出成功次数,eNodeB间异频切换出尝试次数=NEW.eNodeB间异频切换出尝试次数,
                eNodeB间同频切换出成功次数=NEW.eNodeB间同频切换出成功次数,eNodeB间同频切换出尝试次数=NEW.eNodeB间同频切换出尝试次数,
                eNB内切换成功率=NEW.eNB内切换成功率,eNB间切换成功率=NEW.eNB间切换成功率,同频切换成功率zsp=NEW.同频切换成功率zsp,异频切换成功率zsp=NEW.异频切换成功率zsp,
                切换成功率=NEW.切换成功率,小区PDCP层所接收到的上行数据的总吞吐量=NEW.小区PDCP层所接收到的上行数据的总吞吐量,小区PDCP层所发送的下行数据的总吞吐量=NEW.小区PDCP层所发送的下行数据的总吞吐量,
                RRC重建请求次数=NEW.RRC重建请求次数,RRC连接重建比率=NEW.RRC连接重建比率,通过重建回源小区的eNodeB间同频切换出执行成功次数=NEW.通过重建回源小区的eNodeB间同频切换出执行成功次数,
                通过重建回源小区的eNodeB间异频切换出执行成功次数=NEW.通过重建回源小区的eNodeB间异频切换出执行成功次数,通过重建回源小区的eNodeB内同频切换出执行成功次数=NEW.通过重建回源小区的eNodeB内同频切换出执行成功次数,
                通过重建回源小区的eNodeB内异频切换出执行成功次数=NEW.通过重建回源小区的eNodeB内异频切换出执行成功次数,eNB内切换出成功次数=NEW.eNB内切换出成功次数,eNB内切换出请求次数=NEW.eNB内切换出请求次数
                where tbKPI.起始时间=NEW.起始时间 and tbKPI.网元或基站名称=NEW.网元或基站名称 and tbKPI.小区=NEW.小区 and tbKPI.小区名称=NEW.小区名称;
            else
                insert into tbKPI(起始时间,网元或基站名称,小区,小区名称,RRC连接建立完成次数,RRC连接请求次数,RRC建立成功率qf,
                                  E_RAB建立成功总次数,E_RAB建立尝试总次数,E_RAB建立成功率2,eNodeB触发的E_RAB异常释放总次数,小区切换出E_RAB异常释放总次数,
                                  E_RAB掉线率,无线接通率ay,eNodeB发起的S1_RESET导致的UE_Context释放次数,UE_Context异常释放次数,UE_Context建立成功总次数,
                                  无线掉线率,eNodeB内异频切换出成功次数,eNodeB内异频切换出尝试次数,eNodeB内同频切换出成功次数,eNodeB内同频切换出尝试次数,
                                  eNodeB间异频切换出成功次数,eNodeB间异频切换出尝试次数,eNodeB间同频切换出成功次数,eNodeB间同频切换出尝试次数,eNB内切换成功率,
                                  eNB间切换成功率,同频切换成功率zsp,异频切换成功率zsp,切换成功率,小区PDCP层所接收到的上行数据的总吞吐量,小区PDCP层所发送的下行数据的总吞吐量,
                                  RRC重建请求次数,RRC连接重建比率,通过重建回源小区的eNodeB间同频切换出执行成功次数,通过重建回源小区的eNodeB间异频切换出执行成功次数,
                                  通过重建回源小区的eNodeB内同频切换出执行成功次数,通过重建回源小区的eNodeB内异频切换出执行成功次数,eNB内切换出成功次数,eNB内切换出请求次数)
                values(NEW.起始时间,NEW.网元或基站名称,NEW.小区,NEW.小区名称,NEW.RRC连接建立完成次数,NEW.RRC连接请求次数,NEW.RRC建立成功率qf,
                                  NEW.E_RAB建立成功总次数,NEW.E_RAB建立尝试总次数,NEW.E_RAB建立成功率2,NEW.eNodeB触发的E_RAB异常释放总次数,NEW.小区切换出E_RAB异常释放总次数,
                                  NEW.E_RAB掉线率,NEW.无线接通率ay,NEW.eNodeB发起的S1_RESET导致的UE_Context释放次数,NEW.UE_Context异常释放次数,NEW.UE_Context建立成功总次数,
                                  NEW.无线掉线率,NEW.eNodeB内异频切换出成功次数,NEW.eNodeB内异频切换出尝试次数,NEW.eNodeB内同频切换出成功次数,NEW.eNodeB内同频切换出尝试次数,
                                  NEW.eNodeB间异频切换出成功次数,NEW.eNodeB间异频切换出尝试次数,NEW.eNodeB间同频切换出成功次数,NEW.eNodeB间同频切换出尝试次数,NEW.eNB内切换成功率,
                                  NEW.eNB间切换成功率,NEW.同频切换成功率zsp,NEW.异频切换成功率zsp,NEW.切换成功率,NEW.小区PDCP层所接收到的上行数据的总吞吐量,NEW.小区PDCP层所发送的下行数据的总吞吐量,
                                  NEW.RRC重建请求次数,NEW.RRC连接重建比率,NEW.通过重建回源小区的eNodeB间同频切换出执行成功次数,NEW.通过重建回源小区的eNodeB间异频切换出执行成功次数,
                                  NEW.通过重建回源小区的eNodeB内同频切换出执行成功次数,NEW.通过重建回源小区的eNodeB内异频切换出执行成功次数,NEW.eNB内切换出成功次数,NEW.eNB内切换出请求次数);
            end if;
        end
        """,
        """
        before insert on tbPRB_tmp for each row
        begin
            if exists(select tbPRB.小区描述 from tbPRB where tbPRB.起始时间=NEW.起始时间 and tbPRB.网元或基站名称=NEW.网元或基站名称 
                                                        and tbPRB.小区描述=NEW.小区描述 and tbPRB.小区名称=NEW.小区名称) then
                update tbPRB set
                第0个PRB上检测到的干扰噪声的平均值=NEW.第0个PRB上检测到的干扰噪声的平均值,第1个PRB上检测到的干扰噪声的平均值=NEW.第1个PRB上检测到的干扰噪声的平均值,第2个PRB上检测到的干扰噪声的平均值=NEW.第2个PRB上检测到的干扰噪声的平均值,第3个PRB上检测到的干扰噪声的平均值=NEW.第3个PRB上检测到的干扰噪声的平均值,第4个PRB上检测到的干扰噪声的平均值=NEW.第4个PRB上检测到的干扰噪声的平均值,
                第5个PRB上检测到的干扰噪声的平均值=NEW.第5个PRB上检测到的干扰噪声的平均值,第6个PRB上检测到的干扰噪声的平均值=NEW.第6个PRB上检测到的干扰噪声的平均值,第7个PRB上检测到的干扰噪声的平均值=NEW.第7个PRB上检测到的干扰噪声的平均值,第8个PRB上检测到的干扰噪声的平均值=NEW.第8个PRB上检测到的干扰噪声的平均值,第9个PRB上检测到的干扰噪声的平均值=NEW.第9个PRB上检测到的干扰噪声的平均值,
                第10个PRB上检测到的干扰噪声的平均值=NEW.第10个PRB上检测到的干扰噪声的平均值,第11个PRB上检测到的干扰噪声的平均值=NEW.第11个PRB上检测到的干扰噪声的平均值,第12个PRB上检测到的干扰噪声的平均值=NEW.第12个PRB上检测到的干扰噪声的平均值,第13个PRB上检测到的干扰噪声的平均值=NEW.第13个PRB上检测到的干扰噪声的平均值,第14个PRB上检测到的干扰噪声的平均值=NEW.第14个PRB上检测到的干扰噪声的平均值,
                第15个PRB上检测到的干扰噪声的平均值=NEW.第15个PRB上检测到的干扰噪声的平均值,第16个PRB上检测到的干扰噪声的平均值=NEW.第16个PRB上检测到的干扰噪声的平均值,第17个PRB上检测到的干扰噪声的平均值=NEW.第17个PRB上检测到的干扰噪声的平均值,第18个PRB上检测到的干扰噪声的平均值=NEW.第18个PRB上检测到的干扰噪声的平均值,第19个PRB上检测到的干扰噪声的平均值=NEW.第19个PRB上检测到的干扰噪声的平均值,
                第20个PRB上检测到的干扰噪声的平均值=NEW.第20个PRB上检测到的干扰噪声的平均值,第21个PRB上检测到的干扰噪声的平均值=NEW.第21个PRB上检测到的干扰噪声的平均值,第22个PRB上检测到的干扰噪声的平均值=NEW.第22个PRB上检测到的干扰噪声的平均值,第23个PRB上检测到的干扰噪声的平均值=NEW.第23个PRB上检测到的干扰噪声的平均值,第24个PRB上检测到的干扰噪声的平均值=NEW.第24个PRB上检测到的干扰噪声的平均值,
                第25个PRB上检测到的干扰噪声的平均值=NEW.第25个PRB上检测到的干扰噪声的平均值,第26个PRB上检测到的干扰噪声的平均值=NEW.第26个PRB上检测到的干扰噪声的平均值,第27个PRB上检测到的干扰噪声的平均值=NEW.第27个PRB上检测到的干扰噪声的平均值,第28个PRB上检测到的干扰噪声的平均值=NEW.第28个PRB上检测到的干扰噪声的平均值,第29个PRB上检测到的干扰噪声的平均值=NEW.第29个PRB上检测到的干扰噪声的平均值,
                第30个PRB上检测到的干扰噪声的平均值=NEW.第30个PRB上检测到的干扰噪声的平均值,第31个PRB上检测到的干扰噪声的平均值=NEW.第31个PRB上检测到的干扰噪声的平均值,第32个PRB上检测到的干扰噪声的平均值=NEW.第32个PRB上检测到的干扰噪声的平均值,第33个PRB上检测到的干扰噪声的平均值=NEW.第33个PRB上检测到的干扰噪声的平均值,第34个PRB上检测到的干扰噪声的平均值=NEW.第34个PRB上检测到的干扰噪声的平均值,
                第35个PRB上检测到的干扰噪声的平均值=NEW.第35个PRB上检测到的干扰噪声的平均值,第36个PRB上检测到的干扰噪声的平均值=NEW.第36个PRB上检测到的干扰噪声的平均值,第37个PRB上检测到的干扰噪声的平均值=NEW.第37个PRB上检测到的干扰噪声的平均值,第38个PRB上检测到的干扰噪声的平均值=NEW.第38个PRB上检测到的干扰噪声的平均值,第39个PRB上检测到的干扰噪声的平均值=NEW.第39个PRB上检测到的干扰噪声的平均值,
                第40个PRB上检测到的干扰噪声的平均值=NEW.第40个PRB上检测到的干扰噪声的平均值,第41个PRB上检测到的干扰噪声的平均值=NEW.第41个PRB上检测到的干扰噪声的平均值,第42个PRB上检测到的干扰噪声的平均值=NEW.第42个PRB上检测到的干扰噪声的平均值,第43个PRB上检测到的干扰噪声的平均值=NEW.第43个PRB上检测到的干扰噪声的平均值,第44个PRB上检测到的干扰噪声的平均值=NEW.第44个PRB上检测到的干扰噪声的平均值,
                第45个PRB上检测到的干扰噪声的平均值=NEW.第45个PRB上检测到的干扰噪声的平均值,第46个PRB上检测到的干扰噪声的平均值=NEW.第46个PRB上检测到的干扰噪声的平均值,第47个PRB上检测到的干扰噪声的平均值=NEW.第47个PRB上检测到的干扰噪声的平均值,第48个PRB上检测到的干扰噪声的平均值=NEW.第48个PRB上检测到的干扰噪声的平均值,第49个PRB上检测到的干扰噪声的平均值=NEW.第49个PRB上检测到的干扰噪声的平均值,
                第50个PRB上检测到的干扰噪声的平均值=NEW.第50个PRB上检测到的干扰噪声的平均值,第51个PRB上检测到的干扰噪声的平均值=NEW.第51个PRB上检测到的干扰噪声的平均值,第52个PRB上检测到的干扰噪声的平均值=NEW.第52个PRB上检测到的干扰噪声的平均值,第53个PRB上检测到的干扰噪声的平均值=NEW.第53个PRB上检测到的干扰噪声的平均值,第54个PRB上检测到的干扰噪声的平均值=NEW.第54个PRB上检测到的干扰噪声的平均值,
                第55个PRB上检测到的干扰噪声的平均值=NEW.第55个PRB上检测到的干扰噪声的平均值,第56个PRB上检测到的干扰噪声的平均值=NEW.第56个PRB上检测到的干扰噪声的平均值,第57个PRB上检测到的干扰噪声的平均值=NEW.第57个PRB上检测到的干扰噪声的平均值,第58个PRB上检测到的干扰噪声的平均值=NEW.第58个PRB上检测到的干扰噪声的平均值,第59个PRB上检测到的干扰噪声的平均值=NEW.第59个PRB上检测到的干扰噪声的平均值,
                第60个PRB上检测到的干扰噪声的平均值=NEW.第60个PRB上检测到的干扰噪声的平均值,第61个PRB上检测到的干扰噪声的平均值=NEW.第61个PRB上检测到的干扰噪声的平均值,第62个PRB上检测到的干扰噪声的平均值=NEW.第62个PRB上检测到的干扰噪声的平均值,第63个PRB上检测到的干扰噪声的平均值=NEW.第63个PRB上检测到的干扰噪声的平均值,第64个PRB上检测到的干扰噪声的平均值=NEW.第64个PRB上检测到的干扰噪声的平均值,
                第65个PRB上检测到的干扰噪声的平均值=NEW.第65个PRB上检测到的干扰噪声的平均值,第66个PRB上检测到的干扰噪声的平均值=NEW.第66个PRB上检测到的干扰噪声的平均值,第67个PRB上检测到的干扰噪声的平均值=NEW.第67个PRB上检测到的干扰噪声的平均值,第68个PRB上检测到的干扰噪声的平均值=NEW.第68个PRB上检测到的干扰噪声的平均值,第69个PRB上检测到的干扰噪声的平均值=NEW.第69个PRB上检测到的干扰噪声的平均值,
                第70个PRB上检测到的干扰噪声的平均值=NEW.第70个PRB上检测到的干扰噪声的平均值,第71个PRB上检测到的干扰噪声的平均值=NEW.第71个PRB上检测到的干扰噪声的平均值,第72个PRB上检测到的干扰噪声的平均值=NEW.第72个PRB上检测到的干扰噪声的平均值,第73个PRB上检测到的干扰噪声的平均值=NEW.第73个PRB上检测到的干扰噪声的平均值,第74个PRB上检测到的干扰噪声的平均值=NEW.第74个PRB上检测到的干扰噪声的平均值,
                第75个PRB上检测到的干扰噪声的平均值=NEW.第75个PRB上检测到的干扰噪声的平均值,第76个PRB上检测到的干扰噪声的平均值=NEW.第76个PRB上检测到的干扰噪声的平均值,第77个PRB上检测到的干扰噪声的平均值=NEW.第77个PRB上检测到的干扰噪声的平均值,第78个PRB上检测到的干扰噪声的平均值=NEW.第78个PRB上检测到的干扰噪声的平均值,第79个PRB上检测到的干扰噪声的平均值=NEW.第79个PRB上检测到的干扰噪声的平均值,
                第80个PRB上检测到的干扰噪声的平均值=NEW.第80个PRB上检测到的干扰噪声的平均值,第81个PRB上检测到的干扰噪声的平均值=NEW.第81个PRB上检测到的干扰噪声的平均值,第82个PRB上检测到的干扰噪声的平均值=NEW.第82个PRB上检测到的干扰噪声的平均值,第83个PRB上检测到的干扰噪声的平均值=NEW.第83个PRB上检测到的干扰噪声的平均值,第84个PRB上检测到的干扰噪声的平均值=NEW.第84个PRB上检测到的干扰噪声的平均值,
                第85个PRB上检测到的干扰噪声的平均值=NEW.第85个PRB上检测到的干扰噪声的平均值,第86个PRB上检测到的干扰噪声的平均值=NEW.第86个PRB上检测到的干扰噪声的平均值,第87个PRB上检测到的干扰噪声的平均值=NEW.第87个PRB上检测到的干扰噪声的平均值,第88个PRB上检测到的干扰噪声的平均值=NEW.第88个PRB上检测到的干扰噪声的平均值,第89个PRB上检测到的干扰噪声的平均值=NEW.第89个PRB上检测到的干扰噪声的平均值,
                第90个PRB上检测到的干扰噪声的平均值=NEW.第90个PRB上检测到的干扰噪声的平均值,第91个PRB上检测到的干扰噪声的平均值=NEW.第91个PRB上检测到的干扰噪声的平均值,第92个PRB上检测到的干扰噪声的平均值=NEW.第92个PRB上检测到的干扰噪声的平均值,第93个PRB上检测到的干扰噪声的平均值=NEW.第93个PRB上检测到的干扰噪声的平均值,第94个PRB上检测到的干扰噪声的平均值=NEW.第94个PRB上检测到的干扰噪声的平均值,
                第95个PRB上检测到的干扰噪声的平均值=NEW.第95个PRB上检测到的干扰噪声的平均值,第96个PRB上检测到的干扰噪声的平均值=NEW.第96个PRB上检测到的干扰噪声的平均值,第97个PRB上检测到的干扰噪声的平均值=NEW.第97个PRB上检测到的干扰噪声的平均值,第98个PRB上检测到的干扰噪声的平均值=NEW.第98个PRB上检测到的干扰噪声的平均值,第99个PRB上检测到的干扰噪声的平均值=NEW.第99个PRB上检测到的干扰噪声的平均值
                where tbPRB.起始时间=NEW.起始时间 and tbPRB.网元或基站名称=NEW.网元或基站名称 and tbPRB.小区描述=NEW.小区描述 and tbPRB.小区名称=NEW.小区名称;
            else
                insert into tbPRB(起始时间,网元或基站名称,小区描述,小区名称,
                第0个PRB上检测到的干扰噪声的平均值,第1个PRB上检测到的干扰噪声的平均值,第2个PRB上检测到的干扰噪声的平均值,第3个PRB上检测到的干扰噪声的平均值,第4个PRB上检测到的干扰噪声的平均值,第5个PRB上检测到的干扰噪声的平均值,第6个PRB上检测到的干扰噪声的平均值,第7个PRB上检测到的干扰噪声的平均值,第8个PRB上检测到的干扰噪声的平均值,第9个PRB上检测到的干扰噪声的平均值,
                第10个PRB上检测到的干扰噪声的平均值,第11个PRB上检测到的干扰噪声的平均值,第12个PRB上检测到的干扰噪声的平均值,第13个PRB上检测到的干扰噪声的平均值,第14个PRB上检测到的干扰噪声的平均值,第15个PRB上检测到的干扰噪声的平均值,第16个PRB上检测到的干扰噪声的平均值,第17个PRB上检测到的干扰噪声的平均值,第18个PRB上检测到的干扰噪声的平均值,第19个PRB上检测到的干扰噪声的平均值,
                第20个PRB上检测到的干扰噪声的平均值,第21个PRB上检测到的干扰噪声的平均值,第22个PRB上检测到的干扰噪声的平均值,第23个PRB上检测到的干扰噪声的平均值,第24个PRB上检测到的干扰噪声的平均值,第25个PRB上检测到的干扰噪声的平均值,第26个PRB上检测到的干扰噪声的平均值,第27个PRB上检测到的干扰噪声的平均值,第28个PRB上检测到的干扰噪声的平均值,第29个PRB上检测到的干扰噪声的平均值,
                第30个PRB上检测到的干扰噪声的平均值,第31个PRB上检测到的干扰噪声的平均值,第32个PRB上检测到的干扰噪声的平均值,第33个PRB上检测到的干扰噪声的平均值,第34个PRB上检测到的干扰噪声的平均值,第35个PRB上检测到的干扰噪声的平均值,第36个PRB上检测到的干扰噪声的平均值,第37个PRB上检测到的干扰噪声的平均值,第38个PRB上检测到的干扰噪声的平均值,第39个PRB上检测到的干扰噪声的平均值,
                第40个PRB上检测到的干扰噪声的平均值,第41个PRB上检测到的干扰噪声的平均值,第42个PRB上检测到的干扰噪声的平均值,第43个PRB上检测到的干扰噪声的平均值,第44个PRB上检测到的干扰噪声的平均值,第45个PRB上检测到的干扰噪声的平均值,第46个PRB上检测到的干扰噪声的平均值,第47个PRB上检测到的干扰噪声的平均值,第48个PRB上检测到的干扰噪声的平均值,第49个PRB上检测到的干扰噪声的平均值,
                第50个PRB上检测到的干扰噪声的平均值,第51个PRB上检测到的干扰噪声的平均值,第52个PRB上检测到的干扰噪声的平均值,第53个PRB上检测到的干扰噪声的平均值,第54个PRB上检测到的干扰噪声的平均值,第55个PRB上检测到的干扰噪声的平均值,第56个PRB上检测到的干扰噪声的平均值,第57个PRB上检测到的干扰噪声的平均值,第58个PRB上检测到的干扰噪声的平均值,第59个PRB上检测到的干扰噪声的平均值,
                第60个PRB上检测到的干扰噪声的平均值,第61个PRB上检测到的干扰噪声的平均值,第62个PRB上检测到的干扰噪声的平均值,第63个PRB上检测到的干扰噪声的平均值,第64个PRB上检测到的干扰噪声的平均值,第65个PRB上检测到的干扰噪声的平均值,第66个PRB上检测到的干扰噪声的平均值,第67个PRB上检测到的干扰噪声的平均值,第68个PRB上检测到的干扰噪声的平均值,第69个PRB上检测到的干扰噪声的平均值,
                第70个PRB上检测到的干扰噪声的平均值,第71个PRB上检测到的干扰噪声的平均值,第72个PRB上检测到的干扰噪声的平均值,第73个PRB上检测到的干扰噪声的平均值,第74个PRB上检测到的干扰噪声的平均值,第75个PRB上检测到的干扰噪声的平均值,第76个PRB上检测到的干扰噪声的平均值,第77个PRB上检测到的干扰噪声的平均值,第78个PRB上检测到的干扰噪声的平均值,第79个PRB上检测到的干扰噪声的平均值,
                第80个PRB上检测到的干扰噪声的平均值,第81个PRB上检测到的干扰噪声的平均值,第82个PRB上检测到的干扰噪声的平均值,第83个PRB上检测到的干扰噪声的平均值,第84个PRB上检测到的干扰噪声的平均值,第85个PRB上检测到的干扰噪声的平均值,第86个PRB上检测到的干扰噪声的平均值,第87个PRB上检测到的干扰噪声的平均值,第88个PRB上检测到的干扰噪声的平均值,第89个PRB上检测到的干扰噪声的平均值,
                第90个PRB上检测到的干扰噪声的平均值,第91个PRB上检测到的干扰噪声的平均值,第92个PRB上检测到的干扰噪声的平均值,第93个PRB上检测到的干扰噪声的平均值,第94个PRB上检测到的干扰噪声的平均值,第95个PRB上检测到的干扰噪声的平均值,第96个PRB上检测到的干扰噪声的平均值,第97个PRB上检测到的干扰噪声的平均值,第98个PRB上检测到的干扰噪声的平均值,第99个PRB上检测到的干扰噪声的平均值)
                values(NEW.起始时间,NEW.网元或基站名称,NEW.小区描述,NEW.小区名称,
                NEW.第0个PRB上检测到的干扰噪声的平均值,NEW.第1个PRB上检测到的干扰噪声的平均值,NEW.第2个PRB上检测到的干扰噪声的平均值,NEW.第3个PRB上检测到的干扰噪声的平均值,NEW.第4个PRB上检测到的干扰噪声的平均值,NEW.第5个PRB上检测到的干扰噪声的平均值,NEW.第6个PRB上检测到的干扰噪声的平均值,NEW.第7个PRB上检测到的干扰噪声的平均值,NEW.第8个PRB上检测到的干扰噪声的平均值,NEW.第9个PRB上检测到的干扰噪声的平均值,
                NEW.第10个PRB上检测到的干扰噪声的平均值,NEW.第11个PRB上检测到的干扰噪声的平均值,NEW.第12个PRB上检测到的干扰噪声的平均值,NEW.第13个PRB上检测到的干扰噪声的平均值,NEW.第14个PRB上检测到的干扰噪声的平均值,NEW.第15个PRB上检测到的干扰噪声的平均值,NEW.第16个PRB上检测到的干扰噪声的平均值,NEW.第17个PRB上检测到的干扰噪声的平均值,NEW.第18个PRB上检测到的干扰噪声的平均值,NEW.第19个PRB上检测到的干扰噪声的平均值,
                NEW.第20个PRB上检测到的干扰噪声的平均值,NEW.第21个PRB上检测到的干扰噪声的平均值,NEW.第22个PRB上检测到的干扰噪声的平均值,NEW.第23个PRB上检测到的干扰噪声的平均值,NEW.第24个PRB上检测到的干扰噪声的平均值,NEW.第25个PRB上检测到的干扰噪声的平均值,NEW.第26个PRB上检测到的干扰噪声的平均值,NEW.第27个PRB上检测到的干扰噪声的平均值,NEW.第28个PRB上检测到的干扰噪声的平均值,NEW.第29个PRB上检测到的干扰噪声的平均值,
                NEW.第30个PRB上检测到的干扰噪声的平均值,NEW.第31个PRB上检测到的干扰噪声的平均值,NEW.第32个PRB上检测到的干扰噪声的平均值,NEW.第33个PRB上检测到的干扰噪声的平均值,NEW.第34个PRB上检测到的干扰噪声的平均值,NEW.第35个PRB上检测到的干扰噪声的平均值,NEW.第36个PRB上检测到的干扰噪声的平均值,NEW.第37个PRB上检测到的干扰噪声的平均值,NEW.第38个PRB上检测到的干扰噪声的平均值,NEW.第39个PRB上检测到的干扰噪声的平均值,
                NEW.第40个PRB上检测到的干扰噪声的平均值,NEW.第41个PRB上检测到的干扰噪声的平均值,NEW.第42个PRB上检测到的干扰噪声的平均值,NEW.第43个PRB上检测到的干扰噪声的平均值,NEW.第44个PRB上检测到的干扰噪声的平均值,NEW.第45个PRB上检测到的干扰噪声的平均值,NEW.第46个PRB上检测到的干扰噪声的平均值,NEW.第47个PRB上检测到的干扰噪声的平均值,NEW.第48个PRB上检测到的干扰噪声的平均值,NEW.第49个PRB上检测到的干扰噪声的平均值,
                NEW.第50个PRB上检测到的干扰噪声的平均值,NEW.第51个PRB上检测到的干扰噪声的平均值,NEW.第52个PRB上检测到的干扰噪声的平均值,NEW.第53个PRB上检测到的干扰噪声的平均值,NEW.第54个PRB上检测到的干扰噪声的平均值,NEW.第55个PRB上检测到的干扰噪声的平均值,NEW.第56个PRB上检测到的干扰噪声的平均值,NEW.第57个PRB上检测到的干扰噪声的平均值,NEW.第58个PRB上检测到的干扰噪声的平均值,NEW.第59个PRB上检测到的干扰噪声的平均值,
                NEW.第60个PRB上检测到的干扰噪声的平均值,NEW.第61个PRB上检测到的干扰噪声的平均值,NEW.第62个PRB上检测到的干扰噪声的平均值,NEW.第63个PRB上检测到的干扰噪声的平均值,NEW.第64个PRB上检测到的干扰噪声的平均值,NEW.第65个PRB上检测到的干扰噪声的平均值,NEW.第66个PRB上检测到的干扰噪声的平均值,NEW.第67个PRB上检测到的干扰噪声的平均值,NEW.第68个PRB上检测到的干扰噪声的平均值,NEW.第69个PRB上检测到的干扰噪声的平均值,
                NEW.第70个PRB上检测到的干扰噪声的平均值,NEW.第71个PRB上检测到的干扰噪声的平均值,NEW.第72个PRB上检测到的干扰噪声的平均值,NEW.第73个PRB上检测到的干扰噪声的平均值,NEW.第74个PRB上检测到的干扰噪声的平均值,NEW.第75个PRB上检测到的干扰噪声的平均值,NEW.第76个PRB上检测到的干扰噪声的平均值,NEW.第77个PRB上检测到的干扰噪声的平均值,NEW.第78个PRB上检测到的干扰噪声的平均值,NEW.第79个PRB上检测到的干扰噪声的平均值,
                NEW.第80个PRB上检测到的干扰噪声的平均值,NEW.第81个PRB上检测到的干扰噪声的平均值,NEW.第82个PRB上检测到的干扰噪声的平均值,NEW.第83个PRB上检测到的干扰噪声的平均值,NEW.第84个PRB上检测到的干扰噪声的平均值,NEW.第85个PRB上检测到的干扰噪声的平均值,NEW.第86个PRB上检测到的干扰噪声的平均值,NEW.第87个PRB上检测到的干扰噪声的平均值,NEW.第88个PRB上检测到的干扰噪声的平均值,NEW.第89个PRB上检测到的干扰噪声的平均值,
                NEW.第90个PRB上检测到的干扰噪声的平均值,NEW.第91个PRB上检测到的干扰噪声的平均值,NEW.第92个PRB上检测到的干扰噪声的平均值,NEW.第93个PRB上检测到的干扰噪声的平均值,NEW.第94个PRB上检测到的干扰噪声的平均值,NEW.第95个PRB上检测到的干扰噪声的平均值,NEW.第96个PRB上检测到的干扰噪声的平均值,NEW.第97个PRB上检测到的干扰噪声的平均值,NEW.第98个PRB上检测到的干扰噪声的平均值,NEW.第99个PRB上检测到的干扰噪声的平均值);
            end if;
        end
        """,
        """
        before insert on tbMRO_tmp for each row
        begin
            if exists(select tbMRO.TimeStamp,tbMRO.ServingSector,tbMRO.InterferingSector,tbMRO.LteScRSRP,tbMRO.LteNcRSRP from tbMRO where tbMRO.TimeStamp=NEW.TimeStamp and tbMRO.ServingSector=NEW.ServingSector 
                            and tbMRO.InterferingSector=NEW.InterferingSector 
                            and tbMRO.LteScRSRP=NEW.LteScRSRP and tbMRO.LteNcRSRP=NEW.LteNcRSRP) then
                update tbMRO set 
                tbMRO.TimeStamp=NEW.TimeStamp,ServingSector=NEW.ServingSector,InterferingSector=NEW.InterferingSector,LteScRSRP=NEW.LteScRSRP,
                LteNcRSRP=NEW.LteNcRSRP,LteNcEarfcn=NEW.LteNcEarfcn,LteNcPci=NEW.LteNcPci
                where tbMRO.TimeStamp=NEW.TimeStamp and tbMRO.ServingSector=NEW.ServingSector 
                            and tbMRO.InterferingSector=NEW.InterferingSector 
                            and tbMRO.LteScRSRP=NEW.LteScRSRP and tbMRO.LteNcRSRP=NEW.LteNcRSRP;
            else 
                insert into tbMRO(TimeStamp,ServingSector,InterferingSector,LteScRSRP,LteNcRSRP,LteNcEarfcn,LteNcPci)
                values(NEW.TimeStamp,NEW.ServingSector,NEW.InterferingSector,NEW.LteScRSRP,NEW.LteNcRSRP,NEW.LteNcEarfcn,NEW.LteNcPci);
            end if;
        end
        """,
        """
        before insert on tbPRBNEW_tmp for each row
        begin
            if exists(select tbPRBNEW.小区描述 from tbPRBNEW where tbPRBNEW.起始时间=NEW.起始时间 and tbPRBNEW.网元或基站名称=NEW.网元或基站名称 
                                                        and tbPRBNEW.小区描述=NEW.小区描述 and tbPRBNEW.小区名称=NEW.小区名称) then
                update tbPRBNEW set
                第0个PRB上检测到的干扰噪声的平均值=NEW.第0个PRB上检测到的干扰噪声的平均值,第1个PRB上检测到的干扰噪声的平均值=NEW.第1个PRB上检测到的干扰噪声的平均值,第2个PRB上检测到的干扰噪声的平均值=NEW.第2个PRB上检测到的干扰噪声的平均值,第3个PRB上检测到的干扰噪声的平均值=NEW.第3个PRB上检测到的干扰噪声的平均值,第4个PRB上检测到的干扰噪声的平均值=NEW.第4个PRB上检测到的干扰噪声的平均值,
                第5个PRB上检测到的干扰噪声的平均值=NEW.第5个PRB上检测到的干扰噪声的平均值,第6个PRB上检测到的干扰噪声的平均值=NEW.第6个PRB上检测到的干扰噪声的平均值,第7个PRB上检测到的干扰噪声的平均值=NEW.第7个PRB上检测到的干扰噪声的平均值,第8个PRB上检测到的干扰噪声的平均值=NEW.第8个PRB上检测到的干扰噪声的平均值,第9个PRB上检测到的干扰噪声的平均值=NEW.第9个PRB上检测到的干扰噪声的平均值,
                第10个PRB上检测到的干扰噪声的平均值=NEW.第10个PRB上检测到的干扰噪声的平均值,第11个PRB上检测到的干扰噪声的平均值=NEW.第11个PRB上检测到的干扰噪声的平均值,第12个PRB上检测到的干扰噪声的平均值=NEW.第12个PRB上检测到的干扰噪声的平均值,第13个PRB上检测到的干扰噪声的平均值=NEW.第13个PRB上检测到的干扰噪声的平均值,第14个PRB上检测到的干扰噪声的平均值=NEW.第14个PRB上检测到的干扰噪声的平均值,
                第15个PRB上检测到的干扰噪声的平均值=NEW.第15个PRB上检测到的干扰噪声的平均值,第16个PRB上检测到的干扰噪声的平均值=NEW.第16个PRB上检测到的干扰噪声的平均值,第17个PRB上检测到的干扰噪声的平均值=NEW.第17个PRB上检测到的干扰噪声的平均值,第18个PRB上检测到的干扰噪声的平均值=NEW.第18个PRB上检测到的干扰噪声的平均值,第19个PRB上检测到的干扰噪声的平均值=NEW.第19个PRB上检测到的干扰噪声的平均值,
                第20个PRB上检测到的干扰噪声的平均值=NEW.第20个PRB上检测到的干扰噪声的平均值,第21个PRB上检测到的干扰噪声的平均值=NEW.第21个PRB上检测到的干扰噪声的平均值,第22个PRB上检测到的干扰噪声的平均值=NEW.第22个PRB上检测到的干扰噪声的平均值,第23个PRB上检测到的干扰噪声的平均值=NEW.第23个PRB上检测到的干扰噪声的平均值,第24个PRB上检测到的干扰噪声的平均值=NEW.第24个PRB上检测到的干扰噪声的平均值,
                第25个PRB上检测到的干扰噪声的平均值=NEW.第25个PRB上检测到的干扰噪声的平均值,第26个PRB上检测到的干扰噪声的平均值=NEW.第26个PRB上检测到的干扰噪声的平均值,第27个PRB上检测到的干扰噪声的平均值=NEW.第27个PRB上检测到的干扰噪声的平均值,第28个PRB上检测到的干扰噪声的平均值=NEW.第28个PRB上检测到的干扰噪声的平均值,第29个PRB上检测到的干扰噪声的平均值=NEW.第29个PRB上检测到的干扰噪声的平均值,
                第30个PRB上检测到的干扰噪声的平均值=NEW.第30个PRB上检测到的干扰噪声的平均值,第31个PRB上检测到的干扰噪声的平均值=NEW.第31个PRB上检测到的干扰噪声的平均值,第32个PRB上检测到的干扰噪声的平均值=NEW.第32个PRB上检测到的干扰噪声的平均值,第33个PRB上检测到的干扰噪声的平均值=NEW.第33个PRB上检测到的干扰噪声的平均值,第34个PRB上检测到的干扰噪声的平均值=NEW.第34个PRB上检测到的干扰噪声的平均值,
                第35个PRB上检测到的干扰噪声的平均值=NEW.第35个PRB上检测到的干扰噪声的平均值,第36个PRB上检测到的干扰噪声的平均值=NEW.第36个PRB上检测到的干扰噪声的平均值,第37个PRB上检测到的干扰噪声的平均值=NEW.第37个PRB上检测到的干扰噪声的平均值,第38个PRB上检测到的干扰噪声的平均值=NEW.第38个PRB上检测到的干扰噪声的平均值,第39个PRB上检测到的干扰噪声的平均值=NEW.第39个PRB上检测到的干扰噪声的平均值,
                第40个PRB上检测到的干扰噪声的平均值=NEW.第40个PRB上检测到的干扰噪声的平均值,第41个PRB上检测到的干扰噪声的平均值=NEW.第41个PRB上检测到的干扰噪声的平均值,第42个PRB上检测到的干扰噪声的平均值=NEW.第42个PRB上检测到的干扰噪声的平均值,第43个PRB上检测到的干扰噪声的平均值=NEW.第43个PRB上检测到的干扰噪声的平均值,第44个PRB上检测到的干扰噪声的平均值=NEW.第44个PRB上检测到的干扰噪声的平均值,
                第45个PRB上检测到的干扰噪声的平均值=NEW.第45个PRB上检测到的干扰噪声的平均值,第46个PRB上检测到的干扰噪声的平均值=NEW.第46个PRB上检测到的干扰噪声的平均值,第47个PRB上检测到的干扰噪声的平均值=NEW.第47个PRB上检测到的干扰噪声的平均值,第48个PRB上检测到的干扰噪声的平均值=NEW.第48个PRB上检测到的干扰噪声的平均值,第49个PRB上检测到的干扰噪声的平均值=NEW.第49个PRB上检测到的干扰噪声的平均值,
                第50个PRB上检测到的干扰噪声的平均值=NEW.第50个PRB上检测到的干扰噪声的平均值,第51个PRB上检测到的干扰噪声的平均值=NEW.第51个PRB上检测到的干扰噪声的平均值,第52个PRB上检测到的干扰噪声的平均值=NEW.第52个PRB上检测到的干扰噪声的平均值,第53个PRB上检测到的干扰噪声的平均值=NEW.第53个PRB上检测到的干扰噪声的平均值,第54个PRB上检测到的干扰噪声的平均值=NEW.第54个PRB上检测到的干扰噪声的平均值,
                第55个PRB上检测到的干扰噪声的平均值=NEW.第55个PRB上检测到的干扰噪声的平均值,第56个PRB上检测到的干扰噪声的平均值=NEW.第56个PRB上检测到的干扰噪声的平均值,第57个PRB上检测到的干扰噪声的平均值=NEW.第57个PRB上检测到的干扰噪声的平均值,第58个PRB上检测到的干扰噪声的平均值=NEW.第58个PRB上检测到的干扰噪声的平均值,第59个PRB上检测到的干扰噪声的平均值=NEW.第59个PRB上检测到的干扰噪声的平均值,
                第60个PRB上检测到的干扰噪声的平均值=NEW.第60个PRB上检测到的干扰噪声的平均值,第61个PRB上检测到的干扰噪声的平均值=NEW.第61个PRB上检测到的干扰噪声的平均值,第62个PRB上检测到的干扰噪声的平均值=NEW.第62个PRB上检测到的干扰噪声的平均值,第63个PRB上检测到的干扰噪声的平均值=NEW.第63个PRB上检测到的干扰噪声的平均值,第64个PRB上检测到的干扰噪声的平均值=NEW.第64个PRB上检测到的干扰噪声的平均值,
                第65个PRB上检测到的干扰噪声的平均值=NEW.第65个PRB上检测到的干扰噪声的平均值,第66个PRB上检测到的干扰噪声的平均值=NEW.第66个PRB上检测到的干扰噪声的平均值,第67个PRB上检测到的干扰噪声的平均值=NEW.第67个PRB上检测到的干扰噪声的平均值,第68个PRB上检测到的干扰噪声的平均值=NEW.第68个PRB上检测到的干扰噪声的平均值,第69个PRB上检测到的干扰噪声的平均值=NEW.第69个PRB上检测到的干扰噪声的平均值,
                第70个PRB上检测到的干扰噪声的平均值=NEW.第70个PRB上检测到的干扰噪声的平均值,第71个PRB上检测到的干扰噪声的平均值=NEW.第71个PRB上检测到的干扰噪声的平均值,第72个PRB上检测到的干扰噪声的平均值=NEW.第72个PRB上检测到的干扰噪声的平均值,第73个PRB上检测到的干扰噪声的平均值=NEW.第73个PRB上检测到的干扰噪声的平均值,第74个PRB上检测到的干扰噪声的平均值=NEW.第74个PRB上检测到的干扰噪声的平均值,
                第75个PRB上检测到的干扰噪声的平均值=NEW.第75个PRB上检测到的干扰噪声的平均值,第76个PRB上检测到的干扰噪声的平均值=NEW.第76个PRB上检测到的干扰噪声的平均值,第77个PRB上检测到的干扰噪声的平均值=NEW.第77个PRB上检测到的干扰噪声的平均值,第78个PRB上检测到的干扰噪声的平均值=NEW.第78个PRB上检测到的干扰噪声的平均值,第79个PRB上检测到的干扰噪声的平均值=NEW.第79个PRB上检测到的干扰噪声的平均值,
                第80个PRB上检测到的干扰噪声的平均值=NEW.第80个PRB上检测到的干扰噪声的平均值,第81个PRB上检测到的干扰噪声的平均值=NEW.第81个PRB上检测到的干扰噪声的平均值,第82个PRB上检测到的干扰噪声的平均值=NEW.第82个PRB上检测到的干扰噪声的平均值,第83个PRB上检测到的干扰噪声的平均值=NEW.第83个PRB上检测到的干扰噪声的平均值,第84个PRB上检测到的干扰噪声的平均值=NEW.第84个PRB上检测到的干扰噪声的平均值,
                第85个PRB上检测到的干扰噪声的平均值=NEW.第85个PRB上检测到的干扰噪声的平均值,第86个PRB上检测到的干扰噪声的平均值=NEW.第86个PRB上检测到的干扰噪声的平均值,第87个PRB上检测到的干扰噪声的平均值=NEW.第87个PRB上检测到的干扰噪声的平均值,第88个PRB上检测到的干扰噪声的平均值=NEW.第88个PRB上检测到的干扰噪声的平均值,第89个PRB上检测到的干扰噪声的平均值=NEW.第89个PRB上检测到的干扰噪声的平均值,
                第90个PRB上检测到的干扰噪声的平均值=NEW.第90个PRB上检测到的干扰噪声的平均值,第91个PRB上检测到的干扰噪声的平均值=NEW.第91个PRB上检测到的干扰噪声的平均值,第92个PRB上检测到的干扰噪声的平均值=NEW.第92个PRB上检测到的干扰噪声的平均值,第93个PRB上检测到的干扰噪声的平均值=NEW.第93个PRB上检测到的干扰噪声的平均值,第94个PRB上检测到的干扰噪声的平均值=NEW.第94个PRB上检测到的干扰噪声的平均值,
                第95个PRB上检测到的干扰噪声的平均值=NEW.第95个PRB上检测到的干扰噪声的平均值,第96个PRB上检测到的干扰噪声的平均值=NEW.第96个PRB上检测到的干扰噪声的平均值,第97个PRB上检测到的干扰噪声的平均值=NEW.第97个PRB上检测到的干扰噪声的平均值,第98个PRB上检测到的干扰噪声的平均值=NEW.第98个PRB上检测到的干扰噪声的平均值,第99个PRB上检测到的干扰噪声的平均值=NEW.第99个PRB上检测到的干扰噪声的平均值
                where tbPRBNEW.起始时间=NEW.起始时间 and tbPRBNEW.网元或基站名称=NEW.网元或基站名称 and tbPRBNEW.小区描述=NEW.小区描述 and tbPRBNEW.小区名称=NEW.小区名称;
            else
                insert into tbPRBNEW(起始时间,网元或基站名称,小区描述,小区名称,
                第0个PRB上检测到的干扰噪声的平均值,第1个PRB上检测到的干扰噪声的平均值,第2个PRB上检测到的干扰噪声的平均值,第3个PRB上检测到的干扰噪声的平均值,第4个PRB上检测到的干扰噪声的平均值,第5个PRB上检测到的干扰噪声的平均值,第6个PRB上检测到的干扰噪声的平均值,第7个PRB上检测到的干扰噪声的平均值,第8个PRB上检测到的干扰噪声的平均值,第9个PRB上检测到的干扰噪声的平均值,
                第10个PRB上检测到的干扰噪声的平均值,第11个PRB上检测到的干扰噪声的平均值,第12个PRB上检测到的干扰噪声的平均值,第13个PRB上检测到的干扰噪声的平均值,第14个PRB上检测到的干扰噪声的平均值,第15个PRB上检测到的干扰噪声的平均值,第16个PRB上检测到的干扰噪声的平均值,第17个PRB上检测到的干扰噪声的平均值,第18个PRB上检测到的干扰噪声的平均值,第19个PRB上检测到的干扰噪声的平均值,
                第20个PRB上检测到的干扰噪声的平均值,第21个PRB上检测到的干扰噪声的平均值,第22个PRB上检测到的干扰噪声的平均值,第23个PRB上检测到的干扰噪声的平均值,第24个PRB上检测到的干扰噪声的平均值,第25个PRB上检测到的干扰噪声的平均值,第26个PRB上检测到的干扰噪声的平均值,第27个PRB上检测到的干扰噪声的平均值,第28个PRB上检测到的干扰噪声的平均值,第29个PRB上检测到的干扰噪声的平均值,
                第30个PRB上检测到的干扰噪声的平均值,第31个PRB上检测到的干扰噪声的平均值,第32个PRB上检测到的干扰噪声的平均值,第33个PRB上检测到的干扰噪声的平均值,第34个PRB上检测到的干扰噪声的平均值,第35个PRB上检测到的干扰噪声的平均值,第36个PRB上检测到的干扰噪声的平均值,第37个PRB上检测到的干扰噪声的平均值,第38个PRB上检测到的干扰噪声的平均值,第39个PRB上检测到的干扰噪声的平均值,
                第40个PRB上检测到的干扰噪声的平均值,第41个PRB上检测到的干扰噪声的平均值,第42个PRB上检测到的干扰噪声的平均值,第43个PRB上检测到的干扰噪声的平均值,第44个PRB上检测到的干扰噪声的平均值,第45个PRB上检测到的干扰噪声的平均值,第46个PRB上检测到的干扰噪声的平均值,第47个PRB上检测到的干扰噪声的平均值,第48个PRB上检测到的干扰噪声的平均值,第49个PRB上检测到的干扰噪声的平均值,
                第50个PRB上检测到的干扰噪声的平均值,第51个PRB上检测到的干扰噪声的平均值,第52个PRB上检测到的干扰噪声的平均值,第53个PRB上检测到的干扰噪声的平均值,第54个PRB上检测到的干扰噪声的平均值,第55个PRB上检测到的干扰噪声的平均值,第56个PRB上检测到的干扰噪声的平均值,第57个PRB上检测到的干扰噪声的平均值,第58个PRB上检测到的干扰噪声的平均值,第59个PRB上检测到的干扰噪声的平均值,
                第60个PRB上检测到的干扰噪声的平均值,第61个PRB上检测到的干扰噪声的平均值,第62个PRB上检测到的干扰噪声的平均值,第63个PRB上检测到的干扰噪声的平均值,第64个PRB上检测到的干扰噪声的平均值,第65个PRB上检测到的干扰噪声的平均值,第66个PRB上检测到的干扰噪声的平均值,第67个PRB上检测到的干扰噪声的平均值,第68个PRB上检测到的干扰噪声的平均值,第69个PRB上检测到的干扰噪声的平均值,
                第70个PRB上检测到的干扰噪声的平均值,第71个PRB上检测到的干扰噪声的平均值,第72个PRB上检测到的干扰噪声的平均值,第73个PRB上检测到的干扰噪声的平均值,第74个PRB上检测到的干扰噪声的平均值,第75个PRB上检测到的干扰噪声的平均值,第76个PRB上检测到的干扰噪声的平均值,第77个PRB上检测到的干扰噪声的平均值,第78个PRB上检测到的干扰噪声的平均值,第79个PRB上检测到的干扰噪声的平均值,
                第80个PRB上检测到的干扰噪声的平均值,第81个PRB上检测到的干扰噪声的平均值,第82个PRB上检测到的干扰噪声的平均值,第83个PRB上检测到的干扰噪声的平均值,第84个PRB上检测到的干扰噪声的平均值,第85个PRB上检测到的干扰噪声的平均值,第86个PRB上检测到的干扰噪声的平均值,第87个PRB上检测到的干扰噪声的平均值,第88个PRB上检测到的干扰噪声的平均值,第89个PRB上检测到的干扰噪声的平均值,
                第90个PRB上检测到的干扰噪声的平均值,第91个PRB上检测到的干扰噪声的平均值,第92个PRB上检测到的干扰噪声的平均值,第93个PRB上检测到的干扰噪声的平均值,第94个PRB上检测到的干扰噪声的平均值,第95个PRB上检测到的干扰噪声的平均值,第96个PRB上检测到的干扰噪声的平均值,第97个PRB上检测到的干扰噪声的平均值,第98个PRB上检测到的干扰噪声的平均值,第99个PRB上检测到的干扰噪声的平均值)
                values(NEW.起始时间,NEW.网元或基站名称,NEW.小区描述,NEW.小区名称,
                NEW.第0个PRB上检测到的干扰噪声的平均值,NEW.第1个PRB上检测到的干扰噪声的平均值,NEW.第2个PRB上检测到的干扰噪声的平均值,NEW.第3个PRB上检测到的干扰噪声的平均值,NEW.第4个PRB上检测到的干扰噪声的平均值,NEW.第5个PRB上检测到的干扰噪声的平均值,NEW.第6个PRB上检测到的干扰噪声的平均值,NEW.第7个PRB上检测到的干扰噪声的平均值,NEW.第8个PRB上检测到的干扰噪声的平均值,NEW.第9个PRB上检测到的干扰噪声的平均值,
                NEW.第10个PRB上检测到的干扰噪声的平均值,NEW.第11个PRB上检测到的干扰噪声的平均值,NEW.第12个PRB上检测到的干扰噪声的平均值,NEW.第13个PRB上检测到的干扰噪声的平均值,NEW.第14个PRB上检测到的干扰噪声的平均值,NEW.第15个PRB上检测到的干扰噪声的平均值,NEW.第16个PRB上检测到的干扰噪声的平均值,NEW.第17个PRB上检测到的干扰噪声的平均值,NEW.第18个PRB上检测到的干扰噪声的平均值,NEW.第19个PRB上检测到的干扰噪声的平均值,
                NEW.第20个PRB上检测到的干扰噪声的平均值,NEW.第21个PRB上检测到的干扰噪声的平均值,NEW.第22个PRB上检测到的干扰噪声的平均值,NEW.第23个PRB上检测到的干扰噪声的平均值,NEW.第24个PRB上检测到的干扰噪声的平均值,NEW.第25个PRB上检测到的干扰噪声的平均值,NEW.第26个PRB上检测到的干扰噪声的平均值,NEW.第27个PRB上检测到的干扰噪声的平均值,NEW.第28个PRB上检测到的干扰噪声的平均值,NEW.第29个PRB上检测到的干扰噪声的平均值,
                NEW.第30个PRB上检测到的干扰噪声的平均值,NEW.第31个PRB上检测到的干扰噪声的平均值,NEW.第32个PRB上检测到的干扰噪声的平均值,NEW.第33个PRB上检测到的干扰噪声的平均值,NEW.第34个PRB上检测到的干扰噪声的平均值,NEW.第35个PRB上检测到的干扰噪声的平均值,NEW.第36个PRB上检测到的干扰噪声的平均值,NEW.第37个PRB上检测到的干扰噪声的平均值,NEW.第38个PRB上检测到的干扰噪声的平均值,NEW.第39个PRB上检测到的干扰噪声的平均值,
                NEW.第40个PRB上检测到的干扰噪声的平均值,NEW.第41个PRB上检测到的干扰噪声的平均值,NEW.第42个PRB上检测到的干扰噪声的平均值,NEW.第43个PRB上检测到的干扰噪声的平均值,NEW.第44个PRB上检测到的干扰噪声的平均值,NEW.第45个PRB上检测到的干扰噪声的平均值,NEW.第46个PRB上检测到的干扰噪声的平均值,NEW.第47个PRB上检测到的干扰噪声的平均值,NEW.第48个PRB上检测到的干扰噪声的平均值,NEW.第49个PRB上检测到的干扰噪声的平均值,
                NEW.第50个PRB上检测到的干扰噪声的平均值,NEW.第51个PRB上检测到的干扰噪声的平均值,NEW.第52个PRB上检测到的干扰噪声的平均值,NEW.第53个PRB上检测到的干扰噪声的平均值,NEW.第54个PRB上检测到的干扰噪声的平均值,NEW.第55个PRB上检测到的干扰噪声的平均值,NEW.第56个PRB上检测到的干扰噪声的平均值,NEW.第57个PRB上检测到的干扰噪声的平均值,NEW.第58个PRB上检测到的干扰噪声的平均值,NEW.第59个PRB上检测到的干扰噪声的平均值,
                NEW.第60个PRB上检测到的干扰噪声的平均值,NEW.第61个PRB上检测到的干扰噪声的平均值,NEW.第62个PRB上检测到的干扰噪声的平均值,NEW.第63个PRB上检测到的干扰噪声的平均值,NEW.第64个PRB上检测到的干扰噪声的平均值,NEW.第65个PRB上检测到的干扰噪声的平均值,NEW.第66个PRB上检测到的干扰噪声的平均值,NEW.第67个PRB上检测到的干扰噪声的平均值,NEW.第68个PRB上检测到的干扰噪声的平均值,NEW.第69个PRB上检测到的干扰噪声的平均值,
                NEW.第70个PRB上检测到的干扰噪声的平均值,NEW.第71个PRB上检测到的干扰噪声的平均值,NEW.第72个PRB上检测到的干扰噪声的平均值,NEW.第73个PRB上检测到的干扰噪声的平均值,NEW.第74个PRB上检测到的干扰噪声的平均值,NEW.第75个PRB上检测到的干扰噪声的平均值,NEW.第76个PRB上检测到的干扰噪声的平均值,NEW.第77个PRB上检测到的干扰噪声的平均值,NEW.第78个PRB上检测到的干扰噪声的平均值,NEW.第79个PRB上检测到的干扰噪声的平均值,
                NEW.第80个PRB上检测到的干扰噪声的平均值,NEW.第81个PRB上检测到的干扰噪声的平均值,NEW.第82个PRB上检测到的干扰噪声的平均值,NEW.第83个PRB上检测到的干扰噪声的平均值,NEW.第84个PRB上检测到的干扰噪声的平均值,NEW.第85个PRB上检测到的干扰噪声的平均值,NEW.第86个PRB上检测到的干扰噪声的平均值,NEW.第87个PRB上检测到的干扰噪声的平均值,NEW.第88个PRB上检测到的干扰噪声的平均值,NEW.第89个PRB上检测到的干扰噪声的平均值,
                NEW.第90个PRB上检测到的干扰噪声的平均值,NEW.第91个PRB上检测到的干扰噪声的平均值,NEW.第92个PRB上检测到的干扰噪声的平均值,NEW.第93个PRB上检测到的干扰噪声的平均值,NEW.第94个PRB上检测到的干扰噪声的平均值,NEW.第95个PRB上检测到的干扰噪声的平均值,NEW.第96个PRB上检测到的干扰噪声的平均值,NEW.第97个PRB上检测到的干扰噪声的平均值,NEW.第98个PRB上检测到的干扰噪声的平均值,NEW.第99个PRB上检测到的干扰噪声的平均值);
            end if;
        end
        """,
        """
        before insert on tbAdminUSER_tmp for each row
        begin
            if exists(select tbAdminUSER.userName from tbAdminUSER where tbAdminUSER.userName=NEW.userName) then
                update tbAdminUSER set
                passWord=NEW.passWord,regTime=NEW.regTime   
                where userName=NEW.userName;
            else
               insert into tbAdminUSER(userName,passWord,regTime)
               values(NEW.userName,NEW.passWord,NEW.regTime);
            end if;
        end
        """,
        """
        -- 创建触发器TR_IMPORT_tbOrdUSER
        before insert on tbOrdUSER_tmp for each row
        begin
            if exists(select tbOrdUSER.userName from tbOrdUSER where tbOrdUSER.userName=NEW.userName) then
                update tbOrdUSER set
                passWord=NEW.passWord,regTime=NEW.regTime   
                where userName=NEW.userName;
            else
               insert into tbOrdUSER(userName,passWord,regTime)
               values(NEW.userName,NEW.passWord,NEW.regTime);
            end if;
        end
        """,
        """
        before insert on tbC2INEW_tmp for each row
        begin
            if exists(select tbC2INEW.ServingSector,tbC2INEW.InterferingSector from tbC2INEW 
                      where tbC2INEW.ServingSector=NEW.ServingSector and tbC2INEW.InterferingSector=NEW.InterferingSector) then
                update tbC2INEW set
                mean=NEW.mean,std=NEW.std,PrbC2I9=NEW.PrbC2I9,PrbABS6=NEW.PrbABS6   
                where ServingSector=NEW.ServingSector and InterferingSector=NEW.InterferingSector;
            else
               insert into tbC2INEW(ServingSector,InterferingSector,mean,std,PrbC2I9,PrbABS6)
               values(NEW.ServingSector,NEW.InterferingSector,NEW.mean,NEW.std,NEW.PrbC2I9,NEW.PrbABS6);
            end if;
        end
        """,
        """
        before insert on tbC2I3_tmp for each row
        begin
            if not exists(select tbC2I3.SectorA,tbC2I3.SectorB,tbC2I3.SectorC from tbC2I3 
                          where tbC2I3.SectorA=NEW.tbC2I3.SectorA and tbC2I3.SectorB=NEW.tbC2I3.SectorB and tbC2I3.SectorC=NEW.tbC2I3.SectorC) then
               insert into tbC2I3(SectorA,SectorB,SectorC)
               values(NEW.SectorA,NEW.SectorB,NEW.SectorC);
            end if;
        end
        """
]
sql_insert = [
        """
        insert into 
        tbCell_tmp(CITY,SECTOR_ID,SECTOR_NAME,ENODEBID,ENODEB_NAME,EARFCN,PCI,PSS,SSS,TAC,VENDOR,LONGITUDE,LATITUDE,STYLE,AZIMUTH,HEIGHT,ELECTTILT,MECHTILT,TOTLETILT) 
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        """
        insert into 
        tbKPI_tmp(起始时间,网元或基站名称,小区,小区名称,RRC连接建立完成次数,RRC连接请求次数,RRC建立成功率qf,
        E_RAB建立成功总次数,E_RAB建立尝试总次数,E_RAB建立成功率2,eNodeB触发的E_RAB异常释放总次数,小区切换出E_RAB异常释放总次数,
        E_RAB掉线率,无线接通率ay,eNodeB发起的S1_RESET导致的UE_Context释放次数,UE_Context异常释放次数,UE_Context建立成功总次数,
        无线掉线率,eNodeB内异频切换出成功次数,eNodeB内异频切换出尝试次数,eNodeB内同频切换出成功次数,eNodeB内同频切换出尝试次数,
        eNodeB间异频切换出成功次数,eNodeB间异频切换出尝试次数,eNodeB间同频切换出成功次数,eNodeB间同频切换出尝试次数,eNB内切换成功率,
        eNB间切换成功率,同频切换成功率zsp,异频切换成功率zsp,切换成功率,小区PDCP层所接收到的上行数据的总吞吐量,小区PDCP层所发送的下行数据的总吞吐量,
        RRC重建请求次数,RRC连接重建比率,通过重建回源小区的eNodeB间同频切换出执行成功次数,通过重建回源小区的eNodeB间异频切换出执行成功次数,
        通过重建回源小区的eNodeB内同频切换出执行成功次数,通过重建回源小区的eNodeB内异频切换出执行成功次数,eNB内切换出成功次数,eNB内切换出请求次数)
        values(%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        """
        insert into
        tbPRB_tmp(起始时间,网元或基站名称,小区描述,小区名称,
        第0个PRB上检测到的干扰噪声的平均值,第1个PRB上检测到的干扰噪声的平均值,第2个PRB上检测到的干扰噪声的平均值,第3个PRB上检测到的干扰噪声的平均值,第4个PRB上检测到的干扰噪声的平均值,第5个PRB上检测到的干扰噪声的平均值,第6个PRB上检测到的干扰噪声的平均值,第7个PRB上检测到的干扰噪声的平均值,第8个PRB上检测到的干扰噪声的平均值,第9个PRB上检测到的干扰噪声的平均值,
        第10个PRB上检测到的干扰噪声的平均值,第11个PRB上检测到的干扰噪声的平均值,第12个PRB上检测到的干扰噪声的平均值,第13个PRB上检测到的干扰噪声的平均值,第14个PRB上检测到的干扰噪声的平均值,第15个PRB上检测到的干扰噪声的平均值,第16个PRB上检测到的干扰噪声的平均值,第17个PRB上检测到的干扰噪声的平均值,第18个PRB上检测到的干扰噪声的平均值,第19个PRB上检测到的干扰噪声的平均值,
        第20个PRB上检测到的干扰噪声的平均值,第21个PRB上检测到的干扰噪声的平均值,第22个PRB上检测到的干扰噪声的平均值,第23个PRB上检测到的干扰噪声的平均值,第24个PRB上检测到的干扰噪声的平均值,第25个PRB上检测到的干扰噪声的平均值,第26个PRB上检测到的干扰噪声的平均值,第27个PRB上检测到的干扰噪声的平均值,第28个PRB上检测到的干扰噪声的平均值,第29个PRB上检测到的干扰噪声的平均值,
        第30个PRB上检测到的干扰噪声的平均值,第31个PRB上检测到的干扰噪声的平均值,第32个PRB上检测到的干扰噪声的平均值,第33个PRB上检测到的干扰噪声的平均值,第34个PRB上检测到的干扰噪声的平均值,第35个PRB上检测到的干扰噪声的平均值,第36个PRB上检测到的干扰噪声的平均值,第37个PRB上检测到的干扰噪声的平均值,第38个PRB上检测到的干扰噪声的平均值,第39个PRB上检测到的干扰噪声的平均值,
        第40个PRB上检测到的干扰噪声的平均值,第41个PRB上检测到的干扰噪声的平均值,第42个PRB上检测到的干扰噪声的平均值,第43个PRB上检测到的干扰噪声的平均值,第44个PRB上检测到的干扰噪声的平均值,第45个PRB上检测到的干扰噪声的平均值,第46个PRB上检测到的干扰噪声的平均值,第47个PRB上检测到的干扰噪声的平均值,第48个PRB上检测到的干扰噪声的平均值,第49个PRB上检测到的干扰噪声的平均值,
        第50个PRB上检测到的干扰噪声的平均值,第51个PRB上检测到的干扰噪声的平均值,第52个PRB上检测到的干扰噪声的平均值,第53个PRB上检测到的干扰噪声的平均值,第54个PRB上检测到的干扰噪声的平均值,第55个PRB上检测到的干扰噪声的平均值,第56个PRB上检测到的干扰噪声的平均值,第57个PRB上检测到的干扰噪声的平均值,第58个PRB上检测到的干扰噪声的平均值,第59个PRB上检测到的干扰噪声的平均值,
        第60个PRB上检测到的干扰噪声的平均值,第61个PRB上检测到的干扰噪声的平均值,第62个PRB上检测到的干扰噪声的平均值,第63个PRB上检测到的干扰噪声的平均值,第64个PRB上检测到的干扰噪声的平均值,第65个PRB上检测到的干扰噪声的平均值,第66个PRB上检测到的干扰噪声的平均值,第67个PRB上检测到的干扰噪声的平均值,第68个PRB上检测到的干扰噪声的平均值,第69个PRB上检测到的干扰噪声的平均值,
        第70个PRB上检测到的干扰噪声的平均值,第71个PRB上检测到的干扰噪声的平均值,第72个PRB上检测到的干扰噪声的平均值,第73个PRB上检测到的干扰噪声的平均值,第74个PRB上检测到的干扰噪声的平均值,第75个PRB上检测到的干扰噪声的平均值,第76个PRB上检测到的干扰噪声的平均值,第77个PRB上检测到的干扰噪声的平均值,第78个PRB上检测到的干扰噪声的平均值,第79个PRB上检测到的干扰噪声的平均值,
        第80个PRB上检测到的干扰噪声的平均值,第81个PRB上检测到的干扰噪声的平均值,第82个PRB上检测到的干扰噪声的平均值,第83个PRB上检测到的干扰噪声的平均值,第84个PRB上检测到的干扰噪声的平均值,第85个PRB上检测到的干扰噪声的平均值,第86个PRB上检测到的干扰噪声的平均值,第87个PRB上检测到的干扰噪声的平均值,第88个PRB上检测到的干扰噪声的平均值,第89个PRB上检测到的干扰噪声的平均值,
        第90个PRB上检测到的干扰噪声的平均值,第91个PRB上检测到的干扰噪声的平均值,第92个PRB上检测到的干扰噪声的平均值,第93个PRB上检测到的干扰噪声的平均值,第94个PRB上检测到的干扰噪声的平均值,第95个PRB上检测到的干扰噪声的平均值,第96个PRB上检测到的干扰噪声的平均值,第97个PRB上检测到的干扰噪声的平均值,第98个PRB上检测到的干扰噪声的平均值,第99个PRB上检测到的干扰噪声的平均值)
        values(%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """,
        """
        insert into 
        tbMRO_tmp(TimeStamp,ServingSector,InterferingSector,LteScRSRP,LteNcRSRP,LteNcEarfcn,LteNcPci)
        values(%s,%s,%s,%s,%s,%s,%s)
        """,
        """
        insert into 
        tbPRBNEW_tmp(起始时间,网元或基站名称,小区描述,小区名称,
        第0个PRB上检测到的干扰噪声的平均值,第1个PRB上检测到的干扰噪声的平均值,第2个PRB上检测到的干扰噪声的平均值,第3个PRB上检测到的干扰噪声的平均值,第4个PRB上检测到的干扰噪声的平均值,第5个PRB上检测到的干扰噪声的平均值,第6个PRB上检测到的干扰噪声的平均值,第7个PRB上检测到的干扰噪声的平均值,第8个PRB上检测到的干扰噪声的平均值,第9个PRB上检测到的干扰噪声的平均值,
        第10个PRB上检测到的干扰噪声的平均值,第11个PRB上检测到的干扰噪声的平均值,第12个PRB上检测到的干扰噪声的平均值,第13个PRB上检测到的干扰噪声的平均值,第14个PRB上检测到的干扰噪声的平均值,第15个PRB上检测到的干扰噪声的平均值,第16个PRB上检测到的干扰噪声的平均值,第17个PRB上检测到的干扰噪声的平均值,第18个PRB上检测到的干扰噪声的平均值,第19个PRB上检测到的干扰噪声的平均值,
        第20个PRB上检测到的干扰噪声的平均值,第21个PRB上检测到的干扰噪声的平均值,第22个PRB上检测到的干扰噪声的平均值,第23个PRB上检测到的干扰噪声的平均值,第24个PRB上检测到的干扰噪声的平均值,第25个PRB上检测到的干扰噪声的平均值,第26个PRB上检测到的干扰噪声的平均值,第27个PRB上检测到的干扰噪声的平均值,第28个PRB上检测到的干扰噪声的平均值,第29个PRB上检测到的干扰噪声的平均值,
        第30个PRB上检测到的干扰噪声的平均值,第31个PRB上检测到的干扰噪声的平均值,第32个PRB上检测到的干扰噪声的平均值,第33个PRB上检测到的干扰噪声的平均值,第34个PRB上检测到的干扰噪声的平均值,第35个PRB上检测到的干扰噪声的平均值,第36个PRB上检测到的干扰噪声的平均值,第37个PRB上检测到的干扰噪声的平均值,第38个PRB上检测到的干扰噪声的平均值,第39个PRB上检测到的干扰噪声的平均值,
        第40个PRB上检测到的干扰噪声的平均值,第41个PRB上检测到的干扰噪声的平均值,第42个PRB上检测到的干扰噪声的平均值,第43个PRB上检测到的干扰噪声的平均值,第44个PRB上检测到的干扰噪声的平均值,第45个PRB上检测到的干扰噪声的平均值,第46个PRB上检测到的干扰噪声的平均值,第47个PRB上检测到的干扰噪声的平均值,第48个PRB上检测到的干扰噪声的平均值,第49个PRB上检测到的干扰噪声的平均值,
        第50个PRB上检测到的干扰噪声的平均值,第51个PRB上检测到的干扰噪声的平均值,第52个PRB上检测到的干扰噪声的平均值,第53个PRB上检测到的干扰噪声的平均值,第54个PRB上检测到的干扰噪声的平均值,第55个PRB上检测到的干扰噪声的平均值,第56个PRB上检测到的干扰噪声的平均值,第57个PRB上检测到的干扰噪声的平均值,第58个PRB上检测到的干扰噪声的平均值,第59个PRB上检测到的干扰噪声的平均值,
        第60个PRB上检测到的干扰噪声的平均值,第61个PRB上检测到的干扰噪声的平均值,第62个PRB上检测到的干扰噪声的平均值,第63个PRB上检测到的干扰噪声的平均值,第64个PRB上检测到的干扰噪声的平均值,第65个PRB上检测到的干扰噪声的平均值,第66个PRB上检测到的干扰噪声的平均值,第67个PRB上检测到的干扰噪声的平均值,第68个PRB上检测到的干扰噪声的平均值,第69个PRB上检测到的干扰噪声的平均值,
        第70个PRB上检测到的干扰噪声的平均值,第71个PRB上检测到的干扰噪声的平均值,第72个PRB上检测到的干扰噪声的平均值,第73个PRB上检测到的干扰噪声的平均值,第74个PRB上检测到的干扰噪声的平均值,第75个PRB上检测到的干扰噪声的平均值,第76个PRB上检测到的干扰噪声的平均值,第77个PRB上检测到的干扰噪声的平均值,第78个PRB上检测到的干扰噪声的平均值,第79个PRB上检测到的干扰噪声的平均值,
        第80个PRB上检测到的干扰噪声的平均值,第81个PRB上检测到的干扰噪声的平均值,第82个PRB上检测到的干扰噪声的平均值,第83个PRB上检测到的干扰噪声的平均值,第84个PRB上检测到的干扰噪声的平均值,第85个PRB上检测到的干扰噪声的平均值,第86个PRB上检测到的干扰噪声的平均值,第87个PRB上检测到的干扰噪声的平均值,第88个PRB上检测到的干扰噪声的平均值,第89个PRB上检测到的干扰噪声的平均值,
        第90个PRB上检测到的干扰噪声的平均值,第91个PRB上检测到的干扰噪声的平均值,第92个PRB上检测到的干扰噪声的平均值,第93个PRB上检测到的干扰噪声的平均值,第94个PRB上检测到的干扰噪声的平均值,第95个PRB上检测到的干扰噪声的平均值,第96个PRB上检测到的干扰噪声的平均值,第97个PRB上检测到的干扰噪声的平均值,第98个PRB上检测到的干扰噪声的平均值,第99个PRB上检测到的干扰噪声的平均值)
        select 起始时间,网元或基站名称,小区描述,小区名称,
        AVG(第0个PRB上检测到的干扰噪声的平均值),AVG(第1个PRB上检测到的干扰噪声的平均值),AVG(第2个PRB上检测到的干扰噪声的平均值),AVG(第3个PRB上检测到的干扰噪声的平均值),AVG(第4个PRB上检测到的干扰噪声的平均值),AVG(第5个PRB上检测到的干扰噪声的平均值),AVG(第6个PRB上检测到的干扰噪声的平均值),AVG(第7个PRB上检测到的干扰噪声的平均值),AVG(第8个PRB上检测到的干扰噪声的平均值),AVG(第9个PRB上检测到的干扰噪声的平均值),
        AVG(第10个PRB上检测到的干扰噪声的平均值),AVG(第11个PRB上检测到的干扰噪声的平均值),AVG(第12个PRB上检测到的干扰噪声的平均值),AVG(第13个PRB上检测到的干扰噪声的平均值),AVG(第14个PRB上检测到的干扰噪声的平均值),AVG(第15个PRB上检测到的干扰噪声的平均值),AVG(第16个PRB上检测到的干扰噪声的平均值),AVG(第17个PRB上检测到的干扰噪声的平均值),AVG(第18个PRB上检测到的干扰噪声的平均值),AVG(第19个PRB上检测到的干扰噪声的平均值),
        AVG(第20个PRB上检测到的干扰噪声的平均值),AVG(第21个PRB上检测到的干扰噪声的平均值),AVG(第22个PRB上检测到的干扰噪声的平均值),AVG(第23个PRB上检测到的干扰噪声的平均值),AVG(第24个PRB上检测到的干扰噪声的平均值),AVG(第25个PRB上检测到的干扰噪声的平均值),AVG(第26个PRB上检测到的干扰噪声的平均值),AVG(第27个PRB上检测到的干扰噪声的平均值),AVG(第28个PRB上检测到的干扰噪声的平均值),AVG(第29个PRB上检测到的干扰噪声的平均值),
        AVG(第30个PRB上检测到的干扰噪声的平均值),AVG(第31个PRB上检测到的干扰噪声的平均值),AVG(第32个PRB上检测到的干扰噪声的平均值),AVG(第33个PRB上检测到的干扰噪声的平均值),AVG(第34个PRB上检测到的干扰噪声的平均值),AVG(第35个PRB上检测到的干扰噪声的平均值),AVG(第36个PRB上检测到的干扰噪声的平均值),AVG(第37个PRB上检测到的干扰噪声的平均值),AVG(第38个PRB上检测到的干扰噪声的平均值),AVG(第39个PRB上检测到的干扰噪声的平均值),
        AVG(第40个PRB上检测到的干扰噪声的平均值),AVG(第41个PRB上检测到的干扰噪声的平均值),AVG(第42个PRB上检测到的干扰噪声的平均值),AVG(第43个PRB上检测到的干扰噪声的平均值),AVG(第44个PRB上检测到的干扰噪声的平均值),AVG(第45个PRB上检测到的干扰噪声的平均值),AVG(第46个PRB上检测到的干扰噪声的平均值),AVG(第47个PRB上检测到的干扰噪声的平均值),AVG(第48个PRB上检测到的干扰噪声的平均值),AVG(第49个PRB上检测到的干扰噪声的平均值),
        AVG(第50个PRB上检测到的干扰噪声的平均值),AVG(第51个PRB上检测到的干扰噪声的平均值),AVG(第52个PRB上检测到的干扰噪声的平均值),AVG(第53个PRB上检测到的干扰噪声的平均值),AVG(第54个PRB上检测到的干扰噪声的平均值),AVG(第55个PRB上检测到的干扰噪声的平均值),AVG(第56个PRB上检测到的干扰噪声的平均值),AVG(第57个PRB上检测到的干扰噪声的平均值),AVG(第58个PRB上检测到的干扰噪声的平均值),AVG(第59个PRB上检测到的干扰噪声的平均值),
        AVG(第60个PRB上检测到的干扰噪声的平均值),AVG(第61个PRB上检测到的干扰噪声的平均值),AVG(第62个PRB上检测到的干扰噪声的平均值),AVG(第63个PRB上检测到的干扰噪声的平均值),AVG(第64个PRB上检测到的干扰噪声的平均值),AVG(第65个PRB上检测到的干扰噪声的平均值),AVG(第66个PRB上检测到的干扰噪声的平均值),AVG(第67个PRB上检测到的干扰噪声的平均值),AVG(第68个PRB上检测到的干扰噪声的平均值),AVG(第69个PRB上检测到的干扰噪声的平均值),
        AVG(第70个PRB上检测到的干扰噪声的平均值),AVG(第71个PRB上检测到的干扰噪声的平均值),AVG(第72个PRB上检测到的干扰噪声的平均值),AVG(第73个PRB上检测到的干扰噪声的平均值),AVG(第74个PRB上检测到的干扰噪声的平均值),AVG(第75个PRB上检测到的干扰噪声的平均值),AVG(第76个PRB上检测到的干扰噪声的平均值),AVG(第77个PRB上检测到的干扰噪声的平均值),AVG(第78个PRB上检测到的干扰噪声的平均值),AVG(第79个PRB上检测到的干扰噪声的平均值),
        AVG(第80个PRB上检测到的干扰噪声的平均值),AVG(第81个PRB上检测到的干扰噪声的平均值),AVG(第82个PRB上检测到的干扰噪声的平均值),AVG(第83个PRB上检测到的干扰噪声的平均值),AVG(第84个PRB上检测到的干扰噪声的平均值),AVG(第85个PRB上检测到的干扰噪声的平均值),AVG(第86个PRB上检测到的干扰噪声的平均值),AVG(第87个PRB上检测到的干扰噪声的平均值),AVG(第88个PRB上检测到的干扰噪声的平均值),AVG(第89个PRB上检测到的干扰噪声的平均值),
        AVG(第90个PRB上检测到的干扰噪声的平均值),AVG(第91个PRB上检测到的干扰噪声的平均值),AVG(第92个PRB上检测到的干扰噪声的平均值),AVG(第93个PRB上检测到的干扰噪声的平均值),AVG(第94个PRB上检测到的干扰噪声的平均值),AVG(第95个PRB上检测到的干扰噪声的平均值),AVG(第96个PRB上检测到的干扰噪声的平均值),AVG(第97个PRB上检测到的干扰噪声的平均值),AVG(第98个PRB上检测到的干扰噪声的平均值),AVG(第99个PRB上检测到的干扰噪声的平均值)
        from tbPRB group by DATE_FORMAT(起始时间,'%Y%m%d%H'),小区名称;
        """,
        """
        insert into tbC2INEW_tmp(ServingSector,InterferingSector,mean,std,PrbC2I9,PrbABS6)
         values(%s,%s,%s,%s,%s,%s)
        """
]


