import time
from datetime import datetime, timedelta
import os
import pwd
import grp
import subprocess
import bcrypt
import crypt


def welcome():
    lines = ["",
    " _______   __    __        ________                      __           ",
    "|       \ |  \  |  \      |        \                    |  \          ",
    "| $$$$$$$\| $$  | $$       \$$$$$$$$  ______    ______  | $$ __    __ ",
    "| $$__/ $$ \$$\/  $$         | $$    /      \  /      \ | $$|  \  /  \\",
    "| $$    $$  >$$  $$          | $$   |  $$$$$$\|  $$$$$$\| $$ \$$\/  $$",
    "| $$$$$$$  /  $$$$\          | $$   | $$  | $$| $$  | $$| $$  >$$  $$ ",
    "| $$      |  $$ \$$\         | $$   | $$__/ $$| $$__/ $$| $$ /  $$$$\ ",
    "| $$      | $$  | $$         | $$    \$$    $$ \$$    $$| $$|  $$ \$$\\",
    " \$$       \$$   \$$          \$$     \$$$$$$   \$$$$$$  \$$ \$$   \$$",
    "                                                                      ",
    "                                             Helping you take control.",
    "                                                 www.pxtoolx.com      ",
    ""]
    for x in lines:
        print(x)
        time.sleep(0.1)


def licence(name, key):
    try:
        pwd.getpwnam(name)
        gid = grp.getgrnam('pxusers').gr_gid
        subprocess.run(["usermod", "-aG", "pxusers", name])
    except KeyError:
        print(f"user {name} or group pxusers not found")
        return
    else:
        file = f"{os.path.dirname(os.path.realpath(__file__))}/licences/{name}.licence"
        index = 0
        max_index = len(key) - 1
        limit = input(f"enter daily limit for {name}:>>")
        xall = f"0,{limit},{datetime.today() - timedelta(3)}"
        data = bytes(xall, 'utf-8')
        try:
            with open(f"/home/{name}/fm.txt", 'w') as f:
                f.write("<p> Hello Word </p>")
                os.chown(f.name, -1, gid)
                os.chmod(f.name, 0o777)
            with open(f"/home/{name}/leads.txt", 'w') as f:
                f.write("example-email@163.com, Name, Company Name\nexample2@gmail.com, Name Example, 2nd Company Name")
                os.chown(f.name, -1, gid)
                os.chmod(f.name, 0o777)
            with open(f"/home/{name}/links.txt", 'w') as f:
                f.write("google.com, 2ndlink-if-any.com, 3rdlink-and-so-on.com.cn")
                os.chown(f.name, -1, gid)
                os.chmod(f.name, 0o777)
            with open(file, 'wb') as f:
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    f.write(xor_byte.to_bytes(1, 'little'))
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1
                os.chown(f.name, -1, gid)
                os.chmod(f.name, 0o777)
        except Exception as ex:
            print(f"last error >> {ex}")
        else:
            print(f"Licence created successfully for {name}")


def createuser(name):
    password = f"pX-{name.capitalize()}TimePa$$"
    encPass = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))
    subprocess.run(["useradd", "-p", encPass, name])
    print(f"User {name} created successfully")
    licence(name, password)


def check_password(password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    if bcrypt.checkpw(password.encode(), hashed_password):
        return True
    else:
        return False


def check_group_create():
    try:
        grp.getgrnam('pxusers')
        #print("Group 'pxusers' already exists.")
    except KeyError:
        os.system("groupadd pxusers")
        #print("Group 'pxusers' created.")


while True:
    os.system('clear')
    welcome()
    pxm = input("Enter admin password to create user ::>")
    if check_password(pxm):
        check_group_create()
        name = input("Enter username to be created ::>")
        try:
            createuser(str(name))
        except Exception as ex:
            print(f" error creating user >> {ex}")
            time.sleep(1)
            continue
        else:
            break
    else:
        print("Incorrect Password")
