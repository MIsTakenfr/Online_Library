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
            login = "yes"
            return login
        elif user_startup_choice.strip() == "2":
            move_1 = "yes"
            return move_1 #remember to write "move_1 = login_or_signup"
        else:
            print("What you entered was not an option, enter either 1 or 2")
                

def login():
    while True:    
        past_username = input("Enter your username here: ")
        past_id = input("enter your ID here: ")
        if {"username": past_username, "id": past_id} in members_list:
            print(f"Welcome back, {past_username}!")
            #remember to write "move_2 = login_or_signup"
            move_2 = "yes"
            return move_2
        else:
            incorrect = ("Username or ID is incorrect. \n if you would you like to try again, press 1. \nif you want to make a new account, press 2 ")
            if incorrect.strip() == "1":
                print("")
            elif incorrect == "2":
                return_now = "yes"
                #remember
                return return_now
            else:
                print("What you entered was not an option.")
        
                



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