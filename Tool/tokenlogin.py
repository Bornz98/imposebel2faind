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
import json
from discord_webhook import DiscordWebhook
import time
from random import randint


def main(_token):

        
        try:
            opts = webdriver.ChromeOptions()
            opts.add_experimental_option("detach", True)
            driver = webdriver.Chrome('chromedriver.exe', options=opts)
            script = """
                function login(token) {
                setInterval(() => {
                document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
                }, 50);
                setTimeout(() => {
                location.reload();
                }, 2500);
                }   
               """
            driver.get("https://discordapp.com/login")
            driver.execute_script(script+f'\nlogin("{_token}")')
        
        except:
            print("[{Fore.LIGHTRED}!{Fore.RESET}] C'è stato un errrore col codice")
    
    
if __name__ == '__main__':
        os.system('cls')
        token = input("""
         _                 _         _______    _                    
        | |               (_)       |__   __|  | |                 
        | |     ___   __ _ _ _ __      | | ___ | | _____ _ __      
        | |    / _ \ / _` | | '_ \     | |/ _ \| |/ / _ \ '_ \     
        | |____ (_) | (_| | | | | |    | | (_) |   <  __/ | | |    
        |______\___/ \__, |_|_| |_|    |_|\___/|_|\_\___|_| |_|    
                      __/ |                                                                       
                     |___/                                 
        
       ->  Token: """)
main(token)  


