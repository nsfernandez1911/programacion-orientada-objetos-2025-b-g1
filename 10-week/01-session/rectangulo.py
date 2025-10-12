from figura import FiguraGeometrica

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho: float, alto: float, color: str) -> None:
        super().__init__(color)
        if ancho <= 0 or alto <= 0:
            raise ValueError("Ancho y alto deben ser mayores que 0")
        self.__ancho = float(ancho)
        self.__alto = float(alto)

    def area(self) -> float:
        return self.__ancho * self.__alto

    def perimetro(self) -> float:
        return 2 * (self.__ancho + self.__alto)
