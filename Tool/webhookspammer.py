import os, sys, aiohttp, asyncio, time, colorama
from colorama import Fore
print(f"""{Fore.LIGHTBLUE_EX}



██████╗░░█████╗░██████╗░░██████╗░░█████╗░
██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗
██████╦╝██║░░██║██████╔╝██║░░██╗░██║░░██║
██╔══██╗██║░░██║██╔══██╗██║░░╚██╗██║░░██║
██████╦╝╚█████╔╝██║░░██║╚██████╔╝╚█████╔╝
╚═════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░░╚════╝░

░██╗░░░░░░░██╗███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗ 
░██║░░██╗░░██║██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝ 
░╚██╗████╗██╔╝█████╗░░██████╦╝███████║██║░░██║██║░░██║█████═╝░ 
░░████╔═████║░██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔═██╗░ 
░░╚██╔╝░╚██╔╝░███████╗██████╦╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗ 
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝ 
\n 
░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝


{Fore.RESET}""")

class WebhookSpammer:

    def __init__(self, webhook: str, msg: str, tasks: int):
        self.clear = lambda: os.system("cls; clear")
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47"}
        self.webhook = webhook
        self.payload = {"content": msg}
        self.tasks = tasks

    async def webhook_spammer(self, session, webhook, amount):
       while True:
           async with session.post(webhook, json=self.payload) as s:
              if s.status in (200, 201, 204):
                  sys.stdout.write(f"-> Ho inviato  {amount} messagi .\n\n")
              else:
                  json = await s.json()
                  sys.stdout.write(f"-> Errore inviando  {amount} messaggi.\n-> Message: {json['message']}\n-> Riprova Fra: {json['retry_after']}\n\n")
  
    async def start(self):
        self.clear()
        async with aiohttp.ClientSession(headers=self.headers) as session:
            tasks = []
            for amount in range(self.tasks):
                tasks.append(asyncio.create_task(self.webhook_spammer(session, self.webhook, amount)))
            await asyncio.gather(*tasks)
            tasks.clear()

if __name__ == "__main__":
    try:
        client = WebhookSpammer(
        webhook = input(f"{Fore.RED}[1] {Fore.RESET} Webhook URL?: "),
        msg = input("-> Messaggio??: "),
        tasks = int(input("-> Quantità di messaggi?: "))
        )
        start_time = time.time()
        asyncio.get_event_loop().run_until_complete(client.start())
        finish_time = round((time.time() - start_time), 4)
        sys.stdout.write(f"-> Ho finito  in {finish_time}secondi.")
    except Exception as error:
        sys.stdout.write(f"{Fore.RED}[!] {Fore.RESET}Ho finito di spammare, oppure stai essendo ratelimitato.\n Errore: {error}.\n{Fore.RED} [!] {Fore.RESET} Premi INVIO per uscire.\n")
        input("-> ")
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