from library import Library
from library_book import LibraryBook

# Create a new library object.
library = Library()

# Add three new books to the library.
book1 = LibraryBook("Python Crash Course", "Eric Matthes", 2015, "978-1593276034")
book2 = LibraryBook("Python for Data Analysis", "Wes McKinney", 2012, "978-1449319793")
book3 = LibraryBook("Learning Python", "Mark Lutz", 2013, "978-1449355739")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Search for books with the search term "Python" and print the results.
library.search("Python")

# Check out one of the books.
book2.check_out()

# List all of the books in the library.
library.list_books()

# Check in the book that was checked out.
book2.check_in()

# List all of the books in the library again to verify that the book was checked in successfully.
library.list_books()
