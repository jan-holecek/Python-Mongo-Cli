import main

def saveData():
    from colorama import Fore, Style

    #eror zpráva
    error = f"{Fore.RED}ERROR\033[m{Style.RESET_ALL}"

    #získání hodnot od uživatele
    name = str(input("Napiš název příspěvku: "))
    content = str(input("Napiš text příspěvku: "))
    author = str(input("Napiš autora příspěvku: "))

    #zjištění jestli není žádná hodnota neznámá 
    if name == "" or content == "" or author == "":
        print(f"\n{error} | Žádná hodnota nemůže být prázdná!\n")
    else:
        #vytvoření schéma příspěvku
        post = {
            "name": author,
            "title": name,
            "content": content
        }

        #uložení příspěvku do databáze
        savePost = main.collection.insert_one(post)

        print(f'{Fore.GREEN}ÚSPĚCH {Style.RESET_ALL}| Příspěvěk byl poslán do databáze! (id: {savePost.inserted_id})\n')