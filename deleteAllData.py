import database

def deleteAllData():
    from colorama import Fore, Style

    #smazání příspěvku z databáze
    database.collection.delete_many({})

    print(f'{Fore.GREEN}ÚSPĚCH {Style.RESET_ALL}| Všechny příspěvky byly z databáze smazány!\n')