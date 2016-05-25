import MySQLdb
from Credentials import Credentials
import logging
from Commons import Commons

logger = logging.getLogger('Db')
logging.basicConfig(filename=Commons.LOG_FILE, level=Commons.LOGGER_LEVEL, format=Commons.LOGGER_FORMAT)

class Db:

    def __init__(self):
        self.conn = MySQLdb.connect(user=Credentials.DB_USER, passwd=Credentials.DB_PASSWD, host=Credentials.DB_SERVER, db=Credentials.DB_NAME)

    def get_cursor(self):
        return self.conn.cursor()

    def insert(self, query, params=None, auto_commit=True):
        cursor = self.get_cursor()
        cursor.execute(query, params)
        if auto_commit:
            self.conn.commit()

