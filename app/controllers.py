from flask import Blueprint, request, jsonify
from .services import JSONProcessingService

api_bp = Blueprint('api', __name__)

@api_bp.route('/process-json', methods=['GET', 'POST'])
def process_json():
    json_data = request.json
    service = JSONProcessingService()
    processed_data = service.process(json_data)
    return jsonify(processed_data)
