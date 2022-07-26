import os,requests,time, colorama
from colorama import Fore

print(f"""{Fore.LIGHTMAGENTA_EX}




██████╗░░█████╗░██████╗░░██████╗░░█████╗░  ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗  ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║
██████╦╝██║░░██║██████╔╝██║░░██╗░██║░░██║  ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║
██╔══██╗██║░░██║██╔══██╗██║░░╚██╗██║░░██║  ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║
██████╦╝╚█████╔╝██║░░██║╚██████╔╝╚█████╔╝  ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║
╚═════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░░╚════╝░  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝

██╗░░░░░███████╗░█████╗░██╗░░░██╗███████╗██████╗░
██║░░░░░██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░░░░█████╗░░███████║╚██╗░██╔╝█████╗░░██████╔╝
██║░░░░░██╔══╝░░██╔══██║░╚████╔╝░██╔══╝░░██╔══██╗
███████╗███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║
╚══════╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝


{Fore.RESET}
""")
time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
print(f"[~~] GitHub : https://github.com/Bornz98 ")
tokenlist = open("tokens.txt").read().splitlines()

for token in tokenlist:
    try:
        print(f"\n[+] Leave all available guilds")
        guildsIds = requests.get("https://discord.com/api/v7/users/@me/guilds", headers={'Authorization': token}).json()
        for guild in guildsIds:
            try:
                requests.delete(
                    f'https://discord.com/api/v7/users/@me/guilds/'+guild['id'],
                    headers={'Authorization': token})
                print(f"\t[!] Left this server: "+guild['name'])
            except Exception as e:
                print(f"\t[!] the following error occurred : {e}")

        print(f"\nHo cancellato tutti i server per : {token}")
    except Exception as e:
        print(f"\tC'è stato un errore con  {token} Errore : {e}")