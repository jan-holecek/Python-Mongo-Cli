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
        #název projektu
        tprint("Python-Mongo-Cli")

        for function in functionList:
            index = functionList.index(function) + 1
            if index == 5:
                print("\n----------------------------------\n")

            #vypíše jednotlivé funkce
            print(str(index) + ") " + function)
    #spuštění funkce printFunctionList
    printFunctionList()

    #styly textu
    underline = "\033[4m"
    bold = "\033[1m"
    reset = f"{Style.RESET_ALL}"
    error = f"{Fore.RED}ERROR\033[m{Style.RESET_ALL}"

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
            yesNo = str(input("Opravdu chcete smazat všechna data z databáze? (Ano/Ne) ")).lower()
            if yesNo == "ano" or yesNo == "yes" or yesNo == "y":
                deleteAllData()
            else:
                print(f"\n{error} | Vymazání všech dat z databáze bylo zrušeno!\n")
        elif number == "5" or number == "clear" or number == "cls" or number == "smazat" or number == "vyčistit":
            print("\033c", end='')
            printFunctionList()

        #ukončení chodu aplikace v terminálu
        if number == "6" or number == "konec" or number == "exit" or number == "leave" or number == "odejít":
            os.system("cls")
            os._exit(0)

if __name__ == "__main__":
    main()