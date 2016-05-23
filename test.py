from FileNames import FileNames
from FormatFile import FormatFile
from DataFile import DataFile
from Query import Query

dataFolder = "data"
specFolder = "specs"

specFile = "testformat1.csv"
dataFile = "testformat1_2015-06-28.txt"

specPath = specFolder+"/"+specFile 
dataPath = dataFolder+"/"+dataFile

name = FileNames(dataFile)
print(name.dataFileName, name.specFileName, name.Date)

spec = FormatFile(specFolder+"/"+name.specFileName)
print(spec.getFormat())

data = DataFile(dataPath, spec.getFormat())
print(data.data)

q = Query()
for row in data.data:
    print(q.insert_query(name.tableName, [col[0] for col in spec.getFormat()], row))
