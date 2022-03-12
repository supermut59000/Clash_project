import sys
import os
from dotenv import load_dotenv
import datetime
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '..\\Module\\')
from moodle_request import request_moodle


load_dotenv('/home/mathis/Bureau/python/.env')
usr=os.getenv("MOODLE_USR")
pwd=os.getenv("MOODLE_PWD")

r = request_moodle()
r.connection(usr,pwd)
r.img_downloader(r.get_EDT(),"/var/www/html/homework/EDT/")
print(datetime.datetime.utcnow())