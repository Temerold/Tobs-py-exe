import os

print("Inga mellanslag eller \"'\" i filnamn.")
fil = input("Filnamn (.py/.pyw): ")
icon = input("Ikon (.ico): ")
if icon != "":
    icon == " --icon=" + icon + " "
else:
    icon = " "

print("")

os.system("pyinstaller --onefile" + icon + fil)
    
input("\nTryck på enter för att avsluta . . .")
