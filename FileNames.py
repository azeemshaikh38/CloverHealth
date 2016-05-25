import re
from dateutil import parser
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> v2
import logging
from Commons import Commons

logger = logging.getLogger('FileNames')
logging.basicConfig(filename=Commons.LOG_FILE, level=Commons.LOGGER_LEVEL, format=Commons.LOGGER_FORMAT)
<<<<<<< HEAD
=======
>>>>>>> v1
=======
>>>>>>> v2

class FileNames:

    def __init__(self, dataFileName):
        self.dataFileName = dataFileName
        self.tableName, self.specFileName, self.Date = self.parseFileName(dataFileName)

    def getSpecFileName(self):
        return self.specFileName 

    def getFileDate(self):
        return self.Date

    def parseFileName(self, filename):
        filename = re.sub('\.txt$', '', filename)
        m = re.search('(.*)_(\d\d\d\d-\d\d-\d\d)$', filename)
        return m.group(1), m.group(1)+".csv", parser.parse(m.group(2))
