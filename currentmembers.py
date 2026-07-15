#1 imports
#__________________________________________________________________________________

import os
import uuid
import json
#2 setup
#___________________________________________________________________________________

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "members.txt")
with open("members.json", "r") as file:
    members_list = json.load(file)

#3 funtions
#______________________________________________________________________________________

def login_or_signup():
    while True:
        user_startup_choice = input("If you already have an account, you can login. \nTo do that, press 1. \nIf you're new here, press 2 to signup. ")
        if user_startup_choice.strip() == "1":
            move_login = "yes"
            return move_login
        elif user_startup_choice.strip() == "2":
            move_signup = "no" #<-- he doesnt matter
            return move_signup
        else:
            print("What you entered was not an option, enter either 1 or 2")
                

def login():
    while True:    
        email_or_phone = input("You can log in in using your phone number & username or your email & username. \nPress 1 for email and 2 for phone. ")
        
        
        if email_or_phone.strip() == "1":
            past_username = input("Enter your name here: ")
            past_email = input("Enter your email here: ")
            for mail in members_list:
                while True:
                    if mail["email"] == past_email and mail["name"] == past_username:
                        print(f"Welcome back, {past_username}!")
                        login_done = True
                        return login_done
                    else:
                        while True:
                            restart_email = input("You name and/or email did not match any of our users. \nIf you want to try again, press 1. otherwise, press 2 ")
                            if restart_email.strip == "1":
                                restart = "retry"
                                return restart
                            elif restart_email == "2":
                                restart = "restart"
                                return restart
                                #iykyk
                            else:
                                print("what you entered was not on option, try again.")
        elif email_or_phone.strip() == "2":
            past_username = input("Enter your name here: ")
            past_phone = input("Enter your number here: ")
            for number in members_list:
                while True:
                    if number["phone"] == past_phone and number["name"] == past_username:
                        print(f"Welcome back, {past_username}!")
                        login_done = True
                        return login_done
                    else:
                        while True:
                            restart_phone = input("You name and/or number did not match any of our users. \nIf you want to try again, press 1. otherwise, press 2 ")
                            if restart_phone.strip == "1":
                                restart = "retry"
                            elif restart_phone == "2":
                                restart = "restart"
                                return restart
                                #iykyk
                            else:
                                print("what you entered was not on option, try again.")


def signup():
    new_username = input("Enter the username you would like to use here: ")
    new_id = str(uuid.uuid4())
    new_phone = input("Enter your phone number here: ")
    new_email = input("Enter your email here: ")
    
    print(f"Perfect, Welcome {new_username}! Your ID is: {new_id} \nEnjoy the library!")
    
    members_list.append({"id": new_id, "name": new_username, "email": new_email, "phone": new_phone, "max_books_allowed": 3})
    with open("members.json", "w") as file:
        json.dump(members_list, file, indent=4)

def view_all_members():
    print("\n")
    for number, member in enumerate(members_list, 1):
        print(f"\n{number}.\t\tName: {member["name"]}\n\t\tID: {member["id"]}\n\t\tEmail: {member["email"]}\n\t\tPhone number: {member["phone"]}\n\t\tNumber of books that they can borrow at this time: {member["max_books_allowed"]}")

def search_for_member():
    while True:
        search_choice = input("Press 1 to use their ID \nPress 2 to use their username")
        if search_choice.strip() == "1":
            search_id = input("enter their id: ")
            for id in members_list:
                if id["id"] == search_id:
                    print(f"The person you are looking for is named {id["name"]}")
                    #enter how many books they have borrowed rn
                    break
                else:
                    print("No one in the library has that id, try again")
        elif search_choice.strip() == "2":
            search_name = input("enter the username of the person that you want to find.")
            for name in members_list:
                if name["username"] == search_name:
                    print(f"The id of the person you are looking for is {name["id"]}")
                    #^
                    break
                else:
                    print("No one in the library has that name, try again")
        else:
            print("What you entered was not an option, enter either 1 or 2")