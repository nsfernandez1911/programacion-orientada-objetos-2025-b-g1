import pytest
from models.estudiante import Estudiante
from models.profesor import Profesor
from models.persona import Persona


def test_persona_basica():
    persona = Persona("María", 25, "12345678", "maria@email.com")
    assert persona.nombre == "María"
    assert persona.edad == 25
    assert persona.es_mayor_edad() == True
    assert "María" in persona.saludar()

def test_estudiante_presentacion():
    estudiante = Estudiante("Ana", 20, "87654321", "ana@estudiante.edu", "Ingeniería", 6, 4.2)
    assert "estudiante de Ingeniería" in estudiante.presentarse()

def test_profesor_presentacion():
    profesor = Profesor("Carlos", 45, "11223344", "carlos@profesor.edu", "Matemáticas", 5000000, 10)
    assert "enseño Matemáticas" in profesor.presentarse()

def test_metodos_unicos():
    estudiante = Estudiante("Ana", 20, "87654321", "ana@estudiante.edu", "Ingeniería", 6, 4.2)
    profesor = Profesor("Carlos", 45, "11223344", "carlos@profesor.edu", "Matemáticas", 5000000, 10)

    assert "estudiando Ingeniería" in estudiante.estudiar()
    assert "enseña Matemáticas" in profesor.enseñar()

def test_calculo_beca():
    estudiante_bueno = Estudiante("Ana", 20, "87654321", "ana@estudiante.edu", "Ingeniería", 6, 4.2)
    estudiante_malo = Estudiante("Pedro", 19, "11111111", "pedro@estudiante.edu", "Medicina", 3, 3.5)
    
    assert "tiene derecho a beca" in estudiante_bueno.calcular_beca()
    assert "no tiene derecho a beca" in estudiante_malo.calcular_beca()

def test_calculo_prima():
    profesor = Profesor("Carlos", 45, "11223344", "carlos@profesor.edu", "Matemáticas", 5000000, 12)
    resultado = profesor.calcular_prima()
    assert "Prima calculada" in resultado
    assert "12 años de experiencia" in resultado

def test_actualizar_correo():
    persona = Persona("María", 25, "12345678", "maria@email.com")
    resultado = persona.actualizar_correo("maria.nueva@email.com")
    assert "actualizado" in resultado
    assert persona.correo_electronico == "maria.nueva@email.com"

def test_sobrescritura_metodos():
    estudiante = Estudiante("Ana", 20, "87654321", "ana@estudiante.edu", "Ingeniería", 6, 4.2)
    profesor = Profesor("Carlos", 45, "11223344", "carlos@profesor.edu", "Matemáticas", 5000000, 10)
    
    info_estudiante = estudiante.mostrar_informacion()
    info_profesor = profesor.mostrar_informacion()
    
    assert "Carrera: Ingeniería" in info_estudiante
    assert "Semestre: 6" in info_estudiante
    assert "Promedio: 4.2" in info_estudiante
    
    assert "Asignatura: Matemáticas" in info_profesor
    assert "Salario: $5,000,000.00" in info_profesor
    assert "Años de experiencia: 10" in info_profesor
