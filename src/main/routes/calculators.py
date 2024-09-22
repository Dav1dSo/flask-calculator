from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calculators_bp = Blueprint('calculators', __name__)

@calculators_bp.post("/calculator")
def calculator():
    obj = Calculator1()
    
    obj.calculate(request)
    
    return {'msg': 'Deu bom!'}
