import time
from random import randint
import os
import pyperclip

password = ".password.txt"
username = ".username.txt"
path = "."
user_dict = {}

#searching for file
def find(password, username, path):
    print "Searching for File",
    for root, dirs, files in os.walk(path):
        print ".",
        time.sleep(0.5)
        if password in files and username in files:
            print
            return 1
        else:
            print
            return 0

def save(i_username, i_password):
    f_username = open(username, "a+")
    f_password = open(password, "a+")
    f_username.write("%s\n" %(i_username))
    f_password.write("%s\n" % (i_password))
    f_username.close()
    f_password.close()
    return "Username and Password Saved."

def getdir():
    f_username = open(username,"r+")
    f_password = open(password, "r+")
    username_dist = {}
    username_list = []
    for line in f_username:
        username_dist[line.strip()] = ""
        username_list.append(line.strip())

    i = 0
    for line in f_password:
        username_dist[username_list[i]] = line.strip()
        i += 1
    f_password.close()
    f_username.close()
    return username_dist

def set_up():
    if find(password, username, path) == 0:
        f_username = open(username, "w+")
        f_password = open(password, "w+")
        print "\n\n"
        print "******************"
        print "**File Not found**"
        print "******************\n"
        print "Creating file",
        for i in range(randint(1, 10)):
            print ".",
            time.sleep(1)

        print "\nFile created."
        f_password.close()
        f_username.close()
    else:
        print "***File Found***"
        user_dict = getdir()

def run():
    set_up()
    print "\n1. To Save Password"
    print "2. To Retrive Password"
    print "3. To Exit"
    choice = int(raw_input("Enter your Choice: "))

    while True:
        if choice == 1:
            i_username = raw_input("Enter UserName: ")
            i_password = raw_input("Enter Password: ")

            while i_password == "" or i_username == "":
                print "***Username and Password required. Please enter valid username and password.***"
                i_username = raw_input("Enter UserName: ")
                i_password = raw_input("Enter Password: ")

            print save(i_username,i_password)

            while True:
                s_choice = raw_input("\nDo You Want To Continue (y/n): ")
                if s_choice.lower() == 'y':
                    break
                elif s_choice.lower() == 'n':
                    while True:
                        s_choice = raw_input("\n1. To Retrive Your Password \n2. Exit \nChoice:")
                        if int(s_choice) == 1:
                            choice = 2
                            break
                        elif int(s_choice) == 2:
                            print "!!!Thank You!!!"
                            exit()

        elif choice == 2:
            user_dict = getdir()
            print "\n**You are going to retrive your password**"
            r_username = raw_input("Enter username: ")
            while r_username not in user_dict.keys():
                print "\n***Username not found***"
                r_username = raw_input("Enter Username: ")

            r_password = user_dict[r_username]
            pyperclip.copy(r_password)
            spam = pyperclip.paste()
            print "Password \"%s\" for username \"%s\" copied to clipboard." %( "*" * len(r_password), r_username)

            while True:
                s_choice = raw_input("\nDo You Want To Continue (y/n): ")
                if s_choice.lower() == 'y':
                    break
                else:
                    while True:
                        s_choice = raw_input("\n1. To Add Username And Password \n2. Exit \nChoice: ")
                        if int(s_choice) == 1:
                            choice = 1
                            break
                        elif int(s_choice) == 2:
                            print "\n\n!!!Thank You!!!"
                            exit()

        else:
            print "\n\n!!!Thank You!!!"
            exit()





def main():
    run()

if __name__ == '__main__':
    main()