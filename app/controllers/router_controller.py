from flask import Blueprint, jsonify, request
from app.services.manager_service import ManagerService

router_bp = Blueprint('router', __name__, url_prefix='/router')

manager_service = ManagerService()


'''@router_bp.route('/', methods=['GET'])
def get_all_routes():
    routers = router_service.get_all_routers()
    routers_dict = [router.to_dict() for router in routers]
    return jsonify({'routers': routers_dict})'''


@router_bp.route('/access/routers', methods=['POST'])
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
