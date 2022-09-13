import main

def getData():
   from colorama import Fore, Style

   #vyhledání všech dat z databáze
   items = main.collection.find()

   #vypsání všech dat z databáze
   for item in items:
      print(f'\n---------------------------------\n{Fore.GREEN}ID:{Style.RESET_ALL} {item["_id"]}\n - {Fore.GREEN}Nadpis:{Style.RESET_ALL} {item["title"]}\n - {Fore.GREEN}Text:{Style.RESET_ALL} {item["content"]}\n - {Fore.GREEN}Autor:{Style.RESET_ALL} {item["name"]}\n---------------------------------\n')