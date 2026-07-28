#imports
#___________________________________________________________________________________________________
import os
from books import books_list,search_for_book,check_if_books_more_than_1
from currentmembers import search_for_member,check_book_limit
import json


#setup
#___________________________________________________________________________________________________
with open("members.json", "r") as file:
    members_list = json.load(file) 

#defs
#___________________________________________________________________________________________________
def borrow_a_book():

    for book in books_list:

        print("To start, confirm who you are\n")
        member_check = search_for_member()
        if not member_check:
            print("You don't exist")

        print(member_check)

        print("\nNow, what book do you want to borrow?\n\n")
        book_check = search_for_book()
        if not book_check:
            print("that book doesn't exist")

        number_check = check_if_books_more_than_1(book_check)
        if not number_check:
            print("\nthere are none of those left\n")
        
        book_limit = check_book_limit(member_check["max_books_allowed"])
        if not book_limit:
            print("\nyou can't borrow any more books, return one and than you can.")

        member_check["max_books_allowed"] = member_check["max_books_allowed"] - 1
        
        #with open("members.json", "w") as file:
        #    json.dump(members_list, file, indent=4)
        print(members_list)
        





#Check to see if they exist. if the book they want to borrow is in the library. check if ther are more than 1 copies available. check if they have reached their borrowing limit.

borrow_a_book()


