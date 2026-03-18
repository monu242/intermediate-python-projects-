#this is a project for password manager
from cryptography.fernet import Fernet #to generate the special key using Fernet module 
def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key



key = load_key()
fer = Fernet(key)





def add():
    name = input("Account name: ")
    pwd = input("Password:")

    with open ("password.txt","a") as f:
        f.write(name+"  |  "+fer.encrypt(pwd.encode()).decode() +"\n")


def view():
    with open ("password.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:",user," | Password: ",fer.decrypt(passw.encode()).decode())


while True:
    mode = input("Would you like to add a new password or view the password [for quitting tap 'q'](view,add)  ::: ").lower()

    if mode == "q":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("invalid mode !!! ")
