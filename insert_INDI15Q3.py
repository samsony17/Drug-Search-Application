
import csv
from pymongo import MongoClient

INDI15Q3Array = []
conn = MongoClient()
# connecting to MongoDB and creating a database

with open("F:/Spring 16/CSE 5320/Project/Data file/faers_ascii_2015q3/INDI15Q3.txt", 'r') as i:
    for INDI15Q3Row in csv.reader(i, delimiter='$'):
        INDI15Q3Array.append(INDI15Q3Row)

db = conn.drugdb
INDI15Q3Collection = db.INDI15Q3

j = 0
m = 0
for INDI15Q3Row in INDI15Q3Array[1:]:
    dbInsert = {}
    if(INDI15Q3Row[0]!=''):
        dbInsert['PRIMARYID'] = str(INDI15Q3Row[0])
    if(INDI15Q3Row[1]!=''):
        dbInsert['CASEID'] = str(INDI15Q3Row[1])
    if(INDI15Q3Row[2]!=''):
        dbInsert['INDI_DRUG_SEQ'] = str(INDI15Q3Row[2])
    if(INDI15Q3Row[3]!=''):
        dbInsert['INDI_PT'] = str(INDI15Q3Row[3])
        INDI15Q3Collection.insert(dbInsert)
    print dbInsert
#print(db.INDI15Q3.find({PRIMARY_ID: ""}))
