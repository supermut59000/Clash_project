import os
from dotenv import load_dotenv
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '..//Module//')

from Clash_API_call import Clash_API_Call
from DATABASE_HANDLER import Data_handler_my_sql
from moodle_request import request_moodle
load_dotenv('..//..//.env')


host = os.getenv("DATABASE_IP")
database = os.getenv("DATABSE_NAME")
user = os.getenv("DATABASE_USR")
password = os.getenv("DATABASE_PASSWORD")

card=['Electro Giant','Mega Knight','Elite Barbarians']
car_1='Elite Barbarians'
usr='supermat59000'
dic={}
database_handler = Data_handler_my_sql(host, user, password, database)
temp = database_handler.get_player_battle_card(usr)
for value in temp:
	for i in card:
		if i in value:
			if not dic.get(value[1]):
				dic[value[1]]={}
				for i in card:
					dic[value[1]][i]=0
			dic[value[1]][i]=dic[value[1]].get(i)+1

database_handler = Data_handler_my_sql(host, user, password, database)
a = database_handler.get_nb_battle(usr)
for i in a:
	print(i[0],dic.get(i[0]),i[1])
