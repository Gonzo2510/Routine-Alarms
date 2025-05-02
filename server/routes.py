from flask import Blueprint, jsonify, request
from models import db, Routine 

api = Blueprint('api', __name__)

api.route('/routines', methods=['POST'])
def create_routine():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Bad Request', 'message': 'Name is required'}), 400
    
    new_routine = Routine(name=data['name'])
    db.session.add(new_routine)
    db.session.commit()

    return jsonify({'message': 'Routine created successfully', 'routine': new_routine.name}), 201

api.route('/routines', methods=['GET'])
def get_routines():
    routines = Routine.query.all()
    routine_list = [{'id': routine.id, 'name': routine.name, 'is_active': routine.is_active} for routine in routines], 200
    return jsonify(routine_list), 200
