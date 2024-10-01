from flask import Blueprint, request

from src.factories.calculator_1 import Calculator_1
from src.factories.calculator_2 import Calculator_2

calculators_bp = Blueprint("calculators", __name__)


@calculators_bp.post("/calculator/1")
def calculator():

    calc = Calculator_1()
    response = calc.calculate()
    return response, 200


@calculators_bp.post("/calculator/2")
def calculator2():
    calc = Calculator_2()
    response = calc.calculate(request)
    return response, 200
