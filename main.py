#_________________________________________________________________________________________________________________
import os
from currentmembers import view_all_members,search_for_member,main_menu,members_menu,delete_member
from books import books_menu, add_book, view_books, search_for_book, delete_book
import json
import uuid
leave = False
goto_signup = True

with open("books.json", "r") as file:
    books_list = json.load(file)
#___________________________________________________________________________________________________________________
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "members.txt")
#_________________________________________________________________________________________________________________
print("Welcome to the online library!")
print(f"{"_"*100}")
print('')





while True:
    main_menu_choice = main_menu()
    if main_menu_choice == "1":
        books_menu_choice = books_menu()
        if books_menu_choice == "1":
            add_book()
        elif books_menu_choice == "2":
            view_books()
        elif books_menu_choice == "3":
            search_for_book()
        elif books_menu_choice == "4":
            delete_book()
        else:
            print("\nInvalid books menu choice")

    elif main_menu_choice == "2":
        members_menu_choice = members_menu()
        if members_menu_choice == "1":
            pass#do later; add member
        elif members_menu_choice == "2":
            view_all_members()
        elif members_menu_choice == "3":
            search_for_member()
        elif members_menu_choice == "4":
            delete_member()
        else:
            print("\nInvalid members menu choice")
    
    elif main_menu_choice == "3":
        print("Exiting, have a nice day.")

    else:
        print("Invalid main menu choice".center(30, "*"))


# if __name__ == "__main__":
#     main()