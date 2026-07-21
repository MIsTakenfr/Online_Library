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
                    print(f"\nName: {id["name"]}\nID: {id["id"]}\nEmail: {id["email"]}\nPhone number: {id["phone"]}\nNumber of books that they can borrow at this time: {id["max_books_allowed"]}\n")
                    #enter how many books they have borrowed rn
                    break
                else:
                    print("No one in the library has that id, try again")
        elif search_choice.strip() == "2":
            search_name = input("enter the username of the person that you want to find.")
            for name in members_list:
                if name["name"] == search_name:
                    print(f"Name: {name["name"]}\nID: {name["id"]}\nEmail: {name["email"]}\n Phone number: {name["phone"]}\n Number of books that they can borrow at this time: {name["max_books_allowed"]}")
                    #^
                    break
                else:
                    print("No one in the library has that name, try again")
        else:
            print("What you entered was not an option, enter either 1 or 2")


def members_menu():
    print(" Members Menu ".center(30, "="))
    print("\nPress 1. Add member")
    print("\nPress 2. View members")
    print("\nPress 3. Search member")
    print("\nPress 4. Delete member")
    return input("\nPlease select members menu choice : ")
    


def main_menu():
    print(" Main Menu ".center(30, "="))
    print("\nPress 1. Books Menu")
    print("\nPress 2. Members Menu")
    return input("\nPlease select main menu choice : ")

def delete_member():
    method = input("\nPress 1 to use their ID, and press 2 to use their name. ")
    if method.strip() == "1":
        id_delete = input("Enter their id: ")
        for id in members_list:
            if id["id"] == id_delete:
                members_list.remove(id)
                with open("members.json", "w") as file:
                    json.dump(members_list, file, indent=4)
                