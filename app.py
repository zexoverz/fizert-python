import sys
import json
import pandas as pd

command = sys.argv[1]
argument = sys.argv[2:7]

# JSON file
userFile = open ('./db/user.json', "r")
productFile = open ('./db/product.json', "r")

userData = json.loads(userFile.read())
productData = json.loads(productFile.read())


# FIZERT COMMAND
"""
> python app.py register <username> <password> 
> python app.py login <username> <password>
> python app.py product-list 
> python app.py buy <productName> 


NOTE :
1. BUY PRODUCT WAJIB LOGIN
2. TIDAK BISA LOGIN BERSAMAAN
3. HANYA ADMIN SAJA YANG BISA MENAMBAHKAN LIST PRODUCT
"""

def docs():
    print(" ")
    print("Command List --")
    print("> python app.py start (Start App)")
    print("> python app.py register <username> <password>")
    print("> python app.py login <username> <password>")
    print("> python app.py product-list ")
    print("> python app.py buy <productIndex> ")
    print("\n")
    print("NOTE :")
    print("1. BUY PRODUCT WAJIB LOGIN")
    print("2. TIDAK BISA LOGIN BERSAMAAN")
    print("3. HANYA ADMIN SAJA YANG BISA MENAMBAHKAN LIST PRODUCT")
    print("\n")

## --> Logic Feature

def register(username = '', password = ''):
    data = userData

    # Register Validation
    user = list(filter(lambda item: item['username'] == username, data))       

    if(len(username) == 0):
        print("Error ->> Please input username")
        return

    if(len(password) == 0):
        print("Error ->> Please input password")
        return

    if(len(user) != 0):
        print("Error ->> Username Already Registered.")
        return
    
    newUser = {
        "username" : username,
        "password" : password,
        "role" : "admin",
        "status_login" : False
    }

    data.append(newUser)

    # print(data)
    with open("./db/user.json", "w") as outfile:
        json.dump(data, outfile)

    print("Register User Success ")
    print(newUser)


def login(username, password):
    data = userData

    # Register Validation
    if(len(username) == 0):
        print("Error ->> Please input username")
        return

    if(len(password) == 0):
        print("Error ->> Please input password")
        return

    # Check User Already Login
    check = list(filter(lambda item: item['status_login'] == True, data))

    if(len(check) != 0):
        print("Error ->> User Already Login, please logout first then login again.")
        return
    
    # User login logic
    user = list(filter(lambda item: item['username'] == username, data))

    if(len(user) == 0):
        print("Error ->> User Not Found")
        return

    if(password != user[0]['password']):
        print("Error ->> Wrong Password, please input again.")
        return

    # Update Status Login
    def updateStatusLogin(item):
        if(item['username'] == username):
            item['status_login'] = True
        return item
    
    data = list(map(updateStatusLogin, data))

    # Write to JSON
    with open("./db/user.json", "w") as outfile:
        json.dump(data, outfile)

    print("Login User Success ")
    print("username : " + username)
    

def productList():
    if(userLogin == "User Not Login"):
        print("Error ->> User need login to see product list")
        return

    print(pd.DataFrame(productData, columns=["name", "stock", "price", "size"]))




## --> Menu Set Up
user = list(filter(lambda item: item['status_login'] == True, userData))
userLogin = "User Not Login"

if(len(user) != 0):
    userLogin = user[0]['username']

def switch(command):
    if command == "register":
        register(argument[0], argument[1])
    elif command == "login":
        login(argument[0], argument[1])
    elif command == "product-list":
        productList()
    else :
        docs()
        print("please input correct command")

print("\n")
print('==================== FIZERT APP =======================')
print("Auth Login -> " + userLogin)
switch(command)



