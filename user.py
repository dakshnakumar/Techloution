# user.py
from models import User
from storage import Storage

class UserManager:
    def __init__(self, storage):

        """
        Initialize the UserManager with a storage object.
        Loads the users from the storage and sets it as an attribute.

        Args:
        storage (Storage): An instance of the Storage class that handles user data.

        Returns:
        None
        """
        
        self.storage = storage
        self.users = self.storage.load_users()

    def add_user(self, user):

        """
        Add a new user to the UserManager.

        Args:
        user (User): An instance of the User class containing the user's information.

        Returns:
        None

        Raises:
        ValueError: If the user ID already exists in the UserManager.

        This method first checks if a user with the same ID already exists in the UserManager.
        If so, it raises a ValueError with an appropriate message. Otherwise, it appends the new user to the list of users and saves the updated list to the storage.
        """
        
        existing_user = self.get_user_by_id(user.user_id)
        if existing_user:
            return ValueError("The user id already exists, Try with different id")
        else:
            self.users.append(user)
            self.storage.save_users(self.users)
            return print("User added successfully")

    def update_user(self, user_id, name=None):

        """
        Update a user's information in the UserManager.

        Args:
        user_id (str): The unique identifier of the user to be updated.
        name (str, optional): The new name of the user. Defaults to None.

        Returns:
        None

        This method first checks if a user with the given ID exists in the UserManager.
        If so, it updates the user's name if a new name is provided. Otherwise, it does nothing.
        Finally, it saves the updated list of users to the storage.
        """
        
        user = self.get_user_by_id(user_id)
        if user:
            if name:
                user.name = name
            self.storage.save_users(self.users)

    def delete_user(self, user_id):

        """
        Delete a user from the UserManager.

        Args:
        user_id (str): The unique identifier of the user to be deleted.

        Returns:
        None

        This method first checks if a user with the given ID exists in the UserManager.
        If so, it removes the user from the list of users and saves the updated list to the storage.
        """

        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            self.storage.save_users(self.users)

    def list_users(self):
        """
        List all users in the UserManager.

        Returns:
        list: A list of all users in the UserManager.
        """
        return self.users

    def search_users(self, name=None, user_id=None):

        """
        Search for users in the UserManager based on their name or user ID.

        Args:
        name (str, optional): The name of the user to search for. Defaults to None.
        user_id (str, optional): The unique identifier of the user to search for. Defaults to None.

        Returns:
        list: A list of users that match the search criteria.

        This method iterates through all users in the UserManager and checks if the provided name or user ID matches any user in the list. If a match is found, the user is added to the results list. Finally, the method returns the list of matching users.
        """

        results = []
        for user in self.users:
            if (name and name.lower() in user.name.lower()) or \
               (user_id and user_id == user.user_id):
                results.append(user)
        return results

    def get_user_by_id(self, user_id):

        """
        Search for a user in the UserManager based on their unique ID.

        Args:
        user_id (str): The unique identifier of the user to search for.

        Returns:
        User: The user object with the matching user ID, or None if no match is found.

        This method iterates through all users in the UserManager and checks if the provided user ID matches any user in the list. If a match is found, the user object is returned. If no match is found, None is returned.
        """
        
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None