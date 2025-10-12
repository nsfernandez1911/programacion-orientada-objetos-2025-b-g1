import math
from figura import FiguraGeometrica

class Circulo(FiguraGeometrica):
    def __init__(self, radio: float, color: str) -> None:
        super().__init__(color)
        if radio <= 0:
            raise ValueError("El radio debe ser mayor que 0")
        self.__radio = float(radio)

    def area(self) -> float:
        return math.pi * (self.__radio ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.__radio
