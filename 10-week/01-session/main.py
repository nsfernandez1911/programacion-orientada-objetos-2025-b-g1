from rectangulo import Rectangulo
from circulo import Circulo
from triangulo import Triangulo

def mostrar_figura(figura):
    """Muestra la descripción, el área y el perímetro de una figura geométrica."""
    print(figura.descripcion())
    print(f"Área: {round(figura.area(), 2)}")
    print(f"Perímetro: {round(figura.perimetro(), 2)}")
    print("-" * 30)


def main():
    """Programa principal para probar las clases de figuras geométricas."""
    print("=== FIGURAS GEOMÉTRICAS ===\n")


    # Crear figuras
    rect = Rectangulo(5, 3, "rojo")
    circ = Circulo(4, "azul")
    tri = Triangulo(3, 4, 5, "verde")


    # Mostrar resultados
    mostrar_figura(rect)
    mostrar_figura(circ)
    mostrar_figura(tri)


if __name__ == "__main__":
    main()
