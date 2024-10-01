import numpy as np
from typing import List
from .interfaces.DriverHandlerInterface import DriverHandlerInterface

class HandleNumpy(DriverHandlerInterface):
    
    def __init__(self) -> None:
        self.__np = np 
    
    def standart_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers) 

    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)