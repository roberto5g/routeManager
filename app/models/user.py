from flask_login import UserMixin
from app.extensions.database import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), unique=True, nullable=False)

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_authenticated():
        return True

    def get_id(self):
        return str(self.id)

    @property
    def password(self):
        raise AttributeError('A senha não pode ser acessada diretamente.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.login}>"

    def to_dict(self):
        return {
            'id': self.id,
            'login': self.login,
        }
