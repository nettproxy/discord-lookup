import colorama, websocket, time, os, ctypes, shutil, urllib.request
from colorama import Fore, Style
colorama.init(autoreset=True)

debugmode = True
threaddebugmode = False
debugmode2 = True

def debug(*args, **kwargs):
    if debugmode == True:
        print(Fore.YELLOW + "[DEBUG]", *args, **kwargs)

def bridge(*args, **kwargs):
    if debugmode == True:
        print("")
        print(Fore.LIGHTYELLOW_EX + "[BRIDGE]", *args, **kwargs)

def info(*args, **kwargs):
    if debugmode == True:
        print(Fore.BLUE + "[INFO]", *args, **kwargs)
def success(*args, **kwargs):
    if debugmode == True:
        print(Fore.GREEN + "[SUCCESS]", *args, **kwargs)

def error(*args, **kwargs):
    if debugmode == True:
        print(Fore.RED + "[ERROR]", *args, **kwargs)

def offset(*args, **kwargs):
    if debugmode == True:
        print(Fore.GREEN + "[OFFSET]", *args, **kwargs)

def printthread(*args, **kwargs):
    if threaddebugmode == True:
        print(Fore.MAGENTA + "[THREADS]", *args, **kwargs)

def printsinglethread(*args, **kwargs):
    if debugmode == True and threaddebugmode == False:
        print("")
        print(Fore.MAGENTA + "[THREAD]", *args, **kwargs)
        print("")
