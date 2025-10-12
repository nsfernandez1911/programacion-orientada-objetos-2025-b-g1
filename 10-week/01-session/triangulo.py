import math
from figura import FiguraGeometrica

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1: float, lado2: float, lado3: float, color: str) -> None:
        super().__init__(color)
        if min(lado1, lado2, lado3) <= 0:
            raise ValueError("Los lados deben ser mayores que 0")
        if not (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1):
            raise ValueError("No cumple desigualdad triangular")
        self.__lado1 = float(lado1)
        self.__lado2 = float(lado2)
        self.__lado3 = float(lado3)

    def perimetro(self) -> float:
        return self.__lado1 + self.__lado2 + self.__lado3

    def area(self) -> float:
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3))


