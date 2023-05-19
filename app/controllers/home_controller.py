from flask import Blueprint, render_template

app_bp = Blueprint('app', __name__, url_prefix='/app')


@app_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app_bp.route('/gerenciar/ip')
def gerenciar_ip():
    return render_template('ips.html')


@app_bp.route('/gerenciar/usuarios')
def gerenciar_usuarios():
    return render_template('usuarios.html')
