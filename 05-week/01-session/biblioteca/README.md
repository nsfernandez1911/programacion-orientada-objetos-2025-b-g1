# Biblioteca Digital: Préstamos y Penalizaciones

## Cómo Ejecutar

```bash
python app.py
```

## Comandos de Ejemplo

### Crear Usuario
```
Opción: 3
Nombre: Ana López
Documento: 98765432
✓ Usuario creado: Ana López (Doc: 98765432)
```

### Realizar Préstamo
```
Opción: 4
Seleccionar usuario: 1
Seleccionar material: 1
✓ Préstamo creado exitosamente!
  Usuario: Juan Pérez
  Material: El Quijote
  Fecha límite: 2025-09-20
  Días préstamo: 14
```

### Simular Vencimiento y Ver Penalización
```
Opción: 8
Seleccionar préstamo: 1
Días de atraso: 5
✅ Penalización: $1500

Opción: 7 (Ver vencidos)
=== PRÉSTAMOS VENCIDOS ===
• Juan Pérez - El Quijote
  Días atraso: 5
  Penalización: $1500
```

## Cómo se Evidencian los 4 Pilares

### 1. ABSTRACCIÓN
**Archivo:** `domain/items.py`
```python
class Item(ABC):
    @abstractmethod
    def loan_days(self) -> int:
        pass
    
    @abstractmethod
    def penalty_per_day(self) -> int:
        pass
```

### 2. HERENCIA
**Archivo:** `domain/items.py`
```python
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
```

### 3. POLIMORFISMO
**Archivo:** `domain/loan.py`
```python
# Mismo código funciona para Book y Magazine
def __init__(self, user, item):
    self.due_date = self.loan_date + timedelta(days=item.loan_days())

def calculate_penalty(self):
    return max(0, self.days_overdue) * self.item.penalty_per_day()
```

### 4. ENCAPSULACIÓN
**Archivo:** `domain/items.py` y `domain/user.py`
```python
# Stock protegido con validación
class Item(ABC):
    def __init__(self, titulo, stock=1):
        self._stock = stock
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter 
    def stock(self, value):
        if value < 0:
            raise ValueError("Stock no puede ser negativo")
        self._stock = value

# Document_id protegido
class User:
    def __init__(self, nombre, document_id):
        self._document_id = document_id
    
    @property
    def document_id(self):
        return self._document_id
```