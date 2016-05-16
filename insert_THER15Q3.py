
import csv
from pymongo import MongoClient 

THER15Q3Array = []
conn = MongoClient()
# connecting to MongoDB and creating a database

with open("F:/Spring 16/CSE 5320/Project/Data file/faers_ascii_2015q3/THER15Q3.txt", 'r') as i:
    for THER15Q3Row in csv.reader(i, delimiter='$'):
        THER15Q3Array.append(THER15Q3Row)

db = conn.drugdb
THER15Q3Collection = db.THER15Q3

j = 0
m = 0
for THER15Q3Row in THER15Q3Array[1:]:
    dbInsert = {}
    if(THER15Q3Row[0]!=''):
        dbInsert['PRIMARYID'] = str(THER15Q3Row[0])
    if(THER15Q3Row[1]!=''):
        dbInsert['CASEID'] = str(THER15Q3Row[1])
    if(THER15Q3Row[2]!=''):
        dbInsert['DSG_DRUG_SEQ'] = str(THER15Q3Row[2])
    if(THER15Q3Row[3]!=''):
        dbInsert['START_DT'] = str(THER15Q3Row[3])
    if(THER15Q3Row[4]!=''):
        dbInsert['END_DT'] = str(THER15Q3Row[4])
    if(THER15Q3Row[5]!=''):
        dbInsert['DUR'] = str(THER15Q3Row[5])
    if(THER15Q3Row[6]!=''):
        dbInsert['DUR_COD'] = str(THER15Q3Row[6])
    
    THER15Q3Collection.insert(dbInsert)
    print dbInsert
#print(db.THER15Q3.find({PRIMARY_ID: ""}))
