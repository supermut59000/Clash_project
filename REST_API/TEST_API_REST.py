from flask import Flask , request
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

import os
import json
import datetime

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '..//Module//')

from Clash_API_call import Clash_API_Call
from DATABASE_HANDLER import Data_handler_my_sql
from moodle_request import request_moodle
load_dotenv('..//..//.env')


app = Flask(__name__)
CORS(app)

host = os.getenv("DATABASE_IP")
database = os.getenv("DATABSE_NAME")
user = os.getenv("DATABASE_USR")
password = os.getenv("DATABASE_PASSWORD")

@app.route("/tracked", methods= ['GET'])
def tracked():
	data_dic={}
	data= []
	database_handler = Data_handler_my_sql(host, user, password, database)
	temp = database_handler.get_tracked_usr()
	for i in range(len(temp)):
		temp_d={}
		temp_d["pseudo"]= temp[i][0]
		database_handler = Data_handler_my_sql(host, user, password, database)
		temp_tr = database_handler.get_usr_tr(temp[i][0])
		if temp_tr ==[]:
			database_handler = Data_handler_my_sql(host, user, password, database)
			temp_tr = database_handler.get_usr_start_tr(temp[i][0])
			temp_d["trophie"] = temp_tr[0][0]
		else:
			temp_d["trophie"] =temp_tr[0][0]
		data.append(temp_d)
		data = sorted(data, key=lambda d: d['trophie'], reverse=True) 
	return json.dumps(data)


@app.route("/oui/<player_pseudo>")
def info(player_pseudo):
	database_handler = Data_handler_my_sql(host, user, password, database)
	player_tag = database_handler.get_usr_pseudo(player_pseudo)[0]
	temp = Clash_API_Call.API_request_tracked_general_info(player_tag[1:])
	data=[]
	data.append({"pseudo":temp[1]})
	data.append({"level":temp[2]})
	data.append({"trophie":temp[3][4]})
	data.append({"wr":round((temp[3][0]/(temp[3][0]+temp[3][1]))*100,2)})
	return json.dumps(data)

@app.route("/ouitr/<player_pseudo>")
def tr(player_pseudo):
	database_handler = Data_handler_my_sql(host, user, password, database)
	temp = database_handler.get_tr_player(player_pseudo)
	data = []
	for i in range(len(temp)):
		data.append({"time":temp[i][2].strftime("%m/%d/%Y, %H:%M:%S"),"tr":temp[i][1]})
	return json.dumps(data)

@app.route("/hw")
def work():
	usr = os.getenv("MOODLE_USR")
	pwd = os.getenv("MOODLE_PWD")
	r = request_moodle()
	r.connection(usr,pwd)
	data = r.get_work_to_do()
	return json.dumps(data)



if __name__ == "__main__":
	app.run(host='0.0.0.0')