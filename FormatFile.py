import csv
import logging
from Commons import Commons

logger = logging.getLogger('FormatFile')
logging.basicConfig(filename=Commons.LOG_FILE, level=Commons.LOGGER_LEVEL, format=Commons.LOGGER_FORMAT)

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
