import database

def deleteData():
    from colorama import Fore, Style
    from bson.objectid import ObjectId

    #eror zpráva
    error = f"{Fore.RED}ERROR\033[m{Style.RESET_ALL}"

    #získání hodnot od uživatele
    id = str(input("Zadej ID příspěvku: "))

    #zjištění jestli není žádná hodnota neznámá 
    if id == "":
        print(f"\n{error} | Hodnota ID nemůže být prázdná!\n")
    else:
        #smazání příspěvku z databáze
        deletePost = database.collection.delete_one({'_id': ObjectId(id)})

        print(f'{Fore.GREEN}ÚSPĚCH {Style.RESET_ALL}| Příspěvěk byl smazán z databáze! (id: {id})\n')