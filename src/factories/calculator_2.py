
from src.calculators.calculator_2 import Calculator_2
from src.drivers.numpy_handler import HandleNumpy

def calculator_2_factory():
    numpy = HandleNumpy()
    calc = Calculator_2(numpy)
    return calc