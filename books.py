import json
import uuid


with open("books.json", "r") as file:
    books_list = json.load(file)

######################################################################################################

def add_book():
    new_isbn = input("what is the ISBN of the book? ")
    new_book = input("what's the name of the book? ")
    new_author = input("Who is the author? ")
    new_copies = int(input("How many copies of it are you donating? "))
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
    with open ("books.json", "r") as file:
        for number, thing in enumerate(books_list, 1):
            print(f"{number}. \t\tID:\t{thing["id"]}\n\t\tName:\t{thing["title"]}\n\t\tAuthor:\t{thing["author"]}\n\t\tISBN:\t{thing["ISBN"]}\n\t\tNumber of copies:\t{thing["number of copies"]}\n")


def search_for_book():
    while True:
        search_choice = input("Press 1 to use their ID \nPress 2 to use their ISBN")
        if search_choice.strip() == "1":
            search_id = input("enter it's id: ")
            for id in books_list:
                if id["id"] == search_id:
                    print(f"\nName: {id["title"]}\nID: {id["id"]}\nISBN: {id["ISBN"]}\nAuthor: {id["author"]}\nNumber of books that are in stock: {id["number of copies"]}\n")
                    break
                else:
                    print("That book is a figment of your imagination, try again")
        elif search_choice.strip() == "2":
            search_name = input("enter the ISBN of the book that you want to find. ")
            for name in books_list:
                if name["ISBN"] == search_name:
                    print(f"Name: {name["title"]}\nID: {name["id"]}\nEmail: {name["ISBN"]}\nAuthor: {name["author"]}\nNumber of books that are in stock: {name["number of copies"]}")
                    #^
                    break
                else:
                    print("That ISBN dosen't exist and it never will, try again")
        else:
            print("What you entered was not an option, enter either 1 or 2")



search_for_book()