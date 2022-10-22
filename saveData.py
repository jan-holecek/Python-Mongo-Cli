from email.mime import image
from pydoc import describe
import main
import datetime

def saveData():
    from colorama import Fore, Style

    #eror zpráva
    error = f"{Fore.RED}ERROR\033[m{Style.RESET_ALL}"

    #získání hodnot od uživatele
    name = str(input("Napiš název příspěvku: "))
    content = str(input("Napiš text příspěvku: "))
    description = str(input("Napiš krátký popis textu příspěvku: "))
    author = str(input("Napiš autora příspěvku: "))
    imageUrl = str(input("Napiše URL náhledového obrázku: "))

    current_time = datetime.datetime.now()
    createdAt = f"{current_time.day}.{current_time.month}. {current_time.year}"

    #zjištění jestli není žádná hodnota neznámá 
    if name == "" or content == "" or author == "" or description == "" or imageUrl == "":
        print(f"\n{error} | Žádná hodnota nemůže být prázdná!\n")
    else:
        #vytvoření schéma příspěvku
        post = {
            "name": author,
            "title": name,
            "content": content,
            "description": description,
            "imageUrl": imageUrl,
            "createdAt": createdAt
        }

        #uložení příspěvku do databáze
        savePost = main.collection.insert_one(post)

        print(f'{Fore.GREEN}ÚSPĚCH {Style.RESET_ALL}| Příspěvěk byl poslán do databáze! (id: {savePost.inserted_id})\n')