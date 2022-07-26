import os

try:
    from threading import Thread
except:
    os.system("pip install threading")
try:
    from colorama import Fore
except:
    os.system("pip install colorama")
try:
    from requests import post, get
except:
    os.system("pip install requests")
try:
    from time import sleep
except:
    os.system("pip install time")
try:
  from pystyle import Colorate, Colors, Center, Write
except:
    os.system("pip install pystyle")
try:
    from os.path import exists
except:
    os.system("pip install os.path")

try:
    from os import system, name
except:
    os.system("pip install os")
try:
    import string
except:
    os.system("pip install string")
try:
    from random import shuffle
except:
    os.system("pip install random")

def style_print(text, color=Colors.red_to_yellow, interval=0.01):
    Write.Print(text + "\n", color, interval)

def style_input(text, color=Colors.red_to_yellow, interval=0.01):
    result = Write.Input(text, color, interval)
    return result

def is_number(text):
    numbers = list("0123456789")
    for chr in text:
        if not chr in numbers: return False
    return True

if name == "nt":
  def clear(): system("cls")
else:
  def clear(): system("clear")

class Spam:

    def __init__(self, tokens=None, channel_id=None, message=None, delay=None) -> None:

        self.tokens = tokens
        self.channel_id = channel_id
        self.message = message
        self.delay = delay

    def get_accounts(self):
        self.accounts = []
        for token in self.tokens:

            auth = {"authorization": token}

            account = get("https://discord.com/api/users/@me", headers=auth).json()
            self.accounts.append(account)


    def start(self):

        def send(token):

            auth = {"authorization": token}

            if self.message.count("RANDOM") > 0:
                random = list(string.ascii_letters)
                shuffle(random)

                payload = {"content": self.message.replace("RANDOM", "".join(random))}
            else:
                payload = {"content": self.message}

            msg = post(f"https://discord.com/api/channels/{self.channel_id}/messages", headers=auth, data=payload).reason

            if msg == "OK":
                print(Colorate.Horizontal(Colors.red_to_yellow, "Message sent by " + self.accounts[self.tokens.index(token)].get("username")))

        while True:
            for token in self.tokens:

                Thread(target=send, args=(token, )).start()
                sleep(self.delay / 1000)

    def verify_tokens(self):

        succes = []
        fails = []

        for token in self.tokens:

            auth = {"authorization": token}

            response = get("https://discord.com/api/users/@me/guilds", headers=auth)

            if response.reason == "OK":
                succes.append(token)
            else:
                fails.append(token)

        return fails, succes

    def verify_channel_id(self):

        succes = []
        fails = []
        
        for token in self.tokens:

            auth = {"authorization": token}

            response = get(f"https://discord.com/api/channels/{self.channel_id}", headers=auth)

            if response.reason == "OK":
                succes.append(token)
            else:
                fails.append(token)

        return fails, succes

def main():

    title = """

██████╗░░█████╗░██████╗░░██████╗░░█████╗░  ██████╗░░█████╗░██╗██████╗░███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗  ██╔══██╗██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
██████╦╝██║░░██║██████╔╝██║░░██╗░██║░░██║  ██████╔╝███████║██║██║░░██║█████╗░░██████╔╝
██╔══██╗██║░░██║██╔══██╗██║░░╚██╗██║░░██║  ██╔══██╗██╔══██║██║██║░░██║██╔══╝░░██╔══██╗
██████╦╝╚█████╔╝██║░░██║╚██████╔╝╚█████╔╝  ██║░░██║██║░░██║██║██████╔╝███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░░╚════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
"""

    title = Center.XCenter(title)
    title = Colorate.Vertical(Colors.yellow_to_red, title)

    print(f'{Fore.LIGHTBLUE_EX} ' + title)

    if not exists("./tokens.txt") or open("tokens.txt", "r").read() == "":
        style_print("Bro non hai token mettili in  tokens.txt.")
        style_input("Premi INVIO per continuare...")
        open("tokens.txt", "w")
        exit()

    tokens=open("tokens.txt", "r").read().splitlines()

    spam = Spam(
        tokens=tokens
    )

    style_print("Caricamento...\n")

    fails, succes = spam.verify_tokens()

    clear()
    print(title)

    if len(fails) > 0:

        if len(tokens) > len(fails):

            open("invalids_tokens.txt", "w").write("\n".join(fails))

            style_print(f"{len(fails)}/{len(tokens)} non vanno più rip.")
            style_print("i token invalidi sono su  invalids_tokens.txt.")

            y_or_n = ""

            while y_or_n != "y" and y_or_n != "n":
                y_or_n = style_input(f"Vuoi continuare con {len(succes)} tokens ? (y/n) > ")

            if y_or_n == "n":
                style_input("Premi INVIO per continuare...")
                exit()
            if y_or_n == "y":
                for fail in fails: tokens.remove(fail)

        else:
            style_input("Non ci sono token da usare.\nPremi INVIO per continuare...")
            exit()
    
    clear()
    print(title)

    spam.channel_id = style_input("nserisci l'ID del canale dove i token devono spammare -> ")

    clear()
    print(title)

    style_print("Caricamento...")

    fails, succes = spam.verify_channel_id()

    clear()
    print(title)

    if len(fails) > 0:

        if len(tokens) > len(fails):

            open("tokens_failed_acces.txt", "w").write("\n".join(fails))

            style_print(f"{len(fails)}/{len(tokens)} non possono vedere il canale")
            style_print("I token che non possono vedere il canale sono in  tokens_failed_acces.txt")

            y_or_n = ""

            while y_or_n != "s" and y_or_n != "n":
                y_or_n = style_input(f"Vuoi continuare con i  {len(succes)} token ? (s/n) -> ")

            if y_or_n == "n":
                style_input("Premi INVIO per continuare...")
                exit()
            if y_or_n == "s":
                for fail in fails: tokens.remove(fail)

        else:
            style_input("Nessun token può accedere al canale .\n Premi INVIO per continuare...")
            exit()
    
    clear()
    print(title)

    spam.message = style_input("Inserisci il messaggio che deve essere inviato  -> ")

    while len(spam.message) + spam.message.count("RANDOM") * 52 < 1:
        spam.message = style_input("Troppo corto, riprova ->")
    while len(spam.message) + spam.message.count("RANDOM") * 52 > 2000:
        spam.message = style_input("Troppo lungo, riprova > ")

    spam.delay = style_input("Inserisci il ritardo dei messaggi. > ")

    while not is_number(spam.delay):
        style_input("Il ritardo deve essere un numero, riprova. -> ")
    
    spam.delay = int(spam.delay)

    clear()
    print(title)

    style_print("Caricamento...")

    spam.get_accounts()

    clear()
    print(title)

    spam.start()
    


main()

    