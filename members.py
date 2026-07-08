import os
import uuid
import json



script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "members.txt")
member_usernames = []
member_IDs = []
#make a new one to sign up, make them each only do one thing
def login_1():
    member_yes_or_no = input('Are you a member already? if so, press "1". If not, press "2" in order to register.')
    return member_yes_or_no
member_yes_or_no = login_1()

def login_2():    
    while True:
        if member_yes_or_no.strip() == "1":
            name_check = input("Hello again! Enter your name here: ")
            password_check = input("Enter your ID here: ")
            if name_check in member_usernames and password_check in member_IDs:
                print("Welcome back ",name_check,"!" )
                #global lets_move_on
                #lets_move_on = 1
                break
                
            
            else:
                try_again = ("Your username and/or ID is wrong. Press 1 try again, or press 2 to make a new one?")
                if try_again == "1":
                    print("")
                elif try_again == "2":
                    break
        elif member_yes_or_no.strip() == "2":
            new_username = input("Enter the username you would like to use here: ")
            new_id = str(uuid.uuid4())
            member_usernames.append(new_username)
            #make a dict
            member_IDs.append(new_id)
            file = open(file_path, 'a')
            file.write(new_username)
            file.write("\n")
            file.close()
            print(f'Welcome {new_username}!')
            #global can_we_move_on
            #can_we_move_on = 1
            break

def view_all_members():
    file = open(file_path, "r")
    members = file.read()
    print("the members are:\n ",members)
    file.close()

def search_for_a_member():
    member_search_method = input("press 1 to search for them by name. press 2 to search for them by id")

