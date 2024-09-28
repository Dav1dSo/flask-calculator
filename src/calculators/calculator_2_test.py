from .calculator_2 import Calculator_2
from pytest import raises

class MockBody:
    def __init__(self, body: dict) -> None:
        self.json = body

def test_calculate():
    mockRequest = MockBody({'Numbers': [2.12, 4.62, 1.32]})
    
    calculator2 = Calculator_2()
    calculator2.calculate(mockRequest)
    formated_response = calculator2.calculate(mockRequest)
    
    assert isinstance(formated_response, dict)  
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.08}}
    
    