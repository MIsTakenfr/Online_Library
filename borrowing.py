#imports
#___________________________________________________________________________________________________
import os
from books import books_data


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

borrow_a_book()


