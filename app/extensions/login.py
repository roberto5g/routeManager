from flask import redirect, url_for
from flask_login import LoginManager


class CustomLoginManager(LoginManager):
    def unauthorized(self):
        return redirect(url_for('login.login'))


login_manager = CustomLoginManager()
login_manager.login_view = 'login'


def init_app(app):
    login_manager.init_app(app)
