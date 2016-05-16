
import csv
from pymongo import MongoClient 

DRUG15Q3Array = []
conn = MongoClient()
# connecting to MongoDB and creating a database

with open("F:/Spring 16/CSE 5320/Project/Data file/faers_ascii_2015q3/DRUG15Q3.txt", 'r') as i:
    for DRUG15Q3Row in csv.reader(i, delimiter='$'):
        DRUG15Q3Array.append(DRUG15Q3Row)

db = conn.drugdb
DRUG15Q3Collection = db.DRUG15Q3

j = 0
m = 0
for DRUG15Q3Row in DRUG15Q3Array[1:]:
        dbInsert = {}
	if(DRUG15Q3Row[0]!=''):
        	dbInsert['PRIMARYID'] = str(DRUG15Q3Row[0])
	if(DRUG15Q3Row[1]!=''):
        	dbInsert['CASEID'] = str(DRUG15Q3Row[1])
	if(DRUG15Q3Row[2]!=''):
        	dbInsert['DRUG_SEQ'] = str(DRUG15Q3Row[2])
	if(DRUG15Q3Row[3]!=''):
        	dbInsert['ROLE_COD'] = str(DRUG15Q3Row[3])
	if(DRUG15Q3Row[4]!=''):
        	dbInsert['DRUGNAME'] = str(DRUG15Q3Row[4])
	if(DRUG15Q3Row[5]!=''):
        	dbInsert['PROD_AI'] = str(DRUG15Q3Row[5])
	if(DRUG15Q3Row[6]!=''):
        	dbInsert['VAL_VBM'] = str(DRUG15Q3Row[6])
	if(DRUG15Q3Row[7]!=''):
        	dbInsert['ROUTE'] = str(DRUG15Q3Row[7])
	if(DRUG15Q3Row[8]!=''):
        	dbInsert['DOSE_VBM'] = str(DRUG15Q3Row[8])
	if(DRUG15Q3Row[9]!=''):
        	dbInsert['CUM_DOSE_CHR'] = str(DRUG15Q3Row[9])
	if(DRUG15Q3Row[10]!=''):
        	dbInsert['CUM_DOSE_UNIT'] = str(DRUG15Q3Row[10])
	if(DRUG15Q3Row[11]!=''):
        	dbInsert['DECHAL'] = str(DRUG15Q3Row[11])
	if(DRUG15Q3Row[12]!=''):
        	dbInsert['RECHAL'] = str(DRUG15Q3Row[12])
	if(DRUG15Q3Row[13]!=''):
        	dbInsert['LOT_NUM'] = str(DRUG15Q3Row[13])
	if(DRUG15Q3Row[14]!=''):
        	dbInsert['EXP_DT'] = str(DRUG15Q3Row[14])
	if(DRUG15Q3Row[15]!=''):
        	dbInsert['NDA_NUM'] = str(DRUG15Q3Row[15])
	if(DRUG15Q3Row[16]!=''):
        	dbInsert['DOSE_AMT'] = str(DRUG15Q3Row[16])
	if(DRUG15Q3Row[17]!=''):
        	dbInsert['DOSE_UNIT'] = str(DRUG15Q3Row[17])
	if(DRUG15Q3Row[18]!=''):
        	dbInsert['DOSE_FORM'] = str(DRUG15Q3Row[18])
	if(DRUG15Q3Row[19]!=''):
        	dbInsert['DOSE_FREQ'] = str(DRUG15Q3Row[19])

        DRUG15Q3Collection.insert(dbInsert)
	print dbInsert
print(db.DRUG15Q3.count())
