from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calculators_bp = Blueprint('calculators', __name__)

@calculators_bp.post("/calculator")
def calculator():
    obj = Calculator1()
    response = obj.calculate(request)
    
    return response, 200