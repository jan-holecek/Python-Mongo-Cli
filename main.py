import pymongo
import os
from art import *
from getData import *
from saveData import *
from deleteData import *
from deleteAllData import *
import json

#načtení údajů k databázi z settings.json souboru
settings = open("settings.json")
settingsData = json.load(settings)

#přihlašovací údaje k databázi
name = settingsData["name"]
password = settingsData["password"]
dbName = settingsData["dbName"]

#připojení k MongoDB
URI = f"mongodb+srv://{name}:{password}@{dbName}.izgvs.mongodb.net/?retryWrites=true&w=majority"
mongoClient = pymongo.MongoClient(URI)
db = mongoClient.test #pojmenování poddatabáze
collection = db.posts #pojmenování kolekce (collection)

def main():
    from colorama import Fore, Style
    #název projektu
    tprint("MongoApp")

    #zjištění akce
    print("1) Ukázat data v databázi\n2) Uložit data do databáze\n3) Smazat určitá data z databáze\n4) Smazat všechna data z databáze\n\n----------------------------------\n\n5) Smazat historii\n6) Exit\n\n")

    #barvy
    underline = "\033[4m"
    bold = "\033[1m"
    error = f"{Fore.RED}ERROR\033[m{Style.RESET_ALL}"
    reset = f"{Style.RESET_ALL}"

    while True:
        #zjištění jestli je číslo vhodně zadáno
        try:
            #číslo potřebné pro určení funkce
            number = str(input("Zadej číslo akce: "))

            #funkce, které se mají vykonat při jednotlivých akcích
            if number == "1":
                print(f"\n\n\n{bold}{underline}DATA V DATABÁZI (1):{reset}\n")
                getData() 
            elif number == "2":
                print(f"\n\n\n{bold}{underline}ULOŽENÍ DAT DO DATABÁZE (2):{reset}\n")
                saveData()
            elif number == "3":
                print(f"\n\n\n{bold}{underline}SMAZÁNÍ URČITÝCH DAT Z DATABÁZE (3):{reset}\n")
                deleteData()
            elif number == "4":
                print(f"\n\n\n{bold}{underline}SMAZÁNÍ VŠECH DAT Z DATABÁZE (4):{reset}\n")
                deleteAllData()
            elif number == "5" or number == "clear" or number == "cls":
                os.system("cls")
                os.system("py database.py")

            #ukončení chodu aplikace v terminálu
            if number == "6" or number == "exit":
                return

        #akce při špatně zadaném čísle
        except:
            print(f"\n{error} | Zadej platné číslo!\n")

if __name__ == "__main__":
    main()