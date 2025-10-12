from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, color: str) -> None:
        if not isinstance(color, str) or not color.strip():
            raise ValueError("El color debe ser una cadena no vacía")
        self._color = color.strip()

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimetro(self) -> float:
        pass

    def descripcion(self) -> str:
        return f"Figura de color {self._color}"
