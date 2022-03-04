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
database_handler = Data_handler_my_sql(host, user, password, database)
temp = database_handler.get_player_battle_card(usr)
for counter,value in enumerate(temp):
	if car_1 in value:
		print(counter,value)
 
"""
dic_raciste={}
for i in card:
	database_handler = Data_handler_my_sql(host, user, password, database)
	temp = database_handler.get_battle_with_card(usr,i)
	for i in temp:
		if not dic_raciste.get(i[0]):
			dic_raciste[i[0]]=[i[1],int(i[2])]
		else:
			dic_raciste[i[0]][0]+=i[1]
			dic_raciste[i[0]][1]+=int(i[2])


dic_battle={}
database_handler = Data_handler_my_sql(host, user, password, database)
temp = database_handler.get_nb_battle(usr)
for i in temp:
	dic_battle[i[0]]=i[1]


for i in dic_raciste:
	print(i,str(round(dic_raciste[i][0]/dic_battle[i]*100,2))+"%",
		str(round(dic_raciste[i][1]/dic_raciste[i][0]*100,2))+"%")
"""