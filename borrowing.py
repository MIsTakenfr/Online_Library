#imports
#___________________________________________________________________________________________________
import os
from books import books_list,search_for_book,check_if_books_more_than_1
from currentmembers import search_for_member,check_book_limit


#setup
#___________________________________________________________________________________________________
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "members.txt")

#defs
#___________________________________________________________________________________________________
def borrow_a_book():

    for book in books_list:

        print("To start, confirm who you are\n")
        member_check = search_for_member()
        if not member_check:
            print("You don't exist")

        print("\nNow, what book do you want to borrow?\n\n")
        book_check = search_for_book()
        if not book_check:
            print("that book doesn't exist")

        number_check = check_if_books_more_than_1(book_check)
        if not number_check:
            print("\nthere are none of those left\n")
        else:
            print("hi")
        # book_limit = check_book_limit(member_check)
        # if not book_limit:
        #     print("\nyou can't borrow any more books, return one and than you can.")





#Check to see if they exist. if the book they want to borrow is in the library. check if ther are more than 1 copies available. check if they have reached their borrowing limit.

borrow_a_book()


