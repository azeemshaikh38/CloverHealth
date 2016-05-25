<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> v2
import logging
from Commons import Commons

logger = logging.getLogger('Query')
logging.basicConfig(filename=Commons.LOG_FILE, level=Commons.LOGGER_LEVEL, format=Commons.LOGGER_FORMAT)
<<<<<<< HEAD
=======
>>>>>>> v1
=======
>>>>>>> v2

class Query:

    def insert_query(self, tablename, col_names, vals):
        if len(col_names)==0 or len(vals)==0:
            raise Exception("col_names or vals cannot be empty")
        if len(col_names)!=len(vals):
            raise Exception("Length of col_names and vals is different")
<<<<<<< HEAD
<<<<<<< HEAD
        col_names_query = ", ".join([tablename+'.'+col_name for col_name in col_names])
=======
        col_names_query = ", ".join([col_name for col_name in col_names])
>>>>>>> v1
=======
        col_names_query = ", ".join([tablename+'.'+col_name for col_name in col_names])
>>>>>>> v4
        col_vals_query  = ", ".join(['%s' for val in vals])
        query = """INSERT INTO {} ({}) VALUES ({})""".format(tablename, col_names_query, col_vals_query)
        params = tuple(vals)
        return query, params
