from flask import request
from typing import Dict

class Calculator1:
    def calculate(self, request: request) -> Dict:
        body = request.json
        input_data = self.__verify_body(body)
        first_process = self.__first_process(input_data)
        print(first_process)
        print(input_data)
        
    def __verify_body(self, body: request) -> float:
        if "number" not in body:
            raise Exception("Número não enviado!")
        input_data = body.get("number")
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = first_part ** 0.257
        return second_part