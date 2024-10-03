from typing import Dict, List
from pytest import raises
from src.calculators.calculator_3 import Calculator_3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3
class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 10000000

def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1,2,3,4,5]})
    calculate_3 = Calculator_3(MockDriverHandlerError())
    
    with raises(Exception) as excinfo:
        calculate_3.calculate(mock_request)
        
    assert str(excinfo.value) == "Variancia menor que multiplicação"    
    
def test_calculate():
    mock_request = MockRequest({"numbers": [1,1,1,1, 100]})
    calculate_3 = Calculator_3(MockDriverHandler())
    
    response = calculate_3.calculate(mock_request)
        
       
    