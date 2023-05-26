from flask import Blueprint, request, redirect, url_for
from flask_login import login_required
from app.services.user_service import UserService

user_bp = Blueprint('user', __name__, url_prefix='/user')

user_service = UserService()


@user_bp.route('/create/user', methods=['POST'])
@login_required
def create_user():
    login = request.form.get('login')
    password = request.form.get('user_password')
    user_service.create_user(login, password)
    return redirect(url_for('app.user_manager'))


@user_bp.route('/delete/user', methods=['POST'])
@login_required
def delete_user():
    user = request.form.get('user')
    user_service.delete_user(user)
    return redirect(url_for('app.user_manager'))

