import sys
import os
import datetime
from threading import Thread
from dotenv import load_dotenv
sys.path.insert(1, '..//Module//')
from Clash_API_call import Clash_API_Call
from DATABASE_HANDLER import Data_handler_my_sql
load_dotenv('/home/mathis/Bureau/python/.env')

host = os.getenv("DATABASE_IP")
database = os.getenv("DATABSE_NAME")
user = os.getenv("DATABASE_USR")
password = os.getenv("DATABASE_PASSWORD")

player = "#9UPLRG2R"

def usr_last_battle_decks(player_tag: str):
    database_handler = Data_handler_my_sql(host, user, password, database)
    temp = Clash_API_Call.usr_last_battle_decks(player_tag[1:])
    temp_usr =  database_handler.get_usr_deck(temp[0][1])
    database_handler = Data_handler_my_sql(host, user, password, database)
    temp_opponent =  database_handler.get_usr_enemy_deck(temp[0][3])
    trouve_usr = False
    for i in temp_usr:
        cards = i[1:9]
        compteur = 0 
        for j in list(cards):
            if j in temp[0][0]:
                compteur = compteur +1
        if compteur == 8:
            trouve_usr = True
            deck_id_usr = i[0:1]
        
    if not trouve_usr:
        database_handler = Data_handler_my_sql(host, user, password, database)
        deck_id_usr = database_handler.insert_usr_deck(
            temp[0][0][0],
            temp[0][0][1],
            temp[0][0][2],
            temp[0][0][3],
            temp[0][0][4],
            temp[0][0][5],
            temp[0][0][6],
            temp[0][0][7],
            temp[0][1])[0]

    trouve_opponent = False
    for i in temp_opponent:
        cards = i[1:9]
        compteur = 0 
        for j in list(cards):
            if j in temp[0][2]:
                compteur = compteur +1
        if compteur == 8:
            trouve_opponent = True
            deck_id_opponent = i[0:1]
        
    if not trouve_opponent:
        database_handler = Data_handler_my_sql(host, user, password, database)
        deck_id_opponent = database_handler.insert_usr_enemy_deck(
            temp[0][2][0],
            temp[0][2][1],
            temp[0][2][2],
            temp[0][2][3],
            temp[0][2][4],
            temp[0][2][5],
            temp[0][2][6],
            temp[0][2][7],
            temp[0][3])[0]

    win = temp[2]
    usr_current_tr = temp[1]
    battle_type = temp[3]
    battle_time = temp[4]
    return deck_id_usr,deck_id_opponent,usr_current_tr,battle_type,battle_time,win


def main(player_tag : str):
    temp = usr_last_battle_decks(player_tag)
    battle_time = datetime.datetime(int(temp[4][0:4]),
    int(temp[4][4:6]),
    int(temp[4][6:8]),
    int(temp[4][9:11]),
    int(temp[4][11:13]),
    int(temp[4][13:15]))
    database_handler = Data_handler_my_sql(host, user, password, database)
    if database_handler.get_last_battle(player_tag) == []:
        database_handler = Data_handler_my_sql(host, user, password, database)
        database_handler.insert_new_battle(
            player_tag,
            temp[0][0],
            temp[1][0],
            temp[2],
            temp[3],
            battle_time,
            temp[5],)
        return
    database_handler = Data_handler_my_sql(host, user, password, database)
    if battle_time != database_handler.get_last_battle(player_tag)[0][1]:
        database_handler = Data_handler_my_sql(host, user, password, database)
        database_handler.insert_new_battle(
            player_tag,
            temp[0][0],
            temp[1][0],
            temp[2],
            temp[3],
            battle_time,
            temp[5],)
        return
    return

database_handler = Data_handler_my_sql(host, user, password, database)
temp = database_handler.get_tracked_usr_tag()
for i in range(len(temp)):
    temp[i]=temp[i][0]

class prout(Thread):
    def __init__(self, queue ):
        Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            if len(self.queue) !=0:
                usr = self.queue.pop()
                main(usr)
            else:
                return

        
database_handler = Data_handler_my_sql(host, user, password, database)
temp = database_handler.get_tracked_usr_tag()
for i in range(len(temp)):
    temp[i]=temp[i][0]


t_count=8
Clash_status = Clash_API_Call.get_API_status()
if Clash_status == 200:
    for i in range (t_count):
        t = prout(temp)
        t.start()
    t.join()
    status = " Done"
elif Clash_status == 503:
    status = " Maintenance"
elif Clash_status == 403:
    status == " Acces Denied"
print(datetime.datetime.utcnow(),status)
