# -*- coding: utf-8 -*-
import pandas as pd

# tbC2I
csv_data = pd.read_csv('data/tbC2I.csv',
                       encoding='utf-8',
                       usecols=['SCELL', 'NCELL', 'C2I_Mean'])
with open('data/tbC2I.txt', "a+", encoding='utf-8') as f:
    for index, row in csv_data.iterrows():
        f.write(row['SCELL'] + " " + row['NCELL'] + " " + str(row['C2I_Mean']) +
                "\n")

# tbCell
csv_data = pd.read_csv('data/tbCell.csv',
                       encoding='utf-8',
                       usecols=['SECTOR_ID', 'LONGITUDE', 'LATITUDE'])
coordinate_dict = {}
for index, row in csv_data.iterrows():
    coordinate_dict[str(row['SECTOR_ID'])] = [row['LONGITUDE'], row['LATITUDE']]
with open('data/coordinate.txt', "a+", encoding='utf-8') as f:
    f.write(str(coordinate_dict))
