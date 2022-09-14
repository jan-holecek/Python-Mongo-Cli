import main

def deleteAllData():
    from colorama import Fore, Style

    #eror zpráva
    error = f"{Fore.RED}ERROR\033[m{Style.RESET_ALL}"

    #počet příspěvků v kolekci
    itemsCount = main.collection.count_documents({})

    #smazání příspěvku z databáze
    main.collection.delete_many({})

    if str(itemsCount) == "0":
        print(f"\n{error} | V dané kolekci se nenachází žádné příspevky!\n")
    else:
        print(f'{Fore.GREEN}ÚSPĚCH {Style.RESET_ALL}| Všechny příspěvky byly z databáze smazány! (Smazáno: {itemsCount})\n')