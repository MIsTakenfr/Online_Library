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
        search_id = input("Enter email: ")
        for member in members_list:
            if member["email"] == search_id:
                print(f"\nName: {member["name"]}\nID: {member["id"]}\nEmail: {member["email"]}\nPhone number: {member["phone"]}\nNumber of books that they can borrow at this time: {member["max_books_allowed"]}\n")
                #enter how many books they have borrowed rn
                return member
        print("No one in the library has that email, try again")
        return False


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
    print("\nPress 3. Exit")
    return input("\nPlease select main menu choice : ")

def delete_member():
    while True:
        method = input("\nPress 1 to use their ID, and press 2 to use their name. ")
        if method.strip() == "1":
            id_delete = input("Enter their id: ")
            for id in members_list:
                if id["id"] == id_delete:
                    members_list.remove(id)
                    with open("members.json", "w") as file:
                        json.dump(members_list, file, indent=4)
                        return
                print("None of the members have that ID")
        elif method.strip() == "2":
            name_delete = input("Enter their name: ")
            for name in members_list:
                if name["name"] == name_delete:
                    members_list.remove(name)
                    with open("members.json", "w") as file:
                        json.dump(members_list, file, indent=4)
                        return
                print("None of the members have that name")

def check_book_limit(max_books):
    if max_books > 0:
        return True
    return False





# for member in members_list:
#     member["id"] = str(uuid.uuid4())
# with open("members.json", "w") as file:
#     json.dump(members_list, file,indent=4)