class LibraryBook:
    def __init__(self, title, author, publication_year, isbn, available=True):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.available = available
        
    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year}) - ISBN: {self.isbn}"
    
    def check_out(self):
        if not self.available:
            print("Sorry, this book is not available for checkout.")
        else:
            self.available = False
            print("Book checked out successfully.")
    
    def check_in(self):
        if self.available:
            print("This book is already available.")
        else:
            self.available = True
            print("Book checked in successfully.")

class Library:
    def __init__(self):
        self.books = []
        self.total_books = 0
        self.available_books = 0
    
    def add_book(self, book):
        self.books.append(book)
        self.total_books += 1
        self.available_books += 1
        print(f"{book.title} added to the library.")
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            self.total_books -= 1
            self.available_books -= 1 if book.available else 0
            print(f"{book.title} removed from the library.")
        else:
            print("Book not found in library.")
    
    def search(self, term):
        results = []
        for book in self.books:
            if term in book.title or term in book.author:
                results.append(book)
        if results:
            print(f"Search results for '{term}':")
            for book in results:
                print(book)
        else:
            print(f"No results found for '{term}'.")
            
    
    def list_books(self):
        print(f"Total books: {self.total_books}")
        print(f"Available books: {self.available_books}")
        print("All books in the library:")
        for book in self.books:
            print(book)
        print("--------------------")
