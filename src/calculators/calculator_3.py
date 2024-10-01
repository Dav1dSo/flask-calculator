from src.drivers.interfaces.DriverHandlerInterface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List

class Calculator_3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.driver_handler = driver_handler
        
    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        
        self.__verify_results(variance=variance, multiplication=multiplication)
    
        return self.__format_response(multiplication)
    
    def __validate_body(self, body: Dict) -> List[float]:  # type: ignore
        if "numbers" not in body:
            raise Exception("Campo numbers não enviado!")
            
        input_data = body["numbers"]
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        if not numbers:
            return 0

        mean = sum(numbers) / len(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplicador = 1
        
        for num in numbers:
            multiplicador *= num
        
        return multiplicador
    
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception("Variancia menor que multiplicação")
        
    def __format_response(self, calculator_number: float) -> Dict:
        return {"data": {"Calculator": 3, "value": calculator_number, "success": True}}
