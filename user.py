# user.py
from models import User
from storage import Storage

class UserManager:
    def __init__(self, storage):
        self.storage = storage
        self.users = self.storage.load_users()

    def add_user(self, user):
        existing_user = self.get_user_by_id(user.user_id)
        if existing_user:
            return print("The user id already exists, Try with different id")
        else:
            self.users.append(user)
            self.storage.save_users(self.users)
            return print("User added successfully")

    def update_user(self, user_id, name=None):
        user = self.get_user_by_id(user_id)
        if user:
            if name:
                user.name = name
            self.storage.save_users(self.users)

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.users.remove(user)
            self.storage.save_users(self.users)

    def list_users(self):
        return self.users

    def search_users(self, name=None, user_id=None):
        results = []
        for user in self.users:
            if (name and name.lower() in user.name.lower()) or \
               (user_id and user_id == user.user_id):
                results.append(user)
        return results

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None