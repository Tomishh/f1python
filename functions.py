import json
import shutil
import os
from time import sleep

from numpy import full


def make_predics(pilots_json):
    pilots=json.load(open(pilots_json))
    predict=[]
    for i in range(1):
        choice_valide=False
        while choice_valide==False:
            choice=input(f"Pilot in {i+1} place : ")
            print(choice)
            choice.upper()
            print(choice)
            if choice in pilots:
                predict.append(choice) 
                choice_valide=True
            else:
                print("Pilot not found, enter name again")
    return predict

def create_pilot_dict(path):
    pilots=["HAM","RUS","VER","PER","RIC","NOR","GAS","TSU","VET","STR","MSC","MAG","ALB","LAT","BOT","ZHO","OCO","ALO","LEC","SAI"]
    json_format = json.dumps(pilots)
    with open(path, "w") as f:
        f.write(json_format)

def copy_full_pilots_list(destination):
    shutil.copyfile("./source/full_pilot_list.json",destination)

def enchanced_print(string):
    print("\n------------------------------------------------------\n"+string+"\n------------------------------------------------------\n")


def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def ask_menu_question():
    choice=""
    while choice!="1" and choice!="2" and choice!="3" and choice!="4" and choice!="0":
        choice=input("Enter a number : ")
    return choice

def save_predictions(name, data,path):
    f = open(path+"/saves/"+name+".json", "w")
    json.dump(data, f)

def load_predictions(name,path):
    f = open(path+"/saves/"+name+".json", "r")
    data = json.load(f)
    full_data= get_full_data(path+"/full_pilot_list.json")
    for alias in data:
        detail_data=get_pilot_detail_data(alias,full_data)
        print(detail_data)
        input("Press enter to continue")

def get_full_data(path):
    f = open(path,"r")
    data = json.load(f)
    return data

def get_pilot_detail_data(alias,full_data):
    detail_data={}
    for i in full_data['driver']:
        if i['alias']==alias:
            detail_data["alias"]=alias
            detail_data["name"]=i['infos'][0]["name"]
            detail_data["team"]=i['infos'][0]["team"]
            detail_data["number"]=i['infos'][0]["number"]
    return detail_data


