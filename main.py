from curses.textpad import Textbox
from functions import *
import os
import npyscreen
import random

#test if data :

appdata_path=os.getenv('APPDATA')+"\\f1-python-data"+"\\"
if not os.path.exists(appdata_path):
    os.mkdir(appdata_path)

if not os.path.exists(appdata_path+"saves"):
    os.mkdir(appdata_path+"saves")

if not os.path.exists(appdata_path+"pilots.json"):
    print("No data found, creating new one")
    create_pilot_dict(appdata_path+"pilots.json")

if not os.path.exists(appdata_path+"full_pilot_list.json"):
    print("No data found, creating new one")
    copy_full_pilots_list(appdata_path+"full_pilot_list.json")



#menu page
while True:
    clear()
    enchanced_print("Welcome to F1-Python-Data\nSelect a page below to continue:\n\n1. Enter predictions\n2. View predictions\n3. View predictions results\n4. View full pilot list\n0. Exit")
    match ask_menu_question():
        case "1":
            clear()
            predicts=make_predics(appdata_path+"pilots.json")
            enchanced_print("Enter predictions file name :")
            name=input(">>>")
            save_predictions(name, predicts,appdata_path)
            exit()
        case "2":
            clear()
            enchanced_print("Enter predictions name file :")
            validity=False
            while validity==False:
                name=input(">>>")
                if check_file_validity(appdata_path+"saves/"+name+".json"):
                    validity=True
            load_predictions(name,appdata_path)

