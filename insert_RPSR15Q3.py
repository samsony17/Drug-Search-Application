
import csv
from pymongo import MongoClient 

RPSR15Q3Array = []
conn = MongoClient()
# connecting to MongoDB and creating a database

with open("F:/Spring 16/CSE 5320/Project/Data file/faers_ascii_2015q3/RPSR15Q3.txt", 'r') as i:
    for RPSR15Q3Row in csv.reader(i, delimiter='$'):
        RPSR15Q3Array.append(RPSR15Q3Row)

db = conn.drugdb
RPSR15Q3Collection = db.RPSR15Q3

j = 0
m = 0
for RPSR15Q3Row in RPSR15Q3Array[1:]:
    dbInsert = {}
    if(RPSR15Q3Row[0]!=''):
        dbInsert['PRIMARYID'] = str(RPSR15Q3Row[0])
    if(RPSR15Q3Row[1]!=''):
        dbInsert['CASEID'] = str(RPSR15Q3Row[1])
    if(RPSR15Q3Row[2]!=''):
        dbInsert['RPSR_COD'] = str(RPSR15Q3Row[2])
        RPSR15Q3Collection.insert(dbInsert)
    print dbInsert
#print(db.RPSR15Q3.find({PRIMARY_ID: ""}))
