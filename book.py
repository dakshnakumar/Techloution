# book.py
from models import Book
from storage import Storage

class BookManager:
    def __init__(self, storage):
    
     """
     Initialize the BookManager with a storage object.
     Load the books from the storage and store them in the `books` attribute.

     Args:
     storage (Storage): An instance of the Storage class that handles the storage and retrieval of data.

     Returns:
     None
     """
        
     self.storage = storage
     self.books = self.storage.load_books()
        

    def add_book(self, book):

        """
        Add a new book to the list of books.

        Args:
        book (Book): An instance of the Book class that contains the details of the new book.

        Returns:
        None
        """

        existing_book = self.get_book_by_isbn(book.isbn)
        if existing_book:
            return print("The ISBN number already exists, Try with different number")
        else:
            self.books.append(book)
            self.storage.save_books(self.books)
            return print("Book added successfully")

    def update_book(self, isbn, title=None, author=None):

        """
        Update the details of an existing book.

        Args:
        isbn (str): The ISBN number of the book to be updated.
        title (str, optional): The new title of the book. Defaults to None.
        author (str, optional): The new author of the book. Defaults to None.

        Returns:
        None

        """
        
        book = self.get_book_by_isbn(isbn)
        if book:
            if title:
                book.title = title
            if author:
                book.author = author
            self.storage.save_books(self.books)

    def delete_book(self, isbn):
        """
        Delete a book from the list of books.

        Args:
        isbn (str): The ISBN number of the book to be deleted.

        Returns:
        None 
        """

        book = self.get_book_by_isbn(isbn)
        if book:
            self.books.remove(book)
            self.storage.save_books(self.books)
            return print("Book deleted successfully")
        else:
            return print("To delete the book, add the book first")

    def list_books(self):

        """

        List all the books in the storage.

        Returns:
        A list of all the books in the storage.


        """

        return self.books

    def search_books(self, title=None, author=None, isbn=None):

        """
        Search for books based on title, author, or ISBN.

        Args:
        title (str, optional): The title of the book to search for. Defaults to None.
        author (str, optional): The author of the book to search for. Defaults to None.
        isbn (str, optional): The ISBN number of the book to search for. Defaults to None.

        Returns:
        A list of books that match the search criteria.
        """

        results = []
        for book in self.books:
            if book.available and (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (isbn and isbn == book.isbn):
                results.append(book)
        return results

    def get_book_by_isbn(self, isbn):
       
        """
        Search for a book by its ISBN number.

        Args:
        isbn (str): The ISBN number of the book to search for.

        Returns:
        A Book object if the book is found, otherwise None.
        """

        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def update_book_availability(self, book, available):

        """
        Update the availability status of a book.

        Args:
        book (Book): The book object to update.
        available (bool): The new availability status of the book.

        Returns:
        None

        This method updates the availability status of a book. It takes a book object 
        and a boolean value representing the new availability status. 
        It then updates the availability attribute of the book object and saves 
        the updated list of books to the storage.
        """

        book.available = available
        self.storage.save_books(self.books)



