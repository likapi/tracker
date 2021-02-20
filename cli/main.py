#!/usr/bin/python3
from os import system, name
from sys import platform as _platform
from time import sleep
import pyfiglet
from pyfiglet import Figlet
import colorama
from colorama import Fore, Back, Style
import urllib.request, json
import datetime

#config
colorama.init() #colorama init
font = Figlet(font='graffiti') #pyfiglet font
now = datetime.datetime.now() #datetime get time

def sys():
	if _platform == "linux" or _platform == "linux2":
		main()
	elif _platform == "darwin":
		print(Fore.GREEN + """
	Mac Os détecté, vous devez utiliser linux...
		""")
		close()
	elif _platform == "win32" or _platform == "win64":
		print(Fore.GREEN + """
	Windows détecté, vous devez utiliser linux...
		""")
		close()
	else:
		print(Fore.GREEN + """
	Impossible d'identifier le système d'exploitation...
		""")
		close()

def banner():
	banner = font.renderText("  LikapiTrack")
	print(Fore.RED + banner + """
		--- """,module_name,""" ---""")
	print(Fore.CYAN + """
	 Github: https://github.com/likapi
	  Documentation: https://likapi.github.io/docs""" + Fore.MAGENTA + """
	   Instagram: @likapi.sh - Twitter: @likapi_sh
	 """)

def main():
	global module_name
	module_name = "Développé par Keany Vy KHUN"
	banner()
	print(Fore.YELLOW + """
     [1]. Ping     [2]. Recherche     [3]. Bibliothèque     [4]. Historique
     [5]. Service  [6]. Mon Compte    [7]. Documentation    [8]. Notation
     [9]. Aide     [0]. Quitter 
		""")
	menu = input(Fore.WHITE + """
	  Entrez un numéro : """)
	if menu != "":
		if menu == "0":
			close()
		elif menu == "1":
			clear()
			ping()
		elif menu == "4":
			clear()
			history()
		elif menu == "2" or menu == "3" or menu == "5" or menu == "6" or menu == "7" or menu == "8":
			coming()
		else:
			print(Fore.GREEN + """
	  Nombre invalide
			""")
			sleep(2)
			clear()
			main()
	else:
		print(Fore.GREEN + """
	  Aucun nombre sélectionné...
		""")
		sleep(2)
		clear()
		main()

def ping():
	global module_name
	module_name = "Ping APIs (REST)"
	banner()
	hostname = input(Fore.WHITE + """
	  Entrez l'url de l'API : """)
	if hostname != "":
		try:
			response = urllib.request.urlopen(hostname)
			data = json.loads(response.read())
			print("\n	 Status: " + Fore.GREEN + "OK")
			print(Fore.YELLOW + "	 Url:", hostname)
			print(Fore.YELLOW + "	 JSON:",data,"\n\n")
		except ValueError:
			print(Fore.GREEN + """
	  API indisponible...
	 		""")
			sleep(2)
			clear()
			ping()
		else:
			prelog = str(str(now.year)+"/"+str(now.month)+"/"+str(now.day)+"|"+str(now.hour)+"-"+str(now.minute)+"-"+str(now.second))
			log = prelog.replace(" ","")
			history = open("history.txt", "a+")
			history.write(log + "(" + hostname + ")" + "\n")
			history.close()
			exit()
	else:
		print(Fore.GREEN + """
	  Aucune url entrée...
	 	""")
		sleep(2)
		clear()
		ping()

def history():
	global module_name
	module_name = "Historique des APIs"
	banner()
	print(Fore.YELLOW + """
     [1]. Afficher     [2]. Supprimer
		""")
	history = input(Fore.WHITE + """
	  Entrez un numéro : """)
	if history != "":
		if history == "1":
			history_read = open("history.txt", "r+")
			print(Fore.YELLOW + "\n     ",history_read.readlines(),"\n")
			history_read.close()
			exit()
		elif history == "2":
			history_del = open("history.txt", "w+")
			history_del.write("")
			print(Fore.GREEN + """
	  Suppression de l'historique effectuée...
			""")
			history_del.close()
			exit()
		else:
			print(Fore.GREEN + """
	  	Nombre invalide
			""")
			sleep(2)
			clear()
			history()
	else:
		print(Fore.GREEN + """
	  Aucun nombre sélectionné...
		""")
		sleep(2)
		clear()
		history()

def coming():
	print(Fore.GREEN + """
	  Bientôt disponible...
	 """)
	sleep(2)
	clear()
	main()


def close():
	print(Fore.GREEN + """
	  Fermeture du client Likapi...
		""")
	exit()

def clear():
	#clear la console
	_ = system('clear') 

if __name__ == "__main__":
	clear()
	sys()
