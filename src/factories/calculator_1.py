
from src.calculators.calculator_1 import Calculator_1
from src.drivers.numpy_handler import HandleNumpy

def calculator_1_factory():
    numpy = HandleNumpy()
    calc = Calculator_1(numpy)
    return calc