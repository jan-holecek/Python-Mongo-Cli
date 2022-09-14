import main

def deleteData():
    from colorama import Fore, Style
    from bson.objectid import ObjectId

    #eror zpráva
    error = f"{Fore.RED}ERROR\033[m{Style.RESET_ALL}"

    #všechny příspěvky v kolekci
    items = main.collection.find()
    #počet příspěvků v kolekci
    itemsCount = main.collection.count_documents({})

    #list pro všechny ID příspěvků v databázi
    idList = []

    #zjištění jestli se v kolekci nachází nějaké příspěvky
    if str(itemsCount) == "0": 
        print(f"\n{error} | V dané kolekci se nenachází žádné příspevky!\n")
    else:
        #získání hodnot od uživatele
        id = str(input("Zadej ID příspěvku: "))

        for item in items:
            idList.append(item["_id"]) #přidání všech ID do listu

            for oneId in idList:
                if id == oneId: #zjištění jestli je zadaná ID v listu příspěvků
                    if id == "": #pokud je ID hodnota prázdná pošle error zprávu
                        print(f"\n{error} | Hodnota ID nemůže být prázdná!\n")
                    else:
                        #smazání příspěvku z databáze
                        deletePost = main.collection.delete_one({'_id': ObjectId(id)})

                        print(f'{Fore.GREEN}ÚSPĚCH {Style.RESET_ALL}| Příspěvěk byl smazán z databáze! (id: {id})\n')
                else:
                    print(f"\n{error} | Zadali jste špatné ID!\n")

    

