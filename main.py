#_________________________________________________________________________________________________________________
import os
from currentmembers import view_all_members,search_for_member,main_menu,members_menu
from books import books_menu,add_book 
leave = False
goto_signup = True
#___________________________________________________________________________________________________________________
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "members.txt")
#_________________________________________________________________________________________________________________
print("Welcome to the online library!")
print(f"{"_"*100}")
print('')

# while True:
#     if leave == True:
#         break
#     los = login_or_signup()
#     if los == "yes" and goto_signup == True:
#         login_answer = login()
#         if login_answer == True:
#             break
            
#         elif login_answer == "restart":
#             goto_signup = False
#         elif login_answer == "retry":
#             print("")
#         else:
#             print("how the hell did this happen")
#     else:
#         signup()
#         break

# print("bet")

while True:
    main_menu_choice = main_menu()
    if main_menu_choice == "1":
        books_menu_choice = books_menu()
        if books_menu_choice == "1":
            add_book()
        elif books_menu_choice == "2":
            pass
        elif books_menu_choice == "3":
            pass
        elif books_menu_choice == "4":
            pass
        else:
            print("\nInvalid books menu choice")

    elif main_menu_choice == "2":
        members_menu_choice = members_menu()
        if members_menu_choice == "1":
            pass
        elif members_menu_choice == "2":
            view_all_members()
        elif members_menu_choice == "3":
            search_for_member()
        elif members_menu_choice == "4":
            pass
        else:
            print("\nInvalid members menu choice")

else:
    print("Invalid main menu choice".center(30, "*"))










# while True:
#     user_menu_choice = input("What would you like to do? \nPress 1 to add a new book. \nPress 2 to view all books. \nPress 3 to search for a book. \nPress 4 to remove a book. \nPress 5 to view all members. \nPress 6 to search for a member. \nPress 7 to borrow a book. \nPress 8 to remove a book. \nPress 9 to display all borrowed books")
#     if user_menu_choice == "1":
#         new_book = input("what's the name of the book")
#     elif user_menu_choice == "2":
#         pass
#     elif user_menu_choice == "3":
#         pass
#     elif user_menu_choice == "4":
#         pass
#     elif user_menu_choice == "5":
#         view_all_members()
        
#         break
#     elif user_menu_choice == "6":
#         search_for_member()
    

##############$$$$$$$$$$$$$$$$$$###############%%%%%%%%%%%%%%%%%%%%%
#people cant ente str for int stuff make it so