from .calculator_2 import Calculator_2
from drivers.numpy_handler import HandleNumpy
from drivers.interfaces.DriverHandlerInterface import DriverHandlerInterface

class MockBody:
    def __init__(self, body: dict) -> None:
        self.json = body


class MockdriverHandler(DriverHandlerInterface):
    def standart_derivation(self, numbers: list[float]) -> float:
        return 3


def test_calculate_integration():
    mockRequest = MockBody({"Numbers": [2.12, 4.62, 1.32]})

    driver = HandleNumpy()
    calculator2 = Calculator_2(driver)
    calculator2.calculate(mockRequest)
    formated_response = calculator2.calculate(mockRequest)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 2, "result": 0.08}}


def test_calculate_unit():
    mockRequest = MockBody({"Numbers": [2.12, 4.62, 1.32]})

    driver = MockdriverHandler()
    calculator2 = Calculator_2(driver)
    calculator2.calculate(mockRequest)
    formated_response = calculator2.calculate(mockRequest)

    assert isinstance(formated_response, dict)
    assert formated_response == {"data": {"Calculator": 2, "result": 0.33}}
