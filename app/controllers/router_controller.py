from flask import Blueprint, jsonify, request, redirect, url_for
from flask_login import login_required
from app.services.manager_service import ManagerService
from app.services.router_service import RouterService

router_bp = Blueprint('router', __name__, url_prefix='/router')

manager_service = ManagerService()
router_service = RouterService()


@router_bp.route('/access/routers', methods=['POST'])
@login_required
def access_routers():

    dist = {
        "username": request.form.get('username'),
        "password": request.form.get('password'),
        "command": request.form.get('command'),
        "ip_address": request.form.get('ip_address'),
        "list_address": request.form.get('list_address'),
    }

    manager_service.process_router_data(dist)

    return jsonify({'message': 'Data processed successfully'})


@router_bp.route('/create/router', methods=['POST'])
@login_required
def create_router():
    ip_address = request.form.get('ip_address')
    router_service.create_router(ip_address)
    return redirect(url_for('app.route_manager'))


@router_bp.route('/delete/router', methods=['POST'])
@login_required
def delete_router():
    ip_address = request.form.get('ip_address')
    router_service.delete_router(ip_address)
    return redirect(url_for('app.route_manager'))

