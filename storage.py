# storage.py
import json
import os
from models import Book, User, Checkout
from datetime import datetime

class Storage:
    def __init__(self, book_file, user_file, checkout_file):

        """
        Initialize the Storage class with the provided file paths for books, users, and checkouts.

        Args:
        book_file (str): The path to the JSON file containing the books data.
        user_file (str): The path to the JSON file containing the users data.
        checkout_file (str): The path to the JSON file containing the checkouts data.

        Attributes:
        book_file (str): The path to the JSON file containing the books data.
        user_file (str): The path to the JSON file containing the users data.
        checkout_file (str): The path to the JSON file containing the checkouts data.
        """
        
        self.book_file = book_file
        self.user_file = user_file
        self.checkout_file = checkout_file

    def load_books(self):

        """
        Load the books data from the JSON file specified by the `book_file` attribute.

        Args:
        None

        Returns:
        A list of `Book` objects loaded from the JSON file. If the file does not exist, an empty list is returned.

        Raises:
        FileNotFoundError: If the `book_file` does not exist.

        Note:
        This method first attempts to open and load the JSON file. If the file does not exist, an empty list is returned.
        """
        
        try:
            with open(self.book_file, 'r') as file:
                book_data = json.load(file)
            books = [Book(**data) for data in book_data]
        except FileNotFoundError:
            books = []
        return books

    def save_books(self, books):

        """
        Save the provided list of books to the JSON file specified by the `book_file` attribute.

        Args:
        books (list): A list of `Book` objects to be saved to the JSON file.

        Returns:
        None

        Raises:
        FileNotFoundError: If the `book_file` does not exist.

        Note:
        This method first checks if the `book_file` already contains data. If it does, it will print a message indicating that the book already exists.
        """
        
        book_data = [vars(book) for book in books]
        with open(self.book_file, 'r') as file:
         existing_data = json.load(file)
        if existing_data in book_data:
         print("The Book already exists")
        else:
         with open(self.book_file, 'w') as file:
            json.dump(book_data, file, indent=4)

    def load_users(self):

        """
        Load the users data from the JSON file specified by the `user_file` attribute.

        Args:
        None

        Returns:
        A list of `User` objects loaded from the JSON file. If the file does not exist, an empty list is returned.

        Raises:
        FileNotFoundError: If the `user_file` does not exist.

        Note:
        This method first attempts to open and load the JSON file. If the file does not exist, an empty list is returned.
        """
        
        try:
            with open(self.user_file, 'r') as file:
                user_data = json.load(file)
            users = [User(**data) for data in user_data]
        except FileNotFoundError:
            users = []
        return users

    def save_users(self, users):

        """
        Save the provided list of users to the JSON file specified by the `user_file` attribute.

        Args:
        users (list): A list of `User` objects to be saved to the JSON file.

        Returns:
        None

        Raises:
        FileNotFoundError: If the `user_file` does not exist.

        Note:
        This method first checks if the `user_file` already contains data. If it does, it will print a message indicating that the user already exists.
        """
        
        user_data = [vars(user) for user in users]
        with open(self.user_file, 'w') as file:
            json.dump(user_data, file, indent=4)

    def load_checkouts(self):

        """
        Load the checkouts data from the JSON file specified by the `checkout_file` attribute.

        Args:
        None

        Returns:
        A list of `Checkout` objects loaded from the JSON file. If the file does not exist, an empty list is returned.

        Raises:
        FileNotFoundError: If the `checkout_file` does not exist.
        json.JSONDecodeError: If the JSON data in the file is invalid.

        Note:
        This method first attempts to open and load the JSON file. If the file does not exist, an empty list is returned.
        """
        
        try:
            with open(self.checkout_file, 'r') as file:
                checkout_data = json.load(file)
            checkouts = []
            for data in checkout_data:
                user = User(**data['user'])
                book = Book(**data['book'])
                checkout_date = datetime.fromisoformat(data['checkout_date'])
                checkin_date = data['checkin_date']
                checkin_date = datetime.fromisoformat(checkin_date) if checkin_date else None
                checkout = Checkout(user, book)
                checkout.checkout_date = checkout_date
                checkout.checkin_date = checkin_date
                checkouts.append(checkout)
            return checkouts
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_checkouts(self, checkouts):

        """
        Save the provided list of checkouts to the JSON file specified by the `checkout_file` attribute.

        Args:
        checkouts (list): A list of `Checkout` objects to be saved to the JSON file.

        Returns:
        None

        Raises:
        FileNotFoundError: If the `checkout_file` does not exist.
        json.JSONDecodeError: If the JSON data in the file is invalid.

        Note:
        This method first checks if the `checkout_file` already contains data. If it does, it will print a message indicating that the checkout already exists.
        """
        
        checkout_data = []
        for checkout in checkouts:
            data = {
                'user': vars(checkout.user),
                'book': vars(checkout.book),
                'checkout_date': checkout.checkout_date.isoformat(),
                'checkin_date': checkout.checkin_date.isoformat() if checkout.checkin_date else None
            }
            checkout_data.append(data)

        with open(self.checkout_file, 'w') as file:
            json.dump(checkout_data, file, indent=4)