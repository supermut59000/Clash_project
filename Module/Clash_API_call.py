import urllib.request
import json
import os
from dotenv import load_dotenv
from PIL import Image
import datetime
from PIL import PngImagePlugin
LARGE_ENOUGH_NUMBER = 100
PngImagePlugin.MAX_TEXT_CHUNK = LARGE_ENOUGH_NUMBER * (1024**2)
"""
Avoid the data decrompress max value
"""

load_dotenv('..//..//.env')

TOKEN = os.getenv("API_TOKEN_CLASH")
base_url = "https://api.clashroyale.com/v1"
PATH = os.getcwd()

class Clash_API_Call:
    def get_API_status():
        endpoint = "/players/%23" + "9UPLRG2R" 
        request1 = urllib.request.Request(
            base_url + endpoint, None, {"Authorization": "Bearer %s" % TOKEN}
        )
        reponse_temp = urllib.request.urlopen(request1)
        return reponse_temp.getcode()

    def API_request_tracked_battlelog(player_tag: str):
        endpoint = "/players/%23" + player_tag + "/battlelog"
        request1 = urllib.request.Request(
            base_url + endpoint, None, {"Authorization": "Bearer %s" % TOKEN}
        )
        response = urllib.request.urlopen(request1).read().decode("utf-8")
        data = json.loads(response)  # Convert into dict
        tracked_info = data[0]["team"][0]
        opponent = data[0]["opponent"][0]
        battle_type = data[0]["type"]

        return tracked_info, opponent, battle_type

    def API_request_tracked_general_info(player_tag: str):
        endpoint = "/players/%23" + player_tag
        request1 = urllib.request.Request(
            base_url + endpoint, None, {"Authorization": "Bearer %s" % TOKEN}
        )
        response = urllib.request.urlopen(request1).read().decode("utf-8")
        data = json.loads(response)  # Convert into disctionnary
        tag = data["tag"]
        name = data["name"]
        current_lvl = data["expLevel"]

        win = data["wins"]
        lose = data["losses"]
        nb_battle = data["battleCount"]
        crowns = data["threeCrownWins"]
        current_trophies = data["trophies"]

        battle_info = [win , lose , nb_battle , crowns , current_trophies]

        return tag , name , current_lvl , battle_info 

    def get_all_clan_member(clan_tag: str) -> list:
        endpoint = "/clans/%23" + clan_tag + "/members"
        request1 = urllib.request.Request(
            base_url + endpoint, None, {"Authorization": "Bearer %s" % TOKEN}
        )
        response = urllib.request.urlopen(request1).read().decode("utf-8")
        data = json.loads(response)  # Convert into disctionnary
        temp = []
        for i in range(len(data["items"])):
            temp.append(data["items"][i]["tag"])
        return temp

    def creation_png_of_the_deck(player_tag: str):
        endpoint = "/players/%23" + player_tag
        request1 = urllib.request.Request(
            base_url + endpoint, None, {"Authorization": "Bearer %s" % TOKEN}
        )
        response = urllib.request.urlopen(request1).read().decode("utf-8")
        data = json.loads(response)  # Convert into disctionnary
        
        avg_level = 0
        data_temp = []
        for i in data["currentDeck"]:
            temp = [i["level"],i["maxLevel"]]
            data_temp.append(temp)
        for i in data_temp:
            if i[1] == 14:
                avg_level = avg_level + i[0]
            elif i[1] == 12:
                avg_level = avg_level + i[0] + 2
            elif i[1] == 9:
                avg_level = avg_level + i[0] + 5
            elif i[1] == 6:
                avg_level = avg_level + i[0] + 8

        temp_1 = []
        for i in range(len(data["currentDeck"])):
            temp_1.append(os.getcwd() + "/Img" + "/" + data["currentDeck"][i]["name"] + ".png")

        im1 = Image.open(temp_1[0])
        im2 = Image.open(temp_1[1])
        im3 = Image.open(temp_1[2])
        im4 = Image.open(temp_1[3])
        im5 = Image.open(temp_1[4])
        im6 = Image.open(temp_1[5])
        im7 = Image.open(temp_1[6])
        im8 = Image.open(temp_1[7])

        deck = Image.new("RGB", (im1.width * 4, im1.height * 2))
        deck.paste(im1, (0, 0), im1)
        deck.paste(im2, (im1.width, 0), im2)
        deck.paste(im3, (im1.width * 2, 0), im3)
        deck.paste(im4, (im1.width * 3, 0), im4)
        deck.paste(im5, (0, im1.height), im5)
        deck.paste(im6, (im1.width, im1.height), im6)
        deck.paste(im7, (im1.width * 2, im1.height), im7)
        deck.paste(im8, (im1.width * 3, im1.height), im8)
        deck.save(PATH + "/deck.png")
        return avg_level/8


    def get_all_cards():
        endpoint = "/cards/"
        request1 = urllib.request.Request(
            base_url + endpoint, None, {"Authorization": "Bearer %s" % TOKEN}
        )
        response = urllib.request.urlopen(request1).read().decode("utf-8")
        data = json.loads(response)  

        return data["items"]

    def usr_last_battle_decks(player_tag : str):
        endpoint = "/players/%23" + player_tag + "/battlelog"
        request1 = urllib.request.Request(
            base_url + endpoint, None, {"Authorization": "Bearer %s" % TOKEN}
        )
        reponse_temp = urllib.request.urlopen(request1)
        status_code = reponse_temp.getcode()
        response = reponse_temp.read().decode("utf-8")
        data = json.loads(response) 
        deck_usr = []
        deck_opponent = []
        avg_level_usr = 0
        avg_level_opponent = 0
        data_temp = []
        for i in data[0]["team"][0]["cards"]:
            deck_usr.append(i["name"])
            temp = [i["level"],i["maxLevel"]]
            data_temp.append(temp)
    

        for i in data_temp:
            if i[1] == 14:
                avg_level_usr = avg_level_usr + i[0]
            elif i[1] == 12:
                avg_level_usr = avg_level_usr + i[0] + 2
            elif i[1] == 9:
                avg_level_usr = avg_level_usr + i[0] + 5
            elif i[1] == 6:
                avg_level_usr = avg_level_usr + i[0] + 8
            
        data_temp = []
        for i in data[0]["opponent"][0]["cards"]:
            deck_opponent.append(i["name"])
            temp = [i["level"],i["maxLevel"]]
            data_temp.append(temp)
                

        for i in data_temp:
            if i[1] == 14:
                avg_level_opponent = avg_level_opponent + i[0]
            elif i[1] == 12:
                avg_level_opponent = avg_level_opponent + i[0] + 2
            elif i[1] == 9:
                avg_level_opponent = avg_level_opponent + i[0] + 5
            elif i[1] == 6:
                avg_level_opponent = avg_level_opponent + i[0] + 8
        if "trophyChange" not in data[0]["team"][0].keys():
            tr_change = 0
        else:
            tr_change = data[0]["team"][0]["trophyChange"]
        if "startingTrophies" not in data[0]["team"][0]:
            current_tr = 0
        else :
            current_tr = data[0]["team"][0]["startingTrophies"] + tr_change
        win = 0
        if data[0]["type"] == "boatBattle":
            if data[0]["boatBattleWon"]:
                win=1
        else:
            if data[0]["team"][0]["crowns"] >data[0]["opponent"][0]["crowns"]:
                win = 1
        battle_type = data[0]["type"]
        battle_time = data[0]["battleTime"]
        deck = [deck_usr ,
        avg_level_usr/8 ,
        deck_opponent ,
        avg_level_opponent/8]
        return deck , current_tr , win ,battle_type,battle_time,data[0],status_code