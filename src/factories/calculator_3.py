from src.drivers.numpy_handler import HandleNumpy
from src.calculators.calculator_3 import Calculator_3

def calculator_3_factory():
    numpy_handler = HandleNumpy()
    calc = Calculator_3(HandleNumpy)
    
    return calc