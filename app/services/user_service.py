from app.repositories.user_repository import UserRepository
from flask_login import current_user


class UserService:

    def __init__(self):
        self.user_repository = UserRepository()

    def get_all_users(self):
        users_response = self.user_repository.get_all()
        users_dict = [user.to_dict() for user in users_response]
        return users_dict

    def get_user(self, user_id):
        return self.user_repository.get_by_id(user_id)

    def get_user_login(self, login):
        return self.user_repository.get_by_login(login)

    def create_user(self, login, password):
        existing_user = self.get_user_login(login)
        if existing_user:
            return False
        return self.user_repository.create(login, password)

    def update_user(self, user_id, login, password):
        return self.user_repository.update(user_id, login, password)

    def delete_user(self, user_id):
        return self.user_repository.delete(user_id)

    @staticmethod
    def logged_user():
        return current_user.login


