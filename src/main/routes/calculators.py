from flask import Blueprint, request
from src.calculators.calculator_1 import Calculator_1
from src.calculators.calculator_2 import Calculator_2
from src.drivers.numpy_handler import HandleNumpy

calculators_bp = Blueprint("calculators", __name__)


@calculators_bp.post("/calculator/1")
def calculator():
    obj = Calculator_1()
    response = obj.calculate(request)

    return response, 200



def calculator2():
    numpy_handler = HandleNumpy()
    calc = Calculator_2(numpy_handler)
    response = calc.calculate(request)
    return response, 200
