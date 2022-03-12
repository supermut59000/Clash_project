import sys
import datetime
import urllib.request
import matplotlib.pyplot as plt
import os
import json
from threading import Thread
from queue import Queue
import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '..\\Module\\')

from Clash_API_call import Clash_API_Call
from DATABASE_HANDLER import Data_handler_my_sql
from moodle_request import request_moodle

load_dotenv('..\\..\\.env')
usr=os.getenv("MOODLE_USR")
pwd=os.getenv("MOODLE_PWD")

host =os.getenv("DATABASE_IP")
database =os.getenv("DATABSE_NAME")
user =os.getenv("DATABASE_USR")
password =os.getenv("DATABASE_PASSWORD")


player_tag = "#9UPLRG2R"
clan_tag="#LLV9GG2P"
player_pseudo = "supermat59000"


database_handler = Data_handler_my_sql(host, user, password, database)
print(database_handler.get_usr_start_tr(player_pseudo))
#r = request_moodle()
#r.connection(usr,pwd)
#print(r.get_work_to_do())

#r.img_downloader(r.get_EDT(),os.getcwd())

#print(Clash_API_Call.get_API_status())
#temp = Clash_API_Call.usr_last_battle_decks(player_tag[1:])
#print(temp[1])