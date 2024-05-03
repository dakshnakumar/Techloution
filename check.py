# check.py

import datetime
from models import Checkout
from storage import Storage

class CheckoutManager:
    def __init__(self, storage,book_manager):
        self.storage = storage
        self.book_manager = book_manager
        self.checkouts = self.storage.load_checkouts()

    def checkout_book(self, user, book):
        if book.available == False:
            print("Book is not available")
        else :
            checkout = Checkout(user, book)
            self.checkouts.append(checkout)
            self.book_manager.update_book_availability(book, False)  # Mark the book as unavailable
            self.storage.save_checkouts(self.checkouts)


    def checkin_book(self, user, book):
        checkout = self.get_checkout(user, book)
        if checkout:
            checkout.checkin_date = datetime.datetime.now()
            self.book_manager.update_book_availability(book, True)
            self.storage.save_checkouts(self.checkouts)

    def list_checkouts(self):
        return self.checkouts

    def get_checkout(self, user, book):
        for checkout in self.checkouts:
            if checkout.user == user and checkout.book == book:
                return checkout
        return None
    
    def get_user_history(self, user):
        """Get the checkout and checkin history for a user."""
        history = []
        for checkout in self.checkouts:
            if checkout.user == user:
                history.append(checkout)
        return history

    def get_current_checkouts(self, user):
        """Get the current checkouts for a user."""
        current_checkouts = []
        for checkout in self.checkouts:
            if checkout.user == user and checkout.checkin_date is None:
                current_checkouts.append(checkout)
        return current_checkouts