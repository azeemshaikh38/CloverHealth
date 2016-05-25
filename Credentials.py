import ConfigParser
import os.path

cfg = ConfigParser.ConfigParser()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

LOCAL_FILE = os.path.join(BASE_DIR, "credentials.cfg")
filename = None
if os.path.exists(LOCAL_FILE):
    filename = LOCAL_FILE
else:
    raise Exception("No credentials file given")

cfg.read(filename)

class Credentials:
    DB_SERVER = cfg.get("DB", "SERVER")
    DB_USER = cfg.get("DB", "USER")
    DB_PASSWD = cfg.get("DB", "PASSWD")
