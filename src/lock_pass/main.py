from __future__ import print_function
from getpass import getpass
import ast
import os
import sys
import pyperclip
from subprocess import call

login = ".login.txt"
path = os.path.join(os.path.expanduser('~'))
# user_dict = {}


# searching for file
def find(login, path):
    for root, dirs, files in os.walk(path):
        if login in files:
            return 1
        else:
            return 0


def save(i_username, i_password):
    user_dict = getdir()
    user_dict[i_username] = i_password

    with open(os.path.join(os.path.expanduser('~'), login), "w+") as f:
        f.write("%s" % (user_dict))
    print("Username and Password Saved.")
    return user_dict


def getdir():
    username_dict = {}
    with open(os.path.join(os.path.expanduser('~'), login), "r+") as f:
        for file in f:
            if file == "":
                username_dict = {}
            else:
                username_dict = ast.literal_eval(file.strip())
    return username_dict


def set_up():
    global user_dict
    if find(login, path) == 0:
        with open(os.path.join(os.path.expanduser('~'), login),"w+") as f:
            return {}
    else:
        return getdir()


def run():
    user_dict = set_up()
    print("\n1. To Save Password")
    print("2. To Retrive Password")
    print("3. View Username")
    print("4. To Exit")
    choice = input("Enter your Choice: ").strip()

    while True:
        if choice == "1":
            i_username = input("UserName: ").strip()

            while i_username == "":
                print("***Username required.***")
                i_username = input("UserName: ").strip()

            while i_username in user_dict.keys():
                print("***Username already exist***")
                i_username = input("UserName: ").strip()

            i_password = getpass(prompt="Password: ").strip()
            while i_password == "":
                print("***Password required***")
                i_password = getpass(prompt="Password: ").strip()

            c_password = getpass(prompt="Confirm Password: ").strip()

            while c_password != i_password:
                i_username = input("UserName: ").strip()
                i_password = getpass(prompt="Password: ").strip()
                c_password = getpass(prompt="Confirm Password: ").strip()

            user_dict = save(i_username, i_password)

            while True:
                s_choice = input("\nDo You Want To Continue (y/n): ").strip()
                if s_choice.lower() == 'y':
                    break
                elif s_choice.lower() == 'n':
                    while True:
                        s_choice = input("\n1. To Retrive Your Password \n2. View Username\n3. Exit \nChoice:").strip()
                        if int(s_choice) == 1:
                            choice = "2"
                            break
                        elif int(s_choice) == 2:
                            choice = "3"
                            break
                        elif int(s_choice) == 3:
                            print("!!!Thank You!!!")
                            sys.exit(0)
                        else:
                            continue
                    break

        elif choice == "2":
            user_dict = getdir()
            print("\n**You are going to retrive your password**")
            r_username = input("Enter username: ").strip()

            while r_username not in user_dict.keys():
                print("\n***Username not found***")
                print("\nSome Username And Password are:")
                i = 0
                for user in user_dict.keys():
                    print("%d. %s => %s" % (i, user, "*" * len(user_dict[user])))
                    i += 1
                r_username = input("\nEnter Username: ").strip()

            r_password = user_dict[r_username]
            try:
                pyperclip.copy(r_password)
                print("Password \"%s\" for username \"%s\" copied to clipboard." % ("*" * len(r_password), r_username))
            except Exception:
                print("\nTo install either xclip, xsel, PyQt4 or gtk to run this application properly.")
                call(["sudo", "-S", "apt-get", "install", "xclip"])
                print("\n\n\nYour set has been completed. You can run this application properly now.\n\n\n")
                sys.exit(0)

            while True:
                s_choice = input("\nDo You Want To Continue (y/n): ").strip()
                if s_choice.lower() == 'y':
                    break
                else:
                    while True:
                        s_choice = input(
                            "\n1. To Add Username And Password \n2. View Username \n3. Exit \nChoice: ").strip()
                        if int(s_choice) == 1:
                            choice = "1"
                            break
                        elif int(s_choice) == 2:
                            choice = "3"
                            break
                        elif int(s_choice) == 3:
                            print("\n\n!!!Thank You!!!")
                            sys.exit(0)
                        else:
                            continue
                    break

        elif choice == "3":
            if len(user_dict) == 0:
                print("\nUsername and Password not found.")
                run()

            else:
                print("\n**Saved Username and Password**")
                i = 1
                for user in user_dict.keys():
                    print("%d. %s => %s" % (i, user, "*" * len(user_dict[user])))
                    i += 1
                # print user_dict

                while True:
                    s_choice = input(
                        "\n1. To Add Username And Password \n2. To Retrive Password  \n3. Exit \nChoice: ").strip()
                    if int(s_choice) == 1:
                        choice = "1"
                        break
                    elif int(s_choice) == 2:
                        choice = "2"
                        break
                    elif int(s_choice) == 3:
                        print("\n\n!!!Thank You!!!")
                        sys.exit(0)
                    else:
                        continue

        elif choice == "4":
            print("\n\n!!!Thank You!!!")
            sys.exit(0)

        else:
            print("\n1. To Save Password")
            print("2. To Retrive Password")
            print("3. View Username")
            print("4. To Exit")
            choice = input("Enter your Choice: ").strip()
            continue


def main():
    run()


if __name__ == '__main__':
    main()
