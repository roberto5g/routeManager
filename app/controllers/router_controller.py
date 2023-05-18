from flask import Blueprint, jsonify, request
from app.services.router_service import RouterService

router_bp = Blueprint('router', __name__, url_prefix='/routes')

router_service = RouterService()


@router_bp.route('/', methods=['GET'])
def get_all_routes():
    routes = router_service.get_all_routers()

    return jsonify(routes)

