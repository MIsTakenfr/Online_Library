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
    identity = input("How would you like to identify the book you want to borrow? \npress 1 to use the ISBN, or, \npress 2 to use the name.")
    if identity == "1":
        isbn_from_user = input("enter the name ISBN number here: ")
        for book in books_data:
            if book["isbn"] == isbn_from_user:
                print(f"{book["id"]} andddddd {book["copies"]}")
                copies = book["copies"]
                check_if_books_more_than_1(copies)


#Check to see if they exist. if the book they want to borrow is in the library. check if ther are more than 1 copies available. check if they have reached their borrowing limit.

borrow_a_book()


