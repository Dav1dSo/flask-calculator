from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.DriverHandlerInterface import DriverHandlerInterface

class Calculator_2:
    def __init__(self, drive_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = drive_handler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json 
        input_data = self.__validate_body(body)
        calculator_number = self.__process_data(input_data)

        format_response = self.__format_response(calculator_number)
        
        return format_response
        
    def __validate_body(self, body: Dict) -> List[float]: # type: ignore 
        if "Numbers" not in body:
            raise Exception("Campo numbers não enviado!")
            
        input_data = body["Numbers"]
        return input_data
    
    
    def __process_data(self, input_data: List[float]) -> float:
        first_process = [(num * 11) ** 0.95 for num in input_data]
        
        result = self.__driver_handler.standart_derivation(first_process)
        
        result = 1/result
        
        return result
        
    def __format_response(self, calculator_number: float) -> Dict:
        return {"data": {"Calculator": 2, "result": round(calculator_number, 2)}}
        
    