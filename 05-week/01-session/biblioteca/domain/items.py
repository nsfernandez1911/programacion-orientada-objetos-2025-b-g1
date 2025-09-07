from abc import ABC, abstractmethod

class Item(ABC):
    
    def __init__(self, titulo, stock=1):
        self.titulo = titulo
        self._stock = stock  
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter 
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock no puede ser negativo")
        self._stock = value
    
    @abstractmethod
    def loan_days(self) -> int:
        pass
    
    @abstractmethod
    def penalty_per_day(self) -> int:
        pass

class Book(Item):
    
    def loan_days(self) -> int:
        return 14
    
    def penalty_per_day(self) -> int:
        return 300

class Magazine(Item):
    
    def loan_days(self) -> int:
        return 7
    
    def penalty_per_day(self) -> int:
        return 200