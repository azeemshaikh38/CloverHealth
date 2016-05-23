import MySQLdb
<<<<<<< HEAD
from Credentials import Credentials
import logging
from Commons import Commons

logger = logging.getLogger('Db')
logging.basicConfig(filename=Commons.LOG_FILE, level=Commons.LOGGER_LEVEL, format=Commons.LOGGER_FORMAT)
=======
>>>>>>> v1

class Db:

    def __init__(self):
<<<<<<< HEAD
        self.conn = MySQLdb.connect(user=Credentials.DB_USER, passwd=Credentials.DB_PASSWD, host=Credentials.DB_SERVER, db=Credentials.DB_NAME)
=======
        self.conn = MySQLdb.connect(user='azeem', passwd='Aus316+ghus', host='mafia.chl88ez3ycw9.us-west-2.rds.amazonaws.com')
>>>>>>> v1

    def get_cursor(self):
        return self.conn.cursor()

    def insert(self, query, params=None, auto_commit=True):
        cursor = self.get_cursor()
        cursor.execute(query, params)
        if auto_commit:
            self.conn.commit()

