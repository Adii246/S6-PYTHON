'''
Problem Statement

A small library wants to manage its book collection efficiently. The library needs a system where:

Books can be added to the library.

Users can borrow (lend) books.

Users can return borrowed books.

The system should keep track of available and borrowed books.

Class Design

We will create a class Library, which will manage a collection of books.

Class: Library

Attributes:

books: A dictionary that stores book titles and their availability status.
Methods:

add_book(title): Adds a book to the library.

lend_book(title, user): Lends a book to a user (only if available).

return_book(title): Returns a book back to the library.

display_books(): Displays all available books.
'''
class library:
    def __init__(self):
        self.books={}
    def add_book(self,title):
        self.books[title]="Available"
    def lend_book(self,title,user):
        if self.books.get(title)=="Available":
            self.books[title]=f"lent to {user}"
            print(f"Book lented to {user}")
        else:
            print("Book not available")
            
   
    def return_book(self,title,user):
        if "lent to" in self.books.get(title):
            self.books[title]="Available"
            print(f"Book returned by {user}")
        

    def display_books(self):
        
        print("BOOKS AND STATUS")
        for title,status in self.books.items():
            print(f"{title}:{status}")
l=library()
l.add_book("PYTHON")
l.add_book("DS")
l.add_book("COMPILER DESIGN")
l.lend_book("PYTHON","ALICE")
l.return_book("PYTHON","ALICE")
l.lend_book("PYTHON","Adi")
l.display_books()






        
