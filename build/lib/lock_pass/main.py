from __future__ import print_function
import os
import sys
import pyperclip

login = ".login.txt"
path = os.path.join(os.path.expanduser('~'))
user_dict = {}

#searching for file
def find(login, path):
     for root, dirs, files in os.walk(path):
        if login in files:
            return 1
        else:
            return 0

def save(i_username, i_password):
    f_login = open(os.path.join(os.path.expanduser('~'), login), "a+")
    f_login.write("%s %s\n" %(i_username, i_password))
    f_login.close()
    print("Username and Password Saved.")
    return getdir()

def getdir():
    f_login = open(os.path.join(os.path.expanduser('~'), login), "r+")
    username_dict = {}
    for line in f_login:
        username_dict[line.split(" ")[0]] = line.split(" ")[1].strip()
    f_login.close()
    return username_dict

def set_up():
    if find(login, path) == 0:
        f_login= open(os.path.join(os.path.expanduser('~'), login), "w+")
        f_login.close()
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
            i_username = input("Enter UserName: ").strip()
            i_password = input("Enter Password: ").strip()

            while i_password == "" or i_username == "":
                print("***Username and Password required. Please enter valid username and password.***")
                i_username = input("Enter UserName: ").strip()
                i_password = input("Enter Password: ").strip()

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
                for user in user_dict.keys():
                    print("%d. %s => %s" %(i,user,"*" * len(user_dict[user])))
                    i += 1
                r_username = input("\nEnter Username: ").strip()

            r_password = user_dict[r_username]
            pyperclip.copy(r_password)

            print("Password \"%s\" for username \"%s\" copied to clipboard." %( "*" * len(r_password), r_username))


            while True:
                s_choice = input("\nDo You Want To Continue (y/n): ").strip()
                if s_choice.lower() == 'y':
                    break
                else:
                    while True:
                        s_choice = input("\n1. To Add Username And Password \n2. View Username \n3. Exit \nChoice: ").strip()
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
                    print("%d. %s => %s" %(i,user,"*" * len(user_dict[user])))
                    i += 1
                # print user_dict

                while True:
                    s_choice = input("\n1. To Add Username And Password \n2. To Retrive Password  \n3. Exit \nChoice: ").strip()
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