from flask import Blueprint, render_template
from flask_login import login_required
from app.services.router_service import RouterService
from app.services.user_service import UserService
from app.services.log_service import LogService

router_service = RouterService()
user_service = UserService()
log_service = LogService()

app_bp = Blueprint('app', __name__, url_prefix='/app')


@app_bp.route('/', methods=['GET'])
@login_required
def home():
    return render_template('index.html')


@app_bp.route('/gerenciar/ip')
@login_required
def route_manager():
    routers = router_service.get_all_routers()
    return render_template('ips.html', routers=routers)


@app_bp.route('/gerenciar/usuarios')
@login_required
def user_manager():
    users = user_service.get_all_users()
    return render_template('usuarios.html', users=users)


@app_bp.route('/gerenciar/logs')
@login_required
def log_manager():
    logs = log_service.get_all_logs()
    return render_template('logs.html', logs=logs)

