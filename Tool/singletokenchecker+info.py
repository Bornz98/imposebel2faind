import os, requests, colorama
from colorama import Fore
print(f"""



██████╗░░█████╗░██████╗░░██████╗░░█████╗░  ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗  ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║
██████╦╝██║░░██║██████╔╝██║░░██╗░██║░░██║  ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║
██╔══██╗██║░░██║██╔══██╗██║░░╚██╗██║░░██║  ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║
██████╦╝╚█████╔╝██║░░██║╚██████╔╝╚█████╔╝  ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║
╚═════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░░╚════╝░  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝

██╗███╗░░██╗███████╗░█████╗░
██║████╗░██║██╔════╝██╔══██╗
██║██╔██╗██║█████╗░░██║░░██║
██║██║╚████║██╔══╝░░██║░░██║
██║██║░╚███║██║░░░░░╚█████╔╝
╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░

{Fore.RESET}
""")

token = input(f"-> {Fore.RED}Token:{Fore.RESET}")
head = {'Authorization': str(token)}
r = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
if r.status_code == 200:
        print(f'{Fore.GREEN} Token Valido!')
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        print(f'''
        [User Name] {userName}
        [2 Factor] {mfa}
        [Email] {email}
        [Phone number] {phone}
            ''')
        input("Premi invio per continuare")
        os.system("python BORGOTOOL.py")
else:
        print(f"{Fore.RED} Token Invalido! {Fore.RESET}")
def scelta():
    print("Tornare al tool o chiudere il cmd? 1/2")
    respost = input()
    if respost == "1":
        os.system("cls && python BORGOTOOL.py")
    elif respost == "2":
        os._exit()
    else:
        pass
scelta()