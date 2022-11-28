import sys
import json

command = sys.argv[1]
argument = sys.argv[2:7]

# FIZERT COMMAND
"""
> python app.py register <username> <password> 
> python app.py login <username> <password>
> python app.py product-list 
> python app.py buy <productName> 


NOTE :
1. BUY PRODUCT WAJIB LOGIN
2. TIDAK BISA LOGIN BERSAMAAN
3. HANYA ADMIN SAJA YANG BISA MENAMBAH KAN LIST PRODUCT
"""

def docs():
    print("Command List --")
    print("> python app.py register <username> <password>")
    print("> python app.py login <username> <password>")
    print("> python app.py product-list ")
    print("> python app.py buy <productName> ")
    print("\n")
    print("NOTE :")
    print("1. BUY PRODUCT WAJIB LOGIN")
    print("2. TIDAK BISA LOGIN BERSAMAAN")
    print("3. HANYA ADMIN SAJA YANG BISA MENAMBAH KAN LIST PRODUCT")
    print("\n")

## --> Logic Feature

def register(username = '', password = ''):
    # JSON file
    file = open ('./db/user.json', "r")
    data = json.loads(file.read())

    # Register Validation
    if(len(username) == 0):
        print("Error ->> Please input username")
        return

    if(len(password) == 0):
        print("Error ->> Please input password")
        return
    
    newUser = {
        "username" : username,
        "password" : password,
        "role" : "user",
        "status_login" : False
    }

    data.append(newUser)

    # print(data)
    with open("./db/user.json", "w") as outfile:
        json.dump(data, outfile)
    print("Register User Success ")
    print(newUser)



## --> Menu Set Up

def switch(command):
    if command == "register":
        register(argument[0], argument[1])
    elif command == "login":
        print("LOGIN")
    else :
        docs()
        print("plesae input correct command")

print("\n")
print('==================== FIZERT APP =======================')
switch(command)



