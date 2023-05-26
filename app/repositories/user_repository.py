from app.models.user import User
from app.extensions.database import db


class UserRepository:

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_by_login(login):
        return User.query.filter_by(login=login).first()

    @staticmethod
    def create(login, password):
        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, user_id, login, password):
        user = self.get_by_id(user_id)
        user.login = login
        user.password = password
        db.session.commit()
        return user

    def delete(self, user_id):
        user = self.get_by_id(user_id)
        db.session.delete(user)
        db.session.commit()
