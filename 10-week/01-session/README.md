# Taller de Programación Orientada a Objetos
## Jerarquía de Clases de Figuras Geométricas

### 1. Introducción
El presente trabajo desarrolla una jerarquía de clases en Python que representa diferentes figuras geométricas, aplicando los principios fundamentales de la Programación Orientada a Objetos (POO): abstracción, herencia, encapsulamiento y polimorfismo.

### 2. Estructura del Proyecto
```
jerarquia-clases/
├─ src/
│  ├─ figura.py
│  ├─ rectangulo.py
│  ├─ circulo.py
│  └─ triangulo.py
└─ README.md
```

### 3. Descripción de Clases
- **figura.py:** Clase abstracta `FiguraGeometrica`, base de las demás figuras.
- **rectangulo.py:** Clase `Rectangulo` que calcula área y perímetro de un rectángulo.
- **circulo.py:** Clase `Circulo` que calcula área y perímetro de un círculo.
- **triangulo.py:** Clase `Triangulo` que calcula área y perímetro con la fórmula de Herón.

### 4. Principios de POO Aplicados
| Principio | Aplicación |
|------------|-------------|
| Abstracción | Clase base `FiguraGeometrica` con métodos abstractos. |
| Herencia | Clases hijas derivan de la clase abstracta. |
| Encapsulamiento | Uso de atributos privados y protegidos. |
| Polimorfismo | Métodos `area()` y `perimetro()` redefinidos en cada clase. |

### 5. Ejemplo de Uso
```python
from src.rectangulo import Rectangulo
from src.circulo import Circulo
from src.triangulo import Triangulo

r = Rectangulo(3, 4, 'rojo')
print(r.descripcion(), r.area(), r.perimetro())

c = Circulo(2.5, 'azul')
print(c.descripcion(), round(c.area(), 2), round(c.perimetro(), 2))

t = Triangulo(3, 4, 5, 'verde')
print(t.descripcion(), round(t.area(), 2), t.perimetro())
```

### 6. Conclusión
El proyecto demuestra la correcta aplicación de los pilares de la POO, permitiendo un diseño modular, extensible y bien organizado de las clases.

### 7. Autor
**Autor:** Nicolás Fernández Vargas  
**Materia:** Programación Orientada a Objetos  
**Facultad:** Ingeniería de mecatronica   