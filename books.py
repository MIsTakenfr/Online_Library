import uuid


#imports
#__________________________________________________________________________________________________



books_data = [
    {'id': 1, 'title': 'The Echo of Silence', 'author': 'J.R. Reynolds', 'isbn': '978-754-24-13278-4', 'copies': 4},
    {'id': 2, 'title': 'Whispers in the Wind', 'author': 'Sarah Jenkins', 'isbn': '978-328-27-23434-8', 'copies': 2},
    {'id': 3, 'title': 'Shadows of tomorrow', 'author': 'Michael Chang', 'isbn': '978-704-64-14165-0', 'copies': 2},
    {'id': 4, 'title': 'The Golden Horizon', 'author': 'Elena Rostova', 'isbn': '978-323-39-76237-9', 'copies': 1},
    {'id': 5, 'title': 'Beneath the Sapphire Sky', 'author': 'David Vance', 'isbn': '978-674-35-95181-8', 'copies': 7},
    {'id': 6, 'title': 'Chronicles of the Lost', 'author': 'Amina Yusuf', 'isbn': '978-325-67-87236-4', 'copies': 13},
    {'id': 7, 'title': 'The Midnight Oracle', 'author': "Liam O'Connor", 'isbn': '978-990-10-30926-6', 'copies': 6},
    {'id': 8, 'title': 'Forgotten Realms', 'author': 'Chloe Mercer', 'isbn': '978-384-29-38221-5', 'copies': 2},
    {'id': 9, 'title': 'Secrets of the Ancient Oak', 'author': 'Arthur Pendelton', 'isbn': '978-194-58-22676-5', 'copies': 14},
    {'id': 10, 'title': "The Alchemist's Daughter", 'author': 'Sophia Lin', 'isbn': '978-452-87-44671-0', 'copies': 12},
    {'id': 11, 'title': 'Rivers of Destiny', 'author': 'Marcus Aurel', 'isbn': '978-570-78-26361-6', 'copies': 2},
    {'id': 12, 'title': 'Starlight Melodies', 'author': 'Emily Dickinson', 'isbn': '978-665-47-92397-9', 'copies': 15},
    {'id': 13, 'title': 'The Iron Citadel', 'author': 'Gabriel Garcia', 'isbn': '978-982-56-85674-3', 'copies': 12},
    {'id': 14, 'title': 'Echoes from the Past', 'author': 'Harper Lee', 'isbn': '978-171-15-96673-3', 'copies': 13},
    {'id': 15, 'title': 'Beyond the Horizon', 'author': 'George Orwell', 'isbn': '978-396-20-40512-1', 'copies': 7},
    {'id': 16, 'title': 'The Silent Guardian', 'author': 'Virginia Woolf', 'isbn': '978-384-68-93320-5', 'copies': 3},
    {'id': 17, 'title': 'Tides of Fortune', 'author': 'Leo Tolstoy', 'isbn': '978-479-55-37460-4', 'copies': 12},
    {'id': 18, 'title': 'The Last Ember', 'author': 'Jane Austen', 'isbn': '978-799-92-19358-9', 'copies': 11},
    {'id': 19, 'title': 'Labyrinths of Mind', 'author': 'John Steinbeck', 'isbn': '978-275-78-42087-2', 'copies': 8},
    {'id': 20, 'title': "The Weaver's Loom", 'author': 'Toni Morrison', 'isbn': '978-488-44-93886-8', 'copies': 4},
]


#other data
#_______________________________________________________________________________________________________


def add_a_book():
    new_isbn = input("what is the ISBN of the book?")
    new_book = input("what's the name of the book?")
    new_author = input("Who is the author?")
    new_copies = input("How many copies of it are you donating?")
    new_id = str(uuid.uuid4())
    book = {"id": new_id, "title": new_book, "author": new_author, "isbn": new_isbn, "copies": new_copies}
    books_data.append(book)