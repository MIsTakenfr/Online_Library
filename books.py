import uuid

def add_book():
    new_isbn = input("what is the ISBN of the book? ")
    new_book = input("what's the name of the book? ")
    new_author = input("Who is the author? ")
    new_copies = int(input("How many copies of it are you donating? "))
    new_id = str(uuid.uuid4())
    book = {"id": new_id, "title": new_book, "author": new_author, "isbn": new_isbn, "copies": new_copies}
    books_data.append(book)