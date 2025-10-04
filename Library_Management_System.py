class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.borrowed:
                book.borrowed = True
                return f"You have borrowed {title} by {book.author}"
        return "Book not available"

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.borrowed:
                book.borrowed = False
                return f"You have returned {title} by {book.author}"
        return "Book not borrowed"

library = Library()
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")

while True:
    print("1. Borrow book")
    print("2. Return book")
    choice = input("Choose an option: ")
    if choice == "1":
        title = input("Enter book title: ")
        print(library.borrow_book(title))
    elif choice == "2":
        title = input("Enter book title: ")
        print(library.return_book(title))
