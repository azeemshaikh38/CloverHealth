import csv

class FormatFile:
    
    def __init__(self, path):
        self.specFormat = []
        with open(path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                self.specFormat.append(row)
        self.specFormat.pop(0)

    def getFormat(self):
        return self.specFormat 

    def getCols(self):
        return [col[0] for col in self.specFormat]                   
