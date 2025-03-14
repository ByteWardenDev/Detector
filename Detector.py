import os 
os.system("cls")
os.system("title ")
import scapy.all as scapy
from pystyle import *
import time
import re

RED = '\033[1;91m'
WHITE = '\033[0m'
GREEN = '\033[1;32m'
GRAY = '\033[1;90m'
GOLD = '\033[0;33m'
BLUE = '\033[1;34m'
CYAN = '\033[1;36m'

def packet(packet):
    try:
        if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.Raw):
            data = packet.getlayer(scapy.Raw).load
            try:
                data_str = data.decode("utf-8", "ignore")
            except:
                data_str = str(data)
            
            if b"GET /texture" in data or b"/skin" in data:
                timestamp = time.strftime("%H:%M:%S")
                print(f" [{timestamp}] {GRAY}[{RED} + {GRAY}] {WHITE}Player detected!")
                
                username_match = re.search(r"/skin/([a-zA-Z0-9_]{1,16})", data_str)
                if username_match:
                    username = username_match.group(1)
                    print(f" [{timestamp}] {GRAY}[{YELLOW} INFO {GRAY}] {WHITE} Possible username: {username}")
            
            if ("mc." in data_str or "play." in data_str) and "{" not in data_str:
                server_match = re.search(r"((?:mc|play)\.[\w\.-]+\.\w+)", data_str)
                if server_match:
                    server = server_match.group(1)
                    timestamp = time.strftime("%H:%M:%S")
                    print(f" [{timestamp}] {GRAY}[{RED} + {GRAY}] {WHITE} Server detected: {server}")
    except Exception as e:
        pass

def main():
    art = f"""
       ██████╗ ███████╗████████╗███████╗ ██████╗████████╗ ██████╗ ██████╗ 
       ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗
       ██║  ██║█████╗     ██║   █████╗  ██║        ██║   ██║   ██║██████╔╝
       ██║  ██║██╔══╝     ██║   ██╔══╝  ██║        ██║   ██║   ██║██╔══██╗
       ██████╔╝███████╗   ██║   ███████╗╚██████╗   ██║   ╚██████╔╝██║  ██║
       ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝

                              {BLUE}╭────────────────────╮
                              │ {WHITE}Fork By: {RED}Crusader{BLUE}  │
                              ╰────────────────────╯{WHITE}    
    """
    print(Colorate.Vertical(Colors.white_to_blue, Center.XCenter(art)))
    print()
    
    try:
        scapy.sniff(filter='', prn=packet, store=0)
    except KeyboardInterrupt:
        exit()

if __name__ == "__main__":
    main()
