This repository contains the codes that covers the following tasks for # LIBRARY-BOOKS:

An implemention of a library management system in Python. The system allows users to add books, remove books, search for books, and display a list of all books in the library. Moreover, Each book has the following attributes: title, author, publication year, and ISBN. Additionally, the system is capable of keeping track of the total number of books in the library, as well as the number of available books (i.e. not currently checked out).


***General implementation***


These codes are for A Python class called `LibraryBook` that represents a single book in the library. The class have the following methods:

A short code snippet that demonstrates how to use the `Library` class to perform the following actions:


- Create a new library object.

- Add three new books to the library.

- Search for books with the search term "Python" and print the results.

- Check out one of the books.

- List all of the books in the library.

- Check in the book that was checked out.

- List all of the books in the library again to verify that the book was checked in successfully.


**---------------------------------**


The main.py file contains an example of how you can use library and libraryBooks classes in a separate Python file


After successful running of main.py the results will be as follows:



Python Crash Course added to the library.
Python for Data Analysis added to the library.
Learning Python added to the library.
Search results for 'Python':
Python Crash Course by Eric Matthes (2015) - ISBN: 978-1593276034
Python for Data Analysis by Wes McKinney (2012) - ISBN: 978-1449319793
Learning Python by Mark Lutz (2013) - ISBN: 978-1449355739
Book checked out successfully.
Total books: 3
Available books: 2
All books in the library:
Python Crash Course by Eric Matthes (2015) - ISBN: 978-1593276034
Python for Data Analysis by Wes McKinney (2012) - ISBN: 978-1449319793
Learning Python by Mark Lutz (2013) - ISBN: 978-1449355739
--------------------
Book checked in successfully.
Total books: 3
Available books: 3
All books in the library:
Python Crash Course by Eric Matthes (2015) - ISBN: 978-1593276034
Python for Data Analysis by Wes McKinney (2012) - ISBN: 978-1449319793
Learning Python by Mark Lutz (2013) - ISBN: 978-1449355739
--------------------
