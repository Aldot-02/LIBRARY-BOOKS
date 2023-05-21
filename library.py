from library_book import LibraryBook

class Library:
    def __init__(self):
        # Initialize the Library object with empty lists for books and attributes to track book counts
        self.books = []  # List to store the books in the library
        self.total_books = 0  # Variable to track the total number of books
        self.available_books = 0  # Variable to track the number of available books

    def add_book(self, book):
        # Add a book to the library
        self.books.append(book)  # Append the book to the list of books
        self.total_books += 1  # Increment the total number of books
        self.available_books += 1  # Increment the number of available books
        print(f"{book.title} added to the library.")

    def remove_book(self, book):
        # Remove a book from the library
        if book in self.books:
            self.books.remove(book)  # Remove the book from the list of books
            self.total_books -= 1  # Decrement the total number of books
            self.available_books -= 1 if book.available else 0  # Decrement the number of available books if the book is available
            print(f"{book.title} removed from the library.")
        else:
            print("Book not found in library.")

    def search(self, term):
        # Search for books in the library based on a search term
        results = []
        for book in self.books:
            if term in book.title or term in book.author:
                results.append(book)  # Add the book to the results if the search term is present in the title or author
        if results:
            print(f"Search results for '{term}':")
            for book in results:
                print(book)  # Print the details of each book in the results
        else:
            print(f"No results found for '{term}'.")

    def list_books(self):
        # Display the details of all the books in the library
        print(f"Total books: {self.total_books}")  # Print the total number of books
        print(f"Available books: {self.available_books}")  # Print the number of available books
        print("All books in the library:")
        for book in self.books:
            print(book)  # Print the details of each book in the library
        print("--------------------")
