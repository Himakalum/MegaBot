import time
import urllib
import sys
import os

os.system('clear')

bar = "\033[1;33;40m\n_________________________________________________\n"

name = """\033[1;32;40m
_______________________________________________________________________
\033[1;33;40m      __  __               _      ____        _   _
\033[1;31;40m     |  \/  | ___  __ _   / \    |  _ \ _   _| \ | |
\033[1;33;40m     | |\/| |/ _ \/ _` | / O \   | |_) | | | |  \| |
\033[1;31;40m     | |  | |  __/ (_| |/ ___ \  |  _ <| |_| | |\  |
\033[1;33;40m     |_|  |_|\___|\__, /_/   \_\ |_| \_\\____/|_| \_|
\033[1;31;40m                  |___/

\033[1;36;40m              [+] Tool Created by Sri Lanka
\033[1;32;40m________________________________________________________________________
"""
print(name, "")


try:
    f = open("auth.txt", "r")
    auth = f.read()
    f.close 
except:
    wr = os.environ.get('auth')


try:
    f = open("url.txt", "r")
    f = open("url.txt", "r")
    url1 = f.read()
    f.close
except:
    wr = os.environ.get('url')
    url1 = wr
try:
    import requests


except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    print('%s Requests has been installed.')
    os.system('clear')
    import requests


def main():
    os.system("clear")
    print(name,"\n")
    s = int(os.environ.get('s'))
    header = {"Host": "megarun.dialog.lk",
              "Authorization": wr, "X-Unity-Version": "2018.3.0f2"}
    url = os.environ.get('url')
    
    ss = 0
    while s > ss:
        os.system("clear")
        print(name)
        size = 0
        res = requests.get(url, headers=header)
        resp = str(res)
        if resp == '<Response [204]>':
            print(bar)
            print("\n\033[1;32;40m [+] No Data ... [+]")
            print(bar)  
        elif resp == '<Response [200]>':
            print(bar)
            print("\n\033[1;32;40m [+] You Won Check Your Data Balance ... [+]")
            print(bar)
        else:
            print(bar)
            print("\n\033[1;31;40m [+] Check Again, I think You are Blocked User... [+]")
            print(bar)
        

        ss+=1
        print("\033[1;0;40m\n",str(ss), "Please Wait For Next Request",end="")
        for i in range(200):
            
            pr = i/200*100
            print("\033[1;36;40m\n>>> [+]",str(int(pr)) +"% ",end="")
            
            time.sleep(0.5)
            sys.stdout.write("\033[F")
        
    os.system('figlet FINISHED')
    again()


def again():
    again = input('\033[1;0;40m\nDo You want use again (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()
