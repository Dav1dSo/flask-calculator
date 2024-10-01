from typing import Dict
from src.calculators.calculator_3 import Calculator_3
from src.drivers.numpy_handler import HandleNumpy

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest({"numbers": [1,2,3,4,5]})
    calculate_3 = Calculator_3(HandleNumpy())
    
    response = calculate_3.calculate(mock_request)
    
    
    