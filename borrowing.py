#imports
#___________________________________________________________________________________________________
import os
from books import books_data,search_for_book,check_if_books_more_than_1
from currentmembers import search_for_member


#setup
#___________________________________________________________________________________________________
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "members.txt")

#defs
#___________________________________________________________________________________________________
def borrow_a_book():
    while True:
        while True:
            identity = input("How would you like to identify the book you want to borrow? Press 1 to use the ISBN.")
            if identity == "1":
                isbn_from_user = input("enter the name ISBN number here: ")
                for book in books_data:
                    if book["isbn"] == isbn_from_user:
                        copies = book["copies"]
                        member_check = search_for_member()
                        if member_check == False:
                            print("You don't exist")
                            break
                        book_check = search_for_book()
                        if book_check == False:
                            print("that book doesn't exist")
                            break
                        





                check_if_books_more_than_1(copies)


#Check to see if they exist. if the book they want to borrow is in the library. check if ther are more than 1 copies available. check if they have reached their borrowing limit.

borrow_a_book()


