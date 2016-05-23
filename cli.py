import os
from FileNames import FileNames
from FormatFile import FormatFile
from DataFile import DataFile
from Query import Query
from Db import Db

dataFolder = "data"
specFolder = "specs"

db = Db()
q = Query()

for filename in os.listdir(dataFolder):
    name = FileNames(filename)
    spec = FormatFile(specFolder+"/"+name.specFileName)
    data = DataFile(dataFolder+"/"+filename, spec.getFormat())
    for row in data.getData():
        query, params = q.insert_query(name.tableName, spec.getCols(), row)
        print(query, params)
<<<<<<< HEAD
        db.insert(query, params) 
=======
        #db.insert(query, params) 
>>>>>>> v1
