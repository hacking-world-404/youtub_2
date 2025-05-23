from os import system as c
import time
import random
import os

# Colors
A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

# Logo
def logo():
    c('clear')
    print(f"""{R}
██████╗  █████╗  ██████╗██╗  ██╗██╗███╗   ██╗
██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║
██████╔╝███████║██║     █████╔╝ ██║██╔██╗ ██║
██╔═══╝ ██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║
██║     ██║  ██║╚██████╗██║  ██╗██║██║ ╚████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
{P} HACKING WORLD - YOUTUBE SUBSCRIBER TOOL
{A}------------------------------------------------
""")

# Root Permission Check
def check_root():
    print(f"{Y}[!] Checking Root Permission...")
    time.sleep(2)
    if os.path.exists("/system/bin/su"):
        print(f"{G}[✓] Root Permission Granted!\n")
        time.sleep(1)
        return True
    else:
        print(f"{R}[x] Root Permission Denied!")
        print(f"{C}Tool cannot run without root permission.")
        exit()

# Subscriber Hack
def sub_hack():
    logo()
    channel = input(f"{C}[+] Enter YouTube Channel ID: ")

    check_root()

    print(f"\n{Y}[*] Connecting to YouTube Server...")
    time.sleep(2)

    print(f"{G}[✓] Channel Found: {channel}\n")
    time.sleep(1)

    subs = random.randint(1000, 5000)
    for i in range(subs, subs+15000, random.randint(500, 1500)):
        print(f"{C}[+] Current Subscribers: {i}")
        time.sleep(0.7)

    print(f"\n{G}[✓] Unlimited Subscribers Sent Successfully!")
    print(f"{P}[*] Note: Open YouTube App to Check Subscribers (Prank!)")
    input(f"\n{C}Press Enter To Exit...")

# Start Tool
sub_hack()