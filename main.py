import pymongo
import os
import json
from art import *
from getData import *
from saveData import *
from deleteData import *
from deleteAllData import *

#načtení údajů k databázi z settings.json souboru
settings = open("settings.json")
settingsData = json.load(settings)

#přihlašovací údaje k databázi
name = settingsData["name"]
password = settingsData["password"]
dbName = settingsData["dbName"]
subdatabaseName = settingsData["subdatabaseName"]
collectionName = settingsData["collectionName"]

#připojení k MongoDB
URI = f"mongodb+srv://{name}:{password}@{dbName}.izgvs.mongodb.net/?retryWrites=true&w=majority"
mongoClient = pymongo.MongoClient(URI)
db = mongoClient[subdatabaseName] #pojmenování poddatabáze
collection = db[collectionName] #pojmenování kolekce (collection)

def main():
    from colorama import Fore, Style
    #název projektu
    tprint("Python-Mongo-Cli")

    #list se seznamem funkcí 
    functionList = [
        "Zobrazit data z databáze",
        "Uložit data do databáze",
        "Smazat určitá data z databáze",
        "Smazat všechna data z databáze",
        "Smazat historii",
        "Konec\n",
    ]

    #funkce na vypsání listu funkcí
    def printFunctionList():
        for function in functionList:
            index = functionList.index(function) + 1
            if index == 5:
                print("\n----------------------------------\n")

            print(str(index) + ") " + function)
    #spuštění funkce printFunctionList
    printFunctionList()

    #barvy
    underline = "\033[4m"
    bold = "\033[1m"
    reset = f"{Style.RESET_ALL}"

    while True:
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
            print("\033c", end='')
            tprint("Python-Mongo-Cli")
            printFunctionList()

        #ukončení chodu aplikace v terminálu
        if number == "6" or number == "konec" or number == "exit":
            os._exit(0)

if __name__ == "__main__":
    main()