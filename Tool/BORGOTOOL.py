from pystyle import Colors, Colorate
from PIL import Image
from colr import Colr
import os
from colorama import Fore
import requests, os
import requests
import random
import os
import multiprocessing
import keyboard
import base64
import sys 
import os, sys, time, os.path, pyperclip, pyautogui, ctypes
from colorama import Fore
from selenium import webdriver
import requests
import psutil
from PIL import Image
import emoji
import pyperclip
from selenium import webdriver
from aiohttp.client import ClientSession
import sys, os, asyncio, shutil, colorama, encodings.idna, time, random
from colorama import Fore
import pymongo
from pymongo.errors import OperationFailure
from pypresence.presence import AioPresence
from tasksio import TaskPool
from aiohttp import client_exceptions
from sys import exit
import asyncio
import pathlib
import re
import sys # to access the system
from pystyle import Colors, Colorate
from pystyle import Write, Colors
from pystyle import Center
from pystyle import Box
import json
from discord_webhook import DiscordWebhook
import time
from random import randint
try:
    import climage
except:
    os.system("pip install climage")
from ribbon import rainbow



class OWL():
    def __init__(self, rpc: AioPresence):
        self.tokens = []
        self.rpc = rpc

        # Checker
        self.checking = False
        self.checked = []
        self.totalChecked = []
        # Checker
        self.center = shutil.get_terminal_size().columns
        for token in open("tokens.txt"):
            if token != '':
                self.tokens.append(
                    token.replace("\n", "").replace('\r\n',
                                                   '').replace('\r', ''))
os.system("color f && cls ")

output = climage.convert('banner.png')
print(output + (Colorate.Vertical(Colors.blue_to_white, Center.XCenter( """

░█████╗░███╗░░██╗░██████╗░███████╗██╗░░░░░░██████╗  ██╗░░░██╗░░███╗░░
██╔══██╗████╗░██║██╔════╝░██╔════╝██║░░░░░██╔════╝  ██║░░░██║░████║░░
███████║██╔██╗██║██║░░██╗░█████╗░░██║░░░░░╚█████╗░  ╚██╗░██╔╝██╔██║░░
██╔══██║██║╚████║██║░░╚██║██╔══╝░░██║░░░░░░╚═══██╗  ░╚████╔╝░╚═╝██║░░
██║░░██║██║░╚███║╚██████╔╝███████╗███████╗██████╔╝  ░░╚██╔╝░░███████╗
╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚══════╝╚═════╝░  ░░░╚═╝░░░╚══════╝
 
\n
 """))))

print((Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter( " \nTool By  Bornz#0001 "))))
print("\n\n\n")
print(Box.DoubleCube("GESTIONE TOKEN         BJD"))
print(Box.DoubleCube("[1] Single Token Checker + Token Info\n[2] Token Login\n[3]Nickname Changer\n[4] Bio Changer \n[5] Multiple Token Checker"))

risposta = Write.Input(Box.Lines("Seleziona un opzione"), Colors.cyan_to_blue, interval=0.0025)






risposta = input("->")
if risposta == "1":
    os.system("cls && python singletokenchecker+info.py")
elif risposta == "2":
    os.system("cls && python webhookspammer.py")
elif risposta == "3":
    os.system("cls && python tokenlogin.py")
elif risposta == "4":
    os.system("cls && python serverjoiner.py")
elif risposta == "6":
    os.system("cls && python tokenchecker+serverraider.py")
