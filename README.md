# Library Management System

This is a command-line application for managing a library's books, users, and book checkout/checkin operations. The application is built using Python and follows an object-oriented design approach.

## Features

* **Book Management**:
  * Add, update, delete, list, and search books
  * Search books by title, author, or ISBN
  * Track book availability

* **User Management**:
  * Add, update, delete, list, and search users
  * Search users by name or user ID

* **Checkout Management**:
  * Check out a book for a user
  * Check in a book for a user
  * List all current checkouts
  * Retrieve checkout/checkin history for a user
  * Retrieve current checkouts for a user

* **Storage**:
  * Persistent storage of books, users, and checkouts using JSON files
  * Automatic loading and saving of data

* **Error Handling and Input Validation**:
  * Comprehensive error handling and input validation throughout the application

## Project Structure

```
library-management-system/
├── book.py
├── check.py
│── books.json
│── checkouts.json
│── users.json
├── main.py
├── models.py
├── storage.py
└── user.py
```

* book.py: Manages operations related to books (add, update, delete, list, search).
* check.py: Manages operations related to checking out and checking in books, as well as retrieving checkout history and current checkouts.
* main.py: Entry point of the application, containing the main menu and flow control.
* models.py: Defines the Book, User, and Checkout classes.
* storage.py: Handles persistent storage and retrieval of data using JSON files.
* user.py: Manages operations related to users (add, update, delete, list, search).

## Getting Started

### Prerequisites

* Python 3.x

### Installation

1. Clone the repository:

```
git clone https://github.com/your-username/library-management-system.git
```

2. Navigate to the project directory:

```
cd library-management-system
```

3. Run the application:
   
```
python main.py
```

# Application Flow

1. The application starts by displaying the main menu with options for Book Management, User Management, Checkout Management, and Exit.

2. Depending on the user's choice, the corresponding management menu is displayed.

3. In each management menu, users can perform various operations like adding, updating, deleting, listing, and searching for books or users.

4. In the Checkout Management menu, users can check out or check in books, list all current checkouts, and retrieve checkout/checkin history or current checkouts for a specific user.

5. The application utilizes the `Storage` class to persistently store and retrieve data from JSON files located in the `data/` directory.

# Storage Mechanism

The application uses JSON files to store data persistently. The `Storage` class handles the loading and saving of data to and from these JSON files.

* `books.json`: Stores book data (title, author, ISBN, availability status).
* `users.json`: Stores user data (name, user ID).
* `checkouts.json`: Stores checkout data (user, book, checkout date, checkin date).

When the application starts, the `Storage` class loads the existing data from the JSON files. Any changes made during the application's runtime (e.g., adding a book, updating a user, checking out a book) are automatically saved back to the corresponding JSON file.

# Error Handling and Input Validation

The application implements comprehensive error handling and input validation throughout its codebase. Whenever an invalid input or an exceptional condition occurs, appropriate error messages are displayed to the user, preventing unexpected behavior or crashes.

For example, when adding a new book, the application checks if a book with the same ISBN already exists in the system and raises a `ValueError` if it does. Similarly, when attempting to check out a book, the application ensures that the book is available and that the specified user exists.

# Scalability and Extensibility

The modular design of the application, with clear separation of concerns, makes it easy to extend and scale the system in the future.

* **Adding New Features**: New features, such as due dates for books, late fees, or book categories, can be added by creating new classes or modifying existing ones without affecting the core functionality.

* **Changing Storage Mechanism**: The storage mechanism can be easily changed by modifying the `Storage` class. For example, instead of using JSON files, the application could be adapted to use a database for data storage.

* **Adding New Item Types**: The application can be extended to manage other types of items (e.g., magazines, DVDs) by creating new classes that inherit from a base class and implementing the necessary functionality in the respective manager classes.




