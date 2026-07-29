import json
import uuid
from validators import new_copy_error

with open("books.json", "r") as file:
    books_list = json.load(file)

######################################################################################################

def add_book():
    new_isbn = input("what is the isbn of the book? ")
    new_book = input("what's the name of the book? ")
    new_author = input("Who is the author? ")
    new_copies = new_copy_error()#this is the best piece of work ive ever done (:
    new_id = str(uuid.uuid4())
    book = {"id": new_id, "title": new_book, "author": new_author, "isbn": new_isbn, "copies": new_copies}
    books_list.append(book)
    with open("books.json", "w") as file:
        json.dump(books_list, file, indent=4)

def books_menu():
    print(" Books Menu ".center(30, "="))
    print("\nPress 1. Add book")
    print("\nPress 2. View books")
    print("\nPress 3. Search book")
    print("\nPress 4. Delete book")
    return input("\nPlease select books menu choice : ")

def view_books():
    for number, thing in enumerate(books_list, 1):
        print(f"{number}.")
        print(f"\t\tID:\t{thing['id']}")
        print(f"\t\tName:\t{thing['title']}")
        print(f"\t\tAuthor:\t{thing['author']}")
        print(f"\t\tisbn:\t{thing['isbn']}")
        print(f"\t\tNumber of copies:\t{thing['copies']}\n")

def search_for_book():
    while True:
        search_name = input("enter the isbn of the book. \n")
        for book in books_list:
            if book["isbn"] == search_name:
                print(f"Name: {book["title"]}\nID: {book["id"]}\nEmail: {book["isbn"]}\nAuthor: {book["author"]}\nNumber of books that are in stock: {book["copies"]}")
                return book
        print("that book doesn't exist")
        return False

def delete_book():
    print(" Delete Book Record ".center(40, "="))
    book_isbn = input("\nEnter the book's isbn : ")
    
    for book in books_list:
        if book["isbn"] == book_isbn:
            books_list.remove(book)
            with open("books.json", "w") as file:
                        json.dump(books_list, file, indent=4)
            
            print("\nBook has been deleted succesfully".upper())
            return
    
    print("\nThere's no such book")
    
    

def check_if_books_more_than_1(copies):
    if copies > 0:
        return True
    return False