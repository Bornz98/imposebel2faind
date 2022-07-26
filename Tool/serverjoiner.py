import aiohttp, asyncio, colorama, tasksio, os
from colorama import Fore
print(f"""{Fore.LIGHTCYAN_EX}


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
async def join_server(token, inv):
        headers = {"Authorization": token, "accept": "*/*", "accept-language": "en-US", "connection": "keep-alive", "cookie": f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US', "DNT": "1", "origin": "https://discord.com", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "referer": "https://discord.com/channels/@me", "TE": "Trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36", "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"}
        async with aiohttp.ClientSession(headers=headers) as serverjoinersession:
            async with serverjoinersession.post(f"https://discord.com/api/v9/invites/{inv}") as response:
                if response.status in (204, 200, 201):
                    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Un Token è entrato nel server")
                else:
                    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Un token non è riuscito ad entrare nel server, sarà che gli serve la captcha key o è locked lol")
async def start_join(inv):
        async with tasksio.TaskPool(10_000) as pool:
         for token in open('tokens.txt', 'r').readlines():
            tk = token.strip()
        await pool.put(join_server(tk, inv))
try:
        inv = input("Inserisci l'invito del server discord.gg/")
        asyncio.run(start_join(inv))
except:
        print("C'è stato un errore sconosciuto, riprova o vuol dire che Bornz è una pippa")
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