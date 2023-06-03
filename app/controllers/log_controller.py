from flask import Blueprint, jsonify
from flask_login import login_required
from app.services.log_service import LogService

log_bp = Blueprint('log', __name__, url_prefix='/log')

log_service = LogService()


@log_bp.route('/load', methods=['GET'])
@login_required
def load_logs():

    logs = log_service.get_all_logs()

    return jsonify({'data': logs})




