
import csv
from pymongo import MongoClient 

REAC15Q3Array = []
conn = MongoClient()
# connecting to MongoDB and creating a database

with open("F:/Spring 16/CSE 5320/Project/Data file/faers_ascii_2015q3/REAC15Q3.txt", 'r') as i:
    for REAC15Q3Row in csv.reader(i, delimiter='$'):
        REAC15Q3Array.append(REAC15Q3Row)

db = conn.drugdb
REAC15Q3Collection = db.REAC15Q3

j = 0
m = 0
for REAC15Q3Row in REAC15Q3Array[1:]:
    dbInsert = {}
    if(REAC15Q3Row[0]!=''):
        dbInsert['PRIMARYID'] = str(REAC15Q3Row[0])
    if(REAC15Q3Row[1]!=''):
        dbInsert['CASEID'] = str(REAC15Q3Row[1])
    if(REAC15Q3Row[2]!=''):
        dbInsert['PT'] = str(REAC15Q3Row[2])
    if(REAC15Q3Row[3]!=''):
        dbInsert['DRUG_REC_ACT'] = str(REAC15Q3Row[3])
        REAC15Q3Collection.insert(dbInsert)
    print dbInsert
#print(db.REAC15Q3.find({PRIMARY_ID: ""}))
