import os
import sys
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

def print_logo():
    print(Fore.CYAN + Style.BRIGHT + r"""
  ______   ____   ____    _____  
 /___  /  / __ \ / __ \  / ___/  
   / /  / / / // / / // /_/ _/   
  / /__/ /_/ // /_/ // / /    
 /_____/\____/ \____/ /__/    
                                
    """)
    print(Fore.GREEN + "        === Bienvenue dans ZOOP ===\n")

def show_menu():
    print(Fore.YELLOW + "Choisis une plateforme :")
    print("  1 = YouTube")
    print("  2 = TikTok")
    print("  3 = Instagram")
    print("  0 = Quitter\n")

def get_url():
    return input(Fore.WHITE + "\nEntre l'URL de la vidéo : ").strip()

def get_format():
    fmt = input("Format souhaité (mp3 / mp4) : ").strip().lower()
    if fmt not in ['mp3', 'mp4']:
        print(Fore.RED + "Format invalide.")
        return get_format()
    return fmt

def call_youtube():
    try:
        subprocess.run(['python', 'youtube.py'])
    except Exception as e:
        print(Fore.RED + f"Erreur pendant l’exécution : {e}")


def call_tiktok():
    try:
        subprocess.run(['python', 'tiktok.py'])
    except Exception as e:
        print(Fore.RED + f"Erreur pendant l’exécution : {e}")

def call_instagram():
    try:
        subprocess.run(['python', 'instagram.py'])
    except Exception as e:
        print(Fore.RED + f"Erreur pendant l’exécution : {e}")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_logo()
        show_menu()
        choice = input(Fore.WHITE + "Ton choix : ").strip()

        if choice == '0':
            break
        elif choice == '1':
            call_youtube()
        elif choice == '2':
            call_tiktok()
        elif choice == '3':
            call_instagram()
        else:
            print(Fore.RED + "Choix invalide.")
            input("Press Enter pour réessayer...")

if __name__ == '__main__':
    main()
