# models.py

import datetime

class Book:

    """
    A class representing a book with its title, author, ISBN, and availability.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
        available (bool): A flag indicating whether the book is available for checkout.

    Methods:
        __init__(self, title, author, isbn, available): Initializes a new Book object.
        __repr__(self): Returns a string representation of the Book object.
    """

    def __init__(self, title, author, isbn, available):

        """
        Initializes a new Book object with the given title, author, ISBN, and availability.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            available (bool): A flag indicating whether the book is available for checkout.
        """

        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available  # Add a flag to track availability

    def __repr__(self):

        """
        Returns a string representation of the Book object.

        Returns:
            str: A string representation of the Book object in the format "Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}',available= '{self.available}')".
        """

        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}',available= '{self.available}')"

class User:

    """
    A class representing a user with a name and a unique user ID.

    Attributes:
        name (str): The name of the user.
        user_id (str): A unique identifier for the user.

    Methods:
        __init__(self, name, user_id): Initializes a new User object.
        __repr__(self): Returns a string representation of the User object.
    """

    def __init__(self, name, user_id):

        """
        Initializes a new User object with the given name and user ID.

        Args:
            name (str): The name of the user.
            user_id (str): A unique identifier for the user.
        """

        self.name = name
        self.user_id = user_id

    def __repr__(self):

        """
        Returns a string representation of the User object.

        Returns:
            str: A string representation of the User object in the format "User(name='{self.name}', user_id='{self.user_id}')".
        """

        return f"User(name='{self.name}', user_id='{self.user_id}')"

class Checkout:

    """
    A class representing a book checkout.

    Attributes:
        user (User): The user who checked out the book.
        book (Book): The book that was checked out.
        checkout_date (datetime.datetime): The date and time when the book was checked out.
        checkin_date (datetime.datetime | None): The date and time when the book was checked in, 
        or None if the book has not been checked in yet.

    Methods:
        __init__(self, user, book): Initializes a new Checkout object with the given user and book.
        __repr__(self): Returns a string representation of the Checkout object.
    """

    def __init__(self, user, book):

        """
        Initializes a new Checkout object with the given user and book.

        Args:
            user (User): The user who checked out the book.
            book (Book): The book that was checked out.

        Attributes:
            self.user (User): The user who checked out the book.
            self.book (Book): The book that was checked out.
            self.checkout_date (datetime.datetime): The date and time when the book was checked out.
            self.checkin_date (datetime.datetime | None): The date and time when the book was checked in, 
            or None if the book has not been checked in yet.
        """

        self.user = user
        self.book = book
        self.checkout_date = datetime.datetime.now()
        self.checkin_date = None

    def __repr__(self):
        return f"Checkout(user='{self.user}', book='{self.book}')"