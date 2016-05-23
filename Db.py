import MySQLdb

class Db:

    def __init__(self):
        self.conn = MySQLdb.connect(user='azeem', passwd='Aus316+ghus', host='mafia.chl88ez3ycw9.us-west-2.rds.amazonaws.com')

    def get_cursor(self):
        return self.conn.cursor()

    def insert(self, query, params=None, auto_commit=True):
        cursor = self.get_cursor()
        cursor.execute(query, params)
        if auto_commit:
            self.conn.commit()

