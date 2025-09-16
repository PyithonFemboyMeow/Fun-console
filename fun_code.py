#console
import os
import socket
import shutil

print("$/ for conmands in help")

lst_help = "df", "cf", "status", "lf", "host", "meow", "byte"

def byte():
    text = input(">>>")
    br = ' '.join(format(ord(char), '08b') for char in text)
    print(f"$/ {br}")

def meow():
    inp_meow = input(">>>")
    print(f"$/ meow: {inp_meow} :3")

def host():
    hostname = socket.gethostname()
    ip_add = socket.gethostbyname(hostname)
    print(f"$/ {hostname} {ip_add}")

def lf():
    print("$/ tir list")
    for fold in os.listdir():
        print(f"---  {fold}")

def status():
    print("$/ v0.3 Beta, Dev ArduinoCat")

def df():
    try:
        inp_df = input(">>>")
        if os.path.exists(inp_df):
            shutil.rmtree(inp_df)
            print("$/ folder delate")
        else:
            print("$/ not folder")
    except Exception as e:
        print(f"$/ error debug ")

def cf():
    inp_cf = input(">>>")
    os.mkdir(inp_cf)
    print("$/ folder create")

def help_com():
    print(f"$/ {lst_help}")
    
    
def choice_com():
    if user == "help":
        help_com()
    elif user == "cf":
        cf()
    elif user == "df":
        df()
    elif user == "status":
        status()
    elif user == "lf":
        lf()
    elif user == "host":
        host()
    elif user == "meow":
        meow()
    elif user == "byte":
        byte()
        
        
if __name__ == "__main__":
    while True:
        user = input("$ ")
        choice_com()
