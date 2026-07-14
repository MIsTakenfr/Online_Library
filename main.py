#_________________________________________________________________________________________________________________
import os
from currentmembers import view_all_members, login_or_signup, signup, search_for_member
import json
#___________________________________________________________________________________________________________________
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "members.txt")
#_________________________________________________________________________________________________________________
print("Welcome to the online library!")

login_or_signup()
signup()


while True:
    user_menu_choice = input("What would you like to do? \nPress 1 to add a new book. \nPress 2 to view all books. \nPress 3 to search for a book. \nPress 4 to remove a book. \nPress 5 to view all members. \nPress 6 to search for a member. \nPress 7 to borrow a book. \nPress 8 to remove a book. \nPress 9 to display all borrowed books")
    if user_menu_choice == "1":
        new_book = input("what's the name of the book")
    elif user_menu_choice == "2":
        pass
    elif user_menu_choice == "3":
        pass
    elif user_menu_choice == "4":
        pass
    elif user_menu_choice == "5":
        view_all_members()
        
        break
    elif user_menu_choice == "6":
        search_for_member()
    