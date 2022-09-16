import main

def getData():
   from colorama import Fore, Style

   #eror zpráva
   error = f"{Fore.RED}ERROR\033[m{Style.RESET_ALL}"

   #vyhledání všech dat z databáze
   items = main.collection.find()
   #počet příspěvků v kolekci
   itemsCount = main.collection.count_documents({})

   if str(itemsCount) == "0": 
      print(f"\n{error} | V dané kolekci se nenachází žádné příspevky!\n")
   else:
      #vypsání všech dat z databáze
      for item in items:
         print(f'\n---------------------------------\n{Fore.GREEN}ID:{Style.RESET_ALL} {item["_id"]}\n - {Fore.GREEN}Nadpis:{Style.RESET_ALL} {item["title"]}\n - {Fore.GREEN}Text:{Style.RESET_ALL} {item["content"]}\n - {Fore.GREEN}Autor:{Style.RESET_ALL} {item["name"]}\n - {Fore.GREEN}Vytvořeno:{Style.RESET_ALL} {item["createdAt"]}\n---------------------------------\n')