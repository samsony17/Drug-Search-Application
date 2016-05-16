
import csv
from pymongo import MongoClient 

DEMO15Q3Array = []

conn = MongoClient()
# connecting to MongoDB and creating a database

with open("F:/Spring 16/CSE 5320/Project/Data file/faers_ascii_2015q3/DEMO15Q3.txt", 'r') as i:
    for DEMO15Q3Row in csv.reader(i, delimiter='$'):
        DEMO15Q3Array.append(DEMO15Q3Row)

db = conn.drugdb
DEMO15Q3Collection = db.DEMO15Q3

j = 0
m = 0
#import pdb
#pdb.set_trace()
for DEMO15Q3Row in DEMO15Q3Array[1:]:
    dbInsert = {}
    if(DEMO15Q3Row[0]!=''):
    	dbInsert['PRIMARYID'] = str(DEMO15Q3Row[0])
    if(DEMO15Q3Row[1]!=''):
    	dbInsert['CASEID'] = str(DEMO15Q3Row[1])
    if(DEMO15Q3Row[2]!=''):
    	dbInsert['CASEVERSION'] = str(DEMO15Q3Row[2])
    if(DEMO15Q3Row[3]!=''):
    	dbInsert['I_F_CODE'] = str(DEMO15Q3Row[3])
    if(DEMO15Q3Row[4]!=''):
    	dbInsert['EVENT_DT'] = str(DEMO15Q3Row[4])
    if(DEMO15Q3Row[5]!=''):
    	dbInsert['MFR_DT'] = str(DEMO15Q3Row[5])
    if(DEMO15Q3Row[6]!=''):
    	dbInsert['INIT_FDA_DT'] = str(DEMO15Q3Row[6])
    if(DEMO15Q3Row[7]!=''):
    	dbInsert['FDA_DT'] = str(DEMO15Q3Row[7])
    if(DEMO15Q3Row[8]!=''):
    	dbInsert['REPT_COD'] = str(DEMO15Q3Row[8])
    if(DEMO15Q3Row[9]!=''):
    	dbInsert['MFR_NUM'] = str(DEMO15Q3Row[9])
    if(DEMO15Q3Row[10]!=''):
    	dbInsert['MFR_SNDR'] = str(DEMO15Q3Row[10])
    if(DEMO15Q3Row[11]!=''):
    	dbInsert['LIT_REF'] = str(DEMO15Q3Row[11])
    if(DEMO15Q3Row[12]!=''):
    	dbInsert['AGE'] = str(DEMO15Q3Row[12])
    if(DEMO15Q3Row[13]!=''):
    	dbInsert['AGE_COD'] = str(DEMO15Q3Row[13])
    if(DEMO15Q3Row[14]!=''):
    	dbInsert['AGE_GRP'] = str(DEMO15Q3Row[14])
    if(DEMO15Q3Row[15]!=''):
    	dbInsert['SEX'] = str(DEMO15Q3Row[15])
    if(DEMO15Q3Row[16]!=''):
    	dbInsert['E_SUB'] = str(DEMO15Q3Row[16])
    if(DEMO15Q3Row[17]!=''):
    	dbInsert['WT'] = str(DEMO15Q3Row[17])
    if(DEMO15Q3Row[18]!=''):
    	dbInsert['WT_COD'] = str(DEMO15Q3Row[18])
    if(DEMO15Q3Row[19]!=''):
    	dbInsert['REPT_DT'] = str(DEMO15Q3Row[19])
    if(DEMO15Q3Row[20]!=''):
    	dbInsert['TO_MFR'] = str(DEMO15Q3Row[20])
    if(DEMO15Q3Row[21]!=''):
    	dbInsert['OCCP__COD'] = str(DEMO15Q3Row[21])
    if(DEMO15Q3Row[22]!=''):
    	dbInsert['REPORTER_COUNTRY'] = str(DEMO15Q3Row[22])
    if(DEMO15Q3Row[23]!=''):
    	dbInsert['OCCR_COUNTRY'] = str(DEMO15Q3Row[23])
 
    
    DEMO15Q3Collection.insert(dbInsert)
    print dbInsert

print(db.DEMO15Q3.count())
