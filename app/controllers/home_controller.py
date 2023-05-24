from flask import Blueprint, render_template
from app.services.router_service import RouterService
from app.services.user_service import UserService

router_service = RouterService()
user_service = UserService()

app_bp = Blueprint('app', __name__, url_prefix='/app')


@app_bp.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app_bp.route('/gerenciar/ip')
def route_manager():
    routers = router_service.get_all_routers()
    return render_template('ips.html', routers=routers)


@app_bp.route('/gerenciar/usuarios')
def user_manager():
    users = user_service.get_all_users()
    return render_template('usuarios.html', users=users)
