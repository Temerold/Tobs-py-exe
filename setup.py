import os
import sys

clear = lambda: os.system('cls')
x = 0
while x == 0:
    try:
        os.system('pip install pyinstaller')
        x = 1
    except:
        try:
            os.sytem("py -m pip install pyinstaller")
            x = 1
        except OSError as e:
            y = 0
            while y == 0:
                print(e)
                ign = input("\nKunde inte installer e 3:dje part modul, \"pyinstaller\". Vill du försöka igen? (y/n):\n")
                if ign == "n":
                    sys.exit()
                elif ign != "y" and ign != "n":
                    print("Svara endast med \"y\" eller \"n\".")
