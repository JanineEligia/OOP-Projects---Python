# OOP #4 : Library Management System

class Book:

    def __init__(self, title, author, isbn, available):

        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):

        return f"{self.title} by {self.author} - {self.isbn}"

    def display_info(self):

        print(f"{self.title} by {self.author} - {self.isbn}")

        availablity = "Available" if self.available else "Borrowed"

        print(availablity)

    def borrow_book(self):

        if self.available:

            self.available = False
            
            print("Book borrowed successfully!")

        else:

            print("Sorry, this book is unavailable :(")

    def return_book(self):

        self.available = True

        print("Book returned successfully!")

class Library:

    def __init__(self):

        self.books = []

    def add_book(self):

        new_book_title = input("Enter New Book's Title: ")
        new_book_author = input("Enter New Book's Author: ")
        new_book_isbn = input("Enter New Book's ISBN: ")
        availability = True

        for book in self.books:

            if new_book_isbn == book.isbn:

                print("ISBN already Exist")
                return

        self.books.append(Book(new_book_title, new_book_author, new_book_isbn, availability))

        print("Book Successfully Added!")

    def remove_book(self):

        target_book = input("Input Book's ISBN: ")

        for book in self.books:

            if target_book == book.isbn:

                self.books.remove(book)
                print("Book Removed Successfully!")
                return

        print("This Book Not Found.") 

    def search_book(self):

        target_book = input("Input Book's ISBN: ")

        for book in self.books:

            if target_book == book.isbn:

                book.display_info()
                return
            
        print("Book Not Found.") 
        
    def borrow_book(self):
        
        target_book = input("Input Book's ISBN to Borrow: ")

        for book in self.books:

            if target_book == book.isbn:

                book.borrow_book()
                return
            
        print("Book Not Found.")

    def return_book(self):

        target_book = input("Enter Book's ISBN to Return: ")

        for book in self.books:

            if target_book == book.isbn:

                book.return_book()
                return
            
        print("Book Not Found.")

    def show_books(self):

        for book in self.books:

            book.display_info()

        if not self.books:

            print("There are currently no books in the libary")

library = Library()

while True:

    print("===== Library System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Show All Books")
    print("7. Exit")
    print("==========================")

    choice = input("Plz Enter the Number of your Desired Operation: ")

    if choice == "1":

        library.add_book()

    elif choice == "2":

        library.remove_book()

    elif choice == "3":

        library.search_book()

    elif choice == "4":

        library.borrow_book()

    elif choice == "5":

        library.return_book()

    elif choice == "6":

        library.show_books()

    elif choice == "7":

        print("Thank Your for Using the Program :D")
        break

    else:

        print("Plz Enter A Valid Number from the Menu Above.")