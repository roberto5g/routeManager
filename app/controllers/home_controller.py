from flask import Blueprint, render_template
from flask_login import login_required


app_bp = Blueprint('app', __name__, url_prefix='/app')


@app_bp.route('/', methods=['GET'])
@login_required
def home():
    return render_template('index.html')


@app_bp.route('/gerenciar/ip')
@login_required
def route_manager():
    return render_template('ips.html')


@app_bp.route('/gerenciar/usuarios')
@login_required
def user_manager():
    return render_template('usuarios.html')


@app_bp.route('/gerenciar/logs')
@login_required
def log_manager():
    return render_template('logs.html')

