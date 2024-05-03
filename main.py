# main.py
from book import BookManager
from user import UserManager
from check import CheckoutManager
from storage import Storage
from models import Book, User

storage = Storage('books.json', 'users.json', 'checkouts.json')

book_manager = BookManager(storage)
user_manager = UserManager(storage)
checkout_manager = CheckoutManager(storage,book_manager)


def main_menu():

    """
    Displays the main menu of the Library Management System.

    Returns:
        str: The user's choice from the main menu.
    """


    print("\nLibrary Management System")
    print("1. Book Management")
    print("2. User Management")
    print("3. Checkout Management")
    print("4. Exit")
    choice = input("Enter choice: ")
    return choice

def book_management():

    """
    This function provides a menu for managing books in the library system.

    It allows the user to perform various operations such as adding, updating, deleting, listing, and searching books.

    Args:
        None

    Returns:
        None

    """

    while True:
        print("\nBook Management")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. List Books")
        print("5. Search Books")
        print("6. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn,True)
            book_manager.add_book(book)
            # print(result)
        elif choice == '2':
            isbn = input("Enter ISBN of the book to update: ")
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")
            book_manager.update_book(isbn, title if title else None, author if author else None)
            print("Book updated.")
        elif choice == '3':
            isbn = input("Enter ISBN of the book to delete: ")
            book_manager.delete_book(isbn)
            # print("Book deleted.")
        elif choice == '4':
            books = book_manager.list_books()
            if books:
                print("Books:")
                for book in books:
                    print(book)
            else:
                print("No books found.")
        elif choice == '5':
            title = input("Enter title (leave blank for all): ")
            author = input("Enter author (leave blank for all): ")
            isbn = input("Enter ISBN (leave blank for all): ")
            books = book_manager.search_books(title if title else None, author if author else None, isbn if isbn else None)
            if books:
                print("Books:")
                for book in books:
                    print(book)
            else:
                print("No books found.")
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

def user_management():

    """
    This function provides a menu for managing users in the library system.
    
    It allows the user to perform various operations such as adding, updating, deleting, listing, and searching users.

    Args:
        None

    Returns:
        None

    """

    while True:
        print("\nUser Management")
        print("1. Add User")
        print("2. Update User")
        print("3. Delete User")
        print("4. List Users")
        print("5. Search Users")
        print("6. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user = User(name, user_id)
            user_manager.add_user(user)
            # print("User added.")
        elif choice == '2':
            user_id = input("Enter user ID of the user to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            user_manager.update_user(user_id, name if name else None)
            print("User updated.")
        elif choice == '3':
            user_id = input("Enter user ID of the user to delete: ")
            user_manager.delete_user(user_id)
            print("User deleted.")
        elif choice == '4':
            users = user_manager.list_users()
            if users:
                print("Users:")
                for user in users:
                    print(user)
            else:
                print("No users found.")
        elif choice == '5':
            name = input("Enter name (leave blank for all): ")
            user_id = input("Enter user ID (leave blank for all): ")
            users = user_manager.search_users(name if name else None, user_id if user_id else None)
            if users:
                print("Users:")
                for user in users:
                    print(user)
            else:
                print("No users found.")
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

def checkout_management():

    """
    This function provides a menu for managing checkouts in the library system.

    It allows the user to perform various operations such as checking out and checking in books.

    Args:
        None

    Returns:
        None

    """
     
    while True:
        print("\nCheckout Management")
        print("1. Checkout Book")
        print("2. Checkin Book")
        print("3. List Checkouts")
        print("4. Back to Main Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            user_id = input("Enter user ID: ")
            user = user_manager.get_user_by_id(user_id)
            if user:
                isbn = input("Enter ISBN of the book to checkout: ")
                book = book_manager.get_book_by_isbn(isbn)
                if book:
                    checkout_manager.checkout_book(user, book)
                    print("Book checked out successfully.")
                else:
                    print("Book not found.")
            else:
                print("User not found.")
        elif choice == '2':
            user_id = input("Enter user ID: ")
            user = user_manager.get_user_by_id(user_id)
            if user:
                isbn = input("Enter ISBN of the book to checkin: ")
                book = book_manager.get_book_by_isbn(isbn)
                if book:
                    checkout_manager.checkin_book(user, book)
                    print("Book checked in successfully.")
                else:
                    print("Book not found.")
            else:
                print("User not found.")
        elif choice == '3':
            checkouts = checkout_manager.list_checkouts()
            if checkouts:
                print("Checkouts:")
                for checkout in checkouts:
                    print(checkout)
            else:
                print("No checkouts found.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def main():
    
    """
    This function serves as the main entry point for the Library Management System.
    It continuously prompts the user to choose from the main menu options,
    which include Book Management, User Management, Checkout Management, and Exit.
   
    Args:
        None

    Returns:
        None

    """

    while True:
        choice = main_menu()
        if choice == '1':
            book_management()
        elif choice == '2':
            user_management()
        elif choice == '3':
            checkout_management()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()