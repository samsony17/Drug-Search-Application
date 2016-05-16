
import csv
from pymongo import MongoClient 

OUTC15Q3Array = []
conn = MongoClient()
# connecting to MongoDB and creating a database

with open("F:/Spring 16/CSE 5320/Project/Data file/faers_ascii_2015q3/OUTC15Q3.txt", 'r') as i:
    for OUTC15Q3Row in csv.reader(i, delimiter='$'):
        OUTC15Q3Array.append(OUTC15Q3Row)

db = conn.drugdb
OUTC15Q3Collection = db.OUTC15Q3

j = 0
m = 0
for OUTC15Q3Row in OUTC15Q3Array[1:]:
    dbInsert = {}
    if(OUTC15Q3Row[0]!=''):
        dbInsert['PRIMARYID'] = str(OUTC15Q3Row[0])
    if(OUTC15Q3Row[1]!=''):
        dbInsert['CASEID'] = str(OUTC15Q3Row[1])
    if(OUTC15Q3Row[2]!=''):
        dbInsert['OUTC_COD'] = str(OUTC15Q3Row[2])
        OUTC15Q3Collection.insert(dbInsert)
    print dbInsert
#print(db.OUTC15Q3.find({PRIMARY_ID: ""}))
