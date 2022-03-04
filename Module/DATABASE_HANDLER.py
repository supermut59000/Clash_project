import mysql.connector

class Data_handler_my_sql():
    
    def __init__(self, database_ip, database_user, database_password, database_name):
        self.connector = mysql.connector.connect(host=database_ip,
            database=database_name,
            user=database_user,
            password=database_password
            )
        

    def get_usr_pseudo(self , player_tag : str):
        cursor = self.connector.cursor()
        SELECT = f"SELECT usr_tag "
        FROM =f"FROM Tracked_usr "
        WHERE = f"WHERE usr_pseudo = %s;"
        query = (SELECT + FROM + WHERE)
        cursor.execute(query,(player_tag,),)
        data = cursor.fetchone()
        cursor.close()
        self.connector.close()
        return data

    def new_tracked_usr(
        self,
        usr_tag: str,
        usr_pseudo: str,
        usr_current_lvl: int,
        usr_current_tr: int,
        time: str,
    ):
        cursor = self.connector.cursor()
        INSERT = f"INSERT INTO Tracked_usr"
        ROWS = f"(usr_tag , usr_pseudo , usr_current_lvl , usr_current_tr , start_tracking)"
        VALUES = f"VALUES( %s , %s , %s , %s , %s );"
        query = INSERT + ROWS + VALUES
        try:
            cursor.execute(
                query,
                (
                    usr_tag,
                    usr_pseudo,
                    usr_current_lvl,
                    usr_current_tr,
                    time,
                ),
            )
            self.connector.commit()
        except mysql.connector.Error as error:
            if error.errno == 1062:
                return True,error.errno
        cursor.close()
        self.connector.close()   
        return False

    def get_tracked_usr(self):
        cursor = self.connector.cursor()
        SELECT = f"SELECT usr_pseudo "
        FROM = f"FROM Tracked_usr;"
        query = (SELECT + FROM)
        cursor.execute(query)
        data = cursor.fetchall() 
        cursor.close()
        self.connector.close()   
        return data

    def get_tracked_usr_tag(self):
        cursor = self.connector.cursor()
        SELECT = f"SELECT usr_tag "
        FROM = f"FROM Tracked_usr;"
        query = (SELECT + FROM)
        cursor.execute(query)
        data = cursor.fetchall() 
        cursor.close()
        self.connector.close()   
        return data

    def insert_usr_deck(
        self,
        card_1 : str,
        card_2 : str,
        card_3 : str,
        card_4 : str,
        card_5 : str,
        card_6 : str,
        card_7 : str,
        card_8 : str,
        avg_level : float,):
        cursor = self.connector.cursor()
        INSERT = f"INSERT INTO user_deck"
        ROWS = f"(card_1 , card_2 , card_3 , card_4 , card_5 , card_6 , card_7 , card_8 , avg_card_lvl)"
        VALUES = f"VALUES( %s , %s , %s , %s , %s , %s , %s , %s , %s);"
        query = (INSERT + ROWS + VALUES)
        cursor.execute(
            query,
            (
                card_1,
                card_2,
                card_3,
                card_4,
                card_5,
                card_6,
                card_7,
                card_8,
                avg_level,
            ),)
        self.connector.commit()
        SELECT = f"SELECT user_deck_id "
        FROM = f"FROM user_deck "
        WHERE = f"WHERE card_1 = %s and card_2 = %s and card_3 = %s and card_4 = %s and card_5 = %s and card_6 = %s and card_7 = %s and card_8 = %s;"
        query = (SELECT + FROM + WHERE)
        cursor.execute(
            query,
            (
                card_1,
                card_2,
                card_3,
                card_4,
                card_5,
                card_6,
                card_7,
                card_8,
            ),)
        data = cursor.fetchall()
        cursor.close()
        self.connector.close()
        return data

    def get_usr_deck(self , agv_lvl : float):
        cursor = self.connector.cursor()
        SELECT = f"SELECT * "
        FROM = f"FROM user_deck "
        WHERE = f"WHERE avg_card_lvl = (%s);"
        query = (SELECT + FROM + WHERE)
        cursor.execute(query,(agv_lvl,))
        data = cursor.fetchall() 
        cursor.close()
        self.connector.close()   
        return data


    def insert_usr_enemy_deck(
        self,
        card_1 : str,
        card_2 : str,
        card_3 : str,
        card_4 : str,
        card_5 : str,
        card_6 : str,
        card_7 : str,
        card_8 : str,
        avg_level : float,):
        cursor = self.connector.cursor()
        INSERT = f"INSERT INTO user_enemy_deck "
        ROWS = f"(card_1 , card_2 , card_3 , card_4 , card_5 , card_6 , card_7 , card_8 , avg_card_lvl) "
        VALUES = f"VALUES( %s , %s , %s , %s , %s , %s , %s , %s , %s);"
        query = INSERT + ROWS + VALUES
        cursor.execute(
            query,
            (
                card_1,
                card_2,
                card_3,
                card_4,
                card_5,
                card_6,
                card_7,
                card_8,
                avg_level,
            ),)
        self.connector.commit()
        SELECT = f"SELECT user_deck_id "
        FROM = f"FROM user_enemy_deck "
        WHERE = f"WHERE card_1 = %s and card_2 = %s and card_3 = %s and card_4 = %s and card_5 = %s and card_6 = %s and card_7 = %s and card_8 = %s;"
        query = (SELECT + FROM + WHERE)
        cursor.execute(
            query,
            (
                card_1,
                card_2,
                card_3,
                card_4,
                card_5,
                card_6,
                card_7,
                card_8,
            ),)
        data = cursor.fetchall()
        cursor.close()
        self.connector.close()
        return data

    def get_usr_enemy_deck(self , agv_lvl : float):
        cursor = self.connector.cursor()
        SELECT =f"SELECT * "
        FROM = f"FROM user_enemy_deck "
        WHERE = f"WHERE avg_card_lvl = (%s);"
        query = (SELECT + FROM + WHERE)
        cursor.execute(query,(agv_lvl,))
        data = cursor.fetchall() 
        cursor.close()
        self.connector.close()   
        return data

    def insert_new_battle(self,
        usr_tag : str,
        usr_deck_id : int,
        usr_enemy_deck_id : int,
        usr_current_tr : int,
        battle_type :str,
        battle_time : str,
        win : int):

        cursor = self.connector.cursor()
        INSERT = f"INSERT INTO Battle"
        ROWS = f"(usr_tag , usr_deck_id , usr_enemy_deck_id , usr_current_tr , battle_type , battle_time , win )"
        VALUES = f"VALUES( %s , %s , %s , %s , %s , %s , %s );"
        query = (INSERT + ROWS + VALUES)
        cursor.execute(
            query,
            (
                usr_tag,
                usr_deck_id,
                usr_enemy_deck_id,
                usr_current_tr,
                battle_type,
                battle_time,
                win,
            ))
        self.connector.commit()
        cursor.close()
        self.connector.close()
        return

    def get_last_battle(self, usr_tag :str):
        cursor = self.connector.cursor()
        SELECT = f"SELECT battle_id,Battle_time "
        FROM = f"FROM Battle "
        WHERE = f"WHERE usr_tag = %s ORDER BY Battle_time DESC LIMIT 1;"
        query = (SELECT + FROM + WHERE)
        cursor.execute(query,(usr_tag,),)
        data = cursor.fetchall()
        cursor.close()
        self.connector.close()
        return data


    def get_tr_player(self , player_name : str):
        cursor = self.connector.cursor()
        SELECT = f"SELECT Tracked_usr.usr_pseudo , Battle.usr_current_tr , Battle.battle_time "
        FROM = f"FROM Battle INNER JOIN Tracked_usr ON Battle.usr_tag = Tracked_usr.usr_tag "
        WHERE = f"WHERE Battle.battle_type = 'PvP' and Tracked_usr.usr_pseudo = %s;"
        query = (SELECT + FROM + WHERE)
        cursor.execute(query,(player_name,),)
        data = cursor.fetchall()
        cursor.close()
        self.connector.close()
        return data


    def get_battle_with_card(self , player_name : str, card_name : str):
        cursor = self.connector.cursor()
        SELECT = f"SELECT T.bt,COUNT(T.ps),SUM(T.win) "
        SELECT_1 = f"FROM (SELECT Battle.battle_type as bt,Tracked_usr.usr_pseudo as ps,user_deck.* ,Battle.win as win "
        FROM_1 = f"FROM (user_deck INNER JOIN Battle ON user_deck.user_deck_id = Battle.usr_deck_id) INNER JOIN Tracked_usr ON Battle.usr_tag = Tracked_usr.usr_tag "
        WHERE_1 = f"WHERE card_1 = %s OR card_2 = %s OR card_3 = %s OR card_4 = %s OR card_5 = %s OR card_6 = %s OR card_7 = %s OR card_8 = %s) as T "
        FROM = (SELECT_1 + FROM_1 + WHERE_1)
        GROUP_BY = f"GROUP BY T.bt,T.ps "
        HAVING = f"HAVING T.ps = %s;"
        query = (SELECT + FROM + GROUP_BY + HAVING)
        cursor.execute(query,(card_name,
            card_name,
            card_name,
            card_name,
            card_name,
            card_name,
            card_name,
            card_name,
            player_name,),)
        data = cursor.fetchall()
        cursor.close()
        self.connector.close()
        return data

    def get_player_battle_card(self , player_name : str):
        cursor = self.connector.cursor()
        SELECT = f"SELECT Tracked_usr.usr_pseudo,Battle.battle_type, card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8 "
        FROM = f"FROM (user_deck INNER JOIN Battle ON user_deck.user_deck_id = Battle.usr_deck_id) INNER JOIN Tracked_usr ON Battle.usr_tag = Tracked_usr.usr_tag "
        WHERE = f"WHERE Tracked_usr.usr_pseudo = %s;"
        query = (SELECT + FROM + WHERE)
        cursor.execute(query,(player_name,),)
        data = cursor.fetchall()
        cursor.close()
        self.connector.close()
        return data

    def get_nb_battle(self , player_name : str):
        cursor = self.connector.cursor()
        SELECT = f"SELECT Battle.battle_type,COUNT(*) "
        FROM = f"FROM Battle INNER JOIN Tracked_usr ON Battle.usr_tag = Tracked_usr.usr_tag "
        GROUP_BY = f"GROUP BY Battle.battle_type ,Tracked_usr.usr_pseudo "
        HAVING = f"HAVING Tracked_usr.usr_pseudo = %s;"
        query = (SELECT + FROM + GROUP_BY + HAVING)
        cursor.execute(query,(player_name,),)
        data = cursor.fetchall()
        cursor.close()
        self.connector.close()
        return data


    def get_usr_tr(self, player_name :str):
        cursor = self.connector.cursor()
        SELECT = f"SELECT Battle.usr_current_tr "
        FROM = f"FROM Battle INNER JOIN Tracked_usr ON Battle.usr_tag = Tracked_usr.usr_tag "
        WHERE = f"WHERE Tracked_usr.usr_pseudo = %s AND Battle.battle_type = 'PVP' "
        ORDER_BY= f"ORDER BY Battle_time DESC LIMIT 1;"
        query = (SELECT + FROM + WHERE + ORDER_BY)
        cursor.execute(query,(player_name,),)
        data = cursor.fetchall()
        cursor.close()
        self.connector.close()
        return data

    def get_usr_start_tr(self, player_name :str):
        cursor = self.connector.cursor()
        SELECT = f"SELECT usr_current_tr "
        FROM = f"FROM Tracked_usr "
        WHERE = f"WHERE usr_pseudo = %s ;"
        query = (SELECT + FROM + WHERE )
        cursor.execute(query,(player_name,),)
        data = cursor.fetchall()
        cursor.close()
        self.connector.close()
        return data

