# Taller: Herencia en Programación Orientada a Objetos (Python)

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema para representar a las personas que forman parte de la comunidad académica de una universidad, aplicando los conceptos de herencia en Python. El sistema incluye una clase base `Persona` y dos subclases: `Estudiante` y `Profesor`.

## 🏗️ Estructura del Proyecto

```
taller_herencia/
├── models/
│   ├── __init__.py
│   ├── persona.py      # Clase base Persona
│   ├── estudiante.py   # Clase Estudiante (hereda de Persona)
│   └── profesor.py     # Clase Profesor (hereda de Persona)
├── tests/
│   ├── __init__.py
│   └── test_models.py  # Pruebas unitarias
├── main.py             # Programa principal con demostraciones
├── .gitignore          # Archivo para ignorar archivos temporales
└── README.md           # Este archivo
```

**Nota**: Las carpetas `__pycache__/` se generan automáticamente al ejecutar el código Python y contienen archivos compilados para mejorar el rendimiento. Se pueden borrar sin problemas y se recrean automáticamente cuando sea necesario.

## 🎯 Objetivos Cumplidos

- ✅ **Herencia**: Implementación correcta de jerarquía de clases
- ✅ **Sobrescritura de métodos**: Método `mostrar_informacion()` sobrescrito en subclases
- ✅ **Polimorfismo**: Demostración con método `presentarse()`
- ✅ **Reutilización de código**: Uso de `super().__init__()`
- ✅ **Cálculos específicos**: Beca para estudiantes y prima para profesores
- ✅ **Actualización de datos**: Método para cambiar correo electrónico

## 📚 Clases Implementadas

### 1. Clase Persona (Superclase)

**Atributos:**
- `nombre` (str): Nombre de la persona
- `edad` (int): Edad en años
- `identificacion` (str): Número de identificación
- `correo_electronico` (str): Dirección de correo electrónico

**Métodos:**
- `saludar()`: Muestra un saludo personalizado
- `es_mayor_edad()`: Indica si es mayor de edad (≥18 años)
- `mostrar_informacion()`: Imprime los datos generales
- `actualizar_correo()`: Permite cambiar el correo electrónico

### 2. Clase Estudiante (Subclase de Persona)

**Atributos adicionales:**
- `carrera` (str): Carrera que estudia
- `semestre` (int): Semestre actual
- `promedio` (float): Promedio académico

**Métodos:**
- `estudiar()`: Indica que está estudiando su carrera
- `calcular_beca()`: Determina si tiene derecho a beca (promedio ≥ 4.0)
- `mostrar_informacion()`: Sobrescribe el método de Persona

### 3. Clase Profesor (Subclase de Persona)

**Atributos adicionales:**
- `asignatura` (str): Materia que enseña
- `salario` (float): Salario mensual
- `años_experiencia` (int): Años de experiencia laboral

**Métodos:**
- `dictar_clase()`: Indica que está dictando una asignatura
- `calcular_prima()`: Calcula bono del 10% del salario por cada 5 años de experiencia
- `mostrar_informacion()`: Sobrescribe el método de Persona

## 🚀 Cómo Ejecutar el Proyecto

### Requisitos
- Python 3.7 o superior
- PyPDF2 (para leer el PDF del taller)

### Instalación de dependencias
```bash
pip install PyPDF2
```

### Ejecución del programa principal
```bash
python -m main
```

### Ejecución de pruebas
```bash
python -m pytest tests/test_models.py -v
```

## 📸 Evidencias de Funcionamiento

### Captura Completa de Consola - Ejecución del Programa

```
============================================================
TALLER: HERENCIA EN PROGRAMACIÓN ORIENTADA A OBJETOS
============================================================

1. CREACIÓN DE OBJETOS
------------------------------
✓ Objetos creados exitosamente:
  - Persona: María González
  - Estudiante: Ana García
  - Profesor: Carlos Rodríguez

2. EJECUCIÓN DE MÉTODOS DE CADA CLASE
----------------------------------------

📋 MÉTODOS DE LA CLASE PERSONA:
Saludar: ¡Hola! Mi nombre es María González.
¿Es mayor de edad? True
Información:
Nombre: María González
Edad: 25 años
Identificación: 12345678
Correo: maria.gonzalez@email.com

🎓 MÉTODOS DE LA CLASE ESTUDIANTE:
Estudiar: Ana García está estudiando Ingeniería de Sistemas en el semestre 6.
Cálculo de beca: Ana García tiene derecho a beca con un promedio de 4.2
Información:
Nombre: Ana García
Edad: 20 años
Identificación: 87654321
Correo: ana.garcia@estudiante.edu
Carrera: Ingeniería de Sistemas
Semestre: 6
Promedio: 4.2

👨‍🏫 MÉTODOS DE LA CLASE PROFESOR:
Dictar clase: El profesor Carlos Rodríguez está dictando la clase de Programación Orientada a Objetos.
Cálculo de prima: El profesor Carlos Rodríguez tiene 12 años de experiencia. Prima calculada: $1,000,000.00 ($500,000.00 por cada 5 años)
Información:
Nombre: Carlos Rodríguez
Edad: 45 años
Identificación: 11223344
Correo: carlos.rodriguez@profesor.edu
Asignatura: Programación Orientada a Objetos
Salario: $5,000,000.00
Años de experiencia: 12

3. EVIDENCIA DE HERENCIA
-------------------------
🔄 Demostración de polimorfismo (método presentarse):
  1. Hola, soy María González y tengo 25 años.
  2. Soy Ana García, estudiante de Ingeniería de Sistemas en semestre 6, y tengo 20 años.
  3. Soy el profesor Carlos Rodríguez, tengo 45 años y enseño Programación Orientada a Objetos.

4. SOBRESCRITURA DE MÉTODOS
------------------------------
📝 Comparación del método mostrar_informacion():

🔹 Persona (método base):
Nombre: María González
Edad: 25 años
Identificación: 12345678
Correo: maria.gonzalez@email.com

🔹 Estudiante (método sobrescrito):
Nombre: Ana García
Edad: 20 años
Identificación: 87654321
Correo: ana.garcia@estudiante.edu
Carrera: Ingeniería de Sistemas
Semestre: 6
Promedio: 4.2

🔹 Profesor (método sobrescrito):
Nombre: Carlos Rodríguez
Edad: 45 años
Identificación: 11223344
Correo: carlos.rodriguez@profesor.edu
Asignatura: Programación Orientada a Objetos
Salario: $5,000,000.00
Años de experiencia: 12

5. CÁLCULOS DE BECA Y PRIMA
------------------------------
💰 Cálculo de beca para estudiantes:
  Ana García tiene derecho a beca con un promedio de 4.2

💵 Cálculo de prima para profesores:
  El profesor Carlos Rodríguez tiene 12 años de experiencia. Prima calculada: $1,000,000.00 ($500,000.00 por cada 5 años)

6. ACTUALIZACIÓN DEL CORREO ELECTRÓNICO
----------------------------------------
📧 Actualizando correo de la persona:
  Correo actualizado de 'maria.gonzalez@email.com' a 'maria.gonzalez.nueva@email.com'
  Nuevo correo: maria.gonzalez.nueva@email.com

📧 Actualizando correo del estudiante:
  Correo actualizado de 'ana.garcia@estudiante.edu' a 'ana.garcia.nueva@estudiante.edu'
  Nuevo correo: ana.garcia.nueva@estudiante.edu

📧 Actualizando correo del profesor:
  Correo actualizado de 'carlos.rodriguez@profesor.edu' a 'carlos.rodriguez.nuevo@profesor.edu'
  Nuevo correo: carlos.rodriguez.nuevo@profesor.edu

7. RESUMEN FINAL
---------------
✅ Herencia implementada correctamente
✅ Sobrescritura de métodos funcionando
✅ Cálculos de beca y prima implementados
✅ Actualización de correo electrónico funcionando
✅ Polimorfismo demostrado

============================================================
TALLER COMPLETADO EXITOSAMENTE
============================================================
```

## 🧪 Pruebas Unitarias

El proyecto incluye pruebas unitarias que verifican:

- ✅ Creación correcta de objetos
- ✅ Funcionamiento de métodos básicos
- ✅ Cálculo de becas para estudiantes
- ✅ Cálculo de primas para profesores
- ✅ Actualización de correo electrónico
- ✅ Sobrescritura de métodos

## 📊 Resultados de las Pruebas

```
Ejecutando pruebas del proyecto de herencia...
==================================================
✓ test_persona_basica: PASÓ
✓ test_estudiante_presentacion: PASÓ
✓ test_profesor_presentacion: PASÓ
✓ test_metodos_unicos: PASÓ
✓ test_calculo_beca: PASÓ
✓ test_calculo_prima: PASÓ
✓ test_actualizar_correo: PASÓ
✓ test_sobrescritura_metodos: PASÓ
==================================================
🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE!
El proyecto de herencia funciona correctamente.
```

## 🎓 Conceptos de POO Demostrados

1. **Herencia**: Las clases `Estudiante` y `Profesor` heredan de `Persona`
2. **Encapsulación**: Atributos privados y métodos públicos
3. **Polimorfismo**: Mismo método (`presentarse()`) con diferentes implementaciones
4. **Sobrescritura de métodos**: `mostrar_informacion()` personalizado en cada subclase
5. **Reutilización de código**: Uso de `super()` para llamar métodos de la clase padre

## 📋 Criterios de Evaluación - Cumplimiento

Según los criterios de evaluación del taller, este proyecto cumple con:

### ✅ Implementación correcta del concepto de herencia
- Las clases `Estudiante` y `Profesor` heredan correctamente de `Persona`
- Uso apropiado de `super().__init__()` para inicializar la clase padre
- Reutilización de código mediante herencia

### ✅ Uso adecuado de atributos y métodos en cada clase
- **Persona**: 4 atributos (nombre, edad, identificación, correo) y 4 métodos
- **Estudiante**: 3 atributos adicionales (carrera, semestre, promedio) y 3 métodos
- **Profesor**: 3 atributos adicionales (asignatura, salario, años_experiencia) y 3 métodos

### ✅ Sobrescritura de métodos en las subclases
- Método `mostrar_informacion()` sobrescrito en `Estudiante` y `Profesor`
- Cada subclase incluye información específica además de la información base
- Demostración clara de la diferencia entre método base y sobrescrito

### ✅ Presentación clara de las evidencias de funcionamiento
- Captura completa de consola con toda la ejecución del programa
- Evidencias organizadas por secciones según los requisitos del taller
- Resultados de pruebas unitarias que verifican toda la funcionalidad

## 📝 Conclusión

El proyecto cumple exitosamente con **TODOS** los requisitos del taller de herencia en Python, demostrando:

- ✅ **Implementación correcta del concepto de herencia**
- ✅ **Uso adecuado de atributos y métodos en cada clase**
- ✅ **Sobrescritura de métodos en las subclases**
- ✅ **Funcionalidades específicas como cálculo de becas y primas**
- ✅ **Actualización de datos mediante métodos apropiados**
- ✅ **Presentación clara de las evidencias de funcionamiento**

El código está bien estructurado, documentado y probado, cumpliendo con las mejores prácticas de programación orientada a objetos en Python y **todos los criterios de evaluación del taller**.