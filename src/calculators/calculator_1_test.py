from .calculator_1 import Calculator1
from pytest import raises

class MockBody:
    def __init__(self, body: dict) -> None:
        self.json = body
        
def test_calculate():
    mockRequest = MockBody(body={'number': 15})
    calculator1 = Calculator1()
    
    response = calculator1.calculate(mockRequest)
    
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]
    
    assert response["data"]["Calculator"] == 1
    assert response["data"]["result"] == 13.79

def test_verify_body():
    mockRequest = MockBody(body={'numbe': 15})
    calculator1 = Calculator1()
    
    with raises(Exception) as excInfo:
        response = calculator1.calculate(mockRequest)
        
        assert str(excInfo.value) == 'Número não enviado!'
        
    