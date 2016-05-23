import re
<<<<<<< HEAD
import logging 
from Commons import Commons

logger = logging.getLogger('DataFile')
logging.basicConfig(filename=Commons.LOG_FILE, level=Commons.LOGGER_LEVEL, format=Commons.LOGGER_FORMAT)
=======
>>>>>>> v1

class DataFile:
    
    def __init__(self, path, spec):
        self.data = self.parseData(path, spec)
        self.spec = spec

    def parseData(self, path, spec):
        ret = []
        regex_pattern = "".join(['(.{%s})'%i[1] for i in spec])
        f = open(path, 'r')
        for line in f:
            line = line.strip()
            l_vals = []
            m = re.search(regex_pattern, line)
            for col in range(len(spec)):
                l_vals.append(self.parse(m.group(col+1), spec[col][2]))
            ret.append(l_vals)
        return ret
   
    def parse(self, col_val, col_type):
        if col_type=='TEXT':
            return self.parse_text(col_val)
        elif col_type=='BOOLEAN':
            return self.parse_bool(col_val)
        elif col_type=='INTEGER':
            return self.parse_int(col_val)
        raise Exception("Unrecognized column type {}".format(col_type))

    def parse_text(self, val):
        return str(val)

    def parse_bool(self, val):
        return bool(val)

    def parse_int(self, val):
        return int(val)

    def getData(self):
        return self.data
