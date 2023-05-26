from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.services.user_service import UserService
from app.extensions.login import login_manager

user_service = UserService()

login_bp = Blueprint('login', __name__, url_prefix='/login')


@login_manager.user_loader
def load_user(user_id):
    return user_service.get_user(int(user_id))


@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('app.home'))

    if request.method == 'POST':
        user_login = request.form.get('login')
        user_password = request.form.get('password')
        print(user_login)
        print(user_password)

        user = user_service.get_user_login(user_login)
        if user and user.verify_password(user_password):
            login_user(user)
            return redirect(url_for('app.home'))
        else:
            flash('Credenciais inválidas.', 'error')

    return render_template('login.html')


@login_bp.route('/logout', methods=["POST"])
def logout():
    print("LOOOOO")
    logout_user()
    return redirect(url_for('login.login'))
