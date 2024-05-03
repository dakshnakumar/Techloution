# check.py

import datetime
from models import Checkout
from storage import Storage

class CheckoutManager:
    def __init__(self, storage,book_manager):

        """
        Initialize the CheckoutManager with the provided storage and book_manager.
        Loads the checkouts from the storage and sets them as an attribute.

        Args:
        storage (Storage): The storage object responsible for loading and saving checkouts.
        book_manager (BookManager): The book manager object responsible for managing book availability.

        Returns:
        None
        """
        
        self.storage = storage
        self.book_manager = book_manager
        self.checkouts = self.storage.load_checkouts()

    def checkout_book(self, user, book):

        """
        Checks out a book for a user.

        Args:
        user (User): The user who is checking out the book.
        book (Book): The book to be checked out.

        Raises:
        ValueError: If the book is not available.

        Returns:
        None

        This method first checks if the book is available. If it is, it creates a new Checkout object with the provided user and book,
        appends it to the list of checkouts, marks the book as unavailable, and saves the updated list of checkouts.
        If the book is not available, it raises a ValueError with an appropriate message.
        """
        
        if book.available == False:
            raise ValueError("Book is not available")
        else :
            checkout = Checkout(user, book)
            self.checkouts.append(checkout)
            self.book_manager.update_book_availability(book, False)  # Mark the book as unavailable
            self.storage.save_checkouts(self.checkouts)


    def checkin_book(self, user, book):

        """
        Checks in a book for a user.

        Args:
        user (User): The user who is checking in the book.
        book (Book): The book to be checked in.

        Raises:
        ValueError: If the checkout for the given user and book is not found.

        Returns:
        None

        This method first retrieves the checkout for the provided user and book. If it exists, it updates the checkin_date to the current date and time,
        marks the book as available, and saves the updated list of checkouts. If the checkout is not found, it raises a ValueError with an appropriate message.
        """
        
        checkout = self.get_checkout(user, book)
        if checkout:
            checkout.checkin_date = datetime.datetime.now()
            self.book_manager.update_book_availability(book, True)
            self.storage.save_checkouts(self.checkouts)
        else :
            raise ValueError("Checkout not found for the given user and book")

    def list_checkouts(self):

        """
        Lists all the current checkouts.

        Returns:
        A list of all the current checkouts.
        """
        
        return self.checkouts

    def get_checkout(self, user, book):

        """
        Retrieves the checkout for the provided user and book.

        Args:
        user (User): The user for whom the checkout is being searched.
        book (Book): The book for which the checkout is being searched.

        Returns:
        Checkout: The checkout object if found, otherwise None.

        This method iterates through the list of checkouts and returns the first checkout object where the user and book match.
        If no matching checkout is found, it returns None.
        """
        
        for checkout in self.checkouts:
            if checkout.user == user and checkout.book == book:
                return checkout
        return None
    
    def get_user_history(self, user):
         
        """
        Get the checkout and checkin history for a user.

        Args:
        user (User): The user for whom the history is being searched.

        Returns:
        A list of all the checkouts made by the user, including both checkout and checkin dates.
        """
         
        history = []
        for checkout in self.checkouts:
            if checkout.user == user:
                history.append(checkout)
        return history

    def get_current_checkouts(self, user):

        """
        Get the current checkouts for a user.

        Args:
        user (User): The user for whom the current checkouts are being searched.

        Returns:
        A list of all the current checkouts made by the user, where the checkin_date is None.
        """

        current_checkouts = []
        for checkout in self.checkouts:
            if checkout.user == user and checkout.checkin_date is None:
                current_checkouts.append(checkout)
        return current_checkouts