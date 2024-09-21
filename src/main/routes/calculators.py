from flask import Blueprint, jsonify, request

calculators_bp = Blueprint('calculators', __name__)

@calculators_bp.get("/calculator")
def calculator():
    return {'msg': 'Deu bom!'}
