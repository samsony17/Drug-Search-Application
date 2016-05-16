import xml.etree.ElementTree as ET
from pymongo import MongoClient


conn = MongoClient()
# connecting to MongoDB and creating a database


db = conn.drugdb
Coll = db.XML



tree = ET.parse(
    "F:/Spring 16/CSE 5320/Project/Data file/National Drug File/NDFRT_Public_2014.07.07_TDE.xml")
root = tree.getroot()



i = 0
concept = {}
print("Data from file NDFRT_Public_2014.07.07_TDE.xml\n")

for conceptdef in root.findall('conceptDef'):
    concept = {}
    name = conceptdef.find('name').text
    code = conceptdef.find('code').text
    idval = int(conceptdef.find('id').text)
    concept['name'] = name
    concept['code'] = code
    concept['id'] = idval
    y = {}
    for defcon in conceptdef.findall("definingConcepts"):
        d = defcon.find('concept')
        if d:
         concept['concept'] = defcon.find('concept').text
    print(concept)
Coll.insert(concept)
