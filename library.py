from library_book import LibraryBook

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
